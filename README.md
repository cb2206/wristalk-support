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
/opt/homebrew/bin/python3.12 _build/gen_pages.py
```

(Python 3.12 or later; the system Python 3.9 can't run it.)

## Site-wide values and placeholders

Set at the top of `_build/gen_pages.py`, then regenerate:

| Constant | Current value | Notes |
|---|---|---|
| `SUPPORT_EMAIL` | `hello@wristalk.app` | Cloudflare Email Routing forwards it to the owner. Each page also carries it as `const SUPPORT_EMAIL` at the top of `<head>`; a script fills every `[data-email]` link from it. |
| `SITE_URL` | `https://wristalk.app` | Absolute URLs for canonical, hreflang and Open Graph tags. |
| `APP_STORE_URL` | `https://apps.apple.com/us/app/wristalk/id6816532048` | The App Store product page (live only after release). |
| `APP_STORE_LIVE` | `False` | **Release switch.** While `False`, the badge reads "Coming soon to the App Store" without a link. After release set it to `True` and regenerate: the badge links to `APP_STORE_URL`. |
| `COMPANY_ADDRESS` | 1500 N Grant St, Ste #10470, Denver, CO 80203, USA | Used in privacy policy and terms. |
| `JURISDICTION` | the State of Colorado, USA | Governing law and venue (terms §13), per language. |

## Images

| File | What | Made from |
|---|---|---|
| `assets/icon.png` (512), `icon-192.png`, `apple-touch-icon.png` (180), `favicon-48.png` | Logo, favicons | Wristalk repo `apps/Shared/Assets.xcassets/AppIcon.appiconset/icon-ios-1024.png` (`scripts/render-app-icon.swift`), resized with `sips -z` |
| `assets/og-en.jpg`, `assets/og-de.jpg` (1200×630) | Open Graph / link preview image | The icon plus name and subtitle, drawn with AppKit |
| `assets/screens/<en\|de>/watch-*.webp`, `iphone-*.webp` | Screenshots on the product page | Wristalk repo `docs/release/app-store/screenshots/<lang>/watch` (422 px wide, as is) and `iphone-6.9` (resized to 480 px wide), converted with `cwebp -q 80` |

When the App Store screenshots change, regenerate the WebP files with the same names, per language:

```bash
SRC=../Wristalk/docs/release/app-store/screenshots
for l in en de; do
  for f in $SRC/$l/iphone-6.9/*.png; do sips --resampleWidth 480 "$f" --out /tmp/s.png >/dev/null; cwebp -quiet -q 80 /tmp/s.png -o assets/screens/$l/iphone-$(basename "$f" .png).webp; done
  for f in $SRC/$l/watch/*.png; do cwebp -quiet -q 82 "$f" -o assets/screens/$l/watch-$(basename "$f" .png).webp; done
done
```

Captions and alt texts are in `HOME["watch_shots"]` / `HOME["iphone_shots"]` of each content file.

## Keep in sync with the app

The texts follow the app's ADRs (delivery tiers, end-to-end encryption, retention), the App Store privacy label and
the server's retention rules, the Family Pass paywall (`apps/iPhone/Sources/UI/Onboarding/FamilyPass.swift`) and
the App Store text (`docs/release/app-store/metadata.md`). When those change — supported watch models, retention
times, the Family Pass price or model, in-app menu names — update both languages here and change the effective date on the privacy policy and terms.
