# 交接說明 · 2026-06-13 · 設計宰相 → web 宰相

本批為 VAS 網站改版的六頁設計稿（單檔 HTML，含內嵌 CSS/JS）。
所有檔案皆為 `_preview/` 沙盒命名，**上線時的目標檔名由 web 宰相對應**，建議如下：

| 設計稿 | 對應站上頁面 | 說明 |
|--------|--------------|------|
| `index0613.html` | `index.html` | 新首頁（上一任宰相最終版，直接改在專案根目錄 `index.html`） |
| `instrument-hall.html` | `instrument.html`（器的入口頁） | 正廳 + 取得（雙版本下載卡） + 鏡廊（3D 推進） |
| `treatise-hall.html` | `treatise.html`（思的入口頁） | |
| `harness-constraints.html` | 三柱之一 | |
| `harness-context.html` | 三柱之一 | |
| `harness-entropy.html` | 三柱之一 | |

## 共同注意事項

1. **資源路徑**：除 `index.html` 外，設計稿位於 `_preview/` 子層，圖片引用為 `../img/vasweb.webp`。
   搬到站點根目錄時需把 `../img/` 改為 `img/`（`index.html` 本身已是根目錄路徑，請核對）。
2. **i18n**：設計稿僅有繁中版。`data-lang-key` 與 `en/ja/cn` 四語檔需由 web 宰相按
   CLAUDE-process.md § Haiku Protocol 補齊。語言切換列的連結（`en/instrument.html` 等）已預留。
3. **內部連結**：頁內以相對路徑指向 `guide.html` / `faq.html` / `about.html` /
   `insight.html` / `collab.html` / `context.html` / `self.html` / `harness.html` /
   `us.html` / `treatise.html` / `privacy.html` / `index.html`，請核對與站上實際檔名一致。
4. **SEO**：設計稿未含 canonical / JSON-LD / OG meta，上線前需按
   CLAUDE-process.md § SEO & Structured Data 補。
5. **臺字原則**：文案已遵守「臺」不用「台」；新增文案時同樣遵守。

## instrument-mirror-v2 的行為備註（本批改動最多的一頁）

- **鏡廊推進**以 2D `scale()` 模擬透視（等價公式 `PERS/(PERS-ez)`），刻意**不用**
  `translateZ`/`clip-path`——iOS WebKit 對 3D 變形的裁切不可靠，會壓平景深並產生橫向滾軸。
  請勿「優化」回 3D transform。
- 捲動行程分兩段：前 78% 穿越三面鏡；後 22% 停駐——「ONE VESSEL · TWO WALLS · THE HALL
  OPENS ONTO 思」浮現、門再逼近（`DWELL = 0.78`、`APPROACH = 420`）。
- 窄螢幕（≤900px）鏡框穿越後提早淡出（`nearEnd = 290`），避免殘影留在門上；門本身維持 550。
- 鏡廊順序為 I Insight↔Collab、II Context↔Self、III Harness↔Us（由淺至深，Nova 定案）。
- `prefers-reduced-motion: reduce` 時鏡廊整段隱藏、改顯示攤平版 `.hall-mobile` 與靜態
  `.hall-cap`，請保留這個分支。
- 下載卡 App icon 目前以 `vasweb.webp` 置於黑/米白圓角方塊內作替身；正式 icon 匯出檔
  （黑底/白底瓶身）到位後直接替換 `img src` 即可。

## Git

依 CLAUDE.md：開 `claude/<description>-<id>` 分支、繁中 action-oriented commit、
`git pushall <branch>` 三 remote 同推、經 GitHub PR 合併進 main。
