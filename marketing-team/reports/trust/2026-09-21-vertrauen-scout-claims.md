# Vertrauens- und Scout-Aussagen präzisieren (GitHub-Issue #2)

Datum: 2026-09-21. Rolle: Vertrauen_Lead (Bewertungen und Vertrauen). Status: lokale statische Prüfung abgeschlossen; keine Website-Änderungen vorgenommen; Ersatztexte sind Vorschläge zur Betreiberfreigabe, nicht veröffentlicht.

## Nachweisgrenze

Geprüft wurden die lokalen Dateien unter `J:\03_Voltage_Africa\Voltage_Afrika_Projects\Voltage-Africa B2\B2\voltage-africa-website`: about.html, faq.html, index.html, rankings.html, members.html, review.html, scout-guide.html, terms.html, hire.html, how-it-works.html, dashboard.html sowie assets/website-copy.js, assets/scout-copy.js, assets/network-copy.js, assets/i18n.js, assets/i18n/{en,fr,pt,ar,zh}.js, assets/app.js, assets/data.js, assets/network.js, assets/scout-workspace.js und supabase-setup.sql. Die i18n-Dateien enthalten die Texte jeweils in einer Zeile (Zeile 3); Fundstellen werden daher über Datei + Schlüssel benannt. Kein Browser-Funktionstest, kein Backend-Zugriff, keine Prüfung privater Profile oder Dokumente. Website-Text belegt die kommunizierte Aussage, nicht deren betriebliche Umsetzung. Der Pilotbericht vom 2026-09-10 (reports/pilot/2026-09-10-trust-review.md) wurde als Vorarbeit berücksichtigt; die Seiten wurden seitdem neu gebaut — mehrere damalige Fundstellen (z. B. scout-guide.html:73) liegen jetzt nur noch in den Archivordnern `Files_mit_zip/` und `Voltage_Africa_Deploy_zip/` vor.

## Zusammenfassung

- Die **sichtbaren Live-Texte** (website-copy.js, scout-copy.js, network-copy.js) sind überwiegend vorbildlich ehrlich: „no guaranteed earnings", „Registration does not guarantee jobs", „no guaranteed response time", „Attribution … does not verify a technician's qualifications". rankings.html und members.html zeigen aktuell einen ehrlichen Pausen-Platzhalter.
- Das Problem liegt in den **mit ausgelieferten i18n-Basispaketen** (assets/i18n.js und assets/i18n/en.js, Zeile 3, gespiegelt in fr/pt/ar/zh und dist/): Dort stehen unverändert die aggressiven Alt-Claims — darunter die **Dollar-Belohnungen rw_1–rw_4 und sg_a1_d („$10 up to $100+")**, die terms.html §4 („no cash value") direkt widersprechen. Diese Schlüssel werden von den aktuellen Root-Seiten nicht mehr referenziert, sind aber in allen fünf Sprachpaketen ausgeliefert und jederzeit reaktivierbar.
- **Drei dormant-i18n-Schlüssel werden weiterhin live zur Laufzeit gerendert** (assets/app.js): rk_empty, wl_desc, wl_ok — letztere beide mit undefiniertem „verified technician".
- **„Verified" ist öffentlich nirgends definiert.** Die Datenbank kennt sauber getrennte Stufen (verifications.level 1–4: Identität / Arbeitsnachweis / Referenz / Lizenz, supabase-setup.sql:194–231) — die Website kommuniziert diese Trennung nicht.
- **Review-Claim widerspricht Datenbankverhalten:** review.html verspricht „will be verified", die Tabelle reviews ist aber sofort öffentlich lesbar (Policy `reviews_public_read ... using (true)`, supabase-setup.sql:180–182); das verified-Flag hat keine publikumswirksame Funktion.
- 27 Claims inventarisiert: 11 belegt sagbar, 11 präzisierungsbedürftig, 5 riskant.

## Claims-Inventar mit Bewertung

