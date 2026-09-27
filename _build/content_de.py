"""Deutsche Texte der Wristalk-Support-Seite (Sie-Form). Platzhalter wie %%SUPPORT%% füllt gen_pages.py."""

SKIP = "Zum Inhalt springen"
NAV_LABEL = "Hauptnavigation"
THEME_LABEL = "Helle / dunkle Darstellung umschalten"
NAV = {"home": "Wristalk", "support": "Support", "privacy": "Datenschutz", "terms": "Nutzungsbedingungen"}
BACK_HOME = "← Zurück zu Wristalk"
BACK_SUPPORT = "← Zurück zum Support"

# ---------------------------------------------------------------------------
HOME = {
    "title": "Wristalk — Walkie-Talkie für die Familie",
    "description": "Live-Push-to-Talk für Familien auf Apple Watch und iPhone. Läuft auf Kinderuhren mit "
                   "Familienkonfiguration ohne iPhone. Mit Kindersicherung, Ende-zu-Ende-verschlüsselt.",
    "eyebrow": "Für Apple Watch und iPhone",
    "h1": "Das Walkie-Talkie ist zurück am Handgelenk.",
    "tagline": "Halten Sie die Sprechtaste gedrückt und sprechen Sie. Auf den Uhren Ihrer Familie ist Ihre Stimme "
               "sofort zu hören, ohne zu tippen – wie bei einem echten Walkie-Talkie. Loslassen, und die anderen "
               "können antworten.",
    "badge_small": "Laden im",
    "badge_soon": "Demnächst im",
    "help_link": "Hilfe &amp; FAQ",
    "fineprint": "Kostenlos laden. Den Family Pass eine Woche gratis testen, danach verlängert er sich jährlich.",
    "watch_alt": "Illustration einer Apple Watch mit großer Sprechtaste",
    "watch_name": "Mama",
    "watch_hint": "Halten zum Sprechen",
    "band": "Für Familien gemacht: Kinderuhren mit Familienkonfiguration funktionieren ganz ohne eigenes iPhone, "
            "und Eltern bestimmen, mit wem ein Kind sprechen darf.",
    "features": [
        {"title": "Für Familien gemacht", "items": [
            "Läuft auf Kinderuhren mit Familienkonfiguration – ganz ohne eigenes iPhone.",
            "Eltern bestimmen, mit wem ein Kind sprechen darf. Neue Kontakte und Gruppen brauchen die Zustimmung "
            "der Eltern, und die lässt sich jederzeit ändern.",
            "Sprechen Sie zu zweit oder in Gruppen: die ganze Familie, nur die Kinder, die Großeltern oder "
            "Freunde aus einer anderen Familie.",
        ]},
        {"title": "Live, wenn es darauf ankommt", "items": [
            "Schalten Sie Wristalk ein, und eingehende Sprache wird auf unterstützten Uhren automatisch "
            "abgespielt – ohne zu tippen.",
            "Auf anderen Uhren spielt Wristalk live über Bluetooth-Kopfhörer oder schickt eine Mitteilung, die "
            "Sie zum Anhören antippen.",
            "Akkuschutz und Ausschalt-Timer sorgen dafür, dass Kinderuhren den Tag durchhalten.",
        ]},
        {"title": "Privat von Anfang an", "items": [
            "Jede Sprachnachricht ist Ende-zu-Ende-verschlüsselt. Nur die Personen im Gespräch können sie hören – "
            "nicht wir, niemand sonst.",
            "Nachrichten verschwinden nach dem Abspielen, spätestens nach 10 Minuten. Hat Sie jemand verpasst, "
            "erfahren Sie es.",
            "Anmelden mit Apple. Keine E-Mail-Adresse, keine Telefonnummer, keine Werbung, kein Tracking.",
        ]},
        {"title": "Auch auf dem iPhone", "items": [
            "In der iPhone-App verwalten Sie bequem Personen, Gruppen und die Einstellungen der Kinder.",
            "Sie ist selbst ein Walkie-Talkie mit der Push-to-Talk-Steuerung des Systems – so können auch Eltern "
            "ohne Uhr mitsprechen.",
            "Laden Sie Personen per Code über Nachrichten oder per QR-Code ein.",
        ]},
        {"title": "Ein Pass für die ganze Familie", "items": [
            "Kostenlos laden, die erste Woche Family Pass gratis.",
            "Danach ist der Family Pass ein Jahresabo, abgerechnet über Apple.",
            "Er wird per Familienfreigabe mit Ihrer Apple-Familie geteilt und lässt sich jederzeit in den "
            "App-Store-Einstellungen kündigen.",
        ]},
    ],
    "tiers_title": "Welche Apple Watch?",
    "tiers": [
        {"kind": "live", "title": "Live über den Lautsprecher",
         "text": "Apple Watch SE (3. Generation), Series 10, 11 und 12, Ultra 2, 3 und 4. Ist Wristalk an, wird "
                 "Sprache automatisch abgespielt."},
        {"kind": "notify", "title": "Mitteilungen oder Kopfhörer",
         "text": "Andere Uhren mit watchOS 26, etwa Apple Watch SE (2. Generation) und Series 6 bis 8. Die ganze "
                 "App funktioniert; Nachrichten laufen live über Bluetooth-Kopfhörer, sonst tippen Sie zum "
                 "Anhören auf eine Mitteilung."},
        {"kind": "off", "title": "Nicht unterstützt",
         "text": "Uhren, auf denen watchOS 26 nicht läuft."},
    ],
    "tiers_note": "Jede Uhr bzw. jedes iPhone braucht eine Internetverbindung (WLAN oder Mobilfunk). "
                  "iPhone: iOS 26 oder neuer.",
    "help_title": "Fragen?",
    "help_text": 'Lesen Sie die <a href="%%SUPPORT%%">Support-Seite</a> oder schreiben Sie an %%EMAIL%%.',
}

