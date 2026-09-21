# AEO-Audit: Maschinenlesbare Plattformseiten

**Rolle:** AEO_Foundations (Maschinenlesbare Plattformseiten)
**Datum:** 2026-09-21
**Geprüfter Ist-Stand:** lokaler Website-Code unter `voltage-africa-website/` (statisches HTML, ~59 Root-Seiten + `dist/`-Spiegel, Generatoren `scripts/build-website.mjs` / `scripts/rebuild-website.py`)
**Geprüfte Dateien u. a.:** `index.html`, `faq.html`, `hire.html`, `scout-guide.html`, `members.html`, `rankings.html`, `solar-installers-nairobi.html`, `electricians-nairobi.html`, `guides.html`, `guide-hiring-electrician.html`, `calculators.html`, `robots.txt`, `sitemap.xml`, `assets/i18n.js`; dazu Grep-Sweeps über alle 118 HTML-Dateien (Root + `dist/`).

---

## 1. Zusammenfassung

Die Website hat eine solide Basis: Canonicals auf allen Seiten, sauberes semantisches HTML (genau ein `<h1>` pro Seite, `<section>`/`<details>`/`<ol>`-Strukturen), englische Fallback-Texte stehen inline im initialen HTML — ein Crawler ohne JavaScript sieht also lesbaren englischen Inhalt. Sechs Seiten (guides.html, 4 Ratgeber, calculators.html) haben bereits korrektes JSON-LD (CollectionPage, Article + FAQPage, WebPage, BreadcrumbList).

Die kritischen Lücken:

1. **Generator-Bug auf allen 30 Stadt-/Gewerkeseiten:** `og:title` und `og:description` sind überall die Texte der how-it-works-Seite — die wichtigsten Landingpages teilen sich in Social-/KI-Vorschauen falsch.
2. **Kein JSON-LD auf den Kernseiten:** Startseite (kein Organization/WebSite), `faq.html` (kein FAQPage, obwohl der Inhalt fertig als `<details>/<summary>` vorliegt), `scout-guide.html` (kein HowTo, obwohl ein 5-Schritte-`<ol>` existiert), alle 30 Stadt-/Gewerkeseiten (kein Service/OfferCatalog).
3. **i18n-Falle:** FR/PT/AR/ZH existieren nur als clientseitiger Texttausch via `assets/i18n.js`. Es gibt keine Sprach-URLs, kein einziges `hreflang` in allen 118 HTML-Dateien, und `i18n.js` aktualisiert weder `<title>`/Meta-Description noch das `lang`-Attribut. Für Crawler und Answer Engines ist die Site faktisch nur englisch.
4. **robots.txt** besteht aus 3 Zeilen ohne jede KI-Crawler-Policy; **sitemap.xml** hat keine `lastmod`-Werte und lässt mehrere öffentliche Marketingseiten weg (konsistent zu deren `noindex`, aber bei `locations.html` fachlich fragwürdig).

**Foundation-Score (nach Persona-Scorecard): 4/15.** Discovery 2/6, Parsability 2/6, Capability 0/3.

---

## 2. IST-Befund mit Code-Belegen

### 2.1 Strukturierte Daten (JSON-LD)

Vorhanden **nur** auf 6 von 59 Root-Seiten (Grep über alle `*.html`):

| Datei | Vorhandenes JSON-LD | Bewertung |
|---|---|---|
| `guides.html` | `CollectionPage` + `BreadcrumbList` | korrekt |
| `guide-hiring-electrician.html` | `@graph`: `Article` + `FAQPage` | korrekt, inkl. `inLanguage`, `datePublished` |
| `guide-solar-sizing-nigeria.html`, `guide-choosing-solar-installer-kenya.html`, `guide-office-network-cabling.html` | je 1× JSON-LD (Article/FAQ) | korrekt |
| `calculators.html` | `WebPage` + `BreadcrumbList` | korrekt |
| **alle anderen 53 Root-Seiten** (inkl. `index.html`, `faq.html`, `hire.html`, `how-it-works.html`, `scout-guide.html`, `technicians.html`, `about.html`, **alle 30 Stadt-/Gewerkeseiten**) | **keines** | Lücke |

