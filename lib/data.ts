import productsJson from '../data/products.json'
import fs from 'fs'
import path from 'path'

export type PriceType = 'free' | 'freemium' | 'one-time' | 'subscription'

export interface Category {
  id: string
  name: string
  slug: string
  description: string
  icon: string
  color: string
  gradient: string
}

export interface Brand {
  id: string
  name: string
  slug: string
  website: string
}

export interface Product {
  id: string
  name: string
  slug: string
  brandId?: string
  developer?: string
  categoryId: string
  shortDescription: string
  longDescription?: string
  price: number | null
  priceType: PriceType
  officialUrl: string
  rating: number
  ratingCount: number
  os: string[]
  formats: string[]
  features: string[]
  pros: string[]
  cons: string[]
  targetAudience?: string
  isFeatured: boolean
  isNew: boolean
  tags: string[]
}

export const categories: Category[] = [
  {
    id: 'daw',
    name: 'DAWs',
    slug: 'daws',
    description: 'Digital Audio Workstations — the core of any music production setup.',
    icon: '🎛️',
    color: 'violet',
    gradient: 'from-violet-600 to-purple-700',
  },
  {
    id: 'synth',
    name: 'Synthesizers',
    slug: 'synthesizers',
    description: 'Software synthesizers for electronic sound design and composition.',
    icon: '🎹',
    color: 'pink',
    gradient: 'from-pink-600 to-rose-700',
  },
  {
    id: 'effects',
    name: 'Effects & Processing',
    slug: 'effects',
    description: 'EQs, compressors, reverbs, delays, and creative FX plugins.',
    icon: '⚡',
    color: 'cyan',
    gradient: 'from-cyan-600 to-teal-700',
  },
  {
    id: 'sampler',
    name: 'Samplers & Libraries',
    slug: 'samplers',
    description: 'Sample players, virtual instruments, and professional sound libraries.',
    icon: '🎼',
    color: 'amber',
    gradient: 'from-amber-600 to-orange-700',
  },
  {
    id: 'drums',
    name: 'Drum Machines',
    slug: 'drum-machines',
    description: 'Virtual drum kits, beat production tools, and rhythm plugins.',
    icon: '🥁',
    color: 'red',
    gradient: 'from-red-600 to-orange-700',
  },
  {
    id: 'mastering',
    name: 'Mixing & Mastering',
    slug: 'mixing-mastering',
    description: 'Tools for professional mixing, mastering, and loudness optimization.',
    icon: '🎚️',
    color: 'emerald',
    gradient: 'from-emerald-600 to-green-700',
  },
  {
    id: 'midi',
    name: 'MIDI & Utilities',
    slug: 'midi-utilities',
    description: 'MIDI processors, chord generators, pitch tools, and production utilities.',
    icon: '🔧',
    color: 'blue',
    gradient: 'from-blue-600 to-indigo-700',
  },
  {
    id: 'guitar',
    name: 'Guitar & Bass',
    slug: 'guitar-bass',
    description: 'Amp simulators, guitar effects, and bass processing plugins.',
    icon: '🎸',
    color: 'orange',
    gradient: 'from-orange-600 to-red-700',
  },
  {
    id: 'utility',
    name: 'Analysis & Utility',
    slug: 'analysis-utility',
    description: 'Metering, spectrum analyzers, audio repair, and production tools.',
    icon: '📊',
    color: 'slate',
    gradient: 'from-slate-600 to-gray-700',
  },
  {
    id: 'experimental',
    name: 'Experimental',
    slug: 'experimental',
    description: 'Modular environments, generative tools, and avant-garde audio software.',
    icon: '🔬',
    color: 'purple',
    gradient: 'from-purple-600 to-violet-700',
  },
  {
    id: 'vocal',
    name: 'Vocal Tools',
    slug: 'vocal-tools',
    description: 'Pitch correction, harmonizers, and vocal processing plugins.',
    icon: '🎤',
    color: 'pink',
    gradient: 'from-fuchsia-600 to-pink-700',
  },
]

