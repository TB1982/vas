# VAS 首頁 v2（Version B · 煉金侘寂）· repo-ready

> 交付給網站宰相 · 2026-04-21 · Nova × Claude

這個資料夾是把 `vas-redesign/proposal-B.html` 的**首頁部分**（PART 1 · Home）
拆成可以直接進 repo 的小檔案。提案文件本身（封面、設計備註、結語）不包含在這裡——
那些只是給你跟 Nova 讀的說明文。

## 與現有首頁的關係

現有首頁（`i18n.index`）不動。本次交付是**候選第二版**，用 namespace
`home2` 並存，讓 Nova 跟你決定何時切換。

- 檔名：`index-B.html`（建議最終 merge 時改為 `index.html`，舊版移至 `index-v1.html` 備存）
- i18n namespace：`home2`（完整 key 清單見 `i18n-keys.md`）

## 檔案結構

```
repo-ready/
├── README.md              ← 本檔
├── index-B.html           ← HTML 骨架（< 200 行，只有結構 + data-lang-key）
├── css/
│   ├── tokens.css         ← ash-0~4 灰階、aurora 三色、字型變數
│   ├── shrine.css         ← 首屏：題辭 + 瓶子 + 四道門
│   ├── unfold.css         ← 展開的題辭
│   ├── acquire.css        ← 下載三行（註腳位）
│   └── chronicle.css      ← 版次印記（第十八日 · 器成）
├── img/
│   └── vasweb.webp        ← 與 proposal-B 同一張圖（不動）
└── i18n-keys.md           ← 所有 data-lang-key 對照表
```

## 技術決策

### Tailwind + 原生 CSS 混用

- **結構排版**（padding / grid / flex / max-width）→ Tailwind utility class
- **視覺品牌相關**（ash 灰階、aurora 紫光、drop-shadow 瓶子光暈、breathe keyframes、
  linear-gradient 印記線）→ 原生 CSS 變數與 class

這樣每個檔案都小、職責清楚，Tailwind 不會被迫配置它不擅長的語義色階。

### 字型

直接用 Google Fonts CDN，沿用 `base.css.v3-proposal` 的三軌分工：
- `--serif`：Shippori Mincho + Fraunces + Noto Serif TC（題辭、大標）
- `--mono`：JetBrains Mono（meta 標籤、版次）
- sans 沒在這頁使用（B 首頁極簡，只有 serif + mono）

### i18n

- namespace 使用 `home2`，與 `index` 並存
- 部分富文本值內嵌 HTML（`<em>`、`<wbr>`、`<br>`）——與你既有慣例一致
  （如 `c5phase1Desc` 內嵌 `<code>`、`gkSteps` 內嵌 `<li>`）
- 繁中 key 我已列在 `i18n-keys.md`，其他三語由你接手

## 給宰相的檢查清單

- [ ] `base.css.v3-proposal` 已在 repo 生效（本頁依賴 `--font-serif` / `--font-mono`）
- [ ] i18n core.js 支援 `home2` namespace 載入
- [ ] 四語 `home2` key 都填好
- [ ] header / footer 若要沿用 `shared.footer`，移除 `index-B.html` 裡的 footer，改 include repo 既有 footer partial
- [ ] 驗證 375 / 768 / 1280 三個寬度

## Nova QC

```bash
python3 -m http.server 8081
# 訪問 http://localhost:8081/index-B.html
```

**驗收點：**
- 瓶子有紫色 drop-shadow 光暈、4 秒呼吸
- 四道門 hover 有底線橫過 + 章節名右移 2px
- 切語言時（繁/簡/EN/日），題辭 tagline 不會出現孤兒字
