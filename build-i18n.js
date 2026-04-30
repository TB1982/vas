#!/usr/bin/env node
// build-i18n.js — generate /en/ /ja/ /cn/ static pages from source HTML + i18n data
// Run: node build-i18n.js

'use strict';
const fs   = require('fs');
const path = require('path');
const vm   = require('vm');

const BASE          = __dirname;
const CANONICAL     = 'https://yoursvas.app';
const TARGET_LANGS  = ['en', 'ja', 'cn'];
const PAGES         = ['index.html', 'about.html', 'insight.html', 'collab.html', 'harness.html', 'milestone.html', 'guide.html', 'privacy.html'];

const LANG_META = {
  en: { htmlLang: 'en',       hreflang: 'en',       label: 'EN',   labelFull: 'English'  },
  ja: { htmlLang: 'ja',       hreflang: 'ja',       label: '日',   labelFull: '日本語'    },
  cn: { htmlLang: 'zh-Hans',  hreflang: 'zh-Hans',  label: '简',   labelFull: '简中'      },
};

// ── i18n loader ──────────────────────────────────────────────────────────────

function loadI18n(lang) {
  const src     = fs.readFileSync(path.join(BASE, 'i18n', lang + '.js'), 'utf8');
  const sandbox = { window: { VASI18n: {} } };
  vm.createContext(sandbox);
  vm.runInContext(src, sandbox);
  return sandbox.window.VASI18n[lang];
}

// ── per-page merge strategy (mirrors each page's applyLang) ──────────────────

function getMerged(t, page) {
  const m = {};
  switch (page) {
    case 'index.html':
      Object.assign(m, t.shared   || {});
      break;
    case 'insight.html':
      Object.assign(m, t.shared   || {}, t.insight  || {});
      break;
    case 'collab.html':
      Object.assign(m, t.shared   || {}, t.collab   || {}, t.collab2   || {});
      break;
    case 'harness.html':
      Object.assign(m, t.shared   || {}, t.harness  || {}, t.harness2  || {});
      break;
    case 'milestone.html':
      Object.assign(m, t.shared   || {});
      flat(m, t.chronicle || {}, 'chronicle.');
      break;
    case 'guide.html':
      Object.assign(m, t.shared   || {}, t.guide    || {});
      break;
    case 'about.html':
      Object.assign(m, t.shared   || {});
      flat(m, t.about || {}, 'about.');
      break;
    case 'privacy.html':
      Object.assign(m, t.shared   || {}, t.privacy  || {});
      break;
  }
  // All pages include home2 with 'home2.' prefix (for nav links, footer, etc.)
  flat(m, t.home2 || {}, 'home2.');
  return m;
}
function flat(target, src, prefix) {
  Object.keys(src).forEach(k => { target[prefix + k] = src[k]; });
}

// ── per-page title / meta-desc lookups ───────────────────────────────────────

function getTitle(t, page) {
  switch (page) {
    case 'insight.html':   return (t.insight   || {}).ch1PageTitle            || null;
    case 'collab.html':    return (t.collab2   || {}).ch2PageTitle            || null;
    case 'harness.html':   return (t.harness2  || {}).ch3PageTitle            || null;
    case 'milestone.html': return (t.milestone2|| {}).ch4PageTitle            || null;
    case 'guide.html':     return (t.guide     || {})['docs.title']            || null;
    case 'index.html':     return (t.home2     || {})['title']                || null;
    case 'about.html':     return (t.about     || {})['meta.title']             || null;
    case 'privacy.html':   return (t.privacy   || {}).pageTitle                || null;
  }
  return null;
}

function getMetaDesc(t, page) {
  switch (page) {
    case 'insight.html':   return (t.insight   || {})['ch1.meta.desc']        || null;
    case 'collab.html':    return (t.collab2   || {}).ch2MetaDesc             || null;
    case 'harness.html':   return (t.harness2  || {}).ch3MetaDesc             || null;
    case 'milestone.html': return (t.milestone2|| {}).ch4MetaDesc             || null;
    case 'guide.html':     return (t.guide     || {})['docs.meta.desc']        || null;
    case 'index.html':     return (t.home2     || {})['meta.desc']            || null;
    case 'about.html':     return (t.about     || {})['meta.desc']             || null;
    case 'privacy.html':   return (t.privacy   || {}).metaDesc                || null;
  }
  return null;
}

// ── HTML transforms ───────────────────────────────────────────────────────────

