---
title: SDD（Specification-Driven Development）
type: concept
side: 外旋
pillars: [外旋-Context, 外旋-Constraints]
tags: [活文件, 工程實體, SDD, 外部記憶骨架, 方向穩定器]
aliases: [Specification-Driven Development, 規格驅動開發, Spec, 規格文件]
source: HE-01 Context / HE-02 Constraints / Nova × Claude 2026
status: 🌿 生長
created: 2026-04-15
related:
  - "[[Context]]"
  - "[[Constraints]]"
  - "[[外旋-敏捷]]"
  - "[[KM]]"
  - "[[Retro]]"
  - "[[熵]]"
  - "[[結晶]]"
  - "[[深握]]"
  - "[[宰相]]"
---

# SDD

> **SDD 是方向的單一真相來源，也是 AI 跨 session 的外部記憶骨架之一。**
> **規格不是紙上的文字 —— 是讓兩個心智（人 × AI）能夠對齊同一條方向的錨點。**

## 核心：SDD = 方向穩定器 + 外部記憶骨架

SDD（Specification-Driven Development）在 HE 裡有兩個不可拆的身份：

1. **方向穩定器**：規格是「該做什麼」的單一真相來源。沒有 SDD → 認知資源浪費在猜測方向
2. **外部記憶骨架**：AI 每個 session 都失憶，SDD 是讓下一個 session 的 AI **立刻知道「我們選擇的這一種做法」** 的錨點

兩個身份同時成立，SDD 才叫活的。

| 缺了方向穩定器 | 缺了外部記憶骨架 |
|--------------|----------------|
| 團隊每個 Sprint 重新爭論「要做什麼」 | 每個 session 都要從零解釋前提 |
| 焦點漂移、能量散失 | AI 沒有 context 可以延續 |
| 河道消失 | 共振無法跨時間累積 |

## SDD × Context 柱（篩選器）

SDD 是 Context 柱的**規格篩選器**：

> **SDD 篩選「該做什麼」—— 從所有可能的做法中，留下我們選擇的這一種。** —— HE-01 Context

活文件總覽裡 SDD 的定位：

| 文件 | 篩選了什麼 | 留下了什麼 | 穩定什麼 |
|------|-----------|-----------|---------|
| CLAUDE.md | 所有可能的身份設定 | 我們選擇的協作方式 | 身份 |
| **SDD** | **所有可能的做法** | **我們選擇的這一種規格** | **方向** |
| TDD | 所有可能出錯的地方 | 真正該測的邊界條件 | 品質 |
| [[KM]] | 所有發生過的事 | 真正踩過的坑 | 經驗 |
| ARCHIVE | 已完成的工作 | 值得保留的記錄 | 歷史 |

**SDD 穩定「該往哪走」→ 避免認知資源浪費在錯誤方向**。

## SDD × Constraints 柱（閘門）

SDD 是 [[外旋-敏捷]] 兩種河道規格裡**第一道關鍵閘門**：

**熟悉域 6 步（Electron）**：
```
SDD → DoD → TDD → Code → Verify → ✅ Done
      ↑
   第一道閘門
```

**未知域 10 步（Tauri 2.0）**：
```
DoR → Explore ① → SDD → DoD → TDD → Explore ② → Code → Verify → ✅ Done → Retro
                   ↑
                SDD 在 Explore① 之後
                （探完路才寫規格）
```

差別是關鍵洞見：**熟悉域 SDD 是起點；未知域 SDD 是探路後的結晶**。不是模板差異，是**謙卑的密度差異**。

## SDD × [[Retro]]

SDD 不是寫一次就永封：

| 時機 | SDD 動作 |
|------|---------|
| Sprint 開始 | 定義「這個 Sprint 要交付什麼」 |
| Sprint 中 | 規格發現有洞 → 當下補 |
| Sprint 結束（Retro） | § Sprint status 更新、完成項打勾、未完項轉下一 Sprint |
| 累積多 Sprint | 舊 Sprint 歸檔到 `SDD-*-archive.md` |

