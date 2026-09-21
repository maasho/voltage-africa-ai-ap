# Accessibility- und Mobile-Audit — Voltage Africa Website

**Datum:** 2026-09-21
**Rolle:** Accessibility_Auditor (Mobile Nutzung und Barrierefreiheit)
**Standard:** WCAG 2.2 Level AA (Stichprobe)
**Geprüfter Stand:** lokales Repository `voltage-africa-website/` (Stand 15.–21.09.2026)
**Stichprobe (6 Seiten):** index.html, hire.html, request.html, signup.html, members.html, calculators.html
**Methode:** Code-Audit (HTML/CSS/JS direkt im Quelltext), Kontrastberechnung aus den CSS-Farbwerten, Asset-/Seitengewichts-Analyse. HTML-Dateien sind minifiziert (eine Zeile); Fundstellen nennen daher Element/Kontext plus Zeile der aufbereiteten Kopie (`.tmp/*-pretty.html`).

**Prüfumfang / Grenzen (offen):**
- Kein Screenreader-Test (NVDA/TalkBack) durchgeführt — als offener Punkt markiert. Keine Konformitätsaussage, nur code-basierte Befunde.
- Kein Live-Test im Browser und kein echter 3G-Feldtest; Netzabschätzungen sind Berechnungen aus Dateigrößen.
- WCAG-Fundstellen beziehen sich auf WCAG 2.2 (ab 2.4.11 neu in 2.2).

---

## 1. Zusammenfassung

Die Website ist für die Zielgruppe (günstige Android-Geräte, langsame Netze, kleine Displays) **grundsolide gebaut**: leichte Seiten (47–61 KB gzip, 10–13 Requests), WebP mit srcset, System-Fonts, sauberes Caching/Kompression in `.htaccess`, Textkontraste durchgehend AA-konform, konsistente Formular-Labels und gute RTL-Umschaltung per JS.

Drei kritische Lücken betreffen aber genau die zentralen Aufgaben-Seiten (request/signup/calculators): fehlende `main`-Landmarke und Skip-Link, eine für Screenreader unsichtbare Signup-Erfolgsmeldung und ein unterdrückter Tastaturfokus in den Rechnern. Dazu kommen AA-Verletzungen bei Nicht-Text-Kontrasten (Formularrahmen 1,34:1) und fehlende aria-Verknüpfung der Fehlermeldungen.

**Befunde gesamt: 14 — davon kritisch: 3 · mittel: 6 · niedrig: 5**

| Bereich | Urteil |
|---|---|
| Textkontraste | bestanden (5,4–13,1:1) |
| Nicht-Text-Kontraste (1.4.11) | nicht bestanden (Rahmen 1,34:1 / 1,96:1) |
| Landmarken / Bypass-Blöcke (2.4.1) | nicht bestanden auf 3 von 6 Seiten |
| Statusmeldungen (4.1.3) | nicht bestanden (signup Erfolg, Sprachwechsel) |
| Fokus-Sichtbarkeit (2.4.7/2.4.11) | global gut, auf calculators.html unterdrückt |
| Tastatur-Bedienung | grundsätzlich gegeben (Burger aria-expanded, Escape, display:none-Nav) |
| Mobile Performance | Seitengewicht im 3G-Budget; Verbesserung bei JS-Bündelung möglich |
| RTL (Arabisch) | funktional vorhanden, Detail-Mängel (letter-spacing) |

---

## 2. WCAG-Befunde mit Belegen

### Kritisch

**K1 — Keine `main`-Landmarke und kein Skip-Link auf request.html, signup.html, calculators.html**
- **Kriterium:** 2.4.1 Bypass Blocks (A), 1.3.1 Info and Relationships (A)
- **Beleg:** `<body>` wird jeweils direkt von `<header>` gefolgt, Inhalt liegt in nackten `<section>`-Blöcken (request-pretty Z. 39–40, signup-pretty Z. 44–45, calculators-pretty Z. 63–64). index/hire/members.html haben dagegen Skip-Link + `<main id="main">` (index-pretty Z. 17, 43).
- **Wirkung:** Tastatur- und Screenreader-Nutzer müssen auf den drei wichtigsten Seiten (Projektanfrage, Registrierung) bei jedem Aufruf durch die komplette Kopfzeile mit 5 Sprachbuttons tabben; Hauptbereich ist nicht anspringbar.