export const brands: Brand[] = [
  { id: 'ableton', name: 'Ableton', slug: 'ableton', website: 'https://www.ableton.com' },
  { id: 'image-line', name: 'Image-Line', slug: 'image-line', website: 'https://www.image-line.com' },
  { id: 'apple', name: 'Apple', slug: 'apple', website: 'https://www.apple.com/logic-pro' },
  { id: 'avid', name: 'Avid', slug: 'avid', website: 'https://www.avid.com' },
  { id: 'cockos', name: 'Cockos', slug: 'cockos', website: 'https://www.reaper.fm' },
  { id: 'bitwig', name: 'Bitwig', slug: 'bitwig', website: 'https://www.bitwig.com' },
  { id: 'presonus', name: 'PreSonus', slug: 'presonus', website: 'https://www.presonus.com' },
  { id: 'xfer', name: 'Xfer Records', slug: 'xfer-records', website: 'https://xferrecords.com' },
  { id: 'native-instruments', name: 'Native Instruments', slug: 'native-instruments', website: 'https://www.native-instruments.com' },
  { id: 'spectrasonics', name: 'Spectrasonics', slug: 'spectrasonics', website: 'https://www.spectrasonics.net' },
  { id: 'lennardigital', name: 'LennarDigital', slug: 'lennardigital', website: 'https://www.lennardigital.com' },
  { id: 'fabfilter', name: 'FabFilter', slug: 'fabfilter', website: 'https://www.fabfilter.com' },
  { id: 'izotope', name: 'iZotope', slug: 'izotope', website: 'https://www.izotope.com' },
  { id: 'waves', name: 'Waves', slug: 'waves', website: 'https://www.waves.com' },
  { id: 'soundtoys', name: 'Soundtoys', slug: 'soundtoys', website: 'https://www.soundtoys.com' },
  { id: 'toontrack', name: 'Toontrack', slug: 'toontrack', website: 'https://www.toontrack.com' },
  { id: 'xlnaudio', name: 'XLN Audio', slug: 'xln-audio', website: 'https://www.xlnaudio.com' },
  { id: 'antares', name: 'Antares', slug: 'antares', website: 'https://www.antarestech.com' },
  { id: 'celemony', name: 'Celemony', slug: 'celemony', website: 'https://www.celemony.com' },
  { id: 'kilohearts', name: 'Kilohearts', slug: 'kilohearts', website: 'https://kilohearts.com' },
  { id: 'u-he', name: 'u-he', slug: 'u-he', website: 'https://u-he.com' },
  { id: 'valhalla', name: 'Valhalla DSP', slug: 'valhalla-dsp', website: 'https://valhalladsp.com' },
  { id: 'arturia', name: 'Arturia', slug: 'arturia', website: 'https://www.arturia.com' },
]

