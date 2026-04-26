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
import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).parent.parent
RELEASES_FILE = ROOT / "data" / "releases.json"
STATUS_FILE = ROOT / "data" / "scraper-status.json"

MAX_KEEP = 30
MAX_ARTICLES_PER_SOURCE = 8  # articles to scrape per listing page

# Listing pages that contain links to individual release articles
LISTING_PAGES = [
    {
        "url": "https://www.kvraudio.com/news/",
        "name": "KVR Audio News",
        "link_pattern": r"kvraudio\.com/product/",
        "alt_pattern": r"kvraudio\.com/news/[^\s\)]+-\d+",
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


def write_status(status: str, started_at: str, **extra) -> None:
    """Write a small health file so the scheduler cannot fail silently."""
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "status": status,
        "startedAt": started_at,
        "finishedAt": datetime.now(timezone.utc).isoformat(),
        **extra,
    }
    STATUS_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')


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


def extract_name_from_url(url: str) -> str:
    """Extract a readable product-style name from article URL slug."""
    path = re.sub(r'^https?://[^/]+/', '', url).strip('/')
    if not path:
        return ''
    slug_part = path.split('/')[-1]
    slug_part = re.sub(r'\.(html?|php)$', '', slug_part, flags=re.IGNORECASE)
    slug_part = re.sub(r'^[0-9]+-', '', slug_part)
    slug_part = slug_part.replace('-', ' ').replace('_', ' ')
    slug_part = re.sub(r'\s+', ' ', slug_part).strip()
    if not slug_part:
        return ''
    return slug_part.title()


def is_junk_title_line(line: str) -> bool:
    """Detect obvious navigation/utility lines that should not be used as titles."""
    line_lower = line.lower()
    if contains_ip_address(line):
        return True
    stripped = line.lstrip('#').strip()
    if re.fullmatch(r'(?:\d{1,3}\.){3}\d{1,3}', stripped):
        return True
    if re.fullmatch(r'(?:[a-f0-9]{1,4}:){2,}[a-f0-9]{1,4}', stripped, flags=re.IGNORECASE):
        return True
    if contains_scraped_junk(line):
        return True
    if re.match(r'^\[[^\]]+\]\(https?://[^\)]+\)$', line.strip(), flags=re.IGNORECASE):
        return True
    junk_tokens = [
        '[menu]', '[home]', '[about]', '[contact]', 'share this', 'newsletter',
        'subscribe', 'privacy policy', 'cookie policy', 'terms of use',
        'news ticker', 'ticker', 'software', 'plugins', 'plugin', 'free drum kits',
        'digital audio workstations', 'free digital audio workstations',
    ]
    return any(token in line_lower for token in junk_tokens)


def is_junk_body_line(line: str) -> bool:
    """Detect sidebar/meta lines that should not be used for product description."""
    stripped = line.strip()
    lowered = stripped.lower()
    if not stripped:
        return True
    if contains_scraped_junk(stripped):
        return True
    if stripped.startswith('#'):
        return True
    if re.match(r'^\[[^\]]+\]\(https?://[^\)]+\)$', stripped, flags=re.IGNORECASE):
        return True
    junk_snippets = [
        'subscribe', 'newsletter', 'follow us', 'share this', 'related posts',
        'categories:', 'tags:', 'cookie', 'privacy policy', 'terms of use',
        'advertisement',
        'these are the best', 'digital audio workstations', 'free drum kits',
        'high-quality', 'drum kits', 'sample packs', 'bpb', "bpb's", 'bpb’s',
        "can't find the page", 'cannot find the page', "we're sorry", 'we are sorry',
        'page you were looking for', 'try one of these options',
    ]
    if any(snippet in lowered for snippet in junk_snippets):
        return True
    if stripped.count('**') >= 2:
        return True
    if stripped.count('\\\\') >= 1 or re.search(r'\s\\\s', stripped):
        return True
    return len(stripped) < 25


SCRAPED_JUNK_RE = re.compile(
    r'(\[menu\]|\[close\s*menu\]|closemenu|menuhttps?|menuhttp|close-menu|403\s*-\s*forbidden|please go to|'
    r'bedroom producers blog|news ticker|can\'t find the page|cannot find the page|page you were looking for|'
    r'we\'re sorry|we are sorry|\btypo\b|try one of these options|\bfree drum kits\b|\bdrum kits\b|'
    r'\bdigital audio workstations\b|\bthese are the best\b|\bhigh-quality\b|\bincluded fully free\b|\bbpb\b|\bbpb’s\b|\bbpb\'s\b|'
    r'!\[[^\]]*\]\(https?://|\]\(https?://|'
    r'\\\s*[^\]]+\]\(https?://|\[\\?\[|\*\*|\\\\|\s\\\s)',
    re.IGNORECASE,
)

IPV4_RE = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
IPV6_RE = re.compile(r'\b(?:[a-f0-9]{1,4}:){2,}[a-f0-9]{1,4}\b', re.IGNORECASE)


def contains_scraped_junk(value: str) -> bool:
    return bool(value and SCRAPED_JUNK_RE.search(value))


def contains_ip_address(value: str) -> bool:
    if not value:
        return False
    return bool(IPV4_RE.search(value) or IPV6_RE.search(value))


def is_generic_release_name(name: str) -> bool:
    n = name.strip().lower()
    if not n:
        return True
    if n in {'software', 'plugin', 'plugins', 'news', 'news ticker'}:
        return True
    if len(n) < 6:
        return True
    if not re.search(r'[a-z]', n, flags=re.IGNORECASE):
        return True
    return False


def looks_like_roundup_copy(text: str) -> bool:
    t = text.lower()
    if 'these are the best' in t:
        return True
    if 'high-quality' in t and 'drum kits' in t:
        return True
    if 'free' in t and 'digital audio workstations' in t:
        return True
    if 'bpb' in t or 'bpb’s' in t or "bpb's" in t:
        return True
    if "can't find the page" in t or 'cannot find the page' in t:
        return True
    if "we're sorry" in t or 'we are sorry' in t:
        return True
    if 'page you were looking for' in t:
        return True
    if 'try one of these options' in t:
        return True
    if 'typo' in t and 'options' in t:
        return True
    if 'hundreds of drum sample packs' in t or 'listed my favorites' in t:
        return True
    if 'included fully free tools' in t or 'included fully free' in t:
        return True
    if text.count('**') >= 2:
        return True
    if text.count('\\\\') >= 1:
        return True
    if re.search(r'\s\\\s', text):
        return True
    return False


def normalize_official_url(url: str) -> str:
    """Strip accidental concatenation from markdown link extraction (title glued after URL)."""
    if not url:
        return ''
    u = url.strip()
    for sep in (' "', " '", '\t', '\n', '\r', '<'):
        if sep in u:
            u = u.split(sep, 1)[0].strip()
    u = u.rstrip('.,);')
    return u


def validate_entry(entry: dict) -> tuple[bool, str]:
    """Return (is_valid, reason). Reject obvious parsing garbage."""
    name = str(entry.get('name', '')).strip()
    slug = str(entry.get('slug', '')).strip().lower()
    desc = str(entry.get('shortDescription', '')).strip().lower()
    long_desc = str(entry.get('longDescription', '')).strip().lower()
    official_raw = normalize_official_url(str(entry.get('officialUrl', '')).strip())
    official_url = official_raw.lower()
    source_title = str(entry.get('sourceTitle', '')).strip().lower()
    short_raw = str(entry.get('shortDescription', '')).strip()
    long_raw = str(entry.get('longDescription', '')).strip()
    source_title_raw = str(entry.get('sourceTitle', '')).strip()

    if not name:
        return False, 'name_missing'
    if contains_scraped_junk(name):
        return False, 'name_contains_scraped_junk'
    if contains_ip_address(name):
        return False, 'name_contains_ip_address'
    if is_generic_release_name(name):
        return False, 'name_too_generic'
    if (name.startswith('"') and name.endswith('"')) or (name.startswith('“') and name.endswith('”')):
        return False, 'name_is_quoted_title_fragment'
    if name.startswith('[') and '](' in name:
        return False, 'name_is_markdown_link'
    if len(name) < 5 or len(name) > 100:
        return False, 'name_length_invalid'
    if 'menu' in slug or 'http' in slug:
        return False, 'slug_contains_junk'
    if contains_ip_address(slug):
        return False, 'slug_contains_ip_address'
    if contains_scraped_junk(short_raw) or contains_scraped_junk(long_raw):
        return False, 'description_contains_scraped_junk'
    if contains_ip_address(desc) or contains_ip_address(long_desc):
        return False, 'description_contains_ip_address'
    if looks_like_roundup_copy(short_raw) or looks_like_roundup_copy(long_raw):
        return False, 'description_looks_like_roundup_or_error_page'
    if contains_scraped_junk(source_title_raw):
        return False, 'source_title_contains_scraped_junk'
    if contains_ip_address(source_title):
        return False, 'source_title_contains_ip_address'
    if source_title_raw and is_generic_release_name(source_title_raw):
        return False, 'source_title_too_generic'
    if any(token in desc for token in ['subscribe', 'newsletter', 'follow us']):
        return False, 'description_is_boilerplate'
    if not official_raw.startswith('http'):
        return False, 'official_url_missing_or_invalid'
    if ' ' in official_raw or '"' in official_raw or "'" in official_raw:
        return False, 'official_url_contains_whitespace_or_quotes'
    if '\\n' in official_url or '\n' in official_url:
        return False, 'official_url_contains_newline'
    return True, ''


def run_firecrawl_scrape(url: str, output_path: str) -> bool:
    """Run firecrawl scrape CLI command. Returns True on success."""
    api_key = os.environ.get('FIRECRAWL_API_KEY')
    firecrawl_exe = shutil.which('firecrawl') or shutil.which('firecrawl.cmd') or 'firecrawl'
    cmd = [firecrawl_exe, 'scrape', url, '--only-main-content', '-o', output_path]
    if api_key:
        cmd.extend(['-k', api_key])
    try:
        result = subprocess.run(
            cmd,
            capture_output=True, text=True, timeout=60
        )
        return result.returncode == 0 and Path(output_path).exists() and Path(output_path).stat().st_size > 100
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f'  [firecrawl] error: {e}')
        return False


