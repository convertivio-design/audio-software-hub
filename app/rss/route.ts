import { NextResponse } from 'next/server'
import { getSanitizedReleases, type SanitizedRelease } from '@/lib/data'

export const dynamic = 'force-dynamic'

type Release = SanitizedRelease

export async function GET() {
  const releases: Release[] = getSanitizedReleases()

  const BASE = 'https://audio-software-hub.com'
  const items = releases.slice(0, 20).map(r => `
    <item>
      <title><![CDATA[${r.name}${r.developer ? ` by ${r.developer}` : ''}]]></title>
      <link>${BASE}/releases/${r.slug}</link>
      <guid>${BASE}/releases/${r.slug}</guid>
      <description><![CDATA[${r.shortDescription}]]></description>
      <pubDate>${new Date(r.dateAdded ?? Date.now()).toUTCString()}</pubDate>
      <category>${r.categoryId}</category>
    </item>
  `).join('')

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Audio Software Hub — New Releases</title>
    <link>${BASE}</link>
    <description>Latest music production software releases tracked by Audio Software Hub</description>
    <language>en-us</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <atom:link href="${BASE}/rss" rel="self" type="application/rss+xml"/>
    ${items}
  </channel>
</rss>`

  return new NextResponse(xml, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  })
}
