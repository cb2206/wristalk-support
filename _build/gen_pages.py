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
SUPPORT_EMAIL = "hello@cbgroup.global"      # change again once the wristalk.app domain exists
APP_STORE_URL = "[APP STORE LINK]"           # App Store product URL once the app is live
COMPANY = "CB Group LLC"
COMPANY_ADDRESS = "1500 N Grant St, Ste #10470, Denver, CO 80203, USA"
# Governing law and venue, as it reads inside a sentence in each language.
JURISDICTION = {"en": "the State of Colorado, USA", "de": "des Bundesstaats Colorado, USA"}

LANGS = {"en": "", "de": "de/"}              # language -> folder prefix
PAGES = {"home": "index.html", "support": "support/index.html",
         "privacy": "privacy.html", "terms": "terms.html"}
CONTENT = {"en": content_en, "de": content_de}
LANG_NAME = {"en": "English", "de": "Deutsch"}


def out_path(lang, page):
    return LANGS[lang] + PAGES[page]


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
  .brand img { width: 30px; height: 30px; border-radius: 8px; }
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
  .page-hero .icon { width: 72px; height: 72px; border-radius: 17px; display: block; margin: 0 auto 16px; }

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

  .watch { justify-self: center; width: 220px; height: 262px; border-radius: 58px; background: #000;
    border: 9px solid #2a2d2c; box-shadow: 0 30px 60px rgba(0,0,0,0.35), inset 0 0 0 1px #3a3d3c;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px;
    color: #fff; position: relative; }
  .watch::after { content: ""; position: absolute; right: -16px; top: 70px; width: 8px; height: 38px;
    border-radius: 4px; background: #2a2d2c; }
  .watch .who { font-weight: 700; font-size: 17px; display: flex; align-items: center; gap: 7px; }
  .watch .dot { width: 9px; height: 9px; border-radius: 50%; background: #5ad2b4; box-shadow: 0 0 10px #5ad2b4; }
  .watch .ptt { width: 112px; height: 112px; border-radius: 50%; background: #5ad2b4;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 0 0 10px rgba(90,210,180,0.16), 0 0 0 22px rgba(90,210,180,0.07); }
  .watch .ptt svg { width: 44px; height: 44px; fill: #000; }
  .watch .hint { font-size: 12px; color: #8e8e93; font-weight: 600; }

  main { max-width: 1080px; margin: 0 auto; padding: 32px 16px 56px; }
  main.narrow { max-width: 760px; }
  .back { display: inline-block; margin-bottom: 20px; font-weight: 600; font-size: 14px; }

  .band { font-size: 18px; color: var(--heading); text-align: center; max-width: 820px;
    margin: 8px auto 36px; text-wrap: pretty; }
  .features { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
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
MIC = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 14a3 3 0 0 0 3-3V5a3 3 0 0 0-6 0v6a3 3 0 0 0 3 3zm5-3a5 5 0 0 1-10 0H5a7'
       ' 7 0 0 0 6 6.92V21h2v-3.08A7 7 0 0 0 19 11h-2z"/></svg>')


def email_link(cls="", keep_text=None):
    """A mailto link whose address is filled from SUPPORT_EMAIL (static fallback + JS constant)."""
    c = f' class="{cls}"' if cls else ""
    if keep_text:
        return f'<a{c} data-email data-keep-text href="mailto:{SUPPORT_EMAIL}">{keep_text}</a>'
    return f'<a{c} data-email href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>'


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
    }
    for k, v in reps.items():
        html = html.replace(k, v)
    assert "%%" not in html, f"unreplaced token in {here}: {html[html.index('%%'):][:40]}"
    return html


def page_html(lang, page, title, description, body):
    c = CONTENT[lang]
    here = out_path(lang, page)
    icon = rel(here, "assets/icon.png")
    other = "de" if lang == "en" else "en"
    nav_links = "".join(
        f'<a href="{rel(here, out_path(lang, p))}"{" aria-current=\"page\"" if p == page else ""}>{c.NAV[p]}</a>'
        for p in ("support", "privacy", "terms"))
    footer_links = " · ".join(
        (f'<a href="{rel(here, out_path(lang, p))}">{c.NAV[p]}</a>' if p != page else f'<span>{c.NAV[p]}</span>')
        for p in ("home", "support", "privacy", "terms"))
    alternates = "".join(
        f'\n<link rel="alternate" hreflang="{l}" href="{rel(here, out_path(l, page))}">' for l in LANGS)
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
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="{icon}">
<link rel="apple-touch-icon" href="{icon}">{alternates}
<!-- Site-wide values. The support address is generated from SUPPORT_EMAIL in _build/gen_pages.py (see README.md). -->
<script>
const SUPPORT_EMAIL = "{SUPPORT_EMAIL}";
const APP_STORE_URL = "{APP_STORE_URL}";
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
  var badges = document.querySelectorAll("[data-appstore]");
  for (var j = 0; j < badges.length; j++) {{
    var b = badges[j];
    if (/^\\[/.test(APP_STORE_URL)) {{
      b.removeAttribute("href"); b.setAttribute("aria-disabled", "true"); b.classList.add("soon");
      var s = b.querySelector(".small"); if (s) s.textContent = b.getAttribute("data-soon");
    }} else {{ b.href = APP_STORE_URL; }}
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


def build_home(lang):
    c = CONTENT[lang]
    h = c.HOME
    features = "".join(
        f'<div class="card feature"><h2>{f["title"]}</h2><ul>' + "".join(f"<li>{i}</li>" for i in f["items"])
        + "</ul></div>" for f in h["features"])
    tiers = "".join(
        f'<div class="card tier"><h3><span class="badge {t["kind"]}" aria-hidden="true"></span>{t["title"]}</h3>'
        f'<p>{t["text"]}</p></div>' for t in h["tiers"])
    body = f"""
<header class="hero home-hero">
  <div class="hero-inner">
    <div>
      <p class="eyebrow">{h["eyebrow"]}</p>
      <h1>{h["h1"]}</h1>
      <p class="tagline">{h["tagline"]}</p>
      <div class="cta">
        <a class="storebadge" data-appstore data-soon="{h["badge_soon"]}" href="{APP_STORE_URL}">
          {APPLE_LOGO}<span><span class="small">{h["badge_small"]}</span><span class="big">App Store</span></span>
        </a>
        <a class="textlink" href="%%SUPPORT%%">{h["help_link"]} →</a>
      </div>
      <p class="fineprint">{h["fineprint"]}</p>
    </div>
    <div class="watch" role="img" aria-label="{h["watch_alt"]}">
      <div class="who"><span class="dot"></span>{h["watch_name"]}</div>
      <div class="ptt">{MIC}</div>
      <div class="hint">{h["watch_hint"]}</div>
    </div>
  </div>
</header>
<main id="main">
  <p class="band">{h["band"]}</p>
  <div class="features">{features}</div>
  <h2 class="section-title">{h["tiers_title"]}</h2>
  <div class="tiers">{tiers}</div>
  <p class="tiers-note">{h["tiers_note"]}</p>
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
