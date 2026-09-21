# Growth-Experimente-Backlog für Voltage Africa

**Rolle:** Growth_Hacker (Marktplatz-Experimente) · **Datum:** 2026-09-21 · **Sprache:** Deutsch (intern)

**Datengrundlage:** Website-Kontext (lokal beobachteter Code: request.html, signup.html, rankings.html, members.html, calculators.html, Supabase-Backend), KPI-Framework vom 2026-09-21 (SQL-Skizzen gegen das Schema, **keine Ist-Zahlen**), Länder-Priorisierung vom 2026-09-21 (Quellen abgerufen 2026-09-21). Alle ICE-Scores und Uplift-Erwartungen sind **Hypothesen**, keine Messungen. Es existiert heute **kein Besucher-Tracking** (Lücke L1 im KPI-Framework) — Experimente, die Website-Conversion messen wollen, setzen die dort beschriebene Minimal-Lösung (`page_events` oder Plausible/Umami) oder manuelle Zählung voraus.

---

## 1. Zusammenfassung

Voltage Africa steht im klassischen Cold-Start eines zweiseitigen Marktplatzes: Ohne verfügbare Techniker ist jede Kundenanfrage ein enttäuschtes Versprechen („Instant Matching" ohne Angebot), und ohne Anfragen ist jeder geworbene Techniker nach zwei Wochen inaktiv. Das KPI-Framework bestätigt die Priorität indirekt: Die Frühwarnung bei KPI 2 (`match_rate_pct < 50 %` = „Angebotsseite dünn") wird in der Frühphase fast überall anschlagen.

Konsequenz für diesen Backlog:

