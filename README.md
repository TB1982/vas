# VAS — Visual Annotation Studio

**Product site:** [tb1982.github.io/vas](https://tb1982.github.io/vas/)

A screenshot and visual annotation tool for Mac, built for cross-functional communication.
Born from a collaboration between a PM who can't write a single line of code, and Claude — iterated together to v3.44 in one week.

---

## Pages

| File | URL | Description |
|------|-----|-------------|
| `index.html` | `/` | Product page — download, features, roadmap |
| `guide.html` | `/guide.html` | User guide — screenshots and walkthrough |
| `insight.html` | `/insight.html` | Design insights — the thinking behind VAS |
| `collab.html` | `/collab.html` | Collab notes — how Nova & Claude built it |
| `harness.html` | `/harness.html` | Harness Engineering — methodology essay, 8 chapters |
| `milestone.html` | `/milestone.html` | Version history & roadmap |
| `privacy.html` | `/privacy.html` | Privacy policy |

---

## Stack

Static HTML / Tailwind CSS (CDN) / Vanilla JS — no build tools, no package manager.

Trilingual (zh-Hant / EN / 日本語) via `data-lang-key` + per-page i18n JS files.

---

## i18n Architecture

| File | Exports | Used by |
|------|---------|---------|
| `i18n-shared.js` | `window.VASShared` | All pages — nav, footer, dropdown |
| `i18n-index.js` | `window.VASIndexT` | `index.html` |
| `i18n-guide.js` | `window.VASGuideT` | `guide.html` |
| `i18n-collab.js` | `window.VASCollabT` | `collab.html` |
| `i18n-insight.js` | `window.VASInsightT` | `insight.html` |
| `i18n-harness.js` | `window.VASHarnessT` | `harness.html` |
| `i18n-milestone.js` | `window.VASMilestoneT` | `milestone.html` |
| `i18n-privacy.js` | `window.VASPrivacyT` | `privacy.html` |

Version number single source of truth: `version.js` → `window.VAS_VERSION`.

---

## Local Preview

```bash
python3 -m http.server 8081
```

Open: `http://localhost:8081`

---

## Author

Nova — [babelon1882@gmail.com](mailto:babelon1882@gmail.com)
Part of the [深握計畫 (Deep Holding Project)](https://tb1982.github.io/pm/)

Built with [Claude Code](https://claude.ai/claude-code)