Bewertung: ✅ belegt sagbar · ⚠️ präzisierungsbedürftig · ⛔ riskant

### A. Live sichtbar (website-copy.js / scout-copy.js / network-copy.js / HTML)

| # | Claim (Wortlaut, gekürzt) | Fundstelle | Bewertung | Begründung |
|---|---|---|---|---|
| 1 | „An introduction is not a guarantee of availability or workmanship. Ask for relevant qualifications, references and a written quote." | assets/website-copy.js, en.process_limits_d | ✅ | Trennt Vermittlung und Gewährleistung sauber. |
| 2 | „Registration does not guarantee jobs or earnings." | website-copy.js, en.tech_expect_d; ähnlich en.web_account_note, en.faq4_a | ✅ | Ehrliches Einkommens-Disclaimer. |
| 3 | „We do not promise a technician in every city or a guaranteed response time." | website-copy.js, en.about_focus_d; ähnlich en.faq2_a | ✅ | Keine Abdeckungs-/SLA-Versprechen. |
| 4 | „Free account · Local relationships · No guaranteed earnings" | assets/scout-copy.js, en.sc_free | ✅ | Sauberes Scout-Disclaimer. |
| 5 | „Never create accounts in somebody else's name or promise jobs, income or verification." | scout-copy.js, en.sc_trust_d | ✅ | Anti-Missbrauchsregel für Scouts, deckt Fake-Accounts und Verifizierungsversprechen ab. |
| 6 | „Attribution is based on the invitation link. It does not verify a technician's qualifications or activity." | scout-copy.js, en.sc_ref_note | ✅ | Trennt Zuordnung und Qualifikation. |
| 7 | „Your own checklist, not verified results." | scout-copy.js, en.sc_week_note | ✅ | Kennzeichnet Selbstauskunft. |
| 8 | „No exclusive territories or guaranteed earnings." | assets/network-copy.js, en.net_guide_limits | ✅ | Sauber; Netzwerk-Freigabe durch Betreiber ist in assets/network.js („must approve your network before you can publish") umgesetzt. |
| 9 | „XP and VIP points are granted according to the published rules and have no cash value." | terms.html §4 | ⚠️ | Inhaltlich sagbar, steht aber in direktem Widerspruch zu den ausgelieferten i18n-Dollar-Claims (#18, #19) — ohne Präzisierung „Punkte ohne Geldwert; etwaige bezahlte Programme werden gesondert schriftlich vereinbart" bleibt der Widerspruch bestehen. |
| 10 | „⚠️ Template — replace placeholders and have the final version reviewed by a legal professional before going live." | terms.html, Fußnote | ⚠️ | Ehrlich, aber die Seite ist öffentlich verlinkt; eine als „Terms of use" ausgegebene Vorlage ohne Rechtsprüfung ist als Vertragsgrundlage ungeeignet. |
| 11 | „Thank you! Your review has been submitted and will be verified." | review.html:70 (data-i18n rv_ok) | ⛔ | Widerspricht dem Datenbankverhalten: reviews sind sofort öffentlich (supabase-setup.sql:180–182); ein Prüfschritt vor Veröffentlichung existiert im sichtbaren Code nicht. Zudem ist „verified" bei einer Bewertung inhaltlich nicht definiert. |
| 12 | Pausen-Platzhalter „This section is not currently published." | rankings.html, members.html (website-copy.js, en.pause_*) | ✅ | Ehrlicher Leerzustand statt erfundener Rankings. |

### B. Live zur Laufzeit gerendert (assets/app.js nutzt Schlüssel aus i18n.js)

