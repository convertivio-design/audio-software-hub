/**
 * Deterministic guard: nav-scrape artifacts must match the same rules as
 * lib/data.ts (RELEASE_JUNK_PATTERN) and validate_releases.js (JUNK_PATTERN).
 * Update all three when changing junk detection.
 */
const RELEASE_JUNK_PATTERN =
  /\[menu\]|\[close\s*menu\]|closemenu|menuhttps?|menuhttp|close-menu|403\s*-\s*forbidden|please go to|bedroom producers blog|news ticker|can't find the page|cannot find the page|page you were looking for|we're sorry|we are sorry|typo|try one of these options|\bfree drum kits\b|\bdrum kits\b|\bdigital audio workstations\b|\bthese are the best\b|\bhigh-quality\b|\bincluded fully free\b|\bbpb\b|\bbpb’s\b|\bbpb's\b|!\[[^\]]*\]\(https?:\/\/|\]\(https?:\/\/|\\\s*[^\]]+\]\(https?:\/\/|\[\\?\[|\*\*|\\\\|\s\\\s/i

function slugHasNavArtifact(slug) {
  const s = String(slug || '').trim().toLowerCase()
  if (!s) return true
  if (s.includes('http') || s.includes('menuhttp') || s.includes('closemenu')) return true
  if (/[\[\]#]/.test(String(slug || ''))) return true
  return false
}

const mustMatchJunk = [
  '[MENU](https://synthanatomy.com/2026/04/foo.html#)',
  '[Close Menu](https://bedroomproducersblog.com/free-vst-plugins/daw/#)',
  'close-menuhttpsbedroomproducersblogcomfree',
  'menuhttpssynthanatomycom202604casio',
  '403 - Forbidden',
]

const mustNotMatchJunk = [
  'FabFilter Pro-Q 4 — recently released.',
  'Xfer Records Serum 2',
  'A normal short description without junk.',
]

for (const s of mustMatchJunk) {
  if (!RELEASE_JUNK_PATTERN.test(s)) {
    console.error('FAIL: expected junk match for:', JSON.stringify(s))
    process.exit(1)
  }
}

for (const s of mustNotMatchJunk) {
  if (RELEASE_JUNK_PATTERN.test(s)) {
    console.error('FAIL: expected clean string, got junk match:', JSON.stringify(s))
    process.exit(1)
  }
}

if (!slugHasNavArtifact('menuhttpssynthanatomycom202604')) {
  console.error('FAIL: slug with menuhttp should be artifact')
  process.exit(1)
}
if (slugHasNavArtifact('fabfilter-pro-q-4')) {
  console.error('FAIL: normal slug flagged as artifact')
  process.exit(1)
}

console.log('release_nav_artifact_test: OK')