def run_firecrawl_map(url: str, output_path: str) -> list:
    """Get all URLs from a site using firecrawl map. Returns list of URLs."""
    api_key = os.environ.get('FIRECRAWL_API_KEY')
    firecrawl_exe = shutil.which('firecrawl') or shutil.which('firecrawl.cmd') or 'firecrawl'
    cmd = [firecrawl_exe, 'scrape', url, '--format', 'links', '-o', output_path]
    if api_key:
        cmd.extend(['-k', api_key])
    try:
        result = subprocess.run(
            cmd,
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
    cleaned_links = []
    for link in links:
        link = link.replace('\\n', '').replace('\n', '').strip()
        if link.startswith('http'):
            cleaned_links.append(link)
    return list(dict.fromkeys(cleaned_links))  # dedupe preserving order


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
    url = normalize_official_url(url)
    if not url or ' ' in url or '"' in url or "'" in url:
        return None

    lines = [l.strip() for l in content.splitlines() if l.strip()]
    if not lines:
        return None

    # Title: first meaningful heading, excluding nav/menu lines.
    title = ''
    for line in lines[:20]:
        if is_junk_title_line(line):
            continue
        if line.startswith('# '):
            title = line[2:].strip()
            break
        if line.startswith('## '):
            title = line[3:].strip()
            break
    if not title:
        for line in lines[:25]:
            if is_junk_title_line(line):
                continue
            if len(line) >= 10:
                title = line[:120]
                break
    if not title:
        title = extract_name_from_url(url)
    if not title:
        return None

    # Skip junk titles
    junk_titles = ['page not found', '404', 'login', 'sign in', 'cookie',
                   'privacy', 'terms', 'subscribe', 'newsletter', 'best free',
                   'top 10', 'top 20', 'best plugins', 'all plugins']
    if len(title) < 10 or any(j in title.lower() for j in junk_titles):
        return None

    # Body text: prefer meaningful article lines, skip boilerplate.
    body_lines = []
    for line in lines[1:60]:
        if is_junk_body_line(line):
            continue
        body_lines.append(line)
        if len(body_lines) >= 5:
            break
    body = ' '.join(body_lines)

    full_text = title + ' ' + content[:2000]
    name = extract_product_name(title, full_text)
    if is_junk_title_line(name):
        url_name = extract_name_from_url(url)
        if url_name:
            name = extract_product_name(url_name, full_text)
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

def scrape_releases(dry_run: bool = False):
    started_at = datetime.now(timezone.utc).isoformat()
    source_stats: list[dict] = []
    errors: list[str] = []
    rejected_entries: list[dict] = []
    print('[releases] starting Firecrawl scraper...')

    # Verify firecrawl is available
    firecrawl_exe = shutil.which('firecrawl') or shutil.which('firecrawl.cmd')
    if not firecrawl_exe:
        roaming_bin = Path(os.environ.get('APPDATA', '')) / 'npm' / 'firecrawl.cmd'
        if roaming_bin.exists():
            firecrawl_exe = str(roaming_bin)

    try:
        if not firecrawl_exe:
            raise FileNotFoundError('firecrawl executable not found')
        result = subprocess.run([firecrawl_exe, '--version'], capture_output=True, text=True, timeout=10)
        print(f'[releases] firecrawl version: {result.stdout.strip() or result.stderr.strip()}')
    except FileNotFoundError:
        message = 'firecrawl CLI not found. Install: npm install -g firecrawl-cli'
        print(f'[releases] ERROR: {message}')
        write_status('failure', started_at, error=message)
        sys.exit(1)

    if not os.environ.get('FIRECRAWL_API_KEY'):
        message = 'FIRECRAWL_API_KEY is not set'
        print(f'[releases] ERROR: {message}')
        write_status('failure', started_at, error=message)
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
            stat = {
                "source": source["name"],
                "listingUrl": source["url"],
                "listingScraped": False,
                "candidateLinks": 0,
                "articlesScraped": 0,
                "entriesAdded": 0,
                "entriesRejected": 0,
            }
            print(f'\n[releases] === Source {source_idx+1}/{len(LISTING_PAGES)}: {source["name"]} ===')
            print(f'[releases] Scraping listing page: {source["url"]}')

            # Step 1: Scrape listing page to get article links
            listing_file = str(tmp / f'listing_{source_idx}.md')
            success = run_firecrawl_scrape(source['url'], listing_file)

            if not success:
                message = f'Could not scrape listing page: {source["url"]}'
                errors.append(message)
                source_stats.append(stat)
                print(f'  [!] {message}, skipping')
                continue

            stat["listingScraped"] = True
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
            stat["candidateLinks"] = len(article_links)
            print(f'  [+] Found {len(article_links)} new article links to scrape')

            if not article_links:
                print(f'  [!] No new articles found')
                source_stats.append(stat)
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
                    message = f'Scrape failed: {article_url}'
                    errors.append(message)
                    print(f'    [!] {message}, skipping')
                    continue

                stat["articlesScraped"] += 1
                article_content = Path(article_file).read_text(encoding='utf-8', errors='replace')

                # Step 4: Parse structured data
                entry = parse_release_from_content(article_url, article_content)
                if not entry:
                    print(f'    [!] Could not parse release data, skipping')
                    continue

                if entry['slug'] in existing_slugs:
                    print(f'    [~] Duplicate slug: {entry["slug"]}, skipping')
                    continue

                is_valid, reason = validate_entry(entry)
                if not is_valid:
                    stat["entriesRejected"] += 1
                    rejected_entries.append({
                        "url": article_url,
                        "reason": reason,
                        "name": entry.get("name", ""),
                        "slug": entry.get("slug", ""),
                    })
                    print(f'    [!] Rejected entry: {reason}')
                    continue

                new_entries.append(entry)
                stat["entriesAdded"] += 1
                existing_urls.add(article_url)
                existing_slugs.add(entry['slug'])
                print(f'    [+] {entry["name"]} ({entry["categoryId"]}) [{entry["priceType"]}]')

            print(f'  -> {len([e for e in new_entries if True])} total new entries so far')

            # Delay between sources
            if source_idx < len(LISTING_PAGES) - 1:
                time.sleep(random.uniform(3.0, 5.0))

            source_stats.append(stat)

    if source_stats and not any(s["listingScraped"] for s in source_stats):
        message = 'All listing pages failed to scrape'
        print(f'[releases] ERROR: {message}')
        write_status('failure', started_at, sources=source_stats, errors=errors + [message])
        sys.exit(1)

    if errors and not any(s["articlesScraped"] for s in source_stats):
        message = 'Article scraping failed for all candidate sources'
        print(f'[releases] ERROR: {message}')
        write_status('failure', started_at, sources=source_stats, errors=errors + [message])
        sys.exit(1)

    cleaned_existing: list[dict] = []
    for entry in existing:
        is_valid, reason = validate_entry(entry)
        if is_valid:
            cleaned_existing.append(entry)
            continue
        rejected_entries.append({
            "url": entry.get("officialUrl", ""),
            "reason": f"existing_{reason}",
            "name": entry.get("name", ""),
            "slug": entry.get("slug", ""),
        })

    # Merge: new first, then existing. Keep older entries rather than wiping the
    # homepage when sources have no fresh candidates.
    merged = new_entries + cleaned_existing

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
    deduped = deduped[:MAX_KEEP]

    if dry_run:
        print('[releases] dry-run enabled; not writing releases.json')
    else:
        RELEASES_FILE.write_text(json.dumps(deduped, indent=2, ensure_ascii=False), encoding='utf-8')
        write_status(
            'success',
            started_at,
            dryRun=False,
            existingEntries=len(existing),
            cleanedExistingEntries=len(cleaned_existing),
            newEntries=len(new_entries),
            rejectedEntries=len(rejected_entries),
            outputEntries=len(deduped),
            sources=source_stats,
            errors=errors,
            rejections=rejected_entries[:50],
        )
    print(f'\n[releases] done. {len(new_entries)} new entries scraped, {len(deduped)} total in releases.json')
    return len(new_entries)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape recent audio software releases into data/releases.json')
    parser.add_argument('--dry-run', action='store_true', help='Run discovery and parsing without writing releases.json')
    args = parser.parse_args()
    scrape_releases(dry_run=args.dry_run)
