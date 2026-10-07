// wristalk.app — static site (Workers static assets) plus the few dynamic paths:
//   /.well-known/apple-app-site-association  universal links for invite URLs (same content as the relay's route,
//                                            Wristalk server/src/routes/wellknown.ts; Apple's CDN fetches it here)
//   /join/XXXX-XXXX                          invite landing page when the app is not installed / link opened on a Mac
//   www.wristalk.app                         → 301 to the apex
// Everything else is served from the static files (html_handling "auto-trailing-slash": /terms → terms.html).

const TEAM_ID = "K2LM9FSU6C";
const AASA = {
  applinks: {
    details: [
      {
        appIDs: [`${TEAM_ID}.com.cbgroup.wristalk`, `${TEAM_ID}.com.cbgroup.wristalk.watchkitapp`],
        components: [{ "/": "/join/*", comment: "Invite codes (wristalk.app/join/XXXX-XXXX)" }],
      },
    ],
  },
};

// Invite alphabet (server/src/invites): 2–9 and A–Z without I, O. Lenient: case-insensitive, hyphen optional.
const CODE = /^([2-9A-HJ-NP-Z]{4})-?([2-9A-HJ-NP-Z]{4})$/;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname.startsWith("www.")) {
      url.hostname = url.hostname.slice(4);
      return Response.redirect(url.toString(), 301);
    }
    if (url.pathname === "/.well-known/apple-app-site-association") {
      return new Response(JSON.stringify(AASA), {
        headers: { "Content-Type": "application/json", "Cache-Control": "public, max-age=3600" },
      });
    }
    if (url.pathname.startsWith("/join/")) {
      const m = CODE.exec(decodeURIComponent(url.pathname.slice(6)).replace(/\/$/, "").toUpperCase());
      return joinPage(m ? `${m[1]}-${m[2]}` : null);
    }
    return env.ASSETS.fetch(request);
  },
};

function joinPage(code) {
  const deep = code ? `wristalk://join/${code}` : null;
  const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wristalk invite</title><meta name="robots" content="noindex">
<link rel="icon" href="/assets/icon.png">
<style>
:root{--bg:#fff;--fg:#1d1d1f;--muted:#6e6e73;--accent:#ff9f0a;--card:#f5f5f7}
@media (prefers-color-scheme:dark){:root{--bg:#000;--fg:#f5f5f7;--muted:#a1a1a6;--card:#1c1c1e}}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.5 -apple-system,BlinkMacSystemFont,"Helvetica Neue",sans-serif}
main{max-width:30rem;margin:0 auto;padding:3rem 1rem;text-align:center}
img{width:96px;height:96px;border-radius:22px}
.code{font:600 2rem ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.08em;background:var(--card);border-radius:12px;padding:.6rem 1rem;display:inline-block;margin:1rem 0}
a.button{display:inline-block;background:var(--accent);color:#000;text-decoration:none;font-weight:600;border-radius:999px;padding:.7rem 1.4rem;margin:.5rem 0}
p{color:var(--muted)}
</style></head><body><main>
<img src="/assets/icon.png" alt="Wristalk">
${code
    ? `<h1>You're invited to Wristalk</h1>
<div class="code">${code}</div>
<p><a class="button" href="${deep}">Open in Wristalk</a></p>
<p>No Wristalk yet? Get it from the App Store, then enter this code: on iPhone with “Accept invite”, on Apple Watch with “Enter code”.</p>
<p lang="de">Du bist zu Wristalk eingeladen. Öffne Wristalk auf dem iPhone oder der Apple Watch und gib diesen Code ein.</p>`
    : `<h1>This invite link looks incomplete</h1><p>Ask the sender for the 8-character code and enter it in Wristalk.</p>`}
<p><a href="/">wristalk.app</a></p>
</main></body></html>`;
  return new Response(html, {
    status: code ? 200 : 404,
    headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store", "X-Robots-Tag": "noindex" },
  });
}
