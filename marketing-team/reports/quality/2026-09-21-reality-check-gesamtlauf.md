# Reality Check — Gesamtlauf aller 24 Fachbereichsberichte

**Datum:** 2026-09-21
**Rolle:** Qualitätsprüfer (Reality Checker) — Fach- und Funktionsprüfung
**Geprüfter Bestand:** 24 Berichte unter `marketing-team/reports/<fachbereich>/2026-09-21-*.md`
**Prüfmethode:** Vollständige Lektüre aller 24 Berichte; Strukturprüfung je Bericht; 13 fachliche Stichproben (8 Code-Verifikationen im Website-Repository, 5 externe Web-Verifikationen); Widerspruchs-Check quer durch alle Berichte.
**Prüfmaßstab:** AGENTS.md, SENIOR-STANDARD.md — Belege vor Behauptungen, Datenlücken explizit, keine erfundenen Zahlen, nächste Maßnahmen benannt.

---

## 1. Zusammenfassung

Der Gesamtlauf vom 2026-09-21 ist in dieser Form **freigabefähig (PASS)**. Alle 24 Berichte existieren, sind formal vollständig und halten sich mit sehr hoher Disziplin an den Senior-Standard: Keine erfundenen Kennzahlen, Datenlücken sind fast durchgehend explizit benannt, Sekundärquellen werden als solche gekennzeichnet, und kritische Befunde werden nicht weichgespült.

