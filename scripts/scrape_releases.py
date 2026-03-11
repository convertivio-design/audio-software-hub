#!/usr/bin/env python3
"""
scripts/scrape_releases.py
Scrapes real VST / DAW / plugin RELEASE pages using Firecrawl CLI.

Pipeline:
  1. Scrape listing pages (KVR new plugins, BPB, Synthanatomy) to get article URLs
  2. Filter URLs to only individual release/article pages
  3. Scrape each page with Firecrawl for full text
  4. Extract structured product data from content
  5. Write to data/releases.json

Run every 24-48h via GitHub Actions.
"""

import sys
import os
import re
import json
import time
import random
import hashlib
import subprocess
import tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).parent.parent
RELEASES_FILE = ROOT / "data" / "releases.json"

MAX_KEEP = 30
MAX_AGE_DAYS = 14
MAX_ARTICLES_PER_SOURCE = 8  # articles to scrape per listing page

# Listing pages that contain links to individual release articles
LISTING_PAGES = [
    {
        "url": "https://www.kvraudio.com/news/",
        "name": "KVR Audio News",
        "link_pattern": r"kvraudio\.com/product/",
        "alt_pattern": r"kvraudio\.com/news/\d",
    },
    {
        "url": "https://bedroomproducersblog.com/category/free-vst-plugins/",
        "name": "BPB Free VST",
        "link_pattern": r"bedroomproducersblog\.com/20\d\d/",
    },
    {
        "url": "https://www.synthanatomy.com/",
        "name": "Synthanatomy",
        "link_pattern": r"synthanatomy\.com/20\d\d/",
    },
    {
        "url": "https://www.rekkerd.org/",
        "name": "Rekkerd",
        "link_pattern": r"rekkerd\.org/20\d\d/",
    },
    {
        "url": "https://cdm.link/",
        "name": "CDM",
        "link_pattern": r"cdm\.link/20\d\d/",
    },
]

# keyword -> categoryId
CATEGORY_MAP = {
    "daw": ["daw", "ableton", "logic pro", "fl studio", "cubase", "pro tools",
            "reaper", "bitwig", "studio one", "reason", "garageband", "digital audio workstation"],
    "synth": ["synth", "synthesizer", "eurorack", "oscillator", "modular", "wavetable",
              "fm synth", "analog synth", "virtual analog", "vco", "vca"],
    "effects": ["reverb", "delay", "compressor", "eq ", "equalizer", "distortion",
                "chorus", "flanger", "phaser", "limiter", "saturator", "effect plugin",
                "fx plugin", "mastering plugin", "audio effect"],
    "sampler": ["sampler", "sample player", "kontakt", "sample library", "drum kit",
                "sample pack", "rompler"],
    "drums": ["drum", "beat maker", "drum machine", "rhythm", "percussion", "beatbox"],
    "mastering": ["mastering", "loudness", "stem splitter", "metering", "lufs"],
    "midi": ["midi", "arpeggiator", "sequencer", "midi plugin", "midi tool", "chord"],
    "vocal": ["vocal", "pitch correction", "autotune", "harmony", "voice", "melodyne"],
    "guitar": ["guitar", "amp sim", "amplifier", "cabinet", "guitar plugin", "bass amp"],
    "utility": ["utility", "spectrum analyzer", "tuner", "meter", "router", "bus",
                "plugin host", "standalone"],
}

KNOWN_BRANDS = [
    "FabFilter", "iZotope", "Waves", "Native Instruments", "Arturia", "Roland", "Korg",
    "Moog", "Sequential", "Elektron", "Ableton", "Image-Line", "Bitwig", "PreSonus",
    "Reason Studios", "Avid", "Steinberg", "Plugin Alliance", "Softube", "UAD",
    "Universal Audio", "Eventide", "Output", "Xfer Records", "Matt Tytel",
    "Surge Synth Team", "VCV", "Cherry Audio", "U-He", "Pigments",
    "Spitfire", "EastWest", "Soundtoys", "Valhalla DSP", "Oeksound", "Slate Digital",
    "Brainworx", "IK Multimedia", "Celemony", "Antares", "D16 Group", "TAL Software",
    "Newfangled Audio", "Acustica Audio", "Tone Empire", "Baby Audio", "Devious Machines",
    "Kilohearts", "Cableguys", "Initial Audio", "Heavyocity", "ProjectSAM",
]

BRAND_PATTERN = re.compile(
    r'\b(' + '|'.join(re.escape(b) for b in KNOWN_BRANDS) + r')\b',
    re.IGNORECASE
)

