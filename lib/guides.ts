export interface Guide {
  id: string
  slug: string
  title: string
  description: string
  category: 'Best Of & Roundups' | 'Comparisons' | 'Workflow' | 'Industry Trends'
  contentType: 'Hub & Spoke' | 'Use-Case' | 'Thought Leadership' | 'Listicle' | 'Product Comparison' | 'Alternatives' | 'Platform Comparison' | 'Tutorial' | 'Expert Roundup' | 'Educational Hub' | 'Data-Driven'
  buyerStage: 'Awareness' | 'Consideration' | 'Decision' | 'Implementation' | 'Awareness/Decision'
  targetKeywords: string[]
  datePublished?: string
  lastUpdated?: string
  readingTime?: number
  featuredImage?: string
  featured: boolean
}

export const guides: Guide[] = [
  {
    id: 'ultimate-guide-free-vst-plugins-2026',
    slug: 'the-ultimate-guide-to-free-vst-plugins-2026-edition',
    title: 'The Ultimate Guide to Free VST Plugins (2026 Edition)',
    description: 'Discover the best free VST plugins for music production in 2026. From synthesizers to effects, we cover the top free tools that rival paid alternatives.',
    category: 'Best Of & Roundups',
    contentType: 'Hub & Spoke',
    buyerStage: 'Consideration',
    targetKeywords: ['best free vst plugins', 'free synth vsts'],
    datePublished: '2026-01-15',
    lastUpdated: '2026-08-15',
    readingTime: 18,
    featured: true,
  },
  {
    id: 'best-vocal-processing-chains',
    slug: '10-best-vocal-processing-chains-for-bedroom-producers',
    title: '10 Best Vocal Processing Chains for Bedroom Producers',
    description: 'Professional vocal chains on a budget. Learn the exact plugin combinations used by top engineers for radio-ready vocals in home studios.',
    category: 'Best Of & Roundups',
    contentType: 'Use-Case',
    buyerStage: 'Consideration',
    targetKeywords: ['best vocal plugins', 'vocal chain vst'],
    datePublished: '2026-02-01',
    lastUpdated: '2026-08-10',
    readingTime: 15,
    featured: true,
  },
  {
    id: 'analog-emulation-vs-digital-synths',
    slug: 'analog-emulation-vs-digital-synths-what-actually-sounds-better',
    title: 'Analog Emulation vs. Digital Synths: What Actually Sounds Better?',
    description: 'The definitive showdown. We test analog emulations against native digital synths across blind A/B comparisons. The results may surprise you.',
    category: 'Best Of & Roundups',
    contentType: 'Thought Leadership',
    buyerStage: 'Awareness',
    targetKeywords: ['analog vs digital synths', 'best analog vst'],
    datePublished: '2026-02-15',
    lastUpdated: '2026-08-05',
    readingTime: 12,
    featured: true,
  },
  {
    id: 'top-5-mastering-plugins-low-cpu',
    slug: 'the-top-5-mastering-plugins-that-wont-break-your-cpu',
    title: 'The Top 5 Mastering Plugins That Won\'t Break Your CPU',
    description: 'Master your tracks without melting your laptop. Five lightweight mastering suites that deliver pro results on modest systems.',
    category: 'Best Of & Roundups',
    contentType: 'Listicle',
    buyerStage: 'Consideration',
    targetKeywords: ['best mastering plugins', 'low cpu vsts'],
    datePublished: '2026-03-01',
    lastUpdated: '2026-08-01',
    readingTime: 10,
    featured: false,
  },
  {
    id: 'best-lofi-plugins-vintage-tape',
    slug: 'best-lo-fi-plugins-to-get-that-vintage-tape-sound',
    description: 'Get that warm, gritty vintage sound without the hardware hassle. The best lo-fi and tape emulation plugins for instant character.',
    category: 'Best Of & Roundups',
    contentType: 'Genre Use-Case',
    buyerStage: 'Consideration',
    targetKeywords: ['best lofi plugins', 'tape emulation vst'],
    datePublished: '2026-03-15',
    lastUpdated: '2026-07-28',
    readingTime: 11,
    title: 'Best Lo-Fi Plugins to Get That Vintage Tape Sound',
    featured: false,
  },
  {
    id: 'serum-vs-vital-wavetable-synth',
    slug: 'serum-vs-vital-which-wavetable-synth-should-you-learn-first',
    title: 'Serum vs. Vital: Which Wavetable Synth Should You Learn First?',
    description: 'The two titans of wavetable synthesis compared head-to-head. Workflow, sound quality, CPU, presets, and learning curve — everything you need to decide.',
    category: 'Comparisons',
    contentType: 'Product Comparison',
    buyerStage: 'Decision',
    targetKeywords: ['serum vs vital', 'best wavetable synth'],
    datePublished: '2026-04-01',
    lastUpdated: '2026-07-20',
    readingTime: 14,
    featured: true,
  },
  {
    id: 'ableton-vs-fl-studio-electronic',
    slug: 'ableton-live-12-vs-fl-studio-21-for-electronic-music-production',
    title: 'Ableton Live 12 vs. FL Studio 21 for Electronic Music Production',
    description: 'The two most popular DAWs for electronic music, compared across workflow, stock plugins, performance features, and long-term value.',
    category: 'Comparisons',
    contentType: 'Product Comparison',
    buyerStage: 'Decision',
    targetKeywords: ['ableton vs fl studio'],
    datePublished: '2026-04-15',
    lastUpdated: '2026-07-15',
    readingTime: 16,
    featured: true,
  },
  {
    id: 'fabfilter-pro-q3-alternatives',
    slug: 'fabfilter-pro-q-3-alternatives-best-eqs-under-50',
    title: 'FabFilter Pro-Q 3 Alternatives: Best EQs Under $50',
    description: 'Pro-Q 3 is the gold standard, but at $179 it\'s steep. We tested 15 EQs under $50 to find the best budget alternatives for mixing and mastering.',
    category: 'Comparisons',
    contentType: 'Alternatives',
    buyerStage: 'Decision',
    targetKeywords: ['fabfilter pro q 3 alternatives', 'best cheap eq vst'],
    datePublished: '2026-05-01',
    lastUpdated: '2026-07-10',
    readingTime: 13,
    featured: false,
  },
  {
    id: 'splice-vs-loopcloud',
    slug: 'splice-vs-loopcloud-the-ultimate-sample-subscription-showdown',
    title: 'Splice vs. Loopcloud: The Ultimate Sample Subscription Showdown',
    description: 'Two subscription models, one winner. We compare catalogs, pricing, workflow integration, and licensing to help you choose the right sample platform.',
    category: 'Comparisons',
    contentType: 'Platform Comparison',
    buyerStage: 'Decision',
    targetKeywords: ['splice vs loopcloud'],
    datePublished: '2026-05-15',
    lastUpdated: '2026-07-05',
    readingTime: 12,
    featured: false,
  },
  {
    id: 'organize-plugin-folder-creative-flow',
    slug: 'how-to-organize-your-plugin-folder-for-maximum-creative-flow',
    title: 'How to Organize Your Plugin Folder for Maximum Creative Flow',
    description: 'Stop wasting time scrolling. A practical system for organizing VST plugins that speeds up your workflow and reduces decision fatigue.',
    category: 'Workflow',
    contentType: 'Tutorial',
    buyerStage: 'Implementation',
    targetKeywords: ['how to organize vst plugins'],
    datePublished: '2026-06-01',
    lastUpdated: '2026-06-28',
    readingTime: 8,
    featured: false,
  },
  {
    id: '5-plugin-mix-bus-chain',
    slug: 'the-5-plugin-mix-bus-chain-used-by-top-mixing-engineers',
    title: 'The 5-Plugin Mix Bus Chain Used by Top Mixing Engineers',
    description: 'The exact chain, settings, and rationale from Grammy-winning engineers. Build a master-ready mix bus without overprocessing.',
    category: 'Workflow',
    contentType: 'Expert Roundup',
    buyerStage: 'Implementation',
    targetKeywords: ['mix bus plugin chain'],
    datePublished: '2026-06-15',
    lastUpdated: '2026-06-15',
    readingTime: 11,
    featured: true,
  },
  {
    id: 'translating-hardware-synths-software',
    slug: 'translating-hardware-synths-into-software-workflows',
    title: 'Translating Hardware Synths into Software Workflows',
    description: 'Bridge the gap between physical and virtual. Techniques for recreating hardware synth behavior in your DAW using modern plugins.',
    category: 'Workflow',
    contentType: 'Thought Leadership',
    buyerStage: 'Awareness',
    targetKeywords: ['hardware vs software synths workflow'],
    datePublished: '2026-07-01',
    lastUpdated: '2026-07-01',
    readingTime: 14,
    featured: false,
  },
  {
    id: 'beginners-guide-granular-synthesis',
    slug: 'a-beginners-guide-to-granular-synthesis-and-the-3-best-plugins-for-it',
    title: 'A Beginner\'s Guide to Granular Synthesis (And The 3 Best Plugins for It)',
    description: 'Demystify granular synthesis. Learn the core concepts, hear the techniques, and discover the three best plugins to start with today.',
    category: 'Workflow',
    contentType: 'Educational Hub',
    buyerStage: 'Awareness/Decision',
    targetKeywords: ['what is granular synthesis', 'best granular vst'],
    datePublished: '2026-07-15',
    lastUpdated: '2026-07-15',
    readingTime: 10,
    featured: false,
  },
  {
    id: 'audio-software-pricing-2026',
    slug: 'the-state-of-audio-software-pricing-in-2026-subscriptions-vs-perpetual',
    title: 'The State of Audio Software Pricing in 2026: Subscriptions vs. Perpetual Licenses',
    description: 'Data-driven analysis of pricing trends across 200+ plugins. Which models favor the producer, and where the industry is heading.',
    category: 'Industry Trends',
    contentType: 'Data-Driven',
    buyerStage: 'Awareness',
    targetKeywords: ['music software subscription vs perpetual'],
    datePublished: '2026-08-01',
    lastUpdated: '2026-08-01',
    readingTime: 15,
    featured: true,
  },
  {
    id: 'ai-changing-daw-workflows',
    slug: 'how-ai-is-changing-daw-workflows-without-replacing-producers',
    title: 'How AI is Changing DAW Workflows (Without Replacing Producers)',
    description: 'Beyond the hype: practical AI tools that actually speed up music production. Stem separation, MIDI generation, mixing assistance — what works today.',
    category: 'Industry Trends',
    contentType: 'Thought Leadership',
    buyerStage: 'Awareness',
    targetKeywords: ['ai music production plugins'],
    datePublished: '2026-08-15',
    lastUpdated: '2026-08-15',
    readingTime: 13,
    featured: true,
  },
]

export function getGuideBySlug(slug: string): Guide | undefined {
  return guides.find(g => g.slug === slug)
}

export function getGuidesByCategory(category: Guide['category']): Guide[] {
  return guides.filter(g => g.category === category)
}

export function getFeaturedGuides(): Guide[] {
  return guides.filter(g => g.featured)
}

export function getAllGuideSlugs(): string[] {
  return guides.map(g => g.slug)
}