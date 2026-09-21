# Lokale Paid-Media-Strategie für Mini-Budget (300 $/Monat Testbudget)

**Rolle:** Ads_Stratege (Lokale Suchwerbung) · **Datum:** 2026-09-21 · **Status:** Arbeitsbericht mit Belegen — Kampagnen sind Entwürfe, kein Launch ohne ausdrückliche Autorisierung
**Hinweis zu Zahlen:** Alle CPC-/CPM-Werte sind externe Benchmark-Schätzungen aus Sekundärquellen (Autorität jeweils gekennzeichnet), keine Kontodaten. Alle Quellen wurden am 2026-09-21 abgerufen. Vor Launch sind die tatsächlichen Auktionspreise im Google Keyword Planner und Meta Ads Manager zu prüfen.

---

## 1. Zusammenfassung

1. **Pilotmarkt: Lagos (Nigeria).** Größtes Stadt-Nachfragevolumen Afrikas (17,2 Mio. Einwohner), belegte Stromversorgungskrise und Solar-Nachfrage, englischsprachig (passt zur EN-Website und den Stadt×Gewerk-Landingpages), die niedrigsten recherchierten Such-CPCs der Tier-1-Märkte und ~98 % WhatsApp-Penetration unter Internetnutzern (Upstream-Bericht `2026-09-21-laender-priorisierung.md`).
2. **Kanal: Google Search Ads als Hauptkanal (~70 % des Budgets), Meta Click-to-WhatsApp als zweiter Kanal (~30 %).** Suchanzeigen treffen exakt die vorhandene Landingpage-Logik (Stadt×Gewerk), CTWA nutzt die dominante WhatsApp-Nutzung und umgeht die Conversion-Schwäche statischer Formulare. TikTok scheidet aus: Mindestbudget 20 $/Tag/Anzeigengruppe (= ~600 $/Monat, doppelt so viel wie das Gesamtbudget), Videoproduktion nötig, Self-Serve-Verfügbarkeit in Nigeria unklar.
3. **Vorbedingung vor jeder Nachfragekampagne (gemäß Skill voltage-local-ads):** bestätigte Techniker-Kapazität in Lagos. Ohne belegte passende Profile dürfen keine Nachfragekampagnen laufen — dann startet stattdessen die Techniker-Akquise (CTWA → signup.html).
4. **Tracking ist der eigentliche Engpass, nicht die Anzeigen:** Die Website hat bereits eine Event-Schicht (`vaTrack` → `dataLayer`, in `assets/marketing-agent.js`), aber es ist **kein gtag/GTM/Meta-Pixel installiert** und es gibt **keine Danke-Seite** (request.html zeigt Inline-Erfolg). Minimaler Aufwand (~1 Dev-Tag) macht Kampagnen auswertbar — Details in Abschnitt 5.
5. **Zielgröße (Schätzung, keine Messung):** Kosten pro eingegangener Anfrage 2–10 $ bei Such-CPCs von geschätzt 0,15–0,50 $ (Local Services, Nigeria) und 5–10 % Landingpage-Conversion. Abbruchschwellen in Abschnitt 6.

---

## 2. Kanalwahl mit CPC-Quellen

### 2.1 Vergleich der Kanäle

