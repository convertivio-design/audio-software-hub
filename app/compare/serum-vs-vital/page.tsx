import type { Metadata } from 'next'
import Link from 'next/link'

export const metadata: Metadata = {
  title: "Serum vs Vital: Which Wavetable Synth is Right for You?",
  description: "Compare Xfer Records Serum vs Vital Audio Vital. Features, pricing, sound quality, and value for wavetable synthesis.",
  alternates: { canonical: '/compare/serum-vs-vital' },
}

const productSchema = {
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Serum vs Vital Wavetable Synth Comparison",
  "description": "Compare Xfer Records Serum vs Vital Audio Vital. Features, pricing, sound quality, and value for wavetable synthesis.",
  "url": "https://audiosoftwarehub.online/compare/serum-vs-vital",
  "numberOfItems": 2,
  "itemListElement": [
    {
      "@type": "Product",
      "name": "Xfer Records Serum",
      "description": "Industry standard wavetable synth with massive preset ecosystem. Used by top producers worldwide.",
      "brand": { "@type": "Brand", "name": "Xfer Records" },
      "category": "Synthesizer",
      "offers": {
        "@type": "Offer",
        "price": "189",
        "priceCurrency": "USD"
      }
    },
    {
      "@type": "Product",
      "name": "Vital Audio Vital",
      "description": "Open-source wavetable synth with advanced modulation and spectral warping. Free tier is incredibly capable.",
      "brand": { "@type": "Brand", "name": "Vital Audio" },
      "category": "Synthesizer",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }
    }
  ]
}

function SerumVsVitalPage() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(productSchema) }}
      />
<div className="min-h-screen">
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-4">
        <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-[0.2em]">
          <Link href="/" className="text-white/40 hover:text-white transition-colors">Home</Link>
          <span className="text-white/20">/</span>
          <Link href="/compare" className="text-white/40 hover:text-white transition-colors">Compare</Link>
          <span className="text-white/20">/</span>
          <span className="text-white/60">Serum vs Vital</span>
        </div>
      </div>
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-16">
        <div className="max-w-4xl mx-auto">
          <span className="text-[10px] px-2 py-0.5 border border-white/30 text-white/50 uppercase tracking-widest mb-6 inline-block">Comparison</span>
          <h1 className="text-5xl md:text-6xl font-bold uppercase tracking-tighter font-display text-white mb-6">Serum vs Vital</h1>
          <p className="text-xl text-white/50 font-light mb-8">Which wavetable synth is right for you?</p>
        </div>
      </div>
      <div className="px-6 md:px-20 lg:px-40 py-16">
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
            <div className="border border-white/10 p-8">
              <h2 className="text-2xl font-light font-display text-white mb-2">Xfer Records Serum</h2>
              <p className="text-3xl font-bold text-white mb-4">$189</p>
              <p className="text-white/50 text-sm leading-relaxed mb-6">Industry standard wavetable synth with massive preset ecosystem. Used by top producers worldwide.</p>
              <Link href="/products/serum" className="inline-block px-6 py-3 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors uppercase tracking-widest">View Details</Link>
            </div>
            <div className="border border-white/10 p-8">
              <h2 className="text-2xl font-light font-display text-white mb-2">Vital Audio Vital</h2>
              <p className="text-3xl font-bold text-white mb-4">Free / $25 / $80</p>
              <p className="text-white/50 text-sm leading-relaxed mb-6">Open-source wavetable synth with advanced modulation. Free tier is incredibly capable.</p>
              <Link href="/products/vital" className="inline-block px-6 py-3 bg-white text-black text-xs font-bold rounded-full hover:bg-zinc-200 transition-colors uppercase tracking-widest">View Details</Link>
            </div>
          </div>

          <div className="space-y-6">
            <div className="border border-white/10">
              <div className="grid grid-cols-3 text-[10px] font-bold uppercase tracking-widest border-b border-white/10">
                <div className="p-4 text-white/60">Feature</div>
                <div className="p-4 text-white/60 text-center">Serum</div>
                <div className="p-4 text-white/60 text-center">Vital</div>
              </div>
              <div className="grid grid-cols-3 text-sm border-b border-white/5">
                <div className="p-4 text-white/80">Wavetable Engine</div>
                <div className="p-4 text-white/50 text-center">Excellent</div>
                <div className="p-4 text-white/50 text-center">Excellent</div>
              </div>
              <div className="grid grid-cols-3 text-sm border-b border-white/5">
                <div className="p-4 text-white/80">Modulation System</div>
                <div className="p-4 text-white/50 text-center">Powerful</div>
                <div className="p-4 text-white/50 text-center">Superior</div>
              </div>
              <div className="grid grid-cols-3 text-sm border-b border-white/5">
                <div className="p-4 text-white/80">Preset Ecosystem</div>
                <div className="p-4 text-white/50 text-center">Vast</div>
                <div className="p-4 text-white/50 text-center">Growing</div>
              </div>
              <div className="grid grid-cols-3 text-sm border-b border-white/5">
                <div className="p-4 text-white/80">Pricing</div>
                <div className="p-4 text-white/50 text-center">$$$</div>
                <div className="p-4 text-white/50 text-center">$ or Free</div>
              </div>
              <div className="grid grid-cols-3 text-sm border-b border-white/5">
                <div className="p-4 text-white/80">Built-in FX</div>
                <div className="p-4 text-white/50 text-center">5 FX</div>
                <div className="p-4 text-white/50 text-center">12+ FX</div>
              </div>
              <div className="grid grid-cols-3 text-sm">
                <div className="p-4 text-white/80">Spectrum/Scope</div>
                <div className="p-4 text-white/50 text-center">Basic</div>
                <div className="p-4 text-white/50 text-center">Advanced</div>
              </div>
            </div>

            <div className="border border-white/10 p-8">
              <h2 className="text-2xl font-light font-display text-white mb-4">Verdict</h2>
              <p className="text-white/50 leading-relaxed mb-4"><strong className="text-white/80">Choose Serum</strong> if you want the industry standard with the largest preset library and educational resources. Its ubiquity in professional production is unmatched.</p>
              <p className="text-white/50 leading-relaxed"><strong className="text-white/80">Choose Vital</strong> if you want a more modern wavetable synth with superior modulation options at a lower price. The free tier gives you 75 presets, 3 wavetables, and all features.</p>
            </div>
          </div>

          <div className="mt-12">
            <Link href="/compare?a=serum&b=vital" className="inline-flex items-center gap-2 px-6 py-3 border border-white/20 text-white text-xs font-bold rounded-full hover:bg-white/10 transition-colors uppercase tracking-widest">Interactive Comparison â†’</Link>
            <Link href="/categories/synthesizers" className="inline-flex items-center gap-2 px-6 py-3 border border-white/20 text-white text-xs font-bold rounded-full hover:bg-white/10 transition-colors uppercase tracking-widest ml-4">All Synthesizers</Link>
          </div>
        </div>
      </div>
    </div>
    </>
  )
}

export default SerumVsVitalPage
