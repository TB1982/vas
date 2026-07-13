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

*遇到坑才記，記了就不用再踩第二次。*
