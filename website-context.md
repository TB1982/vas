# VAS Website Context
_This file is maintained by the website Claude (宰相) and synced to vas-desktop for Tauri's reference._
_Last updated: 2026-04-07_

---

## Site
**URL:** https://tb1982.github.io/vas/
**Stack:** Static HTML, Tailwind CSS (CDN), Vanilla JS, trilingual (zh-Hant / EN / JA)

---

## The Story We Tell the World

VAS was built by **a PM who can't write a single line of code**, working with Claude Code.
The website exists to tell that story — not just to sell the app.

Reading flow (shallow → deep):
```
index → collab → harness → milestone
設計    協作      系統        里程碑
```

---

## Inner Pages — Tauri's Memory

### 1. 設計洞察 — Design Insights
**File:** `insight.html`
**URL:** https://tb1982.github.io/vas/insight.html
**What it says:** The design thinking behind VAS — why it looks and works the way it does. Covers visual language, UX decisions, and the philosophy of "annotation as communication."

---

### 2. 開發協作筆記 — Collab Notes
**File:** `collab.html`
**URL:** https://tb1982.github.io/vas/collab.html
**What it says:** How Nova and Claude built VAS together. Documents the evolution of collaboration rules from zero — every rule has a story behind it. Tagline: **「這不是 Prompt 工程的故事。」**

Key themes:
- CLAUDE.md as team charter
- KM (Knowledge Management) as external memory
- Sprint structure for session continuity
- The rule: never wait for Retro to log a KM

---

### 3. 系統建構裏話 — Harness Engineering
**File:** `harness.html`
**URL:** https://tb1982.github.io/vas/harness.html
**What it says:** An 8-chapter essay on methodology. The deepest layer of the VAS story.

Tagline: **「用文組的思維，做最硬核的開發」**
Subtitle: 一個不會寫程式的 PM，如何跟一個失憶大師一起把一個 macOS App 送進 Apple 審查——以及為什麼這個方法論的名字，她到最後才知道。

Chapter overview:
- §01 熵與為何不能要求 AI 完美
- §02 AI 犯的不是技術錯誤
- §03 心理敏捷開發（含圖解）
- §04 整合陰影，而非否認它（榮格 × AI 行為）
- §05 架構，而不僅止是流程（KM / CLAUDE.md / Sprint）
- §06 每個 KM 都是一顆掉下來的蘋果（Electron vs Tauri）
- §07 Harness Engineering — 命名這件事
- §08 共時性 — OpenAI 對照表 + 榮格結語

**§08 的關鍵數字：**
| | OpenAI 實驗 | VAS |
|---|---|---|
| 團隊人數 | 3–7 位工程師 | 1 PM + 1 失憶大師 |
| 開發時間 | 五個月 | 17 天 |
| 總迭代次數 | 約 1,500 | 1,284+（還在數） |
| 每日平均迭代 | 約 10 | 約 75 |
| 人類寫的程式碼 | 零行（規定） | 零行（做不到） |

The essay ends: _「榮格笑著望著我——共時性。」_

---

### 4. 里程碑 — Milestone
**File:** `milestone.html`
**URL:** https://tb1982.github.io/vas/milestone.html
**What it says:** Full version history and roadmap. Covers the Electron era → Tauri migration → Apple submission.

---

## Current App Status
- **Electron version:** Live, free download
- **Tauri version:** Submitted to Apple App Store review (as of 2026-04)
- **Version string on site:** search `迭代至 v` in `index.html` for current number

---

## Author
**Nova** — babelon1882@gmail.com
The PM. The one who can't write code. The one who built it anyway.
