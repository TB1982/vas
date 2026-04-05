# designrule.md — VAS 視覺設計規範
Read this file (along with `base.css`) before making any HTML or CSS change.

---

## Design System — base.css
Single source of truth for shared styles. **Do not redefine any listed class in a per-page `<style>` block.**

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

**Per-page body overrides** (do not remove):
- `index.html` → `<body class="hero-bg">` (same gradient, local specificity)
- `guide.html` → `<body class="gradient-bg">` (darker indigo, defined locally)

---

## Section Header Pattern
Every content section follows this exact structure (divider → English label → Chinese h2):
```html
<div class="divider mx-auto mb-8" id="section-anchor"></div>
<p class="text-center text-xs font-bold tracking-widest text-white/30 uppercase mb-2"
   data-lang-key="sectionLabel">ENGLISH LABEL</p>
<h2 class="text-2xl md:text-3xl font-bold text-center mb-10 text-white/90"
    data-lang-key="sectionTitle">中文標題</h2>
```

---

## Version Badges
`.badge-tauri` (amber) and `.badge-all` (green) are in `base.css`. Do NOT redefine per page.

i18n keys — register in zh / en / ja for every page that uses badges:

| Key | zh | en | ja |
|-----|-----|-----|-----|
| `tauriOnly` / `tauriOnlyBadge` | Tauri 專屬 | Tauri Exclusive | Tauri 専用 |
| `allVersions` | 全版本 | All Versions | 全バージョン |

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
- Language toggle must update `<html lang>`: `document.documentElement.lang = isEnglish ? 'en' : 'zh-Hant'`

Every page with animations must include:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

Orphan prevention — add to every new page's `<style>`:
```css
.glass-card p, .glass-section p { text-wrap: pretty; }
```

---

## RWD
- Mobile-first: Tailwind `sm:` `md:` `lg:` prefixes. No fixed `px` widths on containers.
- Test at: **375px** (mobile) / **768px** (tablet) / **1280px** (desktop).
- Touch targets: min 44×44px (`min-h-[44px] min-w-[44px]`). Images: `max-w-full`.
- When adjusting mobile, always verify desktop is not broken.

---

## Nav System — Mobile Dropdown Pattern

**Rule: Any nav change must be applied to both homepage AND all sub-pages simultaneously.**

VAS has two nav contexts that share the same mobile dropdown pattern:

| Context | Location | Links | JS init |
|---------|----------|-------|---------|
| Homepage floating nav | `index.html` fixed overlay | In-page anchors (功能/細節/起源/版本) | Inline IIFE in `index.html` |
| Sub-page sticky header nav | `guide/insight/collab/milestone.html` | Cross-page links (操作/設計/協作/里程碑) | `VASShared.initNavDropdown()` via each `i18n-*.js` |

**Breakpoint:** `sm` (640px) — below this, show `☰▾` dropdown; above, show pill group.

**HTML pattern (both contexts):**
```html
<!-- Desktop pills (sm+) -->
<div class="nav-pill-group hidden sm:flex">
  <a href="..." class="nav-pill [active]" data-lang-key="...">...</a>
</div>
<!-- Mobile dropdown (below sm) -->
<div class="relative sm:hidden" id="navMobileWrap">
  <button id="navMobileBtn" class="nav-pill-group flex items-center gap-1.5" style="appearance:none;cursor:pointer;" aria-haspopup="true" aria-expanded="false" aria-label="導覽選單">
    <!-- hamburger icon + chevron svg -->
  </button>
  <div id="navMobileMenu" style="display:none; ...">
    <a href="..." class="nav-pill [active]" style="display:block;text-align:center;" data-lang-key="...">...</a>
  </div>
</div>
```

**`initNavDropdown()` is defined in `i18n-shared.js`** — do not duplicate the toggle logic per page.

---

## Design Consistency Check
When reviewing the codebase, check visual consistency as a separate axis from correctness:
- Nav structure (pill style, spacing) matches across homepage and all sub-pages
- Shared UI (dropdowns, badges, dividers) comes from `base.css`, not redefined per page
- Active state present and correct on every sub-page

> Lesson (2026-04-05): Functional links ≠ correct design. Always check design separately.
