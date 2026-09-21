# Audit: Nairobi-Nutzerweg sprachlich und inhaltlich durchgängig

**Rolle:** Lokalisierung_Lead (Sprachen und Länderanpassung) · **Issue:** #3 · **Datum:** 2026-09-21
**Geprüfter Weg:** `index.html` → `hire.html` → `request.html` → `electricians-nairobi.html` / `solar-installers-nairobi.html` (+ `guide-choosing-solar-installer-kenya.html` als unterstützende Nairobi-Seite)
**Methode:** Statische Code-Prüfung des lokalen Website-Ordners (Root = `dist/`, Dateien identisch). Programmatischer Key-Vergleich der i18n-Packs. **Kein Browser-Rendering-Test durchgeführt** (kein Playwright-Lauf); RTL/visuelle Aussagen sind Code-Stichproben, keine Sichtprüfung. Website-Texte belegen kommunizierte Aussagen, nicht deren betriebliche Umsetzung.

---

## 1. Zusammenfassung

Der Nairobi-Nutzerweg funktioniert **auf Englisch** und weitgehend **auf Französisch**. Für **Portugiesisch, Arabisch und Chinesisch bricht der Weg ab dem ersten Screen**: Die komplette neue Website-Textschicht (`WEBSITE_COPY`, 108 Keys: Navigation, Hero, Leistungen, Prozess, CTAs, Footer) existiert nur in EN und FR — der Code-Fallback (`WEBSITE_COPY[l] || WEBSITE_COPY.en`) blendet für PT/AR/ZH still auf Englisch um. Ein Nairobi-Kunde, der oben rechts „ع" oder „中" wählt, sieht eine fast vollständig englische Seite — die Sprachauswahl suggeriert eine Abdeckung, die nicht existiert.

Das Haupt-i18n-Pack (485 Keys) ist dagegen vorbildlich: alle 5 Sprachen decken den Key-Bestand zu 100 % ab, Stichproben der Weg-relevanten Formular-Keys (`rq_*`) sind in FR/PT/AR/ZH tatsächlich übersetzt. Der Bruch liegt also nicht im Übersetzungssystem, sondern in **drei parallelen Copy-Dateien, die nur zweisprachig gepflegt werden**.

Positiv: Keine Fremdwährungen (€/$/£) auf dem gesamten Weg; Kenia ist Standardland (`DEFAULT_COUNTRY="KE"`), +254 steht an erster Stelle der Vorwahlliste, das Platzhalter-Telefonformat ist kenianisch; Ländernamen werden korrekt über `Intl.DisplayNames` lokalisiert; der Kenya-Solar-Guide nutzt KES, EPRA-Lizenzklassen (T1–T3) und KEBS — inhaltlich der stärkste lokalisierte Baustein, aber komplett unübersetzt.

**Kritischster Bruch (1 Zeile):** `assets/website-copy.js` + `assets/scout-copy.js` + `assets/network.js` existieren nur in EN/FR — PT/AR/ZH-Nutzer erhalten Startseite, Navigation, Einwilligungstext und Fehlermeldungen still auf Englisch.

---

## 2. Durchgang-Audit mit Fundstellen

### Schritt 0 — System (gilt für alle Schritte)

| # | Fundstelle | Befund |
|---|-----------|--------|
| F1 | `assets/website-copy.js` (gesamt; Fallback in `applyWebsiteCopy()`: `WEBSITE_COPY[l] \|\| WEBSITE_COPY.en`) | **Kritisch.** 108 Keys (Nav, Hero, Services, Prozessschritte, CTAs, Footer, Fehlertexte) nur in EN + FR. PT/AR/ZH fallen lautlos auf EN zurück. Betrifft `index.html`, `hire.html`, `request.html` und alle Stadtseiten. |
| F2 | `assets/scout-copy.js` (gesamt) | 71 Keys (`sc_nav`, Scout-Teaser auf der Startseite) nur EN + FR → gleicher stiller EN-Fallback für PT/AR/ZH. |
| F3 | `assets/network.js` (`words`-Objekt nur `en`/`fr`; `t = k => (words[lang==='fr'?'fr':'en'][k] \|\| k)`) | Alle Netzwerk-Texte inkl. **Einwilligungstext** nur EN/FR. Der `t()`-Fallback ist hart auf EN verdrahtet — nicht auf das Hauptpack. |
| F4 | `assets/app.js:113–119` (`applyI18n`, `T = k => (I18N[lang][k]) \|\| I18N.en[k] \|\| k`) | Fallback-Logik selbst ist sauber (Key → EN → Key). Problem ist nicht der Mechanismus, sondern fehlende Inhalte (F1–F3). |

