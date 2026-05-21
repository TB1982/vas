# CLAUDE-process.md — VAS 開發流程手冊
_Companion to CLAUDE.md — read that file first. Core rules live there._

---

## Product Strategy

**Two-version positioning — use this framework for all copy involving both versions:**

| | Electron | Tauri |
|--|----------|-------|
| Price | Free | Paid |
| Role | Entry-level / classic | Premium / performance |
| Size | ~113 MB | ~20 MB |
| Version scheme | v3.x (current: v3.60) | v2.x (current: v2.0.8) — independent numbering |
| Distribution | R2 (download.yoursvas.app) | Apple App Store (live since 2026-04-14) |
| Language support | zh-Hant / EN / JA (trilingual, fixed) | zh-Hant / EN / JA / 简中 (quadrilingual) |
| Narrative | 「經典版」— the origin, free forever | 「極致版」— the evolution, App Store |

**Version numbering is completely independent.** Electron and Tauri do not share version numbers. When Nova says "version update", always confirm which version is being updated.

**Simplified Chinese (cn) is Tauri-only.** Electron remains trilingual permanently. When adding CN translations, they apply only to Tauri-era content and UI. Electron-specific pages or contexts: do not add CN.

**Electron maintenance policy:** No new Tauri-exclusive features will be backported intentionally. However, since both versions share frontend code, Electron may incidentally benefit from Tauri updates.

**Active development (as of 2026-04):** Simplified Chinese support + long screenshot / web page screenshot refinement (currently experimental in Tauri).

---

## Design Language

The visual decisions on this site follow from the product philosophy in CLAUDE.md — they are not arbitrary aesthetic choices.

| Element | Why it's right |
|---------|---------------|
| Shippori Mincho | East Asian literary typeface for expressing the inexpressible — not chosen for style, chosen because it handles silence |
| White space | The vessel needs stillness for transformation to occur; filling space is the wrong instinct |
| The bottle shape | The neck is the point of concentration before emergence — that is VAS's core action |
| Dark background | The prima materia is not cheerful; it is unformed, pre-verbal |