**K2 — signup.html: Erfolgsbestätigung wird für Screenreader nicht angekündigt**
- **Kriterium:** 4.1.3 Status Messages (AA); ergänzend 2.4.3 Focus Order (A)
- **Beleg:** `showConfirm()` (signup-pretty Z. 242–251) ersetzt das Formular per `innerHTML`; der neue Inhalt hat weder `role="status"`/`aria-live` noch `tabindex="-1"` + Fokusverschiebung. request.html macht es korrekt (`#rq-success` mit `role="status" tabindex="-1"` und `.focus()`, request-pretty Z. 128, 263–266).
- **Wirkung:** Screenreader-Nutzer erfahren nach dem Absenden nicht, dass der Bestätigungslink verschickt wurde — Kernabschluss der Registrierung entfällt.

**K3 — calculators.html: Tastaturfokus auf Eingabefeldern unterdrückt**
- **Kriterium:** 2.4.7 Focus Visible (A), 2.4.11 Focus Not Obscured/Appearance (AA, WCAG 2.2)
- **Beleg:** Inline-Style `.calc-card input:focus,.calc-card select:focus{border-color:var(--green);outline:none}` (calculators-pretty Z. 44). Spezifität (0,2,1) schlägt die globale Regel `input:focus-visible{outline:2.5px solid var(--green)}` aus style.css Z. 21–23 (0,1,1). Übrig bleibt nur eine 1,5-px-Rahmenfarbänderung von `#d6e1db` nach `#116044`.
- **Wirkung:** Tastaturnutzer sehen auf der Rechnerseite nicht, welches Feld aktiv ist.

### Mittel

**M1 — Formularfeld-Rahmen unter Nicht-Text-Kontrast 3:1**
- **Kriterium:** 1.4.11 Non-text Contrast (AA)
- **Beleg:** `--line:#d6e1db` (website.css Z. 2) auf weißem Grund = **1,34:1** (berechnet). Alle Inputs/Selects/Textareas nutzen diesen Rahmen (calculators-pretty Z. 42, auth-card-Regeln).
- **Wirkung:** Sehbehinderte Nutzer erkennen die Feldgrenzen der Formulare nicht sicher — bei grellem Sonnenlicht auf günstigen Displays zusätzlich kritisch.

**M2 — Ghost-Button-Rahmen unter 3:1**
- **Kriterium:** 1.4.11 Non-text Contrast (AA)
- **Beleg:** `.btn.ghost{border:1px solid #a9beb3}` (website.css Z. 4) = **1,96:1** auf Weiß.

**M3 — Fehlermeldungen nicht mit Feldern verknüpft (request.html)**
- **Kriterium:** 1.3.1 / 3.3.1 (A)
- **Beleg:** Fehlercontainer `#rq-name-err`, `#rq-phone-err` (request-pretty Z. 83, 106) sind weder per `aria-describedby` an die Inputs gebunden noch wird die Fehler-ID referenziert; `aria-describedby` kommt im gesamten Projekt nicht vor (Grep über alle HTML/JS: 0 Treffer).
- **Wirkung:** Screenreader lesen beim Fokussieren des fehlerhaften Feldes nur „ungültiger Eintrag", nicht die konkrete Meldung.

**M4 — signup.html: nur generische Fehlermeldung, kein Fokus-Management bei Validierungsfehlern**
- **Kriterium:** 3.3.1 Error Identification (A), 3.3.3 Error Suggestion (AA)
- **Beleg:** Submit-Handler (signup-pretty Z. 230–241) setzt pro Feld nur Rahmenfarbe + `aria-invalid` und eine Sammelmeldung „Please fill in all fields correctly."; anders als request.html (Z. 249–252) wird nicht auf das erste fehlerhafte Feld fokussiert.
- **Wirkung:** Nutzer erfahren nicht, *welches* Feld wie zu korrigieren ist — auf kleinem Display mit 5 Pflichtfeldern spürbar.

**M5 — calculators.html: ungültige Eingabe schlägt lautlos fehl**
- **Kriterium:** 3.3.1 Error Identification (A)
- **Beleg:** `computeSolar()` (calculators-pretty Z. 286–292): bei ungültiger Eingabe wird das Ergebnis nur per `res.hidden = true` ausgeblendet — keine Fehlermeldung, obwohl das Formular `novalidate` nutzt (Z. 111).
- **Wirkung:** Nutzer interpretieren das als „Rechner kaputt".

**M6 — Sprachwechsel ohne Ankündigung**
- **Kriterium:** 4.1.3 Status Messages (AA)
- **Beleg:** `applyI18n()` (app.js Z. 113–123) ersetzt alle Texte per `textContent`, ohne Live-Region oder Hinweis; der Klick auf einen Sprachbutton erzeugt keine Statusmeldung.

