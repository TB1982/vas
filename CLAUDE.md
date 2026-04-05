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
| Copyright year | 2026– |
| GitHub | `https://github.com/tb1982` |
| LinkedIn | `https://www.linkedin.com/in/yingtzuliu` |
| Instagram | `https://www.instagram.com/liuyingtzu` |

**Rules:** Never use placeholder emails. Never invent domain names — always use `https://tb1982.github.io/vas/` as base. Per-page canonical: `https://tb1982.github.io/vas/<filename>.html`. Never attribute to anyone other than **Nova**.

### Footer — canonical format
```
由 GitHub 部署　｜　Claude Code 傾力打造　｜　Nova（babelon1882@gmail.com）最後更新於 2026
Deployed via GitHub　｜　Built with Claude Code　｜　Last updated 2026 by Nova (babelon1882@gmail.com)
```

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
├── index.html        # VAS product page
├── guide.html        # User guide
├── insight.html      # Design Insight — 設計洞察
├── collab.html       # Collab Notes — 協作筆記
├── milestone.html    # Milestone — 里程碑
├── privacy.html      # Privacy Policy
├── base.css          # Shared styles — single source of truth
├── designrule.md     # Visual design rules — read before any HTML/CSS change
├── i18n-shared.js    # Shared nav/footer translations + dropdown init
├── i18n-index.js     # index.html (window.VASIndexT)
├── i18n-guide.js     # guide.html (window.VASGuideT)
├── i18n-collab.js    # collab.html (window.VASCollabT)
├── i18n-insight.js   # insight.html (window.VASInsightT)
├── i18n-milestone.js # milestone.html (window.VASMilestoneT)
├── i18n-privacy.js   # privacy.html (window.VASPrivacyT)
└── img/              # Screenshots — vas-guide-*.png used in guide.html
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

## Development Workflow

> **Before any HTML or CSS change: read `designrule.md` AND `base.css` first. This is mandatory.**
> **Never push directly to `main`.** Always use a dev branch (`claude/<description>-<id>`).

1. Edit the relevant `.html` file directly.
2. Commit with a Traditional Chinese action message.
3. Push to dev branch; merge to `main` when ready.

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
2. Language toggle (中 → EN → 中) — no missing keys
3. External links correct
4. RWD at ~375px — no horizontal overflow
5. Design consistency — nav style, spacing match across all pages

---

## Conventions

### Language & i18n
- Default language: Traditional Chinese (`lang="zh-Hant"`).
- **Use `臺` not `台`** — `臺灣`, `臺北`, `臺中`, etc. Never substitute silently.

### data-lang-key — Two Places to Update
Every `data-lang-key` element has two sources — update **both**:
1. The HTML text node (renders before/without JS)
2. The `zh`/`en`/`ja` keys in the page's translation map

```html
<p data-lang-key="cb_rect_desc">拖曳選取任意矩形區域後截圖。</p>
<!-- HTML text node AND zh/en/ja map entries must always match -->
```

> Bug (2026-03-29): Updated only the JS map, forgot HTML — old text showed until fix.

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
- Do not push directly to `main`. CDN dependencies: do not move to local files.

---

## Interaction Language
- Communicate with Nova in **Traditional Chinese**.
- CLAUDE.md itself is written and maintained in **English**.
