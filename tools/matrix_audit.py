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

# ════════════════ report ════════════════
quiet = "--quiet" in sys.argv
by_family = {}
for fam, msg in findings:
    by_family.setdefault(fam, []).append(msg)
LABEL = {"chrome": "A · CHROME drift", "links": "B · LINK hygiene", "codename": "C · CODENAME drift",
         "meta": "D · METADATA locale", "sitemap": "E · SITEMAP freshness",
         "llms": "F · LLMS.TXT links"}
total = sum(1 for f, m in findings if not m.startswith("    "))
for fam in ["chrome", "links", "codename", "meta", "sitemap", "llms"]:
    msgs = by_family.get(fam, [])
    print(f"\n══ {LABEL[fam]} ══  ({sum(1 for m in msgs if not m.startswith('    '))} findings)")
    for m in msgs: print(("  " + m) if not m.startswith("    ") else ("  " + m))
    if not msgs: print("  ✓ clean")
print(f"\nTOTAL top-level findings: {total}")
sys.exit(1 if findings else 0)
