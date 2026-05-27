import type { Metadata } from 'next'
import Link from 'next/link'
import { BookOpen, ArrowUpRight } from 'lucide-react'

export const metadata: Metadata = {
  title: 'Guides & Tutorials',
  description: 'Learn about DAWs, synthesizers, plugins, and music production. In-depth guides, tutorials, and comparisons for music producers of all levels.',
  alternates: { canonical: '/guides' },
  openGraph: {
    title: 'Guides & Tutorials — Audio Software Hub',
    description: 'Learn about DAWs, synthesizers, plugins, and music production.',
  },
}

const guides = [
  {
    title: 'What is a DAW? The Ultimate Guide to Digital Audio Workstations',
    slug: 'what-is-a-daw',
    description: 'Everything you need to know about DAWs — what they are, how they work, and how to choose the right one for your music production needs.',
    category: 'DAWs',
    readTime: '12 min',
  },
  {
    title: 'Best Free Serum Presets — 15 Must-Have Sound Packs for 2026',
    slug: 'best-free-serum-presets',
    description: 'Discover the best free Serum presets packs for every genre. From cinematic textures to basses, leads, and pads — all completely free.',
    category: 'Synthesizers',
    readTime: '10 min',
  },
  {
    title: "How to Make Synth Sounds: A Beginner's Guide to Synthesis",
    slug: 'how-to-make-synth-sounds',
    description: 'Learn the fundamentals of synthesis — subtractive, FM, wavetable, and more. Start creating your own synth sounds from scratch.',
    category: 'Synthesizers',
    readTime: '15 min',
  },
  {
    title: 'Best DAW for Hip Hop Production in 2026',
    slug: 'best-daw-for-hip-hop',
    description: 'Find the perfect DAW for making hip hop beats. Compare features, workflow, and pricing for FL Studio, Ableton Live, Logic Pro, and more.',
    category: 'DAWs',
    readTime: '10 min',
  },
  {
    title: 'Best DAW for Electronic Music Production in 2026',
    slug: 'best-daw-for-electronic-music',
    description: 'Which DAW is best for electronic music? We compare Ableton Live, Bitwig Studio, FL Studio, and more for techno, house, ambient, and EDM.',
    category: 'DAWs',
    readTime: '11 min',
  },
  {
    title: 'Music Production Workflow: 10 Tips to Make Better Music Faster',
    slug: 'music-production-workflow',
    description: 'Streamline your music production workflow with these proven tips. From template setups to mixing strategies, produce better music in less time.',
    category: 'Music Production',
    readTime: '13 min',
  },  {
    title: "Best Free VST Plugins 2026 — 20 Essential Free Audio Plugins",
    slug: "best-free-vst-plugins",
    description: "Build a professional plugin collection at zero cost. From synths and reverb to compression and mastering tools — the essential free VST plugins for every producer.",
    category: "Effects & Processing",
    readTime: "14 min",
  },
  {
    title: "Mixing vs. Mastering: A Beginner’s Guide to Audio Post-Production",
    slug: "mixing-vs-mastering",
    description: "Understand the difference between mixing and mastering. Learn the workflows, essential tools, and production chain for professional-sounding releases.",
    category: "Mixing & Mastering",
    readTime: "11 min",
  },
  {
    title: "Best Drum Machines & VST Drum Plugins 2026",
    slug: "best-drum-vst-plugins",
    description: "The best drum VST plugins and software drum machines for hip-hop, electronic, and acoustic production. Compare features, pricing, and find your perfect drum tool.",
    category: "Drum Machines",
    readTime: "14 min",
  },

]

const pageSchema = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://audiosoftwarehub.online' },
        { '@type': 'ListItem', position: 2, name: 'Guides', item: 'https://audiosoftwarehub.online/guides' },
      ],
    },
    {
      '@type': 'CollectionPage',
      name: 'Guides & Tutorials — Audio Software Hub',
      description: 'Learn about DAWs, synthesizers, plugins, and music production.',
      url: 'https://audiosoftwarehub.online/guides',
    },
  ],
}

export default function GuidesPage() {
  return (
    <div className="min-h-screen">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(pageSchema) }}
      />
      {/* Header */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-12">
        <div className="mb-8 flex items-center gap-2 text-[10px] font-bold uppercase tracking-[0.2em]">
          <Link href="/" className="text-white/40 hover:text-white transition-colors">Home</Link>
          <span className="text-white/20">/</span>
          <span className="text-white/60">Guides</span>
        </div>
        <div className="max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 mb-6 border border-white/20 rounded-full">
            <BookOpen className="w-3 h-3 text-white/60" />
            <span className="text-[10px] uppercase tracking-widest text-white/60">Library</span>
          </div>
          <h1 className="text-5xl md:text-6xl font-bold uppercase tracking-tighter font-display text-white mb-4">
            Guides & Tutorials
          </h1>
          <p className="text-white/50 text-lg font-light leading-relaxed">
            Learn about music production software, compare tools, and discover tips to improve your workflow. Each guide is built with real product data from our catalog.
          </p>
        </div>
      </div>

      {/* Guide list */}
      <div className="px-6 md:px-20 lg:px-40 py-16">
        <div className="grid grid-cols-1 gap-px bg-white/10">
          {guides.map((guide, i) => (
            <Link
              key={guide.slug}
              href={`/guides/${guide.slug}`}
              className="group block bg-black border border-white/10 hover:border-white/30 transition-all p-8 md:p-10"
            >
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div className="flex-1">
                  <div className="flex flex-wrap items-center gap-3 mb-3">
                    <span className="text-[10px] font-bold uppercase tracking-widest text-white/40">
                      {String(i + 1).padStart(2, '0')}
                    </span>
                    <span className="text-[10px] px-2 py-0.5 border border-white/20 text-white/50 uppercase tracking-widest">
                      {guide.category}
                    </span>
                    <span className="text-[10px uppercase tracking-widest] text-white/30">{guide.readTime}</span>
                  </div>
                  <h2 className="text-2xl md:text-3xl font-light tracking-tight font-display text-white group-hover:text-white/80 transition-colors mb-3">
                    {guide.title}
                  </h2>
                  <p className="text-white/50 leading-relaxed max-w-2xl text-sm">
                    {guide.description}
                  </p>
                </div>
                <div className="flex items-center gap-6 shrink-0">
                  <ArrowUpRight className="w-5 h-5 text-white/20 group-hover:text-white/60 transition-colors" />
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}