Bemerkenswert ist die **Kreuzvalidierung zwischen Berichten**: Der schwerste Einzelbefund — US-Dollar-Vergütungsversprechen (`rw_1`–`rw_4`, `sg_a1_d`) im Code im Widerspruch zu `terms.html` („no cash value") — wurde von zwei Fachbereichen (community, trust) **unabhängig voneinander** gefunden. Ebenso decken sich der marketplace-Befund (Instant-Match filtert auf Land statt Stadt) mit der analytics-Datenlücke L4 (`profiles` ohne `city`-Abdeckung) und der ads-Befund (kein Tracking-Backend) mit analytics L1.

Das Gesamtrisiko liegt **nicht in den Berichten, sondern im geprüften Objekt**: Der Website-Code enthält drei P0-Befunde (Geldwert-Widerspruch, RLS-Lücke in `profiles`, OG-/Meta-Generator-Bug auf 30 Stadtseiten), die von den Berichten korrekt und belegbar beschrieben werden. Meine Code-Stichproben haben **jede einzelne geprüfte Behauptung der Berichte bestätigt** — in keiner Stichprobe wurde ein Berichtsbefund widerlegt.

**Gesamturteil: PASS (mit Auflagen an den Betrieb, nicht an die Berichte).**

---

## 2. Strukturprüfung

Prüfkriterien je Bericht: Datei existiert · Zusammenfassung vorhanden · Quellen/Datenlücken benannt · Nächste Maßnahmen benannt · Datum 2026-09-21 korrekt.

| # | Fachbereich | Datei | Zusammenfassung | Quellen / Datenlücken | Nächste Maßnahmen | Datum | Struktur |
|---|---|---|---|---|---|---|---|
| 1 | accessibility | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 2 | ads | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 3 | aeo | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 4 | ai-visibility | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 5 | analytics | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 6 | appsec | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 7 | artikel-lagos | ✔ | ✔ | ✔ (gelabelt) | ✔ | ✔ | PASS |
| 8 | artikel-nairobi | ✔ | ✔ | ✔ (gelabelt) | ✔ | ✔ | PASS |
| 9 | community | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 10 | compliance | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 11 | content-roadmap | ✔ | ✔ | ⚠ nur implizit | ✔ | ✔ | **WARN** |
| 12 | creative | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 13 | growth | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 14 | lifecycle | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 15 | linkedin | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 16 | localization | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 17 | marketplace | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 18 | partner | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 19 | pr | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 20 | research | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 21 | seo | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 22 | support | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 23 | trust | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |
| 24 | user-research | ✔ | ✔ | ✔ | ✔ | ✔ | PASS |

**Befund Struktur:** 23/24 vollständig. Einzige Abweichung: **content-roadmap** benennt Quellen und Datenlücken nur implizit innerhalb der Umsetzungshinweise, ohne eigenen Abschnitt — inhaltlich vorhanden, formal nicht dem Standard entsprechend. Reicht für WARN (Struktur), nicht für REVISE.

---

## 3. Fachliche Stichproben

### 3.1 Code-Stichproben (Verifikation im Website-Repository)

| # | Geprüfte Behauptung (Bericht) | Prüfung | Ergebnis |
|---|---|---|---|
| C1 | OG-Bug: Alle 30 Stadt-/Gewerkeseiten tragen `og:title "How it works \| Voltage Africa"` (aeo, seo, localization) | Volltextsuche über alle HTML-Dateien (Root + dist) | **BESTÄTIGT** — 66 HTML-Dateien mit identischem OG-Title; alle Stadtseiten betroffen |
| C2 | Vergütungstexte `rw_1`–`rw_4` nennen $-Beträge ($10–$100 base) im Code (community, trust) | Suche in `assets/i18n.js` + `assets/i18n/en.js` | **BESTÄTIGT** — 8 Treffer (je 4 pro Datei); Widerspruch zu `terms.html` „no cash value" real |
| C3 | Keine `hreflang`-Annotationen auf der gesamten Site (aeo) | Suche über alle HTML-Dateien | **BESTÄTIGT** — 0 Treffer |
| C4 | RLS-Policy `profiles_own_update` erlaubt UPDATE ohne Spaltenbeschränkung; View `verifications_public` ohne `security_invoker` (appsec K1, K3) | `supabase-setup.sql` Z. 26–28, 225–228, 254–258 | **BESTÄTIGT** — K1 und K3 exakt wie beschrieben; `vouch_counts` zeigt, dass das korrekte Muster im selben File existiert |
| C5 | Review-Text „will be verified" widerspricht DB-Verhalten: `reviews_public_read using (true)` (trust #11) | `supabase-setup.sql` Z. 180–182 | **BESTÄTIGT** — Reviews sind sofort öffentlich lesbar, kein Moderationsgate |
| C6 | `request.html` / `calculators.html`: kein `<main>`, kein Skip-Link (accessibility K1); kein Turnstile auf `request.html` (appsec K2) | Direkte Dateiprüfung | **BESTÄTIGT** — beide Befunde korrekt; `signup.html` hat Turnstile (Z. 87–101), aber ebenfalls kein `<main>`/Skip-Link |
| C7 | `assets/data.js:46` hinterlegt deutsche WhatsApp-Nummer `WA_BUSINESS = "491729909687"` (localization F12) | Direkte Dateiprüfung | **BESTÄTIGT** |
| C8 | `locations.html` steht auf `noindex,follow` (seo, aeo) | Direkte Dateiprüfung | **BESTÄTIGT** |
| C9 | Instant-Match filtert Kandidaten auf `country`, nicht `city` (marketplace) | `supabase/functions/instant-match/index.ts` Z. 161–170 | **BESTÄTIGT** — `.eq("country", ...)`; Stadt nur im Nachrichtentext; passt zu analytics L4 (`profiles` ohne city) |
| C10 | `WEBSITE_COPY` deckt nur EN/FR ab, obwohl die Sprachauswahl PT/AR/ZH anbietet (localization) | `assets/website-copy.js` — Top-Level-Keys | **BESTÄTIGT** — nur `en` und `fr`; Sprachbuttons suggerieren Abdeckung, die nicht existiert |

**Zwischenfazit Code:** 10/10 Stichproben bestätigt. Kein einziger Code-Befund der Berichte war falsch oder übertrieben.

### 3.2 Externe Web-Stichproben

| # | Geprüfte Behauptung (Bericht) | Quelle | Ergebnis |
|---|---|---|---|
| W1 | Kenia: ODPC-Registrierung für Data Controller ist Pflicht, Verstoß strafbewehrt, Bußgeld bis KES 5 Mio. / 1 % Jahresumsatz (compliance — zentrale Behauptung) | DPA 2019 §§ 18–24, 63, 72; ODPC Registration Regulations 2021; mehrere Fachquellen | **BESTÄTIGT** — Betrieb ohne Registrierung ist Straftat; Verwaltungsbußgeld bis KES 5 Mio. oder 1 % Umsatz; strafrechtlich bis KES 3 Mio. / 10 Jahre |
| W2 | Google-Ads-CPC Nigeria: Benchmark ~0,66 $ Search, Local Services 0,15–0,50 $ (ads) | Branchen-Benchmarks 2025/2026 (grey.co u. a.) | **BESTÄTIGT** — exakt die vom Bericht genannten Größenordnungen |
| W3 | Afrika-Solarmarkt 2025: +54 % Wachstum (4,5 GW), Nigeria 803 MW (+141 %) (geteilter Kernfakt von research, linkedin, pr) | Global Solar Council, „Africa Market Outlook 2026–2029"; mehrfach sekundär bestätigt (Reuters, Agence Ecofin, PV Tech) | **BESTÄTIGT** — Zahlen übereinstimmend in mindestens 5 unabhängigen Sekundärquellen |
| W4 | IHS Towers: 73 % der Türme mit ausgelagertem O&M (partner) | IHS Holding 20-F / Annual Report 2024 (Primärquelle, SEC) | **BESTÄTIGT** — wörtlich: „as of December 31, 2024, we outsourced certain operations and maintenance activities at 73% of our Towers" (2025: 76 %) |
| W5 | Balozy als dokumentierter Kenia-Wettbewerber mit „SEO & LLM Optimization"-Positionierung (ai-visibility) | balozy.com, App Stores, Presse | **TEILWEISE BESTÄTIGT** — Balozy ist real, aktiv (5.000+ Pros, 40+ Städte) und betreibt erkennbar SEO-getriebenes Content-Marketing; die spezifische Formulierung „LLM Optimization" auf balozy.com konnte ich nicht verifizieren. Kernbefund (Wettbewerber besetzt AI-/SEO-Sichtbarkeit in Kenia) plausibel, Einzelzitat nicht belegt |

**Zwischenfazit Web:** 4/5 voll bestätigt (davon W3 und W4 mit Primär- bzw. mehrfach unabhängigen Sekundärquellen), 1/5 im Kern bestätigt mit unbelegter Detailformulierung.

### 3.3 Nicht verifizierbare Behauptungen

Keine Stichprobe musste wegen fehlender Prüfbarkeit abgebrochen werden. Über die Stichproben hinaus gilt: Berichte, die interne Produktdaten zitieren (z. B. analytics zu Tabelleninhalten), wurden dort plausibilisiert, wo Code-Artefakte (Schema, Edge Functions) dies zuließen; eine Live-Datenbankprüfung war nicht Teil dieses Laufs und ist in den Berichten (appsec, analytics) selbst als ausstehende Maßnahme benannt.

---

## 4. Widerspruchs-Check

**Ergebnis: Kein echter inhaltlicher Widerspruch zwischen den 24 Berichten.** Im Gegenteil — die Querverweise sind konsistent und teils unabhängig doppelt abgesichert:

1. **Geldwert-Widerspruch (Code-intern, nicht berichtsintern):** community und trust haben den Widerspruch `rw_1`–`rw_4` / `sg_a1_d` ($-Beträge) vs. `terms.html` („no cash value") unabhängig voneinander gefunden und übereinstimmend bewertet. Das ist Kreuzvalidierung, kein Widerspruch zwischen Berichten.
2. **ads vs. analytics — kompatibel:** ads stellt fest „kein gtag/GTM/Pixel, aber vaTrack-Event-Schicht vorhanden"; analytics meldet L1 „kein Web-Tracking-Backend". Beide Befunde beschreiben dieselbe Realität aus zwei Richtungen (Events werden geworfen, aber nirgendwo persistent ausgewertet). Kein Widerspruch.
3. **marketplace vs. analytics — deckungsgleich:** Instant-Match filtert auf Land statt Stadt (Code, s. C9); analytics benennt mit L4 fehlende `city`-Granularität in `profiles` als Datenlücke. Ursache und Symptom desselben Problems, konsistent beschrieben.
4. **Konsistente Marktpriorisierung:** Alle strategischen Berichte (research, growth, seo, ads, linkedin, pr, partner) nennen übereinstimmend Tier 1 = Nigeria, Kenia, Ghana, Südafrika. Keine Abweichung gefunden.
5. **Einzige Reibung (Soft-Widerspruch, aufgeklärt):** research/linkedin beschreiben die Website als „in 5 Sprachen verfügbar"; localization weist nach, dass `WEBSITE_COPY` nur EN/FR enthält (s. C10). Das ist kein Fehler in einem der Berichte, sondern ein reales Produktproblem: Die Sprachauswahl verspricht PT/AR/ZH, die Texte existieren nicht. localization hat den Befund korrekt und schärfer formuliert; research/linkedin beschreiben die Oberflächen-Funktionalität. Bewertung: kein Berichtsfehler, sondern bestätigter Produktbefund.

---

## 5. Gesamturteil

| # | Fachbereich | Urteil | Kurzbegründung |
|---|---|---|---|
| 1 | accessibility | **PASS** | Code-Befund K1 stichprobenartig bestätigt (C6); Maßnahmen konkret |
| 2 | ads | **PASS** | CPC-Benchmarks extern bestätigt (W2); Vorbedingungen ehrlich benannt |
| 3 | aeo | **PASS** | OG-Bug (C1) und hreflang (C3) im Code bestätigt; Phasenplan realistisch |
| 4 | ai-visibility | **PASS** | Wettbewerbsbefund im Kern bestätigt (W5); Detailzitat zu Balozy künftig härter labeln |
| 5 | analytics | **PASS** | Datenlücken L1–L4 nachvollziehbar, decken sich mit Code-Befunden |
| 6 | appsec | **PASS** | K1/K2/K3 exakt im Code verifiziert (C4, C6); SQL-Checkliste Q1–Q15 belastbar |
| 7 | artikel-lagos | **PASS** | Quellen mittlerer Güte, aber sauber als solche gelabelt |
| 8 | artikel-nairobi | **PASS** | wie artikel-lagos |
| 9 | community | **PASS** | $-Text-Befund codebestätigt (C2), unabhängig von trust gefunden |
| 10 | compliance | **PASS** | Zentrale Kenia-Behauptung extern bestätigt (W1); Eskalationsliste korrekt priorisiert |
| 11 | content-roadmap | **WARN** | Inhalt belastbar, aber kein expliziter Quellen-/Datenlücken-Abschnitt — Strukturstandard verfehlt |
| 12 | creative | **PASS** | Saubere Trennung Ist-Assets vs. Bedarf |
| 13 | growth | **PASS** | Konsistent mit research/seo/ads; keine erfundenen Funnel-Zahlen |
| 14 | lifecycle | **PASS** | Ehrliche Benennung fehlender Versand-Infrastruktur |
| 15 | linkedin | **PASS** | Geteilter Kernfakt extern bestätigt (W3) |
| 16 | localization | **PASS** | F12 (C7) und EN/FR-Befund (C10) codebestätigt; schärfster Sprachbefund des Laufs |
| 17 | marketplace | **PASS** | Country-Filter-Befund codebestätigt (C9); Coverage-Gate korrekt gefordert |
| 18 | partner | **PASS** | IHS-73-%-Behauptung mit Primärquelle bestätigt (W4) |
| 19 | pr | **PASS** | Kernfakt W3 bestätigt; keine unbelegten Zusagen |
| 20 | research | **PASS** | Zahlenwerk extern bestätigt (W3); Tiers konsistent |
| 21 | seo | **PASS** | OG-/noindex-Befunde codebestätigt (C1, C8) |
| 22 | support | **PASS** | Realistische Einschätzung ohne Support-Backend |
| 23 | trust | **PASS** | Claims #11 (C5) und $-Widerspruch (C2) codebestätigt |
| 24 | user-research | **PASS** | Methodisch sauber; Annahmen als Annahmen markiert |

**Verteilung: 23 × PASS, 1 × WARN, 0 × REVISE.**

**Gesamtlauf-Urteil: PASS** — mit der ausdrücklichen Anmerkung, dass die Auflagen den **Produktzustand** betreffen, nicht die Berichtsqualität: Drei von den Berichten korrekt identifizierte P0-Befunde ($-Claims, RLS, OG-Bug) müssen vor jeder Skalierung der Marketing-Maßnahmen behoben werden.

---

## 6. Die 5 wichtigsten offenen Punkte (an den Betrieb)

1. **Geldwert-Widerspruch beseitigen (blockiert jede Scout-/Marketing-Kommunikation):** `rw_1`–`rw_4` und `sg_a1_d` ($10–$100) aus allen i18n-Sprachpaketen entfernen **oder** ein Vergütungsblatt beschließen und `terms.html` §4 anpassen. Aktuell widerspricht der Code den eigenen AGB — ein rechtliches und Vertrauensrisiko, von community und trust unabhängig belegt (C2).
2. **AppSec P0 umsetzen (K1–K3):** `profiles`-UPDATE-Policy spaltenbeschränken, `verifications_public` mit `security_invoker` absichern (Live-Stand prüfen), Rate-Limit/Turnstile für `requests`/`waitlist` nachziehen. Inklusive Abarbeitung der Orchestrator-SQL-Checkliste Q1–Q15 aus dem appsec-Bericht (C4, C5, C6).
3. **OG-/Meta-Generator-Bug auf 30 Stadtseiten beheben + `locations.html` indexierbar machen (aeo Phase 1):** Solange alle Stadtseiten denselben OG-Title tragen und die Übersichtsseite `noindex` ist, laufen SEO-, Ads- und Social-Pläne ins Leere (C1, C8).
4. **Rechtsklärung vor Skalierung:** Datenschutz-Registrierungen (KE ODPC — Pflicht, strafbewehrt, extern bestätigt W1; GH DPC; NG DCPMI), Einordnung Vermittlungslizenz, Scout-Provisionsmodell. Marketing darf keine „verified"-Claims fahren, solange Registerabgleich und Review-Moderation (C5) nicht stehen (Compliance-Eskalationsliste).
5. **Sprachversprechen ehrlich machen + Coverage messen:** `WEBSITE_COPY`/scout-copy/network existieren nur EN/FR (C10) — PT/AR/ZH-Übersetzungen nachziehen **oder** Sprachbuttons einschränken; parallel i18n-/Sprach-URL-Entscheidung treffen, sonst ist die Tier-2/3-Marktstrategie organisch nicht bespielbar. Ergänzend (Vorbedingung aus ads/marketplace): Ist-Abdeckung an Technikern je Stadt messen, bevor Nachfrage-Kampagnen oder „Live in …"-Claims starten (C9).

---

## 7. Datenlücken dieser Prüfung

- **Keine Live-Datenbankprüfung:** RLS- und View-Befunde wurden gegen `supabase-setup.sql` verifiziert, nicht gegen die produktive Instanz. Der appsec-Bericht benennt dies selbst als ausstehend (Q1–Q15).
- **W5-Detail:** Die Balozy-Formulierung „LLM Optimization" ist unbelegt; der Kernbefund (SEO-getriebener Kenia-Wettbewerber) ist bestätigt.
- **Nicht stichprobiert:** Die übrigen ~16 Berichte wurden vollständig gelesen und plausibilisiert, aber nicht jede Einzelbehauptung extern gegengeprüft. Die Stichprobenauswahl deckte bewusst die risikoträchtigsten Behauptungen ab (Geld, Recht, Sicherheit, geteilte Kernfakten).
