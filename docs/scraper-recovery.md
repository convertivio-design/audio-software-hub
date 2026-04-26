# Scraper Recovery Runbook

## Current Pipeline

`source sites -> scripts/scrape_releases.py -> data/releases.json -> GitHub Actions -> commit -> Vercel deploy -> homepage / releases / sitemap`

## Confirmed Incident State

- Workflow: `.github/workflows/scrape-releases.yml`
- GitHub issue tracker: Linear `NEW-87`
- Vercel project: `audiosoftwarehub.online`
- GitHub repo: `convertivio-design/audio-software-hub`
- Confirmed blocker on 2026-04-25: scheduled GitHub Actions runs fail before job start because the account/org is locked due to a billing issue.

## Recovery Order

1. Clear the GitHub account/org billing lock.
2. Confirm repository secrets exist:
   - `FIRECRAWL_API_KEY`
   - `VERCEL_TOKEN`
   - `VERCEL_ORG_ID`
   - `VERCEL_PROJECT_ID`
   - `VERCEL_GIT_EMAIL`
3. Run the workflow manually from GitHub Actions.
4. Verify the job installs Python deps, installs Firecrawl CLI, runs `scripts/scrape_releases.py`, commits `data/releases.json` and `data/scraper-status.json`, then deploys to Vercel.
5. Confirm production:
   - Homepage new releases changed or `data/scraper-status.json` shows a fresh successful run.
   - `/releases/[slug]` pages for any new entries return 200.
   - `/sitemap.xml` returns 200 and includes release URLs.

## Backfill Policy

Do not backfill a month of releases until one normal scheduled run succeeds. After that, backfill in capped batches and keep duplicate protection enabled.

## Monitoring Note

Healthy scheduled runs update `data/scraper-status.json`, so the workflow may commit and redeploy even when `data/releases.json` has no new releases. This is intentional while NEW-87 is open because ASH needs a visible heartbeat after the silent failure.

## Local Checks

```powershell
python -m py_compile scripts/scrape_releases.py
pnpm build
gh run list --repo convertivio-design/audio-software-hub --workflow "Scrape Releases & Deploy" --limit 10
```

## Failure Modes To Check

- GitHub Actions billing/account lock.
- Missing `FIRECRAWL_API_KEY` secret.
- Firecrawl CLI install failure.
- Scraper finds zero candidates due to changed source markup.
- `data/releases.json` changes but deploy does not complete.
- Vercel production target is canceled or not aliased to `audiosoftwarehub.online`.
