import Link from 'next/link'

export default function NotFound() {
  return (
    <div className="min-h-[60vh] flex flex-col items-center justify-center px-6 text-center">
      <p className="text-[200px] font-bold tracking-tighter text-white/[0.03] leading-none font-display select-none">404</p>
      <h1 className="text-3xl font-bold text-white mb-3 tracking-tighter uppercase font-display -mt-16">Not Found</h1>
      <p className="text-white/40 mb-10 max-w-sm text-sm font-light">
        This page does not exist. The plugin might have been discontinued, or the URL is incorrect.
      </p>
      <div className="flex gap-4">
        <Link
          href="/"
          className="px-8 py-3 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors uppercase tracking-widest"
        >
          Go Home
        </Link>
        <Link
          href="/categories"
          className="px-8 py-3 border border-white/20 text-white text-xs font-bold rounded-full hover:bg-white/5 transition-colors uppercase tracking-widest"
        >
          Browse Categories
        </Link>
      </div>
    </div>
  )
}
