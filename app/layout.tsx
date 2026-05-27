import type { Metadata } from 'next'
import { Inter, Space_Grotesk } from 'next/font/google'
import './globals.css'
import { Navbar } from '@/components/Navbar'
import { Footer } from '@/components/Footer'

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' })
const spaceGrotesk = Space_Grotesk({ subsets: ['latin'], variable: '--font-display' })

export const metadata: Metadata = {
  metadataBase: new URL('https://audiosoftwarehub.online'),
  title: {
    default: 'Audio Software Hub — Find Music Production Software',
    template: '%s | Audio Software Hub',
  },
  description: 'Discover and compare 3,000+ professional music production tools: DAWs, synthesizers, effects plugins, drum machines, and more.',
  keywords: 'VST plugins, DAW, synthesizer, music production, audio plugins, plugins directory',
  alternates: {
    canonical: '/',
    types: {
      'application/rss+xml': 'https://audiosoftwarehub.online/rss',
    },
  },
  openGraph: {
    title: 'Audio Software Hub',
    description: 'The definitive directory of 3,000+ music production tools.',
    type: 'website',
    url: 'https://audiosoftwarehub.online',
    siteName: 'Audio Software Hub',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Audio Software Hub',
    description: 'Find the right music production software.',
  },
  robots: { index: true, follow: true },
}

const websiteSchema = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'WebSite',
      '@id': 'https://audiosoftwarehub.online/#website',
      name: 'Audio Software Hub',
      url: 'https://audiosoftwarehub.online',
      description: 'The definitive directory of music production software',
      potentialAction: {
        '@type': 'SearchAction',
        target: {
          '@type': 'EntryPoint',
          urlTemplate: 'https://audiosoftwarehub.online/search?q={search_term_string}',
        },
        'query-input': 'required name=search_term_string',
      },
    },
    {
      '@type': 'Organization',
      '@id': 'https://audiosoftwarehub.online/#organization',
      name: 'Audio Software Hub',
      url: 'https://audiosoftwarehub.online',
      description: 'Music production software directory and comparison platform',
      sameAs: [
        'https://audiosoftwarehub.online',
      ],
    },
  ],
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${spaceGrotesk.variable}`}>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteSchema) }}
        />
      </head>
      <body className="bg-black text-white min-h-screen flex flex-col antialiased">
        <Navbar />
        <main className="flex-1">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  )
}