| # | Claim (Wortlaut) | Fundstelle | Bewertung | Begründung |
|---|---|---|---|---|
| 13 | „No verified technician in {city} yet? Leave your WhatsApp number and we'll message you the moment one joins." | assets/i18n.js:3, en.wl_desc; gerendert in assets/app.js | ⚠️ | „Verified technician" ist öffentlich nicht definiert (Stufe? Prüfumfang? Datum?). Die DB-Stufen existieren, werden aber nicht kommuniziert. |
| 14 | „Done! We'll WhatsApp you as soon as a verified technician joins {city}." | assets/i18n.js:3, en.wl_ok; app.js | ⚠️ | Wie #13; zusätzlich ein Kommunikationsversprechen ohne dokumentierten Prozess. |
| 15 | „No ranked technicians in {country} yet — be the first and lead your country's Top 20 from day one!" | assets/i18n.js:3, en.rk_empty; app.js | ⚠️ | Ranking-Logik (XP-Sortierung) wird dem Nutzer nicht erklärt; „Top 20" suggeriert Wettbewerbsqualität ohne Datenbasis (VA_DATA ist derzeit ein leerer Stub, assets/data.js:63). |

### C. Dormant, aber in allen 5 Sprachpaketen ausgeliefert (assets/i18n.js, assets/i18n/*.js, je Zeile 3; Kopien in dist/)

| # | Claim (Wortlaut) | Fundstelle | Bewertung | Begründung |
|---|---|---|---|---|
| 16 | „Ranked. Visible. Hired." / „Free for technicians, forever." / „free for technicians — forever. Optional boost features may be offered later." | i18n/en.js:3, en.hero_title, en.hero_lead, en.fq1a | ⚠️ | „Hired" und „forever" sind Versprechen ohne Bedingungsvorbehalt; „forever free" + spätere Boost-Option widersprechen sich leicht. |
| 17 | „Verified technicians" (Statistik-Label) | i18n/en.js:3, en.stat_techs | ⚠️ | Zähler-Label ohne Definition von „verified". |
| 18 | **„$10 base × quality multiplier (0.5–1.5)" / „$25 base …" / „$50 base … + Gold Scout badge" / „$100 base … + HQ newsletter feature"** | **assets/i18n.js:3 und assets/i18n/en.js:3, Schlüssel rw_1, rw_2, rw_3, rw_4** (identisch in fr.js, pt.js, ar.js, zh.js und dist/assets/) | ⛔ | Direkter Widerspruch zu terms.html §4 (Punkte ohne Geldwert). Keine Währungsdefinition hinter „$", keine Anspruchsbedingungen, keine Länderberechtigung, kein Auszahlungsnachweis. |
| 19 | **„VIP points convert into monthly commissions, from $10 up to $100+ and rising with your level."** | **assets/i18n.js:3 und assets/i18n/en.js:3, Schlüssel sg_a1_d** (alle Sprachpakete) | ⛔ | Wie #18; formuliert Punkte→Geld-Umwandlung als Systemversprechen. |
| 20 | „…you bring the best local professionals onto the platform … and get paid for every step of their success." | i18n/en.js:3, en.sg_why_p | ⛔ | Pauschalversprechen Bezahlung „für jeden Schritt"; ohne Vergütungsblatt nicht sagbar. |
| 21 | „browse verified professionals yourself, or describe your project and get matched within 24 hours" | i18n/en.js:3, en.hi_sub | ⛔ | 24-Stunden-SLA ohne Prozessnachweis; widerspricht zudem dem eigenen Live-Disclaimer en.faq2_a („no guaranteed response time") im selben ausgelieferten System. |
| 22 | „✓ Verified profiles & real reviews" / „✓ Ranked by proven, documented work" | i18n/en.js:3, en.hi_trust1, en.hi_trust2 | ⚠️ | „Verified" undefiniert; „proven, documented work" überzeichnet XP-Logik. |
| 23 | „Anti-cheating algorithms and manual quality checks keep it fair." / XP-Tabelle (+10 Projekt, +15 Review, +20 Zertifikat, +25 Vermittlung) | i18n/en.js:3, en.sys_sub, en.fq2a, en.xp_1–4, en.vip_1–4 | ⚠️ | XP-Ereignisse sind als Backend-Tabellen angelegt (xp_events, vip_events, supabase-setup.sql:269 ff.) — teils belegt. „Anti-cheating algorithms" sind im sichtbaren Code nicht nachweisbar; manuelle Prüfung ist für verifications vorgesehen, aber kein dokumentierter Betriebsprozess. |
| 24 | „Share your verified profile … see your verified profile, projects and reviews." | i18n/en.js:3, en.pf_share_t/d | ⚠️ | Profil pauschal „verified" ohne Stufenangabe. |
| 25 | „the best verified professionals in your area" / „Find verified solar, electrical, network & IT pros" / „Find verified local partners in 54 countries" / „a verified technician will give you an exact quote" | i18n/en.js:3, en.rq_sub, en.hero_client_d, en.vid_3_d, en.calc_note | ⚠️ | Wiederholter undefinierter „verified"-Begriff auf 7+ Schlüsseln; „best" und „exact quote" verstärken die Überzeichnung. |
| 26 | „Your rank: #5 of 47 scouts (Africa)" | i18n/en.js:3, en.ds_rank | ⚠️ | Sieht wie echte Rangdaten aus, ist ein harter Beispielwert; bei Reaktivierung Verwechslungsgefahr Demo/Ist. |
| 27 | „Example view — rankings go live with the first verified technicians." | i18n/en.js:3, en.updated | ✅ | Ehrliche Kennzeichnung als Beispielansicht. |