Beleg `guides.html` (Auszug, tatsächlich im Code):

```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {"@type":"ListItem","position":1,"name":"Home","item":"https://www.voltage-africa.com/"},
 {"@type":"ListItem","position":2,"name":"Guides","item":"https://www.voltage-africa.com/guides.html"}]}
```

### 2.2 Meta / Open Graph / Twitter

- **Canonicals:** auf allen 118 Dateien vorhanden (je 1×). Achtung: `index.html` canonicalisiert auf `https://www.voltage-africa.com/index.html`, die Sitemap listet aber die Root-URL `https://www.voltage-africa.com/` — inkonsistent, sollte auf `/` vereinheitlicht werden.
- **Fehlende OG-/Twitter-Tags auf den Kernseiten:** `index.html`, `faq.html`, `hire.html`, `scout-guide.html`, `how-it-works.html`, `technicians.html`, `about.html` und alle 30 Stadt-/Gewerkeseiten haben nur `og:title`/`og:description`/`og:type` — **kein** `og:url`, **kein** `og:image`, **keine** `twitter:card`-Tags. (Die 6 Ratgeber-/Rechnerseiten plus `impressum.html`, `login.html`, `privacy.html`, `request.html`, `review.html`, `signup.html`, `terms.html` haben den vollen Satz.) `assets/og-image.jpg` existiert bereits und wird in den Ratgeber-Templates referenziert.
- **Generator-Bug (kritisch):** Alle 30 Stadt-/Gewerkeseiten tragen die OG-Texte der how-it-works-Seite. Beleg `solar-installers-nairobi.html` (Head):

```html
<title>Solar Installers in Nairobi (Kenya) | Voltage Africa</title>
<meta name="description" content="Solar Installers in Nairobi (Kenya) — Voltage Africa.">
<link rel="canonical" href="https://www.voltage-africa.com/solar-installers-nairobi.html">
<meta property="og:title" content="How it works | Voltage Africa">
<meta property="og:description" content="Understand the steps from a project request to an agreement with a technician.">
```

Grep-Befund: 20× `solar-installers-*.html` und 10× `electricians-*.html` mit identischem falschem `og:title "How it works | Voltage Africa"`. Nebenbefund: Description-Muster inkonsistent — `electricians-nairobi.html` nutzt „Electricians in Nairobi (2026)", `solar-installers-lagos.html` nutzt „Solar Installers in Lagos (Nigeria)".

- **Doppelter Title/Description:** `members.html` und `rankings.html` teilen identisch `<title>Continue with Voltage Africa | Voltage Africa</title>` und dieselbe Description.
- **noindex:** 17 Seiten tragen `<meta name="robots" content="noindex,follow">`: u. a. `dashboard.html`, `messages.html`, `profile.html`, `login.html` (korrekt, privat/App) — aber auch `rankings.html`, `review.html`, `signup.html`, `locations.html`, `investors.html`, `network.html`, `onepager.html`, `marketing.html`. Für `rankings.html` ist das eine Spannung: Die Startseite bewirbt „Live rankings" (Hero-Text in `assets/i18n.js`), die Seite selbst ist aber `noindex` und nicht in der Sitemap. Fachliche Entscheidung nötig: Rankings als indexierbare Vertrauensseite öffnen oder Hero-Claim anpassen.

### 2.3 Semantisches HTML (positiv)