// Enhanced hardcoded products (featured, full detail)
const featuredProducts: Product[] = [
  {
    id: 'ableton-live-12',
    name: 'Ableton Live 12',
    slug: 'ableton-live-12',
    brandId: 'ableton',
    categoryId: 'daw',
    shortDescription: 'The industry-standard DAW for electronic music production and live performance.',
    longDescription: 'Ableton Live 12 is the gold standard for electronic music producers and live performers. Its unique Session and Arrangement views give you unparalleled flexibility — sketch ideas in Session View, then arrange them in the timeline. Live 12 introduces MIDI Transformations, new Meld & Drift devices, and deeper MPE support.',
    price: 499,
    priceType: 'one-time',
    officialUrl: 'https://www.ableton.com/en/live/',
    rating: 4.8,
    ratingCount: 12400,
    os: ['Windows', 'macOS'],
    formats: ['Standalone', 'VST3', 'AU'],
    features: ['Session View', 'Arrangement View', 'Max for Live', 'MIDI Transformation', 'MPE Support', '70+ Instruments & Effects'],
    pros: ['Best workflow for electronic music', 'Excellent live performance features', 'Huge Max for Live ecosystem'],
    cons: ['Expensive Suite version', 'Steep learning curve'],
    targetAudience: 'Electronic producers, DJs, live performers',
    isFeatured: true,
    isNew: false,
    tags: ['daw', 'electronic', 'live performance'],
  },
  {
    id: 'fl-studio-21',
    name: 'FL Studio 21',
    slug: 'fl-studio-21',
    brandId: 'image-line',
    categoryId: 'daw',
    shortDescription: "The beat-maker's DAW with lifetime free updates and a best-in-class piano roll.",
    longDescription: "FL Studio 21 is a powerhouse DAW built around pattern-based composition. Image-Line's promise of lifetime free updates makes it one of the best long-term investments. Loved by hip-hop, EDM, and trap producers worldwide.",
    price: 299,
    priceType: 'one-time',
    officialUrl: 'https://www.image-line.com/fl-studio/',
    rating: 4.7,
    ratingCount: 18600,
    os: ['Windows', 'macOS'],
    formats: ['Standalone'],
    features: ['Lifetime Free Updates', 'Best-in-class Piano Roll', 'Pattern-based Workflow', 'Performance Mode'],
    pros: ['Lifetime free updates', 'Excellent piano roll', 'Huge community'],
    cons: ['macOS support historically lagged', 'Less intuitive linear workflow'],
    targetAudience: 'Beat makers, hip-hop and EDM producers',
    isFeatured: true,
    isNew: false,
    tags: ['daw', 'beat making', 'hip-hop', 'trap'],
  },
  {
    id: 'logic-pro',
    name: 'Logic Pro',
    slug: 'logic-pro',
    brandId: 'apple',
    categoryId: 'daw',
    shortDescription: "Apple's professional DAW — the best value in music production software for Mac.",
    longDescription: 'Logic Pro is Apple\'s flagship DAW. At $199.99 one-time, it packs more value than any competitor. Logic 11 introduced AI Session Players, Stem Splitter, and ChromaGlow. Deep Apple Silicon optimization makes it blazingly fast on M-series Macs.',
    price: 199.99,
    priceType: 'one-time',
    officialUrl: 'https://www.apple.com/logic-pro/',
    rating: 4.9,
    ratingCount: 21000,
    os: ['macOS'],
    formats: ['Standalone', 'AU'],
    features: ['Session Players (AI)', 'Stem Splitter', 'Dolby Atmos', 'Flex Time & Pitch', '6000+ Apple Loops'],
    pros: ['Incredible value at $199', 'Best-in-class built-in plugins', 'Superb Apple Silicon performance'],
    cons: ['macOS only', 'Less portable ecosystem'],
    targetAudience: 'Mac-based producers across all genres',
    isFeatured: true,
    isNew: false,
    tags: ['daw', 'mac', 'apple', 'professional'],
  },
  {
    id: 'serum',
    name: 'Serum',
    slug: 'serum',
    brandId: 'xfer',
    categoryId: 'synth',
    shortDescription: 'The most popular wavetable synthesizer — the go-to for modern EDM sound design.',
    longDescription: "Xfer Records Serum is the definitive wavetable synthesizer and one of the best-selling plugins of all time. Its drag-and-drop wavetable editor, pristine audio quality, and intuitive interface made it the standard for modern electronic music production.",
    price: 9.99,
    priceType: 'subscription',
    officialUrl: 'https://xferrecords.com/products/serum',
    rating: 4.9,
    ratingCount: 28000,
    os: ['Windows', 'macOS'],
    formats: ['VST', 'VST3', 'AU', 'AAX'],
    features: ['Wavetable Editor', 'Drag & Drop Modulation', 'Visual LFO', 'Built-in FX Chain'],
    pros: ['Industry-standard sound quality', 'Incredibly intuitive', 'Massive preset library'],
    cons: ['Subscription model', 'CPU intensive'],
    targetAudience: 'EDM, dubstep, pop, trap producers',
    isFeatured: true,
    isNew: false,
    tags: ['synth', 'wavetable', 'edm', 'bestseller'],
  },
  {
    id: 'vital',
    name: 'Vital',
    slug: 'vital',
    brandId: 'kilohearts',
    categoryId: 'synth',
    shortDescription: 'A free, powerful spectral wavetable synth — arguably the best free plugin ever made.',
    longDescription: 'Vital is a stunning spectral warping wavetable synthesizer available for free. Its spectral warping, formant shifting, and advanced modulation system are remarkable. Rivals paid synths in quality.',
    price: 0,
    priceType: 'freemium',
    officialUrl: 'https://vital.audio/',
    rating: 4.8,
    ratingCount: 15400,
    os: ['Windows', 'macOS', 'Linux'],
    formats: ['VST', 'VST3', 'AU', 'LV2'],
    features: ['Spectral Warping', 'Formant Shifting', 'Visual Modulation', '3 Wavetable Oscillators'],
    pros: ['Free base version is exceptional', 'Rivals paid synths', 'Linux support'],
    cons: ['Preset sharing requires account', 'Paid tiers for more presets'],
    targetAudience: 'All producers, especially budget-conscious',
    isFeatured: true,
    isNew: false,
    tags: ['synth', 'wavetable', 'free', 'spectral'],
  },
  {
    id: 'fabfilter-pro-q3',
    name: 'FabFilter Pro-Q 3',
    slug: 'fabfilter-pro-q3',
    brandId: 'fabfilter',
    categoryId: 'effects',
    shortDescription: 'The industry-standard EQ plugin — surgical precision with a beautiful interface.',
    longDescription: 'FabFilter Pro-Q 3 is universally regarded as the finest EQ plugin available. Up to 24 bands, dynamic EQ, zero-latency linear phase, Mid/Side mode, and spectrum collaboration between instances.',
    price: 179,
    priceType: 'one-time',
    officialUrl: 'https://www.fabfilter.com/products/pro-q-3-equalizer-plug-in',
    rating: 4.9,
    ratingCount: 19500,
    os: ['Windows', 'macOS'],
    formats: ['VST', 'VST3', 'AU', 'AAX'],
    features: ['Up to 24 Bands', 'Dynamic EQ', 'Linear Phase', 'Mid/Side Mode', 'Spectrum Analyzer'],
    pros: ['Best EQ on the market', 'Dynamic EQ built in', 'Spectrum instance collaboration'],
    cons: ['Expensive for a single plugin'],
    targetAudience: 'Mix engineers, mastering engineers, producers',
    isFeatured: true,
    isNew: false,
    tags: ['eq', 'mixing', 'mastering', 'industry standard'],
  },
  {
    id: 'izotope-ozone-11',
    name: 'iZotope Ozone 11',
    slug: 'izotope-ozone-11',
    brandId: 'izotope',
    categoryId: 'mastering',
    shortDescription: 'The complete AI-powered mastering suite — from EQ to limiter to stem splitting.',
    longDescription: 'iZotope Ozone 11 is the most comprehensive mastering plugin suite available. AI-powered Master Assistant, Stem Splitter, Stabilizer, and every mastering module you need.',
    price: 499,
    priceType: 'one-time',
    officialUrl: 'https://www.izotope.com/en/products/ozone.html',
    rating: 4.7,
    ratingCount: 7800,
    os: ['Windows', 'macOS'],
    formats: ['VST', 'VST3', 'AU', 'AAX'],
    features: ['AI Master Assistant', 'Stem Splitter', 'Dynamic EQ', 'Imager', 'Maximizer'],
    pros: ['Complete mastering solution', 'AI assistance speeds workflow', 'Stem splitter is game-changing'],
    cons: ['Very expensive', 'Heavy on CPU'],
    targetAudience: 'Mastering engineers, producers finishing their own tracks',
    isFeatured: true,
    isNew: true,
    tags: ['mastering', 'ai', 'limiter', 'eq'],
  },
  {
    id: 'kontakt-7',
    name: 'Kontakt 7',
    slug: 'kontakt-7',
    brandId: 'native-instruments',
    categoryId: 'sampler',
    shortDescription: "The world's leading sampler — the standard platform for professional virtual instruments.",
    longDescription: "Native Instruments Kontakt 7 is the industry-standard sampling platform. Thousands of professional instrument libraries are built on it. Kontakt 7 introduces improved wavetable synthesis, better scripting, and a modernized interface.",
    price: 399,
    priceType: 'one-time',
    officialUrl: 'https://www.native-instruments.com/en/products/komplete/samplers/kontakt-7/',
    rating: 4.7,
    ratingCount: 13700,
    os: ['Windows', 'macOS'],
    formats: ['VST', 'VST3', 'AU', 'AAX', 'Standalone'],
    features: ['Huge Library Ecosystem', 'Wavetable Synthesis', 'Script Processor', '50+ Included Instruments'],
    pros: ['Unmatched library ecosystem', 'Industry standard for session work'],
    cons: ['Very expensive', 'Large install size'],
    targetAudience: 'Film composers, session musicians, serious producers',
    isFeatured: true,
    isNew: false,
    tags: ['sampler', 'orchestral', 'professional'],
  },
]

