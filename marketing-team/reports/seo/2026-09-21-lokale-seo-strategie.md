# Lokale SEO-Strategie Afrika-Markt für Voltage Africa

**Rolle:** SEO_Spezialist (Lokale SEO) · **Datum:** 2026-09-21 · **Status:** Arbeitsbericht mit Belegen
**Input:** [Länder-Priorisierung Welle 1](../research/2026-09-21-laender-priorisierung.md) (Tier 1: Nigeria, Kenia, Ghana, Südafrika; Tier 2: Senegal, Côte d'Ivoire; Tier 3: Angola, Mosambik)
**Methodik-Hinweis:** Alle Keyword-Fundstellen wurden am 2026-09-21 per Live-Websuche verifiziert (tatsächlich rankende Seiten, FAQ-/PAA-Blöcke auf rankenden Seiten, Formulierungen lokaler Anbieter). **Es wurden keine Suchvolumina erhoben** — ohne Keyword-Planner-/GSC-Zugriff sind Volumen-Angaben nicht seriös möglich. Alle Cluster sind daher nach *belegter Existenz der Suchintention* und strategischem Wert priorisiert, nicht nach Volumen. Dies ist explizit als Datenlücke dokumentiert (Abschnitt 8).

---

## 1. Zusammenfassung

1. **Die Suchintention ist in allen Tier-1-Märkten belegt und deckt sich exakt mit dem Voltage-Modell.** Die dominierenden Suchmuster sind „Beruf + Stadt" (transaktional: „electrician in Lagos", „électricien Abidjan", „eletricista Luanda"), „Beruf + near me" (dringend, mobil), und kostenbezogene Informationsfragen („how much does an electrician charge in Ghana", „cost of solar installation in Nigeria", „prix installation solaire"). Die Konkurrenz rankt mit dünnen Verzeichnis-Listings (Jiji, Kleinanzeigen) oder Einzelbetrieb-Websites — eine Vertrauenslücke, die Voltage mit verifizierten Profilen füllen kann.
2. **Lokale Umgangssprache ist ein Differenzierungshebel:** „fundi (wa umeme)" in Kenia, „dumsor"-Kontext in Ghana, „CoC/certificate of compliance" in Südafrika, „dépannage/urgence" im frankophonen Raum, „gerador vs. solar" in Angola. Kein Mitbewerber außer lokalen Plattformen (FixAm, FIXEX, Fundis, Yemba) besetzt diese Begriffe inhaltlich.
3. **Bestandsbefund der eigenen Seiten (2026-09-21 geprüft):** Die 10 `electricians-*`- und 20 `solar-installers-*`-Stadtseiten sind **inhaltlich dünn** — generische Meta-Description („Solar Installers in Lagos (Nigeria) — Voltage Africa."), **fehlerhafte OG-Tags** (solar-installers-lagos.html zeigt OG-Title/Description von how-it-works), und `locations.html` als Hub ist auf `noindex` gesetzt. Damit existiert die programmatische Hülle, aber ohne indexierbaren Hub und ohne lokale Substanz — das größte technische Defizit vor jeder Skalierung.
4. **Sprach-Architektur-Problem:** Die Website nutzt eine einzige URL pro Seite mit JS-Sprachumschaltung (data-i18n). Für FR- und PT-Märkte (Tier 2/3) ist das ein strukturelles SEO-Hindernis: Google indexiert standardmäßig den gerenderten Ausgangszustand (EN); eigenständige FR/PT-Rankings für „électricien Dakar" oder „eletricista Luanda" sind ohne eigene Sprach-URLs praktisch nicht erreichbar. Hreflang ohne separate Sprach-URLs ist wirkungslos.
5. **Erste 90-Tage-Maßnahme (Empfehlung):** Lagos als Pilot — die drei Lagos-Seiten (electricians-lagos, solar-installers-lagos + neuer Stadtteil-Modifikator) mit echtem lokalem Inhalt ausbauen, OG-/Meta-Fehler beheben, indexierbaren Locations-Hub bauen und Google Business Profile + 5 nigerianische Verzeichnis-Citations anlegen (Details Abschnitt 6).

---

## 2. Keyword-Landschaft je Markt

**Erfassungsmethode:** Pro Markt wurden (a) tatsächlich rankende Seiten für die Kernmuster geprüft, (b) FAQ-Blöcke und „People also search"-Hinweise auf diesen Seiten ausgewertet, (c) Formulierungen lokaler Plattformen (z. B. FixAm: „Also searched as: electrician near me, electrician in my area, electrical contractor, wiring technician") als Beleg realer Suchvarianten übernommen. Anzahl der Cluster pro Markt = Gruppen gleicher Suchintention.

### 2.1 Nigeria 🇳🇬 (EN) — 6 Cluster