`index.html`: genau ein `<h1>` („Good work starts with the right technician."), 5 `<section>`, 4× `<h2>`, 7× `<h3>`, 1 `<ol>` — saubere Hierarchie. `faq.html` nutzt echte `<details>/<summary>`-Paare mit 5 Fragen/Antworten im initialen HTML. `scout-guide.html` nutzt ein `<ol class="scout-steps">` mit 5 nummerierten Schritten. Beide Strukturen sind 1:1 in FAQPage- bzw. HowTo-Schema überführbar. `request.html` nutzt `<form id="rq-form">` ohne `action`/`method` — Absenden nur per JS (Wave-3-Hinweis, kein akuter AEO-Blocker, Guest-Flow existiert).

---

## 3. JSON-LD-Vorlagen je Seitentyp (copy-paste-fertig)

Alle Vorlagen beschreiben nur Inhalte, die auf den Seiten tatsächlich sichtbar sind. **Keine** `aggregateRating`-, Mitgliederzahlen- oder Verifikationswerte einbauen, solange sie nicht belegt sind (voltage-evidence). Einbau jeweils vor `</head>`. Da `scripts/build-website.mjs` / `rebuild-website.py` die Seiten erzeugen und `dist/` den Root spiegelt: Änderungen in die Generatoren einbauen, nicht in 30 Einzeldateien pflegen.

### 3.1 Startseite `index.html` — Organization + WebSite

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.voltage-africa.com/#org",
      "name": "Voltage Africa",
      "url": "https://www.voltage-africa.com/",
      "logo": "https://www.voltage-africa.com/assets/og-image.jpg",
      "description": "Platform connecting customers with electricians, solar installers, network and IT professionals across Africa."
    },
    {
      "@type": "WebSite",
      "@id": "https://www.voltage-africa.com/#website",
      "url": "https://www.voltage-africa.com/",
      "name": "Voltage Africa",
      "publisher": { "@id": "https://www.voltage-africa.com/#org" },
      "inLanguage": "en"
    }
  ]
}
</script>
```

Hinweis: `sameAs` (Social-Profile) erst ergänzen, wenn die Profile-URLs tatsächlich existieren.

### 3.2 Stadt-/Gewerkeseiten — Service + OfferCatalog (Beispiel `solar-installers-nairobi.html`)

Spiegelt den sichtbaren Seiteninhalt (Gewerk, Stadt, Request-CTA). Kein Preis, kein Rating — nicht belegt.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Solar installers",
  "provider": { "@id": "https://www.voltage-africa.com/#org" },
  "areaServed": { "@type": "City", "name": "Nairobi", "containedInPlace": { "@type": "Country", "name": "Kenya" } },
  "url": "https://www.voltage-africa.com/solar-installers-nairobi.html",
  "description": "Describe the solar work you need in Nairobi. Availability depends on the local network; submitting a request does not guarantee a match.",
  "offers": {
    "@type": "Offer",
    "name": "Submit a project request",
    "url": "https://www.voltage-africa.com/request.html?spec=solar&city=Nairobi",
    "price": "0",
    "priceCurrency": "USD"
  }
}
</script>
```

Hinweis: `price: 0` bezieht sich auf das kostenlose Stellen der Anfrage (Beleg: `faq.html`, „Submitting a request … is free"). Falls rechtlich unerwünscht, das `offers`-Objekt weglassen — das Service-Schema allein ist valide. Generator-Logik: `serviceType`, `areaServed`, `url` aus Dateiname/Seitentitel ableiten.

### 3.3 `faq.html` — FAQPage (1:1 aus dem vorhandenen HTML abgeleitet)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is it free?",
      "acceptedAnswer": { "@type": "Answer", "text": "Submitting a request and creating a technician account are free. Agree the cost of work directly with your service provider." } },
    { "@type": "Question", "name": "Do I need an account to request work?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Provide your contact details, location and project description in the request form." } },
    { "@type": "Question", "name": "When will I hear back?",
      "acceptedAnswer": { "@type": "Answer", "text": "There is no guaranteed response time. Availability depends on the location, trade and local network. Contact us if your request needs a follow-up." } },
    { "@type": "Question", "name": "How do I choose a technician?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ask for relevant qualifications, references and a written scope and quote. Confirm availability and payment terms before work begins." } },
    { "@type": "Question", "name": "Will joining guarantee me jobs?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. A profile helps present your experience; opportunities depend on customer demand and suitability." } }
  ]
}
</script>
```

### 3.4 BreadcrumbList — generisch (Beispiel Stadtseite; Muster für alle Unterseiten)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.voltage-africa.com/" },
    { "@type": "ListItem", "position": 2, "name": "Solar installers", "item": "https://www.voltage-africa.com/hire.html" },
    { "@type": "ListItem", "position": 3, "name": "Nairobi", "item": "https://www.voltage-africa.com/solar-installers-nairobi.html" }
  ]
}
</script>
```

