(function () {
  if (typeof gtag !== 'function') return;

  // ── 1. scroll_depth ─────────────────────────────────────────
  var tracked = {};
  window.addEventListener('scroll', function () {
    var h = document.body.scrollHeight - window.innerHeight;
    if (h <= 0) return;
    var pct = Math.round(100 * window.scrollY / h);
    [25, 50, 75, 100].forEach(function (t) {
      if (pct >= t && !tracked[t]) {
        tracked[t] = true;
        gtag('event', 'scroll_depth', { percent_scrolled: t, page_title: document.title });
      }
    });
  });

  document.addEventListener('DOMContentLoaded', function () {

    // ── 2. chapter_view ─────────────────────────────────────────
    document.querySelectorAll('a[href*="insight"], a[href*="collab"], a[href*="harness"], a[href*="milestone"]').forEach(function (link) {
      link.addEventListener('click', function () {
        gtag('event', 'chapter_view', {
          chapter_name: link.textContent.trim(),
          source_page: document.title
        });
      });
    });

    // ── 3. guide_view ────────────────────────────────────────────
    if (/guide\.html/.test(location.pathname)) {
      gtag('event', 'guide_view', { section_name: document.title });
    }

    // ── 4. download_intent (IntersectionObserver on #acquire) ────
    var acquire = document.getElementById('acquire');
    if (acquire && 'IntersectionObserver' in window) {
      var intentFired = false;
      new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting && !intentFired) {
            intentFired = true;
            gtag('event', 'download_intent', { section_visible: 'acquire' });
            obs.disconnect();
          }
        });
      }, { threshold: 0.3 }).observe(acquire);
    }

    // ── 5. download_click / appstore_click / github_release_click
    document.querySelectorAll('a[href*="apps.apple.com"], a[href*="github.com/TB1982/vas/releases"]').forEach(function (link) {
      link.addEventListener('click', function () {
        var isApple = link.href.includes('apps.apple.com');
        gtag('event', 'download_click', {
          version: isApple ? 'tauri' : 'electron',
          link_url: link.href
        });
        if (isApple) {
          gtag('event', 'appstore_click', {
            link_url: link.href,
            page_source: document.title
          });
        } else {
          var seg = link.href.split('/');
          var file = seg[seg.length - 1] || seg[seg.length - 2];
          var ver = (link.href.match(/v[\d.]+/) || ['unknown'])[0];
          gtag('event', 'github_release_click', { file_name: file, version: ver });
        }
      });
    });

    // ── 6. language_switch ───────────────────────────────────────
    document.querySelectorAll('.lang-opt').forEach(function (link) {
      link.addEventListener('click', function () {
        gtag('event', 'language_switch', {
          from_lang: document.documentElement.lang,
          to_lang: link.getAttribute('hreflang') || ''
        });
      });
    });

    // ── 7. outbound_click ────────────────────────────────────────
    document.querySelectorAll('a[href^="http"]').forEach(function (link) {
      if (link.href.includes('apps.apple.com') || link.href.includes('github.com/TB1982/vas/releases')) return;
      link.addEventListener('click', function () {
        gtag('event', 'outbound_click', {
          link_url: link.href,
          link_text: link.textContent.trim().slice(0, 80)
        });
      });
    });

    // ── 8. image_view ────────────────────────────────────────────
    document.querySelectorAll('img').forEach(function (img) {
      img.addEventListener('click', function () {
        gtag('event', 'image_view', {
          image_alt: img.getAttribute('alt') || '',
          page_title: document.title
        });
      });
    });

    // ── 9. brand_touchpoint ──────────────────────────────────────
    var footer = document.querySelector('.site-footer, footer');
    if (footer) {
      footer.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          gtag('event', 'brand_touchpoint', {
            link_text: link.textContent.trim().slice(0, 80)
          });
        });
      });
    }

  });
}());