**Summe: 27 Claims — 11 ✅ sagbar, 11 ⚠️ präzisierungsbedürftig, 5 ⛔ riskant (#11, #18, #19, #20, #21).**

## Ersatztexte (Englisch, zur Betreiberfreigabe)

### E1 — „Verified" als Stufensystem (ersetzt alle pauschalen verified-Claims #13, #14, #17, #22, #24, #25)

Abbildung auf das vorhandene Datenbankmodell (verifications.level 1–4). Öffentlich nur das Label der höchsten bestätigten Stufe zeigen; nie „verified" ohne Stufe:

> **Trust levels on Voltage Africa.** Profiles can carry up to four checked badges, each approved manually by our team:
> **Identity confirmed** — we checked the person's identity document against the profile.
> **Work proof reviewed** — we reviewed documented project evidence (photos, descriptions, client confirmation).
> **Reference checked** — we contacted at least one reference provided by the technician.
> **Licence on file** — the technician submitted a professional licence relevant to their trade and country; we checked the document, not the underlying authority's register in real time.
> A badge confirms only what its level states. It is not a guarantee of work quality, availability or pricing — always ask for a written quote and references before hiring.

Waitlist-Ersatz (wl_desc / wl_ok):

> „No technician with a checked badge in {city} yet — leave your WhatsApp number and we will message you when one joins." / „Done! We will WhatsApp you when a technician with a checked badge joins {city}."

### E2 — Review-Bestätigung ehrlich (ersetzt rv_ok, #11)

Reviews sind technisch sofort sichtbar; der Text muss das abbilden:

> „Thank you! Your review is now published and linked to this project request. Voltage Africa checks reported reviews and removes entries that break our rules."

Alternativ, falls ein Pre-Moderations-Schritt eingebaut wird (empfohlen, siehe Vertrauens-Architektur): „Thank you! Your review has been submitted. It will appear on the profile after a moderation check — usually within 2 working days."

### E3 — Ranking ehrlich erklärt (ersetzt rk_empty, hi_trust2, rank_bezogene Claims #15, #22, #23)

> **How rankings work.** Rankings order profiles by XP. Technicians earn XP for documented projects, published customer reviews, submitted certificates and confirmed placements. XP measures platform activity and documentation — it does not certify professional qualifications and does not guarantee work quality. Check the trust badges and ask for references before you decide.

Leerzustand: „No ranked technicians in {country} yet. Rankings start as soon as the first technicians earn XP — the list never includes everyone, only registered members."

### E4 — Scout-Formulierung ohne Geldwert (ersetzt rw_1–rw_4, sg_a1_d, sg_why_p — #18, #19, #20; anzugleichen mit terms.html §4)

> **Scout recognition.** Scouts earn VIP points for building their local network: activating technicians who complete real profiles, keeping their team active, and supporting confirmed placements. VIP points recognise your contribution and unlock levels and badges — **they have no cash value**. If Voltage Africa offers a paid scout programme in your country, participation, amounts and payment conditions are set out in a separate written agreement. Points alone never create a payment claim.

Ersetzt die $-Tabelle rw_1–rw_4 durch nicht-monetäre Stufen:

> 200+ VIP — „Active District badge" · 500+ VIP — „City Lead badge" · 1.000+ VIP — „Gold Scout badge" · 2.500+ VIP — „Featured in the HQ newsletter"

### E5 — Matching ohne SLA (ersetzt hi_sub, #21)

> „Two ways to hire: browse member profiles yourself, or describe your project and we will check the local network for a suitable match. There is no guaranteed response time — availability depends on your location and trade."

### E6 — Hero/Statistik präzisiert (ersetzt hero_title, hero_lead, stat_techs, fq1a — #16, #17)

> Hero: „Africa's technicians. Documented work. Real reviews. Direct contact."
> Lead: „The platform for electricians, solar installers, network & IT professionals across Africa. Show your projects, collect reviews, and get found by companies. Creating a technician profile is free."
> Statistik-Label: „Technicians with checked badges" (statt „Verified technicians").
> fq1a: „Creating a profile, posting projects, collecting reviews and appearing in the rankings is free for technicians. Optional paid features may be offered later; any change will be announced on this page."

