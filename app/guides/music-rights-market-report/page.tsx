import type { Metadata } from 'next'
import Link from 'next/link'
import MusicRightsReportTabs from './music-rights-report-tabs'

export const metadata: Metadata = {
  title: 'Music Rights Management — Market Strategy & Feasibility Report',
  description:
    'Global music rights management market analysis: TAM/SAM/SOM, customer segments, M&A integration friction, and productization opportunities for royalty infrastructure.',
  alternates: { canonical: '/guides/music-rights-market-report' },
  openGraph: {
    title: 'Music Rights Management — Market Strategy & Feasibility Report',
    description: 'Market sizing, customer tiers, M&A integration friction, and productization opportunities for royalty infrastructure.',
  },
}

const pageSchema = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://audiosoftwarehub.online' },
        { '@type': 'ListItem', position: 2, name: 'Guides', item: 'https://audiosoftwarehub.online/guides' },
        { '@type': 'ListItem', position: 3, name: 'Music Rights Management Market Report', item: 'https://audiosoftwarehub.online/guides/music-rights-market-report' },
      ],
    },
    {
      '@type': 'Article',
      headline: 'Music Rights Management — Market Strategy & Feasibility Report',
      description: 'Global music rights management market analysis and productization opportunities.',
      author: { '@type': 'Organization', name: 'Audio Software Hub' },
      publisher: { '@type': 'Organization', name: 'Audio Software Hub' },
      mainEntityOfPage: { '@type': 'WebPage', '@id': 'https://audiosoftwarehub.online/guides/music-rights-market-report' },
    },
  ],
}

export default function MusicRightsMarketReportPage() {
  return (
    <div className="min-h-screen px-6 md:px-20 lg:px-40 py-16 md:py-24">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(pageSchema) }} />

      <nav className="mb-10 text-sm text-white/40">
        <Link href="/" className="hover:text-white">Home</Link>
        <span className="mx-2">/</span>
        <Link href="/guides" className="hover:text-white">Guides</Link>
        <span className="mx-2">/</span>
        <span className="text-white/60">Music Rights Management Market Report</span>
      </nav>

      <article className="max-w-4xl mx-auto">
        <h1 className="text-4xl md:text-5xl font-bold text-white mb-6 leading-tight">
          Music Rights Management — Market Strategy &amp; Feasibility Report
        </h1>
        <p className="text-white/50 text-sm mb-10">
          Infrastructure &amp; productization opportunities · Market sizing, customer tiers, M&amp;A friction, and recommended entry point
        </p>

        <MusicRightsReportTabs />
      </article>
    </div>
  )
}
