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