| Kanal | Geschätzte Kosten (Pilotmarkt-relevant) | Intent-Qualität | Fit für Voltage | Urteil |
|---|---|---|---|---|
| **Google Search** | Nigeria: Search-CPC Ø ~0,66 $, Spanne 0,30–1,50 $; **Local Services 0,15–0,50 $** (Schätzung, Quelle 1, Autorität NA). Kenia: ~KES 10–100+ (0,08–0,80 $, Quelle 2/3, Autorität NA). Südafrika: Construction & Trades R 13,27 (~0,72 $), Renewable Energy R 19,96 (~1,08 $) (Quelle 4, Autorität NA). Globaler Referenzrahmen: Search-Ø 5,26 $ (WordStream/LocaliQ 2025, >16.000 Kampagnen, Quelle 5, Autorität B) — Afrika-Märkte liegen deutlich darunter | Hoch (aktive Suche „electrician lagos") | Sehr hoch — deckt sich 1:1 mit Stadt×Gewerk-Landingpages und SEO-Keyword-Logik | **Hauptkanal** |
| **Meta (Facebook/Instagram)** | Nigeria: CPM ~1,50 $, CPC ~0,12 $ (Quelle 6, Autorität NA); Kenia: CPM ~2,40 $, CPC ~0,22 $ (Quelle 6); Südafrika: Median-CPC ~0,17 $, CPM ~3,33 $ (Datensatz 3 Mrd. $ Spend, Quelle 7, Autorität NA). Bot-/Qualitätsrisiko in Tier-3-Märkten 20–30 % über Tier 1 (Quelle 6) | Mittel (Discovery) | Hoch als **Click-to-WhatsApp**: 92–98 % WhatsApp-Penetration in Tier-1-Märkten (Upstream-Bericht); CTWA öffnet 72h-Freifenster für Antworten (Quelle 8/9) | **Zweitkanal (nur CTWA-Format)** |
| **TikTok Ads** | Nigeria: CPM ~1,00 $, CPC ~0,08 $ (Quelle 10, Autorität B) — **aber** Plattform-Minimum 20 $/Tag je Anzeigengruppe, 50 $/Tag je Kampagne (Quelle 11, Autorität B) = ~600 $/Monat Minimum, dazu Videoproduktion; Self-Serve-Verfügbarkeit in Nigeria nicht belegt (Datenlücke) | Niedrig (Unterhaltung) | Gering für hochintente Handwerksvermittlung; interessant erst für Techniker-Recruiting bei größerem Budget | **Verworfen für Testphase** |
| **WhatsApp Click-to-Chat (direkt)** | Kein eigenständiges Werbenetz — läuft über Meta CTWA-Anzeigen (Kosten = Meta-CPC/CPM, s. o.). Gespräche, die über einen Anzeigenklick starten, öffnen ein 72-stündiges Freifenster, in dem alle Nachrichtentypen kostenlos sind (Quelle 8, Meta-Doku via Quelle 9, Autorität A für Preismodell-Wechsel). Benchmark „Cost per Conversation Started": 1,50–3,00 $ in US-E-Commerce (Quelle 12, Autorität NA); in Nigeria realistisch deutlich darunter (Schätzung 0,20–1,00 $, unbelegt) | Hoch im Moment der Konversation | Sehr hoch — passt zum bestehenden WhatsApp-Handover in request.html | **Als Format innerhalb Meta, kein separater Kanal** |

### 2.2 Begründung der Kanal-Empfehlung

- **Google Search zuerst**, weil die Nachfrage bereits existiert (Stromausfälle, Solar-Boom sind belegt, Upstream-Bericht) und gesucht wird — Voltage muss nur sichtbar sein. Die gesamte Website-Architektur (Stadt×Gewerk-Seiten) ist für genau diese Queries gebaut. Bei <500 $/Monat zählt nur Bottom-Funnel.
- **Meta CTWA ergänzend**, weil (a) die nigerianischen Klickpreise geschätzt 5–10× unter Search liegen, (b) WhatsApp der dominante Kommunikationsweg ist und (c) die Website ohnehin auf WhatsApp-Handover setzt (request.html baut bereits einen `wa.me`-Link mit Anfragetext). CTWA umgeht zudem Formular-Abbrüche auf mobilen Verbindungen.
- **Budget-Logik:** Bei 300 $/Monat ist Streuung über 3+ Kanäle statistisch unbrauchbar. Zwei Kanäle, ein Markt, zwei Gewerke — das ist die maximale Komplexität, die 300 $ noch auswertbar tragen.

---

## 3. Kampagnenstruktur (300 $/Monat, Pilotmarkt Lagos)

### 3.1 Vorbedingung (Skill voltage-local-ads: keine Nachfrage ohne Kapazität)

- **Check vor Launch:** Anzahl aktiver, passender Elektriker-/Solar-Profile in Lagos (members.html/Supabase) prüfen. Kein Schwellenwert belegt — Arbeitsannahme: **mindestens ~20 kontaktierbare Techniker in Lagos** (Elektrik + Solar), damit Anfragen beantwortet werden können.
- **Fallback:** Liegt die Kapazität darunter, läuft Monat 1 umgekehrt: **Techniker-Kampagne** (Meta CTWA → signup.html, Variante M3 in Abschnitt 4), Nachfrage-Kampagnen starten erst nach Kapazitätsaufbau.

### 3.2 Budgetaufteilung

| Posten | Budget/Monat | Tagesbudget | Erwartetes Volumen (Schätzung, unbelegt) |
|---|---|---|---|
| Google Search, Kampagne NG-Lagos-Core | 210 $ | ~7 $ | 400–900 Klicks (CPC 0,20–0,50 $), 20–70 Anfragen (CVR 5–8 %) |
| Meta CTWA, Kampagne NG-Lagos-WA | 90 $ | ~3 $ | 90–300 gestartete Konversationen (0,30–1,00 $/Konversation, geschätzt) |
| **Gesamt** | **300 $** | **~10 $** | — |

Hinweis: Google-Abrechnung für nigerienbezogene Konten nur in USD; bei Abrechnungsland Nigeria fallen 7,5 % VAT auf Werbeausgaben an (Quelle 1). Abrechnungsland des Voltage-Kontos vor Launch klären.

### 3.3 Google-Search-Struktur

**Eine Kampagne** (Konzentration der Lernphase): `NG-Lagos-Search-Core`

| Ebene | Konfiguration |
|---|---|
| Geotargeting | Lagos (Stadt), Option „Präsenz: Personen im Zielgebiet oder regelmäßig dort" — **nicht** „Interesse am Zielgebiet" (sonst Klicks aus Diaspora/Ausland) |
| Sprache | Englisch |
| Gebotsstrategie | Woche 1–4: „Klicks maximieren" mit max. CPC-Gebot 0,50 $; danach „Conversions maximieren", sobald ≥15 Conversions/Monat getrackt werden (Smart Bidding ohne Daten verbrennt Budget — Quelle 1) |
| Anzeigenplanung | Woche 1–2: 24 h; danach Dayparting nach Daten. Arbeitsannahme: 06:00–23:00 WAT (Stromausfälle/Generator-Nutzung abends → Abendnachfrage wahrscheinlich, unbelegt) |
| Geräte | Mobile-priorisiert (Kenia/Nigeria überwiegend mobil); Desktop-Gebotsanpassung −20 % nach ersten Daten |
| Landingpages | Je Anzeigengruppe die passende Stadt×Gewerk-Seite; Fallback request.html |

**Anzeigengruppen + Keywords (EN, aus der SEO-Logik „Gewerk + Stadt"):**

*AG 1: Electrician* (Start als Phrase + Exact)
- electrician lagos · electrician in lagos · electrical repair lagos · emergency electrician lagos · house wiring lagos · electrician near me · home electrician lagos

*AG 2: Solar & Inverter*
- solar installer lagos · solar installation lagos · solar company lagos · inverter installation lagos · inverter and battery lagos · generator repair lagos · solar panel installer near me

**Negative Keywords (Kampagnenebene, von Tag 1):** jobs, job, vacancy, salary, course, training, free, diy, pdf, wholesale, price of panels (Preisvergleicher ohne Auftragsintent — „solar panel price" bewusst nur in Exact testen, nicht Phrase)

**Wichtig:** Auftraggeber- und Techniker-Keywords strikt trennen (Skill-Vorgabe). „electrician jobs lagos" ist ein **Techniker**-Keyword und gehört — falls Techniker-Akquise nötig — in eine eigene Kampagne Richtung signup.html, nie in die Nachfragekampagne.

### 3.4 Meta-CTWA-Struktur

**Eine Kampagne** `NG-Lagos-WA-Leads`, Ziel „Interaktion/Nachrichten" (Conversations Started), Platzierungen Facebook + Instagram Feed/Reels:

| Ad Set | Zielgruppe | Budget |
|---|---|---|
| AS 1: Haushalte | Lagos, 25–55, Interessen: Home improvement, Solar energy, Generators; Advantage+ aus | ~1,50 $/Tag |
| AS 2: Gewerbe/KMU | Lagos, 25–55, Interessen: Small business owners, Real estate, Facilities; Advantage+ aus | ~1,50 $/Tag |

Beide Ad Sets nutzen die 3 Anzeigenvarianten aus Abschnitt 4.2 (Rotation). Ziel: WhatsApp-Business-Nummer von Voltage Africa mit vorbefüllter Startnachricht („Hi Voltage Africa, I need an electrician in Lagos…").

---

## 4. Anzeigentexte (Englisch)

**Claim-Disziplin (Skill voltage-evidence):** Keine „verified"-Versprechen (Verifizierung ist Website-Claim, nicht betrieblich belegt), keine Preis- oder Zeitversprechen, keine Mitgliederzahlen. Zulässig: der beobachtbare Plattformweg (Anfrage posten → Interessenten antworten → WhatsApp-Kontakt). „Free/without obligation" bezieht sich ausschließlich auf das beobachtbar unentgeltliche Absenden des Anfrageformulars (kein Zahlungsschritt in request.html) — vor Ausspielung von „free" kurz bestätigen, dass das auch für den Live-Prozess gilt.

### 4.1 Fünf Responsive Search Ads (Headlines ≤30 Zeichen, Descriptions ≤90 Zeichen)

**RSA 1 — AG Electrician (Allgemein)**
- H1: `Electrician in Lagos` (20)
- H2: `Find Local Electricians` (23)
- H3: `Post Your Request in Minutes` (28)
- H4: `Compare Electrician Profiles` (28)
- D1: `Describe your electrical job in Lagos. Interested electricians respond to you.` (80)
- D2: `Post a request in minutes — free and without obligation. You choose.` (69)

**RSA 2 — AG Solar & Inverter**
- H1: `Solar Installer in Lagos` (24)
- H2: `Find Solar Installers` (21)
- H3: `Plan Your Solar Project` (23)
- H4: `Solar & Inverter Services` (25)
- D1: `Need solar panels or an inverter in Lagos? Post your project once.` (66)
- D2: `Describe your solar project — interested installers in Lagos respond.` (69)

**RSA 3 — AG Electrician (Reparatur-Fokus)**
- H1: `Electrical Repair in Lagos` (26)
- H2: `Report an Electrical Fault` (26)
- H3: `Home Wiring & Repairs` (21)
- H4: `Post a Repair Request` (21)
- D1: `Faulty wiring, tripping breakers, dead sockets? Post your repair request.` (74)
- D2: `Describe the problem once — electricians in Lagos can respond to you.` (69)

**RSA 4 — AG Solar & Inverter (Backup-Power-Fokus)**
- H1: `Inverter Installation Lagos` (27)
- H2: `Inverter & Battery Setup` (24)
- H3: `Generator Repair in Lagos` (25)
- H4: `Power Backup for Your Home` (26)
- D1: `Backup power for home or business: post your inverter or generator job.` (71)
- D2: `Tell us what you need — interested technicians in Lagos respond.` (64)

**RSA 5 — Gewerbe/B2B (beide AGs testbar)**
- H1: `Commercial Electricians Lagos` (29)
- H2: `Electricians for Business` (25)
- H3: `Facility Electrical Services` (28)
- H4: `Post Your Project Today` (23)
- D1: `Offices, shops, facilities — post your electrical or solar project once.` (72)
- D2: `One request reaches interested technicians in Lagos. You decide.` (64)

### 4.2 Drei Meta-Ad-Varianten (Click-to-WhatsApp)

**M1 — Haushalt / Elektrik**
> **Primary Text:** Power problems at home in Lagos? Describe your electrical job once — interested electricians reach out to you directly on WhatsApp. Posting a request is free and without obligation. You choose who to hire.
> **Headline:** `Find an Electrician in Lagos` (28)

**M2 — Solar / Backup Power**
> **Primary Text:** Tired of outages? Post your solar or inverter project once and hear from installers in Lagos — straight to your WhatsApp. No obligation, you compare and decide.
> **Headline:** `Solar Installers in Lagos` (25)

**M3 — Techniker-Akquise (nur bei Supply-Lücke, Ziel: signup.html)**
> **Primary Text:** Are you an electrician or solar installer in Lagos? Join Voltage Africa and get customer requests from your area — direct to your WhatsApp. Sign up free and complete your profile.
> **Headline:** `Get Job Requests via WhatsApp` (29)

*Hinweis M3: „get customer requests" beschreibt den Plattformweg (Website-Claim), ist kein belegtes Auftragsvolumen — Formulierung vor Ausspielung ggf. zu „receive requests posted in your area" abschwächen.*

---

## 5. Conversion-Tracking-Anforderungen (statische Website + Supabase)

**Ist-Zustand (lokal im Code beobachtet, Stand 2026-09-21):**
- `assets/marketing-agent.js` stellt `window.vaTrack(event, props)` bereit und pusht jedes Event als `va_<event>` in `window.dataLayer` — Kommentar im Code: „GA4 / Google Ads ready". UTM-Parameter (first/last touch) werden in localStorage gespeichert (`vaAttribution()`).
- `request.html` feuert `vaTrack("request_submit", {spec, country})` im Erfolgs-Callback; Erfolg wird **inline** angezeigt (`#rq-success`), **keine Danke-Seite, kein Redirect**. Der Supabase-Insert (`payload = {name, contact, country, city, spec, message}`) enthält **keine** UTM-/GCLID-Felder.
- Seitenweit gefundene Events: `request_submit`, `signup_start`, `signup_complete`, `login`, `review_submit`, `waitlist_submit`, `page_view`, `cta_click`.
- **Kein gtag.js, kein GTM, kein Meta-Pixel irgendwo im HTML** — die Datenbasis existiert, aber kein Tag empfängt sie.

**Minimal nötig (geschätzt ~1 Dev-Tag, kein Framework nötig):**

1. **Google-Tag (gtag.js) seitenweit einbinden** — ein Snippet im gemeinsamen Header/Layout mit GA4-Measurement-ID + Google-Ads-Tag (AW-ID). Damit fließen die bereits vorhandenen dataLayer-Events.
2. **Google-Ads-Conversion „Anfrage" anlegen und mappen:** primäre Conversion = `request_submit`. Konkret: im Erfolgs-Callback von request.html (dort, wo heute `vaTrack("request_submit", …)` steht) zusätzlich `gtag('event','conversion',{send_to:'AW-XXXX/label'})` feuern. Sekundäre Conversions: `signup_complete` (Techniker), WhatsApp-Klick auf `#rq-wa`.
3. **Meta-Pixel-Basiscode einbinden** + Event `Lead` im selben Erfolgs-Callback. Für CTWA-Kampagnen misst Meta „Conversations Started" nativ im Ads Manager — hier ist kein Pixel nötig, wohl aber für Retargeting-Zielgruppen.
4. **GCLID + UTM in Supabase speichern (Lead-Level-Attribution):**
   - `marketing-agent.js` speichert bereits `utm_source/medium/campaign` — zusätzlich `gclid` aus `location.search` in dasselbe Objekt aufnehmen (3 Zeilen).
   - In request.html den Insert-Payload um `utm_source, utm_campaign, gclid` erweitern (aus `window.vaAttribution().last`).
   - Supabase: Tabelle der Anfragen um 3 Spalten erweitern (`ALTER TABLE ... ADD COLUMN utm_source text, utm_campaign text, gclid text;`).
   - Nutzen: wöchentlicher Export „beantwortete/qualifizierte Anfragen" als **Offline-Conversion-Import** in Google Ads (GCLID-basiert) — erst dann ist „Kosten pro *beantworteter* Anfrage" statt nur „pro Formular" messbar.
5. **Optional, empfohlen: `/thanks.html`** als Danke-Seite. Nicht zwingend (Event-basiertes Tracking reicht), aber nützlich als Fallback-Conversion (Seitenaufruf), für Meta-URL-Regeln und als natürliche Stelle für den WhatsApp-Handover.
6. **Consent/DSGVO-Hinweis:** Zielmarkt ist Nigeria (NDPR), die Betreiber-Verantwortung und ggf. EU-Bezug sind zu klären; Consent-Banner-Pflicht vor Launch rechtlich prüfen (hier nicht belegt).

**Ohne Punkt 1–4 kein Launch** — sonst sind weder CPL noch Abbruchkriterien auswertbar.

---

## 6. Abbruchkriterien und Umschichtung (Schwellen)

Alle Schwellen sind Arbeitsannahmen auf Basis der geschätzten CPCs (0,20–0,50 $ Search, 0,30–1,00 $/Konversation CTWA); Bewertung wöchentlich, Entscheidungen frühestens nach statistisch halbwegs brauchbarem Volumen.

| Ebene | Signal | Schwelle | Maßnahme |
|---|---|---|---|
| Keyword/AG | Spend ohne Conversion | >30 $ (~60–100 Klicks) ohne ein `request_submit` | Keyword pausieren oder Match-Type verschärfen; Search-Terms-Report → Negative |
| Anzeige | CTR | <3 % nach ≥500 Impressionen (Referenz: Search-Ø 6,66 %, Quelle 5) | RSA-Texte ersetzen (Variante aus Abschnitt 4.1) |
| Google-Kampagne | Cost per Anfrage | >25 $ nach 4 Wochen bzw. 150 $ Spend (Zielkorridor: 2–10 $) | Struktur-Reset: engere Keywords, LP-Check, Gebote senken; bei 2. Misserfolg Kanalbudget → Meta schieben |
| Meta-Ad-Set | Cost per Conversation | >1,50 $ nach 30 $ Spend | Creative/Target wechseln |
| Meta-Kampagne | Qualität | <10 % der Konversationen qualifiziert (echte Anfrage mit Ort+Gewerk) nach ≥30 Konversationen | Vorbefüllte Nachricht schärfen; ggf. Ad-Set stoppen |
| Gesamttest | Go/No-Go | Nach 8 Wochen / max. 600 $: Kosten pro **beantworteter** Anfrage und Antwortquote der Techniker bewerten | Skalierung (Abuja/Accra) nur bei belegter Beantwortung; sonst Kanal/Marktwechsel |
| Qualitäts-Stopper | Anfragen ohne Techniker-Antwort | >50 % unbeantwortet nach 72 h | Nachfragekampagne **sofort pausieren** (Skill: keine Nachfrage ohne Kapazität), Budget auf M3/Techniker-Akquise |

**Verlustgrenze gesamt:** 600 $ über 8 Wochen. Kein Nachschuss ohne dokumentierte Learnings.

---

## 7. Drei konkrete nächste Maßnahmen

1. **Supply-Check Lagos + Tracking-Sprint (diese Woche):** Techniker-Abdeckung in Lagos zählen (Supabase/members); parallel die 4 Tracking-Punkte aus Abschnitt 5 umsetzen (gtag + Conversion-Mapping + GCLID/UTM in Supabase-Payload + Pixel). Beides ist Launch-Blocker, kein „nice to have".
2. **Konten vorbereiten (ohne Ausgaben):** Google-Ads-Konto mit geklärtem Abrechnungsland/USD-Zahlungsweg anlegen, Kampagnenentwurf nach Abschnitt 3 **pausiert** hochladen, Keyword-Planner-Ist-CPCs für die 14 Keywords gegen die hier geschätzten Werte prüfen und Berichtswerte aktualisieren. Meta Business Manager + WhatsApp-Business-Nummer verbinden, CTWA-Kampagne als Entwurf anlegen.
3. **Autorisierung einholen, dann 2-Wochen-Pilot:** Freigabe für 300 $/Monat × 2 Monate (= 600 $ Verlustgrenze) mit den Schwellen aus Abschnitt 6. Launch nur bei bestätigter Lagos-Kapazität; andernfalls Monat 1 = Techniker-Kampagne (M3) und erneute Prüfung.

---

## 8. Quellenverzeichnis (alle abgerufen am 2026-09-21)

1. Grey — „Google Ads Cost in Nigeria (2026): CPC, Budgets, and How to Pay" (Autorität NA; Nigeria-CPC Ø 0,66 $, Local Services 0,15–0,50 $, USD-Billing, 7,5 % VAT): https://grey.co/blog/google-ads-cost-nigeria
2. Tera Creations — „What's the Cost of Running Google Ads in Kenya?" (Autorität NA; KES-CPCs nach Branche): https://teracreations.com/whats-the-cost-of-running-google-ads-in-kenya-a-realistic-breakdown/
3. Dot Digital — „The Ultimate Guide to Google Ads in Kenya 2025" (Autorität NA; CPC-Spannen KES 15–150): https://digitalagency.co.ke/blog/google-advertising/the-ultimate-guide-to-google-ads-in-kenya-how-to-get-real-roi-in-2025/
4. BaseCloud — „Google Ads Benchmarks for South African Industries" (Autorität NA; Construction & Trades R 13,27, Renewable Energy R 19,96): https://basecloudglobal.com/google-ads-benchmarks-for-south-african-industries/
5. WordStream/LocaliQ via Admanage — „How Much Does Google Ads Cost? 2026 CPC & CPL Benchmarks" (Autorität B; globaler Search-Ø 5,26 $, CTR 6,66 %): https://admanage.ai/blog/how-much-does-it-cost-to-advertise-on-google
6. Adamigo — „Meta Ads CPM & CPC Benchmarks by Country in 2026" (Autorität NA; Nigeria CPM 1,50 $/CPC 0,12 $, Kenia CPM 2,40 $/CPC 0,22 $, Bot-Hinweis): https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026
7. Superads — „Facebook Ads CPC/CPM Benchmarks South Africa 2025" (Autorität NA; Datensatz 3 Mrd. $ Spend): https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/south-africa
8. WhatsApp for Business — „WhatsApp Business Platform Pricing" (offiziell; 72h-Freifenster bei Ad-Klick): https://whatsappbusiness.com/products/platform-pricing/
9. Zoho — „WhatsApp Message Pricing Changes (Effective July 1, 2025)" (Autorität A; Per-Message-Modell): https://help.zoho.com/portal/en/community/topic/whatsapp-message-pricing-changes-effective-july-1-2025
10. Stackmatix — „TikTok Ads Budget Allocation by Country" (Autorität B; Nigeria CPM ~1,00 $/CPC ~0,08 $, Mindestbudgets): https://www.stackmatix.com/blog/tiktok-ads-budget-allocation-by-country
11. Admanage — „TikTok Ads Cost 2026" (Autorität B; Mindestbudget 50 $/Kampagne, 20 $/Tag/Ad-Group): https://admanage.ai/blog/tiktok-ads-cost
12. Koro — „Click-to-WhatsApp & Messenger Ads Strategy 2025" (Autorität NA; Benchmark Cost per Conversation 1,50–3,00 $ US): https://getkoro.app/blog/click-to-whatsapp-and-messenger-ads
13. Upstream (intern): `marketing-team/reports/research/2026-09-21-laender-priorisierung.md` (Marktpriorisierung, WhatsApp-Penetration, Strom-/Solar-Lage)
14. Lokal beobachteter Code: `request.html`, `assets/marketing-agent.js`, `assets/app.js` (vaTrack/dataLayer, Supabase-Payload, kein gtag/GTM/Pixel)

**Datenlücken:** Keine kontoeigenen Daten (kein Google-Ads-/Meta-Konto ausgewertet); TikTok-Self-Serve-Verfügbarkeit Nigeria unbelegt; tatsächliche Suchvolumina der 14 Keywords in Lagos unbekannt (Keyword Planner vor Launch); „Cost per Conversation" Nigeria ist Extrapolation, nicht gemessen.