# URLs to skip
JUNK_URL_PATTERNS = [
    r'/forum', r'/forums', r'/category/', r'/categories/', r'/tag/', r'/tags/',
    r'/page/', r'/author/', r'/feed/', r'/rss', r'/search', r'\?', r'#',
    r'/about', r'/contact', r'/privacy', r'/terms', r'/shop/?$', r'/store/?$',
    r'youtube\.com', r'facebook\.com', r'twitter\.com', r'instagram\.com',
]
JUNK_URL_RE = re.compile('|'.join(JUNK_URL_PATTERNS), re.IGNORECASE)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:80]


def make_id(url: str, name: str) -> str:
    return hashlib.md5(f"{url}:{name}".encode()).hexdigest()[:12]


def detect_category(text: str) -> str:
    text_lower = text.lower()
    for cat_id, keywords in CATEGORY_MAP.items():
        if any(kw in text_lower for kw in keywords):
            return cat_id
    return 'utility'


def detect_price(text: str) -> tuple:
    text_lower = text.lower()
    if any(w in text_lower for w in ['free download', 'free vst', 'free plugin', 'freeware',
                                      'open source', 'name your price', '$0', '€0', '£0']):
        return 0.0, 'free'
    price_match = re.search(r'[\$€£](\d+(?:\.\d{1,2})?)', text_lower)
    if price_match:
        return float(price_match.group(1)), 'one-time'
    if any(w in text_lower for w in ['/month', '/year', 'subscription', 'annual plan', 'per month']):
        return 9.99, 'subscription'
    return 0.0, 'paid'


def extract_developer(text: str) -> str:
    match = BRAND_PATTERN.search(text)
    if match:
        found = match.group(1)
        for brand in KNOWN_BRANDS:
            if brand.lower() == found.lower():
                return brand
        return found
    patterns = [
        r'by\s+([A-Z][A-Za-z0-9\s\-]+?)[\s,\.\-]',
        r'^([A-Z][A-Za-z0-9\-]+)\s+(?:releases?|launches?|announces?|introduces?|unveils?)',
        r'^([A-Z][A-Za-z0-9\-]+)(?:\'s)?\s+new\b',
    ]
    for pat in patterns:
        m = re.search(pat, text[:200])
        if m:
            candidate = m.group(1).strip()
            if 2 < len(candidate) < 40:
                return candidate
    return ''


def extract_product_name(title: str, text: str) -> str:
    """Extract clean product name from title."""
    name = title

    # Strip leading noise
    noise_prefixes = [
        r'^(?:free\s+)?(?:vst|vst3|au|aax|plugin|synth|daw|effect|effects|update|review|preview)[:\s\-]+',
        r'^new\s+(?:free\s+)?(?:vst|plugin|synth|daw|effect)[:\s\-]+',
        r'^(?:review|preview|announced?|released?|launches?|introducing|unveiled?)[:\s\-]+',
        r'^(?:download|get|try)[:\s\-]+',
    ]
    for pat in noise_prefixes:
        name = re.sub(pat, '', name, flags=re.IGNORECASE).strip()

    # Strip trailing noise
    name = re.sub(
        r'\s*[\-\|–—]\s*(?:review|preview|free\s+download|now\s+available|released?|'
        r'announced?|update|v\d+[\.\d]*|vst|plugin|au|aax|mac|windows|pc|ios|android).*$',
        '', name, flags=re.IGNORECASE
    ).strip()

    # Remove year at end
    name = re.sub(r'\s+20\d\d$', '', name).strip()

    # Truncate
    if len(name) > 60:
        name = name[:57].rsplit(' ', 1)[0] + '...'

    return name or title[:60]


def extract_formats(text: str) -> list:
    formats = []
    for fmt in ['VST3', 'VST', 'AU', 'AAX', 'CLAP', 'AUv3', 'iOS', 'Standalone']:
        if re.search(r'\b' + fmt + r'\b', text, re.IGNORECASE):
            formats.append(fmt)
    return formats


def extract_os(text: str) -> list:
    os_list = []
    text_lower = text.lower()
    if any(w in text_lower for w in ['windows', 'pc', 'win ']):
        os_list.append('Windows')
    if any(w in text_lower for w in ['macos', 'mac os', 'mac ', 'apple silicon', 'm1', 'm2', 'm3']):
        os_list.append('macOS')
    if 'linux' in text_lower:
        os_list.append('Linux')
    if 'ios' in text_lower or 'ipad' in text_lower or 'iphone' in text_lower:
        os_list.append('iOS')
    if not os_list:
        os_list = ['Windows', 'macOS']
    return os_list