// Replace data-lang-key element content
function applyTranslations(html, merged) {
  return html.replace(
    /<([a-zA-Z][a-zA-Z0-9]*)[^>]*\bdata-lang-key="([^"]+)"[^>]*>([\s\S]*?)<\/\1>/g,
    function(match, tag, key) {
      if (merged[key] !== undefined) {
        const openEnd = match.indexOf('>') + 1;
        const openTag = match.substring(0, openEnd);
        return openTag + merged[key] + '</' + tag + '>';
      }
      return match;
    }
  );
}

// Fix asset paths: add ../ prefix for resources
function fixPaths(html) {
  // Avoid double-prefixing by checking for existing ../
  return html
    .replace(/\bhref="css\//g,     'href="../css/')
    .replace(/\bsrc="css\//g,      'src="../css/')
    .replace(/\bhref="img\//g,     'href="../img/')
    .replace(/\bsrc="img\//g,      'src="../img/')
    .replace(/\bsrc="i18n\//g,     'src="../i18n/')
    .replace(/\bhref="base\.css"/g,'href="../base.css"')
    .replace(/\bsrc="([^"./][^"]*\.js)"/g, function(m, f) {
      // Only fix root-relative JS files (not CDN, not already prefixed)
      if (f.startsWith('http') || f.startsWith('../') || f.startsWith('/')) return m;
      return 'src="../' + f + '"';
    });
}

// Fix internal page links in nav / acquire section
function fixInternalLinks(html, page) {
  // All pages including privacy.html are generated — relative links resolve within the same dir.
  return html;
}

// Update <html lang="...">
function setHtmlLang(html, langCode) {
  return html.replace(/(<html[^>]*\blang=")[^"]*(")/i, '$1' + langCode + '$2');
}

// Update <link rel="canonical">
function setCanonical(html, lang, page) {
  return html.replace(
    /<link rel="canonical"[^>]*>/,
    `<link rel="canonical" href="${CANONICAL}/${lang}/${page}">`
  );
}

// Update <title>
function setTitle(html, title) {
  if (!title) return html;
  return html.replace(/<title[^>]*>[^<]*<\/title>/, '<title>' + esc(title) + '</title>');
}

// Update meta description + og/twitter tags
function setMetaTags(html, title, desc) {
  if (desc) {
    html = html.replace(
      /(<meta\s+name="description"[^>]*\bcontent=")[^"]*(")/,
      '$1' + esc(desc) + '$2'
    );
    html = html.replace(
      /(<meta\s+property="og:description"\s+content=")[^"]*(")/,
      '$1' + esc(desc) + '$2'
    );
    html = html.replace(
      /(<meta\s+name="twitter:description"\s+content=")[^"]*(")/,
      '$1' + esc(desc) + '$2'
    );
  }
  if (title) {
    html = html.replace(
      /(<meta\s+property="og:title"\s+content=")[^"]*(")/,
      '$1' + esc(title) + '$2'
    );
    html = html.replace(
      /(<meta\s+name="twitter:title"\s+content=")[^"]*(")/,
      '$1' + esc(title) + '$2'
    );
    html = html.replace(
      /(<meta\s+property="og:url"\s+content=")[^"]*(")/,
      '$1' + CANONICAL + '/{{LANG}}/{{PAGE}}$2'
    );
  }
  return html;
}

// Add hreflang link tags (insert before </head>)
function addHreflang(html, page) {
  if (html.includes('hreflang')) return html; // already present
  const tags = [
    `<link rel="alternate" hreflang="zh-Hant" href="${CANONICAL}/${page}">`,
    `<link rel="alternate" hreflang="en"       href="${CANONICAL}/en/${page}">`,
    `<link rel="alternate" hreflang="ja"       href="${CANONICAL}/ja/${page}">`,
    `<link rel="alternate" hreflang="zh-Hans"  href="${CANONICAL}/cn/${page}">`,
    `<link rel="alternate" hreflang="x-default" href="${CANONICAL}/${page}">`,
  ].join('\n');
  return html.replace('</head>', tags + '\n</head>');
}

// Replace langDropdownWrap div regardless of nesting depth (div counter)
function replaceLangDropdown(html, newContent) {
  const m = html.match(/<div[^>]*\bid="langDropdownWrap"[^>]*>/);
  if (!m) return html;
  const start = html.indexOf(m[0]);
  let depth = 0, i = start;
  while (i < html.length) {
    if (html[i] === '<') {
      if (html.slice(i, i + 4) === '<div') depth++;
      else if (html.slice(i, i + 6) === '</div>') {
        depth--;
        if (depth === 0) {
          const end = html.indexOf('>', i) + 1;
          return html.slice(0, start) + newContent + html.slice(end);
        }
      }
    }
    i++;
  }
  return html;
}

// Build the two-section (PC flat + mobile dropdown) lang switcher HTML
function buildLangSwitcherHtml(links, mobileLabel, activeLang) {
  const flatLinks = links.map(l => {
    const isActive = l.code === activeLang;
    const activeStyle = isActive ? ';font-weight:600' : '';
    return `<a href="${l.href}" class="lang-opt${isActive ? ' active' : ''}" hreflang="${l.hreflang}" style="text-decoration:none;white-space:nowrap${activeStyle}">${l.label}</a>`;
  }).join('<span class="lang-sep" aria-hidden="true">/</span>');
  const ddLinks = links.map(l => {
    const active = l.code === activeLang ? ' active' : '';
    return `      <a href="${l.href}" class="lang-opt${active}" hreflang="${l.hreflang}" style="text-decoration:none">${l.label}</a>`;
  }).join('\n');
  return `<div class="site-nav-lang" id="langDropdownWrap">
  <div class="lang-flat-row">
${flatLinks}
  </div>
  <div class="lang-mobile-dd">
    <button class="lang-dropdown-btn" onclick="this.nextElementSibling.classList.toggle('open')" aria-label="語言切換"><span>${mobileLabel}</span></button>
    <div class="lang-dropdown-menu">
${ddLinks}
    </div>
  </div>
</div>`;
}

// Replace JS-based language switcher with static links (PC flat + mobile dropdown)
function replaceStaticLangSwitcher(html, lang, page) {
  const links = [
    { code: 'zh', hreflang: 'zh-Hant', label: '中文',    href: `../${page}` },
    { code: 'en', hreflang: 'en',       label: 'English', href: lang === 'en' ? page : `../en/${page}` },
    { code: 'ja', hreflang: 'ja',       label: '日本語',  href: lang === 'ja' ? page : `../ja/${page}` },
    { code: 'cn', hreflang: 'zh-Hans',  label: '简中',    href: lang === 'cn' ? page : `../cn/${page}` },
  ];
  const mobileLabel = LANG_META[lang].label;
  return replaceLangDropdown(html, buildLangSwitcherHtml(links, mobileLabel, lang));
}

// Disable i18n re-rendering on generated static pages
const HAMBURGER_INLINE = `(function(){var btn=document.getElementById('navMobileBtn'),menu=document.getElementById('navMobileMenu'),chevron=document.getElementById('navMobileChevron');if(!btn||!menu)return;var open=false;function close(){open=false;menu.style.display='none';if(chevron)chevron.style.transform='';btn.setAttribute('aria-expanded','false');}function toggle(e){e.stopPropagation();if(open){close();return;}open=true;menu.style.display='flex';if(chevron)chevron.style.transform='rotate(180deg)';btn.setAttribute('aria-expanded','true');}btn.addEventListener('click',toggle);menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});document.addEventListener('click',close);})();`;

function removeI18nScripts(html) {
  // Remove <script src="...core.js"></script> (specific tag, no content span risk)
  html = html.replace(/<script[^>]*src="[^"]*i18n\/core\.js"[^>]*><\/script>[ \t]*\n?/g, '');
  // Neutralize JS-driven lang switching (VASCore not available on static builds)
  html = html.replace(/\bVASCore\.initDropdown\s*\([^)]*\)\s*;?/g, '');
  // Replace initNavDropdown with inline hamburger so static builds still work
  html = html.replace(/\bVASCore\.initNavDropdown\s*\(\s*\)\s*;?/g, HAMBURGER_INLINE);
  return html;
}

// For guide.html: pre-set language-specific images in static HTML
function fixGuideImages(html, lang) {
  const editorMap = {
    en: ['../img/vas-guide-editor-en.webp', 'VAS screenshot editor — annotation tools, OCR privacy masking and export'],
    ja: ['../img/vas-guide-editor-jp.webp', 'VAS スクリーンショットエディタ——注釈ツール・OCRプライバシーマスク・書き出し機能'],
    cn: ['../img/vas-guide-editor-zh-CN.png','VAS 截图编辑器界面——标注工具、OCR 隐私遮蔽与导出功能完整说明'],
  };
  const toolbarMap = {
    en: ['../img/vastoolbar-en.webp',   'VAS floating toolbar — Mac screenshot annotation tool'],
    ja: ['../img/vastoolbar-jp.webp',   'VAS Macスクリーンショットツール フローティングツールバー'],
    cn: ['../img/vastoolbar-zh-CN.png', 'VAS Mac 截图工具浮动工具栏'],
  };
  if (editorMap[lang]) {
    const [src, alt] = editorMap[lang];
    html = html.replace(
      /(<img[^>]*class="[^"]*js-editor-img[^"]*"[^>]*src=")[^"]*("[^>]*alt=")[^"]*(")/,
      '$1' + src + '$2' + alt + '$3'
    );
  }
  if (toolbarMap[lang]) {
    const [src, alt] = toolbarMap[lang];
    html = html.replace(
      /(<img[^>]*class="[^"]*js-toolbar-img[^"]*"[^>]*src=")[^"]*("[^>]*alt=")[^"]*(")/g,
      '$1' + src + '$2' + alt + '$3'
    );
  }
  return html;
}

// Fix privacy.html JSON-LD: url, inLanguage, name per language
function fixPrivacyJsonLd(html, lang, t) {
  const meta = LANG_META[lang];
  const url  = `${CANONICAL}/${lang}/privacy.html`;
  const name = (t.privacy || {}).appName || 'VAS Privacy Policy';
  html = html.replace(
    /"url":\s*"https:\/\/tb1982\.github\.io\/vas\/privacy\.html"/,
    `"url": "${url}"`
  );
  html = html.replace(
    /"inLanguage":\s*\[[^\]]*\]/,
    `"inLanguage": "${meta.hreflang}"`
  );
  html = html.replace(
    /"name":\s*"VAS Privacy Policy"/,
    `"name": "${name}"`
  );
  return html;
}

// Escape special chars for use in attribute values
function esc(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
}

// ── source zh pages: replace JS dropdown with static links ───────────────────

function patchSourceLangSwitcher() {
  PAGES.forEach(page => {
    const fpath = path.join(BASE, page);
    let html = fs.readFileSync(fpath, 'utf8');
    const links = [
      { code: 'zh', hreflang: 'zh-Hant', label: '中文',    href: page },
      { code: 'en', hreflang: 'en',       label: 'English', href: `en/${page}` },
      { code: 'ja', hreflang: 'ja',       label: '日本語',  href: `ja/${page}` },
      { code: 'cn', hreflang: 'zh-Hans',  label: '简中',    href: `cn/${page}` },
    ];
    html = replaceLangDropdown(html, buildLangSwitcherHtml(links, '中', 'zh'));
    html = html.replace(/\bVASCore\.initDropdown\s*\([^)]+\)\s*;?/g, '');
    fs.writeFileSync(fpath, html, 'utf8');
    console.log(`[zh] lang switcher → ${page}`);
  });
}

// ── source zh pages: add hreflang only ───────────────────────────────────────

function patchSourcePages() {
  PAGES.forEach(page => {
    const fpath = path.join(BASE, page);
    let html = fs.readFileSync(fpath, 'utf8');
    if (!html.includes('hreflang')) {
      html = addHreflang(html, page);
      fs.writeFileSync(fpath, html, 'utf8');
      console.log(`[zh] hreflang → ${page}`);
    }
  });
}

// ── generate one language's pages ────────────────────────────────────────────

function buildLang(lang, t) {
  const meta   = LANG_META[lang];
  const outDir = path.join(BASE, lang);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  PAGES.forEach(page => {
    let html = fs.readFileSync(path.join(BASE, page), 'utf8');

    const merged  = getMerged(t, page);
    const title   = getTitle(t, page);
    const metaDesc= getMetaDesc(t, page);

    html = applyTranslations(html, merged);
    html = setHtmlLang(html, meta.htmlLang);
    html = setCanonical(html, lang, page);
    html = setTitle(html, title);
    html = setMetaTags(html, title, metaDesc);
    html = addHreflang(html, page);
    html = replaceStaticLangSwitcher(html, lang, page);
    html = removeI18nScripts(html);
    html = fixPaths(html);
    html = fixInternalLinks(html, page);
    if (page === 'guide.html')   html = fixGuideImages(html, lang);
    if (page === 'privacy.html') html = fixPrivacyJsonLd(html, lang, t);

    // Fix og:url placeholder
    html = html.replace(/\/{{LANG}}\/{{PAGE}}/g, `/${lang}/${page}`);

    fs.writeFileSync(path.join(outDir, page), html, 'utf8');
    console.log(`[${lang}] ${page}`);
  });
}

// ── main ─────────────────────────────────────────────────────────────────────

function main() {
  console.log('── VAS i18n static build ──');
  patchSourceLangSwitcher();
  patchSourcePages();
  TARGET_LANGS.forEach(lang => {
    const t = loadI18n(lang);
    buildLang(lang, t);
  });
  console.log('── done ──');
}

main();
