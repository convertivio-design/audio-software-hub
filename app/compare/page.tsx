export const dynamic = 'force-dynamic'

import Link from 'next/link'
import { CheckCircle2, XCircle, ExternalLink } from 'lucide-react'
import { getProductBySlug, getCategoryById, getProductDeveloper } from '@/lib/data'
import { formatPrice, formatRating, formatRatingCount, priceTypeBadge } from '@/lib/utils'

interface Props {
  searchParams: { a?: string; b?: string }
}

export async function generateMetadata({ searchParams }: Props) {
  const a = searchParams.a ? getProductBySlug(searchParams.a) : undefined
  const b = searchParams.b ? getProductBySlug(searchParams.b) : undefined
  if (a && b) {
    return {
      title: `${a.name} vs ${b.name} — Audio Software Hub`,
      description: `Side-by-side comparison of ${a.name} and ${b.name}. Compare price, features, pros, cons, OS support, and more.`,
    }
  }
  return {
    title: 'Compare Products — Audio Software Hub',
    description: 'Compare two audio software products side by side.',
  }
}

function Cell({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <div className={`border border-white/10 p-5 ${className}`}>
      {children}
    </div>
  )
}

function Label({ children }: { children: React.ReactNode }) {
  return (
    <p className="text-[10px] uppercase tracking-widest text-white/40 mb-1">{children}</p>
  )
}

