# CLAUDE.md — VAS 產品網站
This file provides guidance for AI assistants working in this repository.
For operational details, workflows, and protocols → see **CLAUDE-process.md**.

---

## Core Rules

1. **Never fabricate identity details.** Use only values from the Identity table below — no invented emails, URLs, or author names.
2. **Never attribute content to anyone other than Nova.**
3. **Never push directly to `main`.** Always develop on a `claude/<description>-<id>` branch.
4. **Never force-process high-density input in a single pass.** When Nova provides multiple documents, frameworks, or dense content layers in one turn, say: *"Let me absorb this layer first — bring me the next one when I'm ready."*
5. **`data-lang-key` always requires two updates:** the HTML text node AND the `zh`/`en`/`ja`/`cn` keys in the page's i18n JS file. Missing either causes visible bugs.
   → For large i18n tasks: **CLAUDE-process.md § Haiku Protocol**
6. **Use `臺` not `台`** — `臺灣`, `臺北`, `臺中`. Never substitute silently.
7. **Milestone numbers require Nova's approval before any edit.** All specific figures in the `milestone` i18n namespace (version numbers, day counts, Sprint counts, dates) must be confirmed with Nova before changing. Nova holds the correct memory — do not infer, update, or globally replace these values unilaterally.
8. **Version release checklist — update all three locations together:**
   - `index.html` JSON-LD `softwareVersion` (Tauri track only — this is the App Store primary)
   - `index.html` JSON-LD offers `name`: `"VAS Pro (Tauri vX.X.X · App Store)"` and `"VAS Classic (Electron vX.XX · Free)"`
   - `index.html` JSON-LD offers `url` for the Electron download link (`/releases/download/vX.XX.X/VAS-X.XX.X-arm64.dmg`)
   - Tauri and Electron version numbers are **independent counters**. Tauri started at v1.0; Electron's first public release was v3.43. Never assume they are in sync.

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
| Author email | babelon1882@gmail.com |
| Project name (ZH) | 深握計畫 |
| Project name (EN) | Deep Holding Project |
| Site canonical URL | `https://tb1982.github.io/vas/` |
| Copyright year | 2026– |
| GitHub | `https://github.com/tb1982` |
| LinkedIn | `https://www.linkedin.com/in/yingtzuliu` |
| Instagram | `https://www.instagram.com/liuyingtzu` |

Per-page canonical: `https://tb1982.github.io/vas/<filename>.html`

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

## Conventions

- **Commit messages:** Traditional Chinese, action-oriented — `更新手機版顯示數字大小` / `新增 OCR 段落說明`
- **New page:** Always update `README.md` and the Repository Structure in CLAUDE-process.md.
- **Version update:** Nova states the new version number directly. Update all hardcoded occurrences in HTML and i18n files. Historical narrative versions (e.g. "一週推出 v3.43") carry `<!--歷史版本，不可更動-->` in HTML or `// 歷史版本，不可更動` in JS — never touch these.
- **KM log:** Append to `km.md` immediately when a bug is resolved. Never wait until retro.

---

## Git
- **Remote:** `https://github.com/TB1982/vas.git`
- **Main branch:** `main` (GitHub Pages source — never push here directly)
- **Dev branches:** `claude/<description>-<id>`
- CDN dependencies: do not move to local files.

---

## Interaction Language
- Communicate with Nova in **Traditional Chinese**.
- CLAUDE.md and CLAUDE-process.md are written and maintained in **English**.

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
