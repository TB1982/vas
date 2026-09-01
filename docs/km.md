# KM — VAS 網站已知坑與解法

## 1. 錨點捲動在手機版落點錯誤（最終解）

**症狀**
點選漢堡選單裡的錨點連結（如「起源」），頁面捲動到錯誤位置；或先捲到正確位置，再被拉回上方錯誤位置（snap 行為）。桌機版 pill 直接點擊正常。

**根本原因（四層疊加，逐步發現）**

| 層次 | 原因 | 影響 |
|------|------|------|
| 1 | 懶加載圖片缺少 `width`/`height` | 圖片載入前高度=0，錨點位置計算偏小 |
| 2 | `getBoundingClientRect()` 在 `close()` 之後、layout 穩定之前呼叫 | 選單收起尚未完成 layout pass，拿到舊值 |
| 3 | 偏移量 `+8px` 太小 | divider 貼著 header，上方沒有呼吸空間 |
| 4 | `window.scrollTo` 與 iOS Safari 原生 anchor 行為競爭 | 先捲對了，再被瀏覽器拉到它自己算的位置（snap） |

**最終解法**

```html
<!-- 所有 loading="lazy" 的圖片必須加 width/height 屬性 -->
<img src="img/foo.webp" width="1920" height="1080" loading="lazy" ...>
```

```css
/* base.css：scroll-margin-top 對齊 sticky header 實際高度 */
.divider {
  scroll-margin-top: 108px; /* header ~64px + 44px buffer */
}
```

```js
// 使用 scrollIntoView（瀏覽器原生），iOS 不會再跟自己競爭
// href="#" 單獨處理，避免 querySelector("#") 拋 SyntaxError
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return; // 回頁首：讓瀏覽器原生處理
        const target = document.querySelector(href);
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});
```

**偵錯歷程摘要**
1. 圖片 CLS → 加 width/height
2. 落點仍偏 → 計算移入 rAF
3. 落對後 snap 回上方 → 換用 scrollIntoView
4. 凌晨 00:44 手機驗收通過（歷時一個下午 + 65 張截圖）

**規則**
- 懶加載圖片一律補 `width`/`height`
- scroll handler 優先用 `scrollIntoView`，不要自己算位置
- `scroll-margin-top` = header 實際高度 + 與 page-section padding-top 對齊的 buffer

---

## 2. iOS Safari `window.scrollTo` 與原生 anchor 競爭

**症狀**
自訂 `window.scrollTo({behavior:'smooth'})` 跑完後，頁面被拉到另一個位置（snap）。

**原因**
iOS Safari 在 `e.preventDefault()` 之後仍可能觸發原生 anchor scroll，兩者覆蓋最終位置。

**解法**
改用 `scrollIntoView`（見坑 1 最終解）。

---

## 3. 首頁 VAS logo 重疊

**症狀**
浮動 nav 與 sticky header 各有一個 VAS，捲動時兩個重疊。

**根本原因**
設計層次過多：浮動 nav（z-60）＋ sticky header（z-50）各自渲染 VAS logo。

**解法**
移除浮動 nav，將頁內錨點連結整合進 sticky header：
- 手機：hamburger 下拉選單（`sm:hidden`）
- 桌機：pill group（`hidden sm:flex`）

只剩一個 VAS，問題消失。

---

## 4. `getBoundingClientRect` vs `offsetTop` 的選擇

**結論：優先用 `scrollIntoView`；若需手動計算，用 `getBoundingClientRect() + window.pageYOffset`，不用 `offsetTop` 遞迴加總。**

`offsetTop` 遞迴：在有 `position: relative` 祖先、margin collapsing 或 sticky 元素的情況下，容易算錯。
`getBoundingClientRect() + pageYOffset`：瀏覽器直接給絕對座標，更可靠——但必須在 layout 穩定後呼叫，且在 iOS 上仍可能與原生行為衝突。
`scrollIntoView`：最省事，讓瀏覽器自己處理所有平台差異。

---

## 5. `href="#"` 觸發 anchor scroll handler 拋錯

**症狀**
點擊 `href="#"` 的連結（如 VAS logo 回頁首），console 出現 SyntaxError。

**原因**
`document.querySelector("#")` 是無效 CSS selector，會拋 SyntaxError。我們的 scroll handler 攔截所有 `a[href^="#"]`，包含 `href="#"`。

**解法**
```js
if (href === '#') return; // 在 querySelector 之前提早 return
```

---

## 6. 圖片語言切換未更新 width/height 屬性