# ---------------------------------------------------------------------------
SUPPORT = {
    "title": "Wristalk — Support",
    "description": "Hilfe und Antworten zu Wristalk, dem Walkie-Talkie für Familien auf Apple Watch und iPhone.",
    "h1": "Wristalk Support",
    "subtitle": "Hilfe &amp; Antworten",
    "contact_title": "Kontakt",
    "contact_text": "Fragen, Probleme oder etwas zu melden? Schreiben Sie uns eine E-Mail, wir melden uns bei Ihnen.",
    "contact_note": "Nennen Sie bitte das Modell Ihrer Uhr bzw. Ihres iPhone und, falls es um eine Nachricht geht, "
                    "ungefähr den Zeitpunkt. Schicken Sie uns niemals Passwörter oder Zahlungsdaten.",
    "toc_label": "Themen",
    "sections": [
        {"id": "start", "title": "Erste Schritte", "faqs": [
            ("Was ist Wristalk?",
             "<p>Wristalk ist ein Walkie-Talkie für Familien auf Apple Watch und iPhone. Sprechtaste gedrückt "
             "halten, sprechen, loslassen – die Personen im Gespräch hören Sie sofort. Sie können zu zweit oder "
             "in Gruppen sprechen, und Eltern bestimmen, mit wem ihre Kinder sprechen dürfen.</p>"),
            ("Was brauche ich?",
             "<ul><li>Eine Apple Watch mit watchOS 26 oder neuer oder ein iPhone mit iOS 26 oder neuer.</li>"
             "<li>Eine Internetverbindung auf jeder Uhr bzw. jedem iPhone (WLAN oder Mobilfunk).</li>"
             "<li>Einen Apple Account für „Mit Apple anmelden“. Wristalk fragt weder nach E-Mail-Adresse noch "
             "nach Telefonnummer.</li></ul>"
             "<p>Die iPhone-App ist optional: Dort verwalten Sie bequem Personen, Gruppen und die Einstellungen "
             "der Kinder, aber alles funktioniert auch auf der Uhr.</p>"),
            ("Welche Apple Watch-Modelle werden unterstützt?",
             "<ul><li><strong>Live über den Lautsprecher:</strong> Apple Watch SE (3. Generation), Series 10, 11 "
             "und 12, Ultra 2, 3 und 4. Solange Wristalk an ist, wird eingehende Sprache automatisch "
             "abgespielt.</li>"
             "<li><strong>Mit Mitteilungen oder Kopfhörern:</strong> Apple Watch SE (2. Generation), Series 6, 7 "
             "und 8 sowie andere Modelle mit watchOS 26. Die ganze App funktioniert. Nachrichten laufen live, "
             "solange Wristalk auf dem Bildschirm geöffnet ist oder Bluetooth-Kopfhörer verbunden sind; sonst "
             "erhalten Sie eine Mitteilung und tippen sie zum Anhören an.</li>"
             "<li><strong>Nicht unterstützt:</strong> Uhren, auf denen watchOS 26 nicht läuft.</li></ul>"),
            ("Braucht mein Kind ein iPhone?",
             "<p>Nein. Die Uhren-App ist für sich vollständig und läuft auf Apple Watches mit "
             "Familienkonfiguration. Installieren Sie Wristalk auf der Uhr aus dem App Store, melden Sie sich mit "
             "dem Apple Account des Kindes an und treten Sie mit einem Einladungscode Ihrer Familie bei. Die "
             "Einstellungen Ihres Kindes verwalten Sie auf Ihrem eigenen iPhone oder Ihrer Uhr.</p>"),
        ]},
        {"id": "people", "title": "Kontakte &amp; Freigaben", "faqs": [
            ("Wie lade ich jemanden ein?",
             "<p>Erstellen Sie in Wristalk einen Einladungscode. Auf dem iPhone können Sie ihn über Nachrichten "
             "senden oder als QR-Code zeigen; auf der Uhr teilen Sie ihn über Nachrichten oder Mail oder zeigen "
             "ihn groß an, damit die andere Person ihn eintippen kann.</p>"
             "<p>Ein Code hat 8 Zeichen, gilt einmal und ist 48 Stunden gültig. Die andere Person öffnet den Link "
             "auf dem iPhone oder gibt den Code in Wristalk ein (auf der Uhr: <span class=\"kbd\">Code "
             "eingeben</span> bzw. <span class=\"kbd\">Ich habe einen Code</span>).</p>"),
            ("Wie funktionieren Freigaben für Kinder?",
             "<p>Jedes Kind hat in Wristalk einen oder mehrere Verantwortliche – die Erwachsenen, die sich um "
             "seine Einstellungen kümmern. Möchte ein Kind jemanden einladen, eine Einladung annehmen oder eine "
             "Gruppe erstellen, wird daraus standardmäßig eine Anfrage an die Verantwortlichen. Auch ein neues "
             "Gerät eines Kindes braucht eine Freigabe.</p>"
             "<p>Verantwortliche erhalten auf Uhr und iPhone eine Mitteilung mit den Tasten Erlauben und "
             "Ablehnen. Offene Anfragen stehen außerdem auf dem iPhone unter <span class=\"kbd\">Kinder → "
             "Freigaben</span> und auf der Uhr unter <span class=\"kbd\">Anfragen</span>. Das Kind sieht, wer was "
             "freigegeben hat.</p>"
             "<p>Für jedes Kind legen Verantwortliche fest, ob es neue Personen einladen, Einladungen annehmen und "
             "Gruppen erstellen darf (nie, mit Freigabe oder frei), wer es zu Gruppen hinzufügen darf und zu "
             "welchen Zeiten Wristalk Nachrichten abspielen darf.</p>"),
            ("Können wir auch mit Personen außerhalb der Familie sprechen?",
             "<p>Ja. Kontakte können aus anderen Familien kommen – Freunde, Großeltern, Nachbarn. Bei Kindern "
             "braucht jeder neue Kontakt die Freigabe eines Verantwortlichen, sofern dieser nichts anderes "
             "erlaubt hat.</p>"),
        ]},
        {"id": "talking", "title": "Sprechen &amp; Zustellung", "faqs": [
            ("Wie spreche ich?",
             "<p>Öffnen Sie einen Kontakt oder eine Gruppe, halten Sie die große Sprechtaste gedrückt, sprechen "
             "Sie und lassen Sie los. Ein kurzer Ton und ein Tippen am Handgelenk zeigen, dass Sie sprechen "
             "können. Es spricht immer nur eine Person; eine Nachricht dauert höchstens 30 Sekunden. Wenn Sie "
             "möchten, schalten Sie „Zum Sprechen tippen“ ein (einmal tippen zum Starten, einmal zum Beenden).</p>"),
            ("Warum muss ich manchmal auf eine Mitteilung tippen, um eine Nachricht zu hören?",
             "<p>Die Apple Watch lässt eine App nur dann live Sprache empfangen, wenn sie gerade aktiv Audio "
             "abspielt. Wenn Sie auf einer unterstützten Uhr <span class=\"kbd\">Wristalk an</span> schalten, "
             "bleibt Wristalk empfangsbereit und spielt eingehende Sprache automatisch ab.</p>"
             "<p>In diesen Fällen nutzt Wristalk stattdessen den Modus <strong>Mitteilen</strong> – Sie erhalten "
             "eine Mitteilung, dass jemand spricht, und tippen sie zum Anhören an:</p>"
             "<ul><li>Wristalk ist ausgeschaltet oder der Ausschalt-Timer ist abgelaufen.</li>"
             "<li>Der Akkuschutz hat wegen niedrigen Akkus auf Mitteilungen umgestellt.</li>"
             "<li>Die Uhr kann im Hintergrund nicht über ihren Lautsprecher abspielen (ältere Modelle), und es "
             "sind keine Kopfhörer verbunden.</li>"
             "<li>Unter Einstellungen → Zustellung ist <span class=\"kbd\">Stattdessen mitteilen</span> "
             "gewählt.</li>"
             "<li>Auf der Uhr eines Kindes: Es ist außerhalb der erlaubten Zeiten, die ein Verantwortlicher "
             "festgelegt hat.</li></ul>"
             "<p>Nachdem Sie getippt und zugehört haben, spielt Wristalk wieder live ab, solange es aktiv "
             "bleibt.</p>"),
            ("Was passiert, wenn jemand meine Nachricht verpasst?",
             "<p>Eine Nachricht wird verschlüsselt aufbewahrt, bis alle sie abgespielt haben – höchstens 10 "
             "Minuten lang (oder 1 bzw. 24 Stunden, wenn die Person, die die Gruppe erstellt hat, eine längere "
             "Zeit gewählt hat). Hat jemand sie nicht rechtzeitig gehört, erhalten Sie eine Mitteilung, dass die "
             "Nachricht nicht angekommen ist, und die andere Person sieht im Gespräch einen Hinweis "
             "„verpasst“.</p>"),
            ("Was machen Akkuschutz und Ausschalt-Timer?",
             "<p>Live-Wiedergabe hält die Uhr empfangsbereit und braucht mehr Akku. Der "
             "<strong>Akkuschutz</strong> wechselt von automatischem Abspielen zu Mitteilungen, sobald der Akku "
             "unter eine gewählte Grenze fällt (standardmäßig 20 %); beim Laden pausiert er. Der "
             "<strong>Ausschalt-Timer</strong> („Automatisch aus“) schaltet Wristalk nach 2 Stunden, 4 Stunden "
             "oder heute Abend aus.</p>"
             "<p>Beides finden Sie in den Einstellungen der Uhr. Auf der Uhr eines Kindes legt ein "
             "Verantwortlicher den Akkuschutz fest (auf dem iPhone unter Kinder).</p>"),
        ]},
        {"id": "pass", "title": "Family Pass", "faqs": [
            ("Was kostet Wristalk?",
             "<p>Wristalk ist kostenlos zu laden. Zum Sprechen braucht Ihre Familie den <strong>Family "
             "Pass</strong>: Die erste Woche ist gratis, danach ist er ein Jahresabo, das sich automatisch "
             "verlängert. Den Preis in Ihrer Währung zeigt der App Store an, bevor Sie bestätigen.</p>"),
            ("Muss jedes Familienmitglied ihn kaufen?",
             "<p>Nein. Der Family Pass unterstützt die Familienfreigabe von Apple – die Mitglieder Ihrer "
             "Apple-Familie erhalten ihn, ohne ihn erneut zu kaufen (das Teilen von Abos muss in den "
             "Einstellungen der Familienfreigabe aktiviert sein).</p>"),
            ("Wie kündige ich das Abo?",
             "<p>Das Abo wird von Apple verwaltet. Öffnen Sie auf dem iPhone <span class=\"kbd\">Einstellungen → "
             "[Ihr Name] → Abonnements → Wristalk</span> und tippen Sie auf „Abo kündigen“ – oder in Wristalk "
             "auf dem iPhone auf <span class=\"kbd\">Einstellungen → Familienpass → Abo verwalten</span>.</p>"
             "<p>Kündigen Sie mindestens 24 Stunden vor der Verlängerung, damit das nächste Jahr nicht berechnet "
             "wird. Der Family Pass bleibt bis zum Ende des bezahlten Zeitraums aktiv. Nur die Person, die ihn "
             "gekauft hat, kann ihn kündigen; das Löschen der App kündigt ihn nicht. Wenn Sie in der "
             "Gratiswoche kündigen, kann der Zugang sofort enden.</p>"),
            ("Kann ich mein Geld zurückbekommen?",
             "<p>Da Apple alle Zahlungen abwickelt, kümmert sich Apple auch um Erstattungen. Beantragen Sie eine "
             "Erstattung unter <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>.</p>"),
            ("Ich habe den Family Pass, aber Wristalk erkennt ihn nicht.",
             "<p>Prüfen Sie, dass Sie im App Store mit dem Apple Account angemeldet sind, der ihn gekauft hat "
             "(oder mit einem aus derselben Apple-Familie), und tippen Sie im Family-Pass-Bildschirm auf "
             "<span class=\"kbd\">Käufe wiederherstellen</span>. Hilft das nicht, schreiben Sie uns.</p>"),
        ]},
        {"id": "privacy", "title": "Datenschutz &amp; Sicherheit", "faqs": [
            ("Können Sie unsere Nachrichten anhören?",
             "<p>Nein. Sprache wird auf Ihren Geräten verschlüsselt, bevor sie sie verlässt, und nur die Geräte "
             "der Personen im Gespräch haben die Schlüssel. Unser Server leitet nur verschlüsselte Daten weiter "
             "und speichert sie kurz. Um zu prüfen, dass niemand einen Schlüssel ausgetauscht hat, vergleichen "
             "Sie die <strong>Sicherheitsnummer</strong> mit einem Kontakt: auf dem iPhone unter Personen, auf "
             "der Uhr in den Gesprächsdetails (<span class=\"kbd\">Sicherheitsnummer zeigen</span>).</p>"
             "<p>Was unser Server dagegen sieht – etwa wer wann mit wem spricht –, erklärt die "
             "<a href=\"%%PRIVACY%%\">Datenschutzerklärung</a>.</p>"),
            ("Wie lösche ich meine Daten?",
             "<ul><li><strong>iPhone:</strong> Einstellungen → Datenschutz → <span class=\"kbd\">Mein Konto "
             "löschen …</span></li>"
             "<li><strong>Uhr:</strong> Einstellungen → Datenschutz → <span class=\"kbd\">Meine Daten "
             "löschen</span></li>"
             "<li><strong>Für ein Kind (Verantwortliche):</strong> auf dem iPhone Kinder → das Kind → "
             "<span class=\"kbd\">Alle Daten von [Name] löschen …</span></li></ul>"
             "<p>Ihr Profil, Ihre Kontakte, Gruppenmitgliedschaften und Geräte werden sofort entfernt; die "
             "übrigen Einträge werden innerhalb von 30 Tagen gelöscht. Sind Sie der letzte Verantwortliche eines "
             "Kindes, löschen Sie zuerst die Daten des Kindes. Das Löschen Ihres Kontos kündigt den Family Pass "
             "nicht – kündigen Sie ihn in den App-Store-Einstellungen.</p>"),
            ("Wie melde ich jemanden?",
             "<p>Wenn Sie oder Ihr Kind sich durch jemanden unwohl fühlen oder jemand Wristalk missbraucht, "
             "melden Sie es uns – über „Melden“ in der App oder per E-Mail an %%EMAIL%% mit dem Anzeigenamen der "
             "Person, dem Gespräch und dem ungefähren Zeitpunkt. Da Sprache Ende-zu-Ende-verschlüsselt ist, "
             "können wir Nachrichten nicht anhören; wir handeln auf Grundlage Ihrer Meldung und der Angaben, die "
             "unser Server hat (etwa wer wann mit wem gesprochen hat). Meldungen werden 90 Tage aufbewahrt.</p>"
             "<p>Sie können eine Gruppe jederzeit verlassen, und Verantwortliche bestimmen, welche Kontakte ein "
             "Kind hat. Ist jemand in Gefahr, wenden Sie sich zuerst an den örtlichen Notruf.</p>"),
        ]},
    ],
}