1. **Angebotsseite zuerst.** 6 von 10 Experimenten zielen auf Techniker-/Scout-Rekrutierung und -Aktivierung. Dabei kommt der **Single-Player-Mode** (sichtbarer Rang, XP, Verifikationsbadge, belegte Projekte) zum Zug: Ein Techniker kann auf Voltage Africa schon Wert aufbauen, *bevor* der erste Auftrag hereinkommt — das öffentliche Ranking wird zum Motivator und zum Selbstmarketing-Werkzeug („Ich bin #3 in Lagos Solar").
2. **WhatsApp ist der Trichter.** Mit 92–98 % WhatsApp-Reichweite unter Internetnutzern in den Tier-1-Märkten (Länder-Bericht, Sekundärquelle mittlerer Güte) ist jeder Flow, der ein Webformular ohne WhatsApp-Handoff enden lässt, verschenkte Conversion. Vier Experimente bauen konsequent auf `wa.me`-Deep-Links.
3. **Kleine Stichproben, qualitative Entscheide.** Bei wenig Traffic ist kein A/B-Test statistisch belastbar. Jede Experimentkarte nennt daher neben der Erfolgsmetrik auch die Entscheidungslogik für kleine n (gemäß Skill voltage-growth: Baseline, Laufzeit und Entscheidungskriterium vorher festlegen, Unsicherheit benennen).
4. **Keine Wachstumskäufe gegen Vertrauen.** Kein Experiment darf Verifikationshürden senken, Bewertungen kaufen oder XP inflationieren — Vertrauen ist laut Länder-Bericht die dokumentierte Marktlücke und damit das Kernversprechen.

**Top-3 nach ICE:** E1 (Öffentliches Stadt-Ranking als Rekrutierungsanker), E3 (WhatsApp-Handoff nach request.html-Submit), E6 (Referral-Link + vorbefüllte WhatsApp-Teilen-Nachricht).

---

## 2. Experiment-Backlog (Übersichtstabelle)

ICE = Impact / Confidence / Ease, je 1–10. Score = Mittelwert. Sortiert nach Score.

| # | Experiment | Thema | I | C | E | ICE | Erfolgsmetrik (KPI-Framework) | Mindestlaufzeit |
|---|---|---|---|---|---|---|---|---|
| E1 | Öffentliches Stadt-Ranking als Rekrutierungsanker | Angebot / Single-Player | 8 | 7 | 8 | **7,7** | KPI 8 (Registrierungen), KPI 9 (Aktivierung) | 4 Wochen |
| E3 | WhatsApp-Handoff nach Anfrage-Submit | Anfrage-Conversion | 8 | 7 | 7 | **7,3** | KPI 2 (Match-Quote), Antwortzeit | 2 Wochen |
| E6 | Persönlicher Referral-Link + WhatsApp-Teilen | Referral-Viralität | 7 | 7 | 8 | **7,3** | KPI 14 (`referred_share_pct`), K-Faktor | 4 Wochen |
| E5 | „Erstes Match in 7 Tagen" (Concierge-Onboarding) | Angebot / Aktivierung | 8 | 6 | 7 | **7,0** | KPI 9, 7-Tage-Aktivität | 4 Wochen |
| E2 | WhatsApp-first Techniker-Onboarding | Angebot / Rekrutierung | 8 | 6 | 7 | **7,0** | KPI 8→9-Kohortenconversion | 3 Wochen |
| E8 | Review-Loop per WhatsApp nach Abschluss | Nachfrage / Belege | 7 | 7 | 6 | **6,7** | KPI 6 (Bewertungsquote), KPI 5 (BCV) | 4 Wochen |
| E4 | request.html in 2 Schritte (Kontakt zuerst) | Anfrage-Conversion | 6 | 6 | 7 | **6,3** | KPI 1 (Anfragen/Woche), Form-Abbruch (nach L1) | 3 Wochen |
| E7 | Scout-Rekrutierung über Elektro-Großhandel | Angebot / Offline-Kanal | 7 | 5 | 6 | **6,0** | KPI 13 (aktive Vouches), KPI 8 | 6 Wochen |
| E9 | Stadt-Landingpage + Gruppen-Seeding mit UTM | Nachfrage / Kanäle | 6 | 5 | 7 | **6,0** | KPI 1 je Stadt, UTM-Anteil | 4 Wochen |
| E10 | Calculator als teilbarer Lead-Magnet | Nachfrage / Viralität | 5 | 5 | 6 | **5,3** | KPI 1 (Anfragen aus Calculator-UTM) | 4 Wochen |

---

## 3. Experiment-Details

### E1 — Öffentliches Stadt-Ranking als Rekrutierungsanker
- **Hypothese:** Techniker in Lagos/Nairobi melden sich eher an, wenn sie ein konkretes, öffentlich sichtbares Ziel haben („Top 10 Elektriker Lagos"), weil der Rang als Vertrauensnachweis gegenüber eigenen Kunden nutzbar ist — auch ohne dass die Plattform schon Aufträge liefert (Single-Player-Mode).
- **Setup:** rankings.html um eine stadtscharfe Ansicht ergänzen (Ranking wird aus vorhandenen XP/Verifikations-/Projektdaten gespeist — statische Seite liest öffentliche, aggregierte Supabase-Daten; **vorher prüfen**, welche Policies öffentliche SELECTs zulassen). Rekrutierungsnachricht in Direktansprache: „Trag dich ein, vervollständige dein Profil, werde in Lagos sichtbar." Messung: KPI 8 (neue Techniker-Registrierungen/Woche, Segment Stadt) und KPI 9 (Profil-Aktivierung innerhalb 7 Tage) vor/nach Launch; zusätzlich qualitativ: Antwortquote auf Outreach-Nachrichten mit vs. ohne Ranking-Verweis (manuell in einer einfachen Tabelle erfassen).
- **Begründung ICE:** Impact 8 (adressiert den Kern-Flaschenhals und schafft dauerhaftes Asset), Confidence 7 (Gamification als Rekrutierungshebel ist plausibel, aber lokale Wirkung unbewiesen), Ease 8 (rankings.html existiert bereits; reine Darstellung + Outreach-Text).
- **Erfolgskriterium (kleines n):** ≥ 2× wöchentliche Registrierungen gegenüber 2-wöchiger Baseline **und** ≥ 50 % Profil-Aktivierung der Neuzugänge; bei n < 10/Woche nur Richtungsentscheid + Interviews.
- **Mindestlaufzeit:** 4 Wochen.
- **Risiko:** Bei sehr dünner Basis zeigt das Ranking leere oder halb leere Listen → Vertrauensschaden statt Anreiz. **Mitigation:** Ranking erst ab ≥ 10 Profilen pro Stadt × Gewerk öffentlich schalten, darunter „Werde einer der ersten 10 verifizierten Elektriker in Lagos" als Waitlist-Framing. Keine künstlichen Profile, keine XP-Manipulation (verboten gemäß voltage-growth).

### E2 — WhatsApp-first Techniker-Onboarding
- **Hypothese:** Ein Anmeldeflow, der auf „Schreib uns auf WhatsApp" statt auf ein Webformular setzt, konvertiert kalte Techniker-Kontakte besser, weil er deren Gewohnheit trifft und sofort menschliche Betreuung signalisiert.
- **Setup:** Auf hire.html/signup.html (Techniker-Seite) primären CTA auf `wa.me`-Link mit vorbefüllter Nachricht („Hallo, ich bin Elektriker in Lagos und möchte bei Voltage Africa mitmachen. Gewerk: ___, Stadtteil: ___") umstellen; Formular bleibt als Sekundär-CTA. Ops legt das Profil im Gespräch an oder führt durch signup.html (Concierge). Messung: Kohortenvergleich Registrierungen→Profil-Aktivierung (KPI 8/9-SQL), Kanal-Attribution über kurze Ops-Tabelle (Quelle: WA vs. Formular).
- **Begründung ICE:** Impact 8 (oberster Trichter des Engpasses), Confidence 6 (WhatsApp-Affinität belegt, aber Flow-Wechsel kann auch Formular-Conversions kannibalisieren — Gesamtsumme zählt), Ease 7 (reine Frontend-/CTA-Änderung).
- **Erfolgskriterium:** Gesamt-Registrierungen (WA + Formular) ≥ 1,5× Baseline; WA-Kanal-Aktivierung ≥ Formular-Aktivierung.
- **Mindestlaufzeit:** 3 Wochen.
- **Risiko:** Ops-Last wächst manuell; ohne schnelle Antwort (< 1 h zu Arbeitszeiten) kippt der Effekt ins Negative. **Mitigation:** Antwort-SLA festlegen, Textbausteine; bei > 10 Chats/Tag Flow teilautomatisieren (WhatsApp-Business-Away-/Quick-Replies).

### E3 — WhatsApp-Handoff nach Anfrage-Submit (request.html)
- **Hypothese:** Ein sofortiger `wa.me`-Deep-Link nach dem Absenden der Anfrage („Deine Anfrage ist eingegangen — tippe hier, um sie direkt an unser Matching-Team zu senden") erhöht die Zahl tatsächlich bearbeitbarer Anfragen und verkürzt die Zeit bis zum ersten Match, weil der Kunde im warmen Moment den Kontakt bestätigt und Zusatzinfos (Foto, Adresse) nachreicht.
- **Setup:** Erfolgsseite/Bestätigungszustand von request.html um Button „Per WhatsApp bestätigen" ergänzen; Link enthält Request-Kurzdaten als Text (keine personenbezogenen Daten in der URL über das hinaus, was der Kunde selbst tippt — Datensparsamkeit prüfen). Messung: KPI 2 (Match-Quote innerhalb 72 h) und `hours_to_first_match` aus dem KPI-Framework, Kohorten vor/nach; Ops markiert Requests mit WA-Kontaktaufnahme.
- **Begründung ICE:** Impact 8 (direkt am Kernversprechen „Instant Matching"), Confidence 7 (Handoff-Mechanik standarderprobt im Marktumfeld), Ease 7 (statische Erfolgsseite + Link-Template; kein Backend-Eingriff nötig).
- **Erfolgskriterium:** Median-Zeit bis erstes Match sinkt unter 24 h in der Test-Stadt; Match-Quote +15 Prozentpunkte gegenüber Baseline-Kohorte (bei kleinem n: Richtungsentscheid + 5 Kunden-Kurzinterviews).
- **Mindestlaufzeit:** 2 Wochen.
- **Risiko:** Doppelte Vorgänge (DB-Insert + WA-Nachricht) erschweren Deduplizierung. **Mitigation:** WA-Text enthält Request-ID; Ops-Matching-Regel dokumentieren.

### E4 — request.html in 2 Schritte (Kontakt zuerst)
- **Hypothese:** Die Anfrage-Conversion steigt, wenn zuerst nur Kontakt + Gewerk + Stadt abgefragt werden und alle Detailfragen in Schritt 2 (oder im WhatsApp-Handoff) folgen — weniger sichtbare Formularlänge, weniger Abbruch.
- **Setup:** Formular in zwei Schritte aufteilen (Frontend-only; Insert erfolgt weiterhin einmalig nach Schritt 2; Abbruch nach Schritt 1 erzeugt **keinen** DB-Eintrag, sondern wird — sobald L1-Tracking beschlossen ist — als Event gezählt; bis dahin manuelle Stichprobe). Messung: KPI 1 (Anfragen/Woche) vor/nach; nach Verfügbarkeit von `page_events`: Start→Submit-Rate je Variante. Vorher festlegen: Mindest-Vollständigkeit für „gültige Anfrage" (N3) darf nicht sinken.
- **Begründung ICE:** Impact 6, Confidence 6 (Formular-Friction ist ein Standardhebel, aber ohne Besucher-Tracking ist die Wirkung nur über Endwerte sichtbar), Ease 7.
- **Erfolgskriterium:** Anfragen/Woche +25 % gegenüber 2-Wochen-Baseline bei gleichbleibender gültiger-Kontakt-Quote.
- **Mindestlaufzeit:** 3 Wochen (wegen kleiner n).
- **Risiko:** Mehr Schrottanfragen (ungerade Kontakte). **Mitigation:** E.164-Validierung beibehalten; Spam-/Validitäts-Flag (L7) mitdenken, sonst misst das Experiment Rauschen.

### E5 — „Erstes Match in 7 Tagen" (Concierge-Onboarding)
- **Hypothese:** Neue Techniker bleiben aktiv, wenn sie innerhalb von 7 Tagen nach vollständigem Profil mindestens ein konkretes Match-Angebot sehen — das erste sichtbare „Geld-Signal" ist der stärkste Retention-Moment in der Cold-Start-Phase.
- **Setup:** Ops-Prozess, kein Feature: Jeder neue Techniker (Rolle `tech`, Profil vollständig) kommt auf eine 7-Tage-Prioritätenliste; eingehende passende Requests werden ihm bevorzugt manuell zugespielt (Insert in `matches` mit Status `offered`); wenn kein organischer Request passt, wird ein realer Auftrag aus dem Ops-Netzwerk vermittelt (kein Fake-Request). Messung: KPI 9 (Aktivierung), Anteil Neuzugänge mit ≥ 1 `matches`-Zeile ≤ 7 Tage, 30-Tage-Aktivität (sobald `last_seen_at`/L5 vorhanden; bis dahin qualitativ über WA-Kontakt).
- **Begründung ICE:** Impact 8 (wirkt auf Retention der knappen Seite), Confidence 6 (offensichtlich richtig, aber begrenzt skalierbar — bewusst als Lern-Experiment), Ease 7 (reine Ops-Disziplin + SQL).
- **Erfolgskriterium:** ≥ 80 % der neuen aktivierten Techniker erhalten ≤ 7 Tage ein Match-Angebot; qualitativ: ≥ 5 Kurzinterviews, ob das Match-Angebot der Aktivierungsgrund war.
- **Mindestlaufzeit:** 4 Wochen.
- **Risiko:** Versprechen ohne Nachfrage erzeugt Enttäuschung. **Mitigation:** Nur kommunizieren, solange Ops die Quote halten kann; sonst als internen Prozess ohne externes Versprechen fahren.

### E6 — Persönlicher Referral-Link + vorbefüllte WhatsApp-Teilen-Nachricht
- **Hypothese:** Der vorhandene +25-XP-Referral-Anreiz wirkt erst, wenn das Teilen ein einzelner Tipp ist: persönlicher Link im Profil plus vorbefüllte WhatsApp-Nachricht. Das erhöht den Anteil geworbener Techniker an Neuanmeldungen (K-Faktor-Baustein).
- **Setup:** Profil-/Dashboard-Bereich um „Empfehlen"-Block ergänzen: persönlicher Referral-Link (vorhandene `referrals`-Struktur nutzen; Zuordnung `referrer_id` → `referred_id` bei Registrierung sicherstellen) und Teilen-Button `https://wa.me/?text=<vorbefüllte Nachricht + Link>` in EN (+ FR/PT-Varianten für spätere Märkte). Messung: KPI 14 (`referred_share_pct`, aktive Referrer/Woche); K-Faktor-Näherung: geworbene aktivierte Techniker ÷ aktive Referrer.
- **Begründung ICE:** Impact 7 (einziger struktureller Wachstums-Loop, der ohne Budget skaliert), Confidence 7 (Anreiz existiert, nur die Reibung fehlt), Ease 8 (Frontend + bestehende Tabelle).
- **Erfolgskriterium:** `referred_share_pct` ≥ 20 % der Techniker-Neuanmeldungen nach 4 Wochen; ≥ 30 % der aktivierten Techniker teilen mindestens einmal.
- **Mindestlaufzeit:** 4 Wochen.
- **Risiko:** XP-Farming durch Scheinregistrierungen. **Mitigation:** Referral-Bonus erst bei **Aktivierung** des Geworbenen gutschreiben (Profil vollständig + Verifikation Level 1), nicht bei bloßer Registrierung — das ist eine Anreiz-Design-Entscheidung, die vor Launch mit dem Team festzulegen ist; XP-Betrug manuell stichprobenartig prüfen. Keine XP-Inflation: Bonus-Höhe unverändert lassen.

### E7 — Scout-Rekrutierung über Elektro-Großhandel und Werkzeugläden
- **Hypothese:** In Lagos/Nairobi sind Elektro-Großhändler und Werkzeugläden die physischen Knotenpunkte, an denen sich Techniker täglich treffen; ein dort angesiedelter Scout (Inhaber/Verkäufer mit QR-Flyer und VIP-Anreiz) rekrutiert günstiger und vertrauenswirksamer als jede Online-Anzeige.
- **Setup:** 5–10 Großhändler pro Stadt ansprechen (persönlich/WhatsApp); Scout-Vertrag nach vorhandenem Scout-/Vouch-Modell; QR-Flyer führt auf eine UTM-markierte Anmeldeseite (EN). Messung: KPI 13 (aktive Vouches je Scout), KPI 8 mit UTM-Quelle; Kosten je aktiviertem Techniker (Druck + Airtime-Incentive).
- **Begründung ICE:** Impact 7 (Zugang zu offline erreichbaren, erfahrenen Technikern — genau die, die online nicht hängen), Confidence 5 (Kanal ist Hypothese, Händler-Bereitschaft unbekannt), Ease 6 (Vertriebsarbeit, kein Code).
- **Erfolgskriterium:** ≥ 3 aktive Scouts mit je ≥ 3 geworbenen Technikern in 6 Wochen; Kosten ≤ 10 $ je aktiviertem Techniker.
- **Mindestlaufzeit:** 6 Wochen.
- **Risiko:** Scout-Qualität (geworbene Techniker ohne taugliche Qualifikation → Vouch-Rückbuchungen). **Mitigation:** Frühwarnung aus KPI 13 (clawback/revoked > 20 %) beachten; Pilot nur mit 1–2 Händlern starten.

### E8 — Review-Loop per WhatsApp nach Abschluss
- **Hypothese:** Ein persönlicher WhatsApp-Review-Link 24–48 h nach Auftragsabschluss hebt die Bewertungsquote so weit, dass der Nordstern „bestätigte Vermittlungen" überhaupt belastbar messbar wird — und jede verifizierte Bewertung stärkt das Ranking (Rückkopplung mit E1).
- **Setup:** Ops-Prozess: Bei `requests.status = 'completed'` erhält der Kunde (Kontakt liegt in `requests.contact` vor) eine WA-Nachricht mit Direktlink auf review.html (Request-Bezug). Keine Belohnung für positive Bewertungen, keine Bewertungsvorgaben (Vertrauensregeln). Messung: KPI 6 (Reviews ÷ completed; Anteil `verified`), KPI 5 (completed_with_review).
- **Begründung ICE:** Impact 7 (macht Nordstern messbar und erzeugt Social Proof), Confidence 7 (Anfrage im richtigen Moment ist bewährte Mechanik), Ease 6 (Ops-Prozess + Link-Template).
- **Erfolgskriterium:** Bewertungsquote ≥ 60 % der abgeschlossenen Aufträge in der Test-Stadt.
- **Mindestlaufzeit:** 4 Wochen.
- **Risiko:** Kunden fühlen sich bedrängt; negative Bewertungen häufen sich sichtbar (das ist erwünscht — ehrliches Signal). **Mitigation:** Genau eine Nachricht + eine Erinnerung nach 72 h, dann Stopp.

### E9 — Stadt-Landingpage + organisches Gruppen-Seeding mit UTM
- **Hypothese:** Fokussierte organische Präsenz in den richtigen Facebook-/WhatsApp-Gruppen (Solar Nigeria, Elektriker-Netzwerke, Facility-Manager-Gruppen) mit stadtscharfer Landingpage erzeugt messbare erste Nachfrage in Lagos und Nairobi — ohne Werbebudget.
- **Setup:** Vorhandene Stadt-/Gewerkeseiten als Ziel nutzen; UTM-Links pro Gruppe (`?utm_source=fb_group&utm_campaign=lagos_solar_w01`); Posting-Rhythmus: 2–3 Gruppen × 2 Beiträge/Woche, nutzenorientiert (kein Spam: Gruppenregeln lesen, Mehrwert-Posts, z. B. Calculator-Verlinkung). Messung: KPI 1 nach Stadt; sobald L1-Tracking steht: UTM-Aufschlüsselung; bis dahin Ops-Feld „Wie gefunden?" im Anfrage-Handoff.
- **Begründung ICE:** Impact 6, Confidence 5 (organische Gruppen-Reichweite schwankt stark, Sperr-Risiko), Ease 7.
- **Erfolgskriterium:** ≥ 5 zuschreibbare Anfragen/Woche aus Seeding nach 4 Wochen.
- **Mindestlaufzeit:** 4 Wochen.
- **Risiko:** Gruppen-Bans bei werblichem Auftreten. **Mitigation:** Helfer-Positionierung, persönliches Profil statt Marken-Spam, max. 2 Beiträge/Gruppe/Woche.

### E10 — Calculator als teilbarer Lead-Magnet
- **Hypothese:** Die vorhandenen Rechner (z. B. Solar-Dimensionierung) sind teilbarer Nutzen: Ergebnis-Seite mit „Diese Auslegung von einem geprüften Installateur prüfen lassen"-CTA erzeugt qualifizierte Anfragen und WhatsApp-Shares auf der Nachfrageseite.
- **Setup:** calculators.html-Ergebnis um CTA „Kostenlose Einschätzung per WhatsApp" (wa.me-Link mit Ergebnis-Parametern im Text) und Teilen-Button ergänzen. Messung: KPI 1 mit UTM `utm_source=calculator`; Share-Events nach L1-Tracking.
- **Begründung ICE:** Impact 5, Confidence 5 (abhängig von Rechner-Qualität und Nachfrage-SEO, beides unbewiesen), Ease 6.
- **Erfolgskriterium:** ≥ 3 Anfragen/Woche über Calculator-UTM nach 4 Wochen.
- **Mindestlaufzeit:** 4 Wochen.
- **Risiko:** Rechner-Ergebnisse fachlich falsch → Vertrauensschaden. **Mitigation:** Einheiten, Systemgrenzen und Annahmen nach Skill voltage-evidence prüfen, bevor der CTA live geht.

---

## 4. Cold-Start-Strategie: 0 → 50 Techniker in Lagos und Nairobi in 90 Tagen

**Rahmenbedingungen:** 1–2-Personen-Team, Mini-Budget < 500 $/Monat (beide Städte zusammen), kein Paid Ads. Zielgröße: 50 **aktivierte** Techniker pro Stadt (definiert als Profil vollständig + Verifikation Level 1 gestartet), nicht 50 rohe Registrierungen. Reihenfolge: **Lagos zuerst** (größter Nachfragepool, Länder-Bericht Platz 1), Nairobi startet 3–4 Wochen versetzt mit übertragenen Learnings (Wettbewerber Fundis validiert dort das Modell, erfordert aber Schärfung: Solar-/IT-Fokus, Scout-System).

### Phase 0 — Vorbereitung (Woche 1)
- Segmentierung festlegen: pro Stadt **2 Gewerke** (Empfehlung Lagos: Elektrik + Solar; Nairobi: Solar + IT/Elektrik) — Fokus schlägt Breite.
- Ranking-Waitlist-Framing vorbereiten (E1), WhatsApp-Business-Profil mit Quick Replies einrichten (E2), UTM-Konventionen festlegen.
- Liste bauen: 100+ konkrete Ansprechziele pro Stadt aus öffentlich sichtbaren Quellen — Jiji.ng-Dienstleistungsrubriken, Facebook-Gruppen, Elektro-Großhändler, technische Colleges, Solarfirmen-Verzeichnisse (Nigeria: 370 neu registrierte Solarfirmen 2025 laut Ember — ein belegter, anschreibbarer Pool). Nur öffentlich sichtbare Kontaktdaten nutzen, keine Scrapes privater Daten ins Repository.

### Phase 1 — Gründer-Kohorte (Woche 2–4, Ziel: je 10)
- **Persönliche 1:1-Ansprache** per WhatsApp/Anruf, keine Massennachrichten. Pitch: „Gehöre zu den ersten 10 geprüften Elektrikern von Lagos auf Voltage Africa — Gründer-Badge, Spitzenplatz im öffentlichen Ranking, wir bringen dir deine ersten Aufträge."
- **Concierge-Onboarding:** Profil gemeinsam im Gespräch anlegen (15 Min), Verifikationsdokumente direkt einfordern. Jede Woche 10–15 Gespräche → 3–5 Aktivierungen.
- **Simultaner Nachfrage-Funken:** Parallel 30–50 reale Testanfragen über Gruppen und eigenes Netzwerk einholen und manuell vermitteln (entspricht Maßnahme 1 des Länder-Berichts). Jede vermittelte Anfrage an die Gründer-Kohorte = E5-Versprechen in Aktion.
- Budget: ~150 $/Stadt für Datenpakete/Airtime als Gesprächs-Incentive (als Aufwand vergüten, nicht als Anmelde-Prämie — sonst falsche Anreize).

### Phase 2 — Referral-Multiplikator (Woche 5–8, Ziel: je 30 kumuliert)
- E6 live: Jede:r der 10 Gründer-Techniker erhält den persönlichen Link; Zielvorgabe im Gespräch: „Bringe 3 Kollegen, die du selbst für gut befindest." Bonus greift erst bei deren Aktivierung.
- E7-Pilot: 2–3 Elektro-Großhändler pro Stadt als Scouts gewinnen (QR-Flyer, VIP-Logik). Erwartung: 5–10 zusätzliche Techniker pro Stadt über diesen Kanal.
- Wöchentliches Ranking-Update per WhatsApp an alle Techniker (Single-Player-Feedback-Loop, hält Aktivität ohne Aufträge).

### Phase 3 — Sichtbarkeit + Sättigung (Woche 9–12, Ziel: je 50 kumuliert)
- Ranking öffentlich schalten (ab ≥ 10 Profilen, s. E1-Mitigation) und in denselben Gruppen teilen, aus denen rekrutiert wurde — geschlossener Loop: Kunden sehen Angebot, Techniker sehen Wettbewerb.
- E9-Seeding auf Nachfrageseite hochfahren, damit die 50 Techniker auch Matches sehen (sonst churnet die mühsam gebaute Seite).
- Nairobi-Learnings zurück nach Lagos spielen (und umgekehrt): welche Pitch-Zeile, welcher Kanal, welche Gewerk-Mischung konvertiert — in einer einfachen wöchentlichen Lern-Tabelle festhalten.

**Erfolgs-Messung der 90 Tage (alle KPI-Framework):** KPI 8 (Registrierungen/Woche je Stadt), KPI 9 (Aktivierung ≤ 7 Tage, Ziel ≥ 60 %), KPI 11 (supply_per_request ≥ 0,5 in den Fokus-Segmenten), KPI 2 (Match-Quote ≥ 50 % in Lagos Elektrik). **Abbruch-/Pivot-Kriterium vorab festlegen:** Wenn nach Woche 6 < 15 aktivierte Techniker in Lagos trotz ≥ 40 Erstgesprächen → Pitch und Zielgruppe (Gewerk, Stadtteil) überarbeiten, bevor Nairobi skaliert wird.

---

## 5. Anti-Patterns — was in dieser Phase NICHT tun

1. **Beide Marktseiten in mehreren Städten/Ländern gleichzeitig anschieben.** Ein Marktplatz in der Frühphase gewinnt durch Dichte, nicht durch Fläche: 50 verfügbare Techniker in einem Segment (Lagos × Elektrik) sind mehr wert als 500 verstreute Profile in fünf Ländern, weil nur Dichte die Match-Quote (KPI 2) über das Vertrauens-Schwellenniveau hebt. Die Länder-Priorisierung hat mit Tier-2/Tier-3 bereits eine Sequenz begründet; sie jetzt zu ignorieren, weil „die Website schon fünf Sprachen hat", verstreut ein 1–2-Personen-Team auf null Wirkung — und jede enttäuschte Anfrage in einer dünnen Stadt beschädigt die Marke lokal nachhaltig (Mundpropaganda-Märkte).
2. **Mit Paid Ads oder Anmelde-Prämien skalieren, bevor Liquidität in einer Nische belegt ist.** Bezahlte Nachfrage, die auf `match_rate_pct < 50 %` trifft, kauft systematisch schlechte erste Erfahrungen — die teuerste Form von Marketing. Ebenso gefährlich: Geld-Prämien für Registrierungen (statt für Aktivierung/ersten Auftrag) erzeugen Scheinprofile und vergiften KPI 8/9 als Steuergrößen. Erst wenn in einem Segment supply_per_request ≥ 0,5 und Annahmequote ≥ 30 % stabil sind, ist ein Mini-Testbudget für Nachfrage-Kanäle sinnvoll — und selbst dann bleiben bei kleinem n alle Schlüsse qualitativ.
3. **Liquidität vortäuschen oder Vertrauenssignale verwässern.** Künstliche Profile, gekaufte oder gestellte Bewertungen, XP-Inflation oder das Absenken der Verifikationshürden, „damit die Liste voller aussieht", zerstören exakt das dokumentierte Alleinstellungsmerkmal: Der Länder-Bericht zeigt, dass die Vertrauenslücke („geprüfte Fachkraft") das Kernproblem dieser Märkte ist und Jiji & Co. sie offen lassen. Ein einziger öffentlich werdender Fake-Fall wäre in eng vernetzten WhatsApp-Communities irreparabel. Regel aus voltage-growth gilt strikt: kein Wachstum, das durch schlechtere oder vorgetäuschte Vermittlung erkauft wird — dazu gehört auch, Ranking- und Verifikationsclaims nur so weit zu kommunizieren, wie sie betrieblich belegt sind (voltage-evidence).

---

## 6. Drei nächste Maßnahmen

1. **E2 + E5 sofort starten (diese Woche, kein Code-Blocker).** WhatsApp-first-CTA für Techniker umstellen und die 7-Tage-Erst-Match-Ops-Routine einführen; parallel die Baseline-SQL aus dem KPI-Framework laufen lassen, damit der Vorher-Zustand dokumentiert ist (Abstimmung mit KPI_Analytics wegen Vorbedingung L3: prüfen, ob `award_xp('profile_completed')` tatsächlich ausgelöst wird — sonst KPI 9 als „nicht messbar" kennzeichnen).
2. **E1 vorbereiten: stadtscharfes Ranking mit Mindest-Schwelle.** Klären, welche Supabase-Policies öffentliche Ranking-Daten zulassen; Waitlist-Framing-Texte (EN) für Lagos Elektrik/Solar erstellen; Launch-Kriterium „≥ 10 Profile je Segment" festlegen.
3. **E6 bauen: Referral-Link + WhatsApp-Teilen im Profil.** Vorab eine Entscheidung festzurren: Bonus-Gutschrift erst bei Aktivierung des Geworbenen (nicht bei Registrierung); Teilen-Texte in EN formulieren, FR/PT als Folgeaufgabe für Tier-2 markieren.

---

*Methodik-Hinweis gemäß SENIOR-STANDARD: Dieser Backlog enthält keine Ist-Zahlen und keine behaupteten Plattformleistungen. ICE-Scores, Uplift-Erwartungen und Kanalannahmen sind Hypothesen mit expliziten Entscheidungs- und Abbruchkriterien; Marktfakten (WhatsApp-Reichweiten, Solar-Marktdaten) stammen aus dem Länder-Bericht vom 2026-09-21 mit dort genannten Quellen und Qualitätsstufen. Kein Experiment schwächt Verifikations- oder Sicherheitsanforderungen für Conversion-Ziele ab.*
