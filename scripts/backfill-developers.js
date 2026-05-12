#!/usr/bin/env node
/**
 * scripts/backfill-developers.js
 *
 * Backfill empty `developer` fields in data/products.json.
 *
 * 1. Apply explicit overrides for flagship products (Ableton Live, FL Studio,
 *    Logic Pro, Cubase, Bitwig Studio, Serum, etc.) by slug.
 * 2. For everything else with an empty developer, try to infer the developer
 *    from the product name by looking for a known-brand prefix.
 * 3. Leave the rest alone — do not invent "Unknown".
 *
 * Run once: `node scripts/backfill-developers.js`. Safe to re-run; idempotent.
 *
 * NEW-92.
 */

const fs = require('fs')
const path = require('path')

const PRODUCTS_PATH = path.join(__dirname, '..', 'data', 'products.json')

// Slug -> Developer name. Manual overrides for the products that show up in
// curated surfaces (Top Picks, comparison defaults, flagship category pages).
const SLUG_OVERRIDES = {
  'ableton-live': 'Ableton',
  'ableton-live-12': 'Ableton',
  'ableton-drum-rack': 'Ableton',
  'bitwig-studio': 'Bitwig',
  'cubase': 'Steinberg',
  'cubase-13': 'Steinberg',
  'fl-studio': 'Image-Line',
  'fl-studio-21': 'Image-Line',
  'garageband': 'Apple',
  'logic-pro': 'Apple',
  'logic-pro-x': 'Apple',
  'pro-tools': 'Avid',
  'reaper': 'Cockos',
  'reason-studios': 'Reason Studios',
  'studio-one': 'PreSonus',
  'serum': 'Xfer Records',
  'serum-2': 'Xfer Records',
  'vital': 'Matt Tytel',
  'omnisphere': 'Spectrasonics',
  'omnisphere-2': 'Spectrasonics',
  'sylenth1': 'LennarDigital',
  'kontakt': 'Native Instruments',
  'kontakt-7': 'Native Instruments',
  'massive': 'Native Instruments',
  'massive-x': 'Native Instruments',
  'fabfilter-pro-q-3': 'FabFilter',
  'fabfilter-pro-q3': 'FabFilter',
  'fabfilter-pro-l-2': 'FabFilter',
  'fabfilter-pro-c-2': 'FabFilter',
  'izotope-ozone-11': 'iZotope',
  'izotope-rx-11': 'iZotope',
  'izotope-neutron-4': 'iZotope',
  'soundtoys-5': 'Soundtoys',
  'valhalla-vintage-verb': 'Valhalla DSP',
  'valhalla-room': 'Valhalla DSP',
  'auto-tune-pro': 'Antares',
  'melodyne': 'Celemony',
  'addictive-drums-2': 'XLN Audio',
  'superior-drummer-3': 'Toontrack',
  'arturia-spark': 'Arturia',
}

// Known-brand prefix mapping: if a product name starts with one of these
// strings (case-insensitive, word-boundary), use the canonical developer name.
// Keep this list short — only brands where the prefix is unambiguous.
const BRAND_PREFIXES = [
  ['ableton ', 'Ableton'],
  ['arturia ', 'Arturia'],
  ['bitwig ', 'Bitwig'],
  ['cherry audio ', 'Cherry Audio'],
  ['d16 group ', 'D16 Group'],
  ['d16 ', 'D16 Group'],
  ['elektron ', 'Elektron'],
  ['eventide ', 'Eventide'],
  ['fabfilter ', 'FabFilter'],
  ['ik multimedia ', 'IK Multimedia'],
  ['image-line ', 'Image-Line'],
  ['image line ', 'Image-Line'],
  ['izotope ', 'iZotope'],
  ['kilohearts ', 'Kilohearts'],
  ['korg ', 'Korg'],
  ['lennardigital ', 'LennarDigital'],
  ['matt tytel ', 'Matt Tytel'],
  ['moog ', 'Moog'],
  ['native instruments ', 'Native Instruments'],
  ['newfangled audio ', 'Newfangled Audio'],
  ['oeksound ', 'Oeksound'],
  ['plugin alliance ', 'Plugin Alliance'],
  ['presonus ', 'PreSonus'],
  ['reason studios ', 'Reason Studios'],
  ['roland ', 'Roland'],
  ['sequential ', 'Sequential'],
  ['slate digital ', 'Slate Digital'],
  ['softube ', 'Softube'],
  ['soundtoys ', 'Soundtoys'],
  ['spectrasonics ', 'Spectrasonics'],
  ['steinberg ', 'Steinberg'],
  ['surge synth team ', 'Surge Synth Team'],
  ['tal software ', 'TAL Software'],
  ['toontrack ', 'Toontrack'],
  ['u-he ', 'u-he'],
  ['universal audio ', 'Universal Audio'],
  ['valhalla ', 'Valhalla DSP'],
  ['waves ', 'Waves'],
  ['xfer records ', 'Xfer Records'],
  ['xfer ', 'Xfer Records'],
  ['xln audio ', 'XLN Audio'],
]

function inferFromName(name) {
  const n = (name || '').toLowerCase()
  for (const [prefix, brand] of BRAND_PREFIXES) {
    if (n.startsWith(prefix)) return brand
  }
  return null
}

function main() {
  const raw = fs.readFileSync(PRODUCTS_PATH, 'utf-8')
  const products = JSON.parse(raw)

  let overridden = 0
  let inferred = 0
  let stillEmpty = 0

  for (const p of products) {
    const currentDev = (p.developer || '').trim()
    if (currentDev) continue // already populated; leave alone

    if (SLUG_OVERRIDES[p.slug]) {
      p.developer = SLUG_OVERRIDES[p.slug]
      overridden += 1
      continue
    }

    const inferredDev = inferFromName(p.name)
    if (inferredDev) {
      p.developer = inferredDev
      inferred += 1
      continue
    }

    stillEmpty += 1
  }

  fs.writeFileSync(PRODUCTS_PATH, JSON.stringify(products, null, 2) + '\n', 'utf-8')

  console.log(`backfill-developers: total=${products.length} overridden=${overridden} inferred=${inferred} still_empty=${stillEmpty}`)
}

main()
