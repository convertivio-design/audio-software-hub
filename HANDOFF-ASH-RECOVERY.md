# ASH Recovery Handoff

## Current State

- Repo: `C:\Users\DELL\Documents\DevProjects\audio-software-hub`
- GitHub: `convertivio-design/audio-software-hub`
- Vercel project: `audiosoftwarehub.online`
- Workflow: `Scrape Releases & Deploy`
- Latest manual run: `24948398929` -> **success**

## What Was Fixed

- GitHub billing lock issue resolved (workflow can run again).
- Workflow now installs required tools before scrape/deploy:
  - Firecrawl CLI
  - pnpm
- Workflow now reads/uses `FIRECRAWL_API_KEY` secret correctly.
- Scraper now passes API key explicitly to Firecrawl commands.
- Scraper reliability hardened:
  - writes `data/scraper-status.json`
  - fails fast when auth/source scraping is broken
  - supports `--dry-run`
  - avoids wiping release history on no-new-release cycles
- Vercel deploy step now uses archive mode:
  - `vercel deploy --prebuilt --archive=tgz --prod ...`
  - fixes Vercel file-count limit error.
- Local build verification passed after OG route runtime fix.

## Follow-Up (Next Session)

1. Monitor next **scheduled** workflow run (not manual) and confirm it is green.
2. Verify freshness after that run:
   - `data/scraper-status.json` updated
   - `data/releases.json` reflects expected changes
   - homepage new releases section looks current
   - `https://audiosoftwarehub.online/sitemap.xml` returns 200
3. If schedule fails, inspect run logs first before code changes.

## One-Line Prompt For New Chat

Continue from `HANDOFF-ASH-RECOVERY.md` in `C:/Users/DELL/Documents/DevProjects/audio-software-hub`; do not redo diagnosis, just monitor the next scheduled run and verify site freshness end-to-end.
