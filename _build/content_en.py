"""English page text for the Wristalk support site. Tokens like %%SUPPORT%% are filled by gen_pages.py."""

SKIP = "Skip to content"
NAV_LABEL = "Main"
THEME_LABEL = "Switch light / dark appearance"
NAV = {"home": "Wristalk", "support": "Support", "privacy": "Privacy", "terms": "Terms"}
BACK_HOME = "← Back to Wristalk"
BACK_SUPPORT = "← Back to Support"
OG_LOCALE = "en_US"
OG_IMAGE_ALT = "Wristalk app icon: an Apple Watch with sound waves. Walkie-talkie for your family."

# ---------------------------------------------------------------------------
HOME = {
    "title": "Wristalk — Walkie-talkie for your family",
    "description": "Push-to-talk for families on Apple Watch and iPhone. Works on kids' Family Setup watches "
                   "without an iPhone. Parental controls, end-to-end encrypted. Free download.",
    "eyebrow": "For Apple Watch and iPhone",
    "h1": "The walkie-talkie is back on your wrist.",
    "tagline": "Hold the talk button and speak. On your family's watches your voice plays right away, no tap "
               "needed — like a real walkie-talkie. Let go, and they can answer.",
    "badge_small": "Download on the",
    "badge_soon": "Coming soon to the",
    "help_link": "Help &amp; FAQ",
    "fineprint": "Free to download from the US App Store. Family Pass: 1 week free, then $19.99/year. "
                 "Requires watchOS 26 or iOS 26.",
    "watch_alt": "Wristalk on Apple Watch: Kyra is talking to the family, playing through the speaker",
    "band": "Made for families: kids' Apple Watch with Family Setup work without an iPhone of their own, and "
            "parents decide who a child can talk to.",
    "features": [
        {"title": "Made for families", "items": [
            "Works on kids' Apple Watch with Family Setup — no iPhone of their own needed.",
            "Parents decide who a child can talk to. New contacts and groups need a guardian's approval, and "
            "guardians set the hours when messages may play.",
            "Talk one-to-one or in groups: the whole family, just the kids, grandparents, or friends from "
            "another family.",
            "Invite people via Messages, with a QR code, or by reading out a short code. Adults can leave or "
            "switch family at any time.",
        ]},
        {"title": "Live when it matters", "items": [
            "On a supported watch a message plays by itself as soon as it arrives — no tap, even with the "
            "wrist down.",
            "After each message Wristalk stays live for 10 minutes, so replies come through instantly. Then it "
            "goes quiet again and saves battery.",
            "Want it live all day? Turn on Keep Wristalk live, with auto-off after 1, 2 or 4 hours or tonight, "
            "and a battery guard.",
            "Nothing plays during Do Not Disturb or Sleep — you see what you missed. Stop a message while it "
            "plays, and delete missed ones.",
        ]},
        {"title": "Private by design", "items": [
            "Every voice message is end-to-end encrypted. Only the people in the conversation can hear it — "
            "not us, not anyone else.",
            "Messages are deleted once they have been played, or after 10 minutes at the latest. If someone "
            "missed you, you're told.",
            "Report or block anyone who bothers you; guardians can do it for their children.",
            "Sign in with Apple. No email address, no phone number, no ads, no tracking.",
        ]},
        {"title": "On iPhone, too", "items": [
            "The iPhone app is the comfortable place to manage people, groups and kids' settings, and to "
            "approve requests.",
            "It is a walkie-talkie of its own, with Apple's system Push to Talk — messages play even while "
            "Wristalk is closed.",
            "So parents without an Apple Watch can talk with the family too.",
        ]},
    ],
    "shots_title": "See it in action",
    # (file, caption, alt text) — files in assets/screens/<lang>/watch-<file>.webp
    "watch_shots": [
        ("01-homeWindow", "Live for 10 minutes after each talk",
         "Wristalk home screen on Apple Watch showing Live, 7 minutes left, and the contact list"),
        ("02-receiving", "Messages play right away",
         "Apple Watch playing a message from Kyra to the family through the speaker"),
        ("03-channelTalking", "Hold to talk, release to send",
         "The talk button on Apple Watch while recording, with a 9-second timer"),
        ("04-missed", "Missed messages, ready to play",
         "List of missed messages from Kyra and Lena with Play buttons"),
        ("05-invite", "Invite with a short code",
         "An 8-character invite code with a Share via Messages button"),
        ("06-approval", "Approve a child's request",
         "Approval request on Apple Watch: Lena wants to add Mia as a contact, with Approve and Deny"),
        ("07-keepLive", "Keep Wristalk live, with auto-off",
         "Keep Wristalk live switch with battery guard at 20 % and auto-off at 10 pm"),
    ],
    "iphone_shots": [
        ("01-talk", "Talk from your iPhone",
         "Talk tab on iPhone with the family's contacts and a large talk button"),
        ("02-people", "Your family and contacts",
         "People tab listing the family members and contacts in other families"),
        ("03-kids", "Parental controls for each child",
         "A child's parental controls: invites, groups, allowed hours and delivery"),
        ("04-approvals", "Approvals in one place",
         "Approvals tab with a pending contact request and earlier decisions"),
        ("05-privacy", "End-to-end encrypted",
         "Encryption screen explaining that Wristalk cannot listen"),
        ("06-invite", "Invite via Messages or QR code",
         "Invite screen with a code, a QR code and a Share via Messages button"),
        ("07-groups", "Groups for every occasion",
         "Groups tab with the family, a football group and a kids' group"),
    ],
    "tiers_title": "Which Apple Watch?",
    "tiers": [
        {"kind": "live", "title": "Live through the speaker",
         "text": "Apple Watch SE (3rd generation), Series 10 and later, Ultra 2 and later. Messages play by "
                 "themselves through the speaker."},
        {"kind": "notify", "title": "Notifications or headphones",
         "text": "Other watches with watchOS 26, such as Apple Watch SE (2nd generation) and Series 6 to 8. "
                 "The full app works; messages play live with Bluetooth headphones, otherwise you tap a "
                 "notification to listen."},
        {"kind": "off", "title": "Not supported",
         "text": "Watches that can't run watchOS 26."},
    ],
    "tiers_note": "Apple Watch: watchOS 26 or later. iPhone: iOS 26 or later. Each watch or iPhone needs an "
                  "internet connection (Wi-Fi or cellular). Available in the US App Store.",
    "pricing": {
        "title": "One Family Pass for everyone",
        "price": "$19.99",
        "per": "/year",
        "trial": "First week free",
        "sub": "Free to download. US price; the App Store shows it before you confirm.",
        "items": [
            "One person subscribes. Apple Family Sharing shares the Family Pass with your Apple family — "
            "kids' watches included.",
            "Each family needs its own Family Pass, including relatives and friends you talk with who are in "
            "another family (see the <a href=\"%%TERMS%%\">Terms</a>).",
            "Renews automatically every year. Cancel at least 24 hours before renewal in your Apple Account "
            "settings (Settings → your name → Subscriptions).",
            "New iPhone or watch? Tap Restore purchases on the Family Pass screen.",
            "If it ends, Wristalk shows the Family Pass screen and your family can't talk until someone "
            "subscribes again. Your family, contacts and groups stay.",
        ],
        "more": "More about the Family Pass",
    },
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
             "<ul><li><strong>Live through the speaker:</strong> Apple Watch SE (3rd generation), Series 10 "
             "and later, Ultra 2 and later. Incoming messages play by themselves, no tap needed.</li>"
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
            ("Where is Wristalk available?",
             "<p>Wristalk is available in the App Store in the United States. The app is in English and "
             "German.</p>"),
        ]},
        {"id": "people", "title": "Contacts &amp; approvals", "faqs": [
            ("How do I invite someone?",
             "<p>Create an invite code in Wristalk. On iPhone you can send it via Messages or show it as a QR "
             "code; on the watch you can share it via Messages or Mail, or show it large on screen so the "
             "other person can type it in.</p>"
             "<p>A code has 8 characters, works once and is valid for 48 hours. The other person opens the "
             "link on their iPhone or enters the code in Wristalk (on the watch: <span class=\"kbd\">Enter "
             "code</span> or <span class=\"kbd\">I have a code</span>).</p>"
             "<p>Codes never contain the letters O and I or the digits 0 and 1, so you can also just read a "
             "code out, for example on the phone.</p>"),
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
            ("How do I leave or switch family?",
             "<p>Adults can leave their family in Settings → <span class=\"kbd\">Leave family</span>, on "
             "iPhone or on the watch. To move to another family, accept a family invite from it; Wristalk asks "
             "you to confirm and then switches for you.</p>"
             "<p>If you bought the Family Pass, it goes with you, and the family you leave needs its own. "
             "Children can't leave their family — a guardian can delete the child's account instead — and the "
             "last adult of a family with children can't leave it.</p>"),
        ]},
        {"id": "talking", "title": "Talking &amp; delivery", "faqs": [
            ("How do I talk?",
             "<p>Open a contact or group, hold the big talk button, speak, and let go. A short sound and "
             "haptic tell you when you can speak. One person talks at a time; a talk lasts up to 30 seconds. "
             "If you prefer, turn on tap to talk (tap once to start, once to stop).</p>"),
            ("Can I start talking without opening Wristalk first?",
             "<p>On Apple Watch, open the Shortcuts app and tap Wristalk's <span class=\"kbd\">Talk</span> "
             "shortcut. Wristalk opens your last conversation and starts talking; tap the shortcut again to "
             "send.</p>"),
            ("How does a message play on the watch by itself?",
             "<p>A message arrives as a notification. On a watch that can play through its speaker, the "
             "notification plays the message right away — no tap, even with the wrist down. Wristalk then stays "
             "<strong>live</strong> for 10 minutes after the last message (5 or 30 minutes under Settings → "
             "Live window), so replies come through instantly. After that the watch goes quiet again and saves "
             "battery.</p>"
             "<p>If you want Wristalk live all day, turn on <span class=\"kbd\">Keep Wristalk live</span> in "
             "Settings. It has an auto-off timer and a battery guard.</p>"),
            ("Why do I sometimes have to tap a notification to hear a message?",
             "<p>In these cases you get a notification that someone talked, with a Play button, instead of "
             "automatic playback:</p>"
             "<ul><li>The watch can't play through its speaker in the background (older models) and no "
             "headphones are connected.</li>"
             "<li>Do Not Disturb or Sleep is on — nothing plays then, and you see what you missed.</li>"
             "<li>The message is older than 10 minutes when it reaches the watch.</li>"
             "<li><span class=\"kbd\">Notify instead</span> is chosen under Settings → Delivery.</li>"
             "<li>On a child's watch: it's outside the allowed hours a guardian has set.</li></ul>"),
            ("What happens if someone misses my message?",
             "<p>A message is kept, encrypted, until everyone has played it — for 10 minutes at the latest "
             "(or 1 hour or 24 hours, if the person who created the group chose a longer time). If someone "
             "didn't hear it in time, you get a notification that they didn't hear your message, and they "
             "see a “missed” marker in the conversation.</p>"),
            ("Can I stop a message or delete missed ones?",
             "<p>Yes. While a message plays in Wristalk, tap <span class=\"kbd\">Stop</span>. Missed messages "
             "are listed in the conversation: play one, swipe it away to delete it, or use "
             "<span class=\"kbd\">Delete all</span>. A deleted message disappears from all your devices.</p>"),
            ("What do the battery guard and auto-off timer do?",
             "<p>Staying live keeps the watch listening, which uses more battery. The "
             "<strong>battery guard</strong> switches from auto-play to notifications when the battery drops "
             "below a level you choose (20 % by default); charging pauses the guard. The "
             "<strong>auto-off timer</strong> ends Keep Wristalk live after 1, 2 or 4 hours or tonight.</p>"
             "<p>You find both in the watch's Settings. On a child's watch, the guardian sets the battery "
             "guard (on iPhone under Kids).</p>"),
        ]},
        {"id": "pass", "title": "Family Pass &amp; pricing", "faqs": [
            ("How much does Wristalk cost?",
             "<p>Wristalk is free to download. To talk, your family needs the <strong>Family Pass</strong>, an "
             "auto-renewing yearly subscription: <strong>$19.99 per year</strong> in the US, with the "
             "<strong>first week free</strong> for new subscribers. The App Store shows the price before you "
             "confirm, and Apple charges your Apple Account when the free week ends.</p>"
             "<p>You can start the Family Pass in Wristalk during setup, or later under "
             "<span class=\"kbd\">Settings → Family Pass</span>.</p>"),
            ("Does everyone in the family have to subscribe?",
             "<p>No — only one person subscribes. The Family Pass supports Apple's Family Sharing, so everyone "
             "in the subscriber's Apple family gets it automatically, kids' watches included (subscription "
             "sharing must be turned on in your Family Sharing settings).</p>"),
            ("Do contacts in other families need their own Family Pass?",
             "<p>Yes. Each Wristalk family needs its own Family Pass (or its free week) — that includes "
             "grandparents, relatives or friends you talk with who are in another family. Family Sharing only "
             "covers the subscriber's own Apple family. See section 5 of the <a href=\"%%TERMS%%\">Terms of "
             "Use</a>.</p>"),
            ("How do I cancel the subscription?",
             "<p>Apple handles the subscription. On iPhone, open <span class=\"kbd\">Settings → [your name] → "
             "Subscriptions → Wristalk</span> and tap Cancel Subscription — or in Wristalk on iPhone, go to "
             "<span class=\"kbd\">Settings → Family Pass → Manage subscription</span>.</p>"
             "<p>Cancel at least 24 hours before the renewal date to avoid being charged for the next year. "
             "You keep the Family Pass until the end of the period you paid for. Only the person who bought "
             "it can cancel it, and deleting the app or your Wristalk account does not cancel it. If you "
             "cancel during the free week, access may end right away.</p>"),
            ("What happens when the Family Pass ends?",
             "<p>When the Family Pass ends — because it was cancelled, or because Apple couldn't renew it — "
             "Wristalk shows the Family Pass screen again, and your family can't talk until someone in the "
             "family subscribes again. Your family, contacts, groups and settings stay.</p>"
             "<p>If Apple has a problem with your payment, Wristalk shows it under Settings → Family Pass. "
             "Update your payment method in your Apple Account to keep the Family Pass.</p>"),
            ("I have the Family Pass, but Wristalk doesn't recognise it.",
             "<p>Make sure you're signed in to the App Store with the Apple Account that bought it (or one in "
             "the same Apple family), then tap <span class=\"kbd\">Restore purchases</span> on the Family "
             "Pass screen — for example on a new iPhone. If that doesn't help, email us.</p>"),
            ("Can I get a refund?",
             "<p>Because Apple processes all payments, refunds are handled by Apple. Request one at "
             "<a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>.</p>"),
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
             "whom and when). We review every report within 24 hours. Reports are kept for 90 days.</p>"
             "<p>You can leave a group at any time, and guardians decide which contacts a child has. If "
             "someone is in danger, contact your local emergency services first.</p>"),
            ("How do I block someone?",
             "<p>Open the person — on iPhone under People, on the watch in the conversation details — and "
             "choose <span class=\"kbd\">Block</span>. Blocked people can't invite you or add you to groups, "
             "and you don't hear them in groups you share. Unblocking works in the same place; the contact "
             "isn't restored automatically.</p>"
             "<p>Guardians can block someone for a child, and only a guardian can lift that block. "
             "<span class=\"kbd\">Report…</span> is in the same place.</p>"),
        ]},
    ],
}

