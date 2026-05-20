# CLAUDE.md — VAS 產品網站
This file provides guidance for AI assistants working in this repository.
For operational details, workflows, and protocols → see **CLAUDE-process.md**.

---

## Core Rules

1. **Identity & values:** Use the Identity table below. If something is missing or seems out of date, ask Nova first — she's happy to confirm or update.
2. **Never attribute content to anyone other than Nova.**
3. **Never push directly to `main`.** Always develop on a `claude/<description>-<id>` branch.
4. **Match Nova's wave rhythm.**

   *Why:* Site updates come in waves — dense crests where Nova batches scope ("一併修", "派 agent 不要客氣"), alternating with padding when she shifts to app dev. Hesitating mid-crest interrupts momentum.

   *How:* Take dense input by default. Decompose it — chunks / agent dispatch / mechanical sed / save Nova-decisions for her. Pause only when ambiguity blocks progress or the decomposition isn't obvious. If you genuinely need her to slow down, just say so — she's not offended.
5. **`data-lang-key` always requires two updates:** the HTML text node AND the `zh`/`en`/`ja`/`cn` keys in the page's i18n JS file. Missing either causes visible bugs.
   → For large i18n tasks: **CLAUDE-process.md § Haiku Protocol**
6. **Use `臺` not `台`** — `臺灣`, `臺北`, `臺中`. Never substitute silently.

---

## Product Philosophy
**VAS takes its name from Jung's alchemical *vas*** — the vessel that holds prima materia and transforms it into lapis. This is not a metaphor; it is the product's actual definition.

The product's core action: taking what cannot yet be expressed in words, making it visible through annotation, and enabling it to be transmitted to another person.

**Copywriting test — ask before writing any copy:** Does this sentence honor the transformation, or does it describe a feature?
- Fails: "讓資訊順勢滑入編輯模式" — describes a SaaS action
- Passes: "有些話不能只用文字說。VAS 替你把它盛起來。" — names the transformation

The visual logic follows from this, not the other way around.
→ Extended design language reference: **CLAUDE-process.md § Design Language**

---

## Project & Author Identity
**Always use these exact values. Never invent alternatives.**

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

Per-page canonical: `https://yoursvas.app/<filename>` — strip `.html` (clean URL convention; Cloudflare Pages serves both).

### Footer — canonical format
```
由 Cloudflare 部署　｜　Claude Code 傾力打造　｜　Nova（nova@yoursvas.app）最後更新於 2026
Deployed via Cloudflare　｜　Built with Claude Code　｜　Last updated 2026 by Nova (nova@yoursvas.app)
```

### Social / JSON-LD author block
```json
"author": {
  "@type": "Person",
  "name": "Nova",
  "email": "nova@yoursvas.app",
  "sameAs": ["https://www.linkedin.com/in/yingtzuliu","https://www.instagram.com/liuyingtzu"]
}
```

---

## Conventions

- **Commit messages:** Traditional Chinese, action-oriented — `更新手機版顯示數字大小` / `新增 OCR 段落說明`
- **New page:** Update `README.md` and the Repository Structure in CLAUDE-process.md (lower priority than user-visible fixes, but don't let it accumulate).
- **Version update:** Nova states the new version number directly. Update all hardcoded occurrences in HTML and i18n files. Historical narrative versions (e.g. "一週推出 v3.43") carry `<!--歷史版本，不可更動-->` in HTML or `// 歷史版本，不可更動` in JS — never touch these.
- **KM log:** Append to `km.md` immediately when a bug is resolved. Never wait until retro.
- **Translation & per-locale wording:** See `GLOSSARY.md` (root) — locked terminology + per-locale conventions (CN Mainland register, JA shinjitai rules, EN clarity preference, tri-script chapter labels).

---

## Git
- **Remotes (三點等邊網)**:
  - `github` = `https://github.com/TB1982/vas.git` — **Cloudflare Pages 部署來源** (source of truth post-2026-05-20 restoration)
  - `origin` = `https://gitlab.com/babelon1882/vas.git` — GitLab，被動鏡像目標
  - `backup` = `~/vas-backup.git` — 本機 bare repo
- **Main branch:** `main` — Cloudflare Pages 從 **github/main** 部署。永遠不直接推 main，透過 **GitHub PR** 合併。
- **Dev branches:** `claude/<description>-<id>` — 透過 `git pushall <branch>` alias 同時推三個 remote。
- **Auto-mirror:** `.github/workflows/mirror-to-gitlab.yml` 在 github/main 變動時自動鏡像至 gitlab/main（GitHub 是 source of truth，GitLab 是被動鏡像；archive tag `pre-mirror-2026-05-11` 保存 pre-restoration 的 GitHub 原 lineage 於 `bd049e9`）。
- **Backup ethos:** GitHub-suspension lesson — diversification is the careful move, not slowing down.
- CDN dependencies: do not move to local files.

---

## Interaction Language
- Communicate with Nova in **Traditional Chinese**.
- Docs (CLAUDE.md, CLAUDE-process.md, GLOSSARY.md, README, memory files): **English**. Embedded quotes or locale-specific examples use that locale's actual text (繁中 / 简中 / 日本語 / English — whichever the content is in).
- **Prefer open conversation.** Use `AskUserQuestion` only for clean binary/ternary alternatives with clearly-named options — not for open-ended or design-judgment questions where Nova may have a framing not yet enumerated.

---

## When to Open CLAUDE-process.md

| Situation | Section |
|-----------|---------|
| Any HTML / CSS / JS change | § Development Workflow |
| i18n update spanning 2+ files or 20+ keys | § Haiku Protocol |
| Creating a new page | § New Page Checklist |
| Applying Claude Design CSS output | § Claude Design Protocol |
| Checking file locations or ownership | § Repository Structure |
| Large read/write task in the main session | § Trickle-Flow Discipline |