**Editorial register per page** (Claude Design's vision):
- `index.html` — Teenage Engineering–style object display: each feature is an independent artifact
- `insight.html` — Pudding-style long-form feature: each insight is a chapter
- `collab.html` — Dual-column script: Nova's thinking left, Claude's response right, timeline axis center
- `harness.html` — Architecture white paper: diagrams, schema, structured comparison
- `milestone.html` — Exhibition wall text: date-led, serial, short narrative per milestone
- `guide.html` — Precision reference: three-column (TOC / explanation / figure), high density allowed

**The Japanese editorial sensibility** runs across all pages: 《Brutus》, 《POPEYE》, Naoto Fukasawa's books — "一壺茶一個想法請自己來看". Short sentences. Sentences that end like a signature followed by a single dot.

### UI & Editorial Standards

These rules prevent known recurring mistakes across all pages.

**1. Translation coverage — special menus**
After any i18n update, explicitly verify these three zones — they are NOT in the main content area and are routinely missed:
- Breathing-light dot-nav labels (`.dn-label[data-lang-key]`)
- Guide left-sidebar TOC groups (`.group[data-lang-key]`)
- Top nav links (`data-lang-key="home2.nav.*"`)

**2. Mobile spacing**
Default section padding (e.g., `64px 0 24px`) and dek `margin-bottom: 56px` are desktop-calibrated. Always add `@media (max-width: 768px)` overrides for both when creating a new section type. Rule of thumb: mobile top-padding ≤ 50% of desktop value.

**3. English heading deduplication**
English headings can echo when layout reflows — e.g., a page-level `<title>` of "User Guide · VAS" combined with an `<h1>` of "VAS User Guide" creates awkward repetition. After writing any English heading, read the full page top-to-bottom and remove accidental echo.

**4. Horizontal nav overflow on mobile**
English labels are typically 1.5–2× wider than their Chinese equivalents. Any horizontal button row (language switcher, nav links, chip rows) must be mentally tested at 375px with full English text before committing. If total width exceeds ~320px, redesign for wrapping or abbreviation.

---

## Repository Structure

```
/
├── index.html              # Home — 4 chapter gates
├── about.html              # Chapter 0 · 序章 · PREFACE
├── echo.html               # Chapter I · 殘響 · ECHOES (cover)
├── insight.html            # Echo p.1 · 設計
├── collab.html             # Echo p.2 · 協作
├── context.html            # Echo p.3 · 信念
├── self.html               # Echo p.4 · 自己
├── harness.html            # Chapter II · 系統 · SYSTEM (cover)
├── us.html                 # Chapter II · ⓘ mirror (Sapere Aude 2.0)
├── vessel.html             # Vessel · 容器論 · Treatise (hidden under harness 呼吸燈)
├── milestone.html          # Chapter III · 里程碑 · CHRONICLE
├── faq.html                # FAQ — eight questions
├── guide.html              # User guide
├── privacy.html            # Privacy policy
├── 404.html                # Error page
│
├── en/                     # English static variants (full page-per-page set)
├── ja/                     # Japanese static variants
├── cn/                     # Simplified Chinese (Mainland register) static variants
│
├── harness/                # Deep layer — 3 pillars (Mandarin-only, in-page JS lang switch)
│   ├── context.html        # Pillar I  — Context management
│   ├── constraints.html    # Pillar II — Constraints as guidance
│   ├── entropy.html        # Pillar III — Coexisting with entropy
│   └── fourier.webp        # Shared figure
│
├── i18n/
│   ├── core.js             # Dynamic loader + dropdown logic for root pages
│   ├── zh.js               # zh-Hant translations
│   ├── en.js               # English
│   ├── ja.js               # Japanese
│   └── cn.js               # Simplified Chinese (Mainland register)
│
├── css/                    # tokens.css / shell.css / page-specific
├── js/                     # analytics.js / per-page scripts
├── img/                    # vas-*.png / vas-*.webp / favicon
│
├── sitemap.xml             # 59 URLs with per-locale hreflang
│
├── CLAUDE.md               # Core rules (always loaded)
├── CLAUDE-process.md       # This file — workflows
├── GLOSSARY.md             # Translation terminology + per-locale conventions
├── README.md               # Public-facing overview
├── km.md                   # Known issues log — append only
└── designrule.md           # Visual design rules
```

**File ownership:**
- Claude Design owns: `css/tokens.css`, `css/shell.css`, HTML layout structure
- Nova owns: all `i18n/*.js`, `data-lang-key` attributes, content text, `km.md`, `GLOSSARY.md`
- Lang static files (`en/`, `ja/`, `cn/`): translation pass owned by Nova + agent; structure mirrors root

---

## Tech Stack

**Main site:**
| Layer | Technology |
|-------|-----------|
| Markup | HTML5 |
| Styling | `css/tokens.css` (design tokens) + `css/shell.css` (shared layout) + page-specific CSS |
| Scripting | Vanilla JavaScript; `i18n/core.js` handles dynamic lang switching on root pages |
| Fonts | Google Fonts — Shippori Mincho, Fraunces, JetBrains Mono |

**Harness deep-layer pages** (`/harness/{context,constraints,entropy}`):
Different stack — Tailwind CDN + inline `<style>` + in-page JS dictionary (`translations` object). Intentionally different to mark "deep layer" visually. Design refactor pending; Nova will hand off to Design when ready.

**No build tools. No package manager. No TypeScript. No testing framework.**

---

## Development Workflow

> **Before any HTML or CSS change: read `designrule.md` AND `css/shell.css` first. Mandatory.**

**Full collaboration loop (7 steps, including 巡水田):**

```
1. spec     → Nova 口述需求
2. exec     → Claude edits / agent dispatch / mechanical sed
3. push     → Tri-remote via `git pushall <branch>` (origin + backup + github)
4. merge    → Nova accepts PR (GitHub UI)
5. deploy   → Cloudflare auto-deploy (~1–2 min after merge)
6. 巡水田    → Nova goes to live front-end, sacral pass on relevant pages
7. flag     → Findings from 巡水田 become input for next PR
```

**Session-end condition:** "Nova 巡完水田沒新發現", NOT "Claude push 完了". See § 巡水田 below.

```bash
# Local preview — always use port 8081
python3 -m http.server 8081
```

### QC Checklist
After any user-visible change, provide this command and ask Nova to verify:

```bash
git pull github <branch-name> && python3 -m http.server 8081
```

開啟：`http://localhost:8081/<filename>.html`

**Present the bash block and the URL as two separate copyable blocks — never embed the URL inside the bash block.**

Nova checks:
1. Content correct
2. Language toggle (中 → EN → 日 → 簡) — no missing keys; verify dot-nav, TOC groups, and nav links specifically
3. External links correct
4. RWD at ~375px — no horizontal overflow
5. Design consistency — nav style, spacing match across all pages

**CSS self-check before committing any new rule:**
- If writing `selector { display: none }` globally AND `@media { selector { display: block } }`, the global rule must appear **before** the `@media` block in the file — otherwise the global rule wins via cascade order.
- If using a page-scope suppressor (`body.is-xxx .selector { display: none }`, specificity ≥ 0,2,1), always add a paired `@media` override with **equal or higher specificity** for interactive states (`is-open`, `is-active`, etc.).

---

## 巡水田 — Sacral Quality Pass

**Why it's a phase, not a bug:**
Nova's design taste operates at granular resolution. Plain-eye review on the deployed site catches things that pre-merge code review can't (real font rendering, real spacing, real readability under actual user agents, the rhythm of em-spans + br-breaks in production). This step is the **quality engine**, not an afterthought.

**Behavior pattern:** After Cloudflare deploys, Nova opens the live front-end and 巡水田 — walks the affected pages, lets her sacral catch anything off. Findings tend to come in clusters of 1–3 per PR.

**Workflow placement:** Step 6 in the 7-step loop above. Findings flow to step 7 (flag → next PR's input).

**Naming this phase explicitly converts what could feel like "scope creep" into a planned ritual.** Two consequences:

- **For Nova:** Stop apologizing for findings. They are the system working as designed. The "I keep adding things" feeling is misread — you are doing exactly the named step.
- **For Claude:** Do not declare a session "done" at push or even at merge. The session ends when Nova returns from 巡水田 with no new findings.

**Optional optimization:** If a finding is mechanical (sed-able, agent-able, no design judgement), Claude can take it immediately without ceremony. If a finding involves design judgement, ask Nova for the call before executing.

---

## New Page Checklist

When creating a new top-level page:
1. Create `<page>.html` (root, zh-Hant primary)
2. Add `data-lang-key="home2.nav.<page>"` to all nav entries — root + en/ja/cn lang variants
3. Add `home2.nav.<page>` key to `i18n/{zh,en,ja,cn}.js`
4. Create full static variants: `en/<page>.html`, `ja/<page>.html`, `cn/<page>.html`
5. Add 4 URL entries to `sitemap.xml` (root + 3 lang) with per-locale `<xhtml:link>` hreflang block
6. Update `README.md` — add to page list
7. Update Repository Structure in this file (CLAUDE-process.md)
8. If new terminology introduced: add to `GLOSSARY.md` § appropriate section

---

## Haiku Protocol

**Trigger — use Agent (haiku) when ANY of these apply:**
- Reading 2+ `i18n-*.js` files in the same task
- Adding or modifying 20+ i18n keys in one pass
- Creating a new full page (HTML + 3-language i18n)
- Applying Claude Design CSS updates across multiple pages

**Scope per Agent call:** one file × one language × max 15 keys

**Prompt template (prevents timeout):**
```
Task: update i18n-[page].js, [zh/en/ja/cn] block only.
Keys to update: [list them explicitly].
Output: return only a JSON object { "key": "value" }. No explanation.
Verification: state how many keys you modified.
```

**Commit rhythm:** zh → commit → en → commit → ja → commit → cn → commit. Each language is an independent checkpoint. Failure in one language does not require redoing the others.

**Main session role:** verify key count, spot-check values, apply via Edit, commit.

---

## Trickle-Flow Discipline

Applies to the main session — not just Haiku agents.

**Rule:** one Edit call = one logical unit. Commits are internal checkpoints, not pauses for Nova's confirmation. Complete the full task, then report once at the end.

**Self-alert triggers — stop and split into sequential steps if:**
- About to read 3+ files in one turn
- About to write 30+ lines in one Edit
- About to modify 2+ `i18n-*.js` files in one pass

**Pattern:**
```
read one file → edit one logical unit → commit → continue
```
Not: read everything → write everything → commit once.

---

## Claude Design Protocol

Claude Design is read-only on this repo — it cannot push. Nova relays its output manually.

**When applying Claude Design changes:**
1. Receive CSS/structure changes from Nova
2. Apply to `base.css` or HTML layout — one page at a time
3. **Never touch `data-lang-key` attributes or i18n values in the same pass**
4. Commit per page, then verify QC checklist

---

## Key Files Reference

| File | Note |
|------|------|
| `index.html` | Version string: search `迭代至 v` / `iterated together to v` |
| `guide.html` | Screenshots: `img/vas-guide-*.png` |
| `i18n/core.js` | Loader logic + dropdown for dynamic lang switching on root pages |
| `sitemap.xml` | 59 URLs, per-locale hreflang. Update on any new page (see § New Page Checklist) |
| `km.md` | KM log — append immediately when a bug is resolved |
| `GLOSSARY.md` | Translation terminology + per-locale conventions — read before any translation pass |