**症狀（潛在）**
切換語言時 `switchLanguage()` 更換 `img.src`，但 HTML 上的 `width`/`height` 屬性仍是原始語言的尺寸，可能造成 CLS。

**現況**
`vastoolbar`、`vasframe`、`sharesheet`、`fast` 四張圖有多語言版本（`-jp`、`-en`）。若各語言版本尺寸相同則無影響；若不同，需在 `switchLanguage` 裡一併更新屬性：

```js
img.src = '...';
img.width = 1920;
img.height = 1080;
```

**待確認**：各語言版本是否尺寸相同。

---

## 7. guide.html 手機版多重 CSS cascade 問題（2026-04）

**症狀群**
1. 手機版 docsDek 說明文字不顯示
2. 呼吸燈觸發點（`.dot-nav-trigger`）在 guide 頁手機版不出現
3. 點擊呼吸燈圓點無反應（游標變手形，但選單不打開）
4. 段落間距在手機版過大

**根本原因**

| # | 症狀 | 根本原因 |
|---|------|----------|
| 1 | docsDek mobile 不顯示 | `.docs-dek--mobile { display: none; }` 全域規則寫在 `@media` 的 `display: block` **之後**，cascade 蓋掉 |
| 2 | 呼吸燈圓點不出現 | `body.is-guide .dot-nav-trigger { display: none; }` 的 specificity (0,2,1) > shell.css 的 `.dot-nav-trigger { display: block; }` (0,1,0) |
| 3 | 點了沒反應 | `body.is-guide .dot-nav { display: none; }` (0,2,1) 蓋掉 `.dot-nav.is-open { display: flex; }` (0,2,0)，is-open toggle 完全無效 |
| 4 | 段落間距過大 | `.docs-section` padding 64px + `.docs-dek` margin-bottom 56px，手機版缺乏 override |

**解法**

```css
/* docs.css — 全域 display:none 必須在 @media display:block 之前 */
.docs-dek--mobile { display: none; }      /* ← 移到 @media 之前 */
@media (max-width: 768px) {
  .docs-dek--mobile { display: block; }   /* 後來者勝 ✓ */
}

/* guide 頁手機版：用更高 specificity 的 @media 解除桌面隱藏 */
@media (max-width: 960px) {
  body.is-guide .dot-nav-trigger { display: block; }
  body.is-guide .dot-nav.is-open { display: flex; }  /* (0,3,1) > (0,2,1) ✓ */
}

/* 手機版間距縮減 */
@media (max-width: 768px) {
  .docs-section { padding: 32px 0 12px; }
  .docs-main .docs-dek { margin-bottom: 20px; }
}
```

**規則**：「全域隱藏 + media query 顯示」時，全域隱藏必須寫在 media query **之前**，讓 media query 成為後來者勝出。若全域 specificity 更高，需在 media query 裡用相同或更高 specificity 的選擇器覆蓋。

---

## 8. 手機版 shrine 序章推不下視口（2026-05）

**症狀**
首頁 shrine 區塊在 iPhone 16 上，「0 · 序章」門仍出現在第一屏視口內，達不到設計意圖（序章應沉到捲軸下）。前後三輪才解決。

**根本原因（三輪疊加）**

| 輪次 | 改動 | 為何不夠 |
|---|---|---|
| 1 | `.shrine { min-height: 100svh }` | shrine 內容已 ~927px > 100svh (~660px)，下限不再起作用 |
| 2 | `grid-template-rows: auto 1fr auto auto` | 內容超過視口時沒有「剩餘空間」可分配給 1fr |
| 3 | `.shrine-vessel { min-height: 50svh }` ✓ | 強制 vessel row 拿到視口固定佔比 |

iPhone 16 視口 100svh ≈ 660px；shrine 內容（題辭 219 + 瓶子 304 + 序章 140 + 四門 212 + padding 52 ≈ 927px）已超過視口 270px。`min-height` 是下限不是上限，`1fr` 分配剩餘空間——兩個前提都失效，必須再加一層強制下限。

**最終解法**

```css
@media (max-width: 768px) {
  .shrine {
    grid-template-rows: auto 1fr auto auto;
    min-height: 100svh;          /* 視口大時撐底 */
  }
  .shrine-vessel {
    min-height: 50svh;            /* 視口小時強制下限 */
  }
}
```

三層各司其職、互不衝突：100svh 處理大視口（iPad mini 直立 1024px）、1fr 處理有剩餘空間時的分配、50svh 處理視口被內容超過時的下限。前兩輪不是錯解，是 fallback 層——刪了反而會在大視口失效。

