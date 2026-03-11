#!/usr/bin/env python3
"""
scripts/scrape_releases.py
Scrapes VST / DAW / plugin release announcements from trusted sources
and writes them to data/releases.json.

Run every 24-48h via GitHub Actions.
"""

import sys
import os
import re
import json
import time
import random
import hashlib
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).parent.parent
RELEASES_FILE = ROOT / "data" / "releases.json"

MAX_KEEP = 30          # max entries to keep in releases.json
MAX_AGE_DAYS = 14      # drop entries older than this
QUERY_DELAY = (2.0, 4.0)
MAX_RETRIES = 3
RETRY_BASE_DELAY = 5

# Trusted release-focused sources
DOMAIN_WHITELIST = {
    "kvraudio.com",
    "bedroomproducersblog.com",
    "rekkerd.org",
    "synthanatomy.com",
    "synthtopia.com",
    "gearnews.com",
    "musicradar.com",
    "sonicstate.com",
    "cdm.link",
    "pro-tools-expert.com",
    "ableton.com",
    "bitwig.com",
    "image-line.com",
    "reasonstudios.com",
    "presonus.com",
    "attackmagazine.com",
    "musictech.com",
    "soundonsound.com",
    "plugin-alliance.com",
    "waves.com",
    "izotope.com",
    "native-instruments.com",
    "pluginboutique.com",
    "audioplugin.deals",
    "vstbuzz.com",
    "arturia.com",
    "fabfilter.com",
    "uaudio.com",
    "softube.com",
    "eventideaudio.com",
}

SEARCH_QUERIES = [
    # Plugin & VST releases
    "site:kvraudio.com OR site:bedroomproducersblog.com new VST plugin released 2026",
    "site:rekkerd.org OR site:synthanatomy.com plugin announced released 2026",
    "site:gearnews.com OR site:musicradar.com new VST DAW plugin 2026",
    "site:sonicstate.com OR site:cdm.link plugin synth released announced 2026",
    "site:pluginboutique.com OR site:audioplugin.deals new plugin deal release",
    # DAW updates
    "site:pro-tools-expert.com OR site:ableton.com DAW update released 2026",
    "site:bitwig.com OR site:image-line.com update release announced 2026",
    "site:reasonstudios.com OR site:presonus.com DAW update 2026",
    # Synth / hardware
    "site:synthtopia.com OR site:sonicstate.com synthesizer announced released 2026",
    # Broad topic queries
    "new VST3 plugin released free download 2026",
    "new DAW update release 2026 audio workstation",
    "(FabFilter OR iZotope OR Waves OR Native Instruments) plugin released 2026",
    "(Arturia OR Roland OR Korg) new software announced 2026",
    "free VST plugin released 2026 site:bedroomproducersblog.com",
    "new synth plugin released 2026 site:synthanatomy.com",
]

# keyword → categoryId
CATEGORY_MAP = {
    "daw": ["daw", "ableton", "logic pro", "fl studio", "cubase", "pro tools",
            "reaper", "bitwig", "studio one", "reason", "garageband", "digital audio workstation"],
    "synth": ["synth", "synthesizer", "eurorack", "oscillator", "modular", "wavetable",
              "fm synth", "analog synth", "virtual analog"],
    "effects": ["reverb", "delay", "compressor", "eq ", "equalizer", "distortion",
                "chorus", "flanger", "phaser", "limiter", "saturator", "effect plugin",
                "fx plugin", "mastering plugin"],
    "sampler": ["sampler", "sample player", "kontakt", "sample library", "drum kit",
                "sample pack", "rompler"],
    "drums": ["drum", "beat maker", "drum machine", "rhythm", "percussion"],
    "mastering": ["mastering", "loudness", "limiter", "stem splitter", "metering"],
    "midi": ["midi", "arpeggiator", "sequencer", "midi plugin", "midi tool"],
    "vocal": ["vocal", "pitch correction", "autotune", "harmony", "voice"],
    "guitar": ["guitar", "amp sim", "amplifier", "cabinet", "guitar plugin"],
    "utility": ["utility", "spectrum analyzer", "tuner", "meter", "router", "bus"],
}

