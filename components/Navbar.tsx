'use client'

import Link from 'next/link'
import { usePathname, useRouter } from 'next/navigation'
import { useState, useRef, useEffect } from 'react'
import { Search, Menu, X, Grid3X3 } from 'lucide-react'

const navLinks = [
  { href: '/categories', label: 'Categories' },
  { href: '/categories/daws', label: 'DAWs' },
  { href: '/categories/synthesizers', label: 'Synths' },
  { href: '/categories/effects', label: 'Effects' },
  { href: '/compare', label: 'Compare' },
]

export function Navbar() {
  const pathname = usePathname()
  const router = useRouter()
  const [menuOpen, setMenuOpen] = useState(false)
  const [searchOpen, setSearchOpen] = useState(false)
  const [query, setQuery] = useState('')
  const inputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (searchOpen) inputRef.current?.focus()
  }, [searchOpen])

  function handleSearch(e: React.FormEvent) {
    e.preventDefault()
    if (query.trim()) {
      router.push(`/search?q=${encodeURIComponent(query.trim())}`)
      setSearchOpen(false)
      setQuery('')
    }
  }

  return (
    <header className="sticky top-0 z-50 bg-black/80 backdrop-blur-md border-b border-white/10">
      <div className="max-w-7xl mx-auto px-6 h-16 md:h-20 flex items-center justify-between">
        {/* Logo + Nav */}
        <div className="flex items-center gap-12">
          <Link href="/" className="flex items-center gap-2 text-white">
            <Grid3X3 className="w-5 h-5" />
            <span className="text-lg font-bold tracking-tighter">audiosoftwarehub</span>
          </Link>
          <nav className="hidden md:flex items-center gap-8">
            {navLinks.map(link => (
              <Link
                key={link.href}
                href={link.href}
                className={`text-xs font-medium uppercase tracking-widest transition-colors ${
                  pathname === link.href
                    ? 'text-white'
                    : 'text-white/60 hover:text-white'
                }`}
              >
                {link.label}
              </Link>
            ))}
          </nav>
        </div>

        {/* Right actions */}
        <div className="flex items-center gap-4">
          {/* Inline search (desktop) */}
          {searchOpen ? (
            <form onSubmit={handleSearch} className="hidden md:flex items-center gap-2">
              <input
                ref={inputRef}
                value={query}
                onChange={e => setQuery(e.target.value)}
                placeholder="Search plugins, DAWs..."
                className="w-56 bg-white/5 border border-white/10 px-3 py-1.5 text-sm text-white placeholder-white/30 focus:outline-none focus:border-white/30 transition-all"
              />
              <button
                type="button"
                onClick={() => setSearchOpen(false)}
                className="text-white/40 hover:text-white"
              >
                <X className="w-4 h-4" />
              </button>
            </form>
          ) : (
            <button
              onClick={() => setSearchOpen(true)}
              className="hidden md:flex items-center gap-3 px-4 py-2 border border-white/20 rounded-full text-sm text-white/50 hover:border-white/40 transition-all"
            >
              <Search className="w-4 h-4" />
              <span>Search</span>
              <kbd className="text-[10px] opacity-50">&#8984;K</kbd>
            </button>
          )}

          {/* Mobile search icon */}
          <Link
            href="/search"
            className="md:hidden p-2 text-white/60 hover:text-white transition-colors"
          >
            <Search className="w-5 h-5" />
          </Link>

          {/* Mobile menu toggle */}
          <button
            onClick={() => setMenuOpen(!menuOpen)}
            className="md:hidden p-2 text-white/60 hover:text-white transition-colors"
          >
            {menuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {menuOpen && (
        <div className="md:hidden border-t border-white/10 px-6 py-4 animate-fade-in">
          <form onSubmit={handleSearch} className="flex gap-2 mb-4">
            <input
              value={query}
              onChange={e => setQuery(e.target.value)}
              placeholder="Search..."
              className="flex-1 bg-white/5 border border-white/10 px-3 py-2 text-sm text-white placeholder-white/30 focus:outline-none focus:border-white/30"
            />
            <button
              type="submit"
              className="px-4 py-2 bg-white text-black text-xs font-bold uppercase tracking-widest hover:bg-zinc-200 transition-colors"
            >
              Go
            </button>
          </form>
          {navLinks.map(link => (
            <Link
              key={link.href}
              href={link.href}
              onClick={() => setMenuOpen(false)}
              className={`block px-3 py-2 text-xs font-bold uppercase tracking-widest transition-colors mb-1 ${
                pathname === link.href
                  ? 'text-white'
                  : 'text-white/60 hover:text-white'
              }`}
            >
              {link.label}
            </Link>
          ))}
        </div>
      )}
    </header>
  )
}