# ---------------------------------------------------------------------------
PRIVACY = {
    "title": "Wristalk — Privacy Policy",
    "description": "How Wristalk handles your data: end-to-end encrypted voice, minimal data, no tracking.",
    "h1": "Privacy Policy",
    "subtitle": "Wristalk · Effective %%EFFECTIVE%%",
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
  <li><strong>Device data.</strong> An app-generated device ID, the device type and model, a device name (such as
    “Apple Watch”), the app version, your devices' public encryption keys, and push notification tokens so we can
    notify your watch or iPhone. We don't use advertising identifiers.</li>
  <li><strong>Sign in with Apple token.</strong> The token Apple issues when you sign in, stored encrypted and used
    only to revoke Wristalk's access to your Apple Account when you delete your account.</li>
  <li><strong>Family, contact and group structure.</strong> Your family, contacts and groups (names and members),
    invites, guardian relationships, parental-control settings, and approval requests and decisions.</li>
  <li><strong>Talk metadata.</strong> For each message: sender, conversation, start and end time, and whether each
    recipient received or played it. We need this to deliver messages, tell senders when someone missed them, and
    handle abuse. It is deleted after 30 days.</li>
  <li><strong>Encrypted voice messages.</strong> Stored only as encrypted data we cannot read, until every recipient
    has played the message — after 10 minutes at the latest, or after the conversation's longer setting
    (1 hour or 24 hours) if its creator chose one.</li>
  <li><strong>Reports.</strong> If you report someone, we keep the report — the reason you chose, your optional note,
    who reported whom, and the conversation concerned — for 90 days. We receive new reports by email once a day. If a
    child files a report, the child's guardians are notified. Reports never contain voice.</li>
  <li><strong>Subscription status.</strong> When you buy or restore the Family Pass, the app sends us Apple's signed
    transaction information (product, dates, whether it is a trial) so we can unlock Wristalk for your family. Apple
    also informs our server of renewals, expirations and refunds. We never receive your payment details.</li>
  <li><strong>Technical data.</strong> Your IP address is processed when your device connects, to deliver the
    service and limit abuse (rate limiting). Rate-limit records are deleted within 2 days. Our hosting provider keeps
    short-lived request logs for troubleshooting, which are deleted automatically after a few days. Our server logs
    contain no voice content.</li>
  <li><strong>Diagnostic logs.</strong> Only if you tap Settings → Help → Send diagnostic log and confirm with Send,
    the app sends this device's technical log to us to help fix a problem. It records what the app did and when (for
    example app launches, talks started and ended, connection changes, settings changes and error codes), with your
    user ID, device ID, family and conversation IDs, the device model, the operating-system version and the app
    version. It contains no names, no voice, no message content, no invite codes and no keys. Only we read it, to
    investigate the problem; you get a reference to quote when you write to us. It is deleted after 30 days, or right
    away when you delete your account.</li>