def run_firecrawl_scrape(url: str, output_path: str) -> bool:
    """Run firecrawl scrape CLI command. Returns True on success."""
    try:
        result = subprocess.run(
            ['firecrawl', 'scrape', url, '--only-main-content', '-o', output_path],
            capture_output=True, text=True, timeout=60
        )
        return result.returncode == 0 and Path(output_path).exists() and Path(output_path).stat().st_size > 100
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f'  [firecrawl] error: {e}')
        return False


def run_firecrawl_map(url: str, output_path: str) -> list:
    """Get all URLs from a site using firecrawl map. Returns list of URLs."""
    try:
        result = subprocess.run(
            ['firecrawl', 'scrape', url, '--format', 'links', '-o', output_path],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0 and Path(output_path).exists():
            content = Path(output_path).read_text(encoding='utf-8', errors='replace')
            # The output might be JSON with links array or plain text
            try:
                data = json.loads(content)
                if isinstance(data, dict):
                    links = data.get('links', data.get('data', {}).get('links', []))
                    return [l.get('url', l) if isinstance(l, dict) else l for l in links]
                elif isinstance(data, list):
                    return [l.get('url', l) if isinstance(l, dict) else l for l in data]
            except json.JSONDecodeError:
                # Plain text — one URL per line
                return [line.strip() for line in content.splitlines() if line.strip().startswith('http')]
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f'  [firecrawl map] error: {e}')
    return []


def extract_links_from_markdown(content: str, base_domain: str) -> list:
    """Extract hyperlinks from markdown content."""
    links = []
    # Markdown links: [text](url)
    for match in re.finditer(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content):
        links.append(match.group(2).strip())
    # Plain URLs in text
    for match in re.finditer(r'https?://[^\s\)\]"\'<>]+', content):
        u = match.group(0).rstrip('.,;:')
        links.append(u)
    return list(dict.fromkeys(links))  # dedupe preserving order


def is_article_url(url: str, pattern: str, alt_pattern: str = None) -> bool:
    """Check if URL looks like an individual article/product page."""
    if JUNK_URL_RE.search(url):
        return False
    if re.search(pattern, url):
        return True
    if alt_pattern and re.search(alt_pattern, url):
        return True
    return False