**規則**
- `min-height: 100svh` + `1fr` 的組合假設「內容 ≤ 視口」。若內容會超過視口，1fr 拿不到空間，必須再給強制 `Xsvh` 下限。
- 手機 row 高度的真實 fallback 是「佔視口比例」（`svh`），不是「佔剩餘比例」（`1fr`）。
- 修 RWD 時先估算「內容總高 vs 視口高」的差距，再決定要靠 min-height、1fr、還是強制 svh。

---

## 9. echo 三語版 brand link `../index.html` 跳繁中首頁（2026-05-17）

**症狀**
在 `en/echo.html` / `ja/echo.html` / `cn/echo.html` 點左上 VAS logo brand link，
不是回到該語言首頁（如 `/en/`），而是跳到繁中根首頁 `/`。

**根本原因**
建立三個 lang 靜態檔時，brand link `href` 寫成 `../index.html` 而不是 `index.html`。
`../` 把路徑往上跳一層、出了 lang 目錄、落到 root。

`faq.html` 三語版本巧合避開這個 bug——它用 `<div>` 包 brand + 內含 `<a href="index.html">`（無 `../`）。

**最終解法**
```html
<!-- lang 靜態檔 brand link：同目錄相對路徑 -->
<a class="site-nav-brand" href="index.html" aria-label="Back to home">
<!-- 不是 -->
<a class="site-nav-brand" href="../index.html" aria-label="Back to home">
```

**規則**
- lang 靜態檔的內部連結（同目錄內）用 `page.html`，不用 `../`。
- `../` 只在跨目錄連結時用（語言切換 / 共享 css、img、js）。
- lang 靜態檔建立後跑一輪「點 brand 確認回到該語言首頁」的人類測試。

---

## 10. Agent 過度套用「図」黑名單 → 図書館 被改成 書庫（2026-05-17）

**症狀**
`ja/context.html` 翻譯後 §04 五層語言 L3 對照物例句出現「書庫」取代原文的「圖書館」。
語意通但不自然——日文 library 的標準字本來就是「図書館」。

**根本原因**
Memory prep 寫的規則是「図 in tech 上下文要改 画像」（適用於 UI / 截圖 figure caption）。
但 agent 把這條當「図」blanket 黑名單，連日常字「図書館」也被換成 alternative「書庫」。

**最終解法**
```diff
- 「書庫のようにしたい、コンビニではなく」
+ 「図書館のようにしたい、コンビニではなく」
```

Memory `translation-prep-self-context-faq.md` 規則描述同步收緊：

> 図 / 窓 — **ONLY in tech / UI context 才換**。日常字詞（図書館、窓辺、設計図）**保持標準 kanji**。

**規則**
- 詞彙黑名單必須附 scope qualifier（什麼上下文才適用）。
- 規則 prep 給 agent 時必須 highlight scope，不能只寫「X→Y」。
- 翻譯 polish ja 時優先用標準字（圖書館、窓辺、設計図 等日常詞用 ja 既有正字）。

---

## 11. JSON-LD inLanguage array 太寬 → AEO per-locale 信任不足（2026-05-17）

**症狀**
全站長章節 html（collab/harness/insight/milestone/guide 等）JSON-LD 寫：

```json
"inLanguage": ["zh-Hant", "en", "ja", "zh-Hans"]
```

——一份 JSON-LD 涵蓋全 4 locale。Google 對 array `inLanguage` 處理有限，
偏好「一個 URL 一份 JSON-LD、單一 locale」，AEO 信任分被攤薄。

**根本原因**
最初設計時為了避免 4 個 lang 變體重複 JSON-LD，採 array 共享 headline / description。
但 Google AEO 機制偏好 per-locale 結構化資料，array 寫法是過時 pattern。

**最終解法**
拆成 per-locale：每個 lang 變體 JSON-LD 改：
- `inLanguage` array → single string（`"en"` / `"ja"` / `"zh-Hans"` / `"zh-Hant"`）
- `headline` / `description` 翻成該 locale 的自然文字
- `url` 對應 lang 變體 clean URL（如 `/en/harness` 不是 `/harness.html`）

**規則**
- JSON-LD 結構化資料一律 per-locale，每個 lang 變體獨立 block。
- 新增 lang 變體時，JSON-LD 翻譯是必做項，不要跳。
- 詳細策略見 `GLOSSARY.md` § 9 URL/SEO conventions。

---

## 12. CN「馬照跑舞照跳」對 Mainland 讀者文化失準（2026-05-17）