</ul>

<h2>3. What we cannot see</h2>
<p>Voice is encrypted on your device before it is sent, with keys that exist only on the devices of the people in
the conversation. Our server passes on and briefly stores this encrypted data, but cannot decrypt it — so we cannot
listen to, transcribe or analyse what you say.</p>
<p>To deliver messages, our server does see who is in which family, contact list and group, who talks to whom, when
and for how long, and the size of the data. Push notifications contain the sender's display name and a
conversation reference (for approval requests, the names of the people involved), never voice content.</p>
<p>Guardians see, for each child in their family, the child's contacts, groups, devices and approval requests, and an
activity log of whom the child talked with and when (the last 30 days). They never hear messages they were not part
of.</p>

<h2>4. No tracking, ads or analytics</h2>
<p>Wristalk contains no advertising, no analytics and no third-party tracking SDKs. We do not sell or share your data
for advertising, and we do not build profiles about you. The app keeps a technical log on your device (without voice
or message content); it only leaves your device if you choose to send or share it, for example with us for support
(section 2, Diagnostic logs).</p>

<h2>5. Service providers</h2>
<ul>
  <li><strong>Cloudflare, Inc.</strong> hosts our server (message relay and database) on its global network. Data is
    processed in the data centres of that network, which may be outside your country, including in the United
    States.</li>
  <li><strong>Apple</strong> provides Sign in with Apple, delivers push notifications (Apple Push Notification
    service), and processes all payments for the Family Pass through the App Store. Apple's privacy policy applies to
    that processing.</li>