def parse_release_from_content(url: str, content: str) -> dict | None:
    """Parse a release entry from scraped article content."""
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    if not lines:
        return None

    # Title: usually the first H1 or largest heading in the content
    title = ''
    for line in lines[:20]:
        if line.startswith('# '):
            title = line[2:].strip()
            break
        if line.startswith('## '):
            title = line[3:].strip()
            break
    if not title and lines:
        title = lines[0][:120]

    # Skip junk titles
    junk_titles = ['page not found', '404', 'login', 'sign in', 'cookie',
                   'privacy', 'terms', 'subscribe', 'newsletter', 'best free',
                   'top 10', 'top 20', 'best plugins', 'all plugins']
    if len(title) < 10 or any(j in title.lower() for j in junk_titles):
        return None

    # Body text: everything after title
    body_lines = []
    for line in lines[1:40]:
        if line.startswith('#'):
            continue
        if len(line) > 30:
            body_lines.append(line)
        if len(body_lines) >= 5:
            break
    body = ' '.join(body_lines)

    full_text = title + ' ' + content[:2000]
    name = extract_product_name(title, full_text)
    developer = extract_developer(full_text)
    category_id = detect_category(full_text)
    price, price_type = detect_price(full_text)
    formats = extract_formats(full_text)
    os_list = extract_os(full_text)

    short_desc = body[:200] if body else f"{name} — newly released."
    long_desc = body[:500] if body else short_desc

    slug = slugify(name)
    entry_id = make_id(url, name)

    return {
        "id": entry_id,
        "slug": slug,
        "name": name,
        "developer": developer or None,
        "categoryId": category_id,
        "price": price,
        "priceType": price_type,
        "shortDescription": short_desc,
        "longDescription": long_desc,
        "officialUrl": url,
        "rating": 4.0,
        "ratingCount": 0,
        "isNew": True,
        "isFeatured": False,
        "os": os_list,
        "formats": formats,
        "features": [],
        "pros": [],
        "cons": ["New — limited reviews"],
        "tags": [category_id],
        "targetAudience": "Music producers and audio engineers",
        "dateAdded": datetime.now(timezone.utc).isoformat(),
        "sourceTitle": title,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def scrape_releases():
    print('[releases] starting Firecrawl scraper...')

    # Verify firecrawl is available
    try:
        result = subprocess.run(['firecrawl', '--version'], capture_output=True, text=True, timeout=10)
        print(f'[releases] firecrawl version: {result.stdout.strip() or result.stderr.strip()}')
    except FileNotFoundError:
        print('[releases] ERROR: firecrawl CLI not found. Install: npm install -g firecrawl-cli')
        sys.exit(1)

    # Load existing releases
    existing: list[dict] = []
    if RELEASES_FILE.exists():
        try:
            existing = json.loads(RELEASES_FILE.read_text(encoding='utf-8'))
            print(f'[releases] loaded {len(existing)} existing entries')
        except Exception as e:
            print(f'[releases] WARNING: could not read releases.json: {e}')

    existing_urls = {e.get('officialUrl', '') for e in existing}
    existing_slugs = {e.get('slug', '') for e in existing}
    new_entries: list[dict] = []

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        for source_idx, source in enumerate(LISTING_PAGES):
            print(f'\n[releases] === Source {source_idx+1}/{len(LISTING_PAGES)}: {source["name"]} ===')
            print(f'[releases] Scraping listing page: {source["url"]}')

            # Step 1: Scrape listing page to get article links
            listing_file = str(tmp / f'listing_{source_idx}.md')
            success = run_firecrawl_scrape(source['url'], listing_file)

            if not success:
                print(f'  [!] Could not scrape listing page, skipping')
                continue

            content = Path(listing_file).read_text(encoding='utf-8', errors='replace')
            print(f'  [+] Got {len(content)} chars from listing page')

            # Step 2: Extract article links
            all_links = extract_links_from_markdown(content, source['url'])
            alt_pattern = source.get('alt_pattern', '')
            article_links = [
                url for url in all_links
                if is_article_url(url, source['link_pattern'], alt_pattern)
                and url not in existing_urls
            ]

            # Deduplicate
            seen = set()
            article_links_deduped = []
            for u in article_links:
                if u not in seen:
                    seen.add(u)
                    article_links_deduped.append(u)

            article_links = article_links_deduped[:MAX_ARTICLES_PER_SOURCE]
            print(f'  [+] Found {len(article_links)} new article links to scrape')

            if not article_links:
                print(f'  [!] No new articles found')
                continue

            # Step 3: Scrape each article
            for art_idx, article_url in enumerate(article_links):
                print(f'  [{art_idx+1}/{len(article_links)}] Scraping: {article_url[:80]}')

                # Small delay to be polite
                if art_idx > 0:
                    time.sleep(random.uniform(1.5, 3.0))

                article_file = str(tmp / f'article_{source_idx}_{art_idx}.md')
                ok = run_firecrawl_scrape(article_url, article_file)

                if not ok:
                    print(f'    [!] Scrape failed, skipping')
                    continue

                article_content = Path(article_file).read_text(encoding='utf-8', errors='replace')

                # Step 4: Parse structured data
                entry = parse_release_from_content(article_url, article_content)
                if not entry:
                    print(f'    [!] Could not parse release data, skipping')
                    continue

                if entry['slug'] in existing_slugs:
                    print(f'    [~] Duplicate slug: {entry["slug"]}, skipping')
                    continue

                new_entries.append(entry)
                existing_urls.add(article_url)
                existing_slugs.add(entry['slug'])
                print(f'    [+] {entry["name"]} ({entry["categoryId"]}) [{entry["priceType"]}]')

            print(f'  -> {len([e for e in new_entries if True])} total new entries so far')

            # Delay between sources
            if source_idx < len(LISTING_PAGES) - 1:
                time.sleep(random.uniform(3.0, 5.0))

    # Merge: new first, then existing, drop old
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_AGE_DAYS)
    merged = new_entries + existing

    # Deduplicate by slug
    seen_slugs: set = set()
    deduped: list = []
    for entry in merged:
        if entry['slug'] not in seen_slugs:
            seen_slugs.add(entry['slug'])
            deduped.append(entry)

    def entry_date(e: dict):
        try:
            return datetime.fromisoformat(e.get('dateAdded', '2020-01-01T00:00:00+00:00'))
        except Exception:
            return datetime.min.replace(tzinfo=timezone.utc)

    deduped.sort(key=entry_date, reverse=True)
    deduped = [e for e in deduped if entry_date(e) > cutoff][:MAX_KEEP]

    RELEASES_FILE.write_text(json.dumps(deduped, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'\n[releases] done. {len(new_entries)} new entries scraped, {len(deduped)} total in releases.json')
    return len(new_entries)


if __name__ == '__main__':
    scrape_releases()