**症狀**
`self.html` chapter dek 第三段用「馬照跑舞照跳」描述「不受 Claude 變笨議論干擾、
仍能正常協作的人」。但這是 HK 1984 政治俚語，Mainland 讀者沒有對應文化共鳴。

**根本原因**
CN 翻譯 agent 直接 simplified 化「马照跑舞照跳」放進 `cn/self.html`。
字能讀，但 idiom 對 Mainland 讀者是空白——失去原本「在喧嘩中仍持續」的力道。

**最終解法**
換 Mainland-native 等義表述：「依然如常」。保留「正常持續」核心語意，
去掉地區性 idiom baggage。

**規則**
- HK / Cantonese / Taiwan-specific 俚語譯成 cn-Mainland 時必須換 Mainland-native 表述。
- 區分「字 simplified 化」（mechanical）vs「idiom localization」（需 cultural judgment）。
- 詳細規則見 `GLOSSARY.md` § 5 CN language strategy。

---

## 13. 執行期 i18n 死碼陷阱：長文 × 重 SEO 的站不要回頭用 runtime 換字（2026-06-14）

**症狀**
本站早期鋪了一層 runtime i18n：`data-lang-key` 屬性 + `i18n/<lang>.js` 語言包 +
`applyLang()` 逐元素 `innerHTML` 換字。但某個時期後新頁全部改成 static-per-locale
（zh 根目錄 / `en/` `ja/` `cn/` 各自獨立硬寫）。兩套並存，舊那套**從未被實際呼叫**
（除了 `404.html` 一行殘留 + archive 紀念頁）。結果：
- agent／未來宰相讀到 `i18n/en.js` 的 `ch3No='Chapter III'`，卻發現頁面顯示硬寫的別的字，
  困惑「到底哪個是真的」——死碼看起來像活的，誤導判斷。
- 真實潛藏 bug：`guide.html` 工具彈窗走 runtime 查 `VASI18n`，但 `applyLang` 從沒被呼叫→
  英／日／簡三版彈窗全部 fallback 顯示**繁中**，沒人發現（譯文鎖在沒人載入的語言包裡）。

**根本原因**
runtime i18n 適合 app-like、輕 SEO、單一 URL 的場景。長文 × 重 SEO × per-locale clean URL
的站，每個語系本來就該是獨立可被爬蟲索引的靜態檔。硬套 runtime 換字 → 既不利 SEO，
又留下一層「看似活、實則死」的碼，是純負債。

**最終解法**
- guide 彈窗譯文從語言包搬進各 `en/ja/cn/guide.html` 的 `popupData`（順手修好繁中 bug）。
- 拆掉整層死碼：29 活頁的 `applyLang`、`404` 呼叫、四語 value packs、`core.js` 的
  `loadLang/updateDropdown/initDropdown`、3660 個 `data-lang-key` 屬性。
- `core.js` 只留活的 `initNavDropdown`（手機版 nav）。archive 紀念頁完全不動（其相對路徑
  `i18n/core.js` 歸檔時已斷，本就 frozen）。
- rendering 不變是硬不變量：死碼不 render，搬譯文只是讓本來該顯示的譯文真的顯示。

**規則**
- 新站／新區塊一律 static-per-locale，不要鋪 runtime i18n。語系切換靠頁面導覽，不靠執行期換字。
- 砍死碼前先確認「真的死」：grep 出所有呼叫點，區分 live consumer vs dead definition；
  archive／紀念頁的相對路徑依賴要單獨確認（常已斷），確認後不動它。
- 拆陷阱優於寫規則記得繞過陷阱——「讓記不住也沒關係的系統」：能刪就刪，不要靠 CLAUDE.md 提醒自己無視死碼。

---

## 14. 四語手冊翻譯 pipeline：cn 用 opencc `tw2sp` 半自動，但最後一成靠渲染的眼睛（2026-07-13）

**場景**
guide 拆成 static-per-locale 七頁後，要一次生 en / ja / cn 各七頁（共 21 頁）。
純手工翻不但慢，還是 Nova 最怕的幻覺高風險區（工具名、隱私欄位）。這筆記下把它
decompose 成「機械層零幻覺 × 散文層可驗」的整套做法，之後加頁／新語系直接沿用。

**兩層方法（每頁都這樣拆）**
- **機械層（宰相自跑確定性腳本，零幻覺）**：chrome／路徑／meta／canonical／hreflang／
  JSON-LD／lang-switcher。腳本吃 slug 就生新頁，每個 `.replace` 配 `assert count==n`——
  改錯數量立刻爆，不會靜默漏改。檔：`en_chrome.py` / `ja_chrome.py` / `cn_build.py`（scratchpad，
  值得的話搬進 repo tools/）。
