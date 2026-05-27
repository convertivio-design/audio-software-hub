import type { Metadata } from 'next'
import Link from 'next/link'
import { Sparkles, ArrowUpRight, Calendar, Tag } from 'lucide-react'
import { getSanitizedReleases } from '@/lib/data'
import { formatPrice, priceTypeBadge } from '@/lib/utils'

export const dynamic = 'force-dynamic'

export const metadata: Metadata = {
  title: 'New Music Software Releases',
  description: 'Discover the latest music software releases, including new VST plugins, DAW updates, virtual instruments, and audio tools added to our directory.',
  openGraph: {
    title: 'New Music Software Releases',
    description: 'Discover the latest music software releases, including new VST plugins, DAW updates, virtual instruments, and audio tools.',
  },
  alternates: {
    canonical: '/releases',
  },
}

export default function ReleasesPage() {
  const releases = getSanitizedReleases()

  return (
    <div className="min-h-screen">
      {/* Breadcrumb */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-4">
        <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-[0.2em]">
          <Link href="/" className="text-white/40 hover:text-white transition-colors">Home</Link>
          <span className="text-white/20">/</span>
          <span className="text-white/60">New Releases</span>
        </div>
      </div>

      {/* Hero */}
      <div className="px-6 md:px-20 lg:px-40 pt-20 pb-16 border-b border-white/10">
        <div className="flex items-center gap-3 mb-6">
          <Sparkles className="w-4 h-4 text-white/40" />
          <span className="text-[10px] uppercase tracking-widest text-white/60">Latest</span>
        </div>
        <h1 className="text-5xl md:text-7xl font-light font-display tracking-tight mb-6">
          New Releases
        </h1>
        <p className="text-lg text-white/50 font-light leading-relaxed max-w-2xl">
          The latest music software releases we&apos;ve discovered — from new plugins and
          virtual instruments to DAW updates and audio tools.
        </p>

        {releases.length > 0 && (
          <p className="text-[10px] uppercase tracking-widest text-white/30 mt-6">
            {releases.length} release{releases.length !== 1 ? 's' : ''} added
          </p>
        )}
      </div>

      {/* Schema */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'CollectionPage',
            name: 'New Music Software Releases',
            description: 'Discover the latest music software releases added to Audio Software Hub.',
            url: 'https://audiosoftwarehub.online/releases',
            breadcrumb: {
              '@type': 'BreadcrumbList',
              itemListElement: [
                { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://audiosoftwarehub.online' },
                { '@type': 'ListItem', position: 2, name: 'New Releases', item: 'https://audiosoftwarehub.online/releases' },
              ],
            },
          }),
        }}
      />

      {/* Releases list */}
      {releases.length === 0 ? (
        <div className="px-6 md:px-20 lg:px-40 py-20">
          <p className="text-white/40 font-light">No releases found yet. Check back soon.</p>
        </div>
      ) : (
        <div className="bg-black">
          <div className="grid grid-cols-1 gap-px bg-white/10">
            {releases.map((release) => {
              const dateStr = release.dateAdded
                ? new Date(release.dateAdded).toLocaleDateString('en-GB', {
                    day: 'numeric',
                    month: 'short',
                    year: 'numeric',
                  })
                : null

              return (
                <Link
                  key={release.slug}
                  href={`/releases/${release.slug}`}
                  className="group px-6 md:px-20 lg:px-40 py-8 bg-black hover:bg-white/[0.02] transition-colors"
                >
                  <div className="flex items-start justify-between gap-6">
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-3 mb-2">
                        <span className="w-1.5 h-1.5 rounded-full bg-green-500 shadow-[0_0_6px_rgba(34,197,94,0.4)] shrink-0" />
                        <span className="text-[10px] uppercase tracking-widest text-white/40">New Release</span>
                        {release.developer && (
                          <>
                            <span className="text-white/20">/</span>
                            <span className="text-[10px] uppercase tracking-widest text-white/30">{release.developer}</span>
                          </>
                        )}
                      </div>

                      <h2 className="text-xl font-display font-light text-white/90 group-hover:text-white transition-colors mb-2">
                        {release.name}
                      </h2>

                      {release.shortDescription && (
                        <p className="text-sm text-white/50 font-light leading-relaxed line-clamp-2">
                          {release.shortDescription}
                        </p>
                      )}

                      <div className="flex items-center gap-4 mt-3">
                        <span className="text-[10px] px-2 py-0.5 border border-white/20 uppercase tracking-tighter text-white/40 italic">
                          {priceTypeBadge(release.priceType as any)}
                        </span>
                        <span className="text-sm text-white/60 font-light font-display">
                          {formatPrice(release.price, release.priceType as any)}
                        </span>
                        {dateStr && (
                          <span className="flex items-center gap-1 text-[10px] uppercase tracking-widest text-white/30">
                            <Calendar className="w-2.5 h-2.5" />
                            {dateStr}
                          </span>
                        )}
                      </div>

                      {release.tags && release.tags.length > 0 && (
                        <div className="flex flex-wrap gap-2 mt-3">
                          {release.tags.slice(0, 3).map(tag => (
                            <span key={tag} className="flex items-center gap-1 px-2 py-0.5 border border-white/10 text-[9px] uppercase tracking-widest text-white/30">
                              <Tag className="w-2 h-2" />
                              {tag}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>

                    <ArrowUpRight className="w-4 h-4 text-white/20 group-hover:text-white/60 transition-colors shrink-0 mt-1" />
                  </div>
                </Link>
              )
            })}
          </div>
        </div>
      )}
    </div>
  )
}