# ---------------------------------------------------------------------------
PRIVACY = {
    "title": "Wristalk — Datenschutzerklärung",
    "description": "Wie Wristalk mit Ihren Daten umgeht: Ende-zu-Ende-verschlüsselte Sprache, wenige Daten, "
                   "kein Tracking.",
    "h1": "Datenschutzerklärung",
    "subtitle": "Wristalk · Gültig ab 27. September 2026",
    "body": """
<div class="summary">
  <p><strong>Das Wichtigste in Kürze</strong></p>
  <ul>
    <li>Ihre Sprachnachrichten sind Ende-zu-Ende-verschlüsselt. Wir können sie nicht anhören.</li>
    <li>Verschlüsselte Nachrichten werden gelöscht, sobald alle sie abgespielt haben – spätestens nach 10 Minuten,
      sofern eine Gruppe keine längere Einstellung nutzt (höchstens 24 Stunden).</li>
    <li>Wir speichern nur, was Wristalk zum Funktionieren braucht: Ihre Apple-Benutzerkennung, einen Anzeigenamen,
      die öffentlichen Schlüssel Ihrer Geräte, wer zu Ihrer Familie, Ihren Kontakten und Gruppen gehört, und für
      30 Tage, wer wann mit wem gesprochen hat.</li>
    <li>Keine Werbung, kein Tracking, keine Analyse, kein Verkauf von Daten.</li>
  </ul>
</div>

<h2>1. Verantwortlicher</h2>
<p>Wristalk wird angeboten von %%COMPANY%%, %%ADDRESS%% („wir“, „uns“). Wir sind Verantwortlicher im Sinne der DSGVO für die hier
beschriebenen personenbezogenen Daten. Kontakt: %%EMAIL%%.</p>

<h2>2. Welche Daten wir speichern und warum</h2>
<ul>
  <li><strong>Kontokennung.</strong> Die Benutzerkennung aus „Mit Apple anmelden“ und eine interne Benutzer-ID. Wir
    fragen bei Apple nur Ihren Namen ab – nicht Ihre E-Mail-Adresse.</li>
  <li><strong>Anzeigename.</strong> Ihr Vorname aus „Mit Apple anmelden“ oder ein Name, den Sie eingeben. Er wird Ihren
    Kontakten angezeigt.</li>
  <li><strong>Gerätedaten.</strong> Eine von der App erzeugte Geräte-ID, die öffentlichen Schlüssel Ihrer Geräte und
    Push-Token, damit wir Ihre Uhr oder Ihr iPhone benachrichtigen können. Werbe-IDs nutzen wir nicht.</li>
  <li><strong>Familien-, Kontakt- und Gruppenstruktur.</strong> Ihre Familie, Kontakte und Gruppen (Namen und
    Mitglieder), Einladungen, Verantwortlichen-Beziehungen, Einstellungen der Kindersicherung sowie Freigabeanfragen
    und -entscheidungen.</li>
  <li><strong>Gesprächs-Metadaten.</strong> Für jede Nachricht: Absender, Gespräch, Beginn und Ende sowie, ob jeder
    Empfänger sie erhalten bzw. abgespielt hat. Wir brauchen das, um Nachrichten zuzustellen, Absendern mitzuteilen,
    wenn jemand sie verpasst hat, und um Missbrauch zu bearbeiten. Diese Daten werden nach 30 Tagen gelöscht.</li>
  <li><strong>Verschlüsselte Sprachnachrichten.</strong> Nur als verschlüsselte Daten gespeichert, die wir nicht lesen
    können – bis jeder Empfänger die Nachricht abgespielt hat, höchstens 10 Minuten lang oder, falls die Person, die das
    Gespräch erstellt hat, eine längere Zeit gewählt hat, 1 bzw. 24 Stunden.</li>
  <li><strong>Meldungen.</strong> Wenn Sie jemanden melden, bewahren wir die Meldung und die zur Prüfung nötigen
    Angaben 90 Tage auf.</li>
  <li><strong>Abo-Status.</strong> Wenn Sie den Family Pass kaufen oder wiederherstellen, sendet uns die App Apples
    signierte Transaktionsdaten (Produkt, Zeitraum, ob es sich um einen Probezeitraum handelt), damit wir Wristalk für
    Ihre Familie freischalten können. Ihre Zahlungsdaten erhalten wir nie.</li>
  <li><strong>Technische Daten.</strong> Ihre IP-Adresse wird beim Verbindungsaufbau verarbeitet, um den Dienst zu
    erbringen und Missbrauch zu begrenzen (Ratenbegrenzung). Diese Einträge werden innerhalb von 2 Tagen gelöscht.
    Unsere Server-Protokolle enthalten keine Sprachinhalte.</li>
</ul>

<h2>3. Was wir nicht sehen können</h2>
<p>Sprache wird auf Ihrem Gerät verschlüsselt, bevor sie gesendet wird – mit Schlüsseln, die nur auf den Geräten der
Personen im Gespräch existieren. Unser Server leitet diese verschlüsselten Daten weiter und speichert sie kurz, kann
sie aber nicht entschlüsseln. Wir können also nicht anhören, abschreiben oder auswerten, was Sie sagen.</p>
<p>Um Nachrichten zuzustellen, sieht unser Server allerdings, wer zu welcher Familie, Kontaktliste und Gruppe gehört,
wer mit wem spricht, wann und wie lange, sowie die Größe der Daten. Push-Mitteilungen enthalten den Anzeigenamen des
Absenders und einen Verweis auf das Gespräch, niemals Sprachinhalte.</p>

<h2>4. Kein Tracking, keine Werbung, keine Analyse</h2>
<p>Wristalk enthält keine Werbung, keine Analyse-Tools und keine Tracking-SDKs von Drittanbietern. Wir verkaufen Ihre
Daten nicht, geben sie nicht für Werbezwecke weiter und erstellen keine Profile über Sie. Die App führt auf Ihrem
Gerät ein technisches Protokoll (ohne Sprache oder Nachrichteninhalte); es verlässt Ihr Gerät nur, wenn Sie es selbst
teilen, zum Beispiel mit uns für den Support.</p>

<h2>5. Dienstleister</h2>
<ul>
  <li><strong>Cloudflare, Inc.</strong> betreibt unseren Server (Nachrichtenvermittlung und Datenbank) in seinem
    weltweiten Netzwerk. Daten werden in den Rechenzentren dieses Netzwerks verarbeitet, die außerhalb Ihres Landes
    liegen können, auch in den USA.</li>
  <li><strong>Apple</strong> stellt „Mit Apple anmelden“ bereit, stellt Push-Mitteilungen zu (Apple Push Notification
    Service) und wickelt alle Zahlungen für den Family Pass über den App Store ab. Für diese Verarbeitung gilt die
    Datenschutzrichtlinie von Apple.</li>
</ul>
<p>Andere erhalten personenbezogene Daten von uns nur, wenn das Gesetz es verlangt.</p>

<h2>6. Speicherdauer</h2>
<ul>
  <li>Verschlüsselte Sprachnachrichten: bis alle sie abgespielt haben, höchstens 10 Minuten (oder gemäß Einstellung
    des Gesprächs, höchstens 24 Stunden).</li>
  <li>Gesprächs-Metadaten: 30 Tage.</li>
  <li>Meldungen: 90 Tage.</li>
  <li>Einladungscodes: 7 Tage nach Ablauf oder Verwendung gelöscht.</li>
  <li>Konto-, Geräte-, Familien-, Kontakt- und Gruppendaten: solange Ihr Konto besteht. Wenn Sie Ihr Konto löschen,
    werden Profil, Mitgliedschaften, Kontakte und Geräte sofort entfernt und die übrigen Einträge innerhalb von
    30 Tagen gelöscht.</li>
</ul>

<h2>7. Kinder</h2>
<p>Kinder nutzen Wristalk unter der Aufsicht eines Elternteils oder einer anderen verantwortlichen Person. Diese nimmt
das Kind in die Familie auf und bestimmt, mit wem es sprechen darf: Neue Kontakte und Gruppen brauchen ihre Freigabe,
sofern sie nichts anderes erlaubt. Verantwortliche können außerdem erlaubte Zeiten und Akku-Einstellungen
festlegen.</p>
<p>Wir erheben von Kindern nicht mehr Daten als von Erwachsenen, zeigen ihnen keine Werbung, und nichts, was ein Kind
sagt, können wir hören. Verantwortliche können alle Daten eines Kindes jederzeit in der iPhone-App löschen (Kinder →
das Kind → Alle Daten löschen) oder uns per E-Mail darum bitten.</p>

<h2>8. Rechtsgrundlagen (EWR, Vereinigtes Königreich und Schweiz)</h2>
<p>Wir verarbeiten Ihre Daten, um Wristalk im Rahmen unseres Vertrags mit Ihnen bereitzustellen (Art. 6 Abs. 1 lit. b
DSGVO), um Wristalk sicher zu halten und Meldungen über Missbrauch zu bearbeiten (berechtigte Interessen, Art. 6
Abs. 1 lit. f DSGVO) und um rechtliche Pflichten zu erfüllen (Art. 6 Abs. 1 lit. c DSGVO). Kinder unter dem in ihrem
Land geltenden Mindestalter für die Einwilligung nutzen Wristalk mit Einwilligung und unter Aufsicht ihrer Eltern
bzw. Verantwortlichen.</p>

<h2>9. Übermittlung in andere Länder</h2>
<p>Wir haben unseren Sitz in den USA, und unsere Dienstleister verarbeiten Daten weltweit. Werden Daten aus dem EWR,
dem Vereinigten Königreich oder der Schweiz in andere Länder übermittelt, stützen wir uns auf geeignete Garantien wie
die Standardvertragsklauseln der Europäischen Kommission oder einen Angemessenheitsbeschluss.</p>

<h2>10. Sicherheit</h2>
<p>Sprache ist Ende-zu-Ende-verschlüsselt. Die Schlüssel jedes Geräts werden in dessen Sicherheits-Hardware erzeugt
und dort aufbewahrt, und alle Verbindungen zu unserem Server sind verschlüsselt. Der Zugriff auf unsere Systeme ist
beschränkt.</p>

<h2>11. Ihre Rechte</h2>
<p>Je nach Wohnort haben Sie das Recht auf Auskunft über Ihre Daten, auf Berichtigung und Löschung, auf Einschränkung
der Verarbeitung, auf Widerspruch und auf Datenübertragbarkeit. Ihr Konto und Ihre Daten können Sie jederzeit selbst
löschen: auf dem iPhone unter Einstellungen → Datenschutz → Mein Konto löschen …, auf der Uhr unter Einstellungen →
Datenschutz → Meine Daten löschen. Für alle anderen Anliegen schreiben Sie uns an %%EMAIL%%. Außerdem können Sie sich
bei einer Datenschutz-Aufsichtsbehörde beschweren, insbesondere in dem Land, in dem Sie leben.</p>

<h2>12. Änderungen</h2>
<p>Wenn wir diese Erklärung ändern, veröffentlichen wir die neue Fassung hier mit neuem Gültigkeitsdatum und
informieren Sie über wesentliche Änderungen in geeigneter Weise.</p>

<h2>13. Kontakt</h2>
<p>%%COMPANY%%, %%ADDRESS%%<br>E-Mail: %%EMAIL%%</p>
<p style="font-size:14px;color:var(--faint)">Bei Abweichungen zwischen dieser Übersetzung und der englischen Fassung
ist die englische Fassung maßgeblich, soweit gesetzlich zulässig.</p>
""",
}

