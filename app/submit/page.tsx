import Link from 'next/link'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Submit a Music Production Tool — Audio Software Hub',
  description: 'Know a plugin, DAW, or audio tool missing from our directory? Submit it and our team will review it within 48 hours.',
}

export default function SubmitPage() {
  return (
    <div className="min-h-screen">
      {/* Breadcrumb */}
      <div className="border-b border-white/10 px-6 md:px-20 lg:px-40 py-4">
        <div className="flex items-center gap-2 text-[10px] font-bold uppercase tracking-[0.2em]">
          <Link href="/" className="text-white/40 hover:text-white transition-colors">Home</Link>
          <span className="text-white/20">/</span>
          <span className="text-white/60">Submit a Tool</span>
        </div>
      </div>

      {/* Header */}
      <div className="px-6 md:px-20 lg:px-40 pt-20 pb-16 border-b border-white/10">
        <div className="flex items-center gap-2 mb-6">
          <span className="w-2 h-2 rounded-full border border-white/40" />
          <span className="text-[10px] uppercase tracking-widest text-white/60">Directory</span>
        </div>
        <h1 className="text-5xl md:text-6xl font-light tracking-tight font-display mb-6">Submit a Tool</h1>
        <p className="text-lg text-white/50 font-light leading-relaxed max-w-2xl">
          Know a plugin, DAW, or audio tool missing from our directory? Let us know.
        </p>
      </div>

      {/* Form */}
      <div className="px-6 md:px-20 lg:px-40 py-20">
        <div className="max-w-2xl">
          <form action="#" method="GET" className="space-y-8">

            {/* Tool Name */}
            <div className="space-y-2">
              <label htmlFor="tool-name" className="block text-[10px] uppercase tracking-widest text-white/40">
                Tool Name
              </label>
              <input
                id="tool-name"
                name="name"
                type="text"
                required
                className="w-full bg-transparent border border-white/10 px-4 py-3 text-sm text-white placeholder:text-white/20 outline-none focus:border-white/30 transition-colors"
                placeholder="e.g. Serum 2"
              />
            </div>

            {/* Developer */}
            <div className="space-y-2">
              <label htmlFor="developer" className="block text-[10px] uppercase tracking-widest text-white/40">
                Developer / Company
              </label>
              <input
                id="developer"
                name="developer"
                type="text"
                required
                className="w-full bg-transparent border border-white/10 px-4 py-3 text-sm text-white placeholder:text-white/20 outline-none focus:border-white/30 transition-colors"
                placeholder="e.g. Xfer Records"
              />
            </div>

            {/* Category */}
            <div className="space-y-2">
              <label htmlFor="category" className="block text-[10px] uppercase tracking-widest text-white/40">
                Category
              </label>
              <select
                id="category"
                name="category"
                required
                className="w-full bg-black border border-white/10 px-4 py-3 text-sm text-white outline-none focus:border-white/30 transition-colors appearance-none cursor-pointer"
              >
                <option value="" disabled selected className="text-white/20">Select a category</option>
                <option value="daw">DAW</option>
                <option value="synth">Synthesizer</option>
                <option value="effects">Effects</option>
                <option value="sampler">Sampler</option>
                <option value="drums">Drum Machine</option>
                <option value="mastering">Mastering</option>
                <option value="midi">MIDI &amp; Utilities</option>
                <option value="guitar">Guitar &amp; Bass</option>
                <option value="vocal">Vocal</option>
                <option value="utility">Utility</option>
                <option value="experimental">Experimental</option>
              </select>
            </div>

            {/* Official URL */}
            <div className="space-y-2">
              <label htmlFor="url" className="block text-[10px] uppercase tracking-widest text-white/40">
                Official URL
              </label>
              <input
                id="url"
                name="url"
                type="url"
                required
                className="w-full bg-transparent border border-white/10 px-4 py-3 text-sm text-white placeholder:text-white/20 outline-none focus:border-white/30 transition-colors"
                placeholder="https://example.com"
              />
            </div>

            {/* Price + Price Type */}
            <div className="grid grid-cols-2 gap-6">
              <div className="space-y-2">
                <label htmlFor="price" className="block text-[10px] uppercase tracking-widest text-white/40">
                  Price <span className="text-white/20">(optional)</span>
                </label>
                <input
                  id="price"
                  name="price"
                  type="number"
                  min="0"
                  step="0.01"
                  className="w-full bg-transparent border border-white/10 px-4 py-3 text-sm text-white placeholder:text-white/20 outline-none focus:border-white/30 transition-colors"
                  placeholder="e.g. 199"
                />
              </div>
              <div className="space-y-2">
                <label htmlFor="price-type" className="block text-[10px] uppercase tracking-widest text-white/40">
                  Price Type
                </label>
                <select
                  id="price-type"
                  name="priceType"
                  required
                  className="w-full bg-black border border-white/10 px-4 py-3 text-sm text-white outline-none focus:border-white/30 transition-colors appearance-none cursor-pointer"
                >
                  <option value="" disabled selected className="text-white/20">Select</option>
                  <option value="free">Free</option>
                  <option value="one-time">One-Time</option>
                  <option value="subscription">Subscription</option>
                  <option value="freemium">Freemium</option>
                </select>
              </div>
            </div>

            {/* Short Description */}
            <div className="space-y-2">
              <label htmlFor="description" className="block text-[10px] uppercase tracking-widest text-white/40">
                Short Description <span className="text-white/20">(200 chars max)</span>
              </label>
              <textarea
                id="description"
                name="description"
                required
                maxLength={200}
                rows={4}
                className="w-full bg-transparent border border-white/10 px-4 py-3 text-sm text-white placeholder:text-white/20 outline-none focus:border-white/30 transition-colors resize-none"
                placeholder="Briefly describe what this tool does..."
              />
            </div>

            {/* Submit */}
            <div className="pt-4">
              <button
                type="submit"
                className="px-10 py-4 bg-white text-black text-xs font-bold uppercase tracking-widest hover:bg-zinc-200 transition-colors cursor-pointer"
              >
                Submit Tool
              </button>
            </div>
          </form>

          {/* Notice */}
          <div className="mt-12 pt-8 border-t border-white/10">
            <p className="text-[10px] uppercase tracking-widest text-white/30">
              Our team reviews submissions within 48 hours.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