### Niedrig

**N1 — Footer-Logo-Zeichen „ϟ" ohne `aria-hidden`**
- 1.1.1 (A) — alle 6 Seiten, Footer (index-pretty Z. 142 u. a.); im Header korrekt mit `aria-hidden="true"` (Z. 21). Screenreader lesen ein Symbol vor „Voltage Africa".

**N2 — Touch-Targets der Sprachbuttons knapp**
- 2.5.8 Target Size Minimum (AA, WCAG 2.2): formal erfüllt (≥24 px), aber 25–29 × 36 px (website.css Z. 4, Z. 8) liegen deutlich unter der 44-px-Empfehlung — relevant für die wichtigste Interaktion der Zielgruppe.

**N3 — Arabisch: `letter-spacing` nicht zurückgesetzt**
- `.eyebrow{letter-spacing:1.8px}` (website.css Z. 4) hat keinen `[dir="rtl"]`-Reset (style.css Z. 48 ff. löst das für andere Klassen, website.css enthält keinen einzigen `dir=`-Selektor). Arabische Eyebrow-Texte werden durch Zeichenabstand schwerer lesbar.

**N4 — `.reveal`-Inhalte ohne JavaScript unsichtbar**
- `.reveal{opacity:0;transform:translateY(22px)}` (style.css Z. 239); ohne JS (abgebrochenes Laden auf 2G/3G, Fehler in einem der 7 Skripte) bleibt Inhalt unsichtbar. Reduced-Motion ist dagegen sauber global abgedeckt (website.css Z. 12).

**N5 — Hinweis außerhalb der Stichprobe: Endlos-Animationen ohne Reduced-Motion-Schutz**
- `animation:shine 4.2s infinite` (style.css Z. 421–422) auf Profil-/Fut-Karten-Seiten, die nur style.css laden; `covermove` (Z. 608–609) ist für `.p2-cover` geschützt (Z. 610), `shine` nicht. 2.2.2 (A) prüfen, sobald diese Seiten in die Stichprobe kommen.

### Positivbefunde (beibehalten)

- Textkontraste alle ≥ 4,5:1 (z. B. muted `#50645e` auf Weiß 6,31:1; weiß auf Grün `#116044` 7,55:1; rot `#c0392b` 5,44:1) — berechnet aus website.css/style.css.
- Globale `:focus-visible`-Markierung 2,5 px Grün (7,55:1) vorhanden (style.css Z. 21–23).
- Mobile Navigation sauber: `display:none` im geschlossenen Zustand (aus Tab-Reihenfolge), `aria-expanded`, Escape schließt und fokussiert zurück (app.js Z. 143–152).
- RTL: `document.documentElement.dir = "rtl"` bei Arabisch, `lang` wird umgestellt (app.js Z. 115–116), logische CSS-Eigenschaften (`inset-inline`, `padding-inline`) durchgängig.
- request.html: vollständige Labels, `role="alert"`-Fehlercontainer, Fokus auf erstes Fehlerfeld, Erfolgsmeldung mit `role="status"` + Fokus.
- Viewport ohne Zoom-Sperre; Bildmaße (width/height) gegen CLS; native `details/summary`; `type="tel"` mit `inputmode`/`autocomplete`.

---

## 3. Performance- und Mobile-Befund (3G-Realität Afrika)

### Seitengewicht (lokal vermessen, gzip per mod_deflate geschätzt)

| Seite | Roh | gzip ≈ | Requests |
|---|---|---|---|
| index.html | 160,7 KB | ~57 KB | 11 |
| hire.html | 149,6 KB | ~48 KB | 10 |
| members.html | 148,6 KB | ~47 KB | 10 |
| request.html | 188,9 KB | ~61 KB | 13 |
| signup.html | 160,1 KB | ~52 KB | 11 (+ Turnstile/Supabase zur Laufzeit) |
| calculators.html | 163,5 KB | ~52 KB | 10 |

**Bewertung gegen 3G-Budget (~1,5 s LCP):** Das Budget wird grundsätzlich eingehalten — alle Seiten liegen weit unter 500 KB gzip. LCP-Kandidat index.html: Hero-Bild `electrician-480.webp` (8,9 KB mobil) mit `fetchpriority="high"` — erreichbar, sofern Server-RTT stimmt (Annahme, nicht live gemessen).

