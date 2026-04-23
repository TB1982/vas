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

*遇到坑才記，記了就不用再踩第二次。*
