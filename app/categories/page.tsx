import Link from 'next/link'
import { ArrowUpRight, Monitor, Waves, SlidersHorizontal, Library, Drum, Gauge, Cable, Mic, Guitar, Wrench, Sparkles } from 'lucide-react'
import { categories, getProductCount } from '@/lib/data'

// Map category IDs to Lucide icons
const categoryIcons: Record<string, any> = {
  daw: Monitor,
  synth: Waves,
  effects: SlidersHorizontal,
  sampler: Library,
  drums: Drum,
  mastering: Gauge,
  midi: Cable,
  vocal: Mic,
  guitar: Guitar,
  utility: Wrench,
  experimental: Sparkles,
}

export const metadata = {
  title: 'Categories — Audio Software Hub',
  description: 'Browse all music production tool categories.',
}

export default function CategoriesPage() {
  return (
    <div className="min-h-screen">
      <div className="px-6 md:px-20 lg:px-40 py-12">
        {/* Header */}
        <div className="mb-16">
          <div className="flex items-baseline gap-4 mb-2">
            <span className="text-xs font-bold tracking-[0.3em] text-white/40 uppercase">Directory / 2026</span>
          </div>
          <h1 className="text-6xl md:text-8xl font-bold leading-none tracking-tighter uppercase font-display">Categories</h1>
          <div className="mt-4 max-w-xl">
            <p className="text-white/60 text-lg font-light leading-relaxed">
              A curated technical archive of professional audio production tools, digital workstations, and signal processing software.
            </p>
          </div>
        </div>

        {/* Grid — numbered cells with thin borders */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 border-t border-l border-white/20">
          {categories.map((cat, i) => {
            const count = getProductCount(cat.id)
            const Icon = categoryIcons[cat.id] ?? Wrench
            const num = String(i + 1).padStart(2, '0')
            return (
              <Link
                key={cat.slug}
                href={`/categories/${cat.slug}`}
                className="group flex flex-col p-8 border-r border-b border-white/20 hover:bg-white/5 transition-colors cursor-pointer min-h-[240px]"
              >
                <div className="flex justify-between items-start mb-12">
                  <span className="text-xs font-bold tracking-widest text-white/40">{num} /</span>
                  <Icon className="w-5 h-5 text-white/80" />
                </div>
                <div className="mt-auto">
                  <h3 className="text-white text-xl font-bold tracking-tight mb-1 uppercase font-display">{cat.name}</h3>
                  <p className="text-white/40 text-xs font-bold tracking-widest">{count} TOOLS AVAILABLE</p>
                </div>
              </Link>
            )
          })}
        </div>
      </div>
    </div>
  )
}
