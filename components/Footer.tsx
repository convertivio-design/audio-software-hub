import Link from 'next/link'
import { Github, Twitter, Grid3X3, Rss } from 'lucide-react'

const siteLinks = [
  { label: 'Home', href: '/' },
  { label: 'Categories', href: '/categories' },
  { label: 'New Releases', href: '/' },
  { label: 'Search', href: '/search' },
  { label: 'Compare', href: '/compare' },
  { label: 'Submit a Tool', href: '/submit' },
]

const categoryLinks = [
  { label: 'DAWs', href: '/categories/daws' },
  { label: 'Synthesizers', href: '/categories/synthesizers' },
  { label: 'Effects & Processing', href: '/categories/effects' },
  { label: 'Samplers & Libraries', href: '/categories/samplers' },
  { label: 'Drum Machines', href: '/categories/drum-machines' },
  { label: 'Mixing & Mastering', href: '/categories/mixing-mastering' },
  { label: 'MIDI & Utilities', href: '/categories/midi-utilities' },
  { label: 'Guitar & Bass', href: '/categories/guitar-bass' },
  { label: 'Analysis & Utility', href: '/categories/analysis-utility' },
  { label: 'Experimental', href: '/categories/experimental' },
  { label: 'Vocal Tools', href: '/categories/vocal-tools' },
]

export function Footer() {
  return (
    <footer className="border-t border-white/10 bg-black py-32 px-6">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-16 md:gap-8">
        {/* Brand / About */}
        <div className="space-y-8">
          <Link href="/" className="text-2xl font-bold tracking-tighter flex items-center gap-2">
            <Grid3X3 className="w-6 h-6" />
            audiosoftwarehub
          </Link>
          <p className="max-w-xs text-white/40 text-sm leading-relaxed">
            The definitive guide to music production software. Find, compare, and discover the tools that shape modern music.
          </p>
          <div className="flex items-center gap-4">
            <a
              href="https://twitter.com"
              target="_blank"
              rel="noopener noreferrer"
              className="w-10 h-10 border border-white/10 rounded-full flex items-center justify-center hover:bg-white/5 transition-colors text-white/60 hover:text-white"
            >
              <Twitter className="w-4 h-4" />
            </a>
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="w-10 h-10 border border-white/10 rounded-full flex items-center justify-center hover:bg-white/5 transition-colors text-white/60 hover:text-white"
            >
              <Github className="w-4 h-4" />
            </a>
            <Link
              href="/rss"
              className="w-10 h-10 border border-white/10 rounded-full flex items-center justify-center hover:bg-white/5 transition-colors text-white/60 hover:text-white"
              title="RSS Feed"
            >
              <Rss className="w-4 h-4" />
            </Link>
          </div>
          <div>
            <h4 className="text-[10px] uppercase tracking-[0.2em] text-white/40 mb-8">Site Links</h4>
            <ul className="space-y-4 text-sm text-white/60">
              {siteLinks.map(link => (
                <li key={link.href + link.label}>
                  <Link href={link.href} className="hover:text-white transition-colors">
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Categories (col 2) */}
        <div>
          <h4 className="text-[10px] uppercase tracking-[0.2em] text-white/40 mb-8">Categories</h4>
          <ul className="space-y-4 text-sm text-white/60">
            {categoryLinks.map(link => (
              <li key={link.href}>
                <Link href={link.href} className="hover:text-white transition-colors">
                  {link.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        {/* Tools (col 3) */}
        <div>
          <h4 className="text-[10px] uppercase tracking-[0.2em] text-white/40 mb-8">Tools</h4>
          <ul className="space-y-4 text-sm text-white/60">
            <li>
              <Link href="/search" className="hover:text-white transition-colors">Search</Link>
            </li>
            <li>
              <Link href="/compare" className="hover:text-white transition-colors">Compare Tools</Link>
            </li>
            <li>
              <Link href="/submit" className="hover:text-white transition-colors">Submit a Tool</Link>
            </li>
            <li>
              <Link href="/rss" className="hover:text-white transition-colors flex items-center gap-2">
                <Rss className="w-3 h-3" />
                RSS Feed
              </Link>
            </li>
          </ul>
        </div>
      </div>

      <div className="max-w-7xl mx-auto mt-32 pt-12 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-4">
        <p className="text-[10px] text-white/20 tracking-[0.2em] uppercase">
          &copy; 2026 Audio Software Hub. All rights reserved.
        </p>
        <div className="flex items-center gap-4">
          <span className="text-[10px] text-white/20 uppercase tracking-widest">Built for producers, by producers.</span>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]" />
            <span className="text-green-500 text-[10px] font-bold tracking-widest">SYSTEM ONLINE</span>
          </div>
        </div>
      </div>
    </footer>
  )
}
