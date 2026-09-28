# Ideas Backlog — Session Log

## Session 1 — 28 Aug 2026

### Goal
Set up a reusable app-ideas backlog (source of truth + visual viewer) and agree a working framework for future builds.

### What we built
- **`Ideas.md`** — single source of truth. Ideas grouped by complexity tier (Simple / Medium / Complex), each row: `Idea | Category | Description | Scope (v1) | Status`.
  - Categories: Finance | Productivity | Health | Home | Learning | Utility | Work | AI/Agents.
  - Statuses: Idea | In Progress | Built | Parked. Versions embedded in status cell, e.g. `Built (v1.0.1)`.
- **`Ideas.html`** — viewer that reads `Ideas.md` live via `fetch` and parses the markdown tables. No hardcoded data.
  - Redesigned toolbar: segmented controls for Complexity and Status, a dropdown for Category (auto-built from data), a live "Showing X of Y" count, and a Clear-filters link.
  - Cards show complexity, category, status, and a blue version tag (parsed out of the status cell).
- **`serve.ps1`** — local server (port 8090) modeled on WealthOrah's, with `.md` MIME type. Kept as a fallback; Isaac uses the **Live Server** extension instead.

### Key decisions
- Viewer reads `Ideas.md` live (Option 1) — needs a local server / Live Server, not `file://`. Single source of truth kept.
- Merged the earlier "Markets" category into **Finance**.
- Marked shipped apps as **Built** with version tags: WealthOrah `v1.0.1`, Idea Board `v3`, ShiftPlanner `v4.0`. (ShiftPlanner version found in its `app.js` / `sw.js`.)

### Ideas added this session
- Finance/markets (from discussion): Position Size/Risk Calc, Market Hours & Status, Brokerage & Tax Estimator, Index Dashboard, Dual-Market Portfolio Tracker, Stock Comparison Tool, Company Analysis Workbench (enriched with a guided 10-min stock checklist), Index Analytics.
- From "40 digital products" image: Sinking Funds Planner, Bill & Subscription Tracker, Stock Analysis Checklist (10-min), Journaling App, Study/Homeschool Planner, Travel Planner + Packing List.
- **AI/Agents — Bucket A (in-Kiro helpers), tracked as ideas:** Session-Log Scribe (hook), PWA Readiness Checker, Ideas Backlog Curator, New App Scaffolder, Spec Reviewer.
- **Bucket B (AI features inside apps)** — parked in a labelled section for later (Stock Analysis Copilot, Finance Insights, Journaling Prompt, Recipe/Meal, Study Coach, Client Comms).

### Reference sections added to `Ideas.md`
- **Free APIs by purpose** — market data (Alpha Vantage, Finnhub, Twelve Data, CoinGecko), AI/NLP (OpenAI, Cohere, HF, Groq), weather, news, email. Note: keep API keys out of repo & client code.
- **UI/UX tech stacks** — comparison table (vanilla, React, Vue, Svelte, SolidJS, Angular, Next.js, Astro, Flutter) plus add-on layers (Tailwind, GSAP, Framer Motion, Three.js, D3/Chart.js, component libraries).

### Steering file updated (`~/.kiro/steering/identity-and-context.md`)
**Build standards** — at the start of every build, flag & agree:
1. **Rigour level** scaled to app tier (professional craftsmanship, not over-engineered).
2. **UI/UX stack** chosen and justified per app; field kept fully open, name the trade-offs (build step, Windows setup, PWA).
3. **Target platforms** — desktop/laptop web, mobile web, installable PWA, or native Android/iOS; pick lightest that fits; note web→native needs a rewrite.
4. **Monetization watch** — flag any strong candidate and offer to switch to a production-ready track.

**Build quality baseline** (applies during every build): data safety first, consistency across the app family, accessibility & responsiveness by default, verify-before-done, secrets discipline, finish by syncing docs.

**Visual & interaction design**: design tokens (CSS variables), light/dark theming (`prefers-color-scheme`), consistent motion/hover/focus feedback (~120–200ms), emphasis patterns (zoom one / dim others), depth & edges, respect `prefers-reduced-motion`, touch-friendly, tooltips & ARIA where they help, polish details (icons, empty/loading/error states).