Hinweis: Position 2 an die tatsächliche Elternseite anpassen (aktuell fehlt eine indexierbare Gewerke-Übersicht; `locations.html` ist noindex — siehe §5/§6).

### 3.5 `scout-guide.html` — HowTo (aus den 5 sichtbaren Schritten)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "The scout's five-step process",
  "description": "Connect local technicians with customers who need their skills: invite technicians, support their profiles and follow up on real project needs.",
  "step": [
    { "@type": "HowToStep", "position": 1, "name": "Find technicians",
      "text": "Meet electricians, solar installers and IT professionals in your area. Explain what the platform does and invite interested people with your personal link." },
    { "@type": "HowToStep", "position": 2, "name": "Help them become ready",
      "text": "Let each technician register with their own email. Help them add a service area, skills and real project examples, then show them where to read messages." },
    { "@type": "HowToStep", "position": 3, "name": "Find customers with a real need",
      "text": "Speak to households, shops, property managers and local businesses. Help them describe the location, work and preferred timing in a project request." },
    { "@type": "HowToStep", "position": 4, "name": "Start a useful conversation",
      "text": "Introduce the need clearly. Encourage technicians to answer questions and confirm availability. Customers agree the scope and price directly with the technician." },
    { "@type": "HowToStep", "position": 5, "name": "Follow up and bring people back",
      "text": "Check whether both sides have a next step. Encourage project updates, honest feedback and current profiles." }
  ]
}
</script>
```

Hinweis: Der 5. Schritt ist im sichtbaren HTML abgeschnitten/verkürzt („…without sending re…") — vor Einbau den vollständigen Text aus `scout-copy.js` ziehen und die Seite selbst vervollständigen. Keine Einkommensversprechen ins Schema („No guaranteed earnings" ist der sichtbare Claim).

### 3.6 Mitgliederprofile — Person/ProfilePage (Datenschutz zuerst)

Ist-Stand: `profile.html`, `members.html`, `dashboard.html`, `messages.html` sind `noindex` — **das ist korrekt so und soll vorerst bleiben.** Personendaten (Name, Foto, Standort, Bewertungen) dürfen nicht per Schema aus Seiten herausgereicht werden, die Mitglieder als privat erwarten.

Empfehlung: `ProfilePage`/`Person`-Markup **nur** einführen, wenn es eine explizit öffentliche, vom Mitglied opt-in freigegebene Profilansicht gibt. Dann — und nur dann — Vorlage:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "name": "<Anzeigename, nur mit Opt-in>",
    "jobTitle": "<Gewerk, z. B. Electrician>",
    "address": { "@type": "PostalAddress", "addressLocality": "<Stadt>", "addressCountry": "<Land>" },
    "url": "https://www.voltage-africa.com/technicians/<slug>.html"
  }
}
</script>
```

Verbotsliste (voltage-evidence): kein `aggregateRating` ohne belegte Bewertungsgrundlage, keine „Verified"-Claims ohne dokumentierten Prüfprozess, keine Zertifikate, keine privaten Kontaktdaten im JSON-LD.

---

## 4. i18n / Crawler-Risiko

**Was ein Crawler ohne JavaScript sieht:** den englischen Inline-Fallback. Geprüft: In `index.html`, `faq.html`, `hire.html`, `scout-guide.html`, `solar-installers-nairobi.html`, `how-it-works.html` sind **alle** `data-i18n`-Elemente mit englischem Text gefüllt (0 leere Elemente). Das ist der gute Teil — Kerninhalte sind ohne JS lesbar.

