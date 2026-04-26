const fs = require('fs')
const path = require('path')

const RELEASES_PATH = path.join(process.cwd(), 'data', 'releases.json')
const JUNK_PATTERN = /\[menu\]|menuhttps?|menuhttp|close-menu/i

function assert(condition, message) {
  if (!condition) {
    throw new Error(message)
  }
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

    ;['slug', 'name', 'shortDescription', 'sourceTitle', 'officialUrl'].forEach((field) => {
      const value = entry[field]
      if (typeof value === 'string' && JUNK_PATTERN.test(value)) {
        issues.push(`${label}: ${field} contains menu artifact`)
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
