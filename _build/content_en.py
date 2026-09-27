"""English page text for the Wristalk support site. Tokens like %%SUPPORT%% are filled by gen_pages.py."""

SKIP = "Skip to content"
NAV_LABEL = "Main"
THEME_LABEL = "Switch light / dark appearance"
NAV = {"home": "Wristalk", "support": "Support", "privacy": "Privacy", "terms": "Terms"}
BACK_HOME = "← Back to Wristalk"
BACK_SUPPORT = "← Back to Support"

# ---------------------------------------------------------------------------
HOME = {
    "title": "Wristalk — Walkie-talkie for your family",
    "description": "Live push-to-talk for families on Apple Watch and iPhone. Works on kids' Family Setup watches "
                   "without an iPhone. Parental controls, end-to-end encrypted.",
    "eyebrow": "For Apple Watch and iPhone",
    "h1": "The walkie-talkie is back on your wrist.",
    "tagline": "Hold the talk button and speak. On your family's watches your voice plays right away, no tap "
               "needed — like a real walkie-talkie. Let go, and they can answer.",
    "badge_small": "Download on the",
    "badge_soon": "Coming soon to the",
    "help_link": "Help &amp; FAQ",
    "fineprint": "Free to download. Try the Family Pass free for one week, then it renews yearly.",
    "watch_alt": "Illustration of an Apple Watch showing a large talk button",
    "watch_name": "Mum",
    "watch_hint": "Hold to talk",
    "band": "Made for families: kids' Apple Watch with Family Setup work without an iPhone of their own, and "
            "parents decide who a child can talk to.",
    "features": [
        {"title": "Made for families", "items": [
            "Works on kids' Apple Watch with Family Setup — no iPhone of their own needed.",
            "Parents decide who a child can talk to. New contacts and groups need a parent's approval, and "
            "parents can change their mind at any time.",
            "Talk one-to-one or in groups: the whole family, just the kids, grandparents, or friends from "
            "another family.",
        ]},
        {"title": "Live when it matters", "items": [
            "Turn Wristalk on and incoming voice plays automatically on supported watches — no tap needed.",
            "On other watches, Wristalk plays live through Bluetooth headphones, or sends a notification you "
            "tap to listen.",
            "A battery guard and an auto-off timer keep kids' watches going through the day.",
        ]},
        {"title": "Private by design", "items": [
            "Every voice message is end-to-end encrypted. Only the people in the conversation can hear it — "
            "not us, not anyone else.",
            "Messages disappear once they have been played, or after 10 minutes at the latest. If someone "
            "missed you, you're told.",
            "Sign in with Apple. No email address, no phone number, no ads, no tracking.",
        ]},
        {"title": "On iPhone, too", "items": [
            "The iPhone app is the comfortable place to manage people, groups and kids' settings.",
            "It is a walkie-talkie of its own, with the system Push to Talk controls — so parents without a "
            "watch can talk too.",
            "Invite people with a code via Messages or a QR code.",
        ]},
        {"title": "One pass for the whole family", "items": [
            "Free to download, with one week of the Family Pass free.",
            "After that, the Family Pass is a yearly subscription, billed by Apple.",
            "It is shared with your Apple family through Family Sharing, and you can cancel any time in your "
            "App Store settings.",
        ]},
    ],
    "tiers_title": "Which Apple Watch?",
    "tiers": [
        {"kind": "live", "title": "Live through the speaker",
         "text": "Apple Watch SE (3rd generation), Series 10, 11 and 12, Ultra 2, 3 and 4. With Wristalk on, "
                 "voice plays automatically."},
        {"kind": "notify", "title": "Notifications or headphones",
         "text": "Other watches with watchOS 26, such as Apple Watch SE (2nd generation) and Series 6 to 8. "
                 "The full app works; messages play live with Bluetooth headphones, otherwise you tap a "
                 "notification to listen."},
        {"kind": "off", "title": "Not supported",
         "text": "Watches that can't run watchOS 26."},
    ],
    "tiers_note": "Each watch or iPhone needs an internet connection (Wi-Fi or cellular). iPhone: iOS 26 or later.",
    "help_title": "Questions?",
    "help_text": 'Read the <a href="%%SUPPORT%%">support page</a> or write to %%EMAIL%%.',
}