</ul>
<p>We share personal data with others only if the law requires it. New reports are emailed once a day to our support
mailbox, %%EMAIL%%. Our email provider receives these emails and the messages you send us.</p>

<h2>6. How long we keep data</h2>
<ul>
  <li>Encrypted voice messages: until played by everyone, at most 10 minutes (or the conversation's setting, at most
    24 hours).</li>
  <li>Talk metadata: 30 days.</li>
  <li>Diagnostic logs you send us: 30 days.</li>
  <li>Reports: 90 days.</li>
  <li>Invite codes: deleted 7 days after they expire or are used.</li>
  <li>Subscription records: as long as your family exists; Apple's notifications about them, 30 days.</li>
  <li>Account, device, family, contact and group data: as long as your account exists. When you delete your account,
    your profile, memberships, contacts and devices are removed right away and the remaining records are erased within
    30 days.</li>
</ul>

<h2>7. Children</h2>
<p>Children use Wristalk only as members of a family, under the control of a parent or guardian. A guardian brings a
child into the family with an invite code created for a child, and the guardian decides whom the child may talk to:
new contacts and groups need the guardian's approval unless the guardian allows otherwise. Guardians can also set
allowed hours, delivery and battery settings.</p>
<p>From children we collect the same limited data as from adults (section 2): the Sign in with Apple identifier, a
display name, device data, family, contact and group structure, talk metadata and reports. We use it only to provide
Wristalk, never for advertising, and we do not disclose it to third parties except the service providers in
section 5. Nothing a child says can be heard by us.</p>
<p>A guardian can review a child's contacts, groups, devices and activity in the iPhone app (Kids → the child), stop
further collection and delete all of the child's data at any time (Kids → the child → Delete all of the child's
data), or ask us by email at %%EMAIL%%. If we learn that a child under 13 uses Wristalk without a guardian in their
family, we delete the account.</p>
<p>A child can send a diagnostic log (section 2) the same way as an adult, after the same confirmation. The child's
guardians are notified each time. We use a child's log only to fix the problem it was sent for.</p>

<h2>8. Legal bases (EEA, UK and Switzerland)</h2>
<p>We process your data to provide Wristalk under our contract with you (Art. 6(1)(b) GDPR), to keep Wristalk safe, handle abuse
reports and investigate problems from diagnostic logs you send us (legitimate interests, Art. 6(1)(f) GDPR), and to meet legal obligations (Art. 6(1)(c) GDPR).
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
    "subtitle": "Wristalk · Effective %%EFFECTIVE%%",
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
child's use in a family and manages whom the child can talk to. Children under 13 (or the age of digital consent in
their country) may use Wristalk only as a child member of a family set up by their guardian. Guardians are responsible for their children's use of
Wristalk and for deciding that it is appropriate for them.</p>

<h2>5. Family Pass subscription</h2>
<ul>
  <li>Wristalk is free to download. Talking requires an active Family Pass (or its free trial) for your family. Each
    family needs its own Family Pass, including families you talk with as contacts.</li>
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
