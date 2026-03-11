export const dynamic = 'force-dynamic'

import Link from 'next/link'
import {
  Search, ArrowRight, ArrowUpRight,
  Monitor, Waves, SlidersHorizontal, Library, Drum, Gauge, Cable, Mic, Guitar, Wrench, Sparkles, Zap,
} from 'lucide-react'
import { categories, getFeaturedProducts, getNewProducts, getProductCount } from '@/lib/data'
import { formatPrice, formatRating } from '@/lib/utils'
import { ProductCard } from '@/components/ProductCard'

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

export default function HomePage() {
  const featured = getFeaturedProducts()
  const newReleases = getNewProducts()

  return (
    <div className="relative">
      {/* ── Hero ── */}
      <section className="relative overflow-hidden pt-32 pb-40 px-6 border-b border-white/5">
        <div className="max-w-7xl mx-auto relative z-10">
          <div className="inline-block px-3 py-1 mb-8 border border-white/20 rounded-full text-[10px] uppercase tracking-widest text-white/60">
            The definitive music production software directory
          </div>

          <h1 className="text-6xl md:text-8xl font-light tracking-tight mb-12 leading-[1.1] font-display">
            Find the audio tool<br />
            <span className="italic font-normal">you need today</span>
          </h1>

          <p className="max-w-2xl text-xl text-white/50 font-light mb-16 leading-relaxed">
            Discover, compare, and learn about the best DAWs, synthesizers, plugins, and music production tools — all in one place.
          </p>

          {/* Search Bar */}
          <form action="/search" method="GET" className="max-w-3xl">
            <div className="flex items-center p-2 bg-white/5 border border-white/10">
              <Search className="w-4 h-4 text-white/30 ml-4 shrink-0" />
              <input
                name="q"
                type="text"
                placeholder="Search DAWs, synths, effects, plugins..."
                className="flex-1 bg-transparent border-none focus:ring-0 text-white placeholder:text-white/20 px-4 py-4 outline-none text-sm"
              />
              <button
                type="submit"
                className="bg-white text-black px-8 py-4 font-semibold hover:bg-zinc-200 transition-colors text-sm cursor-pointer"
              >
                Search
              </button>
            </div>
          </form>

          {/* Quick Filters */}
          <div className="mt-12 flex flex-wrap gap-3">
            {categories.slice(0, 7).map(cat => (
              <Link
                key={cat.slug}
                href={`/categories/${cat.slug}`}
                className="px-4 py-1.5 border border-white/10 rounded-full text-xs text-white/40 hover:border-white/30 hover:text-white/60 transition-all cursor-pointer"
              >
                # {cat.name}
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* ── Stats Bar ── */}
      <section className="py-12 border-b border-white/5 px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
          <div className="text-center md:text-left">
            <div className="text-4xl font-light mb-1 font-display">3,000+</div>
            <div className="text-[10px] uppercase tracking-[0.2em] text-white/40">Professional Music Tools Catalogued</div>
          </div>
          <div className="hidden md:block h-12 w-[1px] bg-white/10" />
          <div className="text-center md:text-left">
            <div className="text-4xl font-light mb-1 font-display">150+</div>
            <div className="text-[10px] uppercase tracking-[0.2em] text-white/40">Top Tier Manufacturers</div>
          </div>
          <div className="hidden md:block h-12 w-[1px] bg-white/10" />
          <div className="text-center md:text-left">
            <div className="text-4xl font-light mb-1 font-display">24/7</div>
            <div className="text-[10px] uppercase tracking-[0.2em] text-white/40">Real-time Updates</div>
          </div>
        </div>
      </section>

      {/* ── Featured Products ── */}
      <section className="py-32 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="flex items-end justify-between mb-20">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <span className="w-2 h-2 rounded-full bg-white" />
                <span className="text-[10px] uppercase tracking-widest text-white/60">Featured Selection</span>
              </div>
              <h2 className="text-5xl font-light tracking-tight font-display">Top Picks</h2>
            </div>
            <Link
              href="/categories"
              className="group text-sm flex items-center gap-2 text-white/40 hover:text-white transition-all"
            >
              Browse All
              <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </Link>
          </div>

          {/* Featured grid — boutique card style */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 divide-x divide-y divide-white/10 border border-white/10">
            {featured.slice(0, 4).map(product => {
              const developer = product.developer ?? 'Unknown'
              return (
                <div key={product.id} className="group p-8 bg-black hover:bg-white/[0.02] transition-colors cursor-pointer">
                  <div className="flex justify-between items-start mb-12">
                    <div className="w-16 h-16 border border-white/20 flex items-center justify-center">
                      <span className="text-white/30 text-2xl font-display font-bold">{product.name.charAt(0)}</span>
                    </div>
                    <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/40 italic">
                      {product.priceType === 'free' ? 'Free' : product.priceType === 'subscription' ? 'Sub' : 'One-Time'}
                    </span>
                  </div>
                  <div className="space-y-4">
                    <div className="flex justify-between items-center">
                      <span className="text-[10px] uppercase tracking-widest text-white/40">{developer}</span>
                      <span className="flex items-center gap-1 text-[10px] text-white">&#9733; {formatRating(product.rating)}</span>
                    </div>
                    <Link href={`/products/${product.slug}`} className="block">
                      <h3 className="text-2xl font-medium tracking-tight font-display hover:text-white/80 transition-colors">{product.name}</h3>
                    </Link>
                    <p className="text-sm text-white/40 leading-relaxed min-h-[4rem] line-clamp-3">{product.shortDescription}</p>
                    <div className="pt-8 flex justify-between items-center border-t border-white/5">
                      <span className="text-lg font-light">{formatPrice(product.price, product.priceType)}</span>
                      <Link
                        href={`/products/${product.slug}`}
                        className="px-6 py-2 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors"
                      >
                        Details
                      </Link>
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
        </div>
      </section>

      {/* ── New Releases ── */}
      <section className="py-32 px-6 border-t border-white/5">
        <div className="max-w-7xl mx-auto">
          <div className="flex items-end justify-between mb-20">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <span className="w-2 h-2 rounded-full bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.4)]" />
                <span className="text-[10px] uppercase tracking-widest text-white/60">Updated every 24–48h</span>
              </div>
              <h2 className="text-5xl font-light tracking-tight font-display">New Releases</h2>
            </div>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {newReleases.map(product => (
              <ProductCard key={product.id} product={product} detailHref={`/releases/${product.slug}`} />
            ))}
          </div>
        </div>
      </section>

      {/* ── Categories ── */}
      <section className="py-32 px-6">
        <div className="max-w-7xl mx-auto">
          <div className="flex items-end justify-between mb-20">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <span className="w-2 h-2 rounded-full border border-white/40" />
                <span className="text-[10px] uppercase tracking-widest text-white/60">Directory</span>
              </div>
              <h2 className="text-5xl font-light tracking-tight font-display">All Categories</h2>
            </div>
            <Link href="/categories" className="text-sm text-white/40 hover:text-white transition-all underline underline-offset-8 decoration-white/10">
              View All
            </Link>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {categories.map(cat => {
              const count = getProductCount(cat.id)
              const Icon = categoryIcons[cat.id] ?? Wrench
              return (
                <Link
                  key={cat.slug}
                  href={`/categories/${cat.slug}`}
                  className="group flex flex-col justify-between p-8 border border-white/10 hover:border-white/40 transition-all h-64 cursor-pointer"
                >
                  <div className="flex justify-between items-start">
                    <Icon className="w-10 h-10 text-white/70" />
                    <ArrowUpRight className="w-5 h-5 opacity-0 group-hover:opacity-100 transition-opacity text-white/60" />
                  </div>
                  <div>
                    <h3 className="text-2xl font-light mb-2 font-display">{cat.name}</h3>
                    <p className="text-[10px] uppercase tracking-widest text-white/30">{count.toLocaleString()} tools</p>
                  </div>
                </Link>
              )
            })}
          </div>
        </div>
      </section>

      {/* ── CTA Banner ── */}
      <section className="py-40 px-6 border-y border-white/5 overflow-hidden relative">
        <div className="absolute inset-0 flex items-center justify-center opacity-[0.03] pointer-events-none">
          <div className="text-[300px] font-bold tracking-tighter select-none font-display">AUDIO</div>
        </div>
        <div className="max-w-3xl mx-auto text-center relative z-10">
          <h2 className="text-5xl md:text-6xl font-light tracking-tight mb-8 font-display">Ready to build? Find your next essential tool</h2>
          <p className="text-white/40 text-lg mb-12 font-light">Browse 3,000+ professional music production plugins, DAWs, and instruments across every category and price range.</p>
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              href="/categories"
              className="w-full sm:w-auto px-10 py-5 bg-white text-black font-bold text-sm rounded-full hover:bg-zinc-200 transition-all uppercase tracking-widest cursor-pointer text-center"
            >
              Browse Categories
            </Link>
            <Link
              href="/search"
              className="w-full sm:w-auto px-10 py-5 border border-white/20 text-white font-bold text-sm rounded-full hover:bg-white/5 transition-all uppercase tracking-widest cursor-pointer text-center"
            >
              Search Tools
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}
