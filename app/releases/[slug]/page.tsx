export const dynamic = 'force-dynamic'

import { notFound } from 'next/navigation'
import Link from 'next/link'
import { ExternalLink, ArrowLeft, Calendar, Tag } from 'lucide-react'
import { formatPrice, priceTypeBadge } from '@/lib/utils'
import { getCategoryById, getSanitizedReleases, type SanitizedRelease } from '@/lib/data'

type Release = SanitizedRelease

function getReleaseBySlug(slug: string): Release | null {
  const releases = getSanitizedReleases()
  return releases.find(r => r.slug === slug) ?? null
}

interface Props {
  params: { slug: string }
}

export async function generateMetadata({ params }: Props) {
  const release = getReleaseBySlug(params.slug)
  if (!release) return {}
  return {
    title: `${release.name} — Audio Software Hub`,
    description: release.shortDescription,
  }
}

export default function ReleasePage({ params }: Props) {
  const release = getReleaseBySlug(params.slug)
  if (!release) notFound()

  const category = getCategoryById(release.categoryId)
  const dateStr = release.dateAdded
    ? new Date(release.dateAdded).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' })
    : null

  return (
    <div className="min-h-screen">
      {/* Breadcrumb */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-4">
        <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-[0.2em]">
          <Link href="/" className="text-white/40 hover:text-white transition-colors">Home</Link>
          <span className="text-white/20">/</span>
          <span className="text-white/40">New Releases</span>
          <span className="text-white/20">/</span>
          <span className="text-white/60">{release.name}</span>
        </div>
      </div>

      {/* Hero */}
      <div className="px-6 md:px-20 lg:px-40 pt-20 pb-16 border-b border-white/10">
        <Link
          href="/"
          className="inline-flex items-center gap-2 text-white/40 hover:text-white text-xs uppercase tracking-widest transition-colors mb-12"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          Back
        </Link>

        <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-8">
          <div className="flex-1">
            {/* New badge */}
            <div className="flex items-center gap-3 mb-6">
              <span className="w-2 h-2 rounded-full bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.4)]" />
              <span className="text-[10px] uppercase tracking-widest text-white/60">New Release</span>
              {category && (
                <>
                  <span className="text-white/20">/</span>
                  <Link
                    href={`/categories/${category.slug}`}
                    className="text-[10px] uppercase tracking-widest text-white/60 hover:text-white transition-colors"
                  >
                    {category.name}
                  </Link>
                </>
              )}
            </div>

            {release.developer && (
              <p className="text-[10px] uppercase tracking-widest text-white/40 mb-2">{release.developer}</p>
            )}
            <h1 className="text-5xl md:text-6xl font-light tracking-tight font-display mb-6">{release.name}</h1>
            <p className="text-lg text-white/50 font-light leading-relaxed max-w-2xl">{release.shortDescription}</p>
          </div>

          {/* Price + CTA */}
          <div className="flex flex-col gap-4 md:items-end shrink-0">
            <span className="text-[10px] px-3 py-1 border border-white/30 uppercase tracking-tighter text-white/40 italic self-start md:self-end">
              {priceTypeBadge(release.priceType as any)}
            </span>
            <div className="text-4xl font-light font-display">
              {formatPrice(release.price, release.priceType as any)}
            </div>
            <a
              href={release.officialUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-2 px-8 py-4 bg-white text-black text-xs font-bold uppercase tracking-widest hover:bg-zinc-200 transition-colors"
            >
              Visit Official Site
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </div>
        </div>
      </div>

      {/* Details */}
      <div className="px-6 md:px-20 lg:px-40 py-20 grid grid-cols-1 lg:grid-cols-3 gap-16">
        {/* Main */}
        <div className="lg:col-span-2 space-y-12">
          {release.longDescription && release.longDescription !== release.shortDescription && (
            <div>
              <h2 className="text-[10px] uppercase tracking-widest text-white/40 mb-4">About</h2>
              <p className="text-white/60 leading-relaxed">{release.longDescription}</p>
            </div>
          )}

          {release.features?.length > 0 && release.features[0] !== `New release: ${release.name}` && (
            <div>
              <h2 className="text-[10px] uppercase tracking-widest text-white/40 mb-4">Features</h2>
              <ul className="space-y-2">
                {release.features.map((f, i) => (
                  <li key={i} className="flex items-start gap-3 text-sm text-white/60">
                    <span className="w-1 h-1 rounded-full bg-white/40 mt-2 shrink-0" />
                    {f}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <div className="grid grid-cols-2 gap-8">
            {release.pros?.length > 0 && release.pros[0] !== 'Recently released' && (
              <div>
                <h2 className="text-[10px] uppercase tracking-widest text-white/40 mb-4">Pros</h2>
                <ul className="space-y-2">
                  {release.pros.map((p, i) => (
                    <li key={i} className="text-sm text-white/60 flex items-start gap-2">
                      <span className="text-green-400 mt-0.5">+</span>{p}
                    </li>
                  ))}
                </ul>
              </div>
            )}
            {release.cons?.length > 0 && (
              <div>
                <h2 className="text-[10px] uppercase tracking-widest text-white/40 mb-4">Cons</h2>
                <ul className="space-y-2">
                  {release.cons.map((c, i) => (
                    <li key={i} className="text-sm text-white/60 flex items-start gap-2">
                      <span className="text-white/30 mt-0.5">–</span>{c}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-8">
          <div className="border border-white/10 p-6 space-y-5">
            <h2 className="text-[10px] uppercase tracking-widest text-white/40">Details</h2>

            {release.os?.length > 0 && (
              <div>
                <p className="text-[10px] uppercase tracking-widest text-white/30 mb-1">Platform</p>
                <p className="text-sm text-white/70">{release.os.join(', ')}</p>
              </div>
            )}

            {release.formats?.length > 0 && (
              <div>
                <p className="text-[10px] uppercase tracking-widest text-white/30 mb-1">Formats</p>
                <p className="text-sm text-white/70">{release.formats.join(', ')}</p>
              </div>
            )}

            {category && (
              <div>
                <p className="text-[10px] uppercase tracking-widest text-white/30 mb-1">Category</p>
                <Link href={`/categories/${category.slug}`} className="text-sm text-white/70 hover:text-white transition-colors">
                  {category.name}
                </Link>
              </div>
            )}

            {dateStr && (
              <div className="flex items-center gap-2 text-[10px] uppercase tracking-widest text-white/30">
                <Calendar className="w-3 h-3" />
                Added {dateStr}
              </div>
            )}
          </div>

          {release.tags?.length > 0 && (
            <div>
              <h2 className="text-[10px] uppercase tracking-widest text-white/40 mb-3">Tags</h2>
              <div className="flex flex-wrap gap-2">
                {release.tags.map(tag => (
                  <span key={tag} className="flex items-center gap-1 px-3 py-1 border border-white/10 text-[10px] uppercase tracking-widest text-white/40">
                    <Tag className="w-2.5 h-2.5" />
                    {tag}
                  </span>
                ))}
              </div>
            </div>
          )}

          <a
            href={release.officialUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-center gap-2 w-full px-6 py-4 border border-white/20 text-sm text-white/60 hover:text-white hover:border-white/40 transition-all uppercase tracking-widest"
          >
            Official Website
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>
      </div>
    </div>
  )
}
