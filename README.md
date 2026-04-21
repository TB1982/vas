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

Quadrilingual (zh-Hant / EN / 日本語 / 简中) via `data-lang-key` + `i18n/core.js` dynamic loader.

---

## i18n Architecture

| File | Role |
|------|------|
| `i18n/core.js` | Dynamic loader + dropdown logic. No translation data. |
| `i18n/zh.js` | Traditional Chinese — all pages |
| `i18n/en.js` | English — all pages |
| `i18n/ja.js` | Japanese — all pages |
| `i18n/cn.js` | Simplified Chinese — Tauri-only content |

All pages load only `i18n/core.js`; language files are loaded on demand.

---

## Author

Nova — [babelon1882@gmail.com](mailto:babelon1882@gmail.com)
Part of the [深握計畫 (Deep Holding Project)](https://tb1982.github.io/pm/)

Built with [Claude Code](https://claude.ai/claude-code)