# ---------------------------------------------------------------------------
SUPPORT = {
    "title": "Wristalk — Support",
    "description": "Help and answers for Wristalk, the walkie-talkie for families on Apple Watch and iPhone.",
    "h1": "Wristalk Support",
    "subtitle": "Help &amp; answers",
    "contact_title": "Contact",
    "contact_text": "Questions, problems, or something to report? Email us and we'll get back to you.",
    "contact_note": "Please include your watch or iPhone model and, if it's about a message, roughly when it "
                    "happened. Never send us passwords or payment details.",
    "toc_label": "Topics",
    "sections": [
        {"id": "start", "title": "Getting started", "faqs": [
            ("What is Wristalk?",
             "<p>Wristalk is a walkie-talkie for families on Apple Watch and iPhone. Hold the talk button, "
             "speak, and let go — the people in the conversation hear you right away. You can talk one-to-one "
             "or in groups, and parents decide who their children can talk to.</p>"),
            ("What do I need?",
             "<ul><li>An Apple Watch with watchOS 26 or later, or an iPhone with iOS 26 or later.</li>"
             "<li>An internet connection on each watch or iPhone (Wi-Fi or cellular).</li>"
             "<li>An Apple Account to Sign in with Apple. Wristalk doesn't ask for an email address or "
             "phone number.</li></ul>"
             "<p>The iPhone app is optional: it's the comfortable place to manage people, groups and kids' "
             "settings, but everything also works on the watch.</p>"),
            ("Which Apple Watch models are supported?",
             "<ul><li><strong>Live through the speaker:</strong> Apple Watch SE (3rd generation), Series 10, "
             "11 and 12, Ultra 2, 3 and 4. While Wristalk is on, incoming voice plays automatically.</li>"
             "<li><strong>With notifications or headphones:</strong> Apple Watch SE (2nd generation), "
             "Series 6, 7 and 8, and other models that run watchOS 26. The full app works. Messages play "
             "live while Wristalk is open on screen, or with Bluetooth headphones connected; otherwise you "
             "get a notification and tap it to listen.</li>"
             "<li><strong>Not supported:</strong> watches that can't run watchOS 26.</li></ul>"),
            ("Does my child need an iPhone?",
             "<p>No. The watch app is complete on its own and works on Apple Watch set up with Family Setup. "
             "Install Wristalk from the App Store on the watch, sign in with the child's Apple Account, and "
             "join your family with an invite code. You manage your child's settings from your own iPhone "
             "or watch.</p>"),
        ]},
        {"id": "people", "title": "Contacts &amp; approvals", "faqs": [
            ("How do I invite someone?",
             "<p>Create an invite code in Wristalk. On iPhone you can send it via Messages or show it as a QR "
             "code; on the watch you can share it via Messages or Mail, or show it large on screen so the "
             "other person can type it in.</p>"
             "<p>A code has 8 characters, works once and is valid for 48 hours. The other person opens the "
             "link on their iPhone or enters the code in Wristalk (on the watch: <span class=\"kbd\">Enter "
             "code</span> or <span class=\"kbd\">I have a code</span>).</p>"),
            ("How do approvals work for children?",
             "<p>Every child in Wristalk has one or more guardians — the adults who look after their "
             "settings. By default, when a child wants to invite someone, accept an invite or create a "
             "group, it becomes a request to the guardians. A new device for a child needs a guardian's "
             "approval too.</p>"
             "<p>Guardians get a notification on their watch and iPhone with Approve and Deny buttons. "
             "Pending requests are also listed on iPhone under <span class=\"kbd\">Kids → Approvals</span> "
             "and on the watch under <span class=\"kbd\">Requests</span>. The child can see who approved "
             "what.</p>"
             "<p>For each child, guardians can choose whether they may invite new people, accept invites and "
             "create groups (never, with approval, or freely), who can add them to groups, and at which "
             "hours Wristalk may play messages.</p>"),
            ("Can we talk with people outside our family?",
             "<p>Yes. Contacts can come from other families — friends, grandparents, neighbours. For "
             "children, each new contact needs a guardian's approval unless the guardian has allowed "
             "otherwise.</p>"),
        ]},
        {"id": "talking", "title": "Talking &amp; delivery", "faqs": [
            ("How do I talk?",
             "<p>Open a contact or group, hold the big talk button, speak, and let go. A short sound and "
             "haptic tell you when you can speak. One person talks at a time; a talk lasts up to 30 seconds. "
             "If you prefer, turn on tap to talk (tap once to start, once to stop).</p>"),
            ("Why do I sometimes have to tap a notification to hear a message?",
             "<p>Apple Watch only lets an app receive voice live while that app is actively playing audio. "
             "When you switch <span class=\"kbd\">Wristalk on</span> on a supported watch, Wristalk stays "
             "ready and plays incoming voice automatically.</p>"
             "<p>In these cases Wristalk uses <strong>notify</strong> mode instead — you get a notification "
             "that someone is talking, and you tap it to listen:</p>"
             "<ul><li>Wristalk is switched off, or the auto-off timer has ended.</li>"
             "<li>The battery guard switched to notifications because the battery is low.</li>"
             "<li>The watch can't play in the background through its speaker (older models) and no "
             "headphones are connected.</li>"
             "<li><span class=\"kbd\">Notify instead</span> is chosen under Settings → Delivery.</li>"
             "<li>On a child's watch: it's outside the allowed hours a guardian has set.</li></ul>"
             "<p>After you tap and listen, Wristalk plays live again while it stays active.</p>"),
            ("What happens if someone misses my message?",
             "<p>A message is kept, encrypted, until everyone has played it — for 10 minutes at the latest "
             "(or 1 hour or 24 hours, if the person who created the group chose a longer time). If someone "
             "didn't hear it in time, you get a notification that they didn't hear your message, and they "
             "see a “missed” marker in the conversation.</p>"),
            ("What do the battery guard and auto-off timer do?",
             "<p>Playing live keeps the watch listening, which uses more battery. The "
             "<strong>battery guard</strong> switches from auto-play to notifications when the battery drops "
             "below a level you choose (20 % by default); charging pauses the guard. The "
             "<strong>auto-off timer</strong> turns Wristalk off after 2 hours, 4 hours or tonight.</p>"
             "<p>You find both in the watch's Settings. On a child's watch, the guardian sets the battery "
             "guard (on iPhone under Kids).</p>"),
        ]},
        {"id": "pass", "title": "Family Pass", "faqs": [
            ("How much does Wristalk cost?",
             "<p>Wristalk is free to download. To talk, your family needs the <strong>Family Pass</strong>: "
             "the first week is free, then it's a yearly subscription that renews automatically. The price "
             "is shown in the App Store in your currency before you confirm.</p>"),
            ("Does everyone in the family have to buy it?",
             "<p>No. The Family Pass supports Apple's Family Sharing, so the members of your Apple family "
             "group get it without buying it again (subscription sharing must be turned on in your Family "
             "Sharing settings).</p>"),
            ("How do I cancel the subscription?",
             "<p>Apple handles the subscription. On iPhone, open <span class=\"kbd\">Settings → [your name] → "
             "Subscriptions → Wristalk</span> and tap Cancel Subscription — or in Wristalk on iPhone, go to "
             "<span class=\"kbd\">Settings → Family Pass → Manage subscription</span>.</p>"
             "<p>Cancel at least 24 hours before the renewal date to avoid being charged for the next year. "
             "You keep the Family Pass until the end of the period you paid for. Only the person who bought "
             "it can cancel it, and deleting the app does not cancel it. If you cancel during the free week, "
             "access may end right away.</p>"),
            ("Can I get a refund?",
             "<p>Because Apple processes all payments, refunds are handled by Apple. Request one at "
             "<a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>.</p>"),
            ("I have the Family Pass, but Wristalk doesn't recognise it.",
             "<p>Make sure you're signed in to the App Store with the Apple Account that bought it (or one in "
             "the same Apple family), then tap <span class=\"kbd\">Restore purchases</span> on the Family "
             "Pass screen. If that doesn't help, email us.</p>"),
        ]},
        {"id": "privacy", "title": "Privacy &amp; safety", "faqs": [
            ("Can you listen to our messages?",
             "<p>No. Voice is encrypted on your devices before it leaves them, and only the devices of the "
             "people in the conversation have the keys. Our server only passes on and briefly stores "
             "encrypted data. To check that nobody swapped a key, compare the <strong>safety number</strong> "
             "with a contact: on iPhone under People, on the watch in the conversation details "
             "(<span class=\"kbd\">Show safety number</span>).</p>"
             "<p>What our server does see — for example who talks to whom and when — is explained in the "
             "<a href=\"%%PRIVACY%%\">privacy policy</a>.</p>"),
            ("How do I delete my data?",
             "<ul><li><strong>iPhone:</strong> Settings → Privacy → <span class=\"kbd\">Delete my "
             "account…</span></li>"
             "<li><strong>Watch:</strong> Settings → Privacy → <span class=\"kbd\">Delete my data</span></li>"
             "<li><strong>For a child (guardians):</strong> on iPhone, Kids → the child → "
             "<span class=\"kbd\">Delete all of [name]'s data…</span></li></ul>"
             "<p>Your profile, contacts, group memberships and devices are removed right away; the remaining "
             "records are erased within 30 days. If you are the last guardian of a child, delete the child's "
             "data first. Deleting your account does not cancel the Family Pass — cancel it in your App Store "
             "settings.</p>"),
            ("How do I report someone?",
             "<p>If someone makes you or your child uncomfortable or misuses Wristalk, report it to us — with "
             "Report in the app, or by email to %%EMAIL%% with the person's display name, the conversation "
             "and roughly when it happened. Because voice is end-to-end encrypted, we can't listen to "
             "messages; we act on your report and on the information our server has (such as who talked to "
             "whom and when). Reports are kept for 90 days.</p>"
             "<p>You can leave a group at any time, and guardians decide which contacts a child has. If "
             "someone is in danger, contact your local emergency services first.</p>"),
        ]},
    ],
}

