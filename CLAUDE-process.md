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
| Distribution | GitHub Releases | Apple App Store (live since 2026-04-14) |
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

**5. VAS 文案掃「但」** <a id="vas-copy-but"></a>

「但」在 Nova 個人書寫中有正確的位置：當前後句構成真正的邏輯對立或轉折時，「但」是精確的連接詞，給讀者一個緩衝，避免前句的重量直接壓在後句上。

VAS 的器物語氣不適用這個邏輯。「謝謝你走進來，但請繼續探索」——這個「但」在替前一句道歉，彷彿感謝的誠意需要被轉折掉。器物不道歉，不替自己的語氣找出口。

掃描原則：若拿掉「但」後句子仍然完整、語氣仍然流動，就應該拿掉。只有在移除後句意思改變（真正的對立：「這樣做有效，但成本很高」），「但」才是必要的。

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
├── i18n/
│   ├── core.js         # Dynamic loader + dropdown logic — no translations here
│   ├── zh.js           # Traditional Chinese — all pages
│   ├── en.js           # English — all pages
│   ├── ja.js           # Japanese — all pages
│   └── cn.js           # Simplified Chinese — Tauri-only content
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
2. Language toggle (中 → EN → 日 → 簡) — no missing keys; verify dot-nav, TOC groups, and nav links specifically
3. External links correct
4. RWD at ~375px — no horizontal overflow
5. Design consistency — nav style, spacing match across all pages

**CSS self-check before committing any new rule:**
- If writing `selector { display: none }` globally AND `@media { selector { display: block } }`, the global rule must appear **before** the `@media` block in the file — otherwise the global rule wins via cascade order.
- If using a page-scope suppressor (`body.is-xxx .selector { display: none }`, specificity ≥ 0,2,1), always add a paired `@media` override with **equal or higher specificity** for interactive states (`is-open`, `is-active`, etc.).

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