- **散文層**：en/ja 語氣敏感 → 宰相自譯或派 Agent 打草稿（鎖死術語表當緊箍咒），宰相審稿。
  cn → 見下方 tw2sp。

**cn 的關鍵：opencc `tw2sp` 做九成，剩一成是陷阱**
- `pip install opencc-python-reimplemented`，用 **`tw2sp`**（Taiwan→Simplified with **phrases**）——
  它會連**大陸詞彙**一起轉：螢幕→屏幕、檔案→文件、程式→程序、網路→网络、軟體→软件、
  影片→视频、記憶體→内存、伺服器→服务器。`t2s` 只轉字不轉詞，**不要用 t2s**。
- **但 tw2sp 有兩類洞，必須靠「渲染後親眼掃」才抓得到**（Nova 掃簡中語感最準，務必請她過目）：
  1. **漏轉的台味詞**（tw2sp 沒收錄的 vocab pair）——這是本輪 render review 才逼出來的表：

     | tw2sp 留下（台味） | 大陸 | | tw2sp 留下 | 大陸 |
     |---|---|---|---|---|
     | 自訂→自订 | **自定义** | | 拖曳 | **拖动** |
     | 漸層→渐层 | **渐变** | | 浮水印 | **水印** |
     | 鏡射→镜射 | **镜像** | | 尺標→尺标 | **标尺** |
     | 全域 | **全局** | | 復原→复原 | **撤销** |
     | 實色→实色 | **纯色** | | 量測→量测 | **测量** |

  2. **over-correction**（tw2sp 自作聰明改錯）——`文字→文本`（OCR 語境要**改回 文字识别**，對齊 app）、
     另 `辨识→识别`、`屏蔽→遮蔽`、`侦测→检测`、`在地→本地`、`工具列→工具栏`、`缺省→默认`、
     `身分证→身份证`。
  - 這些疊成一張 replace 表，tw2sp 之後跑一遍即可（見 `cn_overlay.py` 的 vocab list）。

**陷阱：tw2sp 會誤轉頁面內嵌的「非簡中內容」**
- 頁內互動 demo 的 JS `I18N` 字典含**日文** value（全画面／開く／遅延キャプチャ…），
  tw2sp 會把日文漢字也轉（開→开、變換→变换）→ 破壞日文 tooltip。
- lang-switcher 的 **`日本語`** 標籤也會被轉成「日本语」。
- **解法**：tw2sp 前先把這些用 ASCII placeholder 保護起來，轉完再還原（`cn_build.py` 的 `@@P..@@` / `@@JPLBL@@`）。

**隱私欄位：每語頁用「該市場實際偵測的欄位」，不是繁中的臺灣格式**
- 產品的 `SWIFT_PRIVACY_SCAN` 對四語各有特化（Code宰相可從 code 撈正本）。翻頁時：
  ja→マイナンバー・郵便番号・氏名・パスワード…；cn→身份证18位・手机号・统一社会信用代码・
  密码・联系人…；示範卡資料也換成該地樣例（ja 山田太郎／cn 张伟＋110105 朝阳区身份证，
  格式要上網核對）。**別把臺灣的身分證字號／統一編號直接翻到別語頁**（不準也不真）。

**驗證法（因語言而異）**
- en：目標是拉丁字母 → 掃「殘留漢字＝漏翻」，乾淨可驗。
- ja/cn：目標本身就是 CJK → 掃「繁體專用字／台味字殘留」跨所有互動狀態（editor 要點遍每個工具
  才顯示隱藏面板）。**注意子串誤報**（如簡中「分量测量」含「量测」子串但語意正確）。
- 每頁一定要**渲染截圖**：SVG 標籤會不會被較長的譯文擠爆、poster/inline img 路徑深一層有沒有漏改，
  只有眼睛看得出來。

**規則**
- cn 一律 `tw2sp` + 疊上方那張 vocab 表 + Nova 語感過目，三者缺一不可。**tw2sp 只到九成，別信它到底。**
- 工具名一律查 app i18n（`src/i18n/*.js`，CI 有 key parity），lookup 不重譯。
- 詞彙策略總則見 `GLOSSARY.md` § 5（cn）／§ 6（ja）／§ 7（en）；本筆補的是「工具與流程」。

---

## ~~BACKLOG~~ RESOLVED · 系統性結構化資料殘留（collab / harness / us）— 2026-08-19 掃出，2026-08-20 全清