**Das Risiko (konkret, mit Beleg):**

1. **Keine indexierbaren Sprachversionen.** `assets/i18n.js` Kopfzeile: „EN pack inline (fallback base), other languages on demand" — FR/PT/AR/ZH werden clientseitig per `textContent`-Tausch injiziert. Es gibt keine Sprach-URLs (kein `/fr/…`, kein `?lang=fr`), und ein Grep über alle 118 HTML-Dateien findet **null** `hreflang`-Attribute. Die Sprachbuttons (`data-lang="fr"` usw. in `index.html`) beweisen keine indexierbare Abdeckung — exakt die Falle, die der Skill `voltage-readable-pages` benennt.
2. **Sprachwechsel ist für Crawler unsichtbar und unvollständig:** `i18n.js` aktualisiert weder `document.title` noch Meta-Description noch das `lang`-Attribut (Grep: keine Treffer für `document.title` / `documentElement.lang` in `i18n.js`). Selbst ein rendernder Crawler sähe nach Sprachwechsel englische Meta-Daten unter `<html lang="en">`.
3. **Konsequenz:** Answer Engines und klassische Suche können die Site nur auf Englisch zitieren. Für Zielmärkte wie Senegal/Côte d'Ivoire (FR), Angola/Mosambik (PT), Maghreb (AR) fehlt damit die gesamte organisch zitierbare Oberfläche.

**Optionen (Entscheidung nötig, Aufwand steigend):**

- **Minimum (1 Tag):** Risiko dokumentieren; keine Codeänderung. Englisch bleibt die einzige Crawler-Sprache.
- **Mittel (2–4 Tage):** Statische Sprachkopien der ~10 wichtigsten Seiten erzeugen (Generator kann das — i18n-Packs liegen in `assets/i18n/` vor), jeweils mit eigenem `<html lang>`, eigenen Titeln/Descriptions und gegenseitigem `hreflang` inkl. `x-default`. Reihenfolge nach Marktpriorität: FR zuerst (Dakar, Abidjan, Douala, Conakry, Cotonou, Lomé, Libreville liegen alle im französischsprachigen Raum).
- **Keine Option:** hreflang ohne echte Sprach-URLs setzen — das würde auf nicht existierende Varianten verweisen.

---

## 5. robots.txt + sitemap.xml

**robots.txt** (kompletter Ist-Stand, 3 Zeilen):

```text
User-agent: *
Allow: /
Sitemap: https://www.voltage-africa.com/sitemap.xml
```

- Sitemap-Verweis korrekt. Keine KI-Crawler-Direktiven: weder explizites Erlauben (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended) noch Sperren. `Allow: /` für `*` lässt technisch alle Crawler durch — es gibt also keine *versehentliche* Sperre, aber auch keine dokumentierte Policy. Gemäß Persona-Regel: Erlauben/Sperren von Trainings-Crawlern ist eine Geschäftsentscheidung — Optionen vorlegen, nicht entscheiden. Zusätzlich fehlen Schutz-Disallows für App-Bereiche (`dashboard.html`, `messages.html`, `profile.html`) — dort wirkt aktuell nur `noindex` (das reicht für Indexierung, nicht gegen Crawling).
- `llms.txt` existiert nicht. Laut Skill `voltage-readable-pages` nur als optionales Experiment ohne garantierten Zitationseffekt — niedrigste Priorität.

**sitemap.xml** (Ist-Stand): 48 URLs, valides XML, alle Stadt-/Gewerkeseiten und Kernseiten enthalten. `index.html` ist über die Root-URL abgedeckt. Fehlend:

