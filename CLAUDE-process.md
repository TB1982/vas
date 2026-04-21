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
| Language support | zh-Hant / EN / JA (trilingual, fixed) | zh-Hant / EN / JA / 简中 (quadrilingual) |
| Narrative | 「經典版」— the origin, free forever | 「極致版」— the evolution, App Store |

**Simplified Chinese (cn) is Tauri-only.** Electron remains trilingual permanently. When adding CN translations, they apply only to Tauri-era content and UI. Electron-specific pages or contexts: do not add CN.

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

---

## Repository Structure

```
/
├── index.html          # VAS product page
├── guide.html          # User guide
├── insight.html        # Design Insight — 設計洞察
├── collab.html         # Collab Notes — 協作筆記
├── harness.html        # Harness Engineering — 系統建構裏話
├── milestone.html      # Milestone — 里程碑
├── privacy.html        # Privacy Policy
├── base.css            # Shared styles — owned by Claude Design; Nova relays changes
├── designrule.md       # Visual design rules — read before any HTML/CSS change
├── km.md               # Known issues & solutions — append only
├── CLAUDE.md           # Core rules (always loaded)
├── CLAUDE-process.md   # This file — workflows and protocols
├── i18n-shared.js      # Shared nav/footer translations + dropdown init
├── i18n-index.js       # index.html (window.VASIndexT)
├── i18n-guide.js       # guide.html (window.VASGuideT)
├── i18n-collab.js      # collab.html (window.VASCollabT)
├── i18n-harness.js     # harness.html (window.VASHarnessT)
├── i18n-insight.js     # insight.html (window.VASInsightT)
├── i18n-milestone.js   # milestone.html (window.VASMilestoneT)
├── i18n-privacy.js     # privacy.html (window.VASPrivacyT)
└── img/                # Screenshots — vas-guide-*.png used in guide.html
```

**File ownership:**
- Claude Design owns: `base.css`, `design-system.html`, HTML layout structure
- 宰相 owns: all `i18n-*.js`, `data-lang-key` attributes, content text, `km.md`, `website-context.md`

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Markup | HTML5 |
| Styling | Tailwind CSS (CDN) + `base.css` |
| Scripting | Vanilla JavaScript |
| Fonts | Google Fonts — Noto Sans TC, Inter |

**No build tools. No package manager. No TypeScript. No testing framework.**

---

## Development Workflow

> **Before any HTML or CSS change: read `designrule.md` AND `base.css` first. Mandatory.**

1. Edit the relevant `.html` or `i18n-*.js` file.
2. Commit with a Traditional Chinese action message.
3. Push to dev branch; merge to `main` when Nova approves.

```bash
# Local preview — always use port 8081
python3 -m http.server 8081
```

### QC Checklist
After any user-visible change, provide this command and ask Nova to verify:

```bash
git pull origin <branch-name> && python3 -m http.server 8081
```

開啟：`http://localhost:8081/<filename>.html`

**Present the bash block and the URL as two separate copyable blocks — never embed the URL inside the bash block.**

Nova checks:
1. Content correct
2. Language toggle (中 → EN → 日 → 簡) — no missing keys
3. External links correct
4. RWD at ~375px — no horizontal overflow
5. Design consistency — nav style, spacing match across all pages

---

## New Page Checklist

When creating a new page:
1. Create `<page>.html` and `i18n-<page>.js`
2. Add the page to `i18n-shared.js` nav entries (all languages)
3. Update `README.md` — add to page list
4. Update Repository Structure in this file (CLAUDE-process.md)
5. Create `website-context.md` entry for the new page

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
| `i18n-shared.js` | `initDropdown()` / `updateDropdown()` — shared by all pages |
| `km.md` | KM log — append immediately when a bug is resolved |