// Merge: featured products take priority, then JSON-imported products
function buildProductList(): Product[] {
  const importedRaw = productsJson as any[]
  const featuredSlugs = new Set(featuredProducts.map(p => p.slug))

  // Remove any imported products that duplicate a featured one (by slug or name)
  const featuredNames = new Set(featuredProducts.map(p => p.name.toLowerCase()))
  const filtered = importedRaw
    .filter(p => !featuredSlugs.has(p.slug) && !featuredNames.has(p.name.toLowerCase()))
    .map(p => ({
      ...p,
      os: p.os ?? p.platforms ?? ['Windows', 'macOS'],
      formats: p.formats ?? ['VST3', 'AU', 'AAX'],
      features: p.features ?? [`Professional ${p.categoryId ?? 'audio'} tool`, `By ${p.developer ?? 'unknown'}`, 'High-quality audio processing'],
      pros: p.pros ?? ['Professional quality', 'Widely used'],
      cons: p.cons ?? ['Check system requirements'],
      tags: p.tags ?? [p.categoryId ?? 'audio'],
      shortDescription: p.shortDescription ?? p.description ?? `${p.name} by ${p.developer ?? 'unknown'}.`,
      longDescription: p.longDescription ?? p.description ?? `${p.name} is a professional ${p.categoryId ?? 'audio'} tool by ${p.developer ?? 'unknown'}.`,
      targetAudience: p.targetAudience ?? 'Music producers and audio engineers',
      isFeatured: p.isFeatured ?? p.featured ?? false,
      isNew: p.isNew ?? false,
      categoryId: p.categoryId ?? p.category ?? 'utility',
      price: typeof p.price === 'string' ? parseFloat(p.price) || 0 : (p.price ?? 0),
      officialUrl: p.officialUrl ?? p.url ?? '#',
    } as Product))

  return [...featuredProducts, ...filtered]
}

