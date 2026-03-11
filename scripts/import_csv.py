"""
import_csv.py — Clean and import music_directory_full_structure_complete.csv
into data/products.json for the Music Tech Directory app.

Usage:
    python scripts/import_csv.py

Output:
    data/products.json
"""

import csv
import json
import re
import os
import unicodedata

CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'source.csv')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'products.json')

# Map CSV category names → app category IDs
CATEGORY_MAP = {
    'Digital Audio Workstations': 'daw',
    'Synthesizers': 'synth',
    'Effects Plugins': 'effects',
    'Sample Libraries': 'sampler',
    'Drum Machines & Drum Plugins': 'drums',
    'MIDI Tools': 'midi',
    'Utility & Analysis Tools': 'utility',
    'Creative Effects': 'effects',
    'Mastering Tools': 'mastering',
    'Guitar & Bass Plugins': 'guitar',
    'Experimental & Unique Tools': 'experimental',
    'Free Plugins': 'free',
}

# Junk row patterns to skip
JUNK_PATTERNS = [
    r'^\d+$',                          # Pure numbers: "1", "3", "5"
    r'^if you',                         # "If you're looking for..."
    r'^\d+\.',                          # Numbered list items like "49."
    r'^here are',                       # "Here are some trusted..."
    r'^plugin boutique\s*:',
    r'^kvr audio\s*:',
    r'^bedroom producers',
    r'^producer hive',
    r'^the plugin site',
    r'^gearslutz',
    r'^producerspot',
    r'^loopmasters\s*:',
]

def is_junk(name: str) -> bool:
    name_lower = name.strip().lower()
    if not name_lower:
        return True
    for pattern in JUNK_PATTERNS:
        if re.match(pattern, name_lower):
            return True
    return False

def clean_url(url: str) -> str:
    """Strip 'Official Product Page: ', 'Official Download Page: ', etc."""
    url = url.strip()
    # Remove common prefixes
    prefixes = [
        r'^official\s+product\s+page\s*:\s*',
        r'^official\s+download\s+page\s*:\s*',
        r'^official\s+website\s*:\s*',
        r'^official\s+[a-z\s]+page\s*:\s*',
    ]
    for p in prefixes:
        url = re.sub(p, '', url, flags=re.IGNORECASE)
    # Extract first URL if multiple are present
    urls = re.findall(r'https?://[^\s\),]+', url)
    return urls[0].rstrip('.,)') if urls else url.strip()

def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text

def clean_name(name: str) -> str:
    """Remove trailing colons, numbers, and annotation text."""
    name = name.strip()
    # Remove trailing colon
    name = name.rstrip(':')
    # Remove trailing parenthetical
    name = re.sub(r'\s*\([^)]*\)\s*$', '', name)
    # Remove "by Developer" suffix if present
    name = re.sub(r'\s+by\s+[A-Za-z\s]+$', '', name)
    # Remove leading numbering like "49. "
    name = re.sub(r'^\d+\.\s*', '', name)
    return name.strip()

def infer_price_type(name: str, category_id: str) -> str:
    """Best-effort price type inference from name."""
    name_lower = name.lower()
    if 'free' in name_lower or category_id == 'free':
        return 'free'
    return 'one-time'

def main():
    # Read source CSV
    source = os.path.expanduser(r'~\Downloads\music_directory_full_structure_complete.csv')
    if not os.path.exists(source):
        print(f"ERROR: CSV not found at {source}")
        print("Place the CSV at: C:/Users/DELL/Downloads/music_directory_full_structure_complete.csv")
        return

    rows = []
    with open(source, encoding='utf-8-sig') as f:
        # Skip leading blank lines to find the real header row
        lines = f.readlines()
    non_blank = [l for l in lines if l.strip()]
    import io
    reader = csv.DictReader(io.StringIO(''.join(non_blank)))
    for row in reader:
        rows.append(row)

    print(f"Read {len(rows)} rows from CSV")

    products = []
    seen_slugs = set()
    seen_names = set()

    for row in rows:
        raw_name = row.get('Name', '').strip()
        if is_junk(raw_name):
            continue

        name = clean_name(raw_name)
        if not name or len(name) < 2:
            continue

        name_key = name.lower().strip()
        if name_key in seen_names:
            continue
        seen_names.add(name_key)

        raw_url = row.get('Official URL', '').strip()
        url = clean_url(raw_url) if raw_url else ''

        raw_cat = row.get('Category', '').strip()
        category_id = CATEGORY_MAP.get(raw_cat, 'effects')

        # Fix obviously wrong category (Free Plugins → keep type but flag free)
        is_free = category_id == 'free'
        if is_free:
            # Try to infer real category from name
            name_lower = name.lower()
            if any(w in name_lower for w in ['daw', 'studio', 'live', 'logic', 'cubase', 'reaper', 'protools', 'pro tools', 'reason', 'bitwig']):
                category_id = 'daw'
            elif any(w in name_lower for w in ['serum', 'vital', 'synth', 'massive', 'omnisphere', 'pigments', 'phase plant', 'surge']):
                category_id = 'synth'
            elif any(w in name_lower for w in ['drum', 'battery', 'ezdrummer', 'superior', 'addictive']):
                category_id = 'drums'
            elif any(w in name_lower for w in ['kontakt', 'labs', 'spitfire', 'sample', 'library', 'arcade']):
                category_id = 'sampler'
            elif any(w in name_lower for w in ['midi', 'chord', 'scaler', 'arp']):
                category_id = 'midi'
            else:
                category_id = 'effects'

        price_type = 'free' if is_free else infer_price_type(name, category_id)

        # Build slug
        base_slug = slugify(name)
        slug = base_slug
        counter = 2
        while slug in seen_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1
        seen_slugs.add(slug)

        # Extract developer from name if in "Product by Developer" format
        developer = row.get('Developer', '').strip()
        if not developer:
            match = re.search(r'\s+by\s+([A-Za-z][A-Za-z\s]+)$', raw_name)
            if match:
                developer = match.group(1).strip()

        product = {
            "id": slug,
            "name": name,
            "slug": slug,
            "developer": developer,
            "categoryId": category_id,
            "shortDescription": row.get('Description & key features', '').strip() or f"{name} — music production tool.",
            "price": None,
            "priceType": price_type,
            "officialUrl": url,
            "rating": 0,
            "ratingCount": 0,
            "os": [],
            "formats": [],
            "features": [],
            "pros": [],
            "cons": [],
            "tags": [category_id],
            "isFeatured": False,
            "isNew": False,
        }
        products.append(product)

    # Sort by category then name
    products.sort(key=lambda p: (p['categoryId'], p['name'].lower()))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    by_cat = {}
    for p in products:
        by_cat[p['categoryId']] = by_cat.get(p['categoryId'], 0) + 1

    print(f"\nImported {len(products)} clean products:")
    for cat, count in sorted(by_cat.items(), key=lambda x: -x[1]):
        print(f"  {cat:20s} {count}")
    print(f"\nOutput: {OUT_PATH}")

if __name__ == '__main__':
    main()
