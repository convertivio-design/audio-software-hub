import Link from 'next/link'
import { ExternalLink } from 'lucide-react'
import { formatPrice, formatRating, priceTypeBadge } from '@/lib/utils'
import { type Product, getCategoryById, getProductDeveloper } from '@/lib/data'

interface ProductCardProps {
  product: Product
  className?: string
  compact?: boolean
  detailHref?: string
}

export function ProductCard({ product, className, compact = false, detailHref }: ProductCardProps) {
  const category = getCategoryById(product.categoryId)
  const developer = getProductDeveloper(product)
  const href = detailHref ?? `/products/${product.slug}`

  return (
    <div
      className={`group flex flex-col border border-white/10 hover:bg-white/[0.03] transition-colors cursor-pointer ${className ?? ''}`}
    >
      {/* Content */}
      <div className="flex flex-col flex-1 p-6">
        {/* Top: category + price type */}
        <div className="flex justify-between items-start mb-8">
          <span className="text-[9px] font-bold text-white/40 uppercase tracking-widest">
            {category?.name ?? 'Audio'}
          </span>
          <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/40 italic">
            {priceTypeBadge(product.priceType)}
          </span>
        </div>

        {/* Developer + Name */}
        <div className="space-y-1 mb-3">
          <div className="flex justify-between items-center">
            {developer && (
              <span className="text-[10px] uppercase tracking-widest text-white/40">{developer}</span>
            )}
            <span className="text-[10px] text-white">&#9733; {formatRating(product.rating)}</span>
          </div>
          <Link
            href={href}
            className="text-lg font-medium tracking-tight text-white hover:text-white/80 transition-colors font-display block"
          >
            {product.name}
          </Link>
        </div>

        {!compact && (
          <p className="text-sm text-white/40 leading-relaxed line-clamp-2 mb-6 flex-1">
            {product.shortDescription}
          </p>
        )}

        {/* Footer */}
        <div className="flex items-center justify-between mt-auto pt-4 border-t border-white/5">
          <span className="text-lg font-light text-white">
            {formatPrice(product.price, product.priceType)}
          </span>
          <div className="flex items-center gap-2">
            <a
              href={product.officialUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="text-white/20 hover:text-white transition-colors"
              title="Official site"
            >
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
            <Link
              href={href}
              className="px-5 py-1.5 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors"
            >
              Details
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
