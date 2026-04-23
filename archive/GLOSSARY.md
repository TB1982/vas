# VAS Redesign · 詞彙表

> 宰相與我之間的共用詞。看到文件裡任何一個詞不確定，先翻這張表。

---

## 結構層級

| 詞 | 意思 | 例 |
|---|---|---|
| **Shell · 殼** | 章節頁的共用骨架——nav、目錄、內容槽、過場、footer 這五塊組合起來 | `chapter-shell.html` 就是殼的範本 |
| **Chapter · 章** | 四個大區塊：I 設計 / II 協作 / III 系統 / IV 里程碑 | 每章一個 HTML 頁面 |
| **Section · 小節** | 章之內的段落 | 章 I 有五節：01 底色、02 字重、03 主體擺位、04 CTA、05 四道門 |
| **Passage · 過場** | 章末往下一章的那段收尾，**不是按鈕** | 安靜收尾 + 下一章名字懸在頁底，一滑過去就翻頁 |
| **Colophon · 落款** | 古書匠人落款的位置 | 首屏瓶子旁已有一處；章末也會用到 |

---

## 元件層級

| 詞 | 意思 | 出現在 |
|---|---|---|
| **Gate · 門** | 首屏那四個入口的稱呼 | 僅首屏 `.shrine-gates` 底下 |
| **Line · 行** | Acquire 區的三行下載條目 | 僅 Acquire |
| **Note-row · 備註列** | 設計備註的「從→到」雙欄列 | 僅 Design Notes（如果要做內部文件） |
| **Chronicle-line · 版次線** | 那道兩端淡、中間紫的漸層橫線 | 首頁版次印記；章末過場會重用 |
| **Halo · 暈光** | 瓶子背後的紫色 radial-gradient + blur | 首屏瓶子（其他地方不要用） |
| **TOC · 章目錄** | 章頂那張「第一節 … 第二節 …」的輕量列表 | 每章開頭 |

---

## 視覺詞

| 詞 | 意思 |
|---|---|
| **Ash · 陶灰** | 字色五階（ash-0 最亮到 ash-4 最淡） |
| **Aurora · 極光** | 瓶子的三色（紫 violet、粉 pink、藍 blue）——**極光只屬於瓶子**，不要亂用 |
| **Void · 曗場** | 深暗底色（三階） |
| **Rule · 分隔線** | 兩階：rule 基本、rule-strong 強調 |

---

## 特殊概念

| 詞 | 意思 |
|---|---|
| **Trail · 光點** | III · 系統 / Harness 的彩蛋——**三顆紫點**：首屏第三道門、Chapter III 章頂、Chapter III 某處（最後一顆是真正的 Harness Engineering 入口）。不說破。 |
| **Unfold · 展開** | 首屏的「為何存在」區塊的別名 |
| **Breathe · 呼吸** | 四個動效：nav brand mark 6s、halo 4s、room 10s、aurora 8s（未用） |

---

## 命名規則

- CSS class 前綴：`shrine-`、`unfold-`、`acquire-`、`chronicle-`、`site-`、`chapter-`（新）、`toc-`（新）、`section-`（新）、`passage-`（新）
- CSS 變數前綴：`--vas-`（避免撞 repo 既有變數）
- i18n namespace：`home2`（首頁 v2）、`ch1` / `ch2` / `ch3` / `ch4`（四章）

> 不用 `nav-`、`btn-`、`card-` 這類泛用名——容易撞 Tailwind 和 repo 既有樣式。
