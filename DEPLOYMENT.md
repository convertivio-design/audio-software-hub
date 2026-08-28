# AudioSoftwareHub Deployment & Automation Guide

## Project Overview
- **Domain**: `audiosoftwarehub.online`
- **Vercel Project**: `audiosoftwarehub.online` (ID: `prj_HLKzzEhw9TEBGPC2IoO14OgEORDl`)
- **GitHub Repo**: `convertivio-design/audio-software-hub`
- **Framework**: Next.js 14 + Tailwind + TypeScript
- **Data Files**: `data/releases.json`, `data/products.json`, `data/scraper-status.json`

## Vercel Configuration
- **Production URL**: https://audiosoftwarehub.online
- **Vercel Project Owner**: `projectsinternal`
- **Build Command**: `pnpm build`
- **Install Command**: `pnpm install`
- **Node Version**: 24.x
- **Framework Preset**: Other

## Required GitHub Secrets
Configure these in GitHub repo settings → Secrets and variables → Actions:

| Secret | Description | Source |
|--------|-------------|--------|
| `FIRECRAWL_API_KEY` | Firecrawl API key for scraping | Firecrawl Dashboard |
| `VERCEL_TOKEN` | Vercel access token | Vercel Account Settings → Tokens |
| `VERCEL_ORG_ID` | Vercel organization ID | `vercel inspect` or project settings |
| `VERCEL_PROJECT_ID` | Vercel project ID | `vercel inspect` or project settings |
| `VERCEL_GIT_EMAIL` | Git email for automated commits | Any valid email |
| `INDEXNOW_KEY` | Bing IndexNow API key | Bing Webmaster Tools |

## Local Development

### Prerequisites
- Node.js 18.18+ (Node 20 recommended)
- Python 3.11+
- pnpm 8+
- Firecrawl API key

### Setup
```bash
cd audio-software-hub-master
pnpm install

# Install Python dependencies
pip install -r requirements.txt

# Create .env file
echo "FIRECRAWL_API_KEY=your_key_here" > .env
```

### Run Scraper Manually
```bash
# From audio-software-hub-master directory
python scripts/scrape_releases.py

# Dry run (no write)
python scripts/scrape_releases.py --dry-run

# Scrape KVR database (one-time bulk)
python scripts/scrape_kvr.py --pages 10 --max 500
```

### Local Development Server
```bash
cd audio-software-hub-master
pnpm dev
# Opens http://localhost:3000
```

## Automation Pipeline

### Scraper Schedule
- **Runs**: Every 2 days at 06:00 UTC
- **Workflow**: `.github/workflows/scrape-releases.yml`
- **Trigger**: Scheduled + Manual (`workflow_dispatch`)

### Pipeline Steps
1. **Scrape Listings** - Fetch article links from KVR, BPB, Rekkerd
2. **Scrape Articles** - Use Firecrawl to get full content
3. **Parse & Validate** - Extract structured data, filter junk
4. **Update JSON** - Merge new releases into `data/releases.json`
5. **Git Commit** - Commit `releases.json` + `scraper-status.json`
6. **Vercel Deploy** - Build and deploy to production
7. **IndexNow Ping** - Notify Bing of sitemap changes
8. **Verification** - Confirm live site shows latest release

### Scraper Sources
| Source | URL | Pattern |
|--------|-----|---------|
| KVR Audio News | https://www.kvraudio.com/news/ | `kvraudio.com/product/` |
| BPB Free VST | https://bedroomproducersblog.com/category/free-vst-plugins/ | `bedroomproducersblog.com/20\d\d/` |
| Rekkerd | https://www.rekkerd.org/ | `rekkerd.org/20\d\d/` |

### Data Flow
```
Source Sites → Firecrawl Scrape → Parse/Validate → releases.json → Git Commit → Vercel Deploy → Live Site
```

