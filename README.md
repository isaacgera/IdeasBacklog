# Capture Ideas

A mobile-first, installable **PWA** over the app-ideas backlog. Browse every idea
(filter by complexity, status, category, or search) and **capture new ideas on the go** —
each new idea is committed straight into `Ideas.md` via the GitHub API, so there's a single
source of truth shared by phone and laptop.

Hosted on **GitHub Pages** from this public `IdeasBacklog` repo.

## Files

| File | Purpose |
|---|---|
| `Ideas.md` | **Single source of truth** — the backlog, as markdown tables per complexity tier. |
| `Ideas.html` | The app: responsive board + capture form + PIN gate + GitHub-sync + PWA. |
| `manifest.webmanifest` | PWA manifest (name, theme, icons, standalone display). |
| `sw.js` | Service worker — offline app shell; network-first for `Ideas.md`. |
| `icons/` | PWA icons (192, 512, maskable). |
| `overview.html` | One-page summary of the app. |
| `userguide.html` | End-user guide (PIN, browsing, capturing, token setup, install, offline). |
| `serve.ps1` | Local dev server for testing over HTTP. |
| `scripts/make-icons.py` | Regenerates the PWA icons (stdlib only, no dependencies). |

## Backlog format

Ideas live under `## Simple` / `## Medium` / `## Complex` headings, one table each:

```
| Idea | Category | Description | Scope (v1) | Status |
```

- **Status:** `Idea` | `In Progress` | `Built` | `Parked` (a version may sit in parens, e.g. `Built (Capture Ideas v1.0.0)`).
- **Category:** Finance | Productivity | Health | Home | Learning | Utility | Work | AI/Agents | Devotional.

## Running locally

Serve over HTTP (not `file://`, since the page fetches `Ideas.md`):

```
./serve.ps1        # then open http://localhost:8090/Ideas.html
```

or use the VS Code **Live Server** extension.

## Capture setup (write access)

Browsing needs nothing. To save ideas from a device, add a GitHub **fine-grained token**
(scoped to only this repo, **Contents: Read & write**) in the app's **Settings**. The token
is stored only on that device and is never committed. See `userguide.html` for step-by-step.

## Security note

This repo is **public**, so `Ideas.md` is readable by anyone. The in-app PIN is a soft UI
gate, not data security — don't put anything sensitive in the backlog.

---

Powered by Forjé · © 2026 Isaac A Gera. All rights reserved.
