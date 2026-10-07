# Wristalk support site

Public support, privacy and terms pages for **Wristalk** (push-to-talk for Apple Watch and iPhone, by CB Group LLC).
Static HTML served at **<https://wristalk.app>** by the Cloudflare Worker `wristalk-site` (`wrangler.jsonc`,
`worker/index.js`: universal-link file, `/join/<code>` invite page, www → apex). Deploy: `npx wrangler deploy`.
GitHub Pages (<https://cb2206.github.io/wristalk-support/>) still serves a copy from `main`.

| Page | English | German |
|---|---|---|
| Product page | `index.html` | `de/index.html` |
| Support / FAQ | `support/index.html` | `de/support/index.html` |
| Privacy policy | `privacy.html` | `de/privacy.html` |
| Terms of use | `terms.html` | `de/terms.html` |

All internal links are relative, so the site works under `/wristalk-support/` and on a custom domain later.
No build step is needed to view it — open any `.html` file or the Pages URL.

## Editing

The HTML is **generated**. Edit the sources, then regenerate and commit the HTML:

- `_build/content_en.py`, `_build/content_de.py` — all page text (small HTML snippets).
- `_build/gen_pages.py` — shared layout, CSS, and the site-wide values below.

```bash
python3 _build/gen_pages.py
```

## Site-wide values and placeholders

Set at the top of `_build/gen_pages.py`, then regenerate:

| Constant | Current value | Notes |
|---|---|---|
| `SUPPORT_EMAIL` | `hello@wristalk.app` | Cloudflare Email Routing forwards it to the owner. Each page also carries it as `const SUPPORT_EMAIL` at the top of `<head>`; a script fills every `[data-email]` link from it. |
| `APP_STORE_URL` | `[APP STORE LINK]` | **Placeholder.** While it starts with `[`, the App Store badge renders as "Coming soon" without a link. Put the App Store product URL here after release. |
| `COMPANY_ADDRESS` | 1500 N Grant St, Ste #10470, Denver, CO 80203, USA | Used in privacy policy and terms. |
| `JURISDICTION` | the State of Colorado, USA | Governing law and venue (terms §13), per language. |

Quick replacement without Python (for example the App Store link), from the repo root:

```bash
grep -rl '\[APP STORE LINK\]' --include='*.html' --include='*.py' . | xargs sed -i '' 's#\[APP STORE LINK\]#https://apps.apple.com/app/id6816532048#g'
```

(Prefer editing the constant and regenerating so the sources and HTML stay in sync.)

## Keep in sync with the app

The texts follow the app's ADRs (delivery tiers, end-to-end encryption, retention), the App Store privacy label and
the server's retention rules. When those change — supported watch models, retention times, the Family Pass model,
in-app menu names — update both languages here and change the effective date on the privacy policy and terms.