### Schritt 1 — `index.html` (Startseite)

| # | Fundstelle | Befund |
|---|-----------|--------|
| F5 | `index.html` (gesamt, 43 eindeutige `data-i18n`-Keys) | **100 % der sichtbaren Startseiten-Texte** stammen aus `WEBSITE_COPY`/`SCOUT_COPY` → für PT/AR/ZH komplett Englisch (Hero „Good work starts with the right technician.", alle vier Leistungskacheln, Prozess, CTAs „Describe your project"). Kein einziger Key fehlt technisch — inhaltlich ist die Seite in 3 von 5 Sprachen unlokalisiert. |
| F6 | `index.html` Header | Sprachumschalter EN/FR/PT/ع/中 vorhanden und funktional (`loadLang` lädt Packs bei Bedarf, `localStorage va_lang`). Die Auswahl beweist keine Abdeckung — genau der hier dokumentierte Bruch. |

### Schritt 2 — `hire.html` (Gewerkeauswahl)

| # | Fundstelle | Befund |
|---|-----------|--------|
| F7 | `hire.html` (25 eindeutige Keys: `hire_title`, `hire_desc`, `services_title`, `service_*`) | Gleicher Befund wie F5: gesamte Seite EN für PT/AR/ZH. Die Gewerke-Kacheln sind die Kernhandlung der Seite — unübersetzte Kernhandlung nach Abnahmekriterium. |

### Schritt 3 — `request.html` (Anfrageformular)

