import { notFound } from 'next/navigation'
import Link from 'next/link'
import {
  ExternalLink, Monitor, CheckCircle2,
  XCircle, Puzzle, Users, Tag, ArrowUpRight,
} from 'lucide-react'
import {
  getProductBySlug, getCategoryById, getProductDeveloper,
  getProductsByCategory, products as allProducts,
} from '@/lib/data'
import { formatPrice, formatRating, formatRatingCount, priceTypeBadge } from '@/lib/utils'
import { ProductCard } from '@/components/ProductCard'

interface Props {
  params: { slug: string }
}

export async function generateStaticParams() {
  return allProducts.map(p => ({ slug: p.slug }))
}

export async function generateMetadata({ params }: Props) {
  const product = getProductBySlug(params.slug)
  if (!product) return {}
  return {
    title: `${product.name} — Audio Software Hub`,
    description: product.shortDescription,
    alternates: { canonical: `/products/${product.slug}` },
    openGraph: {
      title: `${product.name} — Audio Software Hub`,
      description: product.shortDescription,
      images: [{ url: '/og-image.png', width: 1200, height: 630, alt: product.name }],
    },
  }
}

export default function ProductPage({ params }: Props) {
  const product = getProductBySlug(params.slug)
  if (!product) notFound()

  const category = getCategoryById(product.categoryId)
  const developer = getProductDeveloper(product)
  const related = getProductsByCategory(product.categoryId)
    .filter(p => p.id !== product.id)
    .slice(0, 4)

  return (
    <div className="min-h-screen">
      {/* Breadcrumb */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-4">
        <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-[0.2em]">
          <Link href="/categories" className="text-white/40 hover:text-white transition-colors">Directory</Link>
          <span className="text-white/20">/</span>
          {category && (
            <>
              <Link href={`/categories/${category.slug}`} className="text-white/40 hover:text-white transition-colors">
                {category.name}
              </Link>
              <span className="text-white/20">/</span>
            </>
          )}
          <span className="text-white/60">{product.name}</span>
        </div>
      </div>

      {/* Hero */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-12">
        <div className="flex flex-col lg:flex-row items-start gap-8">
          {/* Left: Info */}
          <div className="flex-1">
            <div className="flex flex-wrap items-center gap-3 mb-4">
              {category && (
                <Link
                  href={`/categories/${category.slug}`}
                  className="text-[10px] font-bold uppercase tracking-widest text-white/40 hover:text-white transition-colors"
                >
                  {category.name}
                </Link>
              )}
              <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/40 italic">
                {priceTypeBadge(product.priceType)}
              </span>
              {product.isNew && (
                <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/60">
                  New
                </span>
              )}
              {product.isFeatured && (
                <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/60">
                  Featured
                </span>
              )}
            </div>

            <h1 className="text-4xl md:text-5xl font-bold text-white tracking-tighter uppercase font-display mb-2">{product.name}</h1>
            {developer && (
              <p className="text-white/40 mb-6">
                <span className="text-[10px] font-bold uppercase tracking-widest">by </span>
                <a href={product.officialUrl} target="_blank" rel="noopener noreferrer" className="text-white/60 hover:text-white transition-colors">
                  {developer}
                </a>
              </p>
            )}

            <p className="text-white/50 text-lg font-light leading-relaxed mb-8 max-w-2xl">{product.shortDescription}</p>

            {product.rating !== null && product.ratingCount > 0 && (
              <div className="flex items-center gap-4">
                <span className="text-sm text-white">&#9733; {formatRating(product.rating)}</span>
                <span className="text-xs text-white/30">({formatRatingCount(product.ratingCount)} ratings)</span>
              </div>
            )}
          </div>

          {/* Right: Price + CTA */}
          <div className="lg:text-right shrink-0 border border-white/10 p-8">
            <p className="text-[10px] uppercase tracking-widest text-white/40 mb-2">Price</p>
            <p className="text-3xl font-light text-white mb-1 font-display">
              {formatPrice(product.price, product.priceType)}
            </p>
            {product.priceType === 'subscription' && (
              <p className="text-[10px] text-white/30 uppercase tracking-widest mb-6">Billed monthly</p>
            )}
            {product.priceType === 'one-time' && (
              <p className="text-[10px] text-white/30 uppercase tracking-widest mb-6">One-time purchase</p>
            )}
            {product.priceType === 'free' && <div className="mb-6" />}
            {product.priceType === 'freemium' && <div className="mb-6" />}
            <a
              href={product.officialUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 px-8 py-3 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors uppercase tracking-widest"
            >
              Visit Official Site
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="px-6 md:px-20 lg:px-40 py-16">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-px bg-white/10">
          {/* Left: Description + Features + Pros/Cons */}
          <div className="lg:col-span-2 bg-black space-y-0">
            {/* Description */}
            <div className="border border-white/10 p-8">
              <h2 className="text-[10px] font-bold uppercase tracking-widest text-white/40 mb-6">About</h2>
              <p className="text-white/50 leading-relaxed">{product.longDescription}</p>
            </div>

            {/* Key Features */}
            <div className="border border-white/10 border-t-0 p-8">
              <h2 className="text-[10px] font-bold uppercase tracking-widest text-white/40 mb-6">Key Features</h2>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {product.features.map((feature, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                    <span className="mt-1.5 w-1 h-1 bg-white/40 shrink-0" />
                    {feature}
                  </li>
                ))}
              </ul>
            </div>

            {/* Pros & Cons */}
            <div className="grid grid-cols-1 sm:grid-cols-2">
              <div className="border border-white/10 border-t-0 p-8">
                <h3 className="text-[10px] font-bold uppercase tracking-widest text-green-500/80 mb-4 flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5" />
                  Pros
                </h3>
                <ul className="space-y-2">
                  {product.pros.map((pro, i) => (
                    <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                      <span className="mt-0.5 text-green-500/60 shrink-0">+</span>
                      {pro}
                    </li>
                  ))}
                </ul>
              </div>
              <div className="border border-white/10 border-t-0 border-l-0 p-8">
                <h3 className="text-[10px] font-bold uppercase tracking-widest text-red-500/80 mb-4 flex items-center gap-2">
                  <XCircle className="w-3.5 h-3.5" />
                  Cons
                </h3>
                <ul className="space-y-2">
                  {product.cons.map((con, i) => (
                    <li key={i} className="flex items-start gap-2 text-sm text-white/60">
                      <span className="mt-0.5 text-red-500/60 shrink-0">-</span>
                      {con}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          {/* Right: Specs */}
          <div className="bg-black">
            <div className="border border-white/10 border-l-0 p-8 space-y-8 h-full">
              <h2 className="text-[10px] font-bold uppercase tracking-widest text-white/40">Specifications</h2>

              <div>
                <p className="text-[10px] text-white/30 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                  <Monitor className="w-3 h-3" /> OS Support
                </p>
                <div className="flex flex-wrap gap-2">
                  {product.os.map(os => (
                    <span key={os} className="text-[10px] px-2 py-1 border border-white/10 text-white/60 uppercase tracking-widest">
                      {os}
                    </span>
                  ))}
                </div>
              </div>

              {product.formats.length > 0 && (
                <div>
                  <p className="text-[10px] text-white/30 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                    <Puzzle className="w-3 h-3" /> Plugin Formats
                  </p>
                  <div className="flex flex-wrap gap-2">
                    {product.formats.map(fmt => (
                      <span key={fmt} className="text-[10px] px-2 py-1 border border-white/20 text-white/70 uppercase tracking-widest">
                        {fmt}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              <div>
                <p className="text-[10px] text-white/30 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                  <Users className="w-3 h-3" /> Best For
                </p>
                <p className="text-sm text-white/50">{product.targetAudience}</p>
              </div>

              <div>
                <p className="text-[10px] text-white/30 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                  <Tag className="w-3 h-3" /> Tags
                </p>
                <div className="flex flex-wrap gap-2">
                  {product.tags.map(tag => (
                    <span key={tag} className="text-[10px] px-2 py-0.5 border border-white/10 text-white/40 uppercase tracking-widest">
                      #{tag}
                    </span>
                  ))}
                </div>
              </div>

              {/* CTA */}
              <div className="border-t border-white/10 pt-8 mt-auto">
                <p className="text-[10px] uppercase tracking-widest text-white/40 mb-2">Get {product.name}</p>
                <p className="text-2xl font-light text-white mb-4 font-display">{formatPrice(product.price, product.priceType)}</p>
                <a
                  href={product.officialUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block w-full py-3 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors text-center uppercase tracking-widest"
                >
                  Visit Official Site
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* JSON-LD: SoftwareApplication */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'SoftwareApplication',
            name: product.name,
            applicationCategory: 'MultimediaApplication',
            operatingSystem: product.os.join(', '),
            description: product.shortDescription,
            offers: {
              '@type': 'Offer',
              price: product.price ?? 0,
              priceCurrency: 'USD',
            },
            ...(product.ratingCount > 0 && {
              aggregateRating: {
                '@type': 'AggregateRating',
                ratingValue: product.rating,
                ratingCount: product.ratingCount,
              },
            }),
          }),
        }}
      />

      {/* Related products */}
      {related.length > 0 && (
        <div className="border-t border-white/10 px-6 md:px-20 lg:px-40 py-16">
          <div className="flex items-end justify-between mb-10">
            <div>
              <p className="text-[10px] uppercase tracking-widest text-white/40 mb-2">Related</p>
              <h2 className="text-3xl font-light text-white tracking-tight font-display">
                More {category?.name}
              </h2>
            </div>
            {category && (
              <Link
                href={`/categories/${category.slug}`}
                className="flex items-center gap-1 text-[10px] text-white/40 hover:text-white uppercase tracking-widest transition-colors"
              >
                View All <ArrowUpRight className="w-3 h-3" />
              </Link>
            )}
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            {related.map(p => (
              <ProductCard key={p.id} product={p} />
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