# ---------------------------------------------------------------------------
PRIVACY = {
    "title": "Wristalk — Privacy Policy",
    "description": "How Wristalk handles your data: end-to-end encrypted voice, minimal data, no tracking.",
    "h1": "Privacy Policy",
    "subtitle": "Wristalk · Effective September 27, 2026",
    "body": """
<div class="summary">
  <p><strong>The short version</strong></p>
  <ul>
    <li>Your voice messages are end-to-end encrypted. We cannot listen to them.</li>
    <li>Encrypted messages are deleted once everyone has played them — after 10 minutes at the latest, unless a
      group uses a longer setting (at most 24 hours).</li>
    <li>We store only what Wristalk needs to work: your Apple user ID, a display name, your devices' public keys,
      who is in your family, contacts and groups, and for 30 days who talked with whom and when.</li>
    <li>No ads, no tracking, no analytics, no selling of data.</li>
  </ul>
</div>

<h2>1. Who is responsible</h2>
<p>Wristalk is provided by %%COMPANY%%, %%ADDRESS%% (“we”, “us”). We are the controller of the personal data
described here. Contact: %%EMAIL%%.</p>

<h2>2. Data we store and why</h2>
<ul>
  <li><strong>Account identifier.</strong> The user identifier from Sign in with Apple and an internal user ID.
    We ask Apple for your name only — not for your email address.</li>
  <li><strong>Display name.</strong> Your given name from Sign in with Apple, or a name you type. It is shown to your
    contacts.</li>
  <li><strong>Device data.</strong> An app-generated device ID, your devices' public encryption keys, and push
    notification tokens so we can notify your watch or iPhone. We don't use advertising identifiers.</li>
  <li><strong>Family, contact and group structure.</strong> Your family, contacts and groups (names and members),
    invites, guardian relationships, parental-control settings, and approval requests and decisions.</li>
  <li><strong>Talk metadata.</strong> For each message: sender, conversation, start and end time, and whether each
    recipient received or played it. We need this to deliver messages, tell senders when someone missed them, and
    handle abuse. It is deleted after 30 days.</li>
  <li><strong>Encrypted voice messages.</strong> Stored only as encrypted data we cannot read, until every recipient
    has played the message — after 10 minutes at the latest, or after the conversation's longer setting
    (1 hour or 24 hours) if its creator chose one.</li>
  <li><strong>Reports.</strong> If you report someone, we keep the report and the information needed to review it
    for 90 days.</li>
  <li><strong>Subscription status.</strong> When you buy or restore the Family Pass, the app sends us Apple's signed
    transaction information (product, dates, whether it is a trial) so we can unlock Wristalk for your family. We never
    receive your payment details.</li>
  <li><strong>Technical data.</strong> Your IP address is processed when your device connects, to deliver the
    service and limit abuse (rate limiting). Rate-limit records are deleted within 2 days. Our server logs contain no
    voice content.</li>
</ul>

<h2>3. What we cannot see</h2>
<p>Voice is encrypted on your device before it is sent, with keys that exist only on the devices of the people in
the conversation. Our server passes on and briefly stores this encrypted data, but cannot decrypt it — so we cannot
listen to, transcribe or analyse what you say.</p>
<p>To deliver messages, our server does see who is in which family, contact list and group, who talks to whom, when
and for how long, and the size of the data. Push notifications contain the sender's display name and a
conversation reference, never voice content.</p>

<h2>4. No tracking, ads or analytics</h2>
<p>Wristalk contains no advertising, no analytics and no third-party tracking SDKs. We do not sell or share your data
for advertising, and we do not build profiles about you. The app keeps a technical log on your device (without voice
or message content); it only leaves your device if you choose to share it, for example with us for support.</p>

<h2>5. Service providers</h2>
<ul>
  <li><strong>Cloudflare, Inc.</strong> hosts our server (message relay and database) on its global network. Data is
    processed in the data centres of that network, which may be outside your country, including in the United
    States.</li>
  <li><strong>Apple</strong> provides Sign in with Apple, delivers push notifications (Apple Push Notification
    service), and processes all payments for the Family Pass through the App Store. Apple's privacy policy applies to
    that processing.</li>
</ul>
<p>We share personal data with others only if the law requires it.</p>

<h2>6. How long we keep data</h2>
<ul>
  <li>Encrypted voice messages: until played by everyone, at most 10 minutes (or the conversation's setting, at most
    24 hours).</li>
  <li>Talk metadata: 30 days.</li>
  <li>Reports: 90 days.</li>
  <li>Invite codes: deleted 7 days after they expire or are used.</li>
  <li>Account, device, family, contact and group data: as long as your account exists. When you delete your account,
    your profile, memberships, contacts and devices are removed right away and the remaining records are erased within
    30 days.</li>
</ul>

<h2>7. Children</h2>
<p>Children use Wristalk under the control of a parent or guardian. A guardian brings a child into the family, and
the guardian decides whom the child may talk to: new contacts and groups need the guardian's approval unless the
guardian allows otherwise. Guardians can also set allowed hours and battery settings.</p>
<p>We do not collect more data from children than from adults, we show them no ads, and nothing a child says can be
heard by us. A guardian can delete all of a child's data at any time in the iPhone app (Kids → the child → Delete all
of the child's data), or ask us by email.</p>

<h2>8. Legal bases (EEA, UK and Switzerland)</h2>
<p>We process your data to provide Wristalk under our contract with you (Art. 6(1)(b) GDPR), to keep Wristalk safe and
handle abuse reports (legitimate interests, Art. 6(1)(f) GDPR), and to meet legal obligations (Art. 6(1)(c) GDPR).
For children below the age of digital consent in their country, Wristalk is used with the consent and under the
control of their parent or guardian.</p>

<h2>9. International transfers</h2>
<p>We are based in the United States, and our providers process data worldwide. Where data from the EEA, UK or
Switzerland is transferred to other countries, we rely on appropriate safeguards such as the European Commission's
Standard Contractual Clauses or an adequacy decision.</p>

<h2>10. Security</h2>
<p>Voice is end-to-end encrypted. Each device's keys are created and kept in its secure hardware, and all connections
to our server are encrypted in transit. Access to our systems is restricted.</p>

<h2>11. Your rights</h2>
<p>Depending on where you live, you have the right to access your data, have it corrected or deleted, restrict or
object to its processing, and receive it in a portable format. You can delete your account and data yourself at any
time: on iPhone under Settings → Privacy → Delete my account…, on the watch under Settings → Privacy → Delete my
data. For any other request, email us at %%EMAIL%%. You also have the right to lodge a complaint with a data
protection supervisory authority, in particular in the country where you live.</p>

<h2>12. Changes</h2>
<p>If we change this policy, we will publish the new version here with a new effective date and inform you in a
suitable way about significant changes.</p>

<h2>13. Contact</h2>
<p>%%COMPANY%%, %%ADDRESS%%<br>Email: %%EMAIL%%</p>
""",
}