> es 鏡廊翻譯途中，Explore 摸 en 源頭時掀出的跨語系 bug。collab/harness/us 這組當初大概同源複製，錯誤一起繁殖。en 層在 es 3a 前已修（commit 8577bda）；**ja/cn 層 2026-08-20 全數修畢**（下方 checkbox 皆 ✅）。ja/us 的 headline/description 是鏡射頁面既有的日文 meta（非新編日文，故安全無需 Nova 過目）。
> **掃描時新發現（交全站格式稽核處理）**：`cn/us.html` 的 og:description 與 JSON-LD description 有**繁體字滲漏**（當／學會／關係，應为 当／学会／关系）——tw2sp 漏網，屬字集洩漏類，見下方全站稽核。

**Bug A · `og:locale` 誤植 zh_TW（非 root 頁）**
- root 的 `collab.html` / `harness.html` 是 zh_TW＝**正確，不動**。
- 錯的是非 root 頁：
  - [x] `ja/collab.html`、`ja/harness.html` → `ja_JP`
  - [x] `cn/collab.html`、`cn/harness.html` → `zh_CN`
  - （`en/collab.html`、`en/harness.html` → `en_US`：**en 層，es 3b 前已修**）
- 純機械修，安全。

**Bug B · `us.html` JSON-LD 跨語系錯譯**
- root `us.html`：headline 繁中、inLanguage zh-Hant＝**正確，不動**。
- [x] `ja/us.html`：headline 目前是**繁體中文**「容器一直是我們」（日文頁掛中文標題，日本讀者會看到中文）→ 需**日文** headline/description；inLanguage `zh-Hant`→`ja`。⚠ **日文 headline 要碰日文內容，動前先給 Nova／日文語感過目。**
- [x] `cn/us.html`：headline 已简中（OK），但 inLanguage `zh-Hant`→`zh-Hans`。
- （`en/us.html`：headline 繁中→英文、inLanguage→en、url 去 .html、**切換器壞掉**（按鈕標籤「中」→EN、zh-Hant href 指錯、en/active 狀態）：**en 層，es 3b 前已修**）

**收尾驗證**：修完各頁 grep `og:locale`／`inLanguage` 確認每頁對應自己的語系；us 三頁的 headline 語言要各歸其語。

---

## 修 cn 繁體字滲漏：用 tw2s（非 tw2sp），並小心 麼→幺（2026-08-20）

**背景**：全站稽核掃出 6 個 cn 頁有繁體字滲漏（tw2sp 建置時漏網 / 事後編輯帶入）——us、collab 嚴重（us 連 og/twitter/JSON-LD metadata 都有），insight/harness 中等、about/treatise 輕微。

**方法（只補滲漏、不重建）**：
- 用 **OpenCC `tw2s`**（**不是** `tw2sp`）——`tw2s` 只轉字形、片語感知（`著/着` 助詞辨析正確、`顯著→显著` 保留）；`tw2sp` 會多做台→陸**詞彙**轉換（`文件→文档`、`文字→文本`），修滲漏時屬過度、會改到刻意保留的詞。
- **只轉可見文字**：保護 `<script>`（內嵌日文 i18n dict，km.md 舊坑）/`<style>`/`<!--註解-->`/`日本語` 標籤，用 placeholder 挖空→轉→還原。整檔硬跑會誤轉日文與繁中註解。

**⚠ 陷阱：`麼→幺`**。tw2s 把 `什麼/怎麼/為什麼` 轉成 `什幺/怎幺`（`幺` 是別的字），正解是 `什么/怎么`（`么`）。轉完必須 **post-fix `幺→么`**（本站無合法 `幺`，可全域替換）。這正是「tw2sp 只到九成，別信它到底」的實例。

**驗證**：用 `OpenCC('t2s').convert(ch)!=ch` 逐字判斷是否仍為繁體（權威，勝過手列繁體字表——手列會漏 `寫` 之類）；再核上下文敏感字（`覆`盖 vs 答`覆`→复、`鍊`金术/精`鍊`→炼 vs 链）。

---

## 15. scaffold 的 f-string 陷阱：`{slug}` 寫成字面值，兩波都靠 site_audit 才抓到（2026-08-20）

**場景**
es scaffold 的 `head_common()` 改 JSON-LD `"url"`：**舊字串**是 f-string（`f'...en/{slug}"'`，配對正確），
**新字串**卻漏了 `f` 前綴（`'...es/{slug}"'`）——`{slug}` 原封不動寫進頁面，變成字面
`https://yoursvas.app/es/{slug}`。assert count==1 照過（因為舊字串比對正常），**靜默漏網**。

