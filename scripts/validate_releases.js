const fs = require('fs')
const path = require('path')

const RELEASES_PATH = path.join(process.cwd(), 'data', 'releases.json')
const JUNK_PATTERN = /\[menu\]|menuhttps?|menuhttp|close-menu|403\s*-\s*forbidden|please go to|bedroom producers blog|news ticker|can't find the page|cannot find the page|page you were looking for|we're sorry|we are sorry|typo|try one of these options|\bfree drum kits\b|\bdrum kits\b|\bdigital audio workstations\b|\bthese are the best\b|\bhigh-quality\b|\bincluded fully free\b|\bbpb\b|\bbpb’s\b|\bbpb's\b|!\[[^\]]*\]\(https?:\/\/|\]\(https?:\/\/|\\\s*[^\]]+\]\(https?:\/\/|\[\\?\[|\*\*|\\\\|\s\\\s|— newly released\.|— recently released\./i
const IP_PATTERN = /\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[a-f0-9]{1,4}:){2,}[a-f0-9]{1,4}\b/i

function normalizeOfficialUrl(url) {
  let u = String(url || '').trim()
  for (const sep of [' "', " '", '\t', '\n', '\r', '<']) {
    const i = u.indexOf(sep)
    if (i !== -1) u = u.slice(0, i).trim()
  }
  return u.replace(/[.,);]+$/g, '')
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message)
  }
}

function isGenericName(name) {
  const n = String(name || '').trim().toLowerCase()
  if (!n) return true
  if (n === 'software' || n === 'plugin' || n === 'plugins' || n === 'news' || n === 'news ticker') return true
  if (n.length < 6) return true
  if (!/[a-z]/i.test(n)) return true
  return false
}

function looksLikeRoundupCopy(text) {
  const t = String(text || '').toLowerCase()
  if (/\bthese are the best\b/.test(t)) return true
  if (/\bhigh-quality\b/.test(t) && /\bdrum kits\b/.test(t)) return true
  if (/\bfree\b/.test(t) && /\bdigital audio workstations\b/.test(t)) return true
  if (/\bbpb\b/.test(t) || /\bbpb’s\b/.test(t) || /\bbpb's\b/.test(t)) return true
  if (/\bcan't find the page\b/.test(t) || /\bcannot find the page\b/.test(t)) return true
  if (/\bwe're sorry\b/.test(t) || /\bwe are sorry\b/.test(t)) return true
  if (/\bpage you were looking for\b/.test(t)) return true
  if (/\btry one of these options\b/.test(t)) return true
  if (/\btypo\b/.test(t) && /\boptions\b/.test(t)) return true
  if (/\bhundreds of drum sample packs\b/.test(t) || /\blisted my favorites\b/.test(t)) return true
  if (/\bincluded fully free tools\b/.test(t) || /\bincluded fully free\b/.test(t)) return true
  if ((String(text).match(/\*\*/g) || []).length >= 2) return true
  if ((String(text).match(/\\\\/g) || []).length >= 1) return true
  if ((String(text).match(/\s\\\s/g) || []).length >= 1) return true
  return false
}

function main() {
  const raw = fs.readFileSync(RELEASES_PATH, 'utf-8')
  const releases = JSON.parse(raw)
  assert(Array.isArray(releases), 'releases.json must be an array')

  const issues = []

  releases.forEach((entry, idx) => {
    const label = `entry[${idx}]`
    const slug = typeof entry.slug === 'string' ? entry.slug.trim() : ''
    const name = typeof entry.name === 'string' ? entry.name.trim() : ''
    const shortDescription = typeof entry.shortDescription === 'string' ? entry.shortDescription.trim() : ''

    if (!slug) issues.push(`${label}: missing slug`)
    if (!name) issues.push(`${label}: missing name`)
    if (!shortDescription) issues.push(`${label}: missing shortDescription`)
    if (isGenericName(name)) issues.push(`${label}: name is too generic`)
    if (
      (name.startsWith('"') && name.endsWith('"')) ||
      (name.startsWith('“') && name.endsWith('”'))
    ) {
      issues.push(`${label}: name is a quoted title fragment`)
    }
    if (typeof entry.sourceTitle === 'string' && isGenericName(entry.sourceTitle)) {
      issues.push(`${label}: sourceTitle is too generic`)
    }
    if (looksLikeRoundupCopy(shortDescription) || looksLikeRoundupCopy(entry.longDescription)) {
      issues.push(`${label}: description looks like a roundup / error page`)
    }

    ;['slug', 'name', 'shortDescription', 'longDescription', 'sourceTitle', 'officialUrl'].forEach((field) => {
      const value = field === 'officialUrl' && typeof entry[field] === 'string'
        ? normalizeOfficialUrl(entry[field])
        : entry[field]
      if (typeof value === 'string' && JUNK_PATTERN.test(value)) {
        issues.push(`${label}: ${field} contains scraped junk`)
      }
      if (typeof value === 'string' && IP_PATTERN.test(value)) {
        issues.push(`${label}: ${field} contains IP/address artifact`)
      }
      if (field === 'officialUrl' && typeof value === 'string') {
        if (!value.startsWith('http')) issues.push(`${label}: officialUrl must start with http(s)`)
        if (value.includes(' ') || value.includes('"') || value.includes("'")) {
          issues.push(`${label}: officialUrl contains whitespace or quotes`)
        }
      }
    })
  })

  if (issues.length > 0) {
    throw new Error(`Release validation failed:\n- ${issues.join('\n- ')}`)
  }

  console.log(`Release validation passed (${releases.length} entries)`)
}

try {
  main()
} catch (error) {
  console.error(error.message || error)
  process.exit(1)
}
