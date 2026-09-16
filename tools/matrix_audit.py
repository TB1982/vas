#!/usr/bin/env python3
"""
Matrix audit — treats the site as a (page × locale) grid, not isolated files.
Three check families, all grid-aware so a finding in one locale is checked in all:
  A. chrome    — shared header/footer must not drift within a locale
  B. links     — es cross-page links must not point at /en/ when an es sibling exists
  C. codenames — the same chapter's display name must agree across every slot
                 (echo TOC vs passage-nav) — catches time-series translation drift.

Usage:  python3 tools/matrix_audit.py [--quiet]
Exit 1 if any finding, else 0.  Excludes archive/.
"""
import re, glob, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
LOCALES = {"root": "", "en": "en/", "ja": "ja/", "cn": "cn/", "es": "es/"}

def pages_for(loc, prefix):
    """html files belonging to a locale (root = top-level + guide/ + harness/)."""
    if loc == "root":
        fs = glob.glob("*.html") + glob.glob("guide/*.html") + glob.glob("harness/*.html")
    else:
        fs = glob.glob(prefix + "**/*.html", recursive=True)
    return [f for f in sorted(fs) if not f.startswith("archive/")]

def slug_of(f, prefix):
    return f[len(prefix):] if prefix and f.startswith(prefix) else f

def read(f):
    return open(f, encoding="utf-8").read()

findings = []
def flag(family, msg):
    findings.append((family, msg))

# ── build the grid ──
GRID = {loc: {slug_of(f, pre): f for f in pages_for(loc, pre)} for loc, pre in LOCALES.items()}
ES_SLUGS = set(GRID["es"].keys())  # which slugs have an es sibling

# ════════════════ A. CHROME consistency (footer credit) ════════════════
# credit sentence end-markers per locale (footer "VAS — ... days/器物")
CREDIT_END = {"root": "器物。", "cn": "器物。", "en": "twenty-five days.",
              "ja": "作り上げた器。", "es": "veinticinco días."}
def footer_credit(s, end):
    m = re.search(r'<strong[^>]*>VAS</strong>\s*[—–-]{1,2}\s*(.*?' + re.escape(end) + r')', s, re.S)
    if not m: return None
    return re.sub(r'\s+', ' ', m.group(1))  # normalize whitespace; ignores <strong> style diff

for loc, pre in LOCALES.items():
    end = CREDIT_END[loc]
    variants = {}
    for slug, f in GRID[loc].items():
        c = footer_credit(read(f), end)
        if c: variants.setdefault(c, []).append(slug)
    if len(variants) > 1:
        flag("chrome", f"[{loc}] footer credit has {len(variants)} variants:")
        for c, files in sorted(variants.items(), key=lambda kv: -len(kv[1])):
            flag("chrome", f"    ({len(files)}×) {c[:70]}…  e.g. {files[0]}")

# ── A2. header nav labels: within a locale, the standard nav must read the same everywhere ──
NAV_LINK = re.compile(r'<div class="site-nav-links">(.*?)</div>', re.S)
def nav_labels(s):
    m = NAV_LINK.search(s)
    if not m: return None
    labels = re.findall(r'<a [^>]*>([^<]+)</a>', m.group(1))
    return " · ".join(l.strip() for l in labels)
for loc, pre in LOCALES.items():
    variants = {}
    for slug, f in GRID[loc].items():
        n = nav_labels(read(f))
        if n: variants.setdefault(n, []).append(slug)
    if len(variants) > 1:
        flag("chrome", f"[{loc}] header nav has {len(variants)} label-sets:")
        for n, files in sorted(variants.items(), key=lambda kv: -len(kv[1])):
            flag("chrome", f"    ({len(files)}×) {n}  e.g. {files[0]}")

# ════════════════ B. LINK hygiene (es → /en/ when es sibling exists) ════════════════
EN_LINK = re.compile(r'href="(?:\.\./|/)?en/([A-Za-z0-9_/-]+?)(?:\.html)?(?:#[^"]*)?"')
for slug, f in GRID["es"].items():
    s = read(f)
    for m in re.finditer(EN_LINK, s):
        target = m.group(1)                      # e.g. "insight", "guide/arrange", "vessel"
        tslug = target + ".html"
        # own-page en sibling (switcher / hreflang) is legit
        if tslug == slug or target == slug.replace(".html", ""): continue
        if target + ".html" == slug: continue
        # legit only if target has NO es sibling (true /en/ fallback)
        if tslug in ES_SLUGS:
            # exclude same-page hreflang/switcher forms already handled; report cross-page
            line = s[:m.start()].count("\n") + 1
            ctx = s[max(0, m.start()-0):m.end()]
            flag("links", f"[es/{slug}] L{line}: links to /en/{target} but es/{tslug} exists → should be /es/")

