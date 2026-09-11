'use client'

import { useState } from 'react'

const TABS = [
  { id: 'summary', label: 'Executive Summary' },
  { id: 'market', label: 'Market Sizing' },
  { id: 'customers', label: 'Customer Universe' },
  { id: 'ma', label: 'M&A & Integration' },
  { id: 'directions', label: 'Six Directions' },
  { id: 'spending', label: 'Spending Benchmarks' },
] as const

type TabId = (typeof TABS)[number]['id']

const MONO = 'font-mono text-white/80'

function Card({ sub, title, children }: { sub: string; title: string; children: React.ReactNode }) {
  return (
    <div className="bg-white/5 border border-white/10 p-5">
      <div className="text-[10px] font-bold uppercase tracking-widest text-white/40 mb-2">{sub}</div>
      <div className="text-white font-semibold mb-2">{title}</div>
      <div className="text-white/60 text-sm leading-relaxed">{children}</div>
    </div>
  )
}

function Note({ tone = 'info', title, children }: { tone?: 'info' | 'warn' | 'danger'; title: string; children: React.ReactNode }) {
  const border = tone === 'warn' ? 'border-l-amber-400' : tone === 'danger' ? 'border-l-red-500' : 'border-l-blue-400'
  return (
    <div className={`border ${border} border-l-4 bg-white/5 p-4 my-5`}>
      <div className="text-white text-sm font-semibold mb-1">{title}</div>
      <div className="text-white/60 text-sm leading-relaxed">{children}</div>
    </div>
  )
}

function ExecutiveSummary() {
  return (
    <div className="space-y-5">
      <p className="text-white/70 leading-relaxed">
        The global music industry is undergoing a structural operational crisis driven by transaction volume inflation, relentless catalog consolidation, and fragmented legacy back-office infrastructure. The operational challenge highlighted by Concord Music&rsquo;s recruitment mandate for its distribution subsidiary Stem signals an industry-wide bottleneck: independent record labels, music publishers, distributors, and catalog consolidators are struggling under the weight of processing billions of monthly streaming micro-transactions across disparate databases, multi-jurisdictional contract structures, and asynchronous delivery formats.
      </p>
      <p className="text-white/70 leading-relaxed">
        The global music rights management market represents a <strong className="text-white">$12.4 billion</strong> opportunity in 2025, projected to grow to <strong className="text-white">$23.8 billion</strong> by 2034 at an <strong className="text-white">8.3%</strong> Compound Annual Growth Rate (CAGR). Concurrently, the specific market for royalty accounting and management software stands at <strong className="text-white">$4.2 billion</strong> in 2025, expanding at a <strong className="text-white">9.8%</strong> CAGR toward <strong className="text-white">$9.8 billion</strong> by 2034. Despite this significant technology market size, an estimated <strong className="text-white">$2.5 billion</strong> in global music royalties remain uncollected or trapped in unclaimed &ldquo;black box&rdquo; accounts annually due to mismatched metadata, non-standardized licensing formats, and incomplete royalty statement reconciliations.
      </p>
      <p className="text-white/70 leading-relaxed">
        This report evaluates six prospective business directions designed to solve these systemic inefficiencies: <strong className="text-white">CatalogSync</strong> (a music-native iPaaS), <strong className="text-white">RoyaltyMind</strong> (an AI royalty anomaly engine), <strong className="text-white">ContractParser</strong> (an LLM music contract intelligence platform), <strong className="text-white">DistroOps Dashboard</strong> (a supply-chain visibility tool), <strong className="text-white">AI Dev Governance Kit</strong> (enterprise developer policy/tooling), and <strong className="text-white">Meridian Music Tech</strong> (a technical product consulting firm).
      </p>
      <p className="text-white/70 leading-relaxed">
        The analysis indicates that launching a boutique technical consulting firm (<strong className="text-white">Meridian Music Tech</strong>) represents the optimal strategic entry point. This service-led wedge provides immediate non-dilutive cash flow, grants direct access to client database schemas, and offers low-risk validation for productizing a dual-engine B2B SaaS suite: <strong className="text-white">CatalogSync</strong> for backend middleware integration and <strong className="text-white">RoyaltyMind</strong> for automated streaming royalty anomaly detection.
      </p>
    </div>
  )
}

