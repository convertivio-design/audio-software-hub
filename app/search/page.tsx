import Link from 'next/link'
import { Search, Package } from 'lucide-react'
import { searchProducts, categories } from '@/lib/data'
import { ProductCard } from '@/components/ProductCard'

export const metadata = {
  title: 'Search — Audio Software Hub',
}

interface Props {
  searchParams: { q?: string }
}

export default function SearchPage({ searchParams }: Props) {
  const query = searchParams.q?.trim() ?? ''
  const results = query ? searchProducts(query) : []

  return (
    <div className="min-h-screen">
      {/* Header */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-12">
        <div className="flex items-baseline gap-4 mb-2">
          <span className="text-xs font-bold tracking-[0.3em] text-white/40 uppercase">System / Search</span>
        </div>
        <h1 className="text-5xl md:text-6xl font-bold leading-none tracking-tighter uppercase font-display mb-8">Search</h1>

        {/* Search form */}
        <form action="/search" method="GET" className="max-w-3xl">
          <div className="flex items-center p-2 bg-white/5 border border-white/10">
            <Search className="w-4 h-4 text-white/30 ml-4 shrink-0" />
            <input
              name="q"
              type="text"
              defaultValue={query}
              placeholder="Search DAWs, synthesizers, effects, plugins..."
              autoFocus
              className="flex-1 bg-transparent border-none focus:ring-0 text-white placeholder:text-white/20 px-4 py-3 text-sm outline-none"
            />
            <button
              type="submit"
              className="px-8 py-3 bg-white text-black text-xs font-bold uppercase tracking-widest hover:bg-zinc-200 transition-colors"
            >
              Search
            </button>
          </div>
        </form>
      </div>

      <div className="px-6 md:px-20 lg:px-40 py-12">
        {/* Results */}
        {query ? (
          <div>
            <p className="text-[10px] font-bold uppercase tracking-widest text-white/40 mb-8">
              {results.length > 0
                ? `${results.length} result${results.length !== 1 ? 's' : ''} for "${query}"`
                : `No results for "${query}"`}
            </p>

            {results.length > 0 ? (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
                {results.map(product => (
                  <ProductCard key={product.id} product={product} />
                ))}
              </div>
            ) : (
              <div className="text-center py-20 border border-white/10">
                <Package className="w-8 h-8 text-white/20 mx-auto mb-4" />
                <p className="text-lg text-white font-medium mb-2 font-display">No tools found</p>
                <p className="text-white/40 text-sm mb-8">Try a different search term or browse by category.</p>
                <Link
                  href="/categories"
                  className="inline-flex px-8 py-3 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors uppercase tracking-widest"
                >
                  Browse Categories
                </Link>
              </div>
            )}
          </div>
        ) : (
          /* Empty state — show categories */
          <div>
            <p className="text-[10px] font-bold uppercase tracking-widest text-white/40 mb-8">Or browse by category</p>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-px bg-white/10 border border-white/10">
              {categories.map(cat => (
                <Link
                  key={cat.slug}
                  href={`/categories/${cat.slug}`}
                  className="group flex items-center gap-3 p-6 bg-black hover:bg-white/[0.03] transition-colors cursor-pointer"
                >
                  <div>
                    <p className="text-sm font-medium text-white uppercase tracking-tight font-display">{cat.name}</p>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
