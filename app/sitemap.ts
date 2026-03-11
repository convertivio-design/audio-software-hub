import { MetadataRoute } from 'next'
import { products, categories } from '@/lib/data'
import fs from 'fs'
import path from 'path'

const BASE_URL = 'https://audio-software-hub.com'

export default function sitemap(): MetadataRoute.Sitemap {
  // Load releases
  let releases: { slug: string }[] = []
  try {
    const raw = fs.readFileSync(path.join(process.cwd(), 'data', 'releases.json'), 'utf-8')
    releases = JSON.parse(raw)
  } catch {}

  const staticRoutes: MetadataRoute.Sitemap = [
    { url: BASE_URL, lastModified: new Date(), changeFrequency: 'daily', priority: 1.0 },
    { url: `${BASE_URL}/categories`, lastModified: new Date(), changeFrequency: 'weekly', priority: 0.9 },
    { url: `${BASE_URL}/search`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.5 },
  ]

  const categoryRoutes: MetadataRoute.Sitemap = categories.map(cat => ({
    url: `${BASE_URL}/categories/${cat.slug}`,
    lastModified: new Date(),
    changeFrequency: 'weekly' as const,
    priority: 0.8,
  }))

  const productRoutes: MetadataRoute.Sitemap = products.map(p => ({
    url: `${BASE_URL}/products/${p.slug}`,
    lastModified: new Date(),
    changeFrequency: 'monthly' as const,
    priority: 0.6,
  }))

  const releaseRoutes: MetadataRoute.Sitemap = releases.map(r => ({
    url: `${BASE_URL}/releases/${r.slug}`,
    lastModified: new Date(),
    changeFrequency: 'weekly' as const,
    priority: 0.7,
  }))

  return [...staticRoutes, ...categoryRoutes, ...productRoutes, ...releaseRoutes]
}