# Known brands to help extract developer name from title
KNOWN_BRANDS = [
    "FabFilter", "iZotope", "Waves", "Native Instruments", "Arturia", "Roland", "Korg",
    "Moog", "Sequential", "Elektron", "Ableton", "Image-Line", "Bitwig", "PreSonus",
    "Reason Studios", "Avid", "Steinberg", "Plugin Alliance", "Softube", "UAD",
    "Universal Audio", "Eventide", "Output", "Xfer Records", "Matt Tytel",
    "Surge Synth Team", "VCV", "Cherry Audio", "U-He", "Diva", "Pigments",
    "Serum", "Vital", "LABS", "Spitfire", "EastWest", "ProjectSAM",
    "Soundtoys", "Valhalla DSP", "Zynaptiq", "Oeksound", "Slate Digital",
    "Brainworx", "Sonnox", "McDSP", "Flux", "Nugen Audio", "T-RackS", "IK Multimedia",
    "Celemony", "Melodyne", "Antares", "Auto-Tune", "Synchro Arts", "Revoice",
    "Little Alter Boy", "Soundshifter", "Ohm Force", "D16 Group", "TAL Software",
    "Newfangled Audio", "Acustica Audio", "Kazrog", "Nomad Factory",
]

BRAND_PATTERN = re.compile(
    r'\b(' + '|'.join(re.escape(b) for b in KNOWN_BRANDS) + r')\b',
    re.IGNORECASE
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:80]


def get_domain(url: str) -> str:
    match = re.search(r'https?://(?:www\.)?([^/]+)', url)
    return match.group(1).lower() if match else ''


def is_whitelisted(url: str) -> bool:
    domain = get_domain(url)
    return any(domain == w or domain.endswith('.' + w) for w in DOMAIN_WHITELIST)


def extract_developer(title: str, description: str) -> str:
    """Try to extract developer/brand from title or description."""
    text = title + ' ' + (description or '')
    match = BRAND_PATTERN.search(text)
    if match:
        # Return canonical casing from KNOWN_BRANDS
        found = match.group(1)
        for brand in KNOWN_BRANDS:
            if brand.lower() == found.lower():
                return brand
        return found

    # Pattern: "XYZ by Developer" or "Developer releases XYZ" or "Developer's XYZ"
    patterns = [
        r'by\s+([A-Z][A-Za-z0-9\s]+?)[\s,\.\-]',
        r'^([A-Z][A-Za-z0-9]+)\s+(?:releases?|launches?|announces?|introduces?|unveils?)',
        r'^([A-Z][A-Za-z0-9]+)(?:\'s)?\s+new\b',
    ]
    for pat in patterns:
        m = re.search(pat, title)
        if m:
            candidate = m.group(1).strip()
            if len(candidate) > 2 and len(candidate) < 40:
                return candidate
    return ''


def extract_name(title: str) -> str:
    """Extract product name from release announcement title."""
    # Strip common prefixes
    prefixes = [
        r'^(?:free\s+)?(?:vst|plugin|synth|daw|effect|update)[\s:\-]+',
        r'^new\s+(?:free\s+)?(?:vst|plugin|synth|daw)[\s:\-]+',
        r'^(?:review|preview|announced?|released?|launches?|introducing|introducing|unveiled?)[\s:\-]+',
    ]
    name = title
    for pat in prefixes:
        name = re.sub(pat, '', name, flags=re.IGNORECASE).strip()

    # Strip trailing noise like " - Review", " Now Available", " Released", " Free Download"
    name = re.sub(
        r'\s*[\-–—]\s*(?:review|preview|free\s+download|now\s+available|released?|announced?|update|v\d+[\.\d]*).*$',
        '', name, flags=re.IGNORECASE
    ).strip()

    # Remove year at end
    name = re.sub(r'\s+20\d\d$', '', name).strip()

    # Truncate if still too long
    if len(name) > 60:
        name = name[:57].rsplit(' ', 1)[0] + '...'

    return name or title[:60]


def detect_category(title: str, description: str) -> str:
    text = (title + ' ' + (description or '')).lower()
    for cat_id, keywords in CATEGORY_MAP.items():
        if any(kw in text for kw in keywords):
            return cat_id
    return 'utility'


def detect_price(title: str, description: str) -> tuple[float, str]:
    """Returns (price, priceType)."""
    text = (title + ' ' + (description or '')).lower()

    # Free indicators
    if any(w in text for w in ['free download', 'free vst', 'free plugin', 'freeware', 'open source']):
        return 0.0, 'free'

    # Price patterns like $49, €29, £19
    price_match = re.search(r'[\$€£](\d+(?:\.\d{1,2})?)', text)
    if price_match:
        return float(price_match.group(1)), 'one-time'

    # Subscription hints
    if any(w in text for w in ['/month', '/year', 'subscription', 'annual plan']):
        return 9.99, 'subscription'

    # Default: paid, unknown price
    return 0.0, 'paid'