# ---------------------------------------------------------------------------
TERMS = {
    "title": "Wristalk — Nutzungsbedingungen",
    "description": "Nutzungsbedingungen für Wristalk, einschließlich des Family-Pass-Abos.",
    "h1": "Nutzungsbedingungen",
    "subtitle": "Wristalk · Gültig ab 27. September 2026",
    "body": """
<h2>1. Über diese Bedingungen</h2>
<p>Diese Bedingungen regeln die Nutzung der Wristalk-Apps für Apple Watch und iPhone und des zugehörigen Dienstes
(„Wristalk“), angeboten von %%COMPANY%%, %%ADDRESS%% („wir“, „uns“). Mit der Nutzung von Wristalk stimmen Sie diesen
Bedingungen zu. Sie ergänzen Apples Endbenutzer-Lizenzvertrag für lizenzierte Apps (Licensed Application End User
License Agreement); bei Widersprüchen gelten, soweit zulässig, diese Bedingungen.</p>

<h2>2. Der Dienst</h2>
<p>Mit Wristalk können freigegebene Kontakte und Gruppen einander kurze Sprachnachrichten senden (Push-to-Talk).
Nachrichten sind Ende-zu-Ende-verschlüsselt und werden nach dem Abspielen gelöscht, spätestens nach Ablauf der
Aufbewahrungszeit des Gesprächs. Wie Nachrichten zugestellt werden – automatisch oder per Mitteilung –, hängt vom
Gerätemodell, seinen Einstellungen und dem Netz ab.</p>
<p><strong>Wristalk ist kein Notrufdienst.</strong> Nachrichten können sich verzögern oder nicht ankommen, etwa ohne
Internetverbindung oder bei niedrigem Akku. Verlassen Sie sich im Notfall nicht auf Wristalk – wählen Sie den
örtlichen Notruf.</p>

<h2>3. Ihr Konto</h2>
<p>Sie melden sich mit Ihrem Apple Account an. Schützen Sie Ihre Geräte und verwenden Sie einen Anzeigenamen, mit dem
Sie sich nicht als jemand anderes ausgeben. Sie sind für die Aktivitäten Ihres Kontos und Ihrer Geräte
verantwortlich.</p>

<h2>4. Kinder und Verantwortliche</h2>
<p>Kinder dürfen Wristalk nur mit Einwilligung und unter Aufsicht eines Elternteils oder einer anderen
verantwortlichen Person nutzen, die die Nutzung des Kindes in einer Familie einrichtet und bestimmt, mit wem das Kind
sprechen darf. Verantwortliche sind für die Nutzung durch ihre Kinder verantwortlich und entscheiden, ob Wristalk für
sie geeignet ist.</p>

<h2>5. Family-Pass-Abo</h2>
<ul>
  <li>Wristalk ist kostenlos zu laden. Zum Sprechen braucht Ihre Familie einen aktiven Family Pass.</li>
  <li>Berechtigte Neukunden erhalten einen <strong>kostenlosen Probezeitraum von 7 Tagen</strong>. Danach ist der
    Family Pass ein <strong>Jahresabo, das sich automatisch verlängert</strong>, zu dem Preis, den der App Store vor
    Ihrer Bestätigung anzeigt.</li>
  <li>Die Zahlung wird von Apple über Ihren Apple Account abgerechnet, wenn der Probezeitraum endet (bzw. beim Kauf,
    wenn Sie keinen Anspruch auf den Probezeitraum haben). Das Abo verlängert sich jedes Jahr automatisch, sofern Sie
    es nicht spätestens 24 Stunden vor Ende des laufenden Zeitraums kündigen.</li>
  <li>Sie verwalten oder kündigen das Abo in den Einstellungen Ihres App-Store-Accounts (auf dem iPhone: Einstellungen
    → Ihr Name → Abonnements). Eine Kündigung wird zum Ende des laufenden Zeitraums wirksam; das Löschen der App oder
    Ihres Wristalk-Kontos kündigt das Abo nicht.</li>
  <li>Der Family Pass unterstützt die Familienfreigabe von Apple, sodass die Mitglieder der Apple-Familie der
    kaufenden Person ihn ohne Zusatzkosten nutzen können.</li>
  <li>Apple wickelt alle Zahlungen ab. Erstattungen bearbeitet Apple nach seinen Richtlinien
    (<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>); wir selbst können keine Erstattungen
    vornehmen.</li>
  <li>Ändert sich der Preis, informiert Apple Sie vorab gemäß seinen Regeln.</li>
</ul>

<h2>6. Zulässige Nutzung</h2>
<p>Bitte gehen Sie freundlich miteinander um. Bei der Nutzung von Wristalk dürfen Sie nicht:</p>
<ul>
  <li>andere belästigen, bedrohen, mobben, einschüchtern oder verfolgen oder hasserfüllte, sexuelle oder anderweitig
    missbräuchliche Inhalte senden;</li>
  <li>Rechtswidriges senden oder etwas, das Kinder ausnutzt oder gefährdet;</li>
  <li>versuchen, Kinder ohne Freigabe ihrer Verantwortlichen zu kontaktieren, oder die Kindersicherung umgehen;</li>
  <li>sich als andere Personen ausgeben oder Spam senden;</li>
  <li>Wristalk oder unsere Server stören, angreifen, überlasten oder sich unbefugten Zugang verschaffen oder anders als
    über die Wristalk-Apps automatisiert darauf zugreifen.</li>
</ul>
<p>Verstößt jemand gegen diese Regeln, melden Sie es in der App oder per E-Mail an %%EMAIL%%. Sie können Gruppen
jederzeit verlassen, und Verantwortliche bestimmen, welche Kontakte ein Kind hat. Wir können Konten sperren oder
beenden, die gegen diese Bedingungen verstoßen.</p>

<h2>7. Ihre Inhalte</h2>
<p>Was Sie sagen, gehört Ihnen. Da Sprache Ende-zu-Ende-verschlüsselt ist, haben wir keinen Zugriff darauf. Sie
erlauben uns lediglich, die verschlüsselten Daten zu übertragen und kurz zu speichern, soweit das für die Zustellung
Ihrer Nachrichten nötig ist. Für das, was Sie senden, sind Sie verantwortlich.</p>

<h2>8. Datenschutz</h2>
<p>Unsere <a href="%%PRIVACY%%">Datenschutzerklärung</a> erklärt, welche Daten wir verarbeiten und warum.</p>

<h2>9. Änderungen und Verfügbarkeit</h2>
<p>Wir entwickeln Wristalk weiter und können Funktionen ändern, hinzufügen oder entfernen. Wir bemühen uns um eine hohe
Verfügbarkeit, können aber nicht garantieren, dass Wristalk jederzeit ohne Unterbrechung funktioniert. Sollten wir
Wristalk einstellen, informieren wir Sie, soweit zumutbar, vorab.</p>

<h2>10. Gewährleistungsausschluss</h2>
<p>Soweit gesetzlich zulässig, wird Wristalk „wie besehen“ und „wie verfügbar“ bereitgestellt, ohne ausdrückliche oder
stillschweigende Gewährleistung, einschließlich der Gewährleistung der Marktgängigkeit, der Eignung für einen
bestimmten Zweck und der Nichtverletzung von Rechten Dritter.</p>

<h2>11. Haftungsbeschränkung</h2>
<p>Soweit gesetzlich zulässig, haften wir nicht für indirekte, zufällige, besondere oder Folgeschäden oder für
verlorene Daten oder nicht zugestellte Nachrichten, und unsere Gesamthaftung ist auf den Betrag begrenzt, den Sie in
den 12 Monaten vor dem Anspruch für den Family Pass gezahlt haben. Nichts in diesen Bedingungen beschränkt eine
Haftung, die gesetzlich nicht beschränkt werden kann, etwa bei Vorsatz, grober Fahrlässigkeit oder Verletzung von
Leben, Körper oder Gesundheit, oder Ihre Rechte nach zwingendem Verbraucherschutzrecht.</p>

<h2>12. Beendigung der Nutzung</h2>
<p>Sie können Wristalk jederzeit nicht mehr nutzen und Ihr Konto in der App löschen (iPhone: Einstellungen →
Datenschutz → Mein Konto löschen …; Uhr: Einstellungen → Datenschutz → Meine Daten löschen). Denken Sie daran, den
Family Pass separat in den App-Store-Einstellungen zu kündigen.</p>

<h2>13. Anwendbares Recht</h2>
<p>Für diese Bedingungen gilt das Recht %%JURISDICTION%% unter Ausschluss seiner Kollisionsnormen; zuständig sind die
dortigen Gerichte. Als Verbraucher behalten Sie zusätzlich den Schutz der zwingenden Vorschriften des Landes, in dem Sie
leben, und können Ansprüche auch vor den dortigen Gerichten geltend machen.</p>

<h2>14. Änderungen dieser Bedingungen</h2>
<p>Wir können diese Bedingungen aktualisieren. Wir veröffentlichen die neue Fassung hier mit neuem Gültigkeitsdatum und
informieren Sie über wesentliche Änderungen in geeigneter Weise. Nutzen Sie Wristalk nach deren Inkrafttreten weiter,
gelten die aktualisierten Bedingungen.</p>

<h2>15. Kontakt</h2>
<p>%%COMPANY%%, %%ADDRESS%%<br>E-Mail: %%EMAIL%%</p>
<p style="font-size:14px;color:var(--faint)">Bei Abweichungen zwischen dieser Übersetzung und der englischen Fassung
ist die englische Fassung maßgeblich, soweit gesetzlich zulässig.</p>
""",
}
