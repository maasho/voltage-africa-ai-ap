# KI-Sichtbarkeits-Strategie (GEO/AI-SEO) für Voltage Africa

**Rolle:** KI_Sichtbarkeit (AI Citation Strategist) · **Datum:** 2026-09-21 · **Status:** Arbeitsbericht mit Stichproben-Belegen
**Methodik-Hinweis:** In dieser Laufzeitumgebung steht kein direkter Zugang zu ChatGPT, Perplexity, Gemini oder Google AI Overviews zur Verfügung. Der Wettbewerbsbefund beruht daher auf 7 stichprobenartigen Websuchen (2026-09-21), die zeigen, welche Quellen und Plattformen für die Ziel-Fragen indexiert und auffindbar sind — das ist der Pool, aus dem KI-Assistenten mit Suchanbindung (Perplexity, ChatGPT-Browsing, AI Overviews) zitieren. Er ersetzt keine echte Multi-Assistenten-Basismessung; der Messplan in Abschnitt 5 definiert, wie diese im ersten Monat nachgeholt wird. Alle Aussagen zur Konkurrenz sind Belege für die kommunizierte Positionierung, nicht für tatsächliche Marktmacht (voltage-evidence).

---

## 1. Zusammenfassung

1. **Voltage Africa ist im Zitationspool faktisch unsichtbar.** Bei der Markensuche erscheint nur die eigene Website; bei keiner der kategoriebezogenen Stichproben (Lagos, Nairobi, Accra, Johannesburg, Abidjan/Dakar) taucht voltage-africa.com auf. Wettbewerber wie **Balozy (Kenia)**, **Kandua/ServiceLink SA (Südafrika)** und **TrustAm/9jaTrade (Nigeria)** dominieren den Pool — teilweise mit explizit auf KI-Zitation optimierten Inhalten (Balozy dokumentiert seine „LLM-Optimization" offen auf der eigenen Seite).
2. **Der frankophone Markt ist die größte Lücke = Chance.** Für Abidjan/Dakar werden kaum dedizierte Plattformen zitiert, sondern Facebook-/Instagram-/TikTok-Posts, das B2B-Verzeichnis Go Africa Online und Einzelanbieter (Yemba). Wer hier zuerst strukturierte, französische Stadt×Gewerk-Inhalte mit klaren Entitäten aufbaut, kann die KI-Antworten faktisch definieren.
3. **Wichtigster Hebel: strukturierte Entitäts- und FAQ-Daten auf den bereits vorhandenen Stadt-/Gewerkeseiten plus Präsenz in den Verzeichnissen, die KI-Antworten füttern** (Go Africa Online, Destinali, StartupList Africa, LinkedIn, ggf. Wikidata/Crunchbase). KI-Assistenten zitieren bevorzugt Seiten mit FAQPage-/Service-Schema, klarer Markenentität und Drittbestätigung.
4. **Ehrlichkeitsvorbehalt:** KI-Antworten sind nicht-deterministisch. Alle Maßnahmen verbessern die Zitationswahrscheinlichkeit; eine Zitation kann nie garantiert werden. Baseline-Messung vor jeder Fix-Implementierung ist Pflicht (Persona-Regel 4).

---

## 2. Prompt-Landschaft (29 Prompts, gruppiert nach Intention)

Aufbauend auf der Länder-Priorisierung (Tier 1: NG, KE, GH, ZA; Tier 2: SN, CI) und den Top-Städten Lagos, Nairobi, Accra, Abidjan, Dakar, Johannesburg.

### A. Empfehlung / „Best-of" (Nachfrageseite, EN)
1. „How do I find a reliable electrician in Lagos?"
2. „What is the best platform to hire a solar installer in Kenya?"
3. „Who are trusted solar installation companies in Accra?"
4. „Recommend a verified fundi for house wiring in Nairobi."
5. „Best app to find vetted artisans in Ghana 2026."
6. „Where can I find a certified electrician in Johannesburg?"

### B. Vergleich (EN)
7. „Fundis vs Balozy — which is better for hiring electricians in Kenya?"
8. „Kandua vs Snupit for finding contractors in South Africa."
9. „Is Jiji a good way to find electricians in Nigeria?"
10. „What are alternatives to word-of-mouth for hiring artisans in Lagos?"

### C. How-to / Kosten / Verifikation (EN)
11. „How much does an electrician charge in Lagos?"
12. „How do I verify an electrician's licence in Ghana?" (Energy Commission)
13. „What should I check before hiring a solar installer in Kenya?" (EPRA-Register)
14. „How do I get a solar system installed at my home in Nigeria — who does it?"
15. „How do I get a Certificate of Compliance for electrical work in South Africa?"

### D. Problem / Notfall (EN)
16. „My breaker keeps tripping — who can fix it in Abuja today?"
17. „Emergency electrician near me in Nairobi."
18. „Generator or solar for my home in Ghana — who can advise and install?"

### E. Frankophon (FR, Tier 2)
19. „Comment trouver un électricien fiable à Abidjan ?"
20. „Quelle plateforme pour trouver un artisan vérifié à Dakar ?"
21. „Combien coûte un dépannage électrique à Abidjan ?"
22. „Où trouver un installateur solaire qualifié au Sénégal ?"
23. „Comment vérifier la qualification d'un électricien en Côte d'Ivoire ?"

### F. Angebotsseite (Techniker, EN/FR)
24. „How can electricians in Nigeria find more customers online?"
25. „Best platform for solar installers to get jobs in Africa."
26. „How to become a verified fundi and get more jobs in Kenya."
27. „Quel site pour trouver des clients en tant qu'électricien au Sénégal ?"

### G. B2B / internationale Partner (EN)
28. „How can an international company find verified local electrical partners in Africa?"
29. „Where can I hire vetted solar technicians for a project in Nigeria or Kenya?"

**Begründung der Auswahl:** A–D spiegeln die belegten Nachfragetreiber (Stromausfälle, Solar-Boom, Vertrauensproblem „geprüfte Fachkraft"). E adressiert die wettbewerbsarme FR-Lücke. F deckt die zweite Marktseite ab (Techniker-Akquise, Rankings/XP-Modell). G entspricht dem auf der Startseite kommunizierten Partner-Angebot („Find verified local partners in 54 countries").

---

## 3. Wettbewerbsbefund (Stichproben 2026-09-21)

### 3.1 Wer wird aktuell gefunden/zitiert — und warum

| Markt | Gefundene Plattformen/Quellen (Auswahl) | Warum sie gewinnen |
|---|---|---|
| **Nigeria (Lagos)** | TrustAm (Blog „Day in the Life of an Electrician in Lagos"), 9jaTrade, Worka, Fixstant, ArtisanOga, wrkman, Fanntal, Everyone.ng; Verzeichnis Destinali | Stadt+Gewerk-spezifische Blogartikel, „verified"-Claims, Review-Snippets, Plattform-Erklärseiten |
| **Kenia (Nairobi/Solar)** | **Balozy** (mehrere Treffer, u. a. „Electricians in Nairobi", „Solar Installation in Kenya"), Fundis, Fundi Link, FundiFix, Fundi Interior Solutions; Solar-Blogs (solarcityecoenergies, naicity) | Balozy betreibt **explizit dokumentierte LLM-Optimierung**: eigener Abschnitt „SEO & LLM Optimization: Why This Blog Ranks" mit LLM-Phrasen, klarer Heading-Struktur, Cluster-Erwähnungen (Syokimau, Machakos, Nairobi). Beleg: balozy.com/solar-installation-in-kenya/ |
| **Ghana (Accra)** | FIXEX, PocketFixer, Flexi Book, **ESCA Tech** (wirbt mit Energy-Commission-Lizenzprüfung), ArteeZan; Instagram-Reels (JustFixIt, TrustLocalGH) | App-Landingpages mit FAQ-Blöcken, Lizenz-/Verifizierungs-Claims, lokale Preistransparenz (Cedi, MoMo) |
| **Südafrika** | **Kandua**, Snupit, **ServiceLink SA** (Vergleichsartikel „Top 5 Snupit Alternatives" mit FAQ-Schema-Struktur), Bark | Vergleichs-/„Best-of"-Content mit Feature-Tabellen, Review-Authenticity-Claims, Autor-Box mit Expertise-Angabe |
| **Frankophon (CI/SN)** | **Kein dominanter Plattform-Anbieter.** Treffer: Facebook-/Instagram-/TikTok-Posts einzelner Elektriker, **Go Africa Online** (panafrikanisches B2B-Verzeichnis, Rubrik „Électriciens"), Yemba Services (Abidjan-Guides mit FAQ), sMaxSell (Verzeichnis „Artisans vérifiés Afrique de l'Ouest") | Verzeichnisse + Social Posts; fast keine strukturierten Plattform-Inhalte → Definitionsmacht ist offen |

### 3.2 Zitationsrelevante Muster (generalisiert aus den Stichproben)

1. **Verzeichnisse füttern KI-Antworten nachweislich als Geschäftsmodell:** Destinali verkauft Listings explizit mit „Your free listing is visible in Google and AI search from day one — AI search tools crawl structured directories when answering local business questions" (destinali.com/free-business-listing, abgerufen 2026-09-21). Das bestätigt: strukturierte Drittverzeichnisse sind ein direkter Zitationskanal.
2. **FAQ-Blöcke auf Service-Seiten gewinnen:** FIXEX (Accra), Fundi Link (FAQ-Seite), Yemba (Abidjan mit „Questions fréquentes"), ServiceLink SA (ausführliche FAQ) haben alle sichtbare Q&A-Strukturen — exakt das Format, das Antwortmaschinen übernehmen.
3. **Verifikations-Claims sind das Differenzierungs-Keyword:** „NIN-verified" (Worka, Fanntal), „Energy Commission licensed" (ESCA Tech), „5-step verification" (ServiceLink SA), „EPRA" (Kenia-Kontext). KI-Antworten auf „reliable/trusted"-Fragen greifen genau diese Signale auf.
4. **Social-Media-Posts erscheinen in schwach abgedeckten Märkten** (Ghana- und FR-Stichprobe: Instagram/Facebook/TikTok mit Autorität A). Dort fehlt es an strukturierten Webquellen — ein Nachteil für die Antwortqualität, eine Chance für Voltage.
5. **Voltage Africa selbst:** Nur die eigene Domain wird bei Markensuche gefunden (Startseite, faq.html, about.html, contact.html). Kein einziger Dritttreffer, kein Verzeichnis, kein Presse-/Profilfund in der Stichprobe. Wikidata-/Wikipedia-/Crunchbase-Status: in der Markensuche kein Eintrag aufgetaucht (nicht abschließend verifiziert — siehe Datenlücken).

---

## 4. Zitier-Hebel für voltage-africa.com (konkret)

### 4.1 Strukturierte Daten (Schema.org) — je Seitentyp

| Seitentyp (lokal vorhanden laut WEBSITE-CONTEXT) | Schema-Typen | Schlüsselfelder |
|---|---|---|
| Alle Seiten (Layout) | `Organization` + `WebSite` | name „Voltage Africa" (konsistent, kein Wechsel mit „Voltage Afrika"), url, logo, sameAs (LinkedIn, Facebook, Crunchbase, Wikidata sobald vorhanden), contactPoint |
| Startseite | zusätzlich `WebSite` mit `potentialAction` (SearchAction), `Organization` mit `areaServed` (Kontinent/Länderliste) | Länder nur nennen, wenn Abdeckung belegbar — sonst „Afrika" als areaServed ohne Zahlenclaims |
| Stadt-/Gewerkeseiten (z. B. Elektriker Lagos) | `Service` (+ optional `FAQPage`) | serviceType („Electrician services"), areaServed: City + Country, provider: Organization, ggf. `offers` nur mit belegten Preisrahmen |
| rankings.html | `ItemList` (Rankings) | itemListElement mit Position, nur echte Profildaten; keine erfundenen Bewertungen |
| members.html / profile.html | `ProfilePage` / `Person` (sparsam, DSGVO-/Einwilligungsprüfung) | nur öffentlich freigegebene Profildaten, jobTitle, nationality/areaServed |
| faq.html + Ratgeber | `FAQPage`, `Article`/`BlogPosting` | Q&A exakt in Prompt-Mustern formulieren (s. Abschnitt 2); Article mit author, datePublished, dateModified |
| about.html / contact.html | `AboutPage`/`ContactPage` + Verweis auf Organization | eindeutige Entity-Verknüpfung via `@id` |
| Rechner (calculators.html) | `WebApplication` | name, applicationCategory, isAccessibleForFree |

**Regeln:** Nur markieren, was auf der Seite sichtbar steht (Google-/Qualitätsrichtlinien). `aggregateRating`/`review` nur mit echten, nachvollziehbaren Bewertungen — sonst weglassen (Abmahn-/Spam-Risiko und Widerspruch zu voltage-evidence). Keine afrikanische Gesamtabdeckung („54 countries") in strukturierten Daten behaupten, solange die Anbieterabdeckung nicht belegt ist.

### 4.2 FAQ-Formate nach Prompt-Mustern

- Pro Start-Stadt × Gewerk eine FAQ-Sektion mit 5–8 Fragen, die wörtlich die Prompt-Muster aus Abschnitt 2 spiegeln: „How much does an electrician cost in Lagos?", „How do I verify an electrician's licence in Ghana?" → Antworten mit lokalen, belegten Fakten (EPRA-Register Kenia, Energy Commission Ghana, CoC/SANS 10142-1 Südafrika, NEMSA-Status Nigeria — Letzterer vor Veröffentlichung primär prüfen, vgl. Länderbericht Maßnahme 2).
- FR-Versionen für Abidjan/Dakar parallel aufbauen (nicht maschinell übersetzen lassen ohne Prüfung): „Comment trouver un électricien fiable à Abidjan ?"
- Antwortstil: direkte Antwort im ersten Satz (40–60 Wörter), dann Details — das ist das von Antwortmaschinen bevorzugte Extraktionsformat.

### 4.3 Eindeutige Entitäten

- **Namens-Konsistenz:** „Voltage Africa" überall identisch (Website, Verzeichnisse, Social, Schema). Keine Varianten („Voltage Afrika", „VoltageAfrica") streuen.
- **Organization-Entity mit stabiler `@id`** (z. B. `https://www.voltage-africa.com/#org`), auf die alle Service-/FAQ-Markups verweisen.
- **AreaServed sauber trennen:** Land ≠ Sprache ≠ Stadt. Pro belegtem Markt eigene Entity-Angaben.

### 4.4 Quellenwürdigkeit: Drittseiten, die KI-Antworten füttern (priorisiert)

| Priorität | Quelle | Warum | Aufwand |
|---|---|---|---|
| P1 | **LinkedIn-Unternehmensseite** | Wird von allen Assistenten gern zitiert; Snupit-Stichprobe zeigt LinkedIn-Indexierung | gering |
| P1 | **Go Africa Online** (goafricaonline.com) | Das im FR-Raum zitierte panafrikanische Verzeichnis — direkter Tier-2-Hebel | gering |
| P1 | **Destinali** (destinali.com) | Verkauft explizit AI-Search-Sichtbarkeit; strukturiertes Listing | gering (kostenlos) |
| P2 | **StartupList Africa** (startuplist.africa) | Wird in der Wettbewerbsrecherche als Sektor-Quelle genutzt; füttert „African startups"-Antworten | gering |
| P2 | **Crunchbase-Profil** | Standard-Entity-Quelle für ChatGPT/Perplexity bei Firmenfragen | gering |
| P2 | **Wikidata-Eintrag** | Maschinenlesbare Entität; Hürde niedrig, Nutzen für Knowledge Graph mittel | gering–mittel |
| P3 | **Wikipedia** | Aktuell **nicht empfohlen**: Keine unabhängige Berichterstattung belegt → Relevanzkriterien nicht erfüllt, Artikel würde gelöscht und schadet. Erst nach echter Presseberichterstattung neu bewerten | — |
| P3 | Länder-Verzeichnisse (z. B. BusinessList Nigeria, Yellow Pages Kenya, GhanaYello) | lokale Long-Tail-Zitationen | mittel |
| P2 | Google Business Profile (sofern physischer Standort/Service-Area zulässig) | Gemini/AI-Overviews nutzen Google-Ökosystem-Signale | gering–mittel |

### 4.5 Wikipedia/Wikidata/Crunchbase — Bewertung

- **Crunchbase: ja, sofort.** Kostenlos, kein Relevanznachweis nötig, hohe Zitationsfrequenz in KI-Antworten zu Firmen.
- **Wikidata: ja, kurzfristig.** Eintrag mit Sitz, Tätigkeitsfeld, Website, Social-IDs. Auf Neutralität achten (keine Werbesprache), sonst Löschantrag.
- **Wikipedia: nein, vorerst.** Ohne belegte unabhängige Berichterstattung (Presse, Fachmedien) ist enzyklopädische Relevanz nicht darstellbar. Wirkungsvoller Zwischenschritt: 2–3 belegbare Presse-/Fachartikel (z. B. TechCabal, Disrupt Africa) anstreben, dann Neubewertung.

### 4.6 Weitere Signale

- **`llms.txt`** im Webroot (kurze, faktische Beschreibung + Links zu Kerndokumenten): aufstrebender Standard, geringer Aufwand, Wirkung nicht gesichert — als Experiment kennzeichnen.
- **Sauberes HTML statt JS-only-Rendering** auf allen Landingpages prüfen: KI-Crawler lesen bevorzugt statisch ausgelieferten Text (der lokal beobachtete Code ist HTML-basiert — positiv, aber Live-Rendering verifizieren).
- **Datumssignale:** datePublished/dateModified auf Ratgebern pflegen; Perplexity und AI Overviews gewichten Aktualität.

---

## 5. Messplan (monatlich)

### 5.1 Test-Setup

- **Prompt-Set:** die 29 Prompts aus Abschnitt 2, eingefroren pro Messmonat (Versionierung im Report-Ordner); neue Prompts ergänzen, nie ersetzen.
- **Assistenten (4):** ChatGPT (mit Browsing), Perplexity, Google AI Overviews/Gemini, Claude (ohne Suche = Trainingsdaten-Baseline). Pro Prompt **3 Wiederholungen** (Nicht-Determinismus), neue Konversation je Durchlauf.
- **Sprachen:** EN-Prompts und FR-Prompts getrennt auswerten; keine Mischquoten.
- **Dokumentation je Run:** System, Modus (Browsing an/aus), Datum, Prompt, Volltext-Antwort (Anhang), Kodierung.

### 5.2 Kodierung je Antwort (getrennt erfassen, nicht vermischen)

| Code | Definition |
|---|---|
| M1 | Markenerwähnung („Voltage Africa" im Text) |
| C1 | Zitation mit Link/Quellenangabe auf voltage-africa.com |
| R1 | Empfehlung als eine der genannten Optionen (Liste/Empfehlungssatz) |
| R2 | Empfehlung als **Top-/Hauptempfehlung** |
| P1 | Ein konkretes Technikerprofil von Voltage Africa wird genannt |
| Kx | Konkurrent X wird genannt/zitiert (pro Konkurrent kodieren) |

Ausfälle (Fehler, keine Antwort) gehen **nicht** in den Erfolgsnenner (Skill voltage-ai-visibility).

### 5.3 Scorecard-Vorlage (monatlich)

```markdown
# KI-Sichtbarkeits-Scorecard Voltage Africa — [YYYY-MM]
## Setup: Prompts n=29 (EN 24 / FR 5), 3 Wiederholungen, Systeme: ChatGPT+Browse, Perplexity, AI Overviews/Gemini, Claude

| System            | Abfragen (n) | M1 Erwähnung | C1 Zitation | R1 Empfehlung | R2 Top-Empfehlung | Top-Konkurrent (Kx) | Zitationsrate Voltage | Zitationsrate Top-Konkurrent | Lücke |
|-------------------|--------------|--------------|-------------|---------------|-------------------|---------------------|----------------------|------------------------------|-------|
| ChatGPT+Browse    | 87           |              |             |               |                   |                     |                      |                              |       |
| Perplexity        | 87           |              |             |               |                   |                     |                      |                              |       |
| AI Overviews/Gemini| 87          |              |             |               |                   |                     |                      |                              |       |
| Claude (kein Browse)| 87         |              |             |               |                   |                     |                      |                              |       |

## Lost-Prompt-Analyse
| Prompt | System | Wer wird stattdessen zitiert | Warum (Hypothese) | Fix | Prio |
|--------|--------|------------------------------|-------------------|-----|------|

## Trend vs. Vormonat: [± pp je Kennzahl]
```

### 5.4 Zielwerte (Orientierung, keine Garantie)

- Monat 1: **Baseline** (Erwartung aus heutiger Stichprobe: Zitationsrate ≈ 0 % — zu belegen, nicht anzunehmen).
- Monat 3: Erwähnung (M1) in ≥ 10 % der EN-Tier-1-Prompts bei ≥ 2 Systemen; erste C1-Zitationen über Verzeichnis-Profile.
- Monat 6 (Ausblick): Top-3-Nennung (R1) in der FR-Gruppe (Tier 2), wo der Pool heute leer ist.

---

## 6. 90-Tage-Maßnahmenliste (priorisiert nach Aufwand/Wirkung)

| # | Maßnahme | Aufwand | Erwartete Wirkung | Zeitraum |
|---|----------|---------|-------------------|----------|
| 1 | **Schema-Grundgerüst:** Organization+WebSite sitewide, Service+areaServed auf Stadt-/Gewerkeseiten, FAQPage auf faq.html (vorher Live-Audit des aktuellen Markups; Website-Stack nicht als bekannt voraussetzen) | mittel | hoch | Woche 1–3 |
| 2 | **Drittprofile anlegen:** LinkedIn-Unternehmensseite, Crunchbase, StartupList Africa, Go Africa Online (FR!), Destinali — identische Beschreibung, konsistenter Name, sameAs-Verlinkung | gering | hoch | Woche 1–2 |
| 3 | **Baseline-Messung** nach Abschnitt 5 (erste vollständige Scorecard) | mittel | Messbarkeit herstellen (Pflicht vor Fixes) | Woche 2–3 |
| 4 | **FAQ-Blöcke EN** für Lagos, Nairobi, Accra + FAQPage-Schema, Fragen wörtlich aus Prompt-Landschaft, Antworten mit belegten lokalen Fakten (Lizenzregister, Preisrahmen — nur mit Quelle) | mittel | hoch | Woche 3–6 |
| 5 | **FR-Content-Sprint:** FAQ + Stadtseiten Abidjan & Dakar auf Französisch (Prompts 19–23, 27) — Angriff auf den leeren FR-Zitationspool | mittel | hoch (geringer Wettbewerb) | Woche 5–8 |
| 6 | **Wikidata-Eintrag** + sameAs-Verknüpfung | gering | mittel | Woche 6 |
| 7 | **Verifikations-Entity-Seite:** „How Voltage Africa verifies technicians" (EN/FR) mit sauber getrennten Prüfstufen (Selbstauskunft/Identität/Dokumente/Zulassung) — nur kommunizieren, was tatsächlich umgesetzt ist | mittel | hoch für „trusted/reliable"-Prompts | Woche 6–9 |
| 8 | **Vergleichs-/Guide-Content:** „How to choose a solar installer in Kenya (EPRA checklist)", „Electrician costs in Lagos 2026" — datenbasiert, mit Quellen | mittel–hoch | mittel–hoch | Woche 8–12 |
| 9 | **llms.txt** + Prüfung statisches HTML-Rendering der Kerneiten | gering | unklar (Experiment) | Woche 9 |
| 10 | **Zweite Messung (Recheck Tag ~60) + dritte Messung (Tag ~90),** Lost-Prompt-Analyse, Fix-Pack Runde 2 | mittel | Iteration | laufend ab Woche 8 |
| 11 | **Presse-Anbahnung** (TechCabal, Disrupt Africa o. ä.) als Vorbereitung späterer Wikipedia-Relevanz | hoch | langfristig | ab Woche 10 (parallel) |

**Nicht tun:** Review-/Rating-Markup ohne echte Bewertungen, „54 Länder"-Abdeckung in Schema/Content ohne Beleg, Wikipedia-Artikel ohne Pressegrundlage, automatisierte Massenkommentare in Foren (Risiko: Spam-Signal, Reputation).

---

## 7. Quellen (alle abgerufen am 2026-09-21)

1. Balozy — „Trusted Solar Installation in Kenya" (enthält Abschnitt „SEO & LLM Optimization"): https://www.balozy.com/solar-installation-in-kenya/
2. Balozy — „Electricians in Nairobi: Verified Fundis": https://www.balozy.com/electricians-in-nairobi-verified-fundis-balozy/
3. TrustAm — „Day in the Life of an Electrician in Lagos": https://www.trustamai.com/blog/day-in-the-life-of-an-electrician-in-lagos-what-its-really-like
4. 9jaTrade — https://9jatrade.com/
5. Worka (NIN-Verifizierung) — https://myworka.com.ng/
6. Destinali — „Free Business Listing … visible in Google and AI search": https://destinali.com/free-business-listing
7. Fundis (Kenia) — https://fundis.co.ke/
8. Fundi Link (inkl. FAQ) — https://fundilink.com/ und https://www.fundilink.com/faq
9. ESCA Tech — „Electrician in Accra — Energy Commission licensed": https://escatechapp.com/electrician-accra
10. FIXEX — „Electrician Near You in Accra": https://fixex.app/services/electrician
11. PocketFixer Ghana — https://pocketfixer.app/
12. Kandua — https://kandua.com/
13. ServiceLink SA — „Top 5 Snupit Alternatives": https://www.servicelinksa.co.za/snupit-alternatives-south-africa/
14. Go Africa Online — Verzeichnis „Électriciens": https://www.goafricaonline.com/annuaire/electriciens
15. Yemba Services — „Électricien à Abidjan" + „Quand appeler un électricien à Abidjan": https://yembaservices.com/electricien-a-abidjan/ , https://yembaservices.com/electricien-a-abidjan-depannage-urgence/
16. sMaxSell — „Artisans vérifiés Afrique de l'Ouest": https://artisan.smaxsell.com/services/electricite
17. Voltage Africa — Startseite, FAQ, About, Contact: https://www.voltage-africa.com/ , /faq.html , /about.html , /contact.html
18. Upstream: Länder-Priorisierung 2026-09-21 (marketing-team/reports/research/2026-09-21-laender-priorisierung.md) — Wettbewerbs- und Marktkontext, vollständiges Quellenverzeichnis dort.

## 8. Datenlücken (explizit)

1. **Keine echte Multi-Assistenten-Messung:** Der Wettbewerbsbefund ist ein Websearch-Proxy, keine getestete KI-Antwort. Baseline (Abschnitt 5) steht noch aus; die heutigen Befunde können Zitationsverhalten nur approximieren.
2. **Kein technisches Audit des Live-Markups:** Ob voltage-africa.com bereits Schema.org ausliefert, wie das HTML gerendert wird und ob Crawler-Zugang (robots.txt, Sitemap) sauber ist, wurde in diesem Lauf nicht geprüft — Voraussetzung für Maßnahme 1.
3. **Wikidata-/Wikipedia-/Crunchbase-Ist-Stand** nicht abschließend verifiziert (kein Fund in der Marken-Stichprobe, aber keine Registerabfrage durchgeführt).
4. **Keine Daten zum tatsächlichen KI-Nutzungsanteil** in den Zielmärkten (wie viele Nutzer in Lagos/Nairobi/Accra/Abidjan tatsächlich KI-Assistenten statt Google/WhatsApp-Gruppen für die Handwerkersuche nutzen — Annahme aus dem Briefing, nicht belegt).
5. **Wettbewerbsstärke nur qualitativ:** Nutzer-/Traffic-Zahlen von Balozy, Kandua, TrustAm & Co. unbekannt; Zitationshäufigkeit in echten Assistenten-Antworten ungemessen.
6. **Verifizierungsstatus Voltage Africa:** Was die Plattform tatsächlich prüft (Identität, Dokumente, Zulassung), ist nicht belegt — Maßnahme 7 darf nur umsetzen, was betrieblich stimmt.
