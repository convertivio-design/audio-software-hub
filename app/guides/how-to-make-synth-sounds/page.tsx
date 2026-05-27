import type { Metadata } from "next"
import Link from "next/link"

export const metadata: Metadata = {
  title: "How to Make Synth Sounds: A Beginner's Guide to Synthesis | Audio Software Hub",
  description: "Learn how to make synth sounds from scratch. Covers subtractive, FM, wavetable, and granular synthesis with step-by-step examples and recommended synths.",
  alternates: { canonical: "/guides/how-to-make-synth-sounds" },
  openGraph: {
    title: "How to Make Synth Sounds: A Beginner's Guide to Synthesis",
    description: "Learn how to make synth sounds from scratch covering subtractive, FM, wavetable, and granular synthesis.",
  },
}

export default function HowToMakeSynthSoundsPage() {
  return (
    <div className="min-h-screen px-6 md:px-20 lg:px-40 py-16 md:py-24">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({"@context":"https://schema.org","@type":"Article","headline":"How to Make Synth Sounds: A Beginner's Guide to Synthesis","description":"A complete beginner guide to synthesis.","datePublished":"2026-05-24","author":{"@type":"Organization","name":"Audio Software Hub"}})}} />
      <nav className="mb-10 text-sm text-white/40"><Link href="/" className="hover:text-white">Home</Link><span className="mx-2">/</span><Link href="/guides" className="hover:text-white">Guides</Link><span className="mx-2">/</span><span className="text-white/60">Synth Sounds</span></nav>
      <article className="max-w-3xl mx-auto">
        <h1 className="text-4xl md:text-5xl font-bold text-white mb-6 leading-tight">How to Make Synth Sounds: A Beginner's Guide to Synthesis</h1>
        <p className="text-white/50 text-sm mb-10">Updated May 24, 2026</p>
        <div className="text-white/70 space-y-6 leading-relaxed">
<p>Learning how to make synth sounds is one of the most rewarding skills in music production. This guide walks you through the fundamentals of sound synthesis and shows you how to create your first patches.</p>
<h2 className="text-xl font-bold text-white mt-8 mb-3">What Is Sound Synthesis?</h2>
<p>Sound synthesis is the electronic generation of audio signals. A synthesizer creates sound using oscillators generating raw waveforms: sine, sawtooth, square, and triangle. These are shaped by filters, envelopes, and effects. Modern software synths like <Link href="/products/serum" className="text-blue-400 hover:underline">Serum</Link>, <Link href="/products/vital" className="text-blue-400 hover:underline">Vital</Link>, and <Link href="/products/massive-x" className="text-blue-400 hover:underline">Massive X</Link> make synthesis accessible.</p>
<h2 className="text-xl font-bold text-white mt-8 mb-3">The Four Main Types of Synthesis</h2>
<p><strong>Subtractive:</strong> Start with rich waveform, remove frequencies via filter. Bass example: sawtooth + low-pass filter at 200Hz + envelope on cutoff + resonance.</p>
<p><strong>FM:</strong> One oscillator modulates another's frequency. Bell example: sine carrier 261Hz + modulator 14:1 ratio + quick decay envelope.</p>
<p><strong>Wavetable:</strong> Morph between waveforms. Pad example: morphing wavetable + slow envelope + LFO on filter + reverb.</p>
<p><strong>Granular:</strong> Break audio into tiny grains. Best for ambient and cinematic textures.</p>
<h2 className="text-xl font-bold text-white mt-8 mb-3">Terminology</h2>
<div className="border border-white/10 p-4 my-4 space-y-2 text-sm">
<div><strong>Oscillator (VCO):</strong> Generates raw waveform.</div>
<div><strong>Filter (VCF):</strong> Removes frequencies.</div>
<div><strong>Envelope (ADSR):</strong> Shapes parameters over time.</div>
<div><strong>LFO:</strong> Cyclic modulation source.</div>
</div>
<h2 className="text-xl font-bold text-white mt-8 mb-3">Best Synths for Learning</h2>
<ul className="list-disc pl-6 space-y-1">
<li><Link href="/products/serum" className="text-blue-400 hover:underline">Serum</Link> &mdash; Visual wavetable synth, huge community.</li>
<li><Link href="/products/vital" className="text-blue-400 hover:underline">Vital</Link> &mdash; Free, three oscillators. <Link href="/compare/serum-vs-vital" className="text-blue-400 hover:underline">Compare</Link></li>
<li><Link href="/products/pigments" className="text-blue-400 hover:underline">Pigments</Link> &mdash; Combines analog, wavetable, FM, granular.</li>
</ul>
<div className="border-t border-white/10 pt-6 mt-8">
<h3 className="font-bold text-white mb-3">Related Guides</h3>
<ul className="space-y-1">
<li><Link href="/guides/what-is-a-daw" className="text-blue-400 hover:underline">What is a DAW?</Link></li>
<li><Link href="/guides/best-free-serum-presets" className="text-blue-400 hover:underline">Best Free Serum Presets</Link></li>
</ul>
</div>
        </div>
      </article>
    </div>
  )
}