# ---------------------------------------------------------------------------
TERMS = {
    "title": "Wristalk — Terms of Use",
    "description": "Terms of use for Wristalk, including the Family Pass subscription.",
    "h1": "Terms of Use",
    "subtitle": "Wristalk · Effective September 27, 2026",
    "body": """
<h2>1. About these terms</h2>
<p>These terms govern your use of the Wristalk apps for Apple Watch and iPhone and the related service (“Wristalk”),
provided by %%COMPANY%%, %%ADDRESS%% (“we”, “us”). By using Wristalk you agree to these terms. They supplement Apple's
Licensed Application End User License Agreement; if the two conflict, these terms apply to the extent permitted.</p>

<h2>2. The service</h2>
<p>Wristalk lets approved contacts and groups send each other short voice messages (push-to-talk). Messages are
end-to-end encrypted and deleted after they have been played, or after the conversation's retention time at the
latest. How messages are delivered — automatically or by notification — depends on your device model, its settings
and the network.</p>
<p><strong>Wristalk is not an emergency service.</strong> Messages can be delayed or fail to arrive, for example
without an internet connection or when a battery is low. Do not rely on Wristalk to reach anyone in an emergency —
call your local emergency number.</p>

<h2>3. Your account</h2>
<p>You sign in with your Apple Account. Keep your devices secure, and use a display name that doesn't impersonate
anyone. You are responsible for activity from your account and devices.</p>

<h2>4. Children and guardians</h2>
<p>Children may use Wristalk only with the consent and under the control of a parent or guardian, who sets up the
child's use in a family and manages whom the child can talk to. Guardians are responsible for their children's use of
Wristalk and for deciding that it is appropriate for them.</p>

<h2>5. Family Pass subscription</h2>
<ul>
  <li>Wristalk is free to download. Talking requires an active Family Pass for your family.</li>
  <li>Eligible new subscribers get a <strong>free 7-day trial</strong>. After the trial, the Family Pass is an
    <strong>annual, automatically renewing subscription</strong> at the price shown in the App Store before you
    confirm.</li>
  <li>Payment is charged to your Apple Account by Apple when the trial ends (or at purchase, if you're not eligible for
    the trial). The subscription renews automatically each year unless you cancel it at least 24 hours before the end
    of the current period.</li>
  <li>You can manage or cancel the subscription in your App Store account settings (on iPhone: Settings → your name →
    Subscriptions). Cancelling takes effect at the end of the current period; deleting the app or your Wristalk
    account does not cancel it.</li>
  <li>The Family Pass supports Apple Family Sharing, so members of the purchaser's Apple family group can use it at no
    extra cost.</li>
  <li>Apple processes all payments. Refunds are handled by Apple under its policies
    (<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>); we cannot issue refunds ourselves.</li>
  <li>If the price changes, Apple informs you in advance as required by its rules.</li>
</ul>

<h2>6. Acceptable use</h2>
<p>Please be kind. When using Wristalk you must not:</p>
<ul>
  <li>harass, threaten, bully, intimidate or stalk anyone, or send hateful, sexual or otherwise abusive content;</li>
  <li>send anything illegal, or anything that exploits or endangers children;</li>
  <li>try to contact children without their guardian's approval, or get around parental controls;</li>
  <li>impersonate other people or send spam;</li>
  <li>interfere with, attack, overload, or try to gain unauthorised access to Wristalk or our servers, or access them
    by automated means other than the Wristalk apps.</li>
</ul>
<p>If someone breaks these rules, report them in the app or email us at %%EMAIL%%. You can leave groups at any time,
and guardians decide which contacts a child has. We may suspend or end accounts that break these terms.</p>

<h2>7. Your content</h2>
<p>What you say is yours. Because voice is end-to-end encrypted, we cannot access it. You allow us only to transmit
and briefly store the encrypted data as needed to deliver your messages. You are responsible for what you send.</p>

<h2>8. Privacy</h2>
<p>Our <a href="%%PRIVACY%%">Privacy Policy</a> explains what data we process and why.</p>

<h2>9. Changes and availability</h2>
<p>We keep improving Wristalk and may change, add or remove features. We aim to keep Wristalk available but cannot
guarantee that it will always work without interruption. If we ever discontinue Wristalk, we will tell you in advance
where reasonably possible.</p>

<h2>10. Disclaimer</h2>
<p>To the extent permitted by law, Wristalk is provided “as is” and “as available”, without warranties of any kind,
express or implied, including merchantability, fitness for a particular purpose and non-infringement.</p>

<h2>11. Limitation of liability</h2>
<p>To the extent permitted by law, we are not liable for indirect, incidental, special or consequential damages, or for
lost data or messages that were not delivered, and our total liability is limited to the amount you paid for the
Family Pass in the 12 months before the claim. Nothing in these terms limits liability that cannot be limited by law,
such as for intent, gross negligence, or injury to life, body or health, or your rights under mandatory consumer
protection law.</p>

<h2>12. Ending your use</h2>
<p>You can stop using Wristalk at any time and delete your account in the app (iPhone: Settings → Privacy → Delete my
account…; watch: Settings → Privacy → Delete my data). Remember to cancel the Family Pass separately in your App Store
settings.</p>

<h2>13. Governing law</h2>
<p>These terms are governed by the laws of %%JURISDICTION%%, without regard to its conflict-of-laws rules, and the
courts located there have jurisdiction. If you are a consumer, you also keep the protection of the mandatory laws of
the country where you live and may bring claims in the courts there.</p>

<h2>14. Changes to these terms</h2>
<p>We may update these terms. We will publish the new version here with a new effective date and inform you in a
suitable way about significant changes. If you keep using Wristalk after they take effect, the updated terms apply.</p>

<h2>15. Contact</h2>
<p>%%COMPANY%%, %%ADDRESS%%<br>Email: %%EMAIL%%</p>
""",
}