**兩波都犯**：Wave 7a（insight/collab/context）犯一次、Wave 7b（self/harness/us）沿用同一個
buggy 函式又犯一次。抄自己上一版腳本 = 抄自己上一版 bug。

**為什麼 assert 攔不到**：assert 只驗「舊字串出現幾次」，不驗「新字串長得對不對」。
f-string 漏前綴屬於「新字串本身錯」，count 檢查天生盲。

**耐用防線（已生效兩次）**：**scaffold 跑完必跑 `site_audit.py`**——它拿 JSON-LD `url` 對 `canonical`
比對，`{slug}` != `es/self` 立刻爆。deterministic auditor 補 assert 的盲區，兩層才閉環。
新增 scaffold 波次時，這一步不可省。

---

## 16. 矩陣稽核器：以「頁×語系」網格抓共用元件／連結／術語的三軸漂移（2026-08-20）

**病根**
站是 static-per-locale，頁首／頁尾／術語全是**複製**出來的，沒有單一真相源。一份東西
散在一百多檔裡，會沿三軸靜默漂開：沿**頁**（同語系不同頁的頁尾不一）、沿**語系**
（動一個語系，其它四個藏著同款問題）、沿**時間**（echo 的 self 在 3a 譯、self 頁在 3b 譯，
中間 Sí-mismo 才定調，兩邊對不上＝「El yo」那個 bug）。連結是這複製結構最脆的接縫。

**工具**：`tools/matrix_audit.py`（已進 CI `sitemap.yml`，PR 階段強制跑）。
以網格為單位，三族檢查——所以「動一個要順便看其它語系」是天生內建的：
- **A chrome**：頁尾信條 + 頁首 nav 標籤，同語系跨頁該一致，漂了報。
- **B links**：es 連 /en/X 但 X 有 es 手足 → 報（instrument 那類）。
- **C codename**：章名在 echo TOC vs passage-nav **自我一致**策略——不硬編正確值，
  只要各槽位彼此不合就報（El yo vs Sí-mismo 自動爆）。
- **D metadata**：html lang／og:locale／JSON-LD inLanguage 必須符合網格語系（網格位置＝
  ground truth，最準）；並抓 URL 裡的 `{var}` 未解析洩漏（f-string {slug} 那類）。
- **E sitemap**：subprocess 跑 `gen_sitemap.py --check`，頁面異動沒同步重生就報。
- **F llms.txt**：`/llms.txt` 的策展連結必須都指向存在的頁——頁面改名／刪除就報，
  不讓給 AI 的索引悄悄爛掉。

**首跑就抓到兩條眼睛沒抓到的漏網**：en 的 collab 章 echo 寫「Collaboration」但 nav 寫
「Collab」；ja 頁首「About」三種寫法（概要 15／について 3／沒譯的 About 3）。

**用法**：任何動到多語系／共用元件的變更後，`python3 tools/matrix_audit.py`（exit 1＝有漂移，
訊息直指語系×頁×族）。人腦記不住「還有哪裡寫著舊詞」，grep 記得住。
**未治的根**：真正根治是給站一個 build 步驟把 chrome／術語抽成單一來源注入——
那是動部署管線的大工程，static-per-locale 當初為部署單純而選，暫不動；稽核器是止血。

---

*遇到坑才記，記了就不用再踩第二次。*

## #17 · 2026-08-21 · Usage limit 撞牆時多 agent 並行工程的斷頭復原

**現象**:六 agent 並行修多章時撞 session usage limit,三個 agent 死在半路(editor 只完成 zh/cn、arrange 剛起步、shortcuts 已改完但未自檢),工作區留下半成品。使用者按 Try again 後,被中斷輪的另一延續已把三章(pixel/toolbar/OCR)做完、commit 並 push——復原時先 `git status` + `git log` 盤點,發現「以為沒做的已經做完」與「以為做完的只做一半」並存。

**復原模式(有效)**:
1. 先盤點,不先動手:`git status --short` + `git log --oneline` 對照任務清單,分出「已 commit / 半成品 / 未動」三類。
2. 接力 agent 用「verify-and-complete」而非重做:明示「前任已改部分在工作區,驗證勿還原,補缺即可」,並附完整 checklist 讓其逐項核對。
3. 已完成且不會再被動到的章,立即分章 commit(縮小未提交面、stop-hook 也安靜)。
4. 死前「已改完未自檢」的 agent 產出要當未驗貨:shortcuts 全數正確,但必須驗過才知道。