### E7 — Demo-Rang kennzeichnen (ersetzt ds_rank, #26)

> „Example: your rank will appear here once scout rankings go live."

## Vertrauens-Architektur: Missbrauchsrisiken und Gegenmaßnahmen (mit vorhandenem Supabase-Setup machbar)

Das Schema (supabase-setup.sql) enthält bereits gute Fundamente: Reviews sind an eine echte Anfrage gebunden (request_id, unique — eine Bewertung pro Auftrag), Projekte werden erst nach Bestätigung durch client/scout öffentlich (`confirmed_by`), Verifizierungen sind submission-only mit Owner-Freigabe (kein Client-Update, kein Self-Approve), Vouches kennen die Stati active/revoked/clawback. Darauf aufbauend:

### Risiko 1: Fake-Bewertungen (Techniker lässt sich selbst bewerten / Bewertungskauf)

- **Heute offen:** Anonymer Insert mit beliebiger gültiger request_id reicht (Policy `reviews_public_insert`); Reviews sind sofort öffentlich; das verified-Flag ist wirkungslos.
- **Gegenmaßnahmen:** (a) Pre-Moderation: Reviews standardmäßig auf `verified = false` lassen und öffentliche Anzeige/Zählung auf `verified = true` beschränken (View analog zu verifications_public). (b) Review-Link nur an die anfragende E-Mail/WhatsApp der request senden — review.html kennt den „invalid or already used"-Zustand bereits; sicherstellen, dass die request_id nicht ratbar ist (UUID ✅). (c) Dubletten-/Musterprüfung als Betreiber-Query: gleicher reviewer_name über viele tech_ids, gehäufte 5-Sterne-Reviews in <24 h, Review ohne Kontaktaufnahme in messages. (d) „Report review"-Kontakt auf dem Profil; gemeldete Reviews in Prüfqueue. (e) Keine automatische Sperre aus Mustern — Verdacht → Belegprüfung → Entscheidung mit Einspruchsweg.

### Risiko 2: Vouch-Ringe (Scouts stärken sich gegenseitig / vouchen ohne Kenntnis)

