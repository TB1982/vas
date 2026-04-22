# VAS — Visual Annotation Studio

**Product site:** [tb1982.github.io/vas](https://tb1982.github.io/vas/)

A screenshot and visual annotation tool for Mac, built for cross-functional communication.
Born from a collaboration between a PM who can't write a single line of code, and Claude — iterated together over eighteen days.

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

**Archive:** `archive/` — previous versions of all pages above (including v1 variants)

---

## Stack

Static HTML / Tailwind CSS (CDN) / Vanilla JS — no build tools, no package manager.

Quadrilingual (zh-Hant / EN / 日本語 / 简中) via `data-lang-key` + centralized i18n JS files.

---

## i18n Architecture

| File | Role |
|------|------|
| `i18n/core.js` | Runtime loader — `VASCore.loadLang()`, `VASCore.initDropdown()` |
| `i18n/zh.js` | Traditional Chinese (繁體中文) |
| `i18n/en.js` | English |
| `i18n/ja.js` | Japanese (日本語) |
| `i18n/cn.js` | Simplified Chinese (简中) — Tauri only |

Each language file exports a nested object: `shared` (nav, footer) + per-page namespaces (`index`, `home2`, `guide`, …).

---

## CSS Architecture

| File | Used by |
|------|---------|
| `css/tokens.css` | index, chapter shells, docs shell |
| `css/shrine.css` | index — hero section |
| `css/unfold.css` | index — colophon |
| `css/acquire.css` | index — download lines |
| `css/chronicle.css` | index — edition mark |
| `css/shell.css` | Inner page chapter shells |
| `css/docs.css` | Guide / docs shell |

---

## Design System

| File | Description |
|------|-------------|
| `DESIGN-SYSTEM.md` | Visual language spec v1.1 (tokens, typography, motion, Docs Mode) |
| `GLOSSARY.md` | Term definitions shared between design and engineering |
| `HANDOFF.md` | Claude Design → 宰相 handoff notes |
| `chapter-shell.html` | Inner page shell template |
| `docs-shell.html` | Guide/docs shell template |
| `i18n-keys.md` | i18n key list for index |
| `docs-i18n-keys.md` | i18n key list for docs shell |

---

## Author

Nova — [babelon1882@gmail.com](mailto:babelon1882@gmail.com)
Part of the [深握計畫 (Deep Holding Project)](https://tb1982.github.io/pm/)

Built with [Claude Code](https://claude.ai/claude-code)