# ════════════════ C. CODENAME consistency (echo TOC vs passage-nav) ════════════════
# For each locale, collect chapter slug -> {display names} from every slot.
# If a slug carries >1 distinct name, translation drifted across pages/time.
CHAPTERS = {"insight.html", "collab.html", "context.html", "self.html", "harness.html", "us.html"}
def collect_names(loc):
    names = {}  # target-slug -> {name: [where]}
    for slug, f in GRID[loc].items():
        s = read(f)
        # echo TOC:  href="X.html" ... echo-toc-name">NAME
        for m in re.finditer(r'echo-toc-item" href="([^"]+?\.html)".*?echo-toc-name">([^<]+)</', s, re.S):
            t = os.path.basename(m.group(1))
            if t in CHAPTERS:
                names.setdefault(t, {}).setdefault(m.group(2).replace("&nbsp;", " ").strip(), []).append(f"{slug}:echo")
        # passage-nav:  passage-link is-prev/next" href="X.html" ... <span class="name">NAME</span>
        for m in re.finditer(r'passage-link is-(?:prev|next)" href="([^"]+?\.html)".*?<span class="name">([^<]*)</span>', s, re.S):
            t = os.path.basename(m.group(1))
            if t in CHAPTERS:
                names.setdefault(t, {}).setdefault(m.group(2).strip(), []).append(f"{slug}:nav")
    return names

for loc in LOCALES:
    names = collect_names(loc)
    for t, variants in sorted(names.items()):
        if len(variants) > 1:
            flag("codename", f"[{loc}] chapter '{t}' has {len(variants)} names across slots:")
            for name, wheres in variants.items():
                flag("codename", f"    “{name}”  ← {', '.join(wheres)}")

# ════════════════ D. METADATA locale consistency (JSON-LD / html / og must match the grid locale) ════════════════
LANG     = {"root": "zh-Hant", "en": "en", "ja": "ja", "cn": "zh-Hans", "es": "es"}
OGLOCALE = {"root": "zh_TW",   "en": "en_US", "ja": "ja_JP", "cn": "zh_CN", "es": "es_ES"}
INLANG   = {"root": "zh-Hant", "en": "en", "ja": "ja", "cn": "zh-Hans", "es": "es"}
for loc, pre in LOCALES.items():
    for slug, f in GRID[loc].items():
        s = read(f)
        m = re.search(r'<html lang="([^"]*)"', s)
        if m and m.group(1) != LANG[loc]:
            flag("meta", f"[{loc}] {slug}: html lang=\"{m.group(1)}\" ≠ expected \"{LANG[loc]}\"")
        m = re.search(r'property="og:locale" content="([^"]*)"', s)   # absent is OK (e.g. 404)
        if m and m.group(1) != OGLOCALE[loc]:
            flag("meta", f"[{loc}] {slug}: og:locale=\"{m.group(1)}\" ≠ expected \"{OGLOCALE[loc]}\"")
        for m in re.finditer(r'"inLanguage":\s*"([^"]*)"', s):        # every JSON-LD block
            if m.group(1) != INLANG[loc]:
                flag("meta", f"[{loc}] {slug}: JSON-LD inLanguage=\"{m.group(1)}\" ≠ expected \"{INLANG[loc]}\"")
        # literal template-var leak (the f-string {slug} class of bug)
        for m in re.finditer(r'(?:"url":\s*"|rel="canonical" href="|property="og:url" content=")([^"]*\{[^"]*)"', s):
            flag("meta", f"[{loc}] {slug}: unresolved template var in URL → {m.group(1)}")

