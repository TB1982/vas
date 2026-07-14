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
<link rel="canonical" href="https://yoursvas.app/page.html">
<meta property="og:title" content="頁面標題">
<meta property="og:description" content="頁面摘要">
<meta property="og:type" content="website">
<meta property="og:url" content="https://yoursvas.app/page.html">
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
  "author": { "@type": "Person", "name": "Nova", "email": "nova@yoursvas.app" }
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

## 首頁鏡面互動 — 參數地圖（微調指南）

首頁 `index.html`（四語同構：`en/` `ja/` `cn/` 一起改）。鏡面流動 = 中央瓶的升降直接耦合那條縫；hover 任一側字塊則該側拓寬。下面是「想調什麼 → 搜尋哪段 → 怎麼動」。

### 鏡面 `<script>`（頁尾）裡的 `tick` / `measure`

| 想調什麼 | 搜尋 | 怎麼動 |
|---------|------|-------|
| **hover 拉開速度** | `if(hover !== 0){ lastHoverT = now; k = 0.06; }` | 兩個 `0.06` 一起改；小=慢/柔、大=快。下一行 `< 600` 是放開後柔順回流的窗（ms），改慢速度時跟著放大 |
| 自體流動緊跟瓶的程度 | `var k = 0.3;` | 大=線更貼瓶的緩動；小=更鬆（太小會被抹平成均速） |
| 左右擺幅（頂到 LOGO 多遠） | `+ 1.5; /* 流動頂到大字 LOGO` | `+1.5` 是越過 LOGO 緣的餘量，大=線擺更開 |
| hover 多展開一點 | `OPEN_VOID = Math.min(50 + FLOW_AMP + 3` | `+3` ／下一行 `-3` 控制 hover 比呼吸峰再多開多少 |
| 熱區邊緣寬鬆度 | `var padX = 56, padY = 44;` | 越大越好探到 |

### `<style>` 裡的呼吸動畫（四組要一起改才同步）

| 想調什麼 | 搜尋 | 怎麼動 |
|---------|------|-------|
| 呼吸週期 | `animation:float 9s` | 四處 `9s`（`float` / `halo-breathe` / `ink-breathe` / `ground-breathe`）一起改 |
| 緩動曲線 | `cubic-bezier(0.65,0,0.35,1)` | 四處一起改。光譜：Sine `.37,0,.63,1` → Quad `.45,0,.55,1` → **Cubic 現在** → Quart `.76,0,.24,1` → Quint `.83,0,.17,1` |
| 兩端留白時間 | `@keyframes float` 的 `0%,3%` `47%,53%` `97%,100%` | 把 `3` / `47,53` / `97` 的間距拉大 = 停更久。四組 keyframe 都有同樣三停 |
| 瓶浮動振幅 | `translateY(-14px)` | ⚠️ 見下方硬耦合警告 |

> **⚠️ 硬耦合（一定要記住）：** 瓶振幅 `-14px` 在 **CSS（`@keyframes float`）和 JS（`frac = ... ty / -14`）兩邊都有**。改振幅必須**兩邊同步改**，只改一邊瓶與縫就脫鉤。

---

## Design Consistency Check
When reviewing the codebase, check visual consistency as a separate axis from correctness:
- Nav structure (pill style, spacing) matches across homepage and all sub-pages
- Shared UI (dropdowns, badges, dividers) comes from `base.css`, not redefined per page
- Active state present and correct on every sub-page

> Lesson (2026-04-05): Functional links ≠ correct design. Always check design separately.
