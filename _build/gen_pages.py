#!/usr/bin/env python3
"""Generate the Wristalk support site (static HTML, no build step needed to view).

Source of truth: this file (shared page chrome + CSS) and _build/content_en.py /
_build/content_de.py (page text as small HTML snippets).
Output (committed):  index.html, support/index.html, privacy.html, terms.html
                     de/index.html, de/support/index.html, de/privacy.html, de/terms.html

Run from the repo root:  python3 _build/gen_pages.py

All internal links are relative so the site works under
https://cb2206.github.io/wristalk-support/ and on any later custom domain.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import content_de  # noqa: E402
import content_en  # noqa: E402

# ---------------------------------------------------------------------------
# Site-wide values. Change them here and re-run the script.
# ---------------------------------------------------------------------------
SUPPORT_EMAIL = "hello@wristalk.app"         # Cloudflare Email Routing → owner inbox (2026-10-06)
SITE_URL = "https://wristalk.app"            # absolute URLs for canonical, hreflang and Open Graph tags
APP_STORE_URL = "https://apps.apple.com/us/app/wristalk/id6816532048"
APP_STORE_LIVE = False                       # True once the app is live: the "Coming soon" badge becomes a link
COMPANY = "CB Group LLC"
COMPANY_ADDRESS = "1500 N Grant St, Ste #10470, Denver, CO 80203, USA"
# Governing law and venue, as it reads inside a sentence in each language.
JURISDICTION = {"en": "the State of Colorado, USA", "de": "des Bundesstaats Colorado, USA"}
# Effective date of the privacy policy and terms (set when a new version is published), per language.
EFFECTIVE = {"en": "October 28, 2026", "de": "28. Oktober 2026"}

LANGS = {"en": "", "de": "de/"}              # language -> folder prefix
PAGES = {"home": "index.html", "support": "support/index.html",
         "privacy": "privacy.html", "terms": "terms.html"}
CONTENT = {"en": content_en, "de": content_de}
LANG_NAME = {"en": "English", "de": "Deutsch"}


def out_path(lang, page):
    return LANGS[lang] + PAGES[page]


def public_url(lang, page):
    """Absolute URL a page is served at (the worker maps /terms → terms.html, /support/ → support/index.html)."""
    path = out_path(lang, page)
    path = path[:-len("index.html")] if path.endswith("index.html") else path[:-len(".html")]
    return f"{SITE_URL}/{path}"


def rel(from_file, to_file):
    """Relative URL from one generated file to another (both repo-relative)."""
    return os.path.relpath(to_file, os.path.dirname(from_file) or ".").replace(os.sep, "/")


CSS = r"""
  :root {
    --bg: #f5f7f6; --surface: #ffffff; --surface-2: #eef3f1;
    --heading: #0b0f0e; --body: #333d3a; --faint: #59625f;
    --link: #0a7560; --accent: #0a7560; --mint: #5ad2b4; --orange: #b35c00; --orange-fill: #ff9f0a;
    --line: rgba(11,15,14,0.10); --card-border: rgba(11,15,14,0.09);
    --card-shadow: 0 1px 2px rgba(11,15,14,0.04), 0 8px 24px rgba(11,15,14,0.05);
    --nav-bg: rgba(245,247,246,0.9);
    --btn-bg: #0b0f0e; --btn-fg: #ffffff;
    --chip-bg: rgba(10,117,96,0.08); --chip-border: rgba(10,117,96,0.22);
    --hero-glow: radial-gradient(900px 480px at 80% -10%, rgba(90,210,180,0.30), transparent 65%);
    --focus: #0a7560;
  }
  html[data-theme="dark"] {
    --bg: #000000; --surface: #111413; --surface-2: #181c1b;
    --heading: #ffffff; --body: #c8d0cd; --faint: #8e8e93;
    --link: #5ad2b4; --accent: #5ad2b4; --mint: #5ad2b4; --orange: #ff9f0a; --orange-fill: #ff9f0a;
    --line: rgba(255,255,255,0.10); --card-border: rgba(255,255,255,0.08);
    --card-shadow: none;
    --nav-bg: rgba(0,0,0,0.82);
    --btn-bg: #ffffff; --btn-fg: #000000;
    --chip-bg: rgba(90,210,180,0.10); --chip-border: rgba(90,210,180,0.28);
    --hero-glow: radial-gradient(900px 480px at 80% -10%, rgba(90,210,180,0.22), transparent 65%);
    --focus: #5ad2b4;
  }
  * { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }
  body {
    margin: 0; background: var(--bg); color: var(--body);
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased;
  }
  a { color: var(--link); text-underline-offset: 3px; }
  a:hover { text-decoration-thickness: 2px; }
  :focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; border-radius: 6px; }
  .skip { position: absolute; left: -9999px; top: 8px; background: var(--surface); padding: 8px 14px; z-index: 50; }
  .skip:focus { left: 8px; }

  .nav {
    position: sticky; top: 0; z-index: 20; display: flex; align-items: center;
    justify-content: space-between; gap: 12px; padding: 12px 16px;
    background: var(--nav-bg); border-bottom: 1px solid var(--line);
    backdrop-filter: saturate(180%) blur(14px); -webkit-backdrop-filter: saturate(180%) blur(14px);
  }
  .brand { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 17px;
    letter-spacing: -0.3px; color: var(--heading); text-decoration: none; }
  .brand img { width: 30px; height: 30px; border-radius: 8px; box-shadow: 0 0 0 1px var(--line); }
  .navright { display: flex; align-items: center; gap: 6px; }
  .navlinks { display: none; gap: 4px; margin-right: 6px; }
  .navlinks a { font-weight: 600; font-size: 14px; text-decoration: none; padding: 6px 10px; border-radius: 999px; }
  .navlinks a[aria-current="page"] { background: var(--chip-bg); }
  .lang, .theme-btn {
    font: inherit; font-size: 13px; font-weight: 700; color: var(--link); text-decoration: none;
    background: var(--chip-bg); border: 1px solid var(--chip-border); border-radius: 999px;
    min-height: 36px; display: inline-flex; align-items: center; justify-content: center;
  }
  .lang { padding: 0 12px; }
  .theme-btn { width: 36px; padding: 0; cursor: pointer; font-size: 15px; }
  @media (min-width: 720px) { .nav { padding: 12px 28px; } .navlinks { display: flex; } }

  .hero { background: var(--hero-glow), var(--bg); border-bottom: 1px solid var(--line); }
  .hero-inner { max-width: 1080px; margin: 0 auto; padding: 44px 16px 48px; }
  .hero h1 { margin: 0 0 12px; color: var(--heading); font-size: 34px; line-height: 1.1;
    letter-spacing: -1px; font-weight: 800; text-wrap: balance; }
  .hero .subtitle { margin: 0; font-size: 17px; }
  .page-hero .hero-inner { max-width: 760px; text-align: center; }
  .page-hero .icon { width: 72px; height: 72px; border-radius: 17px; display: block; margin: 0 auto 16px;
    box-shadow: 0 0 0 1px var(--line); }

  .home-hero .hero-inner { display: grid; gap: 36px; align-items: center; }
  .eyebrow { display: inline-block; font-size: 13px; font-weight: 700; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--accent); margin: 0 0 14px; }
  .home-hero h1 { font-size: 38px; }
  .tagline { font-size: 18px; margin: 0 0 26px; max-width: 540px; }
  .cta { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 18px; }
  .storebadge { display: inline-flex; align-items: center; gap: 10px; background: var(--btn-bg);
    color: var(--btn-fg); border-radius: 12px; padding: 10px 18px; text-decoration: none; }
  .storebadge svg { width: 24px; height: 24px; fill: var(--btn-fg); }
  .storebadge .small { display: block; font-size: 11px; line-height: 1; opacity: 0.85; }
  .storebadge .big { display: block; font-size: 18px; font-weight: 700; line-height: 1.2; }
  .storebadge.soon { opacity: 0.8; cursor: default; }
  .cta .textlink { font-weight: 700; }
  .fineprint { font-size: 14px; color: var(--faint); margin: 16px 0 0; }

  .watch { justify-self: center; width: 220px; height: 266px; border-radius: 58px; background: #000;
    border: 9px solid #2a2d2c; box-shadow: 0 30px 60px rgba(0,0,0,0.35), inset 0 0 0 1px #3a3d3c;
    position: relative; }
  .watch::after { content: ""; position: absolute; right: -16px; top: 70px; width: 8px; height: 38px;
    border-radius: 4px; background: #2a2d2c; }
  .watch img { display: block; width: 100%; height: 100%; object-fit: cover; border-radius: 49px; }

  main { max-width: 1080px; margin: 0 auto; padding: 32px 16px 56px; }
  main.narrow { max-width: 760px; }
  .back { display: inline-block; margin-bottom: 20px; font-weight: 600; font-size: 14px; }

  .band { font-size: 18px; color: var(--heading); text-align: center; max-width: 820px;
    margin: 8px auto 36px; text-wrap: pretty; }
  .features { display: grid; gap: 16px; grid-template-columns: 1fr; }
  .card { background: var(--surface); border: 1px solid var(--card-border); border-radius: 20px;
    padding: 22px 20px; box-shadow: var(--card-shadow); }
  .feature h2 { font-size: 13px; font-weight: 800; letter-spacing: 1.6px; text-transform: uppercase;
    color: var(--accent); margin: 0 0 14px; }
  .feature ul { list-style: none; margin: 0; padding: 0; }
  .feature li { position: relative; padding: 0 0 12px 22px; font-size: 15px; }
  .feature li::before { content: ""; position: absolute; left: 0; top: 9px; width: 8px; height: 8px;
    border-radius: 50%; background: var(--mint); }

  .section-title { font-size: 26px; font-weight: 800; letter-spacing: -0.6px; color: var(--heading);
    margin: 48px 0 16px; text-align: center; }
  .tiers { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
  .tier h3 { margin: 0 0 6px; font-size: 16px; color: var(--heading); display: flex; align-items: center; gap: 8px; }
  .tier p { margin: 0; font-size: 15px; }
  .badge { display: inline-block; width: 10px; height: 10px; border-radius: 50%; flex: none; }
  .badge.live { background: var(--mint); }
  .badge.notify { background: var(--orange-fill); }
  .badge.off { background: #8e8e93; }
  .tiers-note { text-align: center; font-size: 14px; color: var(--faint); margin: 14px 0 0; }

  .shots-h { font-size: 13px; font-weight: 800; letter-spacing: 1.6px; text-transform: uppercase;
    color: var(--accent); margin: 26px 0 12px; }
  .shots { display: flex; gap: 18px; overflow-x: auto; scroll-snap-type: x mandatory; list-style: none;
    margin: 0 -16px; padding: 4px 16px 18px; scroll-padding-inline: 16px; scrollbar-width: thin; }
  .shots li { flex: none; scroll-snap-align: start; margin: 0; }
  .shots figure { margin: 0; text-align: center; }
  .shots img { display: block; height: auto; background: #000; }
  .shots.watch-shots img { width: 168px; border-radius: 38px; border: 7px solid #2a2d2c; }
  .shots.phone-shots img { width: 190px; border-radius: 26px; border: 1px solid var(--card-border);
    box-shadow: var(--card-shadow); }
  .shots figcaption { font-size: 14px; font-weight: 600; color: var(--heading); margin: 10px auto 0;
    max-width: 180px; line-height: 1.35; }

  .pricing { display: grid; gap: 20px; }
  .price-plan { font-size: 13px; font-weight: 800; letter-spacing: 1.6px; text-transform: uppercase;
    color: var(--accent); margin: 0 0 6px; }
  .price { font-size: 44px; font-weight: 800; letter-spacing: -1px; color: var(--heading); line-height: 1.1; margin: 0; }
  .price span { font-size: 18px; font-weight: 700; letter-spacing: 0; color: var(--body); }
  .price-trial { display: inline-block; margin: 10px 0 12px; font-size: 14px; font-weight: 700; color: var(--link);
    background: var(--chip-bg); border: 1px solid var(--chip-border); border-radius: 999px; padding: 4px 12px; }
  .price-sub { margin: 0; font-size: 14px; color: var(--faint); }
  .pricing ul { list-style: none; margin: 0; padding: 0; }
  .pricing li { position: relative; padding: 0 0 12px 26px; font-size: 15px; }
  .pricing li::before { content: "✓"; position: absolute; left: 0; top: 0; font-weight: 800; color: var(--accent); }
  .pricing .more { margin: 4px 0 0; font-weight: 700; font-size: 15px; }

  .helpbox { margin-top: 40px; text-align: center; }
  .helpbox p { margin: 0 0 6px; }

  .sec-h { font-size: 13px; font-weight: 800; letter-spacing: 1.6px; text-transform: uppercase;
    color: var(--accent); margin: 0 0 12px; }
  section.block { margin-bottom: 30px; }
  .faq { border-bottom: 1px solid var(--line); padding: 16px 0; }
  .faq:first-child { padding-top: 0; }
  .faq:last-child { border-bottom: 0; padding-bottom: 0; }
  .faq h3 { margin: 0 0 6px; font-size: 17px; line-height: 1.35; color: var(--heading); }
  .faq p, .faq li { font-size: 15px; }
  .faq p { margin: 0 0 8px; }
  .faq p:last-child { margin-bottom: 0; }
  .faq ul { margin: 4px 0 8px; padding-left: 20px; }
  .faq li { margin-bottom: 6px; }
  .contact .email-big { font-weight: 800; font-size: 19px; word-break: break-all; }
  .toc { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 26px; padding: 0; list-style: none; }
  .toc a { display: inline-block; font-size: 14px; font-weight: 600; text-decoration: none;
    padding: 6px 12px; border-radius: 999px; background: var(--chip-bg); border: 1px solid var(--chip-border); }
  .kbd { font-weight: 600; color: var(--heading); }

  .legal h2 { font-size: 19px; color: var(--heading); margin: 28px 0 8px; line-height: 1.3; }
  .legal h2:first-child { margin-top: 0; }
  .legal h3 { font-size: 16px; color: var(--heading); margin: 18px 0 6px; }
  .legal p { margin: 0 0 12px; }
  .legal ul { margin: 0 0 12px; padding-left: 20px; }
  .legal li { margin-bottom: 7px; }
  .legal .summary { background: var(--surface-2); border-radius: 14px; padding: 14px 16px; margin: 0 0 20px; }
  .legal .summary p:last-child, .legal .summary ul:last-child { margin-bottom: 0; }
  .legal .caps { text-transform: none; }
  .placeholder { background: rgba(255,159,10,0.18); border-radius: 4px; padding: 0 3px; }

  footer { border-top: 1px solid var(--line); text-align: center; color: var(--faint);
    font-size: 14px; padding: 28px 16px 48px; }
  footer .links a { margin: 0 8px; font-weight: 600; display: inline-block; padding: 4px 0; }
  footer .mail { display: inline-block; margin: 8px 0 10px; }
  footer .copy { font-size: 13px; margin: 0; }

  @media (min-width: 720px) {
    .hero-inner { padding: 64px 28px 68px; }
    .hero h1 { font-size: 42px; }
    .home-hero .hero-inner { grid-template-columns: 1.3fr 1fr; }
    .home-hero h1 { font-size: 52px; letter-spacing: -1.6px; }
    .features { grid-template-columns: 1fr 1fr; }
    .pricing { grid-template-columns: 260px 1fr; gap: 32px; align-items: start; }
    .shots { margin: 0; padding: 4px 0 18px; scroll-padding-inline: 0; }
    main { padding: 40px 28px 64px; }
    .card { padding: 26px 28px; }
  }
"""

HEAD_THEME = """<script>
(function(){
  var t = null;
  try { t = localStorage.getItem("wristalk_theme"); } catch (e) {}
  if (t !== "light" && t !== "dark")
    t = (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light";
  document.documentElement.setAttribute("data-theme", t);
})();
</script>"""

APPLE_LOGO = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8'
              '-1.41-.14-2.76.83-3.47.83-.72 0-1.82-.81-2.99-.79-1.54.02-2.96.9-3.75 2.27-1.6 2.78-.41 6.89 1.15 9.14.76 1.1'
              ' 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 1.24-.02 2.02-1.12 2.77-2.23.87-1.28 1.23'
              '-2.52 1.25-2.58-.03-.01-2.39-.92-2.41-3.66zM14.1 5.84c.63-.77 1.06-1.83.94-2.89-.91.04-2.02.61-2.67 1.37-.58.67'
              '-1.1 1.76-.96 2.8 1.02.08 2.06-.52 2.69-1.28z"/></svg>')


def email_link(cls="", keep_text=None):
    """A mailto link whose address is filled from SUPPORT_EMAIL (static fallback + JS constant)."""
    c = f' class="{cls}"' if cls else ""
    if keep_text:
        return f'<a{c} data-email data-keep-text href="mailto:{SUPPORT_EMAIL}">{keep_text}</a>'
    return f'<a{c} data-email href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>'


def store_badge(h):
    """App Store badge: a link once APP_STORE_LIVE is set, until then a "Coming soon" label without a link."""
    if APP_STORE_LIVE:
        return (f'<a class="storebadge" href="{APP_STORE_URL}">{APPLE_LOGO}<span><span class="small">'
                f'{h["badge_small"]}</span><span class="big">App Store</span></span></a>')
    return (f'<span class="storebadge soon">{APPLE_LOGO}<span><span class="small">{h["badge_soon"]}</span>'
            f'<span class="big">App Store</span></span></span>')


def fill(html, lang, page):
    """Replace %%TOKENS%% in content snippets with links relative to the current page."""
    here = out_path(lang, page)
    reps = {
        "%%EMAIL%%": email_link(),
        "%%HOME%%": rel(here, out_path(lang, "home")),
        "%%SUPPORT%%": rel(here, out_path(lang, "support")),
        "%%PRIVACY%%": rel(here, out_path(lang, "privacy")),
        "%%TERMS%%": rel(here, out_path(lang, "terms")),
        "%%COMPANY%%": COMPANY,
        "%%ADDRESS%%": COMPANY_ADDRESS,
        "%%JURISDICTION%%": JURISDICTION[lang],
        "%%EFFECTIVE%%": EFFECTIVE[lang],
    }
    for k, v in reps.items():
        html = html.replace(k, v)
    assert "%%" not in html, f"unreplaced token in {here}: {html[html.index('%%'):][:40]}"
    return html


def page_html(lang, page, title, description, body):
    c = CONTENT[lang]
    here = out_path(lang, page)
    icon = rel(here, "assets/icon.png")
    url = public_url(lang, page)
    other = "de" if lang == "en" else "en"
    nav_links = "".join(
        f'<a href="{rel(here, out_path(lang, p))}"{" aria-current=\"page\"" if p == page else ""}>{c.NAV[p]}</a>'
        for p in ("support", "privacy", "terms"))
    footer_links = " · ".join(
        (f'<a href="{rel(here, out_path(lang, p))}">{c.NAV[p]}</a>' if p != page else f'<span>{c.NAV[p]}</span>')
        for p in ("home", "support", "privacy", "terms"))
    alternates = "".join(
        f'\n<link rel="alternate" hreflang="{l}" href="{public_url(l, page)}">' for l in LANGS)
    alternates += f'\n<link rel="alternate" hreflang="x-default" href="{public_url("en", page)}">'
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#f5f7f6" media="(prefers-color-scheme: light)">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Wristalk">
<meta property="og:locale" content="{c.OG_LOCALE}">
<meta property="og:image" content="{SITE_URL}/assets/og-{lang}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{c.OG_IMAGE_ALT}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="48x48" href="{rel(here, "assets/favicon-48.png")}">
<link rel="icon" type="image/png" sizes="192x192" href="{rel(here, "assets/icon-192.png")}">
<link rel="apple-touch-icon" href="{rel(here, "assets/apple-touch-icon.png")}">{alternates}
<!-- Site-wide values. The support address is generated from SUPPORT_EMAIL in _build/gen_pages.py (see README.md). -->
<script>
const SUPPORT_EMAIL = "{SUPPORT_EMAIL}";
</script>
{HEAD_THEME}
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">{c.SKIP}</a>
<nav class="nav" aria-label="{c.NAV_LABEL}">
  <a class="brand" href="{rel(here, out_path(lang, "home"))}"><img src="{icon}" alt="" width="30" height="30"> Wristalk</a>
  <span class="navright">
    <span class="navlinks">{nav_links}</span>
    <a class="lang" href="{rel(here, out_path(other, page))}" hreflang="{other}" lang="{other}">{LANG_NAME[other]}</a>
    <button type="button" class="theme-btn" id="theme-toggle" aria-label="{c.THEME_LABEL}">☾</button>
  </span>
</nav>
{body}
<footer>
  <div class="links">{footer_links}</div>
  {email_link("mail")}
  <p class="copy">© 2026 {COMPANY}</p>
</footer>
<script>
(function(){{
  var links = document.querySelectorAll("[data-email]");
  for (var i = 0; i < links.length; i++) {{
    links[i].href = "mailto:" + SUPPORT_EMAIL;
    if (!links[i].hasAttribute("data-keep-text")) links[i].textContent = SUPPORT_EMAIL;
  }}
  var t = document.getElementById("theme-toggle");
  function icon() {{ t.textContent = document.documentElement.getAttribute("data-theme") === "dark" ? "☀" : "☾"; }}
  t.addEventListener("click", function(){{
    var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try {{ localStorage.setItem("wristalk_theme", next); }} catch (e) {{}}
    icon();
  }});
  icon();
}})();
</script>
</body>
</html>
"""


def shots_html(lang, kind, shots):
    """A horizontally scrolling row of screenshots (assets/screens/<lang>/<kind>-<file>.webp, see README.md)."""
    w, h = (168, 205) if kind == "watch" else (190, 413)
    here = out_path(lang, "home")
    items = "".join(
        f'<li><figure><img src="{rel(here, f"assets/screens/{lang}/{kind}-{f}.webp")}" width="{w}" height="{h}" '
        f'loading="lazy" decoding="async" alt="{alt}"><figcaption>{cap}</figcaption></figure></li>'
        for f, cap, alt in shots)
    return f'<ul class="shots {"watch" if kind == "watch" else "phone"}-shots">{items}</ul>'


def build_home(lang):
    c = CONTENT[lang]
    h = c.HOME
    pr = h["pricing"]
    features = "".join(
        f'<div class="card feature"><h2>{f["title"]}</h2><ul>' + "".join(f"<li>{i}</li>" for i in f["items"])
        + "</ul></div>" for f in h["features"])
    tiers = "".join(
        f'<div class="card tier"><h3><span class="badge {t["kind"]}" aria-hidden="true"></span>{t["title"]}</h3>'
        f'<p>{t["text"]}</p></div>' for t in h["tiers"])
    hero_img = rel(out_path(lang, "home"), f"assets/screens/{lang}/watch-02-receiving.webp")
    body = f"""
<header class="hero home-hero">
  <div class="hero-inner">
    <div>
      <p class="eyebrow">{h["eyebrow"]}</p>
      <h1>{h["h1"]}</h1>
      <p class="tagline">{h["tagline"]}</p>
      <div class="cta">
        {store_badge(h)}
        <a class="textlink" href="%%SUPPORT%%">{h["help_link"]} →</a>
      </div>
      <p class="fineprint">{h["fineprint"]}</p>
    </div>
    <div class="watch"><img src="{hero_img}" width="202" height="248" alt="{h["watch_alt"]}"></div>
  </div>
</header>
<main id="main">
  <p class="band">{h["band"]}</p>
  <div class="features">{features}</div>
  <h2 class="section-title" id="screens">{h["shots_title"]}</h2>
  <h3 class="shots-h">Apple Watch</h3>
  {shots_html(lang, "watch", h["watch_shots"])}
  <h3 class="shots-h">iPhone</h3>
  {shots_html(lang, "iphone", h["iphone_shots"])}
  <h2 class="section-title">{h["tiers_title"]}</h2>
  <div class="tiers">{tiers}</div>
  <p class="tiers-note">{h["tiers_note"]}</p>
  <h2 class="section-title" id="pricing">{pr["title"]}</h2>
  <div class="card pricing">
    <div>
      <p class="price-plan">Family Pass</p>
      <p class="price">{pr["price"]}<span>{pr["per"]}</span></p>
      <span class="price-trial">{pr["trial"]}</span>
      <p class="price-sub">{pr["sub"]}</p>
    </div>
    <div>
      <ul>{"".join(f"<li>{i}</li>" for i in pr["items"])}</ul>
      <p class="more"><a href="%%SUPPORT%%#pass">{pr["more"]} →</a></p>
    </div>
  </div>
  <div class="helpbox card">
    <p><strong>{h["help_title"]}</strong></p>
    <p>{h["help_text"]}</p>
  </div>
</main>"""
    return page_html(lang, "home", h["title"], h["description"], fill(body, lang, "home"))


def build_support(lang):
    c = CONTENT[lang]
    s = c.SUPPORT
    toc = "".join(f'<li><a href="#{sec["id"]}">{sec["title"]}</a></li>' for sec in s["sections"])
    secs = ""
    for sec in s["sections"]:
        faqs = "".join(f'<div class="faq"><h3>{q}</h3>{a}</div>' for q, a in sec["faqs"])
        secs += f'\n  <section class="block" id="{sec["id"]}" aria-labelledby="{sec["id"]}-h">' \
                f'<h2 class="sec-h" id="{sec["id"]}-h">{sec["title"]}</h2><div class="card">{faqs}</div></section>'
    body = f"""
<header class="hero page-hero">
  <div class="hero-inner">
    <img class="icon" src="%%ICON%%" alt="" width="72" height="72">
    <h1>{s["h1"]}</h1>
    <p class="subtitle">{s["subtitle"]}</p>
  </div>
</header>
<main id="main" class="narrow">
  <a class="back" href="%%HOME%%">{c.BACK_HOME}</a>
  <section class="block contact" id="contact" aria-labelledby="contact-h">
    <h2 class="sec-h" id="contact-h">{s["contact_title"]}</h2>
    <div class="card">
      <p style="margin:0 0 8px">{s["contact_text"]}</p>
      {email_link("email-big")}
      <p style="margin:10px 0 0;font-size:14px;color:var(--faint)">{s["contact_note"]}</p>
    </div>
  </section>
  <ul class="toc" aria-label="{s["toc_label"]}">{toc}</ul>{secs}
</main>"""
    body = body.replace("%%ICON%%", rel(out_path(lang, "support"), "assets/icon.png"))
    return page_html(lang, "support", s["title"], s["description"], fill(body, lang, "support"))


def build_legal(lang, page):
    c = CONTENT[lang]
    d = c.PRIVACY if page == "privacy" else c.TERMS
    body = f"""
<header class="hero page-hero">
  <div class="hero-inner">
    <img class="icon" src="%%ICON%%" alt="" width="72" height="72">
    <h1>{d["h1"]}</h1>
    <p class="subtitle">{d["subtitle"]}</p>
  </div>
</header>
<main id="main" class="narrow">
  <a class="back" href="%%SUPPORT%%">{c.BACK_SUPPORT}</a>
  <article class="card legal">
{d["body"]}
  </article>
</main>"""
    body = body.replace("%%ICON%%", rel(out_path(lang, page), "assets/icon.png"))
    return page_html(lang, page, d["title"], d["description"], fill(body, lang, page))


def main():
    builders = {"home": build_home, "support": build_support,
                "privacy": lambda l: build_legal(l, "privacy"), "terms": lambda l: build_legal(l, "terms")}
    for lang in LANGS:
        for page, build in builders.items():
            path = os.path.join(REPO, out_path(lang, page))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(build(lang))
            print("wrote", out_path(lang, page))


if __name__ == "__main__":
    main()
