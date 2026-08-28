import { Metadata } from 'next'
import { notFound } from 'next/navigation'
import Link from 'next/link'
import { ChevronLeft, Clock, Tag, Star, BookOpen, ArrowRight, ExternalLink } from 'lucide-react'
import { guides, getGuideBySlug, getAllGuideSlugs, Guide } from '@/lib/guides'

interface Props {
  params: Promise<{ slug: string }>
}

export async function generateStaticParams() {
  const slugs = getAllGuideSlugs()
  return slugs.map(slug => ({ slug }))
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const resolvedParams = await params
  const guide = getGuideBySlug(resolvedParams.slug)
  
  if (!guide) {
    return { title: 'Guide Not Found' }
  }

  return {
    title: `${guide.title} | Audio Software Hub`,
    description: guide.description,
    openGraph: {
      title: guide.title,
      description: guide.description,
      type: 'article',
      publishedTime: guide.datePublished,
      modifiedTime: guide.lastUpdated,
      tags: guide.targetKeywords,
    },
    other: {
      'article:published_time': guide.datePublished || '',
      'article:modified_time': guide.lastUpdated || '',
      'article:tag': guide.targetKeywords.join(','),
    },
  }
}

function getRelatedGuides(currentGuide: Guide, limit: number = 3): Guide[] {
  return guides
    .filter(g => g.id !== currentGuide.id && g.category === currentGuide.category)
    .slice(0, limit)
}