function MarketSizing() {
  const rows: [string, string, string, string, string, string][] = [
    ['TAM — Global Music Rights Management', '$12.40B', '$23.80B (2034)', '8.3% (2026–2034)', 'Cloud deployment (62.5% share) · Streaming growth (>84% of revenue)', 'MarketIntelo'],
    ['SAM — Royalty Management & Accounting', '$4.20B', '$9.80B (2034)', '9.8% (2026–2034)', 'Automated DSR ingestion · Regulatory compliance (MMA, EU Copyright)', 'DataIntelo'],
    ['Adjacent — Music Copyrights & Licensing', '$5.12B', '$16.33B (2034)', '19.8% (2026–2034)', 'Digital distribution rights · Audio fingerprinting · CMOs', 'Intel Market Research'],
    ['Adjacent — Music Licensing Services', '$4.50B', '$9.70B (2031)', '9.5% (2026–2031)', 'Sync licensing ($3.8B) · DRM solutions ($2.6B)', 'Deep Market Insights'],
    ['SOM — Mid-Market Independent Rights Holders', '$185M', '$420M (2030)', '17.8% (2025–2030)', 'Indie labels, publishers, distributors upgrading legacy back-offices', 'Enterprise Benchmarks'],
  ]

  return (
    <div className="space-y-5">
      <p className="text-white/70 leading-relaxed">
        The global music software and rights management ecosystem spans several distinct software categories. The addressable customer base encompasses over <strong className="text-white">300</strong> major and mid-market catalog consolidators, <strong className="text-white">10,000+</strong> independent record labels and publishers, <strong className="text-white">500+</strong> digital distributors, and millions of independent artists generating micro-transactions.
      </p>

      <div className="overflow-x-auto border border-white/10">
        <table className="w-full text-sm min-w-[720px]">
          <thead>
            <tr className="border-b border-white/10 bg-white/5 text-left">
              <th className="p-3 text-[10px] font-bold uppercase tracking-widest text-white/40">Market scope</th>
              <th className="p-3 text-[10px] font-bold uppercase tracking-widest text-white/40">2025</th>
              <th className="p-3 text-[10px] font-bold uppercase tracking-widest text-white/40">Projected</th>
              <th className="p-3 text-[10px] font-bold uppercase tracking-widest text-white/40">CAGR</th>
              <th className="p-3 text-[10px] font-bold uppercase tracking-widest text-white/40">Growth drivers</th>
              <th className="p-3 text-[10px] font-bold uppercase tracking-widest text-white/40">Source</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r[0]} className="border-b border-white/5 last:border-b-0 align-top">
                <td className="p-3 text-white/80">{r[0]}</td>
                <td className="p-3 text-white/70 font-mono whitespace-nowrap">{r[1]}</td>
                <td className="p-3 text-white/70 whitespace-nowrap">{r[2]}</td>
                <td className="p-3 text-white/70 whitespace-nowrap">{r[3]}</td>
                <td className="p-3 text-white/50">{r[4]}</td>
                <td className="p-3 text-white/40 whitespace-nowrap">{r[5]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

function CustomerUniverse() {
  const tiers = [
    ['Catalog consolidators & institutional buyers', '~300 major and large independent label groups (e.g., Concord, BMG, Believe, Beggars Group, PIAS, Reservoir Media, Primary Wave, Hipgnosis) managing catalogs ranging from 100,000 to over 3 million tracks.'],
    ['Independent record labels & publishers', '~10,000 mid-sized commercially active independent entities globally requiring recurring monthly royalty accounting and distribution management.'],
    ['Digital distributors & aggregators', '~500 B2B and DIY distributors (e.g., DistroKid, TuneCore, CD Baby, Symphonic, Empire, Stem) processing release metadata and revenue delivery pipelines.'],
    ['Independent creators & production studios', 'Over 8 million individual artists, songwriters, and boutique production houses utilizing self-service split and payout management interfaces.'],
  ]

  return (
    <div className="space-y-5">
      <p className="text-white/70 leading-relaxed">
        The total customer base needing automated rights and integration software can be segmented across <strong className="text-white">four distinct tiers</strong>:
      </p>
      <div className="space-y-4">
        {tiers.map(([t, d], i) => (
          <div key={t} className="bg-white/5 border border-white/10 p-5">
            <div className="text-[10px] font-bold uppercase tracking-widest text-white/40 mb-2">Tier {i + 1}</div>
            <div className="text-white font-semibold mb-2">{t}</div>
            <div className="text-white/60 text-sm leading-relaxed">{d}</div>
          </div>
        ))}
      </div>
    </div>
  )
}

function MAIntegration() {
  return (
    <div className="space-y-5">
      <p className="text-white/70 leading-relaxed">
        Capital deployment in the independent music sector has transformed recorded music and publishing catalogs into <strong className="text-white">yield-generating financial assets</strong>. Institutional capital inflows are illustrated by Concord&rsquo;s <strong className="text-white">$500 million</strong> Asset-Backed Securitization (ABS) upsize with Apollo Global Management to acquire Round Hill Music Royalty Fund, adding 150,000 tracks and 50 sub-catalogs. Comparable consolidation activity across Hipgnosis, Reservoir Media, Primary Wave, Downtown Music Holdings, and BMG demonstrates an ongoing roll-up trend.
      </p>
      <p className="text-white/70 leading-relaxed">
        Post-acquisition integration represents a primary operational bottleneck for acquiring companies. When a music platform acquires a catalog, incoming rights and financial data arrive stored in incompatible schemas, legacy SQL databases, custom FileMaker installations, or unstandardized spreadsheets. Re-keying contract terms, normalizing artist royalty splits, and re-linking International Standard Recording Codes (ISRCs) to International Standard Musical Work Codes (ISWCs) across disparate Digital Service Provider (DSP) feeds typically takes between <strong className="text-white">6 to 18 months</strong>. During this integration window, cash distributions stall, audit exposure increases, and unmatched royalties flow into DSP &ldquo;black box&rdquo; holding accounts.
      </p>
      <Note tone="warn" title="The spend that friction drives">
        Catalog acquirers allocate <strong className="text-white">$200,000 to over $1,000,000 per transaction</strong> on technical data re-mapping and custom integration engineering.
      </Note>
    </div>
  )
}

function SixDirections() {
  const directions = [
    ['CatalogSync', 'A music-native iPaaS for backend middleware integration.'],
    ['RoyaltyMind', 'An AI royalty anomaly engine for streaming payout detection.'],
    ['ContractParser', 'An LLM music contract intelligence platform.'],
    ['DistroOps Dashboard', 'A supply-chain visibility tool.'],
    ['AI Dev Governance Kit', 'Enterprise developer policy and tooling.'],
    ['Meridian Music Tech', 'A technical product consulting firm.'],
  ]

  return (
    <div className="space-y-5">
      <p className="text-white/70 leading-relaxed">
        Six prospective business directions were evaluated to solve the systemic inefficiencies across royalty processing, contract intelligence, and catalog integration.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {directions.map(([name, desc]) => (
          <div key={name} className="bg-white/5 border border-white/10 p-5">
            <div className="text-white font-semibold mb-1">{name}</div>
            <div className="text-white/60 text-sm leading-relaxed">{desc}</div>
          </div>
        ))}
      </div>
      <Note title="Recommended entry point">
        <strong className="text-white">Meridian Music Tech</strong> (consulting-first) is the optimal strategic wedge: immediate non-dilutive cash flow, direct access to client database schemas, and low-risk validation for productizing a dual-engine B2B SaaS — <strong className="text-white">CatalogSync</strong> (middleware integration) + <strong className="text-white">RoyaltyMind</strong> (royalty anomaly detection).
      </Note>
    </div>
  )
}

function SpendingBenchmarks() {
  return (
    <div className="space-y-5">
      <p className="text-white/70 leading-relaxed">
        Enterprise music companies spend between <strong className="text-white">1.5% and 4.0%</strong> of annual net revenue on technology infrastructure, back-office enterprise resource planning (ERP) software, and data engineering. Mid-market independent labels ($10M to $50M in annual revenue) allocate <strong className="text-white">$150,000 to $600,000</strong> annually for software licensing, hosting, and specialized royalty accounting platforms. Large consolidators managing multi-million-track portfolios routinely spend upwards of <strong className="text-white">$2 million to $5 million per year</strong> when bespoke software development and external M&amp;A integration consulting are included.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card sub="Enterprise" title="1.5% – 4.0% of revenue">
          Annual net revenue spent on tech infrastructure, ERP, and data engineering.
        </Card>
        <Card sub="Mid-market labels" title="$150K – $600K / year">
          Software licensing, hosting, and specialized royalty accounting platforms ($10M–$50M revenue).
        </Card>
        <Card sub="Large consolidators" title="$2M – $5M / year">
          Bespoke software development plus external M&amp;A integration consulting.
        </Card>
      </div>
    </div>
  )
}

export default function MusicRightsReportTabs() {
  const [active, setActive] = useState<TabId>('summary')

  return (
    <div>
      <div className="flex gap-6 border-b border-white/10 overflow-x-auto mb-10">
        {TABS.map((t) => (
          <button
            key={t.id}
            onClick={() => setActive(t.id)}
            className={`shrink-0 px-1 pb-3 text-xs font-bold uppercase tracking-widest transition-colors border-b-2 ${
              active === t.id ? 'text-white border-white' : 'text-white/40 border-transparent hover:text-white'
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      <div className="max-w-4xl">
        {active === 'summary' && <ExecutiveSummary />}
        {active === 'market' && <MarketSizing />}
        {active === 'customers' && <CustomerUniverse />}
        {active === 'ma' && <MAIntegration />}
        {active === 'directions' && <SixDirections />}
        {active === 'spending' && <SpendingBenchmarks />}
      </div>
    </div>
  )
}
