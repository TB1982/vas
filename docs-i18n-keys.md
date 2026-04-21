# i18n keys · VAS Docs（操作手冊 · 單頁版）

Namespace: **`docs`**

> 手冊是**一頁到底**——左側 TOC 是錨點跳轉，不是跨頁連結。所有 `href` 都是 `#id` 形式。
> 語彙規則：清晰第一、不隱喻、不文青、不用「器物/承接/呼吸」這類首頁詞彙。

---

## Meta

| key | 繁中 |
|---|---|
| `docs.title` | `操作手冊 · VAS` |
| `docs.meta.desc` | `VAS 操作手冊——從第一次打開，到熟練使用，一頁讀完。` |

## TOC 通用

| key | 繁中 | EN（≤28 字元） |
|---|---|---|
| `docs.toc.label` | `Table of Contents` | `Table of Contents` |
| `docs.toc.mobile.label` | `跳到 · Jump to` | `Jump to` |
| `docs.nav.welcome` | `Welcome on Board` | `Welcome on Board` |

## TOC 分組 kicker

| key | 繁中 | EN |
|---|---|---|
| `docs.nav.group.start` | `入門 · Getting Started` | `Getting Started` |
| `docs.nav.group.core` | `核心 · Core` | `Core` |
| `docs.nav.group.adv` | `進階 · Advanced` | `Advanced` |

## TOC 項目（錨點）

| key | 錨點 | 繁中 | EN（≤28 字元） |
|---|---|---|---|
| `docs.nav.start.first` | `#first-launch` | `第一次打開 VAS` | `First Launch` |
| `docs.nav.start.perm` | `#permissions` | `授權與隱私` | `Permissions & Privacy` |
| `docs.nav.start.capture` | `#first-capture` | `第一次截圖` | `Your First Capture` |
| `docs.nav.core.toolbar` | `#toolbar` | `工具列` | `Toolbar` |
| `docs.nav.core.editor` | `#editor` | `編輯器` | `Editor` |
| `docs.nav.core.shortcuts` | `#shortcuts` | `快捷鍵` | `Shortcuts` |
| `docs.nav.adv.custom` | `#customization` | `自訂設定` | `Customization` |
| `docs.nav.adv.tips` | `#tips` | `Tips & 疑難` | `Tips & Troubleshooting` |

## Welcome 區塊

| key | 繁中 |
|---|---|
| `docs.welcome.h1` | `Welcome on Board` |
| `docs.welcome.dek` | `這是 VAS 的操作手冊，一頁讀完。往下捲是「入門 → 核心 → 進階」的順序；左側目錄永遠在——點一下就能跳到任何一節。Ctrl + F 搜尋也可以。` |

## 內容占位（待宰相／PM 填）

這些 key 目前在 HTML 裡是 `【此處由內容撰寫者補上：...】` 的灰字占位，翻譯時直接填實際內容即可。

| key | 該節主題 |
|---|---|
| `docs.sec.first.p1` | 下載 / 安裝 / 啟動 三步驟 |
| `docs.sec.perm.p1` | macOS 螢幕錄製權限、資料存放、隱私聲明 |
| `docs.sec.capture.p1` | 呼出 → 框選 → OCR → 編輯 → 送出 五步流程 |
| `docs.sec.toolbar.p1` | 工具列各按鈕（彈窗互動已在 app 內） |
| `docs.sec.editor.p1` | 編輯器的區塊、選取、修改、匯出 |
| `docs.sec.shortcuts.p1` | 全域快捷鍵表（建議用 docs-accordion 分組） |
| `docs.sec.custom.p1` | 外觀 / 快捷鍵 / OCR 選項 |
| `docs.sec.tips.p1` | FAQ（建議用 docs-accordion） |

---

## 英文斷點檢查（mobile ≤375px）

| EN 標題 | 字元 | 狀態 |
|---|---|---|
| `First Launch` | 12 | ✅ |
| `Permissions & Privacy` | 20 | ✅ |
| `Your First Capture` | 18 | ✅ |
| `Toolbar` | 7 | ✅ |
| `Editor` | 6 | ✅ |
| `Shortcuts` | 9 | ✅ |
| `Customization` | 13 | ✅ |
| `Tips & Troubleshooting` | 22 | ✅ |

全部 ≤28 字元，mobile 不會破版。

## 日文／簡中建議

| 區塊 | 日 | 簡中 |
|---|---|---|
| 入門 | `はじめに` | `入门` |
| 核心 | `基本` | `核心` |
| 進階 | `応用` | `进阶` |

---

## 富文本提醒

- `docs.welcome.dek` 可內嵌 `<em>` 強調關鍵字（如「一頁讀完」「永遠在」）——看翻譯需要
- 占位 `docs.sec.*.p1` 未來內容可能包含 `<em>`、`<code>`、列表——i18n loader 請用 innerHTML
