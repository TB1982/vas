#!/usr/bin/env python3
"""VAS sitemap 產生器 —— 讀 sitemap.manifest.json，lastmod 由 git 自動抓，吐出 sitemap.xml。

用法（在 repo 根目錄）：
    python3 tools/gen_sitemap.py            # 產生並覆寫 sitemap.xml
    python3 tools/gen_sitemap.py --check    # 只比對，不寫檔（CI 用；有差異回傳非 0）

新增頁面：在 sitemap.manifest.json 對應 section 的 pages 加一筆
    { "slug": "新網址", "file": "來源檔.html", "changefreq": "monthly", "priority": "0.8" }
lastmod 不用手填 —— 每個語系檔的最後 commit 日期由 git 決定。
"""
import json, os, subprocess, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "sitemap.manifest.json")
OUTPUT = os.path.join(ROOT, "sitemap.xml")
LOCALES = [("root", "", "zh-Hant"), ("en", "/en", "en"), ("ja", "/ja", "ja"), ("cn", "/cn", "zh-Hans")]

def git_lastmod(path, fallback):
    """該檔最後一次 commit 的日期（YYYY-MM-DD）；未進版控則用 fallback（今天）。"""
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return fallback
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        return out or fallback
    except subprocess.CalledProcessError:
        return fallback

def url_for(base, prefix, slug):
    return f"{base}{prefix}/" if slug == "" else f"{base}{prefix}/{slug}"

def locale_file(loc_key, root_file):
    return root_file if loc_key == "root" else f"{loc_key}/{root_file}"

def build():
    man = json.load(open(MANIFEST, encoding="utf-8"))
    base = man["base"]
    today = datetime.date.today().isoformat()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    chunks = []
    for sec in man["sections"]:
        first_in_section = True
        for page in sec["pages"]:
            slug = page["slug"]
            # 四語 hreflang（每個 url 區塊共用同一組）
            alts = []
            for loc_key, prefix, hlang in LOCALES:
                alts.append(f'    <xhtml:link rel="alternate" hreflang="{hlang}" href="{url_for(base, prefix, slug)}"/>')
            alts.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for(base, "", slug)}"/>')
            for loc_key, prefix, hlang in LOCALES:
                loc = url_for(base, prefix, slug)
                lastmod = git_lastmod(locale_file(loc_key, page["file"]), today)
                block = ['  <url>',
                         f'    <loc>{loc}</loc>',
                         f'    <lastmod>{lastmod}</lastmod>',
                         f'    <changefreq>{page["changefreq"]}</changefreq>',
                         f'    <priority>{page["priority"]}</priority>',
                         *alts,
                         '  </url>']
                text = "\n".join(block)
                if first_in_section:
                    comment = "\n".join(f'  <!-- {c} -->' for c in sec["comments"])
                    text = comment + "\n" + text
                    first_in_section = False
                chunks.append(text)
    return "\n".join(out) + "\n\n" + "\n\n".join(chunks) + "\n\n</urlset>\n"

def main():
    xml = build()
    if "--check" in sys.argv:
        cur = open(OUTPUT, encoding="utf-8").read() if os.path.exists(OUTPUT) else ""
        if xml == cur:
            print("sitemap.xml 已是最新，無需更新")
            return 0
        print("sitemap.xml 與產生結果有差異（需重新產生）")
        return 1
    open(OUTPUT, "w", encoding="utf-8").write(xml)
    print(f"已寫入 {OUTPUT}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