**教訓**:並行 fan-out 前,任務切分以「檔案不重疊+單章可獨立 commit」為單位,斷頭時每章都是乾淨的復原邊界。Agent 指示「不碰 git」要含唯讀指令(有 agent 自首跑了 git status)。

## #18 · 2026-09-01 · 會過期的句子，與 matrix_audit G 族

**病徵**:一句話寫下時是真的,產品往前走一步就變成假的,而且沒有任何檢查抓得到——字串完好、連結沒死、語系正確,只是世界變了。八月出現四次:「未來還會開發拼豆用途」(做出來了)、「二十分之一」(體積動了兩次)、章名「像素動畫」(多了第二種文件)、「這條線停在 v3.66」(沒停)。

**寫作面的解**:CLAUDE-process § UI & Editorial Standards 第 5 條——句子只能待在兩種安全模式,無時態(不到一成/兩種文件)或有日期的紀錄(arc-line、過審日)。歷史紀錄一旦寫下永不改寫,這正是它零維護成本的原因。

**工具面的解**:matrix_audit 增 G 族「活值一致性」。
- 稽核前先剝掉歷史區塊(arc-line／arc-divider／密度圖說明／HTML 註解),歷史本來就該持有舊值。
- G1:同一事實寫在多個槽位(下載檔名、Tauri 目前版本、Electron 目前版本),各槽位必須同值。已 positive-control 驗證——注入 index.html 舊版下載連結會被抓出並指名檔案,正是 8 月真實發生過的漏。
- G2:同頁五語系結構平行,體積數字序列必須同序同值;首跑即抓到 guide/toolbar 繁中簡中寫「20mb」而其餘三語寫「20 MB」。
- `--values` 印出活值清單。**清單必須由工具生成,不可手寫**——手寫清單自己就是下一個會過期的東西。

**邊界(重要)**:G 族只能抓「彼此矛盾」,抓不到「全站一致地錯」。五語都寫 303 MB 而真實是 307.3 MB 時它是綠的。那一半只能靠出貨時拿 `--values` 對照現實。別把綠燈當成數字正確。

## #19 · 2026-09-01 · 稽核器的天花板：「合理但指錯東西」的句子

**兩個實例，同一天出現在同一行字上（changelog v3.66 / v3.31）：**

1. **編輯器的量測工具被標成螢幕標尺的名字**——簡中寫「编辑器标尺」（應為尺标）、
   en 寫 editor Ruler（應為 Measure）、es 寫 Regla del editor（應為 Medir）。
   `标尺/Ruler/Regla` 是工具列的螢幕標尺、`尺标/Measure/Medir` 是編輯器量測工具，
   兩個不同工具在繁中與日文剛好同名（尺標／定規），另外三語不同名。km #18 的
   同名不同物陷阱的第二次現身，這次是反方向：不是我誤統一，是原文誤標。
2. **`框選 + Shift 加選複數標註` 的 `+` 被讀成按鍵組合**——因為 `+` 右邊緊接
   `Shift`，視覺上就是 `+Shift`。實際上兩者是並列機制：本站 guide/arrange 寫
   「框選**或** Shift 加選」，而真要講按鍵組合時 guide/editor 寫「Shift＋點選」
   （全形＋、不留空格）。

**共通點——這才是要記的**：兩句都通過所有機械檢查。字串完好、語法正確、語系正確、
連結沒死。matrix_audit 抓得到「同一件事被寫成兩種」（A/C/G 族），抓不到
**「這件事被寫成了另一件事」**——後者需要理解語意，硬做成第八族只會誤報多於真報。
這是稽核器的天花板，不是它的缺陷。

**實際跨過它的方式：多個宰相從不同位置看同一行字。**
Electron 宰相有 SDD 與行為矩陣、網站宰相有頁面與 app 用詞表、Nova 有產品現實。
這次 v3.31 是我判斷錯、Electron 宰相判斷對；他引的兩份來源在 Electron repo、
本 repo 讀不到，於是改以本站頁面獨立佐證同一結論——**轉述的證據要自己驗，
驗不到就換個角度找，不要照單全收**（這條對所有 agent 回報同樣適用）。

**可複用的判準（Electron 宰相提供）**：分隔符 vs 語意符——刪掉那個符號，
兩邊還各自讀得通嗎？通 ⇒ 它在當分隔符 ⇒ 換 `·`；不通（少了一邊那句話就不成立）
⇒ 它在承載語意 ⇒ 留。例：v3.40「XSS 防護 + 畫布尺寸上限」換；
v3.33「Smart Snap · 磁吸 + 均分輔助線」留（兩層結構，`+` 綁住展開的兩半）。
