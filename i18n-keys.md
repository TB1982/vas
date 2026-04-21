# i18n keys · VAS Home v2

Namespace: **`home2`**（和現有 `index` 並存，不覆蓋）

繁中已填；其他三語（简 / EN / 日）由網站宰相接手。

---

## `home2.title`
```
VAS · 給那些未能用文字明說的當下
```

## `home2.meta.desc`
```
VAS 是一只傳遞資訊的煉金容器——把看見的、想說的、想記下的，在進入編輯之前，先承接起來。
```

---

## Nav

| key | 繁中 |
|---|---|
| `home2.nav.design` | 設計 |
| `home2.nav.collaboration` | 協作 |
| `home2.nav.system` | 系統 |
| `home2.nav.milestones` | 里程碑 |

---

## Shrine · 首屏

| key | 繁中 |
|---|---|
| `home2.shrine.kicker` | `A Vessel · since 2026`（此 key 不翻譯——四語保留英文） |
| `home2.shrine.tagline` | `給那些未能用文字明說的<wbr>當下。` |
| `home2.shrine.colophon.zh` | `容器 · 傳遞 · 未完成` |
| `home2.shrine.colophon.en` | `vessel — passage — unfinished`（此 key 不翻譯——四語保留英文副標） |

### Tagline 翻譯斷點提示

斷點用 `<wbr>` 給瀏覽器軟換行提示，避免孤兒字：

- 繁：`給那些未能用文字明說的<wbr>當下。`
- 简：建議 `给那些未能用文字明说的<wbr>当下。`
- EN：`For the moments<wbr> that words could not name.`
- 日：`言葉にならなかった<wbr>その瞬間へ。`

> 斷點位置要讓「最後一塊」至少兩個字元，不讓末行單字懸著。

---

## Shrine Gates · 四道門

| key | 繁中 |
|---|---|
| `home2.gates.1.num` | `I · 設計` |
| `home2.gates.1.name` | `不完美的工具` |
| `home2.gates.2.num` | `II · 協作` |
| `home2.gates.2.name` | `六個故事` |
| `home2.gates.3.num` | `III · 系統` |
| `home2.gates.3.name` | `Harness` |
| `home2.gates.4.num` | `IV · 里程碑` |
| `home2.gates.4.name` | `十八日` |

> **第三道門 · Harness**：此名稱四語保留原文，不翻譯。

---

## Acquire · 取得

| key | 繁中 |
|---|---|
| `home2.acquire.label` | `讓 VAS 走進你的工作流` |
| `home2.acquire.tauri.what` | `Tauri` |
| `home2.acquire.tauri.name` | `VAS 正式版 <em>macOS 12+ · App Store</em>`（內嵌 `<em>`） |
| `home2.acquire.tauri.go` | `→ 前往` |
| `home2.acquire.electron.what` | `Electron` |
| `home2.acquire.electron.name` | `經典版 <em>免費下載 · 持續維護</em>` |
| `home2.acquire.electron.go` | `→ 下載` |
| `home2.acquire.guide.what` | `Guide` |
| `home2.acquire.guide.name` | `操作手冊 <em>工具列 · 編輯器 · 快捷鍵</em>` |
| `home2.acquire.guide.go` | `→ 閱讀` |

> `Tauri` / `Electron` / `Guide` 四語保留英文。

---

## Unfold · 展開的題辭

| key | 繁中 |
|---|---|
| `home2.unfold.label` | `為何存在` |
| `home2.unfold.p1` | `VAS 是一只<em>傳遞資訊的煉金容器</em>——把看見的、想說的、想記下的，在進入編輯之前，先承接起來。` |
| `home2.unfold.p2` | `它不取代任何工具。它是那個<em>中間</em>的位置——在按下截圖鍵、和把檔案丟出去之間，留給你一段可以思考的緩衝。` |
| `home2.unfold.drop` | `這是 VAS 的第一句話，也是最後一句。往下走的四個章節——設計、協作、系統、里程碑——都是這句話的註腳。` |

---

## Chronicle · 版次印記

| key | 繁中 |
|---|---|
| `home2.chronicle.label` | `版次記號` |
| `home2.chronicle.edition` | `第十八日 · 器成` |
| `home2.chronicle.edition.en` | `Eighteenth Day · The Vessel, Formed`（此 key 不翻譯） |

---

## 富文本提醒

以下 key 的值內嵌 HTML 標籤，與 repo 既有慣例（如 `c5phase1Desc`、`gkSteps`）一致：

- `home2.shrine.tagline` · `<wbr>`
- `home2.acquire.*.name` · `<em>`
- `home2.unfold.p1` / `.p2` · `<em>`

i18n 載入時請確保 innerHTML 而非 textContent，否則標籤會被逸出。

---

## 四語總鍵數

**23 個 key** · 繁中全數填好 · 其他三語待填。
