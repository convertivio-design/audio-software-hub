# 🚨 Deploy Discipline — Don't Let This Happen Again

## The Mistake (May 2026)

> **All guide pages, comparison pages, domain URL fix, navbar updates, and enriched product data were sitting UNCOMMITTED in the local repo.**
> The live site (`audiosoftwarehub.online`) showed NONE of it for weeks.
> The user thought the site was updated. It was not.

**Root cause:** Work was done locally but never `git commit` + `git push`ed. The deployment pipeline requires those two steps — without them, nothing reaches the live site.

---

## The Golden Rule

> **Uncommitted work = Undone work. The live site only reflects what's been committed AND pushed.**

---

## The Workflow (every session)

### At the end of EVERY coding session:

```bash
# 1. Check what's changed
git status

# 2. Review changes
git diff --stat

# 3. Commit with a descriptive message
git add -A
git commit -m "clear description of what changed"

# 4. Push to trigger deployment
git push

# 5. Log the deployment in DEPLOY-LOG.md
#    (open C:\Users\DELL\Documents\newsletter-monetization-master\DEPLOY-LOG.md
#     and add an entry)

# 6. Verify the live site loaded the changes
#    (visit the URL or check GitHub Actions deployment status)
```

### At the start of EVERY session:

```bash
# 1. Check if there's stale/uncommitted work from last time
git status

# 2. Pull latest from remote
git pull

# 3. Check DEPLOY-LOG.md for what's deployed and what's pending
```

---

## Where Are The Tools?

| What | Where |
|------|-------|
| **Deploy Log** (master record of all deployments) | `C:\Users\DELL\Documents\newsletter-monetization-master\DEPLOY-LOG.md` |
| **Commit-discipline Cursor rule** | `C:\Users\DELL\.cursor\rules\commit-discipline.mdc` |
| **Commit-discipline Claude Code skill** | `C:\Users\DELL\.claude\skills\commit-discipline.md` |
| **This file** (workspace copy for agents) | Root of this repo (`DEPLOY-DISCIPLINE.md`) |

---

## Active Repos That Need Discipline

- `C:\Users\DELL\Documents\DevProjects\audio-software-hub` → audiosoftwarehub.online
- `C:\Users\DELL\Documents\DevProjects\musicscientists.digital` → musicscientists.digital
- `C:\Users\DELL\Documents\DevProjects\musictech.today` → musictech.today

---

## Quick Reference: Common Commands

```bash
# Check status
git status

# See what's changed
git diff --stat

# Stage all
git add -A

# Commit
git commit -m "description"

# Push (triggers deployment)
git push

# Pull latest
git pull

# See recent commits
git log --oneline -5
```

---

*Last updated: 2026-05-27*

---
## 2026-09-03 update (read this first)

- **Default branch is `master`.** `main` was deleted — never create it again. Push to `master` only.
- Vercel auto-deploys every push to `master` (GitHub integration). Do NOT add a manual Vercel deploy step to Actions — that caused double-deploy failures.
- The Actions workflow now only: scrapes → validates → commits → pings IndexNow. A heartbeat commit keeps the schedule alive.
- Missing `package-lock.json` was breaking `npm ci` in Actions-adjacent tooling — it is now committed.

---

## 2026-09-11 — Root cause of the "site not updating" problem (FIXED)

**What was actually wrong:** the Vercel project setting `commandForIgnoringBuildStep`
was inverted. It read:

```
if [ "$VERCEL_ENV" == "preview" ]; then exit 1; else exit 0; fi
```

In Vercel, `exit 0` = IGNORE the build, `exit 1` = PROCEED. So it cancelled every
**production** build and built only previews — the exact opposite of what was wanted.
Every push to `master` was silently skipped by Vercel. This is why the site appeared
"not to update."

**Fixed** to the correct logic (preview skipped, production built):

```
if [ "$VERCEL_ENV" == "preview" ]; then exit 0; else exit 1; fi
```

**Verified** 2026-09-11: pushed to `master`, Vercel built automatically and reached
`READY` in ~60s (deployment `dpl_3xBBfMSsYpdduzdzcrKixLN1SUgU`).

### Consequences — READ THIS BEFORE CHANGING DEPLOY SETUP

1. **There is exactly ONE deploy path: Vercel's GitHub integration.**
   Push to `master` → Vercel builds and publishes. That is the whole mechanism.

2. **Do NOT add any Vercel deploy step to GitHub Actions.** The old
   `.github/workflows/force-deploy.yml` did that and was **deleted on 2026-09-11**.
   It existed only as a workaround for the bug above and caused double-deploys.
   It must not be recreated.

3. **The `VERCEL_PROJECT_ID` secret was stale for ~6 months** — it pointed at
   `music-tech-directory` (`prj_WuAyNjBRTX0ZbhuBckjma2zHCu0H`) instead of this
   project. It was corrected on 2026-09-11 to `prj_HLKzzEhw9TEBGPC2IoO14OgEORDl`.
   No workflow should need it now; the Git integration does not read it.

4. **`.github/workflows/scrape-releases.yml` is the only workflow left**, and it
   deliberately does NOT deploy. It scrapes → validates → commits → pings IndexNow,
   then waits for the Git integration to publish. Its header comment is accurate.

5. **If the site stops updating again**, check in this order:
   - Vercel dashboard → project `audiosoftwarehub.online` → Settings → Git →
     "Ignored Build Step". It must exit **1** for production.
   - `git log origin/master` vs the latest deployment on Vercel.
   - The `Scrape Releases & Deploy` workflow runs (it commits data every 2 days).