export default function ComparePage({ searchParams }: Props) {
  const slugA = searchParams.a
  const slugB = searchParams.b
  const productA = slugA ? getProductBySlug(slugA) : undefined
  const productB = slugB ? getProductBySlug(slugB) : undefined

  const bothFound = productA && productB

  return (
    <div className="min-h-screen">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://audiosoftwarehub.online"},{"@type":"ListItem","position":2,"name":"Compare","item":"https://audiosoftwarehub.online/compare"}]}) }} />
      {/* Breadcrumb */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-4">
        <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-[0.2em]">
          <Link href="/" className="text-white/40 hover:text-white transition-colors">Home</Link>
          <span className="text-white/20">/</span>
          <span className="text-white/60">Compare</span>
        </div>
      </div>

      {/* Header */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-12">
        <p className="text-[10px] uppercase tracking-widest text-white/40 mb-3">Side-by-Side</p>
        <h1 className="text-4xl md:text-5xl font-bold text-white tracking-tighter uppercase font-display">
          {bothFound ? `${productA.name} vs ${productB.name}` : 'Compare Products'}
        </h1>
        {!bothFound && (
          <p className="text-white/40 mt-4 text-sm font-light">
            Add <span className="text-white/60">?a=product-slug&b=product-slug</span> to the URL to compare two products.
          </p>
        )}
      </div>

      {/* Empty state */}
      {!bothFound && (
        <div className="px-6 md:px-20 lg:px-40 py-24">
          <div className="border border-white/10 p-12 max-w-xl">
            <p className="text-[10px] uppercase tracking-widest text-white/40 mb-4">How to compare</p>
            <p className="text-white/60 text-sm leading-relaxed mb-8">
              Navigate to{' '}
              <span className="text-white font-mono text-xs border border-white/20 px-2 py-0.5">
                /compare?a=ableton-live&b=fl-studio
              </span>{' '}
              using any two product slugs from the directory.
            </p>
            <div className="flex gap-4 mb-8">
              <Link
                href="/categories"
                className="flex items-center gap-2 px-6 py-3 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors uppercase tracking-widest"
              >
                Browse Categories
              </Link>
              <Link
                href="/search"
                className="flex items-center gap-2 px-6 py-3 border border-white/20 text-white text-xs font-bold rounded-full hover:bg-white/10 transition-colors uppercase tracking-widest"
              >
                Search Tools
              </Link>
            </div>
            <p className="text-[10px] uppercase tracking-widest text-white/40 mb-4">Or try an example comparison</p>
            <div className="flex flex-col gap-2">
              {[
                ['ableton-live', 'fl-studio'],
                ['serum', 'vital'],
                ['fabfilter-pro-q-3', 'izotope-ozone-11-standard'],
                ['logic-pro', 'cubase'],
                ['massive-x', 'serum-fx'],
              ].map(([a, b]) => (
                <Link
                  key={`${a}-${b}`}
                  href={`/compare?a=${a}&b=${b}`}
                  className="text-xs text-white/40 hover:text-white transition-colors uppercase tracking-widest underline underline-offset-4 decoration-white/20"
                >
                  {a} vs {b}
                </Link>
              ))}
            </div>
          </div>

        </div>
      )}

      {/* Featured Comparison Articles */}
      <div className="px-6 md:px-20 lg:px-40 py-12">
        <div className="border-t border-white/10 pt-12">
          <h2 className="text-lg font-bold text-white uppercase tracking-widest mb-6">Featured Comparison Articles</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <Link
              href="/compare/serum-vs-vital"
              className="group border border-white/10 p-6 hover:border-white/30 transition-all block"
            >
              <span className="text-[10px] px-2 py-0.5 border border-white/20 text-white/50 uppercase tracking-widest mb-3 inline-block">Synthesizers</span>
              <h3 className="text-xl font-light font-display text-white group-hover:text-white/80 transition-colors mb-2">Serum vs Vital</h3>
              <p className="text-sm text-white/40 leading-relaxed">Which wavetable synth is right for you? Compare features, pricing, sound quality, and value.</p>
            </Link>
            <Link
              href="/compare/cubase-vs-ableton"
              className="group border border-white/10 p-6 hover:border-white/30 transition-all block"
            >
              <span className="text-[10px] px-2 py-0.5 border border-white/20 text-white/50 uppercase tracking-widest mb-3 inline-block">DAWs</span>
              <h3 className="text-xl font-light font-display text-white group-hover:text-white/80 transition-colors mb-2">Cubase vs Ableton Live</h3>
              <p className="text-sm text-white/40 leading-relaxed">Detailed comparison of Steinberg Cubase and Ableton Live for music production in 2026.</p>
            </Link>
          </div>
        </div>
      </div>

      {/* Comparison table */}
      {bothFound && (() => {
        const devA = getProductDeveloper(productA)
        const devB = getProductDeveloper(productB)
        const catA = getCategoryById(productA.categoryId)
        const catB = getCategoryById(productB.categoryId)

        return (
          <div className="px-6 md:px-20 lg:px-40 py-16">
            {/* Column headers */}
            <div className="grid grid-cols-1 md:grid-cols-[200px_1fr_1fr] gap-px bg-white/10 mb-px">
              <div className="bg-black border border-white/10 p-5 hidden md:flex items-end">
                <span className="text-[10px] uppercase tracking-widest text-white/30">Spec</span>
              </div>
              {[productA, productB].map(product => (
                <div key={product.id} className="bg-black border border-white/10 p-5 flex flex-col gap-3">
                  <span className="text-[10px] uppercase tracking-widest text-white/40">
                    {getCategoryById(product.categoryId)?.name ?? 'Audio'}
                  </span>
                  <h2 className="text-2xl md:text-3xl font-bold tracking-tighter uppercase font-display text-white">
                    {product.name}
                  </h2>
                  <p className="text-sm text-white/40 font-light leading-relaxed line-clamp-2">
                    {product.shortDescription}
                  </p>
                  <Link
                    href={`/products/${product.slug}`}
                    className="inline-flex items-center gap-2 mt-2 px-5 py-2 bg-white text-black text-xs font-bold uppercase tracking-widest hover:bg-zinc-200 transition-colors w-fit"
                  >
                    View Details
                    <ExternalLink className="w-3 h-3" />
                  </Link>
                </div>
              ))}
            </div>

            {/* Rows */}
            {[
              {
                label: 'Developer',
                renderA: () => <span className="text-sm text-white/70">{devA || '—'}</span>,
                renderB: () => <span className="text-sm text-white/70">{devB || '—'}</span>,
              },
              {
                label: 'Category',
                renderA: () => <span className="text-sm text-white/70">{catA?.name ?? '—'}</span>,
                renderB: () => <span className="text-sm text-white/70">{catB?.name ?? '—'}</span>,
              },
              {
                label: 'Price',
                renderA: () => <span className="text-lg font-light text-white font-display">{formatPrice(productA.price, productA.priceType)}</span>,
                renderB: () => <span className="text-lg font-light text-white font-display">{formatPrice(productB.price, productB.priceType)}</span>,
              },
              {
                label: 'Price Type',
                renderA: () => (
                  <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/50 italic">
                    {priceTypeBadge(productA.priceType)}
                  </span>
                ),
                renderB: () => (
                  <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/50 italic">
                    {priceTypeBadge(productB.priceType)}
                  </span>
                ),
              },
              {
                label: 'Rating',
                renderA: () => (
                  productA.rating !== null && productA.ratingCount > 0 ? (
                    <div>
                      <span className="text-sm text-white">&#9733; {formatRating(productA.rating)}</span>
                      <span className="text-xs text-white/30 ml-2">({formatRatingCount(productA.ratingCount)})</span>
                    </div>
                  ) : (
                    <span className="text-xs text-white/30">No ratings yet</span>
                  )
                ),
                renderB: () => (
                  productB.rating !== null && productB.ratingCount > 0 ? (
                    <div>
                      <span className="text-sm text-white">&#9733; {formatRating(productB.rating)}</span>
                      <span className="text-xs text-white/30 ml-2">({formatRatingCount(productB.ratingCount)})</span>
                    </div>
                  ) : (
                    <span className="text-xs text-white/30">No ratings yet</span>
                  )
                ),
              },
              {
                label: 'OS',
                renderA: () => (
                  <div className="flex flex-wrap gap-1.5">
                    {productA.os.map(o => (
                      <span key={o} className="text-[10px] px-2 py-0.5 border border-white/10 text-white/60 uppercase tracking-widest">{o}</span>
                    ))}
                  </div>
                ),
                renderB: () => (
                  <div className="flex flex-wrap gap-1.5">
                    {productB.os.map(o => (
                      <span key={o} className="text-[10px] px-2 py-0.5 border border-white/10 text-white/60 uppercase tracking-widest">{o}</span>
                    ))}
                  </div>
                ),
              },
              {
                label: 'Formats',
                renderA: () => (
                  <div className="flex flex-wrap gap-1.5">
                    {productA.formats.length > 0
                      ? productA.formats.map(f => (
                          <span key={f} className="text-[10px] px-2 py-0.5 border border-white/20 text-white/70 uppercase tracking-widest">{f}</span>
                        ))
                      : <span className="text-sm text-white/40">—</span>
                    }
                  </div>
                ),
                renderB: () => (
                  <div className="flex flex-wrap gap-1.5">
                    {productB.formats.length > 0
                      ? productB.formats.map(f => (
                          <span key={f} className="text-[10px] px-2 py-0.5 border border-white/20 text-white/70 uppercase tracking-widest">{f}</span>
                        ))
                      : <span className="text-sm text-white/40">—</span>
                    }
                  </div>
                ),
              },
              {
                label: 'Features',
                renderA: () => (
                  <ul className="space-y-1.5">
                    {productA.features.map((f, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                        <span className="mt-2 w-1 h-1 bg-white/40 shrink-0" />{f}
                      </li>
                    ))}
                  </ul>
                ),
                renderB: () => (
                  <ul className="space-y-1.5">
                    {productB.features.map((f, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                        <span className="mt-2 w-1 h-1 bg-white/40 shrink-0" />{f}
                      </li>
                    ))}
                  </ul>
                ),
              },
              {
                label: 'Pros',
                renderA: () => (
                  <ul className="space-y-1.5">
                    {productA.pros.map((p, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                        <CheckCircle2 className="w-3.5 h-3.5 mt-0.5 text-green-500/60 shrink-0" />{p}
                      </li>
                    ))}
                  </ul>
                ),
                renderB: () => (
                  <ul className="space-y-1.5">
                    {productB.pros.map((p, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                        <CheckCircle2 className="w-3.5 h-3.5 mt-0.5 text-green-500/60 shrink-0" />{p}
                      </li>
                    ))}
                  </ul>
                ),
              },
              {
                label: 'Cons',
                renderA: () => (
                  <ul className="space-y-1.5">
                    {productA.cons.map((c, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                        <XCircle className="w-3.5 h-3.5 mt-0.5 text-red-500/60 shrink-0" />{c}
                      </li>
                    ))}
                  </ul>
                ),
                renderB: () => (
                  <ul className="space-y-1.5">
                    {productB.cons.map((c, i) => (
                      <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                        <XCircle className="w-3.5 h-3.5 mt-0.5 text-red-500/60 shrink-0" />{c}
                      </li>
                    ))}
                  </ul>
                ),
              },
            ].map(row => (
              <div key={row.label} className="grid grid-cols-1 md:grid-cols-[200px_1fr_1fr] gap-px bg-white/10 mb-px">
                <Cell className="bg-black hidden md:flex items-start">
                  <Label>{row.label}</Label>
                </Cell>
                <Cell className="bg-black">
                  <p className="text-[10px] uppercase tracking-widest text-white/40 mb-3 md:hidden">{row.label} — {productA.name}</p>
                  {row.renderA()}
                </Cell>
                <Cell className="bg-black">
                  <p className="text-[10px] uppercase tracking-widest text-white/40 mb-3 md:hidden">{row.label} — {productB.name}</p>
                  {row.renderB()}
                </Cell>
              </div>
            ))}

            {/* Footer CTAs */}
            <div className="grid grid-cols-1 md:grid-cols-[200px_1fr_1fr] gap-px bg-white/10 mt-px">
              <div className="bg-black border border-white/10 p-5 hidden md:block" />
              {[productA, productB].map(product => (
                <div key={product.id} className="bg-black border border-white/10 p-5 flex flex-col gap-3">
                  <p className="text-[10px] uppercase tracking-widest text-white/40">Get {product.name}</p>
                  <p className="text-xl font-light text-white font-display">{formatPrice(product.price, product.priceType)}</p>
                  <div className="flex flex-wrap gap-3">
                    <Link
                      href={`/products/${product.slug}`}
                      className="px-6 py-2.5 bg-white text-black text-xs font-bold uppercase tracking-widest hover:bg-zinc-200 transition-colors"
                    >
                      View Details
                    </Link>
                    <a
                      href={product.officialUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="px-6 py-2.5 border border-white/20 text-white text-xs font-bold uppercase tracking-widest hover:border-white/50 transition-colors flex items-center gap-2"
                    >
                      Official Site
                      <ExternalLink className="w-3 h-3" />
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )
      })()}
    </div>
  )
}
