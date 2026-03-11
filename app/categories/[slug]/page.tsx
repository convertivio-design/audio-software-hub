import type { Metadata } from 'next'
import { notFound } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, Package } from 'lucide-react'
import { getCategoryBySlug, getProductsByCategory } from '@/lib/data'
import { ProductCard } from '@/components/ProductCard'

interface Props {
  params: { slug: string }
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const category = getCategoryBySlug(params.slug)
  if (!category) return {}
  return {
    title: `${category.name} Software & Plugins`,
    description: `Browse ${category.name.toLowerCase()} plugins and software. ${category.description}`,
    alternates: { canonical: `/categories/${category.slug}` },
    openGraph: {
      title: `${category.name} — Audio Software Hub`,
      description: category.description,
    },
  }
}

export default function CategoryPage({ params }: Props) {
  const category = getCategoryBySlug(params.slug)
  if (!category) notFound()

  const products = getProductsByCategory(category.id)
  const featured = products.filter(p => p.isFeatured)
  const rest = products.filter(p => !p.isFeatured)
  const sorted = [...featured, ...rest]

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'Home',
        item: 'https://audio-software-hub.com',
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: 'Categories',
        item: 'https://audio-software-hub.com/categories',
      },
      {
        '@type': 'ListItem',
        position: 3,
        name: category.name,
        item: `https://audio-software-hub.com/categories/${category.slug}`,
      },
    ],
  }

  return (
    <div className="min-h-screen">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }}
      />
      <div className="px-6 md:px-20 lg:px-40 py-12">
        {/* Breadcrumb */}
        <div className="mb-8 flex items-center gap-2">
          <Link
            href="/categories"
            className="inline-flex items-center gap-1.5 text-[10px] font-bold uppercase tracking-[0.2em] text-white/40 hover:text-white transition-colors"
          >
            <ArrowLeft className="w-3 h-3" />
            Directory
          </Link>
          <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-white/20">&gt;</span>
          <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-white/60">{category.name}</span>
        </div>

        {/* Category header */}
        <div className="border-b border-white/10 px-6 py-8 mb-12 flex items-end justify-between">
          <div>
            <p className="text-xs font-bold tracking-widest text-white/40 uppercase mb-2">Category</p>
            <h1 className="text-5xl font-bold uppercase tracking-tighter font-display text-white">{category.name}</h1>
            <p className="text-white/50 text-sm mt-3 max-w-xl leading-relaxed">{category.description}</p>
          </div>
          <div className="text-right shrink-0 ml-8">
            <span className="text-3xl font-mono text-white/80">{products.length}</span>
            <p className="text-[10px] font-bold tracking-widest text-white/40 uppercase mt-1">Tools</p>
          </div>
        </div>

        {/* Products */}
        {sorted.length === 0 ? (
          <div className="text-center py-24 border border-white/10">
            <Package className="w-10 h-10 text-white/20 mx-auto mb-4" />
            <p className="text-white/40 mb-2">No tools listed yet in this category.</p>
            <p className="text-white/20 text-sm">Check back soon -- we are adding new tools regularly.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
            {sorted.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
