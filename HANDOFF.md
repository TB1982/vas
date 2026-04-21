# HANDOFF · Shell & Docs

> 這份檔案是給宰相（web dev）的交付說明。
> 本包只含兩條交付線——**殼範本**（給 Chapter I~IV 套用）與**操作手冊**（單頁版）。
> 首頁 `index-B.html` 與其專屬 css 不在本包內，另行處理。

---

## 兩條線

### ① 殼範本（Shell）
提供 Chapter I~IV 共用的版型骨架——用 `chapter-shell.html` 作為可執行範本，目前以 Chapter I · 設計 當佔位內容。

- `chapter-shell.html` — 範本 HTML
- `css/shell.css` — 殼專用（chapter-header / toc / section / passage）
- `i18n-keys.md` — 殼用翻譯鍵表（namespace：各 chapter.*）
- `GLOSSARY.md` — 用詞表（Shell / Section / Passage / Trail…）

### ② 操作手冊（Docs）
一頁到底、左側 sticky TOC + scroll-spy、手機折疊選單。

- `docs-shell.html` — 手冊 HTML（單頁，錨點跳轉）
- `css/docs.css` — 手冊專用（雙欄 + sticky TOC + mobile `<details>`）
- `docs-i18n-keys.md` — 手冊用翻譯鍵表（namespace：`docs.*`）

### 共用
- `css/tokens.css` — 顏色 / 字體 / 間距 token，兩邊都 link 它，**不要改、不要分岔**
- `DESIGN-SYSTEM.md` — v1.1，含第 9 節「Docs Mode」，說明殼與手冊的分界

---

## 檔案樹

```
handoff/
├── HANDOFF.md              ← 本檔
├── GLOSSARY.md
├── DESIGN-SYSTEM.md        ← v1.1
├── chapter-shell.html      ← 殼範本（Chapter I 佔位）
├── docs-shell.html         ← 手冊單頁版
├── i18n-keys.md            ← 殼用
├── docs-i18n-keys.md       ← 手冊用
└── css/
    ├── tokens.css          ← 共用
    ├── shell.css           ← 殼用
    └── docs.css            ← 手冊用
```

---

## 給宰相的接手順序建議

1. **先讀 `DESIGN-SYSTEM.md`**——特別是第 9 節 Docs Mode，弄清楚「殼 vs 手冊」的分界（哪些沿用、哪些拿掉、哪些是手冊獨有）。
2. **再讀 `GLOSSARY.md`**——用詞統一，避免把 Section 說成 Passage。
3. **打開兩份 HTML 看實況**——`chapter-shell.html` 和 `docs-shell.html` 都可直接雙擊執行，能看到完成品長相。
4. **i18n 串接時**：
   - 殼用 `i18n-keys.md`，手冊用 `docs-i18n-keys.md`
   - `data-lang-key` 屬性已在 HTML 裡標好
   - 英文字串已全部 ≤28 字元，mobile 375px 不破版（檢查表在 `docs-i18n-keys.md` 底部）

---

## 不要動的事

- **`tokens.css`** — 兩條線共用，改了會牽動全站
- **`DESIGN-SYSTEM.md` 第 9 節** — 若殼與手冊的分界要調整，請先跟設計討論
- **英文 TOC 的 ≤28 字元規則** — 這是 mobile 破版的防線，別為了語意完整放寬
- **`docs-shell.html` 的 scroll-spy `<script>`**（在檔尾）— 這塊是單頁手冊的核心互動，除非要換成第三方庫否則別動

---

## 若要擴充

- **殼新增 Chapter**：複製 `chapter-shell.html`，改 kicker / h1 / 內容區塊，沿用 `shell.css`
- **手冊新增章節**：在 `docs-shell.html` 加 `<section class="docs-section" id="...">`，同步更新兩處 TOC（sticky + mobile `<details>`）與 `docs-i18n-keys.md`

---

## 已知佔位

手冊內容目前是 `【此處由內容撰寫者補上：...】` 的灰字佔位——等 PM／內容撰寫者填實際文案。i18n key 已備好（`docs.sec.*.p1`）。

---

© 2026 · VAS · Nova × Claude
