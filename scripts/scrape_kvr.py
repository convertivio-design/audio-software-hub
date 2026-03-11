"""
scrape_kvr.py — Scrape KVR Audio plugin database and append to data/products.json

KVR Audio is the internet's largest free plugin database (~35,000 plugins).
This script scrapes their public browse pages and appends new tools to the JSON.

Usage:
    pip install requests beautifulsoup4
    python scripts/scrape_kvr.py [--pages 50] [--categories all]

Options:
    --pages N        Number of pages per category to scrape (default: 30, ~20 items/page)
    --max N          Max total products to add (default: 3000)
    --delay N        Seconds between requests (default: 1.5)

Output:
    Appends to data/products.json (deduplicates by name)
"""

import json
import os
import re
import time
import argparse
import unicodedata
from urllib.request import urlopen, Request
from urllib.error import URLError
from html.parser import HTMLParser

OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'products.json')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# KVR category IDs → our category slugs
KVR_CATEGORIES = {
    'synths':        ('synth',     'https://www.kvraudio.com/plugins/synths/by-name/page/{}'),
    'effects':       ('effects',   'https://www.kvraudio.com/plugins/effects/by-name/page/{}'),
    'midi':          ('midi',      'https://www.kvraudio.com/plugins/midi-plugins/by-name/page/{}'),
    'instruments':   ('sampler',   'https://www.kvraudio.com/plugins/instruments/by-name/page/{}'),
    'hosts':         ('daw',       'https://www.kvraudio.com/plugins/hosts/by-name/page/{}'),
}

def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

def fetch(url: str, delay: float = 1.5) -> str:
    time.sleep(delay)
    try:
        req = Request(url, headers=HEADERS)
        with urlopen(req, timeout=15) as r:
            return r.read().decode('utf-8', errors='replace')
    except URLError as e:
        print(f"  FETCH ERROR {url}: {e}")
        return ''

class KVRPageParser(HTMLParser):
    """Extract plugin listings from a KVR browse page."""

    def __init__(self):
        super().__init__()
        self.products = []
        self._in_product_name = False
        self._in_developer = False
        self._current = {}
        self._tag_stack = []
        self._in_product_block = False
        self._product_url = ''
        self._capture_next_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # KVR product listings: div.plug-name > a
        cls = attrs.get('class', '')
        if tag == 'div' and 'plug-name' in cls:
            self._in_product_name = True
            self._current = {}
        if self._in_product_name and tag == 'a' and attrs.get('href', '').startswith('/product/'):
            href = attrs.get('href', '')
            self._current['slug_kvr'] = href.strip('/')
            self._current['url'] = 'https://www.kvraudio.com' + href
            self._capture_next_link = True
        # Developer: div.plug-dev > a
        if tag == 'div' and 'plug-dev' in cls:
            self._in_developer = True

    def handle_endtag(self, tag):
        if tag == 'div':
            self._in_product_name = False
            self._in_developer = False

    def handle_data(self, data):
        data = data.strip()
        if not data:
            return
        if self._capture_next_link:
            self._current['name'] = data
            self._capture_next_link = False
        if self._in_developer and 'developer' not in self._current:
            self._current['developer'] = data

    def error(self, message):
        pass


def parse_kvr_page(html: str) -> list:
    """Extract products from KVR HTML using regex (more reliable than HTMLParser for KVR's structure)."""
    products = []

    # KVR listing pattern: product name in <a href="/product/...">NAME</a> within plug-name div
    # Pattern for product blocks
    blocks = re.findall(
        r'<div[^>]*class="[^"]*plug-name[^"]*"[^>]*>.*?</div>',
        html, re.DOTALL
    )

    # Simpler: just extract all /product/ links with their text
    pattern = r'<a\s+href="(/product/([^/"]+)/)"[^>]*>([^<]{2,80})</a>'
    for m in re.finditer(pattern, html):
        path, kvr_slug, name = m.group(1), m.group(2), m.group(3)
        name = name.strip()
        if not name or len(name) < 2:
            continue
        # Skip navigation links
        if name.lower() in ('more', 'next', 'previous', 'kvr audio', 'home'):
            continue
        products.append({
            'name': name,
            'kvr_url': 'https://www.kvraudio.com' + path,
            'kvr_slug': kvr_slug,
        })

    # Deduplicate by name within page
    seen = set()
    unique = []
    for p in products:
        key = p['name'].lower()
        if key not in seen:
            seen.add(key)
            unique.append(p)

    return unique


def scrape_kvr(max_pages: int = 30, max_total: int = 3000, delay: float = 1.5):
    # Load existing products
    existing_products = []
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH, encoding='utf-8') as f:
            existing_products = json.load(f)

    existing_names = {p['name'].lower().strip() for p in existing_products}
    existing_slugs = {p['slug'] for p in existing_products}

    new_products = []
    total_added = 0

    for kvr_cat, (our_cat, url_template) in KVR_CATEGORIES.items():
        if total_added >= max_total:
            break

        print(f"\n[{kvr_cat.upper()}] -> category: {our_cat}")

        for page in range(1, max_pages + 1):
            if total_added >= max_total:
                break

            url = url_template.format(page)
            print(f"  Page {page}: {url}")
            html = fetch(url, delay)

            if not html:
                print(f"  Empty response, stopping category.")
                break

            # Check if we've gone past last page
            if 'No plugins found' in html or 'page not found' in html.lower():
                print(f"  No more pages.")
                break

            items = parse_kvr_page(html)
            if not items:
                print(f"  No products parsed, stopping.")
                break

            added_this_page = 0
            for item in items:
                name = item['name']
                name_key = name.lower().strip()

                if name_key in existing_names:
                    continue
                existing_names.add(name_key)

                # Generate unique slug
                base_slug = slugify(name)
                slug = base_slug
                counter = 2
                while slug in existing_slugs:
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                existing_slugs.add(slug)

                product = {
                    "id": slug,
                    "name": name,
                    "slug": slug,
                    "developer": "",
                    "categoryId": our_cat,
                    "shortDescription": f"{name} — {our_cat} plugin.",
                    "price": None,
                    "priceType": "one-time",
                    "officialUrl": item['kvr_url'],
                    "rating": 0,
                    "ratingCount": 0,
                    "os": [],
                    "formats": [],
                    "features": [],
                    "pros": [],
                    "cons": [],
                    "tags": [our_cat],
                    "isFeatured": False,
                    "isNew": False,
                    "source": "kvr",
                }
                new_products.append(product)
                added_this_page += 1
                total_added += 1

                if total_added >= max_total:
                    break

            print(f"    Added {added_this_page} new products (total new: {total_added})")

            if added_this_page == 0:
                print(f"  No new products this page, stopping category.")
                break

    # Merge and save
    all_products = existing_products + new_products
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(all_products, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*50}")
    print(f"KVR scrape complete.")
    print(f"  New products added: {total_added}")
    print(f"  Total in database:  {len(all_products)}")
    print(f"  Output: {OUT_PATH}")

    return total_added


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape KVR Audio into products.json')
    parser.add_argument('--pages', type=int, default=30, help='Pages per category (default: 30)')
    parser.add_argument('--max', type=int, default=3000, help='Max products to add (default: 3000)')
    parser.add_argument('--delay', type=float, default=1.5, help='Delay between requests in seconds (default: 1.5)')
    args = parser.parse_args()

    print(f"Scraping KVR Audio — max {args.max} products, {args.pages} pages/category, {args.delay}s delay")
    scrape_kvr(max_pages=args.pages, max_total=args.max, delay=args.delay)
