import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

export const dynamic = 'force-dynamic'

interface Release {
  id: string
  slug: string
  name: string
  developer?: string | null
  shortDescription: string
  dateAdded: string
  officialUrl: string
  categoryId: string
}

export async function GET() {
  let releases: Release[] = []
  try {
    const raw = fs.readFileSync(path.join(process.cwd(), 'data', 'releases.json'), 'utf-8')
    releases = JSON.parse(raw)
  } catch {}

  const BASE = 'https://audio-software-hub.com'
  const items = releases.slice(0, 20).map(r => `
    <item>
      <title><![CDATA[${r.name}${r.developer ? ` by ${r.developer}` : ''}]]></title>
      <link>${BASE}/releases/${r.slug}</link>
      <guid>${BASE}/releases/${r.slug}</guid>
      <description><![CDATA[${r.shortDescription}]]></description>
      <pubDate>${new Date(r.dateAdded).toUTCString()}</pubDate>
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