export const products: Product[] = buildProductList()

// Pre-computed indexes — built once at module load, O(1) lookups at render time
const _bySlug = new Map<string, Product>(products.map(p => [p.slug, p]))
const _byCategory = new Map<string, Product[]>()
const _countByCategory = new Map<string, number>()
const _featured: Product[] = []
const _newReleases: Product[] = []

for (const p of products) {
  // category buckets
  const bucket = _byCategory.get(p.categoryId)
  if (bucket) bucket.push(p)
  else _byCategory.set(p.categoryId, [p])
  // counts
  _countByCategory.set(p.categoryId, (_countByCategory.get(p.categoryId) ?? 0) + 1)
  if (p.isFeatured) _featured.push(p)
  if (p.isNew) _newReleases.push(p)
}

// Helpers
export function getCategoryById(id: string): Category | undefined {
  return categories.find(c => c.id === id)
}

export function getCategoryBySlug(slug: string): Category | undefined {
  return categories.find(c => c.slug === slug)
}

export function getBrandById(id: string): Brand | undefined {
  return brands.find(b => b.id === id)
}

export function getProductBySlug(slug: string): Product | undefined {
  return _bySlug.get(slug)
}

export function getProductsByCategory(categoryId: string): Product[] {
  return _byCategory.get(categoryId) ?? []
}

export function getFeaturedProducts(): Product[] {
  return _featured
}

export type SanitizedRelease = Product & { dateAdded?: string; sourceTitle?: string }

const RELEASE_JUNK_PATTERN = /\[menu\]|menuhttps?|menuhttp|close-menu/i

function isSafeReleaseField(value: unknown): value is string {
  return typeof value === 'string' && value.trim().length > 0 && !RELEASE_JUNK_PATTERN.test(value)
}

function toSafeStringArray(value: unknown, fallback: string[]): string[] {
  if (!Array.isArray(value)) return fallback
  const cleaned = value
    .filter((item): item is string => typeof item === 'string')
    .map(item => item.trim())
    .filter(item => item.length > 0 && !RELEASE_JUNK_PATTERN.test(item))
  return cleaned.length > 0 ? cleaned : fallback
}