def make_id(url: str, name: str) -> str:
    return hashlib.md5(f"{url}:{name}".encode()).hexdigest()[:12]


JUNK_URL_PATTERNS = [
    r'/forum', r'/forums', r'/ucp\.php', r'/viewtopic', r'/viewforum',
    r'/category/', r'/categories/', r'/tag/', r'/tags/', r'/page/',
    r'/free-vst-plugins/?$', r'/free-vst-plugins/\w+/?$',  # BPB category pages
    r'/search', r'/author/', r'/feed/', r'/rss',
]
JUNK_URL_RE = re.compile('|'.join(JUNK_URL_PATTERNS), re.IGNORECASE)


def is_junk_url(url: str) -> bool:
    return bool(JUNK_URL_RE.search(url))


def is_junk_title(title: str) -> bool:
    if len(title) < 10:
        return True
    junk = ['page not found', '404', 'login', 'sign in', 'subscribe', 'cookie',
            'privacy policy', 'terms of', 'search results', 'all plugins', 'latest releases',
            'kvr audio - forum', 'vst plugin, au, aax', 'free vst plugins (20',
            'best free', 'top 10', 'top 20', 'best plugins']
    tl = title.lower()
    return any(j in tl for j in junk)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def scrape_releases():
    print('[releases] starting scraper...')
    try:
        from ddgs import DDGS
    except ImportError:
        print('[releases] ERROR: ddgs not installed. Run: pip install duckduckgo-search')
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
    new_entries: list[dict] = []

    with DDGS() as ddgs:
        for qi, query in enumerate(SEARCH_QUERIES):
            if qi > 0:
                time.sleep(random.uniform(*QUERY_DELAY))

            label = query[:70] + '...' if len(query) > 70 else query
            print(f'\n[releases] query {qi+1}/{len(SEARCH_QUERIES)}: {label}')

            results = None
            for attempt in range(MAX_RETRIES):
                try:
                    results = ddgs.text(query, region='wt-wt', safesearch='off',
                                        timelimit='w', max_results=15)
                    break
                except Exception as e:
                    wait = RETRY_BASE_DELAY * (2 ** attempt)
                    print(f'[releases] ERROR attempt {attempt+1}: {e}')
                    if attempt < MAX_RETRIES - 1:
                        time.sleep(wait)

            if not results:
                print('[releases] no results')
                continue

            saved = 0
            for r in results:
                url = r.get('href', '').strip()
                title = r.get('title', '').strip()
                body = r.get('body', '').strip()

                if not url or not title:
                    continue
                if is_junk_title(title):
                    continue
                if is_junk_url(url):
                    continue
                if not is_whitelisted(url):
                    continue
                if url in existing_urls:
                    continue

                name = extract_name(title)
                developer = extract_developer(title, body)
                category_id = detect_category(title, body)
                price, price_type = detect_price(title, body)
                entry_id = make_id(url, name)
                slug = slugify(name)

                entry = {
                    "id": entry_id,
                    "slug": slug,
                    "name": name,
                    "developer": developer or None,
                    "categoryId": category_id,
                    "price": price,
                    "priceType": price_type,
                    "shortDescription": body[:200] if body else f"{name} — new release.",
                    "longDescription": body[:500] if body else f"{name} — recently announced.",
                    "officialUrl": url,
                    "rating": 4.0,
                    "ratingCount": 0,
                    "isNew": True,
                    "isFeatured": False,
                    "os": ["Windows", "macOS"],
                    "formats": [],
                    "features": [f"New release: {name}"],
                    "pros": ["Recently released"],
                    "cons": ["New — limited reviews"],
                    "tags": [category_id],
                    "targetAudience": "Music producers and audio engineers",
                    "dateAdded": datetime.now(timezone.utc).isoformat(),
                    "sourceTitle": title,
                }

                new_entries.append(entry)
                existing_urls.add(url)
                saved += 1
                print(f'  [+] {name} ({category_id}) — {url[:60]}')

            print(f'  -> saved {saved} new entries from this query')

    # Merge: new first, then existing, drop old entries
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_AGE_DAYS)
    merged = new_entries + existing

    # Deduplicate by slug
    seen_slugs: set[str] = set()
    deduped: list[dict] = []
    for entry in merged:
        if entry['slug'] not in seen_slugs:
            seen_slugs.add(entry['slug'])
            deduped.append(entry)

    # Drop old entries, keep MAX_KEEP most recent
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