| # | Fundstelle | Befund |
|---|-----------|--------|
| F8 | `request.html:88` (`data-i18n="web_followup"` „Follow up on WhatsApp") | Key existiert nur in `WEBSITE_COPY` EN/FR → CTA auf der Erfolgsseite für PT/AR/ZH englisch. |
| F9 | `request.html:158` (`T("web_details_error")`), `:215/:223` (`T("web_connection_error")`) | Beide Fehlermeldungen nur EN/FR (`WEBSITE_COPY`) → Validierungs- und Verbindungsfehler für PT/AR/ZH englisch. Die `rq_*`-Formularfehler (`rq_err_name`, `rq_err_phone`) sind dagegen im Hauptpack in allen 5 Sprachen übersetzt — inkonsistente Fehlersprache auf derselben Seite. |
| F10 | `request.html:79` + `:119` (`#rq-consent-text` via `VA_NETWORK.t('consent')`) | **Rechtlich sensibel:** Der Datenschutz-Einwilligungstext erscheint für PT/AR/ZH auf Englisch (F3). HTML-Default ist ebenfalls hartcodiert EN. Einwilligung in einer Sprache, die der Nutzer evtl. nicht versteht. |
| F11 | `request.html:181–184` (WhatsApp-Übergabetext) | Nachricht immer Englisch: `"Hello Voltage Africa — new request: " + catEn + " in " + place …`, Kategorie explizit EN (`I18N.en["cat_"+spec]`). Für Nairobi (EN = Amtssprache) vertretbar, für FR/PT/AR/ZH-Nutzer inkonsistent. Bewusste Entscheidung oder Bug — aktuell undokumentiert. |
| F12 | `assets/data.js:46` (`WA_BUSINESS = "491729909687"`) | WhatsApp-Follow-up läuft über eine **deutsche +49-Nummer**. Für Nairobi-Kunden: internationale Nummer, keine lokale Vertrauensadresse, ggf. Kosten/IR-Erwartung. Keine kenianische oder panafrikanische Nummer hinterlegt. |
| F13 | `request.html:57–68` (Vorwahl-Dropdown) | Ländernamen hartcodiert englisch („🇰🇪 +254 Kenya", „🌍 Other country code"), kein i18n. **Positiv:** Kenia +254 an erster Stelle. |
| F14 | `request.html:70–71` (Platzhalter) | `placeholder="+242"` (Kongo-Beispiel für „andere Vorwahl") ist willkürlich/verwirrend und nicht i18n-pflegbar; `placeholder="712345678"` ist korrektes kenianisches Format — gut, aber ebenfalls hartcodiert. |
| F15 | `electricians-nairobi.html` / `solar-installers-nairobi.html` → `request.html?spec=…&city=Nairobi` (jeweils im CTA) | Links füllen Stadt, aber **nicht das Land** vor (`cc=KE` fehlt); `request.html` nutzt `DEFAULT_COUNTRY="KE"` nicht. Nairobi-Nutzer muss Kenia manuell wählen — vermeidbare Reibung genau auf dem Zielmarktweg. |
| — | `request.html:109` + `assets/app.js` (`countryOptions`, `countryName`) | **Positiv:** Länderauswahl via `Intl.DisplayNames` in der aktiven Sprache, sortiert per `localeCompare` — vorbildlich. |
| — | `request.html:105` (`tf()`-Pattern) | **Positiv:** `rq_phone_hint`, `rq_err_name`, `rq_err_phone`, `rq_sending` existieren im Hauptpack in allen 5 Sprachen; EN-Fallbacks greifen nicht. |

### Schritt 4 — Nairobi-Stadtseiten

| # | Fundstelle | Befund |
|---|-----------|--------|
| F16 | `electricians-nairobi.html`, `solar-installers-nairobi.html` (Hauptinhalt: H1, Lede, H2 „Prepare a useful request", Ratschlag-Absatz) | **Komplett hartcodiert Englisch, null `data-i18n`** im Main-Bereich (nur Nav/Footer haben Keys). In allen 5 Sprachen englisch — auch in EN ist der Inhalt generisch (2 Absätze, austauschbar mit jeder anderen Stadt). |
| F17 | beide Dateien, `<meta property="og:title" content="How it works \| Voltage Africa">` | **Copy-Paste-Fehler:** og:title/og:description von „How it works" — falscher Titel beim Teilen in WhatsApp/Social (genau der Kanal, über den Nairobi-Kunden kommen). |
| F18 | beide Dateien (Inhalt) | Kein Nairobi-Bezug jenseits des Stadtnamens: keine Stadtteile/Einsatzgebiete, keine EPRA-/KEBS-Erwähnung, keine KES-Preisindikation, kein M-Pesa/Safaricom-Kontext. SEO- und Vertrauenschance ungenutzt. |

### Schritt 5 — `guide-choosing-solar-installer-kenya.html` (unterstützend)

| # | Fundstelle | Befund |
|---|-----------|--------|
| F19 | gesamte Datei (74 hartcodierte Textknoten, nur 17 `data-i18n` in Nav/Footer) | **EN-only.** Inhaltlich stark lokalisiert (EPRA-Lizenzklassen T1–T3, KEBS, KES-Preisindikationen 60.000–150.000 / 450.000–1.000.000+, „as of 2026"), aber in keiner weiteren Sprache verfügbar; kein M-Pesa/Safaricom- oder Stadtteil-Bezug. |
| F20 | Guide-CTAs → `request.html` (ohne `cc=KE`/`city=Nairobi`) | Wie F15: Wegübergang ohne Kontextvorbefüllung. |

### Währung, Zahlen, Datum (gesamter Weg)

- **Keine Fremdwährung** (€/$/£, EUR/USD/GBP) auf keiner Weg-Seite — sauber.
- KES erscheint ausschließlich im EN-Guide (`KES 60,000–150,000` — EN-Tausenderformat; bei künftiger Übersetzung sind Zahlformate zu lokalisieren: FR `60 000`, AR-Ziffern klären).
- Keine dynamischen Datumsformate auf dem Weg (© 2026 statisch; `datePublished` ISO 8601). Kein akuter Bruch.

---

## 3. Sprachabdeckungs-Matrix (programmatisch geprüft, 2026-09-21)

### 3.1 Haupt-i18n-Pack — `assets/i18n.js` (EN inline) + `assets/i18n/{fr,pt,ar,zh}.js`

| Sprache | Keys | Fehlende Keys | Überzählige Keys | Werte identisch zu EN |
|---------|------|---------------|-------------------|----------------------|
| EN (Basis) | 485 | — | — | — |
| FR | 485 | 0 | 0 | 10 |
| PT | 485 | 0 | 0 | 8 |
| AR | 485 | 0 | 0 | 0 |
| ZH | 485 | 0 | 0 | 1 |

Identische Werte im Einzelnen: `rw_bonus` („Bonus"), `ms_title` („Messages"), `db_tab3` („📘 Playbook"), `feat_1_t` („Solar & PV"), `foot_legal` („Legal"), `nav_rankings` („Rankings"), `aria_menu` („Menu"), `nav_guides` („Guides"), `nav_messages` („💬 Messages"), `lvl_4` („Expert"), `lvl_5` („Master Partner"), `su_role_scout` („🧭 Scout").
→ Einordnung: „Contact", „Bonus", „Menu", „Messages", „Expert" sind legitime Kognate/Eigennamen. **Prüfbedürftig (mutmaßlich unübersetzt):** `nav_rankings`, `nav_guides`, `db_tab3`, `foot_legal` in FR und PT (betreffen Rankings-/Rechtsseiten, nicht den Kernweg). `lvl_5` „Master Partner" ist ggf. bewusster Markenname — zu entscheiden, nicht still zu übernehmen.

### 3.2 Sekundäre Copy-Dateien — der eigentliche Gap

| Datei | Keys | EN | FR | PT | AR | ZH | Fallback für PT/AR/ZH |
|-------|------|----|----|----|----|----|----------------------|
| `assets/website-copy.js` (`WEBSITE_COPY`) | 108 | ✅ | ✅ | ❌ | ❌ | ❌ | still EN (`WEBSITE_COPY.en`) |
| `assets/scout-copy.js` (`SCOUT_COPY`) | 71 | ✅ | ✅ | ❌ | ❌ | ❌ | still EN |
| `assets/network-copy.js` | 8 | ✅ | ✅ | ❌ | ❌ | ❌ | still EN |
| `assets/network.js` (`words`, inkl. `consent`) | ~40 | ✅ | ✅ | ❌ | ❌ | ❌ | hart EN (`lang==='fr'?'fr':'en'`) |

**Weg-Bilanz:** Für PT/AR/ZH sind auf dem Nairobi-Nutzerweg grob geschätzt **~60–70 % der sichtbaren Texte englisch** (komplette Startseite, komplette Gewerkeseite, Nav/Footer, Consent, 3 Fehlertexte, Follow-up-CTA; übersetzt bleiben nur die `rq_*`-Formularlabels im Hauptpack).

---

## 4. Nairobi-Lokalisierungsanforderungen (inhaltlich)

| Thema | Anforderung | Status heute |
|-------|-------------|--------------|
| Währung | KES mit klarer Mengenangabe und Datums-/Quellenvermerk, wo Preise genannt werden | Nur im Guide (KES, „as of 2026") — gut; Stadtseiten ohne jede Preisindikation |
| Vertrauensanker | EPRA-Registrierung (Solar-PV-Lizenzklassen T1–T3) und KEBS-konforme Komponenten auf den **Stadtseiten** und im Anfrage-Ratgebertext nennen | Nur im Guide vorhanden; Stadtseiten generisch |
| Einsatzgebiete | Nairobi-Stadtteile/Korridore konkret nennen (z. B. Westlands, Kilimani, Karen, Embakasi, Kasarani, Ngong Road, Thika Road) — signalisiert echte lokale Abdeckung | Nirgends vorhanden |
| M-Pesa/Safaricom | Erwähnen, wo Zahlungsabwicklung Thema ist (Ratgeber/FAQ) — **nicht** als Plattform-Zahlungsversprechen ohne belegte Funktion | Nicht vorhanden (auch nicht überstrapaziert — korrekt) |
| Telefon/WhatsApp | Kenianisches Format +254 7XX XXX XXX (Platzhalter bereits korrekt); Follow-up über lokale oder klar gekennzeichnete internationale Nummer | Format ok; Nummer ist +49 (F12) |
| Sprache Kenia | Englisch ist Amtssprache und im Geschäftsverkehr Nairobis tragfähig — der EN-Weg ist legitim. **Swahili wäre die fachlich relevante 6. Sprache für Kenia** (vor ZH); aktuell nicht angeboten | Kein Swahili |
| Sheng/Swahili-Nuancen | **Nicht** in UI-Kerntexten, Consent, Formularen (informell, uneinheitlich, unprofessionell im Vermittlungskontext). Angemessen allenfalls punktuell in lokalem Marketing-Material; erklärte Begriffe wie „fundi" (Handwerker) können im Guide-Fließtext mit Glossar funktionieren | Korrekt nicht vorhanden — kein Handlungsbedarf außer Leitlinie festhalten |

---

## 5. RTL-/AR- und ZH-Sonderprüfung (Code-Stichprobe, keine Sichtprüfung)

- **Grundgerüst korrekt:** `applyI18n()` setzt `document.documentElement.dir = "rtl"` für AR und `lang` korrekt (`assets/app.js:115–116`); Sprachwechsel lädt das AR-Pack bei Bedarf.
- **CSS:** `style.css` enthält 8 `[dir="rtl"]`-Blöcke (ausschließlich `letter-spacing:0`-Resets) und 27 logische Properties (`margin-inline` u. a.); `website.css` 0 RTL-Blöcke, 12 logische Properties. Flex-Layouts mit `gap` und `text-align:start` im Formular sind richtungsneutral — Code-seitig plausibel, **aber ohne Browser-Verifikation nicht als geprüft zu behaupten**. Offene Risiken: Icon-Pfeile/Emoji in Buttons, `flex-direction`-Umkehr in `#rq-phone-row`, Telefon-Input (sollte `dir="ltr"` erhalten für Ziffern).
- **Praxisrelevanz begrenzt:** Für AR-Nutzer bleiben Startseite, Navigation, Consent und Fehlertexte ohnehin englisch (F1–F3, F9, F10) — RTL greift aktuell nur am Hauptpack-Content (Formularlabels). Erst nach F1–F3 lohnt ein vollständiger RTL-Sichtcheck.
- **AR-Pack:** vollständig (0 fehlende Keys, 0 unübersetzte Werte in der Stichprobe — `rq_title` „اطلب فنّيًا", `rq_btn` „احصل على مطابقة — مجانًا" vorhanden und idiomatisch wirkend; Native-Review nicht erfolgt, daher nicht als geprüft behauptet).
- **ZH-Pack:** vollständig; einzige EN-identische Stelle `su_role_scout` („🧭 Scout") — plausibel als Eigenname. ZH hat auf dem Weg denselben WEBSITE_COPY-Bruch wie PT/AR. Für Nairobi ist ZH nachrangig (SW wäre relevanter, s. § 4).

---

## 6. Priorisierte Fix-Liste

### Quick Wins (kleiner Diff, große Wirkung)

| Prio | Datei | Änderung |
|------|-------|----------|
| Q1 | `assets/website-copy.js` (+ `scout-copy.js`, `network.js words`) | PT-, AR-, ZH-Blöcke ergänzen — zumindest die ~40 weg-relevanten Keys (Nav: `web_hire`, `web_tech`, `sc_nav`, `web_how`, `web_foot`; Home: `home_*`, `services_*`, `service_*`, `step*`, `tech_*`, `web_request`, `web_join`; Formular-Nah: `web_followup`, `web_details_error`, `web_connection_error`, `consent`, `routing`). Größter Hebel der gesamten Liste: macht den Weg in 3 Sprachen erst benutzbar. Maschineller Entwurf + Native-Review-Flag. |
| Q2 | `electricians-nairobi.html`, `solar-installers-nairobi.html` | og:title/og:description korrigieren (je 2 Zeilen) — behebt falschen Share-Text in WhatsApp. |
| Q3 | beide Nairobi-Seiten + Guide (CTA-Links) und `request.html` | `cc=KE` an Weg-Links anhängen; in `request.html` `DEFAULT_COUNTRY` als Vorauswahl nutzen. |
| Q4 | `request.html:79/119` + Hauptpack | Einwilligungstext als `rq_consent`-Key ins Hauptpack (485-Key-System, alle 5 Sprachen) statt `VA_NETWORK.words` — behebt den rechtlich sensibelsten Bruch strukturell. |
| Q5 | `request.html:70` | Platzhalter `+242` durch neutrales Beispiel ersetzen oder per `data-i18n-ph` pflegbar machen. |

### Mittelfristig

| Prio | Datei | Änderung |
|------|-------|----------|
| M1 | `electricians-nairobi.html`, `solar-installers-nairobi.html` | Lokaler Content-Block: EPRA/KEBS-Vertrauenshinweis, Einsatzgebiete (Stadtteile), ggf. KES-Preisindikation mit Datum — als i18n-Keys, nicht hartcodiert. |
| M2 | `assets/i18n/{fr,pt}.js` | `nav_rankings`, `nav_guides`, `db_tab3`, `foot_legal`, `nav_messages` native prüfen/nachziehen. |
| M3 | `request.html:57–68` | Vorwahl-Dropdown über `Intl.DisplayNames` lokalisieren (Muster existiert bereits in `countryOptions`). |
| M4 | `request.html:181–184` | WhatsApp-Übergabetext: Kategorie in Nutzersprache (`I18N[lang]`) oder bewusst EN festlegen und als Entscheidung dokumentieren; Klärung einer lokalen/kenianischen WA-Nummer (F12). |
| M5 | `guide-choosing-solar-installer-kenya.html` | Übersetzung priorisieren (FR zuerst — frankophone Nachbarmärkte) oder EN-only kennzeichnen; bei Übersetzung KES-Zahlformate lokalisieren. |

### Workflow-Vorschlag (neue Seiten/Keys)

1. **Single Source:** Neue sichtbare Texte nur als Keys — EN zuerst ins Hauptpack bzw. `WEBSITE_COPY`. Key-Diff-Skript (die hier verwendete Prüfung) als `scripts/check_i18n.py` versionieren und bei jeder Änderung laufen lassen: fehlende Keys = Build-Fehler.
2. **Keine neuen Zweisprachen-Dateien:** `WEBSITE_COPY`-Pattern (nur EN/FR) nicht mehr ausweiten; mittelfristig in das 5-Sprachen-Hauptpack konsolidieren.
3. **Übersetzung:** maschineller Entwurf pro Sprache, dann Native-Review mit Checkliste (Kernhandlungen, Consent/Rechtstexte, Zahlen/Währung, RTL); offene Native-Reviews im Key als Flag sichtbar (`"key@todo-native"`) bis Abnahme.
4. **Abnahme (aus Skill):** keine leeren Labels, keine unübersetzten Kernhandlungen, Consent/Rechtstexte vollständig — Sprachauswahl ohne dahinterliegende Übersetzung gilt als Defekt, nicht als Feature.

---

## 7. Drei nächste Maßnahmen

1. **Q1 umsetzen:** PT/AR/ZH für `WEBSITE_COPY`, `SCOUT_COPY` und `network.js words` (weg-relevante Keys zuerst) als maschinellen Entwurf ergänzen, Native-Review einplanen — danach erstmals vollständiger PT/AR/ZH-Durchgang testbar.
2. **Q2–Q5 als ein Bündel umsetzen** (og-Tags Nairobi, `cc=KE`-Vorbefüllung, `rq_consent`-Key, Platzhalter) und danach den Nairobi-Weg EN + AR (RTL-Stichprobe im Browser) + ZH vollständig durchklicken.
3. **Sprachstrategie Kenia entscheiden:** Swahili als 6. Sprache fachlich bewerten (Zielmarkt Nairobi; relevanter als ZH für diesen Weg) und Native-Review-Prozess benennen (wer prüft, mit welcher Checkliste, welche Abnahme).

---

*Methodik-Hinweis: Alle Fundstellen stammen aus dem lokalen Code-Stand 2026-09-15/16 (`?v=20260915/16`). Root- und `dist/`-Dateien sind byteidentisch. Keine Browser-Ausführung, kein Backend-Zugriff, keine Native-Reviews erfolgt; entsprechende Punkte sind als offen markiert.*