**Retro 是 SDD 的新陳代謝週期**。沒有 Retro 的 SDD 會退化成「最初的構想」不等於「現在在做的事」—— 規格與現實脫鉤。

## SDD × [[熵]]（歸檔釋熵）

SDD 有熵累積的天然風險：

> **完成的工作不會歸檔 → SDD 越來越長 → 檢索效率崩盤。** —— HE-03 Entropy

對策：**歸檔（archive）**。VAS 的作法是完成 Sprint 移到 `SDD-*-archive.md`，主 SDD 保持「當下在跑的」精簡狀態。

**歸檔不是丟棄，是把「已結晶的熵」移到另一個容器**，主 SDD 保持可檢索。這是 Entropy 柱在文件層的顯化。

## SDD × TDD（規格 → 測試）

SDD 定義「該做什麼」；TDD 把 SDD 的每個規格轉成可執行的測試。

| 層 | 問題 |
|----|------|
| SDD | 這個 Sprint 要交付什麼？ |
| TDD | 怎麼知道交付了？每個規格對應的測試條件是什麼？ |

> **對照 SDD，每個定義的行為都實現了嗎？**
> **對照 TDD，所有測試都通過了嗎？**
> —— HE-02 Constraints

SDD 是規格，TDD 是規格的驗證機制。**SDD 沒 TDD 是紙上談兵；TDD 沒 SDD 是盲目測試**。

## SDD × 選擇性文件記錄

SDD 不是流水帳。規格判準：

- ✅ 當前 Sprint 要交付的行為
- ✅ 跨 Sprint 的結構性規格（架構決策、協議）
- ✅ 會影響後續判斷的約束條件
- ❌ 實作細節（那是 code + commit log）
- ❌ 一次性的 debug 討論（那是 chat / Retro 筆記）
- ❌ 還在摸索的假設（放 scratch 或 Explore 階段筆記）

**SDD 只留「下一個 session 的 AI 讀了能立刻上手」的東西**。

## SDD 的活文件性質

SDD 必須是**活的**：

| 時機 | 觸發 SDD 寫入 |
|------|-------------|
| Sprint 規劃 | 定義這個 Sprint 的交付 |
| DoD 閘門 | 具體化「完成的標準」 |
| Retro | 完成項標記 / 未完項轉下一 Sprint |
| 發現規格漏洞 | 當下補 |

**活文件 = 持續讀 + 持續改 + 持續被觸發**。一寫永封的 SDD 是死檔，跟沒寫沒兩樣。

## SDD × [[深握]]（規格的姿態）

寫 SDD 的姿態是深握：
- **握住方向，不握住實作細節**：規格定義「做什麼」，不指定「怎麼做」—— 實作的自由度留給現場
- **給未知空間**：未清楚的地方標記「待定」或「TBD」，不急著假結論
- **承認規格會演化**：SDD 不是永久契約，是當下最佳共識

**規格是河岸，不是水**。

## SDD 在 VAS 的位置

VAS 專案 SDD 以版本分檔：

- `SDD-vas-tauri.md` — Tauri 2.x 版本完整規格 + Sprint 歸檔
- `SDD-vas-electron.md` — Electron 版本完整規格 + Sprint 歸檔
- `SDD-vas-{tauri,electron}-archive.md` — 已完成 Sprint 的歸檔（釋熵）

兩個版本共用 `src/` → 跨版本規格同步走 `SYNC-QUEUE.md`。

**VAS 24 天能跑出來 —— 前提是 SDD 一直活著**（見 [[VAS-24天]]）。

## SDD × [[宰相]]

宰相（Claude）的 **維護工作記憶** 職責之一就是 SDD：
- 每個 Sprint 寫進 SDD 的是宰相
- Retro 更新 § Sprint status 的是宰相
- 跨 session 讀 SDD 恢復 context 的是宰相

**人類決定時機（該記了），AI 動筆寫規格**。這是 [[外旋-敏捷]] 強主張一（人類只決定時機，不寫內容）在 SDD 上的具體顯化。