### Output: `data/releases.json`
Each release entry:
```json
{
  "id": "abc123",
  "slug": "plugin-name",
  "name": "Plugin Name",
  "developer": "Brand Name",
  "categoryId": "synth",
  "price": 0,
  "priceType": "free",
  "shortDescription": "Description...",
  "longDescription": "Full description...",
  "officialUrl": "https://...",
  "rating": null,
  "ratingCount": 0,
  "isNew": true,
  "isFeatured": false,
  "os": ["Windows", "macOS"],
  "formats": ["VST3", "AU"],
  "features": [],
  "pros": [],
  "cons": ["New - limited reviews"],
  "tags": ["synth"],
  "targetAudience": "Music producers and audio engineers",
  "dateAdded": "2026-08-25T06:00:00.000Z",
  "sourceTitle": "Original Article Title"
}
```

## Guides Section (NEW)
- **Route**: `/guides` (index) and `/guides/[slug]` (individual)
- **Content**: 15 SEO-optimized guides in `Content n Docs/ASH_SEO_Guides/`
- **Data**: `lib/guides.ts` with full metadata
- **Sitemap**: Auto-included in `app/sitemap.ts`
- **Navigation**: Added to Navbar as "Guides"

### Guide Categories
1. **Best Of & Roundups** (5 guides)
2. **Comparisons** (4 guides)
3. **Workflow** (4 guides)
4. **Industry Trends** (2 guides)

## Post-Launch Checklist
After each automated run:
- [ ] New releases appear on homepage "New Releases" section
- [ ] Individual release pages work at `/releases/[slug]`
- [ ] Sitemap updated at `https://audiosoftwarehub.online/sitemap.xml`
- [ ] RSS feed updated at `https://audiosoftwarehub.online/rss.xml`
- [ ] No build errors in GitHub Actions
- [ ] Vercel deployment successful
- [ ] IndexNow ping sent (check Bing Webmaster Tools)

## Troubleshooting

### Scraper fails at "Firecrawl CLI not found"
- Ensure `npm install -g firecrawl-cli` runs in workflow
- Check Firecrawl CLI version compatibility

### Scraper fails at "FIRECRAWL_API_KEY not set"
- Verify secret exists in GitHub repo settings
- Check Firecrawl account has credits

### Scraper finds zero candidates
- Source site HTML may have changed
- Check `scripts/scrape_releases.py` link_pattern regexes
- Run locally with `--dry-run` to debug

### Git commit fails
- Ensure `VERCEL_GIT_EMAIL` secret is set
- Check `GITHUB_TOKEN` has write permissions (default)
- Verify branch protection allows Actions bot

### Vercel deploy fails
- Verify all Vercel secrets are correct
- Check `vercel.json` build command matches
- Ensure project not paused or over quota

### Site shows stale content
- Check `vercel alias` correctly set to `audiosoftwarehub.online`
- Verify deployment URL in workflow logs
- Clear Vercel cache if needed

## Manual Vercel Deploy
```bash
cd audio-software-hub-master
pnpm build
npx vercel --prod --token=$VERCEL_TOKEN
npx vercel alias set <deployment-url> audiosoftwarehub.online --token=$VERCEL_TOKEN
```

## KVR Database Scraper (One-time)
For bulk product catalog updates:
```bash
python scripts/scrape_kvr.py --pages 30 --max 3000 --delay 1.5
# Outputs to data/products.json
```

## Monitoring
- **GitHub Actions**: Check `Actions` tab for run history (every 2 days)
- **Vercel Dashboard**: View deployments, functions, analytics
- **Scraper Status**: `data/scraper-status.json` shows last run details
- **Google Search Console**: Monitor indexing of new releases
- **Bing Webmaster Tools**: Verify IndexNow pings received

## Contact & Escalation
- **Primary**: Alistair (owner)
- **Vercel Account**: projectsinternal
- **GitHub Org**: convertivio-design
- **Firecrawl**: Account billing admin
- **Bing IndexNow**: Bing Webmaster Tools

## Known Issues
1. **GitHub Actions Billing**: Periodically check GitHub billing status - org lock prevents scheduled runs
2. **Firecrawl Credits**: Monitor usage - each scrape consumes credits
3. **Source Site Changes**: KVR/BPB/Rekkerd may change HTML requiring regex updates
4. **Vercel Build Time**: Large product catalog may hit build time limits