| # | Cluster (Primärbegriffe) | Intention | Beleg (2026-09-21) |
|---|--------------------------|-----------|---------------------|
| NG-1 | **electrician in Lagos / Abuja**, electrician near me, electrical contractor Lagos, wiring technician | Transaktional | Jiji.ng-Services-Rubrik Electrical Installation; Muster analog zu GH/KE-Plattformen belegt |
| NG-2 | **solar installer / solar company in Lagos**, best solar companies in Lagos, solar installation Lagos | Kommerziell | GVE Group „10 Best Solar Companies in Lagos" (rankender Listicle); Maypatronic (Lagos, „127+ homes powered") |
| NG-3 | **cost of solar installation in Nigeria**, how much is solar inverter in Nigeria, solar panel price in Nigeria (₦-Fragen) | Informational | Rehoteq, Sun Energy Factory, Topsolarpicks, Sun King Nigeria — mehrere konkurrierende Preis-Guides = belegte Nachfrage. Referenzpreise 2026: 1 kVA ab ~₦800.000, 5 kVA Hybrid ₦4,5–6,5 Mio. |
| NG-4 | **how many solar panels for 3-bedroom house Nigeria**, can solar power AC/fridge, solar vs generator cost | Informational (PAA) | FAQ-Blöcke bei Rehoteq, Sun King (EasyBuy-Raten ab ₦2.000/Woche als lokales Zahlungsmuster!) |
| NG-5 | **inverter installation / inverter repair Lagos**, changeover switch, generator connection | Transaktional | Jiji.com.gh-Inverter-Rubrik analog; NG-Begriff „inverter" wird in Nigeria alltagsprachlich für das ganze Backup-System genutzt |
| NG-6 | **NEPA / PHCN problem, light outage** (Symptom-Suchen, z. B. „how to fix tripping breaker") | Informational | Durch Länderbericht belegter Ausfall-Kontext (11 Netzkollapse 2024); symptomatische Suchen leiten auf Reparaturbedarf |

**Lokale Sprachnotizen:** „NEPA" ist der umgangssprachliche Begriff für Netzstrom (offiziell längst PHCN/DisCos) — wird in Suchen und Content weiterhin genutzt. „Inverter" bedeutet in Nigeria das gesamte Heim-Backup-System, nicht nur das Gerät. Solarfinanzierung über Raten („EasyBuy", PAYGo) ist ein eigenes, konversionsstarkes Thema.

### 2.2 Kenia 🇰🇪 (EN + Swahili-Einsprengsel) — 5 Cluster

| # | Cluster | Intention | Beleg |
|---|---------|-----------|-------|
| KE-1 | **electrician in Nairobi / Mombasa**, **fundi wa umeme**, fundi near me | Transaktional | „fundi wa umeme" als Standardbegriff belegt (Thoonjo Rate-Guide 2026, BilaFundi); Plattform Fundis validiert das Muster |
| KE-2 | **solar installer Nairobi**, solar companies in Kenya, best solar system for home Kenya | Kommerziell | EPRA-Lizenzregister als Vertrauensanker (Länderbericht); reifer Off-Grid-Markt |
| KE-3 | **how much does a fundi charge per day / electrician cost Nairobi** | Informational | Thoonjo 2026: Elektriker KES 2.000–3.500/Tag, KES 800–1.500 pro Punkt — konkrete lokale Preisdaten für Content |
| KE-4 | **EPRA licensed electrician**, wiring certificate KPLC, how to verify electrician Kenya | Informational/Trust | Thoonjo: KPLC verlangt Wiring Certificate von EPRA-lizenzierten Elektrikern vor Netzanschluss — perfekter E-E-A-T-Anker für „verifizierte Fachkraft" |
| KE-5 | **Kenya Power outage / planned maintenance**, backup power solutions Nairobi | Informational | Kenya-Power-Wartungsabschaltungen (Länderbericht, Ghafla) |

**Lokale Sprachnotizen:** „fundi" ist der Schlüsselbegriff — wer in Kenia einen Handwerker sucht, sucht einen „fundi". Swahili-Keywords (z. B. „fundi wa umeme Nairobi") sollten als Sekundärbegriffe im EN-Content natürlich eingebunden werden, nicht als eigene Sprachversion (Swahili-Suchvolumen in Google ist kleiner als EN, aber der Begriff signalisiert lokale Relevanz). M-Pesa als Zahlungsvorteil gehört in jeden CTA-Kontext.

### 2.3 Ghana 🇬🇭 (EN) — 5 Cluster

| # | Cluster | Intention | Beleg |
|---|---------|-----------|-------|
| GH-1 | **electrician in Accra / Kumasi / Tema**, electrician near me, electrical contractor, wiring technician | Transaktional | FixAm (70+ Standorte, Ghana-Card-Verifizierung) und FIXEX listen exakt diese „also searched as"-Varianten |
| GH-2 | **emergency electrician Accra**, 24/7 electrician Ghana | Transaktional (dringend) | Flexi Book Guide „Emergency Electrician in Ghana — How to Find One Fast (24/7)"; Niko's Electricals positioniert sich auf „Emergency" |
| GH-3 | **solar installation cost Ghana**, solar + inverter setup price, dumsor solar solution | Informational→Kommerziell | Mehrere Preis-Guides (Optima, Flexi Book „2026 Cost Guide"); Referenzpreise: 6 kW Paket ~GHS 85.000, 12 kVA ~GHS 135.000 (Deep Solar, YouTube-Build Gbawe) |
| GH-4 | **how much does an electrician charge in Ghana**, cost to wire a house, callout fee | Informational (PAA) | FixAm-Blog 2026: Callout GHS 80–250, Kleinjobs GHS 100–600, Hausverkabelung GHS 3.000–15.000+ |
| GH-5 | **ECG prepaid meter wiring**, distribution board upgrade, inverter installation Ghana | Transaktional | FixAm-Preisliste (prepaid meter wiring GHS 200–800); Jiji.com.gh Inverter-Installation ab GH₵ 5.000 |

**Lokale Sprachnotizen:** „Dumsor" (aus/ein — der ghanaische Begriff für Stromausfälle) ist das emotionale Such- und Content-Thema schlechthin; jede Ghana-Solar-Landingpage sollte den Dumsor-Kontext adressieren. Accra-Stadtteile werden granular gesucht (Osu, East Legon, Spintex, Tema, Dansoman — laut FixAm-Abdeckungsliste): Kandidaten für Stadtteil-Modifikatoren.

### 2.4 Südafrika 🇿🇦 (EN) — 6 Cluster

| # | Cluster | Intention | Beleg |
|---|---------|-----------|-------|
| ZA-1 | **electrician near me**, emergency electrician Johannesburg / Cape Town, electrician in [Suburb, z. B. Sandton, Randburg] | Transaktional | Vellu Digital nennt explizit „electrician near me", „emergency electrician Johannesburg", „electrician in Sandton" als hochvolumige Muster (Agentur-Behauptung, aber konsistent mit rankenden Seiten) |
| ZA-2 | **COC certificate electrician**, electrical certificate of compliance cost, CoC for property sale | Transaktional/Trust | electrical-compliance-certificate.co.za rankt auf genau dieses Thema; CoC ist Pflicht beim Immobilienverkauf → eigenständige, konversionsstarke Nachfrage |
| ZA-3 | **solar installer Johannesburg / Cape Town**, solar installation company, PV GreenCard installer, SAPVIA installer | Kommerziell | Energy Bee „How to Choose a Solar Installation Company" (7-Checks-Liste); GREEN Solar Academy (IE/MIE/ETSP-Klassen) |
| ZA-4 | **SSEG registration Cape Town / Johannesburg**, how to register solar with municipality | Informational | SolarPowerGuide: Kommunen-Vergleich (Cape Town 2–6 Wochen kostenlos vs. Ekurhuleni 10–24 Wochen R4.000+); >1.500 SSEG-Anträge/Monat in Kapstadt (Länderbericht) |
| ZA-5 | **solar maintenance / inverter repair / battery upgrade South Africa**, Sunsynk/Deye installer | Transaktional (Aftermarket) | Marktverschiebung nach Loadshedding-Ende (Länderbericht): Wartung, Upgrade, Zertifizierung statt Notfall-Neuinstallation; Energy Bee „Solar System Upgrade 2026" |
| ZA-6 | **electrician rates per hour Johannesburg**, call-out fee, cost to rewire house | Informational | LeadServices: R350–800/h (Klempner-Referenz analog); Branchenübliches PAA-Muster |

**Lokale Sprachnotizen:** Südafrika ist der einzige Markt mit hartem regulatorischem Keyword-Anker: **CoC (SANS 10142-1)**, **SSEG**, **PV GreenCard/SAPVIA**. Wer diese Begriffe inhaltlich sauber besetzt, gewinnt den Trust-Suchraum. Suburb-Level-Seiten (Sandton, Randburg, Fourways) sind das etablierte lokale Muster.

### 2.5 Senegal 🇸🇳 + Côte d'Ivoire 🇨🇮 (FR) — 5 Cluster

| # | Cluster | Intention | Beleg |
|---|---------|-----------|-------|
| FR-1 | **électricien Dakar / Abidjan**, électricien à domicile, dépannage électricien, électricien urgence | Transaktional | Yemba (Abidjan-Plattform) rankt mit Ratgeber „Quand appeler un électricien à Abidjan : Signes, urgence et prix" — belegt Suchintention + Plattform-Muster WhatsApp-Kontakt nach Commune gefiltert |
| FR-2 | **prix électricien Abidjan / Dakar**, tarif dépannage électrique, devis électricien | Informational | Yemba-Preisrahmen in FCFA (Déplacement + Diagnostic: „quelques milliers à dizaines de milliers FCFA") |
| FR-3 | **installateur panneau solaire Dakar / Abidjan**, installation solaire maison, kit solaire Sénégal / Côte d'Ivoire | Kommerziell | Strukturelle Versorgungslücke (Karpowership SN, Netzausfälle CIV — Länderbericht); Wave/Orange-Money-Kontext für Ratenmodelle |
| FR-4 | **prix installation solaire Sénégal / Côte d'Ivoire**, quel kit solaire pour une maison, batterie solaire prix | Informational | Muster aus NG/GH-Preis-Guides übertragbar; lokale FCFA-Preise recherchierbar (Datenlücke, s. Abschnitt 8) |
| FR-5 | **coupures d'électricité / délestage** (Symptom), groupe électrogène vs solaire | Informational | „Délestage" ist der frankophone Standard-Begriff für Lastabwurf — das FR-Äquivalent zu „dumsor"/„loadshedding" |

**Lokale Sprachnotizen:** Frankophone Suchende nutzen „dépannage" (Reparatur/Notdienst) und „devis" (Kostenvoranschlag) — beides gehört in Titles und CTAs. Abidjan wird nach **Communes** gesucht (Cocody, Plateau, Yopougon, Marcory), Dakar nach Stadtteilen (Almadies, Plateau, Ouakam) — Commune-Level ist das natürliche Modifikator-Muster. **Wichtig:** FR-Cluster sind ohne eigene FR-URLs nicht bespielbar (s. Abschnitt 3.4).

### 2.6 Angola 🇦🇴 + Mosambik 🇲🇿 (PT) — 4 Cluster

| # | Cluster | Intention | Beleg |
|---|---------|-----------|-------|
| PT-1 | **eletricista Luanda**, eletricista a domicílio, serviços elétricos Luanda | Transaktional | Angolanisches PT: „eletricista" (brasilianisch wäre identisch, aber „a domicílio" ist EU-PT-Form — Angola folgt EU-PT); Anbieterseiten (EDAFASTTEC) bestätigen Vokabular |
| PT-2 | **painéis solares Luanda / Angola**, kits solares Angola (5 kW, 10 kW, 15 kW), instalação energia solar | Kommerziell | Interlink (Kits 5/10/15 kW, „preço sob consulta"), Sol Power Angola, EDAFASTTEC — mehrere lokale Anbieter = belegter Markt |
| PT-3 | **preço instalação painel solar Angola**, quanto custa energia solar, solar vs gerador (ENDE) | Informational | EDAFASTTEC-Simulator vergleicht explizit „ENDE · Gerador · Solar" (ENDE = staatlicher Verteiler) — bestätigt, dass der Generator-Vergleich die zentrale Kaufentscheidungsfrage ist |
| PT-4 | **manutenção painéis solares**, inversor híbrido, bateria de lítio/gel, bombeamento solar (Agro) | Informational/Aftermarket | Sol Power FAQ (Wartung, 1–3 Tage Installationsdauer); EDAFASTTEC Agro-Solar/Bombeamento — angolanisches Spezialsegment |

**Lokale Sprachnotizen:** Angola-PT verwendet europäisch-portugiesische Formen („factura", „equipa", „telemóvel") — **nicht** brasilianisches PT verwenden. Kwanza (Kz) als Währung; Preistransparenz ist im Markt kaum vorhanden („sob consulta") — ein Preis-Guide wäre hier ein Alleinstellungsmerkmal. Mosambik (Maputo) teilt das Vokabular, ist aber wegen 20 % Internetpenetration erst Welle 3 (Länderbericht).

### Cluster-Gesamtübersicht
**31 Keyword-Cluster** über 6 Märkte/Sprachräume (NG 6, KE 5, GH 5, ZA 6, FR 5, PT 4), davon ~11 transaktional, ~8 kommerziell, ~12 informational/PAA.

---

## 3. Programmatic-SEO-Architektur (Stadt × Gewerk)

### 3.1 Bestandsaufnahme (geprüft 2026-09-21, lokale Dateien)

| Element | Ist-Zustand | Bewertung |
|---------|-------------|-----------|
| Stadtseiten Elektriker | 10 Städte (`electricians-{stadt}.html`) | Hülle vorhanden |
| Stadtseiten Solar | 20 Städte (`solar-installers-{stadt}.html`) | Hülle vorhanden |
| Locations-Hub | `locations.html` mit `noindex,follow` | ❌ Hub unsichtbar für Google — interne Linkstruktur endet im Leeren |
| Meta/OG | Generische Descriptions; **falsche OG-Tags** (OG-Title/Description von how-it-works auf solar-installers-lagos.html) | ❌ Copy-Paste-Fehler, verwässert Snippet-Qualität und Social Shares |
| Gewerke | Nur 2 (electricians, solar-installers) | Techniker/IT fehlen als Seitentyp |
| Sprachen | 1 URL/Seite, JS-Umschaltung (data-i18n), `<html lang="en">` | ❌ FR/PT/AR/ZH ohne eigene indexierbare URLs |
| Sitemap/Hreflang | Laut Briefing kürzlich saniert | Gilt nur für bestehende EN-URLs; ohne Sprach-URLs hat hreflang keine Ziele |

### 3.2 Zielstruktur: vollständige Matrix, gestaffelte Tiefe

**URL-Schema (flach beibehalten, statischer Stack):**
```
/{gewerk}-{stadt}.html                          → bestehend (electricians-lagos.html)
/{gewerk}-{stadt}-{stadtteil}.html              → optional, nur bei belegter Nachfrage + Substanz
/fr/{gewerk}-{stadt}.html  ·  /pt/{gewerk}-{stadt}.html  → Sprachversionen (Phase 2)
```

**Gewerke-Matrix (alle Länder verfügbar, keine künstliche Beschränkung):**

| Gewerk-Slug | EN | FR | PT |
|---|---|---|---|
| electricians | Electricians in {City} | Électriciens à {Ville} | Eletricistas em {Cidade} |
| solar-installers | Solar Installers in {City} | Installateurs solaires à {Ville} | Instaladores de painéis solares em {Cidade} |
| technicians | Technicians in {City} (AC, Generator, General) | Techniciens à {Ville} | Técnicos em {Cidade} |
| it-specialists | IT Specialists in {City} (Networking, Cabling) | Spécialistes IT à {Ville} | Especialistas de TI em {Cidade} |

**Regel „volle Matrix, gestaffelte Tiefe":** Jede Land×Gewerk-Kombination darf existieren (Skalierbarkeit), aber eine Seite geht nur mit **Mindestsubstanz** live (s. 3.3). Seiten ohne Substanz werden nicht veröffentlicht, sondern als „Bald verfügbar"-Eintrag im Hub gelistet — so wächst die Matrix organisch ohne Doorway-Page-Risiko (Google Spam Policy: keine austauschbaren Massen-Städteseiten).

### 3.3 Seiten-Template (Pflichtelemente pro Stadt×Gewerk-Seite)

1. **Title:** `{Trade} in {City} — Verified & Rated | Voltage Africa` (EN) bzw. landessprachige Variante; ≤ 60 Zeichen.
2. **Meta-Description:** Stadt + Gewerk + Vertrauensversprechen + CTA, ≤ 155 Zeichen, **individuell**, nicht generisch.
3. **H1:** „Verified Electricians in Lagos" (Muster). Lokaler Begriff einbauen: „Find a trusted fundi in Nairobi" / „Électricien vérifié à Abidjan".
4. **Lokaler Nutzungskontext (300–600 Wörter, einzigartig pro Stadt):** Stromlage der Stadt (Lagos: Netzausfälle/Generator-Kosten; Accra: Dumsor + ECG-Tarife; Kapstadt: SSEG-Pflicht), typische Aufträge, Stadtteile/Communes als natürliche Erwähnung.
5. **Preisrahmen-Block:** lokale Währung, mit Quellenstand (z. B. „Tagessatz Elektriker Nairobi: KES 2.000–3.500, Stand 2026, Quelle: Marktübersicht") — der stärkste Differenzierer gegenüber Verzeichnissen.
6. **Verifikations-Block:** Was „verifiziert" bei Voltage konkret bedeutet + landesspezifischer Anker (KE: EPRA-Lizenz; ZA: CoC/DoL-Registrierung; GH: Ghana-Card-Prüfung als Referenzpraxis; SN/CI: lokale Qualifikation — **erst nach Regulierungsklärung aus Welle 1, Maßnahme 2**).
7. **Live-Verfügbarkeitsmodul:** Anzahl/Beispiele verfügbarer Techniker der Stadt (nur echte Daten; bei 0 Technikern Seite nicht indexieren — `noindex` bis Mindestbestand erreicht, sonst erzeugt die Seite Frustration statt Conversion).
8. **FAQ-Block (4–6 Fragen, FAQPage-Schema):** PAA-Fragen des jeweiligen Markt-Clusters (Abschnitt 2), in Landessprache.
9. **CTA:** WhatsApp-first (belegte Kanalpräferenz 92–98 % der Internetnutzer, Länderbericht) + request.html.
10. **Schema:** `Service` + `FAQPage` + `BreadcrumbList`; `areaServed` = Stadt. Kein `LocalBusiness`-Schema für Voltage selbst ohne physische Niederlassung — stattdessen Profilseiten der Techniker später mit echten Daten.
11. **Korrekte OG-Tags:** pro Seite eigen (aktueller Copy-Paste-Fehler beheben).
12. **Hreflang-Set:** sobald Sprachversionen existieren, reziprok zwischen EN/FR/PT-Varianten + `x-default` auf EN; `<html lang>` je Version korrekt.

### 3.4 Interne Verlinkung & kanonische Struktur

- **Hub-Strategie:** `locations.html` von `noindex` auf `index` umstellen und zum echten Hub ausbauen: Länder → Städte → Gewerke (3 Ebenen, max. 3 Klicks von Startseite). Zusätzlich `technicians.html` (Gewerke-Hub) mit locations.html gegenseitig verlinken.
- **Kreuzverlinkung Stadt↔Stadt:** auf jeder Stadtseite „Auch verfügbar in: {2–4 Nachbarstädte desselben Landes}" (Lagos↔Abuja, Accra↔Kumasi, Nairobi↔Mombasa, Johannesburg↔Kapstadt/Durban, Abidjan↔Dakar [FR-Raum], Luanda↔[Welle 3]).
- **Kreuzverlinkung Gewerk↔Gewerk:** Stadtseite Elektriker verlinkt Stadtseite Solar derselben Stadt (gleiche Kaufabsicht, Überschneidung „inverter installation").
- **Guides → Stadtseiten:** Jeder Ratgeber endet kontextuell auf passenden Stadtseiten (solar-sizing-nigeria → solar-installers-lagos/-abuja; choosing-solar-installer-kenya → solar-installers-nairobi; hiring-electrician → alle electricians-*). Stadtseiten verlinken zurück auf Guides („Ratgeber: So wählen Sie…").
- **Canonicals:** selbstreferenziell pro URL; Sprachversionen sind eigenständige Dokumente (kein Cross-Canonical zwischen Sprachen).
- **Kannibalisierungs-Regel:** Pro (Stadt×Gewerk) genau eine URL als Owner des Primärkeywords. Stadtteilseiten bekommen den Stadtteil-Modifikator als Primärkeyword, nie das Stadt-Keyword (z. B. Owner „electrician Sandton" = electricians-johannesburg-sandton; Owner „electrician Johannesburg" bleibt electricians-johannesburg).

### 3.5 Sprach-Architektur (kritisch für Tier 2/3)

Empfehlung: **Subdirectory-Ansatz** `/fr/`, `/pt/` (später `/ar/` für Ägypten-Check) mit echten statischen URLs pro Sprachversion, mindestens für die Stadtseiten der FR/PT-Märkte + hire.html + request.html. Begründung: JS-Umschaltung ohne eigene URL macht FR/PT-Rankings faktisch unmöglich (ein Dokument, eine Sprache, kein hreflang-Ziel). Übergangsoption bei begrenzten Ressourcen: für Tier-2-Start nur **10 Kernseiten in FR** (electricians/solar-installers × {abidjan, dakar} + hubs) als vollwertige statische FR-Seiten statt kompletter Site-Spiegelung.

---

## 4. Content-Gap-Analyse

### 4.1 Bestand (4 Guides, alle EN)
`guide-hiring-electrician`, `guide-choosing-solar-installer-kenya`, `guide-solar-sizing-nigeria`, `guide-office-network-cabling` — plus `calculators.html` und `faq.html`.

### 4.2 Belegte Fragen Suchender (aus FAQ-/PAA-Blöcken rankender Seiten, 2026-09-21) → Gap-Mapping

**Nigeria — gefragt, von Voltage nicht beantwortet:**
- „How much does solar installation cost in Nigeria (2026)?" — kVA-Staffel in ₦ (Gap: kein Preis-Guide; Konkurrenz dominiert mit 5+ Guides) → **höchste Priorität**
- „How many solar panels do I need for a 3-bedroom house?" (teils durch sizing-guide abgedeckt, aber ohne ₦-Preise)
- „Is solar cheaper than a diesel generator?" (₦/kWh-Vergleich: Diesel ~₦350–450/kWh vs. Solar ~₦55–80/kWh levelized — Sun Energy Factory)
- „Can I pay for solar in installments?" (PAYGo/EasyBuy-Raten — lokales Zahlungsmuster)
- „How much does an electrician charge in Lagos?" (Callout-/Punkt-Logik analog GH)

**Kenia — gefragt, nicht beantwortet:**
- „How much should you pay a fundi per day?" (KES 2.000–3.500 Elektriker; KES 800–1.500/Punkt — Thoonjo) → Gap
- „What is EPRA licensing / wiring certificate for KPLC?" → Trust-Content, perfekter Fit zu Verifikationsversprechen; **wichtigster einzelner Content-Gap** (verbindet Suchfrage direkt mit dem Voltage-Kernversprechen)
- „Solar PAYGo: how does it work in Kenya?" (reifster PAYGo-Markt, Länderbericht)

**Ghana — gefragt, nicht beantwortet:**
- „How much does an electrician charge in Ghana?" (GHS 80–250 Callout, GHS 100–600 Kleinjobs, GHS 3.000–15.000 Verkabelung — FixAm) → Gap; Konkurrent FixAm besetzt diese Frage bereits mit eigenem Blog
- „Solar installation cost Ghana 2026 / Dumsor-Lösung" (6 kW ~GHS 85.000 Referenz) → Gap
- „Emergency electrician — how to find one fast" → Gap (Dringlichkeitsintention)

**Südafrika — gefragt, nicht beantwortet:**
- „What is a CoC and when do I need one?" (Pflicht bei Verkauf, Versicherung, jeder Elektroinstallation) → Gap
- „How to register SSEG in {Kommune}?" (Kommunen-Vergleich: Kapstadt 2–6 Wochen kostenlos vs. Johannesburg 6–16 Wochen R2.500–15.000) → Gap
- „How to choose a solar installation company" (7-Checks: CoC im eigenen Namen, SAPVIA/PV GreenCard, 5 Jahre Workmanship-Warranty…) → Gap
- „Solar maintenance/upgrade after loadshedding" (Marktverschiebung) → Gap

**Frankophon (SN/CI) — gefragt, nicht beantwortet (komplett weiß, da 0 FR-Content):**
- „Quand appeler un électricien ? Signes, urgence et prix" (Yemba besetzt diese Frage für Abidjan bereits) → Gap
- „Prix installation solaire maison — Sénégal/Côte d'Ivoire" → Gap
- „Groupe électrogène ou solaire — que choisir face au délestage ?" → Gap

**Lusophon (AO) — gefragt, nicht beantwortet:**
- „Quanto custa energia solar em Angola? / Kits solares 5/10/15 kW" (Interlink: „preço sob consulta" — Preistransparenz ist Marktlücke) → Gap
- „Solar ou gerador — comparação ENDE · Gerador · Solar" → Gap

### 4.3 Wichtigster Content-Gap (Gesamtbewertung)
**Der Vertrauens-/Verifikations-Content pro Markt** (Kenia: EPRA + KPLC Wiring Certificate; Südafrika: CoC/SSEG; Ghana/Nigeria: „wie erkenne ich einen geprüften Elektriker"): Er ist gleichzeitig (a) belegte Suchfrage, (b) das Alleinstellungsmerkmal von Voltage gegenüber Jiji & Co., und (c) der E-E-A-T-Anker für alle Stadtseiten. Danach: **Preis-Guides pro Land** (₦/KES/GHS/FCFA/Kz), die den stärksten belegten Informationsbedarf bedienen.

---

## 5. Google Business Profile & lokale Verzeichnisse

### 5.1 Google Business Profile (GBP)
GBP ist in **allen Zielmärkten** verfügbar — die offizielle Google-Support-Länderliste (support.google.com/business/answer/6270107, abgerufen 2026-09-21) enthält u. a. Angola, Côte d'Ivoire und Ghana explizit; Nigeria, Kenia, Südafrika und Senegal sind ebenfalls Teil der Liste. **Einschränkung:** Voltage hat (soweit bekannt) keine physischen Niederlassungen vor Ort. GBP als „Service Area Business" ohne Adresse ist möglich, erfordert aber eine verifizierbare Geschäftsadresse für die Verifikation (Postkarte/Video). **Empfehlung:** GBP pro Pilotstadt anlegen, sobald eine belastbare lokale Verifikationsadresse existiert (z. B. über Scout-/Partner-Struktur); bis dahin keine Scheinadressen (Richtlinienverstoß, Sperr-Risiko). Alternativ zuerst: lokale Citations ohne GBP.

### 5.2 Verzeichnisse je Land (recherchiert 2026-09-21)

| Land | Verzeichnisse / Plattformen | Beleg & Anmerkung |
|---|---|---|
| 🇳🇬 Nigeria | **VConnect** (vconnect.com) — größtes nigerianisches Verzeichnis, Angebotsanfragen; **BusinessList Nigeria** (businesslist.com.ng, 131.155 Listings, Basic 30.000 NGN einmalig); **Finelib** (finelib.com, kostenlos, SEO-Backlink-Wert); **ConnectNigeria** (connectnigeria.com, kostenlos); **NG Contacts** (ngcontacts.com, B2B) | ProInvoice-Guide 2025, RadiusTheme 2026, businesslist.com.ng (jeweils 2026-09-21). Achtung: VConnect/BusinessList sind teils selbst Matching-Kanäle → Profil auf Sichtbarkeit+Backlink ausrichten, nicht auf Lead-Kauf. Jiji.ng (Kleinanzeigen, 169+ Elektro-Inserate, Länderbericht) als Citations-/Marktbeobachtungskanal |
| 🇰🇪 Kenia | **Yellow Pages Kenya** (yellowpageskenya.com); **Mocality** (mocality.co.ke); **Kenya Business Directory**; **Jiji Kenya** (Kleinanzeigen) | Destinali Citations-Guide (2026-09-21). PigiaMe (pigiaMe.co.ke, Kleinanzeigen) — bekannt, in dieser Recherche nicht primär verifiziert → vor Nutzung kurz prüfen |
| 🇬🇭 Ghana | **GhanaYello** (ghanayello.com); **Ghana Business Directory**; **Jiji Ghana** (jiji.com.gh — aktiv mit Solar-Inverter-Rubrik, verifiziert) | Destinali; jiji.com.gh (2026-09-21). Lokale Matching-Plattformen FixAm/FIXEX sind Konkurrenz, kein Citations-Kanal |
| 🇿🇦 Südafrika | **Brabys** (brabys.com — ältestes Verzeichnis Südafrikas, 103 Jahre); **Snupit** (snupit.co.za — 428 Kategorien, 120 Städte, „Pro Verified"); **Hotfrog South Africa**; **Yellow Pages SA**; **Cylex SA** | Brabys, Apify Snupit-Doku, Destinali (2026-09-21). Snupit ist Matching-Plattform (Konkurrenz) — Listing nur zur Citation, Leads laufen über deren System |
| 🇸🇳 Senegal | **Go Africa Online Senegal** (goafricaonline.com — führendes frankophones Afrika-Verzeichnis, Kategorien u. a. „Énergie / Génie électrique"); **Expat-Dakar** (expat-dakar.com, Kleinanzeigen) — vor Nutzung verifizieren | goafricaonline.com (2026-09-21) |
| 🇨🇮 Côte d'Ivoire | **Go Africa Online Côte d'Ivoire**; lokale Kleinanzeigen-Portale prüfen | goafricaonline.com (2026-09-21). Yemba ist Matching-Konkurrenz, kein Citations-Kanal |
| 🇦🇴 Angola | **Go Africa Online Angola** (deckt lusophone Märkte ab); **ProdAfrica** (prodafrica.com, kontinentweites B2B-Verzeichnis) | goafricaonline.com, prodafrica.com (2026-09-21). Dünnste Verzeichnislandschaft aller Märkte — umso höherer Wert jeder Citation |
| Kontinentweit | **Destinali** (1 Mio.+ Listings, 54 Länder, kostenlos); **ProdAfrica**; **Africa Business Pages** (africa-business.com, B2B-Fokus) | destinali.com, prodafrica.com, africa-business.com (2026-09-21). B2B-Verzeichnisse nur sekundär (Voltage ist B2C/B2B2C) |

**Citations-Disziplin:** einheitliche NAP-Daten (Name, Website, Kategorie „Electrician / Solar energy company", WhatsApp-Nummer) über alle Verzeichnisse; vollständige Profile (Beschreibung, Kategorien, Fotos) schlagen Teilprofile.

---

## 6. 90-Tage-Priorisierungsplan

### Phase 1 (Tag 1–30): Fundament reparieren + Lagos-Pilot
1. **Technische Quick Fixes (Woche 1–2):** OG-/Meta-Fehler auf allen 30 Stadtseiten beheben; individuelle Meta-Descriptions; `locations.html` von noindex auf index + Ausbau zum Länder→Städte→Gewerke-Hub; selbstreferenzielle Canonicals prüfen.
2. **Lagos-Trio ausbauen (Woche 2–4):** electricians-lagos, solar-installers-lagos + (neu) Inverter-/Backup-Fokus im Text; je 400–600 Wörter einzigartiger lokaler Kontext (Netzlage, ₦-Preisrahmen mit Quellenstand, Stadtteile Lekki/Ikeja/Yaba/Surulere, FAQ-Block mit FAQPage-Schema, WhatsApp-CTA). Live-Verfügbarkeitsmodul erst, wenn echte Technikerdaten vorliegen — sonst Seiten bis dahin `noindex` lassen.
3. **Citations Nigeria (Woche 3–4):** BusinessList, Finelib, ConnectNigeria, VConnect, Destinali — einheitliche NAP.
4. **Content 1 (Woche 4):** „Solar Installation Cost in Nigeria 2026" (kVA-Staffel, ₦-Preise, Generator-Vergleich, Ratenoptionen) — verlinkt auf beide Lagos-Seiten.

### Phase 2 (Tag 31–60): Tier-1-Rollout EN + Trust-Content
5. **Nairobi & Accra** nach Lagos-Template ausbauen (KE: „fundi"-Begriff, EPRA/KPLC-Block, KES-Preise; GH: Dumsor-Kontext, GHS-Preise, Accra-Stadtteile).
6. **Content 2+3:** „EPRA-Lizenz & KPLC Wiring Certificate: So erkennen Sie einen geprüften Elektriker in Kenia" (EN) + „How much does an electrician charge in Ghana?" (GHS-Guide). Beide auf Stadtseiten verlinken.
7. **Citations Kenia + Ghana** (Yellow Pages Kenya, Mocality, GhanaYello, Jiji-Profile).
8. **Südafrika-Vorbereitung:** electricians-johannesburg + solar-installers-cape-town mit CoC-/SSEG-Blöcken (Nachfrage dort ist Compliance-getrieben); Content 4: „CoC & SSEG: was Hausbesitzer in Südafrika wissen müssen".

### Phase 3 (Tag 61–90): Frankophoner Pilot + Messung
9. **FR-Subdirectory `/fr/`** mit 10 Kernseiten (electricians/solar-installers × abidjan, dakar + FR-Hubs), hreflang-Set EN↔FR reziprok. FR-Content 5: „Quand appeler un électricien à Abidjan — signes, urgence, prix (FCFA)".
10. **Citations FR:** Go Africa Online Senegal + Côte d'Ivoire, Destinali.
11. **Mess-Setup:** Google Search Console einrichten/verifizieren (Voraussetzung für alle Rankings-Aussagen — aktuell nicht vorhanden); Baseline Impressionen/Klicks je Stadtseite dokumentieren; Cannibalization-Check nach 4–6 Wochen GSC-Daten (Owner-Zuordnung pro Cluster prüfen).
12. **Review & Gate:** Erst nach Lagos/Nairobi/Accra-Validierung (Impressionen > 0, erste Klicks, erste WhatsApp-Anfragen) weitere Städte skalieren (Abuja, Kumasi, Mombasa, Kapstadt als nächste Kohorte).

**Explizit NICHT in den 90 Tagen:** Technicians-/IT-Gewerkeseiten (Matrix-Erweiterung erst nach Validierung der zwei Kern-Gewerke), AR-Version/Ägypten (separater Strategie-Check laut Länderbericht), Angola-PT-Seiten (Welle 3, frühestens nach FR-Validierung), Stadtteilseiten (erst wenn Stadtseiten ranken).

---

## 7. Quellen (alle abgerufen am 2026-09-21)

**Keyword-/Suchintentionsbelege:**
1. GVE Group — „10 Best Solar Companies in Lagos": https://gve-group.com/best-solar-companies-in-lagos/
2. Maypatronic (Solar Lagos, Preise/FAQ): https://www.maypatronic.com/
3. Rehoteq — Solar PV Cost Nigeria (kVA-Staffel ₦): https://rehoteq.com/solar.html
4. Sun Energy Factory — Solar Cost Nigeria 2026 (Generator-Vergleich ₦/kWh): https://sunenergyfactory.com/solar-cost-in-nigeria-2026-pricing/
5. Sun King Nigeria — Preise/EasyBuy/FAQ: https://ng.sunking.com/blog/how-much-do-solar-panels-cost-in-nigeria/
6. Topsolarpicks — Solar Panel Price Nigeria: https://topsolarpicks.com/solar-panel-price-in-nigeria-2025/
7. Thoonjo — „How Much Should You Pay a Fundi Per Day in Kenya (2026)" (fundi wa umeme, KES-Sätze, EPRA/KPLC): https://www.thoonjo.com/blog/how-much-should-you-pay-a-fundi-per-day-in-kenya-2026-rate-guide/
8. BilaFundi — Labour Rates Tanzania 2025 (fundi-Begriff bestätigend): https://www.bilafundi.com/blog/labour-rates-in-tanzania-2025-what-contractors-and-clients-should-budget-for
9. FixAm Ghana — Electrician Cost 2026 (GHS-Sätze, „also searched as"-Varianten, Ghana-Card-Verifizierung): https://fixam.pro/blog/electrician-cost-ghana und https://fixam.pro/
10. FIXEX Ghana — Electrician Service („electrician near me, in my area, electrical contractor, wiring technician"): https://fixex.app/services/electrician
11. Flexi Book Ghana — Emergency Electrician / Solar Cost Guides: https://www.flexibookservices.com/
12. Deep Solar Ghana — 6 kW Paket GHS 85.000: https://www.deepsolarghana.com/service-page/6kw-solar-installation-ghs-85-000-00
13. Optima Solar — Cost of Solar Panel Installation in Ghana: https://optimasolarsystems.com/cost-of-solar-panel-installation-in-ghana/
14. Jiji Ghana — Solar Inverter Installation (ab GH₵ 5.000): https://jiji.com.gh/142-inverter-installation/solar
15. Vellu Digital — Electricians Website/SEO SA („electrician near me", „COC certificate electrician", „electrician in Sandton"): https://velludigital.com/industries/electricians
16. Electrical Compliance Certificate SA (CoC, Wireman's Licence, DoL): https://electrical-compliance-certificate.co.za/electrical-contractors/electricians/
17. Energy Bee — Solar Company Auswahl (7 Checks) & Solar Upgrade 2026: https://energybee.co.za/guides/best-solar-installation-companies-complete-directory-south-africa-2026 ; https://energybee.co.za/guides/solar-system-upgrade-south-africa-2026
18. SolarPowerGuide — SSEG Registration Kommunen-Vergleich 2025: https://www.solarpowerguide.co.za/article/laws/sseg-registration-south-africa-2025
19. GREEN Solar Academy — Wer darf CoC ausstellen (IE/MIE/ETSP): https://solar-training.org/who-can-issue-a-coc-for-solar-systems/
20. SurgePV — SANS 10142-1:2024 / CoC / SSEG SA: https://www.surgepv.com/blog/south-africa-load-shedding-solar-sizing
21. LeadServices — Home Services Platform SA (R-Sätze, SAPVIA): https://leadservices.co.za/blog/home-services-platform-south-africa/
22. Yemba — „Quand appeler un électricien à Abidjan : Signes, urgence et prix" (FCFA, WhatsApp, Communes): https://yembaservices.com/electricien-a-abidjan-depannage-urgence/
23. EDAFASTTEC Angola (PT-Vokabular, ENDE·Gerador·Solar-Vergleich, Agro-Solar): https://edaf.ao/
24. Sol Power Angola — FAQ (Installationsdauer, Wartung, Kosten): https://www.solpowerangola.com/
25. Interlink — Kits Solares Angola 5/10/15 kW („preço sob consulta"): https://www.interlinkglobalsolar.com/kits-solares-angola
26. Dialogos UE-Angola — Sistemas Solares Domésticos em Angola (PDF): https://dialogosue-angola.org/wp-content/uploads/2024/07/Sistemas-Solares-Domesticos-em-Angola.pdf

**Verzeichnisse/GBP:**
27. Google Support — GBP Supported countries: https://support.google.com/business/answer/6270107
28. Destinali — „How to Build Local Citations for Businesses in Africa": https://destinali.com/nap/how-to-build-local-citations-for-businesses
29. ProInvoice — Top Business Listing Sites Nigeria 2025: https://proinvoice.co/top-business-listing-sites-in-nigeria-to-grow-your-visibility-2025-guide/
30. RadiusTheme — Business Directories Nigeria: https://www.radiustheme.com/business-directories-in-nigeria/
31. BusinessList Nigeria (131.155 Listings, Preise): https://www.businesslist.com.ng/
32. Finelib Nigeria: https://www.finelib.com/
33. Go Africa Online — Verzeichnis (frankophon/lusophon): https://www.goafricaonline.com/directory
34. Brabys (Südafrika): https://www.brabys.com/za/directories
35. Apify — Snupit-Dokumentation (428 Kategorien, 120 Städte): https://apify.com/crawlerbros/snupit-scraper
36. ProdAfrica: https://maps.prodafrica.com/
37. Africa Business Pages: https://www.africa-business.com/

**Projektintern:**
38. Länder-Priorisierung Welle 1 (2026-09-21): ../research/2026-09-21-laender-priorisierung.md (inkl. Jiji.ng, Fundis, Eskom/Loadshedding, Dumsor, GOGLA/Ember-Marktdaten)

---

## 8. Datenlücken (explizit)

1. **Keine Suchvolumina:** Ohne Keyword-Planner-/GSC-Zugriff sind alle Cluster qualitativ (Existenz der Intention belegt, Größe nicht). Priorisierung basiert auf Belegdichte und Marktfit — nach GSC-Einrichtung (90-Tage-Plan, Maßnahme 11) mit Impressions-Daten nachschärfen.
2. **Keine Rankings-Positionen der eigenen Domain:** GSC nicht verfügbar; ob voltage-africa.com aktuell für irgendein Cluster rankt, ist unbekannt.
3. **FR/PT-Preisdaten dünn:** FCFA-Preise nur als grobe Spanne (Yemba); Kwanza-Preise für Solar in Angola gar nicht öffentlich („sob consulta") — Preis-Guides für diese Märkte erfordern Primärrecherche (Scout-Interviews / Anbieteranfragen).
4. **Kenia-Verzeichnisse:** PigiaMe, Jiji Kenya in dieser Recherche nicht primär verifiziert; Mocality/Yellow Pages Kenya nur über Sekundärquelle (Destinali).
5. **Senegal-Kleinanzeigen:** Expat-Dakar aus Alltagswissen ergänzt, in dieser Recherche nicht primär verifiziert.
6. **Regulierung Elektrohandwerk NG/GH/SN/CI/AO:** offen aus Welle 1 — der „Verifikations-Block" auf Stadtseiten dieser Märkte darf erst nach der Regulierungsmatrix (Welle-1-Maßnahme 2) landesspezifische Zulassungsclaims machen.
7. **Techniker-Verfügbarkeit pro Stadt:** unbekannt — steuert, welche Stadtseiten indexierbar geschaltet werden dürfen (Live-Verfügbarkeitsmodul, Template-Regel 7).
8. **GBP-Verifikationsadresse:** Es existiert keine belegte lokale Geschäftsadresse für GBP-Verifikation; Lösung (Scout-Standort, Partner-Büro, virtuelle Adresse — letztere richtlinienkritisch) muss vor GBP-Anlage geklärt werden.