function toSafePriceType(value: unknown): PriceType {
  return value === 'free' || value === 'freemium' || value === 'subscription' || value === 'one-time'
    ? value
    : 'one-time'
}

function sanitizeReleaseEntry(entry: any): SanitizedRelease | null {
  if (!entry || typeof entry !== 'object') return null
  if (!isSafeReleaseField(entry.slug) || !isSafeReleaseField(entry.name)) return null
  if (!isSafeReleaseField(entry.shortDescription ?? `${entry.name} — recently released.`)) return null
  if (!isSafeReleaseField(entry.officialUrl ?? '#')) return null

  const safeName = entry.name.trim()
  return {
    id: (typeof entry.id === 'string' && entry.id.trim().length > 0 ? entry.id : entry.slug).trim(),
    slug: entry.slug.trim(),
    name: safeName,
    developer: isSafeReleaseField(entry.developer) ? entry.developer.trim() : undefined,
    categoryId: typeof entry.categoryId === 'string' && entry.categoryId.trim().length > 0 ? entry.categoryId : 'utility',
    price: typeof entry.price === 'number' ? entry.price : 0,
    priceType: toSafePriceType(entry.priceType),
    shortDescription: (entry.shortDescription ?? `${safeName} — recently released.`).trim(),
    longDescription: typeof entry.longDescription === 'string'
      ? entry.longDescription.trim()
      : (entry.shortDescription ?? '').trim(),
    officialUrl: (entry.officialUrl ?? '#').trim(),
    rating: typeof entry.rating === 'number' ? entry.rating : 4.0,
    ratingCount: typeof entry.ratingCount === 'number' ? entry.ratingCount : 0,
    isNew: true,
    isFeatured: false,
    os: toSafeStringArray(entry.os, ['Windows', 'macOS']),
    formats: toSafeStringArray(entry.formats, []),
    features: toSafeStringArray(entry.features, ['New release']),
    pros: toSafeStringArray(entry.pros, ['Recently released']),
    cons: toSafeStringArray(entry.cons, ['New - limited reviews']),
    tags: toSafeStringArray(entry.tags, [entry.categoryId ?? 'audio']),
    targetAudience: typeof entry.targetAudience === 'string' && entry.targetAudience.trim().length > 0
      ? entry.targetAudience.trim()
      : 'Music producers and audio engineers',
    dateAdded: typeof entry.dateAdded === 'string' ? entry.dateAdded : undefined,
    sourceTitle: typeof entry.sourceTitle === 'string' ? entry.sourceTitle : undefined,
  }
}

export function getSanitizedReleases(): SanitizedRelease[] {
  try {
    const releasesPath = path.join(process.cwd(), 'data', 'releases.json')
    const raw = fs.readFileSync(releasesPath, 'utf-8')
    const scraped: any[] = JSON.parse(raw)
    if (!Array.isArray(scraped) || scraped.length === 0) return []

    const sanitized = scraped
      .map(sanitizeReleaseEntry)
      .filter((entry): entry is SanitizedRelease => entry !== null)

    return sanitized
  } catch {
    return []
  }
}

export function getNewProducts(): Product[] {
  const sanitized = getSanitizedReleases()
  return sanitized.length > 0 ? sanitized : _newReleases
}

export function searchProducts(query: string): Product[] {
  const q = query.toLowerCase()
  return products.filter(p =>
    p.name.toLowerCase().includes(q) ||
    p.shortDescription.toLowerCase().includes(q) ||
    p.tags.some(t => t.includes(q)) ||
    getCategoryById(p.categoryId)?.name.toLowerCase().includes(q) ||
    (p.developer ?? getBrandById(p.brandId ?? '')?.name ?? '').toLowerCase().includes(q)
  )
}

export function getProductCount(categoryId: string): number {
  return _countByCategory.get(categoryId) ?? 0
}

export function getProductDeveloper(product: Product): string {
  if (product.developer) return product.developer
  if (product.brandId) return getBrandById(product.brandId)?.name ?? ''
  return ''
}