**Konkrete Schwachstellen:**
1. **7–8 einzelne, unminifizierte JS-Dateien pro Seite (~91 KB roh)**, am Body-Ende ohne `defer`/`async` geladen (index-pretty Z. 157–170). Auf 3G mit hohem RTT kostet jede Datei Overhead; kein Bundling/Minifizierung.
2. **`assets/style.css` (44,7 KB roh / ~9,7 KB gz)** ist ein Monolith für alle Seiten (enthält Profile-, Dashboard-, Messages-, Scout- und Fut-Karten-Styles) und lädt auf jeder Seite — geschätzt >70 % ungenutzt auf den Marketing-Seiten.
3. **`assets/i18n.js` (30,0 KB roh)** enthält das komplette EN-Sprachpaket inline auf jeder Seite; andere Sprachen werden sauber on-demand geladen (gutes Muster, aber EN-Basis trimmbar).
4. **Render-blocking:** 2–3 CSS-Dateien (~58 KB roh) im `<head>` — vertretbar, kein kritisches CSS inline.
5. **Drittanbieter zur Laufzeit:** Supabase-SDK (~30 KB gz) per dynamischem Import von jsdelivr **nur auf Auth-Seiten** (supa-auth.js Z. 13, 54 — gutes Muster, nicht render-blockierend, kein SRI). Cloudflare Turnstile auf signup.html (async/defer). Beide erfordern bei langsamem Netz Geduld; request.html fängt Offline sauber ab, **signup.html blockiert ohne geladenes Turnstile-Widget mit nur generischer Meldung** (signup-pretty Z. 255–261) — reales Risiko für die Zielgruppe (siehe M-Liste, Formular-UX).

**Schwerstes Asset im Bestand:** `assets/videos/voltage-partners.mp4` = **836 KB** (weitere: 801 KB, 770 KB) — wird auf **keiner** der Seiten referenziert (Grep über alle HTML/JS ohne Treffer): totes Gewicht im Deploy-Archiv. Schwerstes tatsächlich geladenes Asset: `assets/style.css` (44,7 KB roh). Schwerstes Bild: `assets/img/solar-panels-1200.webp` (176,9 KB, Guide-Seiten außerhalb Stichprobe).

**Positiv:** `.htaccess` mit deflate, immutable 1-Jahres-Cache für versionierte Assets, CSP, HSTS; WebP mit 480/900/1200-srcset und korrekten `sizes`; System-Fonts (kein Webfont-Download); `og-image.jpg` (72 KB) nicht im Seitenladepfad.

---

## 4. Formular-UX auf kleinem Display (request.html / signup.html)

**request.html — gut, mit Lücken:**
- `inputmode="numeric"` + `autocomplete="tel-national"` (Z. 102), `autocomplete="name"` (Z. 82), `address-level2` (Z. 112) — korrekte Tastaturen auf Android. ✅
- Ländervorwahl als Select mit Flags, Freitext-Alternative hinter „Other" (Z. 87–101); E.164-Validierung clientseitig (Z. 218–220). ✅
- Mobile Stapelung ≤420 px, Buttons `min-height:44px` (Z. 30–34). ✅
- Fehler: `role="alert"`, rote Feldränder, `aria-invalid`, Fokus auf erstes Fehlerfeld (Z. 234–252). ✅ — aber **kein `aria-describedby`** (M3), Fehler erst nach Submit (kein Inline-on-blur).
- Einzelschritt mit 7 Feldern + Consent — Schrittlänge vertretbar; WhatsApp-Handover mit vorbefülltem Kontext (Z. 254–258) passt zur Zielgruppe.
- **Kein Entwurfs-Schutz:** bei Verbindungsabbruch nach langem Beschreibungstext (bis 3000 Zeichen) sind alle Eingaben weg — auf instabilen Netzen ärgerlich.

**signup.html — funktional, aber für assistive Nutzung lückenhaft:**
- Rollenwahl als Toggle-Buttons mit `aria-pressed` + sichtbarer Markierung (Z. 84–87) — bedienbar; Radiogroup wäre semantisch sauberer.
- **Erfolg nicht angekündigt (K2), generische Fehler ohne Fokus (M4), kein aria-describedby.**
- **Turnstile ist aktiv konfiguriert** (supabase-config.js Z. 25). Lädt das Widget auf 2G/3G nicht oder blockiert ein Datensparmodus die Drittanbieter-Domain, erscheint nur „Please confirm the human check first." — die Registrierung ist dann unlösbar blockiert (signup-pretty Z. 255–261).
- Nach dem Absenden keine Offline-Rückfallebene (request.html meldet Verbindungsfehler und lässt Eingaben stehen; signup setzt Button zurück, Eingaben bleiben — akzeptabel).

