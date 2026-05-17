# VAS / 深握計畫

The website for **VAS** — a macOS screenshot annotation tool — and the home of the **深握計畫 (Deep Holding Project)**.

**Live site:** https://yoursvas.app/

---

## What's here

This is a vanilla-JS static site, deployed via Cloudflare Pages from this GitLab repo. No build tools, no package manager.

### Top-level pages

| Page | Path | Theme |
|------|------|-------|
| Home | `/` | Product showcase, four chapter gates |
| About | `/about` | Chapter 0 · 序章 · PREFACE — why VAS exists |
| Echoes (cover) | `/echo` | Chapter I · 殘響 · ECHOES — frontispiece |
| ↳ Design | `/insight` | 頁一 · 設計 — five design decisions |
| ↳ Collab | `/collab` | 頁二 · 協作 — six collaboration stories |
| ↳ Trust | `/context` | 頁三 · 信念 — context as a way of trusting yourself |
| ↳ Self | `/self` | 頁四 · 自己 — Claude.md as Jungian Self-mirror |
| Harness | `/harness` | Chapter II · 系統 · SYSTEM — Harness Engineering |
| ↳ Pillar I | `/harness/context` | Context management (deep layer) |
| ↳ Pillar II | `/harness/constraints` | Constraints as guidance (deep layer) |
| ↳ Pillar III | `/harness/entropy` | Coexisting with entropy (deep layer) |
| Us (mirror) | `/us` | Chapter II · ⓘ — Sapere Aude 2.0 (sitemap-only, deliberately not in main nav) |
| Milestones | `/milestone` | Chapter III · 里程碑 · CHRONICLE — 25 days, 80+ versions |
| FAQ | `/faq` | Eight Questions |
| Guide | `/guide` | User manual |
| Privacy | `/privacy` | Privacy policy |
| 404 | `/404` | Error page |

**Localization:** Every top-level page exists in 4 locales — zh-Hant (root), English (`/en/`), Japanese (`/ja/`), Simplified Chinese with Mainland register (`/cn/`).

**Two exceptions:**
- `/harness/{context,constraints,entropy}` — in-page JS lang switcher (zh/en/ja), no `/cn/` variants yet. Pending Design refactor.
- `/us` — sitemap-only, no main nav entry, reachable via the inline-dot from `/harness` chapter end (deliberate "humans must dig" design).

---

## Documentation

| File | Read when |
|------|-----------|
| [CLAUDE.md](CLAUDE.md) | First file any AI assistant should read — core rules, identity, conventions |
| [CLAUDE-process.md](CLAUDE-process.md) | Workflows / protocols / repository structure / 巡水田 phase |
| [GLOSSARY.md](GLOSSARY.md) | Translation terminology + per-locale conventions (CN Mainland, JA shinjitai, EN clarity, etc.) |
| [km.md](km.md) | Known issues & solutions — append-only bug log |
| [designrule.md](designrule.md) | Visual design rules |

---

## Author

**Nova** — nova@yoursvas.app

Site deployed via **Cloudflare Pages** from this **GitLab** repository. Built with **Claude Code**.