# ════════════════ E. SITEMAP freshness (page edits must be reflected in sitemap.xml) ════════════════
import subprocess
try:
    r = subprocess.run([sys.executable, "tools/gen_sitemap.py", "--check"],
                       capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        out = (r.stdout + r.stderr).strip().splitlines()
        flag("sitemap", "sitemap.xml out of sync (run `python3 tools/gen_sitemap.py` and commit):")
        for ln in out[-3:]:
            flag("sitemap", f"    {ln}")
except Exception as e:
    flag("sitemap", f"sitemap check could not run: {e}")

# ════════════════ F. LLMS.TXT link integrity (curated AI index must not silently rot) ════════════════
if os.path.exists("llms.txt"):
    lt = read("llms.txt")
    def resolves(path):
        path = path.rstrip("/")
        if path == "":
            return os.path.exists("index.html")
        cands = [path + ".html", os.path.join(path, "index.html"), path]
        return any(os.path.exists(c) for c in cands)
    for url in re.findall(r'\]\((https://yoursvas\.app/[^)]*)\)', lt):
        path = url.split("https://yoursvas.app/", 1)[1]
        if not resolves(path):
            flag("llms", f"llms.txt links to {url} → no such page")

# ════════════════ G. LIVE-VALUE consistency (facts that track reality must not drift apart) ════════════════
# A "live value" is a number that follows the outside world — current version, download filename, install size.
# It is the opposite of a dated record: history blocks (arc-lines, arc-dividers, the density caption) legitimately
# hold old values and are stripped before checking. Two sub-checks:
#   G1 · one fact, one value — a fact written in several slots across pages must read the same in all of them
#   G2 · locale parity — the five locale files of a page are structurally parallel, so their ordered number
#        sequence must match; a divergence means someone updated one locale and forgot the others.
# What this CANNOT catch: every copy being consistently stale. That needs the outside world — run with
# --values to print the checklist of live values and their locations, then verify those against reality.
HIST = re.compile(r'<div class="arc-line">.*?</div>|<summary class="arc-divider">.*?</summary>'
                  r'|<div class="edensity-cap">.*?</div>|<!--.*?-->', re.S)
def live(s):
    return HIST.sub(" ", s)

# fact name -> list of (regex with one capture group, restrict-to-basename or None for any page)
FACTS = {
    "下載檔名 · download filename": [(r'download\.yoursvas\.app/(VAS-[0-9.]+-arm64\.dmg)', None)],
    "Tauri 目前版本": [(r'　<strong>(v2\.\d+\.\d+)</strong>', "changelog.html"),
                       (r'<span class="meta">(v2\.\d+\.\d+) ', "instrument.html"),
                       (r'(v2\.\d+\.\d+) <span class="ar">', "instrument.html")],
    "Electron 目前版本": [(r'<span class="meta">(v3\.\d+(?:\.\d+)?) ', "instrument.html")],
    # 「本頁收錄 N 個 Sprint」這種計數散在 metadata / JSON-LD / 節奏帶 / 讀數共 25 處，
    # 各語系量詞寫法還不同（Sprints · 個の · 个）。數字寫在 Sprint 前面才是計數；
    # arc 行的「Sprint 195」是數字在後，且已被 live() 濾掉。
    "Sprint 總數": [(r'(\d{3})\s*(?:個の|个|個)?\s*Sprints?\b', "changelog.html")],
}
FACT_VALUES = {}
for fact, slots in FACTS.items():
    vals = {}
    for loc, pre in LOCALES.items():
        for slug, f in GRID[loc].items():
            hit = [rx for rx, base in slots if base is None or slug == base]
            if not hit: continue
            body = live(read(f))
            for rx in hit:
                for m in re.finditer(rx, body):
                    vals.setdefault(m.group(1), []).append(f)
    FACT_VALUES[fact] = vals
    if len(vals) > 1:
        flag("values", f"{fact} 有 {len(vals)} 種值——其中至少一種已過期：")
        for v, fs in sorted(vals.items(), key=lambda kv: -len(kv[1])):
            flag("values", f"    ({len(fs)}×) {v}  例：{fs[0]}")

# G2 · locale parity of numeric facts (MB sizes) on the same page
SIZE_BY_PAGE = {}
NUM = re.compile(r'(\d+(?:\.\d+)?)\s?MB', re.I)  # 單位大小寫不影響數值比對
for slug in sorted(set(GRID["root"]) | set(GRID["en"])):
    seqs = {}
    for loc in LOCALES:
        f = GRID[loc].get(slug)
        if f: seqs[loc] = NUM.findall(live(read(f)))
    if len(seqs) < 2: continue
    forms = {}
    for loc, seq in seqs.items():
        forms.setdefault(tuple(seq), []).append(loc)
    if seqs.get("root"): SIZE_BY_PAGE[slug] = seqs["root"]
    if len(forms) > 1:
        flag("values", f"{slug} 的體積數字跨語系不一致（同頁五語應同序同值）：")
        for seq, locs in sorted(forms.items(), key=lambda kv: -len(kv[1])):
            flag("values", f"    {'/'.join(locs)} → {' · '.join(seq) if seq else '（無）'}")


# ════════════════ report ════════════════
quiet = "--quiet" in sys.argv
by_family = {}
# ════════ H. 內嵌 app 字串 vs docs/app-i18n-table.md ════════
# guide 每一頁都內嵌一張多語工具名對照表（互動示範的 tooltip 用）。
# 那是 app 字串的拷貝，藏在 JS 裡而不是可見文字裡——A 族看 chrome、G 族看數字，
# 兩族都沒有在看它，所以 2026-09 的 es「Región」錯了很久沒人發現（app 是「Área」）。
# 表是快照：app 改字串後這裡會紅，那正是該去對齊的時刻，不是誤報。
APP_TBL = {}
_tbl_path = "docs/app-i18n-table.md"
if os.path.exists(_tbl_path):
    for _ln in open(_tbl_path, encoding="utf-8"):
        _m = re.match(r"\|\s*`([^`]+)`\s*\|(.+)\|\s*$", _ln)
        if not _m: continue
        _c = [x.strip() for x in _m.group(2).split("|")][:5]
        if len(_c) == 5:
            APP_TBL[_m.group(1)] = dict(zip(["cn", "zh", "ja", "en", "es"], _c))

MAP_LANG = {"en": "en", "ja": "ja", "zh-Hans": "cn", "es": "es"}
# 例外：(key, 對照表語系欄) → 為什麼網頁刻意不照抄 app
# 登記例外而不是登記要檢查的項目——忘了登記例外只是誤報（很吵，當天會被修），
# 忘了登記檢查項目則是靜默的洞。要讓失敗的方式是吵的。
APPSTR_OK = {
    # 2026-09-16 已確認為漏譯，app 側已修成「Selector de color」＝網頁現值，隨下一版出。
    # 這條不能現在刪：H 族比對的是 docs/app-i18n-table.md，那是 v2.19.0 的出貨快照，
    # 表裡還寫著「Color」，刪了會立刻紅。**下一份 i18n 導出進表時，連同這條例外一起刪。**
    ("color", "es"): "app 已修正，待下一份 i18n 導出進表後刪除此例外",
}
_seen = {}
for _f in sorted(glob.glob("guide/*.html") + glob.glob("*/guide/*.html")):
    _s = read(_f)
    for _lang, _block in re.findall(r"'([A-Za-z-]+)':\s*\{ fullscreen:(.*?)\}", _s):
        _col = MAP_LANG.get(_lang)
        if not _col: continue
        for _k, _v in re.findall(r"(\w+):'([^']*)'", "fullscreen:" + _block):
            _want = APP_TBL.get(_k, {}).get(_col, "")
            if (_k, _col) in APPSTR_OK: continue
            if _want and not _want.startswith("_（") and _v != _want:
                _seen.setdefault((_k, _lang, _v, _want), []).append(_f)
for (_k, _lang, _got, _want), _fs in sorted(_seen.items()):
    flag("appstr", f"內嵌對照表 {_k}／{_lang} 寫「{_got}」，app 總表是「{_want}」（{len(_fs)} 檔）")

for fam, msg in findings:
    by_family.setdefault(fam, []).append(msg)
LABEL = {"chrome": "A · CHROME drift", "links": "B · LINK hygiene", "codename": "C · CODENAME drift",
         "meta": "D · METADATA locale", "sitemap": "E · SITEMAP freshness",
         "llms": "F · LLMS.TXT links", "values": "G · LIVE-VALUE drift",
         "appstr": "H · APP-STRING drift"}
total = sum(1 for f, m in findings if not m.startswith("    "))
for fam in ["chrome", "links", "codename", "meta", "sitemap", "llms", "values", "appstr"]:
    msgs = by_family.get(fam, [])
    print(f"\n══ {LABEL[fam]} ══  ({sum(1 for m in msgs if not m.startswith('    '))} findings)")
    for m in msgs: print(("  " + m) if not m.startswith("    ") else ("  " + m))
    if not msgs: print("  ✓ clean")
if "--values" in sys.argv:
    print("\n══ 活值清單 · LIVE VALUES ══  (對照現實時看這份，不是看手寫文件)")
    for fact, vals in FACT_VALUES.items():
        print(f"  {fact}")
        for v, fs in sorted(vals.items(), key=lambda kv: -len(kv[1])):
            print(f"    {v}   ({len(fs)} 處：{', '.join(sorted(set(fs))[:3])}{' …' if len(set(fs))>3 else ''})")
    print("  體積（MB · 依頁面出現順序）")
    for slug, seq in sorted(SIZE_BY_PAGE.items()):
        if seq: print(f"    {slug:22s} {' · '.join(seq)}")
print(f"\nTOTAL top-level findings: {total}")
sys.exit(1 if findings else 0)
