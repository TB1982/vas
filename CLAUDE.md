# CLAUDE.md — VAS 產品網站
This file provides guidance for AI assistants working in this repository.

> **這是 VAS 產品網站的獨立 repo**，從 `tb1982/pm` 遷移而來。母專案請見 `https://github.com/TB1982/pm`。

---

## Project & Author Identity
**Always use these exact values. Never invent alternatives.**

| Field | Value |
|-------|-------|
| Author display name | Nova |
| Author email | babelon1882@gmail.com |
| Project name (ZH) | 深握計畫 |
| Project name (EN) | Deep Holding Project |
| Site canonical URL | `https://tb1982.github.io/vas/` |
| Copyright year | 2025–present |
| GitHub | `https://github.com/tb1982` |
| LinkedIn | `https://www.linkedin.com/in/yingtzuliu` |
| Instagram | `https://www.instagram.com/liuyingtzu` |

**Rules:** Never use placeholder emails. Never invent domain names — always use `https://tb1982.github.io/vas/` as base. Per-page canonical: `https://tb1982.github.io/vas/<filename>.html`. Never attribute to anyone other than **Nova**.

### Footer — canonical format
```
由 GitHub 部署　｜　Claude Code 傾力打造　｜　Nova（babelon1882@gmail.com）最後更新於 2026
Deployed via GitHub　｜　Built with Claude Code　｜　Last updated 2026 by Nova (babelon1882@gmail.com)
```

### Version Badges
Two badge classes in `base.css` (do NOT redefine per page):
- `.badge-tauri` — amber — Tauri Exclusive features
- `.badge-all` — green — All Versions (Electron + Tauri)

i18n keys (register in all three languages — zh / en / ja):

| Key | zh | en | ja |
|-----|-----|-----|-----|
| `tauriOnly` / `tauriOnlyBadge` | Tauri 專屬 | Tauri Exclusive | Tauri 専用 |
| `allVersions` | 全版本 | All Versions | 全バージョン |

### Social / JSON-LD author block
```json
"author": {
  "@type": "Person",
  "name": "Nova",
  "email": "babelon1882@gmail.com",
  "sameAs": ["https://github.com/tb1982","https://www.linkedin.com/in/yingtzuliu","https://www.instagram.com/liuyingtzu"]
}
```

---

## Project Overview
**VAS（Visual Annotation Studio）** — Mac screenshot and annotation tool. This repo is the public product website only — trilingual (zh-Hant / EN / JA) static HTML.

- **App repo:** `https://github.com/TB1982/vas-desktop` (private)
- **Site type:** Static HTML — no backend, no build system, no package manager
- **Hosting:** GitHub Pages — `https://tb1982.github.io/vas/`

---