---

## 5. Priorisierte Fix-Liste

### Quick Wins (je <30 Min, sofort)

1. **`<main id="main">` + Skip-Link ergänzen** — request.html, signup.html, calculators.html: nach `<body ...>` die Zeile `<a class="skip-link" href="#main">Skip to content</a>` einfügen und den Inhalt zwischen `</header>` und `<footer>` in `<main id="main">…</main>` wrappen (Fix K1).
2. **signup.html Erfolg ankündigen** — `showConfirm()` (signup-pretty Z. 242–251): Bestätigungs-Container `role="status" tabindex="-1"` geben und nach dem Ersetzen `.focus()` aufrufen (Muster aus request.html Z. 263–266 kopieren) (Fix K2).
3. **calculators.html Fokus-Outline reparieren** — Inline-Style (calculators-pretty Z. 44): `outline:none` entfernen oder durch `outline:2.5px solid var(--green);outline-offset:2px` ersetzen (Fix K3).
4. **Input-Rahmen kontrastfest machen** — website.css Z. 42 (und auth-card-Regeln): Rahmenfarbe von `var(--line)` (`#d6e1db`, 1,34:1) auf `#7d9489` (3,25:1) oder `#6d8377` (4,07:1, berechnet) ändern; `.btn.ghost`-Rahmen `#a9beb3` → `#6d8377` (Fix M1/M2).
5. **aria-describedby in request.html** — `<input id="rq-name" … aria-describedby="rq-name-err">` und `<input id="rq-phone" … aria-describedby="rq-phone-hint rq-phone-err">` ergänzen (Z. 82, 102) (Fix M3).
6. **Footer-Logo:** `<span aria-hidden="true">ϟ</span>` in allen 6 Footern (Fix N1).
7. **Tote Videos entfernen oder referenzieren** — `assets/videos/*.mp4` (2,4 MB gesamt) aus dem Deploy nehmen, wenn ungenutzt.

### Mittelfristig (nächster Sprint)

1. signup.html: feldbezogene Fehlertexte + Fokus auf erstes Fehlerfeld (Muster request.html); Turnstile-Fallback definieren (klare Fehlermeldung „Sicherheitsprüfung konnte nicht geladen — Verbindung prüfen und neu versuchen", Retry-Button) (M4 + Formular-UX).
2. calculators.html: sichtbare Fehlermeldung bei ungültiger Eingabe statt stillem Ausblenden (M5).
3. Sprachwechsel: Live-Region `role="status"` (z. B. „Language: Français") nach `applyI18n()`; `.eyebrow` `[dir="rtl"]{letter-spacing:0}` in website.css (M6, N3).
4. `.reveal` absichern: Inhalt ohne JS sichtbar (`<noscript>`-Override oder `.reveal` erst per JS-Klasse setzen) (N4).
5. Performance: JS bündeln + minifizieren (7–8 → 1–2 Dateien, `defer`); style.css in Kern- und Seiten-CSS splitten; i18n-EN-Basis auf benötigte Keys trimmen. Ziel: <40 KB gz und ≤6 Requests auf Marketing-Seiten.
6. Formular-Entwürfe in `localStorage` zwischenspeichern (request.html) gegen Verbindungsabbrüche.
7. `shine`-Animation mit Reduced-Motion-Schutz versehen (N5, Profilseiten).

---

## 6. Drei nächste Maßnahmen

1. **Quick Wins 1–3 umsetzen** (main-Landmarke/Skip-Link, signup-Erfolgsmeldung, calculators-Fokus) — schließt alle drei kritischen Befunde mit <2 h Aufwand.
2. **Kontrast- und ARIA-Quick-Wins 4–6 nachziehen und verifizieren** (Rahmenfarben, aria-describedby, Footer-Symbol) — danach code-seitig AA-konform in der Stichprobe.
3. **Manuelle Verifikation einplanen:** NVDA (Windows/Chrome) + TalkBack (Android) auf dem kritischen Pfad index → request → Absenden sowie signup → Bestätigung, dazu ein Throttled-3G-Test (Chrome DevTools „Slow 3G") mit Lighthouse/axe als Basis-Scan. Erst danach ist eine Konformitätsaussage zulässig — dieser Bericht ist ein Code-Audit, keine Zertifizierung.
