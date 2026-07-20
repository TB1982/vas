# VAS / 深握計畫

The website for **VAS** — a macOS screenshot annotation tool — and the home of the **深握計畫 (Deep Holding Project)**.

**Live site:** https://yoursvas.app/

---

## What's here

This is a vanilla-JS static site, deployed via Cloudflare Pages. No build tools, no package manager.

### Structure — two sides (2026-06 IA)

The home page (`/`) is two doors: **器 · The Instrument** (the product) and **思 · The Treatise** (the thought). Everything hangs off one of those two sides.

**器 — The Instrument side**

| Page | Path | Role |
|------|------|------|
| Instrument | `/instrument` | 器 · The Instrument — the macOS screenshot tool; its acquire section leads to Changelog / Manual / Milestones |
| Echoes (Mirror Hall) | `/echo` | I · 殘響 · ECHOES — instrument's 鏡廊, the hub for the six chapter pages below |
| ↳ Design | `/insight` | 頁一 · 設計 — five design decisions |
| ↳ Collab | `/collab` | 頁二 · 協作 — six collaboration stories |
| ↳ Trust | `/context` | 頁三 · 信念 — context as a way of trusting yourself |
| ↳ Self | `/self` | 頁四 · 自己 — CLAUDE.md as Jungian Self-mirror |
| ↳ System | `/harness` | 頁五 · 系統 — Harness Engineering (gateway to the 思-side pillars) |
| ↳ Us | `/us` | 頁六 · 我們 — Sapere Aude 2.0 (sitemap-only, not in main nav) |
| Milestones | `/milestone` | 里程碑 · MILESTONE — the narrative journey (十章一終曲, sealed at S104 · 06·28); the per-version/Sprint ledger is split out to Changelog |
| Changelog | `/changelog` | 更新日誌 · CHANGELOG — the full change ledger: Tauri 135 Sprints + Electron 86 versions, newest-first, with rhythm-band / release-density visualizations (reached from instrument's acquire chip and the milestone door) |
| Guide | `/guide` | User manual |
| FAQ | `/faq` | Eight Questions |

The six chapters are three mirror pairs (外 user-facing ↔ 內 dev-reflection): 設計↔協作 · 信念↔自己 · 系統↔我們. Each chapter ends with a left-right pager along one continuous zigzag: `鏡廊(echo) → 頁一 → 頁二 → 頁三 → 頁四 → 頁五 → 頁六 → 冊(treatise)`.

**思 — The Treatise side**

| Page | Path | Role |
|------|------|------|
| Treatise | `/treatise` | 思 · The Treatise — hall presenting two treatises |
| ↳ Harness · Pillar I | `/harness/context` | Context management — 上下文管理的藝術 (sitemap-only) |
| ↳ Harness · Pillar II | `/harness/constraints` | Constraints as guidance — 約束作為引導 (sitemap-only) |
| ↳ Harness · Pillar III | `/harness/entropy` | Coexisting with entropy — 與混亂共處 (sitemap-only) |
| Vessel | `/vessel` | 容器論 — the vas hermeticum treatise (also gated behind harness/self trail-dot doors) |

**Site-wide**

| Page | Path | Role |
|------|------|------|
| About | `/about` | 0 · 序章 · PREFACE — why VAS exists |
| Privacy | `/privacy` | Privacy policy |
| 404 | `/404` | Error page |

**Localization:** Every page — including the three pillars and the treatise — exists in 4 locales as **static per-locale files**: zh-Hant (root), English (`/en/`), Japanese (`/ja/`), Simplified Chinese with Mainland register (`/cn/`). 18 pages × 4 locales, plus `/harness/{context,constraints,entropy}` × 4. There is no runtime i18n — language switching is page navigation.

**Sitemap-only (not in main nav, by design):** `/us`, `/vessel`, and `/harness/{context,constraints,entropy}`. Humans reach them by digging (trail-dot / inline-dot doors); crawlers and AI reach them via sitemap. Hide-from-human ≠ hide-from-machine.

---

## Documentation

| File | Read when |
|------|-----------|
| [CLAUDE.md](CLAUDE.md) | First file any AI assistant should read — core rules, identity, conventions |
| [CLAUDE-process.md](CLAUDE-process.md) | Workflows / protocols / repository structure / 巡水田 phase |
| [GLOSSARY.md](docs/GLOSSARY.md) | Translation terminology + per-locale conventions (CN Mainland, JA shinjitai, EN clarity, etc.) |
| [km.md](docs/km.md) | Known issues & solutions — append-only bug log |
| [designrule.md](docs/designrule.md) | Visual design rules |
| [toolnamemap.md](docs/toolnamemap.md) | Guide tool-name four-language map (from app i18n) |

---

## Author / Project Identity

Canonical values for author attribution and site metadata. Never invent alternatives.

| Field | Value |
|-------|-------|
| Author display name | Nova |
| Author email | nova@yoursvas.app |
| Project name (ZH) | 深握計畫 |
| Project name (EN) | Deep Holding Project |
| Site canonical URL | `https://yoursvas.app/` |
| Copyright year | 2026– |
| LinkedIn | `https://www.linkedin.com/in/yingtzuliu` |
| Instagram | `https://www.instagram.com/liuyingtzu` |

**Per-page canonical**: `https://yoursvas.app/<filename>` — strip `.html` (clean URL convention; Cloudflare Pages serves both).

Site deployed via **Cloudflare Pages** from the **GitHub** repository (source of truth; mirrored to GitLab). Built with **Claude Code**.