- **Heute:** Tabelle vouches vorhanden, Zählung über View vouch_counts; keine öffentliche Erklärung, was ein Vouch bedeutet.
- **Gegenmaßnahmen:** (a) Vouch öffentlich definieren: „A scout stakes part of their VIP standing on this technician; vouches are withdrawn (clawback) if the technician is found to misuse the platform." (b) Max. aktive Vouches pro Scout (z. B. 10) — erzwingt Knappheit. (c) Gegenseitigkeits-Check in der Betreiber-Query: A→B und B→A, Cluster gleicher Stadt ohne Placement-Historie. (d) Clawback durchsetzen und auf dem Scout-Profil sichtbar machen. (e) Vouches nie als Qualifikationsnachweis labeln — nur als Netzwerk-Signal.

### Risiko 3: Scout-Spam und Scheinaktivierungen (Masseneinladungen, Profile in fremdem Namen)

- **Heute gute Basis:** sc_trust_d verbietet Fremd-Accounts und Versprechen; VIP-Aktivierung (vip_1) erfordert vollständiges Profil + erstes Projekt + erste verifizierte Review — Scheinaccounts bringen also keine Punkte; Netzwerk-Seiten starten als Draft mit Betreiber-Freigabe (network.js).
- **Gegenmaßnahmen:** (a) Einladungslinks mit Rate-Limit pro Scout/Tag. (b) Punkte erst nach unabhängig bestätigter Aktivität gutschreiben (bestehende vip_1-Logik beibehalten und kommunizieren). (c) Wiederholte unerwünschte Nachrichten: Opt-out-Hinweis in Einladungstexten (besteht teilweise), Beschwerdeweg an info@voltage-africa.com. (d) Scout-Accounts bei nachgewiesenem Spam: Punkte-Korrektur gemäß terms.html §4, dann Sperre — dokumentiert und mit Einspruch.

### Risiko 4: XP-/Ranking-Manipulation

- **Gegenmaßnahmen:** (a) XP nur aus Backend-Ereignissen (xp_events), keine Client-Inserts — im Schema so angelegt, beibehalten. (b) Monatliche Betreiber-Plausibilitätsabfrage: Top-20 je Land auf fehlende bestätigte Projekte, auffällige XP-Sprünge. (c) terms.html §4 (Korrekturrecht) durch die E3-Ranking-Erklärung ergänzen, damit Nutzer die Logik kennen. (d) „Anti-cheating algorithms" (sys_sub) erst wieder behaupten, wenn mindestens die Abfragen (b) dokumentiert laufen — bis dahin: „manual quality checks".

## Review-Prozess: Betreiber-Workflow für manuelle Verifizierungs-Freigaben

Grundlage: Tabelle verifications (level 1–4, status pending/approved/rejected, evidence_url privat, verified_by, created_at; öffentliche Sicht nur über View verifications_public mit tech_id/level/status). Kein Client-seitiges Approve möglich — Freigabe erfolgt durch Betreiber (Service Role/SQL Editor).

### Checkliste je Stufe

| Stufe | Label (öffentlich, E1) | Prüfumfang | Mindestbelege |
|---|---|---|---|
| 1 | Identity confirmed | Identitätsdokument gegen Profilname/Foto; Plausibilität Land/Stadt | Dokument lesbar, Name stimmt überein, Foto kohärent |
| 2 | Work proof reviewed | Projektfotos/-beschreibungen auf Plausibilität; Kundenbestätigung (projects.confirmed_by) | ≥1 Projekt mit confirmed_by client/scout; keine offensichtlichen Stock-Fotos (Rückwärtssuche stichprobenartig) |
| 3 | Reference checked | Mindestens eine vom Techniker genannte Referenz tatsächlich kontaktiert; kurzes Protokoll (Datum, Kanal, Kernaussage) | Referenz bestätigt Zusammenarbeit und Gewerk |
| 4 | Licence on file | Eingereichte Lizenz auf Gewerk/Land/Gültigkeit prüfen; Dokument, nicht das Register in Echtzeit | Lizenzdokument mit Nummer, Aussteller, Gültigkeitsdatum |

### Ablauf und SLAs

