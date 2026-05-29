# self.html · 無相改版交付　（Claude Design → web 宰相）

> 參考實作檔：`self-mirror.html`（drop-in，已用真 `css/tokens.css` + `css/shell.css`）。
> 一句話：這是把〈自己〉從共用章頁殼放出來、做成一面「會下沉的鏡子」。**留白與克制是功能，不是漏做。**

---

## 範圍
- 只動 **繁中 root `self.html`**。
- `en/ja/cn` 之後照 **Vessel 法**另開：整份語言檔、段落對接翻譯、**不用 i18n key**（與現有 self.html 一致）。

## 套用方式（surgical，不要整檔覆蓋）
1. **先比對 nav + footer 與 repo 現況。** 我的 nav/footer 是 main 快照；若 repo 之後改過，**保留 repo 版**，只換下面兩塊。
2. **替換整個 `<main>`** 為 `self-mirror.html` 的 `<main class="self2">…</main>`。
3. **在 `<head>` 加入**頁面 scoped `<style>`（`.self2 / .gloss / .mirror / .faces / .face-para / .mirror-quote / .self2-coda` 整段）。
4. **移除**原 self.html 的：
   - 章目錄 `<nav class="toc">…</nav>`
   - 右側呼吸燈 `<nav class="dot-nav">` + `.dot-nav-trigger` + 對應的 `initDotNav` inline script

## ⚠️ 刻意為之，不要「修」回去
- **拿掉 TOC 與 dot-nav 是設計決定**，不是疏漏。無相頁不導覽，讓讀者往下沉。請勿依全站 nav 一致性慣例補回。（若要保留全站一致性，請先問 Nova。）
- **鏡句一律不加粗、不上紫底線、不加框**。任何強調都會讓鏡子偏向「佛 / 般若」其中一面——中性是這頁的功能要求。
- 留白大、字少是刻意的。**不要為了「填滿」而加內容或縮小間距。**

## 不要動
- `css/tokens.css`、`css/shell.css` —— 本頁新樣式**全部 scoped 在頁內 `<style>`**，沒碰共用檔。
- i18n —— 繁中 body **無 data-lang-key**，不需碰 `i18n/*.js`。
- `.m-br` 是 tokens.css 既有工具，無新依賴。

## 內容文字異動（Nova owns；列出供 en/ja/cn 對齊）
- coda：「撕破所有**的** Persona」→「撕破所有 Persona」
- §07：「言和行在同一個位置**——**」→「…同一個位置**。**」
- §07：「**而**從 Ego 寫的句子…」→「從 Ego 寫的句子…」（與「從 Self…」平行，鏡子才不歪）
- §07 重構：Ego/Self 的「書寫」段落收進 diptych 兩欄；「句子」兩句升為中央鏡句；開場三句框架合併為一段。

## QC（標準 checklist + 本頁特別項）
- 中 → EN → 日 → 簡 切換（本頁靠語言檔，非 key）。
- **375px**：`.faces` 兩欄在 ≤680px 堆疊；`.m-br` 斷點在 ≤768px 生效。
- **PC**：§07 問句「你的 Claude.md 裡，有多少句是你自己呢？」整句攤平一行（不折）。
- **巡水田**：§07 收尾音量階梯—— 後果對（ash-1·中）→ 問句（ash-0·峰）→ coda（ash-2·殘響）三者可區分。

## 收尾後
- 更新 `km.md`（若沿途有踩坑）。
- en/ja/cn 完成後補 `sitemap.xml` hreflang（如沿用既有 self URL 則不需新增）。