- `lastmod` auf allen URLs (Datum liegt vor: z. B. `datePublished 2026-08-02` in den Ratgebern; Asset-Version `?v=20260915`).
- Öffentliche Marketingseiten fehlen: `signup.html`, `review.html`, `locations.html`, `investors.html`, `network.html`, `onepager.html` — konsistent zu deren `noindex`, aber fachlich prüfen: **`locations.html` als Übersicht aller Standorte wäre die natürliche Breadcrumb-/Verlinkungselternseite für 30 Landingpages und sollte indexierbar + in der Sitemap sein.** `rankings.html`/`members.html` fehlen ebenfalls (noindex, s. §2.2 — Entscheidung offen).
- Korrekt ausgelassen: `dashboard.html`, `messages.html`, `profile.html`, `login.html`, `404.html`.

---

## 6. Priorisierte Umsetzungsliste

**Phase 1 — Quick Wins (Tag 1–3, null Risiko, große Wirkung):**

1. **OG-Bug auf 30 Stadt-/Gewerkeseiten fixen** (`scripts/build-website.mjs` bzw. `rebuild-website.py`): `og:title`/`og:description` aus dem jeweiligen `<title>`/`<meta name="description">` erzeugen. Betroffen: alle `solar-installers-*.html` (20) und `electricians-*.html` (10). Größter sichtbarer Defekt der Site.
2. **FAQPage-JSON-LD in `faq.html`** (Vorlage §3.3 — Inhalt liegt fertig im HTML).
3. **Organization+WebSite-JSON-LD in `index.html`** (Vorlage §3.1) + gleichzeitig Canonical auf `https://www.voltage-africa.com/` vereinheitlichen.
4. **robots.txt: KI-Crawler-Policy dokumentieren** (Vorlage aus Persona-Scorecard; Search-Augmented-Crawler wie PerplexityBot erlauben, Trainings-Crawler als dokumentierte Geschäftsentscheidung) + `Disallow` für `dashboard.html`, `messages.html`, `profile.html`.
5. **OG-/Twitter-Basissatz auf allen Kernseiten ergänzen** (`og:url`, `og:image` → `assets/og-image.jpg`, `twitter:card`) — betroffen: `index.html`, `faq.html`, `hire.html`, `scout-guide.html`, `how-it-works.html`, `technicians.html`, `about.html` + 30 Stadtseiten.

**Phase 2 — Struktur (Woche 2):**

6. HowTo-JSON-LD in `scout-guide.html` (Vorlage §3.5; vorher Schritt-5-Text vervollständigen).
7. Service/OfferCatalog-JSON-LD auf 30 Stadt-/Gewerkeseiten via Generator (Vorlage §3.2).
8. BreadcrumbList auf allen Unterseiten via Generator (Vorlage §3.4).
9. `sitemap.xml`: `lastmod` ergänzen; Entscheidung `locations.html` (indexierbar machen + aufnehmen) und `rankings.html` (noindex vs. Hero-Claim auflösen); Title-/Description-Duplikat `members.html`/`rankings.html` auflösen.

**Phase 3 — Sprache & Optionales (Woche 3–4, Entscheidungsbedarf):**

10. i18n-Entscheidung (§4): statische Sprachkopien der Top-10-Seiten mit hreflang, FR zuerst — oder dokumentierter Verzicht.
11. Optional: `llms.txt` als Experiment (kuratierte Liste der Kernseiten), vierteljährliche Pflege einplanen; kein Zitationseffekt garantiert.
12. Optional/Zukunft: öffentliche Opt-in-Technikerprofile mit `ProfilePage`-Schema (§3.6) — nur nach Datenschutz- und Einwilligungsklärung.

**Abnahme:** Nach Phase 1–2 JSON-LD mit Schema-Validator prüfen (Syntax) und Inhalt gegen sichtbare Seitentexte abgleichen (fachliche Prüfung getrennt, lt. Skill). Foundation-Score-Ziel: ≥ 11/15.

---

*Erstellt nach AGENTS.md / SENIOR-STANDARD. Alle Befunde beziehen sich auf den lokalen Code-Stand 2026-09-21; kein Live-Abruf der produktiven Seite in dieser Session. Syntax- und Fachprüfung der Vorlagen erfolgen getrennt.*