1. **Eingang:** Techniker reicht ein (status pending). Warteschlange nach created_at, älteste zuerst. **Erstprüfung ≤ 5 Werktage.**
2. **Prüfung:** Checkliste der beantragten Stufe; bei Stufe 3–4 Vier-Augen-Prinzip (zweite betriebseigene Person oder dokumentierte Selbstkontrolle mit Begründung, solange Ein-Personen-Betrieb).
3. **Entscheidung:** approved (verified_by + Datum setzen) oder rejected mit Grund aus Katalog: *Dokument unleserlich / Name weicht ab / Beleg nicht nachvollziehbar / Referenz nicht erreichbar nach 2 Versuchen in 10 Werktagen / Dokument abgelaufen / Verdacht auf Fälschung*.
4. **Kommunikation:** Ablehnung mit Grund und Hinweis auf Nachreichung; **Einspruch innerhalb von 14 Tagen**, Bearbeitung ≤ 5 Werktage.
5. **Wiederholprüfung:** Stufe 4 bei Dokumentablauf; Stufe 1–3 Stichprobe 10 %/Quartal oder bei konkretem Hinweis. Widerruf (neuer Status oder Löschung aus View) bei nachgewiesenem Missbrauch — vorher Anhörung.
6. **Protokoll:** Jede Entscheidung mit Prüfer (verified_by), Datum, Stufe und Grund — intern, keine personenbezogenen Belege ins Marketing-Repository.

### Review-Moderation (analog, falls E2-Pre-Moderation umgesetzt)

Tägliche Queue neuer Reviews; Freigabe binnen 2 Werktagen; Entfernungsgründe: kein Bezug zum Auftrag, Beleidigung, erkennbarer Interessenkonflikt, Dublette. Entscheidung dokumentiert, Einspruchsweg wie oben.

## Drei nächste Maßnahmen

1. **P1 — Dollar-Versprechen entfernen oder belegen.** rw_1–rw_4, sg_a1_d und sg_why_p in allen fünf Sprachpaketen (assets/i18n.js, assets/i18n/{en,fr,pt,ar,zh}.js) durch E4 ersetzen und dist/ neu erzeugen; alternativ ein schriftliches Vergütungsblatt (Länder, Währung, Zeitraum, Bedingungen, Auszahlung) beschließen und terms.html §4 präzisieren („no cash value; paid programmes only under separate written terms"). Bis dahin dürfen die Archiv-Versionen (Files_mit_zip/, Voltage_Africa_Deploy_zip/) nicht erneut deployed werden.
2. **P1 — „Verified" durch das Stufensystem E1 ersetzen und rv_ok korrigieren.** Alle pauschalen verified-Claims (wl_desc, wl_ok, stat_techs, hi_trust1/2, pf_share_*, rq_sub, hero_client_d, calc_note u. a.) auf Badge-Labels umstellen; review.html rv_ok durch E2 ersetzen — entweder ehrlich zur Sofort-Veröffentlichung oder Pre-Moderation gemäß Review-Prozess einbauen (View auf verified = true). 24-Stunden-SLA (hi_sub) durch E5 ersetzen.
3. **P2 — Betreiber-Review-Prozess dokumentiert in Betrieb nehmen.** Checklisten, Ablehnungskatalog und SLAs aus diesem Bericht als interne Arbeitsanweisung übernehmen; erste Plausibilitätsabfragen für Reviews/XP/Vouches als gespeicherte SQL-Abfragen anlegen; terms.html-Vorlagenwarnung durch rechtsgeprüfte Fassung ersetzen. Erst wenn 1–3 monatlich nachweisbar laufen, dürfen Claims wie „manual quality checks" wieder unqualifiziert beworben werden.

---
*Erstellt von Vertrauen_Lead am 2026-09-21. Alle Fundstellen beziehen sich auf den lokalen Website-Stand; keine Live-Prüfung, keine Backend-Ausführung, keine Rechtsberatung. Ersatztexte E1–E7 sind Freigabevorschläge an den Betreiber.*