**Documentation & delivery** (finishing an app properly): user-facing docs (User Guide + Presentation/demo + About/Help + README), developer docs (session log + SPEC files), versioning & changelog (single version constant, semver, bump PWA cache), branding & identity, licensing (**always ask** — no default), deployment (static host; test hosted not just local), data & privacy stance (local-first by default; flag any off-device data), browser & offline support.

### Notes / open items
- Couldn't run live browser/HTTP tests from Kiro this session — the terminal prepends a `cd ...;` line that cmd rejects (same shell-syntax snag as the Agent Toolkit session). Verified logic by inspection; Isaac confirmed the page renders well (toolbar + version tags).
- Board idea (drag-and-drop status like the team's Idea Board) discussed and parked for later.

### Next session
- Pick a first build from the backlog and run the 4-point Build-standards flag.
- Strong low-effort starters: Session-Log Scribe (Kiro hook) or a Simple Finance tool (Position Size Calc / Stock Analysis Checklist).

---

## Session 2 — 28 Aug 2026

### Goal
Clarify Kiro's five build/workflow modes and bake mode-selection guidance into the global steering file.

### What we did
- Walked through the five workflow modes — **Default (Vibe)**, **Plan**, **Quick Spec**, **Spec**, **Bug Fix** — with when to use each and their weaknesses.
- Mapped modes to the backlog's complexity tiers (Simple / Medium / Complex) and to real projects (WealthOrah, ShiftPlanner), including which mode to start in and when to shift.

### Steering file updated (`~/.kiro/steering/identity-and-context.md`)
Added a new section **"Choosing a build mode (pick it at the start of every task)"**, placed right after "How we work" and before "Projects worked on so far". It contains:
- **Mode definitions** — one-line purpose + best-fit for each of the five modes.
- **Starting mode by tier** table:
  - **Simple** → start in Default; shift to Quick Spec only if scope creeps.
  - **Medium** → start in Quick Spec; promote to full Spec if it's a keeper to ship/document; drop to Default for small tweaks.
  - **Complex** → start in Plan (agree stack/platform/rigour), then Spec to build and document.
  - **Any shipped app** → Default for everyday work; Bug Fix for defects; Quick Spec / Spec for genuinely new features.
- **Shift triggers** — scope growth promotes Default → Quick Spec/Spec; a tiny isolated change drops Spec → Default; a "bug" that's really a feature moves Bug Fix → Quick Spec/Spec; anything meant to ship should pass through Spec to keep SPEC files + SESSION-LOG as source of truth.

### Key decisions
- Ceremony scales to the app's complexity tier — don't over-spec a Simple tool or under-plan a Complex one.
- Forjé should name the chosen mode and why at the start of each task.
- Guidance deliberately tied to `Ideas.md` tiers and the SPEC/SESSION-LOG habit so it reinforces existing rules.

### Notes / open items
- Steering is `inclusion: always`, so the new section loads from the **next** session; the current session still ran on the pre-edit version.
- Edit confirmed written to the file; not yet exercised live in a session.

### Next session
- Optionally dry-run the new mode-selection step on a backlog idea (e.g. Position Size Calculator or Habit Tracker) to see it in action.

---

## Session 3 — 28 Aug 2026

### Goal
First real build off the backlog (the Bill Splitter, now **Splitzy**), plus adding a steering rule that keeps `Ideas.md` status in sync automatically-by-habit.

### What we did
- **Built Splitzy** (the Tip / Bill Splitter idea) in **Default (Vibe)** mode — vanilla HTML/CSS/JS, installable PWA, no build step. Full history in the project's own log at `Projects/Bill Splitter/SESSION-LOG.md`. Currently at **v1.2.1** (hotfix), pending Isaac's live re-check.
  - Iterations: v1.0.0 core → v1.1.0 (renamed Splitzy, currency selector, round-up fix, 2-col layout, multi-bill) → v1.2.0 (3-card layout, currency-toggle value fix + no negatives, per-bill dates, PNG/PDF export) → v1.2.1 (hotfix: an embedded `<script>` tag in the PDF export had broken script parsing, killing all JS).
- **Updated the Tip / Bill Splitter row** in `Ideas.md`: `Idea` → `In Progress (Splitzy v1.2.1)`, with refreshed Description/Scope (multi-bill, currency, dates, PNG/PDF, PWA).

### Steering file updated (`~/.kiro/steering/identity-and-context.md`)
Added a new section **"Keep the Ideas backlog status in sync (start and end of every build)"**, placed right after "Choosing a build mode". Chose **Option A** (a judgment-based steering rule) over hooks/scripts for now. It says:
- **Start of build:** find the matching `Ideas.md` row and move it **Idea → In Progress** when real work begins. **If no row exists, add it to the backlog first** (right tier/category/description/scope) — Isaac's caveat.
- **End of build:** set **Built** (with version, e.g. `Built (Splitzy v1.2.1)`) once shipped and verified, or **Parked** if shelved; keep description/scope honest if the app outgrew the idea.
- **Notes:** transitions need judgment (don't flip mechanically); editing `Ideas.md` is enough since `Ideas.html` reads it live; complements the existing "finish by syncing docs" step.

### Key decisions
- Went with **Option A** now; noted **Option B** (a SessionStart reminder hook) and **Option C** (the backlogged "Ideas Backlog Curator" agent) as future upgrades for stronger automation.
- Status stays **In Progress** for Splitzy until the v1.2.1 hotfix passes Isaac's live check, then flip to **Built**.

### Notes / open items
- Steering is `inclusion: always` → the new rule loads next session; applied manually this session by choice.
- Known environment constraint unchanged: can't run live browser tests here (Windows shell quirk), so Splitzy verified by inspection + Isaac's manual checks.

### Next session
- Confirm Splitzy v1.2.1 live check; if good, set `Ideas.md` to `Built (Splitzy v1.2.1)`.
- Optionally build **Option B** (SessionStart reminder hook) and/or start the **Ideas Backlog Curator** agent for fuller automation.

---

## Session 4 — 6 Sep 2026

### Goal
Analyse Isaac's personal budget workbook (`Personal Budget - IAG.xlsx`), report insights, and decide whether it's worth adding to the backlog.

### What we did
- **Read and analysed `finance-apps/WealthOrah/WealthOrah+/Personal Budget - IAG.xlsx`** by unzipping the `.xlsx` and parsing the sheet XML (an initial paste came through as raw binary; reading from disk was the reliable route).
  - Early reads reflected an older version with extra tabs (an inherited M.C.G Residency society ledger); Isaac then stripped the file down to just his budget. Final version = **5 tabs**: Annual, Overview, Compulsory, Desires, Invest.
  - Isaac updated it live mid-session (added **Aug & Sep 2026**), so the final analysis covers **38 months, Aug 2023 → Sep 2026**.
- **Delivered a detailed report:**
  - Model = salary-driven **50/25/25** (Needs/Wants/Investments), each bucket split into weighted sub-categories with budget-vs-actual + surplus/deficit; `Annual` tab projects a long-range wealth curve.
  - Lifetime (38 mo): income ~29.69M, spend ~22.11M; **Invest rose to ~5.25M (17.7%)** after the big Jul-2026 windfall (10.6M "Others") was deployed across Aug/Sep — the standout positive change.
  - Cumulative savings peaked ~11.35M (Jul-26) then drew down to ~7.58M by Sep-26 (large Aug-26 Compulsory outlay + heavy investing).
  - Steady-income months roughly break even → **wealth is built from windfalls, not salary**; actual salary is tracking below the Annual projection's ~10% raise assumption.
  - Key improvements flagged: separate **recurring vs windfall income** with their own allocation rule; label the Aug-26 Needs spike and the Invest "Others" 2.66M bucket; retire phantom categories (Car and Crypto are 0 across all 38 months); round allocation formulas (12-decimal noise); clean stray junk cells.

### Backlog changes (`Ideas/Ideas.md`)
- **Added `Budget Planner`** — Medium / Finance / **Idea**. Salary-driven allocation budgeter with recurring-vs-windfall handling, cumulative savings, and long-range projection; local-first PWA, deliberately WealthOrah-compatible so it can later fold in as a Budget Allocator module. Scope note: **start in Plan mode** to agree the WealthOrah data-model attachment before building.
- **Parked `Personal Budget Lite`** → status `Parked (merged into Budget Planner)`; its category-limits/envelope approach becomes Budget Planner's optional "simple mode". Row kept intact (recoverable), so the backlog has one active Finance budgeting idea instead of two competing rows.

### Key decisions
- Budget Planner is a **module for WealthOrah**, not a standalone app (avoids duplicating shell/storage/branding; the app-family consistency rule).
- Tiered **Medium** (Complex only if the full multi-year projection + scenarios are included).
- Chose to **park & merge** Personal Budget Lite (option b) rather than keep two overlapping rows.
- Intake only — no build started; Budget Planner stays at `Idea`.

### Notes / open items
- The IAG workbook lives under `WealthOrah+/` but is Isaac's personal data, not app source — analysis only, nothing written to it.
- When Budget Planner is picked up: open in **Plan mode** first to agree how it attaches to WealthOrah's data model.

### Next session
- If building Budget Planner: Plan-mode session on the WealthOrah data-model fit (income types, allocation rules, projection), then Spec.

---

## Session 5 — 15 Sep 2026

### Goal
Capture a new app idea, then run a backlog hygiene pass.

### What we did
- **New idea intake (via New App Scaffolder agent):** Added **Sample Data Generator (Kiro agent)** — Medium / AI/Agents / **Idea**. A Kiro agent that generates realistic sample/random test data shaped to a target app's data model (reads the app's SPEC-design/requirements + code, outputs a separate seed/export the user imports deliberately; never overwrites real data; local-first). Scaffolder added the `Ideas.md` row and created `AI-Agents/Sample Data Generator (Kiro agent)/` with the 6 standard placeholder docs. Intake only — status left at `Idea`. (Its own scaffold log holds the detail.) Note: `scaffold-idea.ps1` exited non-zero (known Windows/cmd false-negative); success verified by confirming folder + 6 docs on disk + today's SESSION-LOG stamp.
- **Backlog hygiene (via Ideas Backlog Curator agent):** Ran a propose-only audit. Backlog found structurally healthy (all three tier tables well-formed, valid categories/statuses, parser-safe). Isaac approved actioning the surfaced items.

### Edits applied to `Ideas/Ideas.md`
- **Idea Board** — version tag corrected `Built (v3)` → `Built (Idea Board v2.4.8)`. Root cause: the old "v3" was shorthand for the v3 *modular architecture*, not a semantic version; that refactor is frozen at ~v2.3-era code while live work ships from the root monolith (confirmed against `app.js` `APP_VERSION='2.4.8'`, `sw.js` cache `v2.4.8`, and the app's SPEC-tasks note). Scope also reworded to reflect reality (ships from monolith; v3 refactor started but frozen).
- **MathFun** — Description/Scope trimmed from embedded v1.2/v1.3 changelog detail to a concise summary (no version change; still `Built (MathFun v1.3.1)`).
- **WealthOrah** — status tag `Built (WealthOrah+ v1.0.4)` → `Built (WealthOrah v1.0.4)` so row name, folder, and overview link align (chose 4-b).
- **Spec Reviewer (Kiro agent)** — re-tiered Medium → Simple, joining the other read-only auditor agents (PWA Readiness Checker, Pre-Live Testing Agent). Rationale (2-a): read-only auditors = Simple; read+write agents = Medium.

### Verification
All three tier tables remain well-formed; Spec Reviewer appears once (in Simple); no stray blank rows — Ideas.html parses cleanly.

### Staleness flags (for a later pass)
- Idea Board SPEC docs may reference "v3" as a live version (now contradicts Built v2.4.8).
- WealthOrah SPEC docs / overview.html may still say "WealthOrah+" (now diverges from the aligned backlog naming).
- Sample Data Generator SPEC trilogy is correctly placeholder, not stale.

### Next session
No status transitions pending. Optionally reconcile the Idea Board / WealthOrah SPEC-doc references flagged above.

---

## Session 6 — 21 Sep 2026

### Goal
Cross-project housekeeping: merge two overlapping backlog ideas into **Stock RA**, create its overview, then roll out a unified dark theme across ALL overview.html files to match Ideas.html.

### What was done

#### 1. Backlog merge — Stock RA
- Merged two Simple/Finance In Progress ideas — "Position Size / Risk Calculator" and "Stock Analysis Checklist (10-min)" — into a single idea: **Stock RA**.
- Updated the `Ideas.md` row with a combined description/scope (Tab 1 = Checklist, Tab 2 = Position Sizer), kept status **In Progress**.
- Updated the Complex-tier Company Analysis Workbench reference to point at "Stock RA's checklist tab" instead of the old separate idea.
- Verified no stale references remain across the backlog.

#### 2. Stock RA overview created
- Created `Finance/Stock RA/overview.html` with all four content sections filled in (What it is, Who it's for, Why it's useful, How it helps day to day).
- Initially styled with the light scaffold theme; restyled to the dark palette in the next step.

#### 3. Dark-theme overview rollout (all apps)
- Updated **every** `overview.html` across the workspace to use the Ideas.html dark theme palette:
  - Background `#0f1420`, cards `#1a2130`, text `#e6e9ef`, accent `#5b8def`.
  - STUB tags render amber-on-dark; BUILT tags render green-on-dark.
- **67+ files** touched across: AI-Agents (11), Devotional (4), Finance (17 + Stock RA), finance-apps (2), hospital-tools (1), Productivity (6), Home (5), Health (4), Learning (8), Work (5), Utility (4).
- Per-app specifics preserved: Housekeeper's `.chip.risk` class, ShiftPlanner's Suneetha K copyright.
- Travel Planner's custom teal theme replaced with the unified dark palette.
- Inline footers replaced with class-based `<footer class="footer">` markup.
- Print media query reverts to light for PDF export. All body content preserved.

#### 4. Ideas.html iframe fix
- Changed the iframe background from white (`#fff`) to `var(--bg)` to prevent a white flash before dark-themed overviews load. Updated the CSS comment.

#### 5. Scaffold scripts updated
- Both `scripts/scaffold-idea.ps1` and `scripts/scaffold-ideas.ps1` overview.html templates updated from light to dark theme, so future scaffolds generate dark-themed overviews automatically.

#### 6. New idea — Scaffold Sync (Kiro agent)
- Added to the backlog: Simple / AI/Agents / status **Idea**.
- Folder + 6 placeholder docs scaffolded at `AI-Agents/Scaffold Sync (Kiro agent)/`.
- Purpose: propagate template-level changes (like this dark-theme rollout) across scaffolded files in batch. Parked for when the need arises.

#### 7. Stock RA scaffold completed
- Created the remaining 5 scaffold docs in `Finance/Stock RA/`: SESSION-LOG.md, SPEC-requirements.md, SPEC-design.md, SPEC-tasks.md, userguide.html. Overview already existed from step 2.

#### 8. Ideas count confirmed
- Board now has **67 ideas** (17 Simple + 32 Medium + 17 Complex + 1 new = 67).

### What was NOT done / deferred
- **Stock RA build** — deferred to next session (context budget recommendation).
- The old folders (`Finance/Position Size - Risk Calculator`, `Finance/Stock Analysis Checklist (10-min)`) still exist and could be cleaned up (Housekeeper candidate).
- Stray file: `c:\temp\_run-scaffold.cmd` from the scaffolder workaround — Isaac can delete manually.

### Key decisions
- Unified dark palette chosen to match Ideas.html (the board viewer), making the iframe-embedded overviews visually seamless.
- Travel Planner's custom teal theme sacrificed for family-wide consistency.
- Scaffold scripts updated so the dark theme is the default for all future scaffolds.
- Scaffold Sync agent idea captured but left at Idea (not worth building until the pattern recurs).

### Notes
- Cross-project session — touched the Ideas backlog and overview.html files across all app folders. Logged here (Ideas session log) rather than in any one app's log.
- No version bumps on any app (display/branding changes only).

### Next session
- **Build Stock RA** (Quick Spec or Spec mode, depending on scope agreement). Read `Finance/Stock RA/SESSION-LOG.md` first.
- Optionally clean up the two old Finance folders via Housekeeper.

---

## Session 7 — 28 Sep 2026

### Goal
Build **Capture Ideas** — a mobile-first, installable PWA layer over the Ideas backlog that lets ideas be browsed and captured on the phone, committing straight to `Ideas.md` on GitHub.

### Build standards agreed (4-point flag)
- **Mode:** Quick Spec-ish, run conversationally (one focused feature on the existing board).
- **Tier:** Simple (single page, no backend of our own).
- **Stack:** Vanilla HTML/CSS/JS — the same `Ideas.html` made responsive, no build step (matches the family).
- **Platform:** Mobile web first + installable PWA.
- **Copyright:** Isaac A Gera. **Licence:** MIT.

### Approach decided (how "sync" works without a backend)
Explored options for writing back to `Ideas.md` from a phone. A plain page can't write to disk, so we went with **GitHub as the shared source of truth**: host on **GitHub Pages** from a public repo `IdeasBacklog`, and have the capture form commit rows to `Ideas.md` via the **GitHub REST API** using a user-supplied fine-grained token (stored only on the device, never committed). Read side needs no token; only writes do.

### What we built (all inside `Ideas/`, ships as the `IdeasBacklog` repo)
- **`Ideas.html`** reworked in place:
  - **PIN gate** landing screen — PIN created in-app, stored as a SHA-256 hash (never plaintext/in-code), unlock remembered per session, reset option.
  - **Responsive board** — toolbar stacks, single-column cards, 44px tap targets under 720px; Add-idea pill collapses to an icon under 460px.
  - **Capture form** → commits a correctly-formatted row into the right tier table via the GitHub API, with a **SHA-conflict retry** so concurrent laptop/phone edits can't silently clobber. Pipe chars escaped so the table can't break.
  - **Settings** — owner/repo/branch (pre-filled `isaacgera`/`IdeasBacklog`/`main`), token, change-PIN; all namespaced `captureideas_*` in localStorage.
  - **Offline queue** — captures made offline/without a token are stashed locally and auto-committed once online + token set.
  - **Light/dark theme toggle** (persisted; first load follows `prefers-color-scheme`), header **Add idea** pill + theme + settings, Forjé branding footer.
- **`manifest.webmanifest`** + **`sw.js`** — installable PWA; cache-first app shell, network-first `Ideas.md`, never caches `api.github.com`.
- **`icons/`** — 192/512/maskable PNGs via `scripts/make-icons.py` (stdlib-only PNG writer, no Pillow).
- **`overview.html`**, **`userguide.html`**, **`README.md`**, **`LICENSE`** (MIT) — full delivery docs.
- **`Ideas.md`** — added the **Capture Ideas** row (Simple / Utility) with an explicit `[overview](overview.html)` link so its card opens the overview; status **In Progress**.

### Verification done here
- **Row insertion logic** ported to Python and tested against the real `Ideas.md`: exactly one row added to the correct tier, other tiers untouched, pipes escaped, diff = one line. (Data-safety guarantee for the source of truth.)
- **Lighthouse** (Isaac, live): Performance ~96, **Accessibility 100 in both light and dark**, Best Practices 100, **SEO 100**. Several rounds of contrast fixes got there.
- **Two agent audits run before push** (dogfooding the roster):
  - **PWA Readiness Checker** — found 2 offline gaps → fixed: precache `Ideas.md`; cache/match it under a stable key so the `?t=` buster doesn't cause an offline miss. Bumped SW `CACHE_NAME` to `capture-ideas-v1.0.1`.
  - **Pre-Live Testing Agent** — found 2 real focus Blockers → fixed: modal **focus trap**, **focus return** to trigger, background `#app` set `inert`; added **`aria-pressed`** to the segmented filter groups + capture complexity chips; tightened Escape to close only the topmost modal.

### Contrast lessons (recorded so we don't repeat)
- A single accent token can't serve as *text* in both themes: the darker `--accent-strong` reads on white (light mode) but fails as text on the dark bg (3.36:1). Fix: footer-brand and card `.open-hint` are now **theme-aware** — `--accent` in dark, `--accent-strong` in light — both pass ≥4.5:1. Buttons that use `--accent-strong` as a *background* with white text are fine (that pairing was the one originally checked).

### Status / backlog
- `Ideas.md` **Capture Ideas** row = **In Progress** (code-complete, docs complete, Lighthouse clean). Per the backlog-sync rule, it flips to **`Built (Capture Ideas v1.0.0)`** only after Isaac's live phone-capture test confirms the GitHub commit chain works end-to-end.

### Outstanding (the only thing left)
1. Push to the public `IdeasBacklog` repo, enable GitHub Pages, create the fine-grained PAT (Contents: R/W, this repo only, expiry).
2. **Live phone test:** open the Pages URL → set PIN → Settings → paste token → Add a throwaway idea → confirm the commit lands in `Ideas.md` and the card appears → delete the test row.
3. On confirmation: set the row to `Built (Capture Ideas v1.0.0)`.

### Notes
- No version bump elsewhere. The SW `CACHE_NAME` v1.0.1 is a cache-buster, not an app-version change (app stays v1.0.0).
- Couldn't run live browser/GitHub-API tests here (no browser + Windows shell quirk); logic verified by inspection + Python simulation, visuals/scores verified by Isaac on Live Server.
