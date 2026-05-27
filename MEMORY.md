# Audio Software Hub — agent memory (ASH)

Last updated: 2026-04-26

## Production + deploy

- **Site:** `https://audiosoftwarehub.online/`
- **Repo:** `https://github.com/convertivio-design/audio-software-hub`
- **Release scrape + deploy workflow:** `.github/workflows/scrape-releases.yml` (GitHub Actions)
- **Trigger (local):** `gh workflow run scrape-releases.yml --ref master`
- **Note:** GitHub MCP `actions_run_trigger` may return **403** for workflow dispatch; `gh` works when authenticated.

## Release data corruption guardrails (2026-04-26)

These commits are the “don’t ship scraped garbage” stack:

- `d913f15` — broaden junk detection + run `npm run validate:releases` in CI after scraping.
- `0cca768` — reject **IPv4/IPv6 address artifacts** in scraped release fields (KVR-style blocked pages were surfacing IPs as “product names”).
- `d94f224` — workflow auto-commit updating `data/releases.json` after the scrape/deploy run.

Runtime defense (even if `data/releases.json` is bad): `lib/data.ts` sanitizes releases before UI uses them.

## Quick verification commands (Windows PowerShell)

```powershell
# HTTP
(Invoke-WebRequest -UseBasicParsing https://audiosoftwarehub.online/).StatusCode
(Invoke-WebRequest -UseBasicParsing https://audiosoftwarehub.online/sitemap.xml).StatusCode

# Obvious junk tokens
$content = (Invoke-WebRequest -UseBasicParsing https://audiosoftwarehub.online/).Content
@('[MENU]','menuhttp','menuhttps','close-menu').ForEach({ "$_= $(([regex]::Matches($content,$_,'IgnoreCase')).Count)" })

# IP artifacts (should be 0 in visible HTML after fix)
@{
  ipv4 = ([regex]::Matches($content,'\b(?:\d{1,3}\.){3}\d{1,3}\b').Count)
  ipv6 = ([regex]::Matches($content,'\b(?:[a-f0-9]{1,4}:){2,}[a-f0-9]{1,4}\b','IgnoreCase').Count)
}

# Freshness proxy: ensure newest release slug from `origin/master` appears in HTML
$slug = (node -e "const {execSync}=require('child_process'); const j=execSync('git show origin/master:data/releases.json',{encoding:'utf8'}); console.log(JSON.parse(j)[0].slug);")
[regex]::IsMatch($content, [regex]::Escape($slug), 'IgnoreCase')
```

## Local validation

```powershell
npm run validate:releases
```
