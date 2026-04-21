# VAS Redesign · 設計規範（Design System）

> 給網站宰相的操作手冊。不是原理，是**抄這個**。
> 讀完後應該能獨立套用在四章任何一頁。
> 有疑問時翻 `GLOSSARY.md` 對詞。

**版本**：v1.1 · 2026-04-21 · Nova × Claude
**適用範圍**：VAS 官網首頁 v2（`home2`）、四章（`ch1`–`ch4`）、**操作手冊（`docs`）**
**不適用**：後台、changelog——那些用 repo 既有系統

**兩種模式**：
- **Shrine Mode · 扉頁態**（首頁 + 四章）——氣質為先、留白靠字、氛圍有光暈
- **Docs Mode · 手冊態**（操作手冊）——清晰為先、留白靠版、**不用 halo/room gradient、不用 aurora 氛圍**

兩種模式共享 token（ash / 字型 / void / rule），但動效、間距、元件規則不同。詳見第 9 節「Docs Mode」。

---

## 目錄

1. [核心信條](#核心信條)
2. [Token · 變數](#token--變數)
   - 2.1 [色票 · Ash 陶灰](#21-色票--ash-陶灰)
   - 2.2 [色票 · Aurora 極光](#22-色票--aurora-極光)
   - 2.3 [色票 · Void 曗場](#23-色票--void-曗場)
   - 2.4 [色票 · Rule 分隔線](#24-色票--rule-分隔線)
   - 2.5 [字型三軌](#25-字型三軌)
3. [版式](#版式)
4. [元件](#元件)
5. [動效](#動效)
6. [文案節奏](#文案節奏)
7. [彩蛋 · Trail 光點](#彩蛋--trail-光點)
8. [套用檢查清單](#套用檢查清單)
9. [Docs Mode · 手冊態](#docs-mode--手冊態)

---

## 核心信條

> 三句話。所有設計決定都從這三句推出來，矛盾時以這三句為準。

1. **器物站到底。** 瓶子的光只屬於瓶子，不可滲進背景或他處；aurora 三色只用在與瓶子直接相關的元素。
2. **文字讓讀者停下，不是催他動。** 首屏沒有 CTA 按鈕；下載移到「註腳位」；所有動效慢到第一眼像靜的。
3. **一章滑過一章。** 頁首不變大變小、章末不給大按鈕、過場是「翻頁」不是「選單」——順讀感是第一優先。

---

## Token · 變數

### 2.1 色票 · Ash 陶灰

窯燒陶器的灰階。文字層級從 ash-0（最亮）到 ash-4（最淡）。

| 變數 | 值 | 用在哪 | 不該用在哪 |
|---|---|---|---|
| `--vas-ash-0` | `rgba(240,232,220,0.94)` | 主文、h1/h2 大標、章節名 | 不要用在 hover 以外的次要元素——會搶視覺 |
| `--vas-ash-1` | `rgba(240,232,220,0.78)` | 段落正文、`.gloss`、`.whisper`、footer 正文 | 不要低於這階當正文色——會讀不清 |
| `--vas-ash-2` | `rgba(240,232,220,0.60)` | mono 標籤、nav 連結、圖說 | 不要當章節名或 h2 |
| `--vas-ash-3` | `rgba(240,232,220,0.42)` | 微標籤、章節序號、分隔字符 | 不要當段落正文——太淡 |
| `--vas-ash-4` | `rgba(240,232,220,0.24)` | 版權聲明、極度次要的英文副標 | 不要用在任何可互動元素 |

**範例**：
```html
<h2 style="color: var(--vas-ash-0)">章節名</h2>
<p  style="color: var(--vas-ash-1)">段落正文，可讀度保底。</p>
<div style="color: var(--vas-ash-2); font-family: var(--vas-mono)">SECTION · 01</div>
<span style="color: var(--vas-ash-4)">© 2026</span>
```

**可讀度底線**：ash-1 是正文可用色的最底——任何 body copy 不可低於此階。

---

### 2.2 色票 · Aurora 極光

瓶子的光。**只用在與瓶子直接相關的元素**，不可當裝飾色。

| 變數 | 值 | 用在哪 | 不該用在哪 |
|---|---|---|---|
| `--vas-aurora-violet` | `#c471f5` | 瓶子光暈主色、hover 強調、Trail 光點、em 底線 | ❌ 大面積背景、❌ 文字正文、❌ 邊框整圈 |
| `--vas-aurora-pink` | `#fa71cd` | 瓶子光暈漸層副色、nav mark 漸層 | 極少量使用——除以上兩處外基本不用 |
| `--vas-aurora-blue` | `#4facfe` | 房間氣場（`.shrine::before`）的副色 | 幾乎不用，備用色 |

**可用強度**：
- 實色：只在「光點」（4px 圓點）、em 底線、hover 狀態線
- 半透明（< 0.3 alpha）：瓶子 halo、chronicle-line 中段、房間氣場

**絕對不可**：
- 拿 aurora-violet 當段落文字色
- 用 gradient background 覆蓋超過 30% 面積
- 在非「瓶子」語意的元素上使用（e.g. 章節 header 的底色、Acquire 按鈕的填色）

---

### 2.3 色票 · Void 曗場

深暗底色三階。

| 變數 | 值 | 用在哪 |
|---|---|---|
| `--vas-void` | `#0e0b1a` | body 主背景、mock-frame 內 |
| `--vas-void-up` | `#15121f` | 提亮一階——瀏覽器框殼、章節 header 背景（若要區隔） |
| `--vas-void-up2` | `#1b1825` | 提亮二階——備用，目前未使用 |

**注意**：void 帶一點紫，不是純黑。這是為了讓瓶子的紫光**融進**場景——如果用純黑 `#000`，紫光會有「外星貼圖」的違和感。

---

### 2.4 色票 · Rule 分隔線

| 變數 | 值 | 用在哪 |
|---|---|---|
| `--vas-rule` | `rgba(240,232,220,0.08)` | 一般分隔線（section 之間、chapter-row 之間） |
| `--vas-rule-strong` | `rgba(240,232,220,0.18)` | 強調分隔線（mock-frame 邊框、章節 header 底邊） |

---

### 2.5 字型三軌

**不用 sans-serif**。全站只用 serif + mono 兩軌。

| 變數 | 值 | 用在哪 | 不該用在哪 |
|---|---|---|---|
| `--vas-serif` | `'Shippori Mincho', 'Fraunces', 'Noto Serif TC', serif` | 所有正文、標題、章節名 | 不要用在 labels、章節序號、metadata |
| `--vas-serif-en` | `'Fraunces', 'Shippori Mincho', serif` | 純英文字段落（若有獨立英文排版） | 混排中英時用 `--vas-serif`（Shippori 先） |
| `--vas-mono` | `'JetBrains Mono', 'SF Mono', monospace` | 章節序號、labels、metadata、版次、uppercase 小字 | 不要用在段落正文（會硬） |

**字重規則**：
- serif：300（h1 主標極輕）、400（正文）、500（章節名 / em 強調）、600（double em 強強調）
- mono：400（一般 label）、500（hover 或強調 label）
- **不要用 700 以上**——B 案整體輕，重字重會破氣

---

## 版式

### 3.1 網格單位

**8px 為基本單位**。所有間距（padding、margin、gap）都應該是 8 的倍數：
`8 · 16 · 24 · 32 · 48 · 64 · 80 · 100 · 120`

> 例外：`14px` 用在 `.acquire-body .line` 的 padding（小節奏），`28px` 用在 `.shrine-gate` 的 padding。這些是有意的「逃出網格」——讓局部節奏不被 8px 鎖死。

### 3.2 斷點

| 斷點 | 用在 | 觸發什麼 |
|---|---|---|
| `> 768px` | desktop 預設 | 所有多欄 grid 生效 |
| `≤ 768px` | mobile | 所有 grid 塌成單欄、padding 從 48px 降到 24px |
| `≤ 900px` | tablet（僅 `.note-row`） | 專給備註雙欄的中間態 |

**不要加更多斷點**。三組夠了，多了維護成本暴增。

### 3.3 最大寬度

| 場景 | max-width | 理由 |
|---|---|---|
| 正文段落（unfold、envoy） | `32ch` ~ `44ch` | 閱讀最舒服的字數 |
| 敘事區塊（chronicle、acquire、unfold 整體） | `1040px` | 不做全寬，留兩側呼吸 |
| 章節內容槽 | `960px` | 比敘事區塊再收一點，更像書的版心 |
| 首屏 shrine | 全寬 | **唯一例外**——器物要滿版氣場 |

### 3.4 Padding 節奏

**section 之間的垂直節奏**（已校準）：

| 段落 | padding-top | padding-bottom |
|---|---|---|
| `.shrine`（首屏） | 80px | 48px |
| `.unfold` | 100px | 80px |
| `.acquire` | 80px | 80px |
| `.chronicle` | 72px | 56px |
| `.site-foot` | 56px | 40px |

> 章節頁會多一組 `.chapter-header` / `.toc` / `.section` / `.passage`——見元件章節。

---

## 元件

每個元件都有四項：**定義 · 結構 · 用在哪 · 不該用在哪**。

### 4.1 Gate · 門（僅首屏）

**定義**：首屏四道門。首屏唯一入口。

**結構**：
```html
<a class="shrine-gate [hidden-door]" href="#">
  <div class="num">I · 設計</div>
  <div class="name">不完美的工具</div>
</a>
```

- 寬度：`repeat(4, 1fr)`（mobile：`1fr 1fr`）
- 右邊框 `--vas-rule` 做分隔
- hover：頂部一條紫線從左展開到右（600ms）、`.num` 轉紫、`.name` 右移 2px

**用在哪**：只有 `.shrine-gates` 容器內。

**不該用在哪**：章節頁、footer、nav——那些地方的連結用 `.site-nav-links a` 樣式。

---

### 4.2 Line · 行（僅 Acquire）

**定義**：下載三行——Tauri / Electron / Guide。

**結構**：
```html
<a class="line" href="#">
  <div class="what">Tauri</div>
  <div class="name">VAS 正式版 <em>macOS 12+ · App Store</em></div>
  <div class="go">→ 前往</div>
</a>
```

- 三欄 flex：`what`（100px mono 標籤）· `name`（flex: 1 serif 主文）· `go`（mono 動作）
- 下邊框 `--vas-rule`；最後一行無邊框
- hover：`.go` 轉紫

**用在哪**：只在 Acquire section。

**不該用在哪**：章節內、footer——章節內的下載（如果需要）用章節 section 自己的樣式。

---

### 4.3 Chronicle-line · 版次線

**定義**：兩端淡、中間紫的漸層橫線。

**結構**：
```html
<div class="chronicle-line"></div>
```
```css
.chronicle-line {
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    var(--vas-ash-2) 30%,
    var(--vas-aurora-violet) 50%,
    var(--vas-ash-2) 70%,
    transparent 100%);
}
```

**用在哪**：首頁版次印記區、**章末過場**（下一章名字出現之前）。

**不該用在哪**：普通的 section 分隔——那用 `border-top: 1px solid var(--vas-rule)`。
Chronicle-line 是「儀式線」，用多了就不儀式。全站出現**不超過三次**。

---

### 4.4 Halo · 暈光

**定義**：瓶子背後的紫色 radial-gradient + blur。

**結構**：
```html
<div class="halo"></div>
<img src="..." />
```
```css
.halo {
  width: 70%; height: 70%; top: 15%; left: 15%;
  background: radial-gradient(circle,
    rgba(196,113,245,0.28) 0%,
    rgba(250,113,205,0.15) 40%,
    transparent 70%);
  filter: blur(40px);
  animation: shrine-halo 4s ease-in-out infinite;
}
```

**用在哪**：**只有首屏瓶子**。

**不該用在哪**：任何其他圖片、元件、卡片。這是瓶子的簽名動作，分給別人就不是瓶子了。

---

### 4.5 TOC · 章目錄（新）

**定義**：章頂那張「第一節 … 第二節 …」的輕量列表。像書的目錄頁，不像網頁的黏邊 TOC。

**結構**：
```html
<nav class="toc">
  <div class="toc-label">章目錄</div>
  <ol class="toc-list">
    <li><a href="#sec-01"><span class="no">01</span><span class="name">底色</span></a></li>
    <li><a href="#sec-02"><span class="no">02</span><span class="name">字重</span></a></li>
    ...
  </ol>
</nav>
```

- `.toc-label`：mono 10px、ash-3、uppercase
- `.toc-list`：serif 17px、ash-0、無 list-style、每項 padding 14px
- `.no`：mono 11px、ash-2、右邊一個中圓點分隔
- hover：整列微亮（ash-0）、`.no` 轉紫

**用在哪**：每章章頂，緊接在章節 header 之後。

**不該用在哪**：首頁（首頁有四道門，不需要目錄）、單節短章（如果某章只有一節，不需要 TOC）。

---

### 4.6 Section · 小節（新）

**定義**：章之內的段落單位。一個 section 一個小節。

**結構**：
```html
<section class="section" id="sec-01">
  <div class="section-head">
    <div class="section-no">01</div>
    <h3 class="section-name">底色</h3>
    <div class="section-kicker">純粹溫黑，不帶紫調</div>
  </div>
  <div class="section-body">
    <p>內容正文……</p>
  </div>
</section>
```

- `.section`：上下 padding 80px，border-top `--vas-rule`
- `.section-head`：三欄 grid（80px / 1fr / auto），align-items baseline
- `.section-no`：mono 11px、ash-3
- `.section-name`：serif 32px、weight 500、ash-0
- `.section-kicker`：serif 15px、ash-1、italic off
- `.section-body`：max-width 44ch、serif 17px、line-height 1.95

**用在哪**：章節內所有小節。

**不該用在哪**：首頁（首頁用 `.shrine` / `.unfold` 等具名 section）。

---

### 4.7 Passage · 過場（新）

**定義**：章末收尾——安靜地把讀者送到下一章。**不是按鈕**。

**結構**：
```html
<section class="passage">
  <div class="passage-colophon">
    章 I · 設計<br>
    <span class="faint">Chapter I · Design · End</span>
  </div>
  <div class="chronicle-line"></div>
  <a class="passage-next" href="ch2.html">
    <div class="num">II · 協作</div>
    <div class="name">六個故事</div>
    <div class="arrow">↓</div>
  </a>
</section>
```

- 上下 padding 120px 48px
- `.passage-colophon`：mono 11px、ash-2、靠左、標出當前章已結束
- `.chronicle-line`：中段紫線
- `.passage-next`：三欄 grid（180px / 1fr / auto），hover 整塊微亮
  - `.num`：mono 11px、ash-3（hover 轉紫）
  - `.name`：serif 22px、weight 500、ash-0
  - `.arrow`：serif 24px、ash-2、垂直方向（不是右）

**用在哪**：每章的最後。

**不該用在哪**：章內、首頁——首頁往章節的路徑是「四道門」，不需要過場。
第四章（里程碑）的過場可以改成「回首頁」，或什麼都不放——那是書的結尾。

---

## 動效

全站只有五個 keyframes。加新動效之前先確認現有的不能覆蓋。

| 名稱 | 週期 | 強度 | 用在 |
|---|---|---|---|
| `vas-breathe` | 6s | opacity 0.75→1, scale 1→1.15 | `.site-nav-brand .mark` |
| `shrine-halo` | 4s | opacity 0.8→1, scale 1→1.08 | 瓶子 halo |
| `shrine-room` | 10s | opacity 0.9→1, scale 1→1.04 | 首屏紫漸層氣場 |
| `gate-line`（inline transition） | 600ms | width 0→100% | `.shrine-gate:hover::before` |
| `em-underline`（靜態漸層） | — | — | `.unfold-body em` 的文字底色 |

**規則**：
- 不要加 scroll-triggered parallax
- 不要加 stagger entry（section 依序 fade-in）
- 不要加 hover glow blur（會跟 halo 衝突）
- 新動效必須**慢到第一眼像靜的**——4 秒以下、位移 < 8px、scale < 1.05 是天花板

---

## 文案節奏

### 6.1 mono vs serif 的分工

| mono（JetBrains Mono） | serif（Shippori Mincho） |
|---|---|
| 章節序號（I · 設計） | 章節名（不完美的工具） |
| 小標 label（版次記號、為何存在） | 段落正文 |
| metadata（macOS 12+ · App Store） | 標題（h1/h2/h3） |
| 版次（Eighteenth Day · The Vessel, Formed） | emphasis（em 強調） |
| uppercase 全大寫小字 | 引言、題辭、所有「意義」類文字 |

**口訣**：**mono 承擔「這是什麼」；serif 承擔「這是誰」。**

### 6.2 em 的用法

`<em>` 在全站**只有兩種用法**：

1. **底線光**（unfold-body）：半透明紫色背景貼在字底
   ```css
   em {
     background: linear-gradient(180deg, transparent 62%, rgba(196,113,245,0.22) 62%);
   }
   ```
2. **紫字**（note-row 的 `.to em`）：直接 `color: var(--vas-aurora-violet)`

不要拿 `<em>` 做 italic——**全站不用 italic**（除瀏覽器預設的 `<i>` 之外）。

### 6.3 標點習慣

| 場景 | 用 | 不用 |
|---|---|---|
| 中文列舉 | `·`（間隔號 U+00B7） | `、` |
| 中文標題連字 | `——`（兩個破折號） | `-`、`—` |
| 中英混排 | 中文之後空半型空格再接英文 | 不空格硬貼 |
| 強調 | `**粗**`（md）或 `<em>` | CAPS、!!! |

---

## 彩蛋 · Trail 光點

**三顆紫點，從首頁走到內核。不說破。**

### 位置

| 順 | 位置 | 類型 | 互動 |
|---|---|---|---|
| **第一顆** | 首屏第三道門（`.shrine-gate.hidden-door`）的 name 後 | 裝飾光點 | 本身就是連結（進 Chapter III） |
| **第二顆** | Chapter III 章頂某處——建議在章節序號「III」的右上角 | 裝飾光點 | 純裝飾，不可點（但 hover 時變亮） |
| **第三顆** | Chapter III 內容中某一句的字尾 | **真正的門** | 點下去進 Harness Engineering 頁面 |

### 樣式（共用）

```css
.trail-dot {
  display: inline-block;
  width: 4px; height: 4px; border-radius: 50%;
  background: var(--vas-aurora-violet);
  margin-left: 8px;
  vertical-align: middle;
  opacity: 0.4;
  transition: opacity .4s;
}
.trail-dot:hover { opacity: 1; }
```

### 第三顆的特殊處理

第三顆是門，不是裝飾——所以它需要：
- `cursor: pointer`
- `opacity: 0.5`（比前兩顆稍亮，給留意的人一個機會）
- hover 時不只是亮，還加一圈極微的光暈 `box-shadow: 0 0 8px var(--vas-aurora-violet)`
- 連結到 `/harness-engineering`（或 repo 既定路徑）

### 不該做的

- ❌ 不要在文中寫「仔細找找看會有彩蛋」
- ❌ 不要給光點加 tooltip（「點我進入 Harness」）
- ❌ 不要讓光點閃爍（用 animation 會太張揚）
- ❌ 不要超過三顆——更多就不神秘了

---

## 套用檢查清單

做新頁面時，順這張單子走過一遍：

- [ ] 底色用 `--vas-void`，不是純黑
- [ ] 正文色不低於 `--vas-ash-1`
- [ ] 所有 mono 字都 uppercase + letter-spacing 0.14–0.22em
- [ ] 沒有用 Italic（除 `<i>` 瀏覽器預設）
- [ ] 沒有給任何非瓶子元素加 aurora 色
- [ ] 動效不超過 4 秒、位移不超過 8px
- [ ] 大 section 之間至少 80px 垂直 padding
- [ ] 章節有 TOC、章末有 Passage
- [ ] Passage 不是按鈕，是翻頁
- [ ] 斷點只用 768px 一條（900px 僅限 note-row）
- [ ] CSS class 前綴正確、沒撞 repo 既有樣式
- [ ] i18n key 都在對的 namespace 下

---

## Docs Mode · 手冊態

> 操作手冊（`/docs`）和首頁四章走**不同的設計策略**。這節把差異說清楚。

### 9.1 核心信條（手冊專屬）

1. **進來就懂，著出去。** 讀者不設限——新手、熟手、觀望者、找答案的人。任何一種人進來都得能帶著答案離開。
2. **說「怎麼用」，不說「為什麼」。** 為什麼交給四章。手冊只講操作。
3. **呼吸給版面，不給文字。** 首頁可以用「極少字」當留白；手冊不行——手冊要用**版面留白**（padding、gap、max-width）來呼吸，**文字本身要清晰無模糊**。
4. **不隱喻、不文青。** 標題直接點出功能；段落直接說步驟；**不准用「器物」「承接」「呼吸」這類首頁用詞**。

### 9.2 和 Shrine Mode 的差異對照

| 項目 | Shrine Mode（首頁四章） | Docs Mode（手冊） |
|---|---|---|
| **halo / room gradient** | ✅ 用 | ❌ **完全拿掉** |
| **aurora 氛圍** | ✅ 瓶子光暈、em 底線 | ❌ 只留 aurora-violet 做 hover / 少量強調；**絕不當背景** |
| **Trail 光點** | ✅ 首屏、ch3 各一顆 | ❌ 不在手冊出現 |
| **正文字色** | `ash-1`（留氛圍） | `ash-0`（留可讀） |
| **section 上下 padding** | 80–120px | **48–64px**（收一階） |
| **h1 字重** | 300（極輕） | **500**（實在） |
| **em 強調** | 底線光 | **色塊標注**（背景 `rgba(196,113,245,0.08)` + 邊框 1px）或粗體 |
| **動效** | breathe / halo / room | **只保留 hover 過渡**，不自動循環 |
| **Italic** | ❌ 不用 | ❌ 不用（同上） |
| **語彙** | 隱喻、題辭 | 指令、步驟、定義 |

### 9.3 Docs Mode 專屬元件

#### 9.3.1 Docs Layout · 雙欄版

**結構**：
```html
<div class="docs-layout">
  <aside class="docs-toc-sticky"> ... 側邊固定目錄 ... </aside>
  <main class="docs-main"> ... 內容 ... </main>
</div>
```

- 桌面：`grid-template-columns: 220px 1fr`（TOC 220px）
- 手機：**塌成單欄**，TOC 改用 `<details>` 折疊
- TOC 是 `position: sticky; top: 72px`（nav 高度 + 一點氣口）

#### 9.3.2 Docs TOC · 側邊目錄

- 字體：`--vas-serif`、15px、ash-1
- 當前章節 highlight：ash-0 + 左側一條 2px 紫線
- hover：ash-0
- **英文長標題處理**：`text-wrap: balance`、`line-height: 1.45`（`[lang="en"]` 再拉到 1.35 避免過鬆）

#### 9.3.3 Mobile TOC · `<details>` 折疊

```html
<details class="docs-toc-mobile">
  <summary>Table of Contents · 本章目錄</summary>
  <ol>...</ol>
</details>
```

- `<summary>`：mono 11px、ash-2、uppercase；前綴用 CSS `::before` 加一個「+」，open 時變「−」
- 展開時 item 換行、border-bottom 分隔——**無論多長都不破版**
- 只在 ≤ 768px 顯示；桌面 `display: none`

#### 9.3.4 Docs Card · 手冊卡片

用在 Welcome 的三塊入口、Tips、進階雜項。

```html
<a class="docs-card" href="#">
  <div class="docs-card-kicker">01 · Getting Started</div>
  <h3 class="docs-card-name">第一次打開 VAS</h3>
  <p class="docs-card-desc">從下載、授權、第一次截圖到第一次丟出去——五個動作走完 VAS 的一個循環。</p>
  <div class="docs-card-meta">5 min · 入門</div>
</a>
```

- padding 32px、border 1px `--vas-rule`、border-radius 2px（**不要圓角**——手冊不用圓潤感）
- hover：border-color 轉 `--vas-rule-strong`、kicker 轉紫、無位移
- 卡片之間 gap 16px；**不要卡片陰影**

#### 9.3.5 Docs Accordion · 手風琴

用在 FAQ、快捷鍵分組、長列表。

```html
<details class="docs-accordion">
  <summary>
    <span class="name">如何關閉 OCR 自動識別？</span>
    <span class="mark">+</span>
  </summary>
  <div class="docs-accordion-body">...</div>
</details>
```

- `<summary>`：padding 20px 0、border-bottom 1px rule、cursor pointer
- `.mark`：mono 16px、`open` 時變「−」
- body：padding 0 0 20px、serif 16px、ash-1、line-height 1.85

### 9.4 RWD · 英文斷字

**三層防線**（重要——英文最易破版）：

1. **內容層**：手冊 TOC 英文標題 ≤ 28 字元。超過拆成 title + kicker。
2. **CSS 層**：
   ```css
   .docs-toc-name,
   .docs-card-name,
   .docs-accordion summary .name {
     word-break: keep-all;      /* 中日韓不破字 */
     overflow-wrap: break-word; /* 但超長英文單字允許斷 */
     hyphens: auto;             /* 英文連字號斷行 */
     text-wrap: balance;        /* 多行時分配均勻 */
   }
   [lang="en"] .docs-toc-name { line-height: 1.35; }
   ```
3. **形式層**：≤ 375px 時 serif 正文從 17px 降到 16px，給英文多一口氣。

### 9.5 Docs Mode 套用檢查清單

- [ ] 頁面上沒有 halo、room gradient、aurora 背景光
- [ ] 沒有自動循環的動效（breathe / halo）
- [ ] 正文色是 ash-0，不是 ash-1
- [ ] 標題字重 500，不是 300
- [ ] em 用色塊標注或粗體，不用底線光
- [ ] TOC 桌面 sticky、手機 `<details>`
- [ ] 所有可變寬元素套了「三層防線」的 CSS
- [ ] 語彙是指令、步驟、定義；**沒有「器物」「承接」「呼吸」**
- [ ] i18n namespace 在 `docs.*` 之下

---

## 給宰相的一句話

> 如果任何一條規範和你的 repo 現況衝突，**以 repo 為準**，回報我調整規範。這份文件是**候選**，不是聖旨。
>
> — Nova × Claude · 2026.04.21