## Repository Structure
```
/
├── index.html       # VAS product page
├── guide.html       # User guide
├── insight.html     # Design Insight — 設計洞察
├── collab.html      # Collab Notes — 協作筆記
├── milestone.html   # Milestone — 里程碑
├── privacy.html     # Privacy Policy
├── base.css         # Shared styles — single source of truth
├── i18n-shared.js   # Shared nav/footer translations + dropdown init
├── i18n-index.js    # index.html translations (window.VASIndexT)
├── i18n-guide.js    # guide.html translations (window.VASGuideT)
├── i18n-collab.js   # collab.html translations (window.VASCollabT)
├── i18n-insight.js  # insight.html translations (window.VASInsightT)
├── i18n-milestone.js# milestone.html translations (window.VASMilestoneT)
├── i18n-privacy.js  # privacy.html translations (window.VASPrivacyT)
└── img/             # Screenshots — vas-guide-*.png used in guide.html
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Markup | HTML5 |
| Styling | Tailwind CSS (CDN) + `base.css` (shared rules) |
| Scripting | Vanilla JavaScript |
| Fonts | Google Fonts — Noto Sans TC, Inter |

**No build tools. No package manager. No TypeScript. No testing framework.**

---

## Design System — base.css

**Rule: Read `base.css` before creating any new page or writing any CSS.**

`base.css` is the single source of truth for all shared styles. Do not redefine any class listed below in a per-page `<style>` block.

| Class | Purpose |
|-------|---------|
| `.gradient-text` | Purple→pink→blue gradient text |
| `.tag` | Small uppercase label above card headings (purple) |
| `.nav-sub-link` | Sub-page nav links (`:hover` + `.active` included) |
| `.badge-tauri` | Amber badge — Tauri Exclusive |
| `.badge-all` | Green badge — All Versions |
| `.glass-section` | Static glass block (`bg 0.04`, no hover) |
| `.glass-card` | Interactive glass card (`bg 0.06`, hover lift -4px) |
| `.nav-pill-group` | Pill nav container |
| `.nav-pill` | Pill nav link (`:hover` + `.active` included) |
| `.lang-dropdown-btn/menu/opt` | Language switcher dropdown |
| `.divider` | Pink gradient divider bar (`scroll-margin-top: 90px`) |
| `.page-section` | Section vertical padding |

**Design tokens:**

| Token | Value |
|-------|-------|
| Page background | `linear-gradient(145deg, #0f0c29 0%, #302b63 50%, #24243e 100%)` |
| Brand gradient | `linear-gradient(135deg, #c471f5 0%, #fa71cd 50%, #4facfe 100%)` |
| Body text | `rgba(255,255,255,0.85)` |
| Glass subtle | `rgba(255,255,255,0.04)` → `.glass-section` |
| Glass card | `rgba(255,255,255,0.06)` → `.glass-card` |
| Font stack | `'Inter', 'Noto Sans TC', sans-serif` |

**Per-page body overrides** (do not remove these classes):
- `index.html` → `<body class="hero-bg">` (defined locally for specificity)
- `guide.html` → `<body class="gradient-bg">` (darker indigo, defined locally)

---

## Development Workflow

1. Edit the relevant `.html` file directly.
2. Commit with a Traditional Chinese action message.
3. Push to dev branch (`claude/<description>-<id>`); merge to `main` when ready.

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

**Present the bash block and the URL as two separate copyable blocks — never embed the URL as a comment inside the bash block.**

Nova checks:
1. Content correct
2. Language toggle (中 → EN → 中) — no missing keys
3. External links correct
4. RWD at ~375px — no horizontal overflow
5. Design consistency — nav style, spacing match across all pages

> **Lesson (2026-04-05):** Nav inconsistency was missed because links were functional. Broken ≠ bad design. Always review design consistency separately from technical correctness.

---

## Conventions

### Language & i18n
- Default language: Traditional Chinese (`lang="zh-Hant"`).
- Toggle: `中` / `EN` via JS. Update `document.documentElement.lang` on switch.
- **Use `臺` not `台`** — `臺灣`, `臺北`, `臺中`, etc. Never substitute silently.

### data-lang-key — Two Places to Update
Every `data-lang-key` element has two sources that **must be updated together**:
1. The HTML text node (renders before JS, or without JS)
2. The `zh`/`en`/`ja` keys in the page's translation map

```html
<p data-lang-key="cb_rect_desc">拖曳選取任意矩形區域後截圖。</p>
<!-- Both the HTML text node AND the zh/en/ja map entries must match -->
```

> Bug (2026-03-29): Updated only the JS map, forgot the HTML text node — old text showed until fix.

### Styling & RWD
- Tailwind utility classes are primary. Page-specific rules go in `<head><style>`. Never redefine base.css classes.
- Mobile-first: use `sm:` `md:` `lg:` prefixes. Test at 375 / 768 / 1280px.
- Touch targets: minimum 44×44px (`min-h-[44px] min-w-[44px]`). Images: `max-w-full`.

### Commit Messages
Traditional Chinese, action-oriented: `更新手機版顯示數字大小` / `新增 OCR 段落說明`

---

## Key Files
| File | Note |
|------|------|
| `index.html` | Version string: search `迭代至 v` / `iterated together to v` |
| `guide.html` | Screenshots: `img/vas-guide-*.png` |
| `i18n-shared.js` | `initDropdown()` / `updateDropdown()` — shared by all pages |

---

## Git
- **Remote:** `https://github.com/TB1982/vas.git`
- **Main branch:** `main` (GitHub Pages source)
- **Dev branches:** `claude/<description>-<id>`
- Do not push directly to `main`; always use a dev branch.
- CDN dependencies: do not move to local files without updating all references.

---

## AEO — Answer Engine Optimisation

### Required `<head>` metadata (every page)
```html
<meta name="description" content="頁面摘要，100–160字元">
<link rel="canonical" href="https://tb1982.github.io/vas/page.html">
<meta property="og:title" content="頁面標題">
<meta property="og:description" content="頁面摘要">
<meta property="og:type" content="website">
<meta property="og:url" content="https://tb1982.github.io/vas/page.html">
<meta property="og:locale" content="zh_TW">
```

### JSON-LD (before `</body>`)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "頁面名稱",
  "description": "頁面描述",
  "inLanguage": "zh-Hant",
  "author": { "@type": "Person", "name": "Nova", "email": "babelon1882@gmail.com" }
}
</script>
```
- `"Article"` for insight.html, collab.html. `"SoftwareApplication"` for index.html.

---

## Accessibility (A11y)
Target: WCAG 2.1 Level AA.

- Every `<img>`: `alt=""` (decorative) or descriptive text.
- Heading hierarchy: one `<h1>`, then `<h2>` → `<h3>` in order, no skipping.
- Colour contrast: body text ≥ 4.5:1 against background.
- Language toggle: `document.documentElement.lang = isEnglish ? 'en' : 'zh-Hant'`

Every page with animations must include:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

Orphan prevention — add to every new page's `<style>` block:
```css
.glass-card p, .glass-section p { text-wrap: pretty; }
```

---

## Safety Rules — Destructive Actions
**STOP and ask before:**
- Deleting files / directories
- `git reset --hard`, `git restore`, `git checkout --`
- `git push --force`
- Any action that cannot be undone in one step

---

## Interaction Language
- Communicate with Nova in **Traditional Chinese**.
- CLAUDE.md itself is written and maintained in **English**.