export default async function GuidePage({ params }: Props) {
  const resolvedParams = await params
  const guide = getGuideBySlug(resolvedParams.slug)

  if (!guide) {
    notFound()
  }

  const relatedGuides = getRelatedGuides(guide)
  const categoryIcons: Record<Guide['category'], string> = {
    'Best Of & Roundups': '🏆',
    'Comparisons': '⚖️',
    'Workflow': '🔧',
    'Industry Trends': '📈',
  }

  return (
    <article className="min-h-screen bg-black text-white">
      {/* Breadcrumb */}
      <nav className="px-6 py-4 border-b border-white/5" aria-label="Breadcrumb">
        <div className="max-w-4xl mx-auto flex items-center gap-2 text-[10px] uppercase tracking-widest">
          <Link href="/" className="text-white/40 hover:text-white transition-colors">Home</Link>
          <ChevronLeft className="w-3 h-3 text-white/20" />
          <Link href="/guides" className="text-white/40 hover:text-white transition-colors">Guides</Link>
          <ChevronLeft className="w-3 h-3 text-white/20" />
          <span className="text-white/60 truncate max-w-[200px]" aria-current="page">{guide.title}</span>
        </div>
      </nav>

      {/* Guide Header */}
      <header className="px-6 py-16 border-b border-white/5">
        <div className="max-w-4xl mx-auto">
          <div className="flex flex-wrap items-center gap-3 mb-6">
            <span className="text-2xl">{categoryIcons[guide.category]}</span>
            <Link
              href={`/guides?category=${guide.category.toLowerCase().replace(/ & /g, '-').replace(/\s+/g, '-')}`}
              className="px-3 py-1 border border-white/20 rounded-full text-[10px] uppercase tracking-widest text-white/50 hover:border-white/40 hover:text-white transition-all"
            >
              {guide.category}
            </Link>
            <span className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-[10px] uppercase tracking-widest text-white/40 italic">
              {guide.contentType}
            </span>
            {guide.featured && (
              <span className="flex items-center gap-1 px-3 py-1 bg-yellow-500/10 border border-yellow-500/30 rounded-full text-[10px] uppercase tracking-widest text-yellow-400">
                <Star className="w-3 h-3 fill-current" />
                Featured
              </span>
            )}
            <span className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-[10px] uppercase tracking-widest text-white/40">
              {guide.buyerStage}
            </span>
          </div>

          <h1 className="text-4xl md:text-5xl lg:text-6xl font-light tracking-tight leading-[1.15] font-display mb-8">
            {guide.title}
          </h1>

          <p className="text-xl text-white/50 font-light leading-relaxed mb-10 max-w-3xl">
            {guide.description}
          </p>

          <div className="flex flex-wrap items-center gap-6 text-sm text-white/40">
            <div className="flex items-center gap-2">
              <Clock className="w-4 h-4" />
              <span>{guide.readingTime} min read</span>
            </div>
            {guide.datePublished && (
              <div className="flex items-center gap-2">
                <BookOpen className="w-4 h-4" />
                <time dateTime={guide.datePublished}>
                  {new Date(guide.datePublished).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
                </time>
              </div>
            )}
            {guide.lastUpdated && guide.lastUpdated !== guide.datePublished && (
              <div className="flex items-center gap-2">
                <span className="text-[10px] uppercase tracking-widest">Updated</span>
                <time dateTime={guide.lastUpdated}>
                  {new Date(guide.lastUpdated).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })}
                </time>
              </div>
            )}
          </div>

          {/* Target Keywords */}
          <div className="mt-8 flex flex-wrap gap-2">
            {guide.targetKeywords.map((keyword, i) => (
              <span key={i} className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-[10px] uppercase tracking-widest text-white/50">
                {keyword}
              </span>
            ))}
          </div>
        </div>
      </header>

      {/* Guide Content */}
      <div className="px-6 py-16">
        <div className="max-w-4xl mx-auto">
          {/* Table of Contents */}
          <aside className="hidden lg:block fixed left-[calc(50%+720px)] top-40 w-64" aria-label="Table of contents">
            <nav className="bg-black/50 border border-white/10 rounded-lg p-4">
              <h3 className="text-[10px] uppercase tracking-widest text-white/60 mb-3">On This Page</h3>
              <ol className="space-y-2 text-sm">
                <li><a href="#introduction" className="text-white/50 hover:text-white transition-colors">Introduction</a></li>
                <li><a href="#main-content" className="text-white/50 hover:text-white transition-colors">Main Content</a></li>
                <li><a href="#conclusion" className="text-white/50 hover:text-white transition-colors">Conclusion & Recommendation</a></li>
              </ol>
            </nav>
          </aside>

          {/* Introduction */}
          <section id="introduction" className="prose prose-invert max-w-none mb-16">
            <h2 className="text-2xl font-light tracking-tight mb-6 font-display">Introduction</h2>
            <p className="text-white/60 leading-relaxed text-lg mb-6">
              {guide.description}
            </p>
            <p className="text-white/50 leading-relaxed">
              This guide covers everything you need to know about <strong>{guide.targetKeywords.join(' and ')}</strong>. 
              Whether you're a beginner looking for your first plugin or a seasoned pro evaluating alternatives, 
              we've tested and analyzed the top options so you don't have to.
            </p>
          </section>

          {/* Main Content Placeholder */}
          <section id="main-content" className="prose prose-invert max-w-none mb-16">
            <h2 className="text-2xl font-light tracking-tight mb-6 font-display">Main Content</h2>
            
            <div className="bg-white/5 border border-white/10 rounded-lg p-8 mb-8">
              <p className="text-white/60 leading-relaxed mb-4">
                <strong>Content coming soon.</strong> This guide is currently being researched and written by our editorial team.
              </p>
              <p className="text-white/50 leading-relaxed mb-4">
                We're building comprehensive, tested content for each guide. The final version will include:
              </p>
              <ul className="list-disc list-inside space-y-2 text-white/50 mb-4">
                <li>Hands-on testing results and screenshots</li>
                <li>Comparison tables with specs, pricing, and features</li>
                <li>Workflow integration tips and best practices</li>
                <li>Pros/cons based on real production use</li>
                <li>Direct links to official downloads and trials</li>
              </ul>
              <p className="text-white/50 leading-relaxed">
                Check back soon, or <a href="/categories" className="text-cyan-400 hover:text-cyan-300 underline">browse the directory</a> for individual tool reviews.
              </p>
            </div>

            {/* Sample structure based on content type */}
            {guide.contentType === 'Hub & Spoke' && (
              <div className="space-y-12">
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">Top Recommendations</h3>
                  <p className="text-white/50 leading-relaxed mb-4">
                    Our top picks for {guide.targetKeywords[0]}, tested across workflow, sound quality, and value.
                  </p>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {[1, 2, 3, 4].map(i => (
                      <div key={i} className="p-4 bg-white/5 border border-white/10 rounded-lg">
                        <h4 className="font-medium mb-2">Tool Name {i}</h4>
                        <p className="text-white/40 text-sm">Description coming soon...</p>
                      </div>
                    ))}
                  </div>
                </section>
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">How to Choose</h3>
                  <p className="text-white/50 leading-relaxed">
                    Key factors to consider when selecting the right tool for your workflow and budget.
                  </p>
                </section>
              </div>
            )}

            {guide.contentType === 'Product Comparison' && (
              <div className="space-y-12">
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">Head-to-Head Comparison</h3>
                  <div className="overflow-x-auto">
                    <table className="w-full text-sm">
                      <thead>
                        <tr className="border-b border-white/10">
                          <th className="text-left py-2 px-3 font-medium text-white/60">Feature</th>
                          <th className="text-left py-2 px-3 font-medium text-white/60">Option A</th>
                          <th className="text-left py-2 px-3 font-medium text-white/60">Option B</th>
                        </tr>
                      </thead>
                      <tbody>
                        {[
                          ['Price', '$9.99/mo (Rent-to-Own)', 'Free / $80 Pro'],
                          ['Wavetable Engine', 'Classic wavetable', 'Spectral warping'],
                          ['Modulation', 'Drag & drop', 'Visual matrix'],
                          ['CPU Usage', 'High', 'Moderate'],
                          ['Presets', '1000+', '500+'],
                          ['Platforms', 'Win/Mac', 'Win/Mac/Linux'],
                        ].map((row, i) => (
                          <tr key={i} className="border-b border-white/5">
                            <td className="py-2 px-3 text-white/50">{row[0]}</td>
                            <td className="py-2 px-3 text-white/60">{row[1]}</td>
                            <td className="py-2 px-3 text-white/60">{row[2]}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </section>
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">Verdict</h3>
                  <p className="text-white/50 leading-relaxed">
                    Detailed verdict coming soon based on hands-on testing across multiple genres and workflows.
                  </p>
                </section>
              </div>
            )}

            {guide.contentType === 'Tutorial' && (
              <div className="space-y-12">
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">Step-by-Step Workflow</h3>
                  <p className="text-white/50 leading-relaxed mb-4">
                    Follow this workflow to achieve professional results in your own productions.
                  </p>
                  <ol className="space-y-6">
                    {[1, 2, 3, 4, 5].map(step => (
                      <li key={step} className="flex gap-4">
                        <span className="flex-shrink-0 w-8 h-8 rounded-full bg-white/10 border border-white/20 flex items-center justify-center font-medium text-white">
                          {step}
                        </span>
                        <div>
                          <h4 className="font-medium mb-1">Step {step}: Title Coming Soon</h4>
                          <p className="text-white/40 text-sm">Detailed instructions and screenshots coming soon...</p>
                        </div>
                      </li>
                    ))}
                  </ol>
                </section>
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">Pro Tips</h3>
                  <ul className="list-disc list-inside space-y-2 text-white/50">
                    <li>Tip 1: Optimize your workflow</li>
                    <li>Tip 2: Common mistakes to avoid</li>
                    <li>Tip 3: Advanced techniques</li>
                  </ul>
                </section>
              </div>
            )}

            {/* Default content for other types */}
            {guide.contentType !== 'Hub & Spoke' && guide.contentType !== 'Product Comparison' && guide.contentType !== 'Tutorial' && (
              <div className="space-y-12">
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">Key Insights</h3>
                  <p className="text-white/50 leading-relaxed mb-4">
                    Our analysis of {guide.targetKeywords.join(', ')} reveals several important findings:
                  </p>
                  <ul className="list-disc list-inside space-y-3 text-white/50">
                    <li>Insight 1: Detailed analysis coming soon</li>
                    <li>Insight 2: Data-driven comparison results</li>
                    <li>Insight 3: Practical recommendations for your workflow</li>
                  </ul>
                </section>
                <section>
                  <h3 className="text-xl font-medium tracking-tight mb-4 font-display">Detailed Breakdown</h3>
                  <p className="text-white/50 leading-relaxed mb-4">
                    Comprehensive breakdown of features, pricing, and use cases.
                  </p>
                  <div className="bg-white/5 border border-white/10 rounded-lg p-6">
                    <p className="text-white/50 text-center py-8">Full content coming soon</p>
                  </div>
                </section>
              </div>
            )}
          </section>

          {/* Conclusion */}
          <section id="conclusion" className="prose prose-invert max-w-none mb-16">
            <h2 className="text-2xl font-light tracking-tight mb-6 font-display">Conclusion & Recommendation</h2>
            <div className="bg-white/5 border border-white/10 rounded-lg p-8">
              <p className="text-white/60 leading-relaxed mb-4">
                <strong>Bottom line:</strong> Our final recommendation based on extensive testing will be published here.
              </p>
              <p className="text-white/50 leading-relaxed">
                In the meantime, explore related tools in our <a href="/categories" className="text-cyan-400 hover:text-cyan-300 underline">directory</a> 
                or check out the <a href="/guides" className="text-cyan-400 hover:text-cyan-300 underline">other guides</a> in this category.
              </p>
            </div>
          </section>

          {/* Related Guides */}
          {relatedGuides.length > 0 && (
            <section className="border-t border-white/5 pt-16">
              <h2 className="text-2xl font-light tracking-tight mb-8 font-display">Related Guides</h2>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {relatedGuides.map(related => (
                  <Link
                    key={related.slug}
                    href={`/guides/${related.slug}`}
                    className="group p-6 border border-white/10 hover:border-white/30 hover:bg-white/[0.02] transition-all"
                  >
                    <div className="flex items-center gap-2 mb-3">
                      <span className="text-xl">{categoryIcons[related.category]}</span>
                      <span className="text-[10px] px-2 py-0.5 border border-white/30 uppercase tracking-tighter text-white/40 italic">
                        {related.contentType}
                      </span>
                    </div>
                    <h3 className="text-lg font-medium tracking-tight font-display hover:text-white/80 transition-colors mb-2 line-clamp-2">
                      {related.title}
                    </h3>
                    <p className="text-sm text-white/40 leading-relaxed line-clamp-2">
                      {related.description}
                    </p>
                  </Link>
                ))}
              </div>
            </section>
          )}

          {/* CTA to Directory */}
          <section className="mt-16 p-8 bg-white/5 border border-white/10 rounded-lg text-center">
            <h3 className="text-xl font-light tracking-tight mb-4 font-display">Looking for a specific tool?</h3>
            <p className="text-white/50 mb-6 max-w-2xl mx-auto">
              Browse our directory of 3,000+ plugins, DAWs, and instruments with detailed specs, pricing, and reviews.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link
                href="/categories"
                className="w-full sm:w-auto px-8 py-4 bg-white text-black font-bold text-sm rounded-full hover:bg-zinc-200 transition-all uppercase tracking-widest cursor-pointer text-center"
              >
                Browse Directory
              </Link>
              <Link
                href="/search"
                className="w-full sm:w-auto px-8 py-4 border border-white/20 text-white font-bold text-sm rounded-full hover:bg-white/5 transition-all uppercase tracking-widest cursor-pointer text-center"
              >
                Search Tools
              </Link>
            </div>
          </section>
        </div>
      </div>

      {/* JSON-LD Schema */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'Article',
            headline: guide.title,
            description: guide.description,
            datePublished: guide.datePublished,
            dateModified: guide.lastUpdated || guide.datePublished,
            author: {
              '@type': 'Organization',
              name: 'Audio Software Hub',
            },
            publisher: {
              '@type': 'Organization',
              name: 'Audio Software Hub',
              logo: {
                '@type': 'ImageObject',
                url: 'https://audiosoftwarehub.online/logo.png',
              },
            },
            mainEntityOfPage: {
              '@type': 'WebPage',
              '@id': `https://audiosoftwarehub.online/guides/${guide.slug}`,
            },
            keywords: guide.targetKeywords.join(', '),
          }),
        }}
      />
    </article>
  )
}