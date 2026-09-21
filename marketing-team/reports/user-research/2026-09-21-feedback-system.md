# Feedback- und Research-System für Voltage Africa

**Rolle:** Nutzer_Feedback (Product Feedback Synthesizer)
**Datum:** 2026-09-21
**Status:** Entwurf zur Umsetzung ohne neue Infrastruktur (WhatsApp + eine Supabase-Tabelle)

---

## 1. Zusammenfassung

Voltage Africa hat aktuell kein systematisches Feedbacksystem; vorhandene Website-Texte belegen kommunizierte Angebote, keine betriebliche Umsetzung (vgl. WEBSITE-CONTEXT.md). Dieses Konzept baut einen schlanken, mehrstufigen Feedback-Loop auf, der die reale Nutzung abbildet: WhatsApp als zentraler Kanal, kurze mobilfreundliche Erhebungen mit maximal 3 Fragen pro Touchpoint, und vertiefende Interviews für drei Gruppen (Kunden nach Vermittlung, registrierte Techniker, aktive Scouts).

Kernelemente:

- **4 Feedback-Touchpoints** entlang der Journey (nach Vermittlung, In-Product, Scout-Runde, Registrierungsabbruch) mit fertigen englischen Fragetexten.
- **3 Interview-Leitfäden** (Englisch, je 8–10 Fragen) mit Fokus Vertrauen, Zahlungsbereitschaft, Hürden.
- **Monatlicher Synthese-Prozess** mit Tagging-Schema, Themen-Clustern und einer Entscheidungsvorlage „Weiter / Ändern / Stoppen".
- **Explizites Bias-Management**: Survivorship-Bias, Scout-Bias, Sprach-/Kanal-Bias werden im Design adressiert, nicht erst in der Auswertung.

Alles speichert in einer einzigen Supabase-Tabelle `feedback_responses`; WhatsApp-Versand erfolgt manuell oder über den bestehenden WhatsApp-Kanal. Keine neue Infrastruktur, keine neuen Tools.

---

## 2. Feedback-Kanäle mit Fragetexten

Grundregeln für alle Touchpoints:

- Max. 3 Fragen, davon max. 1 Freitext; Antworten per Zahl (1–5) oder Emoji, damit sie per WhatsApp-Reply ohne Tastaturaufwand beantwortbar sind.
- Versand in der Sprache des bisherigen Kontakts (EN als Standard, FR/PT nach Kontaktsprache; Land und Sprache getrennt behandeln).
- Einwilligungszeile am Anfang jeder Erhebung: *"Your answers help us improve Voltage Africa. Reply STOP to opt out."*
- Keine XP/VIP-Punkte als Anreiz für positive Bewertungen; Anreize (falls genutzt) nur für Teilnahme, nie inhaltlich gekoppelt.

### Touchpoint 1: WhatsApp-Umfrage nach abgeschlossener Vermittlung (Kunde)

**Auslöser:** 48–72 Stunden nach bestätigter Vermittlung. **Ziel:** Vertrauen und Vermittlungsqualität.

> Hi {first_name}, this is Voltage Africa. You recently hired {technician_name} through us. 3 quick questions (reply with a number):
>
> 1. How satisfied were you with the technician's work? (1 = very bad, 5 = excellent)
> 2. How much did you trust the technician before the job started? (1 = not at all, 5 = fully)
> 3. What almost stopped you from booking? (Reply with one word, e.g. price, trust, time, payment)

### Touchpoint 2: WhatsApp-Umfrage nach abgeschlossener Vermittlung (Techniker)

**Auslöser:** Parallel zu Touchpoint 1, an die vermittelte Fachkraft. **Ziel:** Gegenseite prüfen, Diskrepanzen sichtbar machen (z. B. Zahlungsprobleme).

> Hi {first_name}, quick check from Voltage Africa about your job with {customer_name}. 3 questions (reply with a number):
>
> 1. Did the customer pay you as agreed? (1 = not at all, 5 = yes, fully and on time)
> 2. Was the job description from the customer clear? (1 = very unclear, 5 = very clear)
> 3. What was the hardest part of this job for you? (One word, e.g. payment, transport, tools, communication)

### Touchpoint 3: Kurze In-Product-Umfrage (Website: hire.html / signup.html / profile.html)

**Auslöser:** Nach dem 3. Login bzw. nach dem 2. abgeschlossenen Prozessschritt, einmalig pro Nutzer und Quartal. Umsetzung als einfache Inline-Frage mit Link auf WhatsApp (kein neues Formular-Backend nötig; Antwort kommt per WhatsApp-Reply in denselben Eingang). **Ziel:** Reibung im laufenden Prozess.

> Quick question from Voltage Africa — help us improve:
>
> 1. How easy was it to use this page today? (1 = very hard, 5 = very easy)
> 2. What were you trying to do? (Post a job / Complete my profile / Find work / Other)
> 3. Did anything block you? (Yes / No — if yes, one word: what?)

### Touchpoint 4: Scout-Feedbackrunde (monatlich, WhatsApp-Gruppennachricht an aktive Scouts)

**Auslöser:** Monatlich, an Scouts mit mindestens 1 geworbenem Profil im Zeitraum. **Ziel:** Referral-Loop und Echtheit der geworbenen Profile prüfen.

> Hi {first_name}, monthly scout check-in from Voltage Africa. 3 questions:
>
> 1. How many people did you refer this month who are actually still active? (Number)
> 2. Would you recommend scouting for Voltage Africa to a friend? (1 = no, 5 = yes, definitely)
> 3. What is the one thing that would make you refer more people? (One word, e.g. payout, tools, support, status)

### Touchpoint 5: Abbruch-Feedback bei Registrierung (Techniker)

**Auslöser:** signup.html gestartet, aber nach 7 Tagen kein vollständiges Profil. Eine einzige WhatsApp-Nachricht, kein zweites Follow-up (Vermeidung von Druck und Spam-Risiko). **Ziel:** Hürden im Registrierungsprozess — die Gruppe, die sonst unsichtbar bleibt (Gegenmaßnahme gegen Survivorship-Bias).

> Hi {first_name}, you started signing up on Voltage Africa but didn't finish. No problem — one quick question so we can fix it:
>
> 1. What stopped you from finishing your profile? (Reply with a number: 1 = too complicated, 2 = missing documents, 3 = no jobs near me, 4 = don't trust it, 5 = other — tell us in one word)

**Datenhaltung (eine Supabase-Tabelle, kein neues Backend):**

Tabelle `feedback_responses` mit Feldern: `id`, `created_at`, `touchpoint` (1–5), `respondent_role` (customer / technician / scout), `country_city`, `language`, `channel` (whatsapp / web), `q1_score` (int, nullable), `q2_value` (text), `q3_verbatim` (text), `consent` (bool), `anonymized_token` (Hash, keine Klarnamen/Telefonnummern im Analysedatensatz). Erfassung zunächst manuell per Copy-Paste aus WhatsApp in eine einfache Eingabemaske oder CSV-Import — bewusst niedrigschwellig, bis Volumen Automatisierung rechtfertigt.

---

## 3. Interview-Leitfäden (Englisch)

Allgemeine Durchführungsregeln:

- Dauer 20–30 Minuten, per WhatsApp-Anruf oder vor Ort; Sprache nach Präferenz der Person (Leitfaden EN, Übersetzung durch interviewende Person dokumentieren).
- Einwilligung zu Beginn, Anonymisierung in jeder Dokumentation. Keine erfundenen Zitate in Berichten: nur wörtlich dokumentierte Aussagen verwenden.
- Pro Gruppe und Monat Ziel 5–8 Interviews; Stichprobe, Dubletten und Gegenbelege im Synthesebericht sichtbar machen (Abnahmekriterium laut voltage-user-research).

### Leitfaden A: Kunden nach abgeschlossener Vermittlung

1. Can you walk me through how you found and hired the technician, step by step?
2. What made you trust — or not trust — the technician before the work started?
3. What did you check before agreeing on the job? (Profile, reviews, price, personal call?)
4. Was there a moment where you almost cancelled or chose someone else? What happened?
5. How did payment work, and how did you feel about it?
6. Would you pay a fee to Voltage Africa for this service? Why or why not?
7. What would need to be true for you to use Voltage Africa again without hesitation?
8. If a friend asked you whether to use Voltage Africa, what would you tell them?
9. Is there anything about the process that felt unsafe or unclear?

### Leitfaden B: Registrierte Techniker

1. Tell me about your experience from signing up to today — what went well, what was hard?
2. How many real jobs have come to you through Voltage Africa so far?
3. What do you think customers look at before they choose you?
4. Have you ever had a payment problem with a customer from the platform? What happened?
5. What documents or proof did you need to provide? Was anything unclear or difficult to get?
6. Do the XP/VIP points and rankings matter to you? Do you believe they bring you more jobs?
7. Would you pay for a better position or more visibility on the platform? Why or why not?
8. What other ways do you currently find work, and how does Voltage Africa compare?
9. What is the one thing we could change that would bring you more good jobs?
10. Have you ever thought about deleting your profile? What triggered that thought?

### Leitfaden C: Aktive Scouts

1. How did you become a scout, and what motivated you at the start?
2. Walk me through how you typically find and refer a technician.
3. How many of the people you referred are still active today? Why did the others stop?
4. What do the people you refer ask you before they sign up? What worries them?
5. Have you received the rewards or recognition you expected? How did that feel?
6. Do you ever refer people you don't know well? What do you check before referring someone?
7. Would you still scout if the points had no rewards attached? Why or why not?
8. What would make you refer twice as many people next month?
9. Have you seen any fake profiles or misuse in the scout system? Can you describe it (without names)?
10. If you ran the scout program for a day, what is the first thing you would change?

---

## 4. Synthese-Prozess (monatlich)

### 4.1 Eingang und Bereinigung

1. Alle Rohantworten des Monats aus `feedback_responses` plus Interview-Mitschnitte/Notizen sammeln.
2. Dubletten entfernen (gleiche Person, gleicher Touchpoint, gleicher Zeitraum → `anonymized_token` prüfen).
3. **Personen zählen, nicht Nachrichten** (voltage-user-research): Ein aktiver Scout mit 20 Nachrichten ist eine Stimme, nicht zwanzig.
4. Gemeldetes Problem und vorgeschlagene Lösung getrennt erfassen — Nutzer diagnostizieren gut, verschreiben schlecht.

### 4.2 Tagging-Schema

Jede Antwort/jedes Verbatim erhält Tags aus vier festen Dimensionen:

- **Marktseite:** `customer` / `technician` / `scout`
- **Prozessschritt:** `registration` / `profile` / `matching` / `job_execution` / `payment` / `referral`
- **Thema:** `trust` / `price_payment` / `usability` / `language` / `supply_demand` (keine passenden Jobs/Techniker) / `verification` / `communication` / `rewards_xp`
- **Schwere:** `blocker` (verhindert Vermittlung) / `friction` (verzögert/verärgert) / `nice_to_have`

Ort (Stadt/Land) und Sprache sind Pflicht-Metadaten, keine Tags — Afrika wird nie als einheitlicher Markt aggregiert, Cluster werden immer pro Stadt/Gewerk gebildet.

### 4.3 Themen-Cluster

- Pro Monat die 5 häufigsten Themen-Cluster pro Marktseite bilden, jeweils mit: Anzahl betroffener **Personen**, Schwere-Verteilung, 2–3 wörtliche Belege (anonymisiert), Gegenbelege (Fälle, in denen es funktioniert hat).
- Kleine Stichproben explizit kennzeichnen: *"n = 7 Techniker, nur Lagos, nur WhatsApp-Responder — kein Marktanteil."*
- Priorisierung nach drei Kriterien: **Häufigkeit × Schwere × Einfluss auf sichere erfolgreiche Vermittlung** (nicht auf Lautstärke).

### 4.4 Entscheidungsvorlage „Weiter / Ändern / Stoppen"

Pro priorisiertem Cluster eine halbe Seite:

| Feld | Inhalt |
|---|---|
| Erkenntnis | Ein Satz, z. B. „Techniker in {Stadt} brechen die Registrierung beim Dokumentenupload ab." |
| Beleg | n Personen, Touchpoints, Zeitraum, wörtliche Belege, Gegenbelege |
| Betroffener Prozessschritt | Tag aus 4.2 |
| Hypothese | Überprüfbare Produktfrage, z. B. „Wenn wir den Upload auf 2 Dokumente reduzieren, steigt die Fertigstellungsquote um X." |
| Entscheidung | **Weiter** (aktuelles Vorgehen bestätigt, messen weiter) / **Ändern** (konkrete Maßnahme + Testhypothese + Verantwortliche Rolle) / **Stoppen** (Feature/Prozess einstellen, mit Begründung) |
| Erfolgsmaß | Woran man in 4–8 Wochen erkennt, ob die Entscheidung richtig war |

Jede Synthese endet mit mindestens einer **überprüfbaren Produktfrage oder Testhypothese** an Produkt/Plattform (Abnahmekriterium). Ergebnisse gehen als Entscheidungsvorlage ans Marketingteam und — sofern Website-Code betroffen — als fachliches Briefing, nie als direkter Code-Eingriff.

---

## 5. Verzerrungen und Gegenmaßnahmen

| Verzerrung | Mechanismus bei Voltage Africa | Gegenmaßnahme im Design |
|---|---|---|
| **Survivorship-Bias** (gewichtigste) | Feedback kommt überwiegend von erfolgreich Vermittelten und vollständig Registrierten; Abbrecher und nie-Vermittelte sind unsichtbar. Man lernt nur, warum es klappt, nicht warum es scheitert. | Touchpoint 5 (Abbruch-Feedback) erreicht gezielt Nicht-Abschließer. Touchpoint 2 fragt die Gegenseite derselben Vermittlung; Diskrepanzen werden sichtbar. In der Synthese Pflichtangabe: Anteil Antwortende vs. Angeschriebene pro Touchpoint; Cluster ohne Abbrecher-Perspektive werden als „einseitig belegt" markiert. |
| **Scout-Bias** | Scouts verdienen an der Plattform (XP/VIP, Status) und berichten tendenziell positiv; geworbene Profile sind zudem nicht zufällig (Freunde/Bekannte, selbe Stadt, selbes Netzwerk). | Scout-Feedback wird nie mit Kunden-/Techniker-Feedback vermischt; eigener Cluster mit Kennzeichnung „interessengebunden". Leitfaden C enthält Kontrollfragen zu toten Profilen (Frage 3) und Anreizabhängigkeit (Frage 7). Referral-Erfolg wird gegen Plattformdaten geprüft, nicht nur gegen Selbstauskunft. |
| **Sprach-/Kanal-Bias** | Nur WhatsApp-Responder mit ausreichend EN/FR antworten; wer den Kanal oder die Sprache nicht nutzt, fehlt systematisch. | Sprache des bisherigen Kontakts verwenden, nicht Standard-EN erzwingen. Antwortoptionen als Zahlen/Emoji (geringe Sprachhürde). In der Synthese Rekrutierungs- und Sprachbias je Stichprobe kennzeichnen (voltage-user-research). |
| **Anreiz-/Höflichkeits-Bias** | Wenn Feedback mit Belohnung oder mit der vermittelnden Plattform selbst verknüpft ist, wird höflich-positiv geantwortet. | Keine Belohnung für Inhalt, nur ggf. für Teilnahme; Fragen neutral formuliert („What almost stopped you…" statt „How great was…"); Interviews durch eine Person führen, die nicht für die Vergütung der Befragten zuständig ist. |
| **Selbstselektion kleiner Stichproben** | n = 5–15 pro Gruppe und Monat ist kein Markt. | Jede Erkenntnis trägt Stichprobenangabe und Vertrauenshinweis; keine Prozentangaben aus einstelligen Stichproben; Entscheidungen mit niedriger Beleglage bekommen Testhypothese statt Sofortmaßnahme. |

---

## 6. Drei nächste Maßnahmen

1. **Supabase-Tabelle `feedback_responses` anlegen und Touchpoint 1 + 2 pilotieren** (Woche 1–2): Schema wie in Abschnitt 2 beschrieben; für die nächsten 10 bestätigten Vermittlungen beide Seiten anschreiben. Ziel: Antwortquote und Diskrepanz Kunde/Techniker bei Zahlung messen. Liefert die erste echte Datenbasis, bevor Interviews starten.
2. **Abbruch-Feedback (Touchpoint 5) aktivieren** (Woche 2–3): Alle unvollständigen Registrierungen der letzten 30 Tage einmalig anschreiben. Dies ist der schnellste Weg zur unsichtbarsten und wichtigsten Gruppe (Survivorship-Gegenmaßnahme) — erwartbare Erkenntnis: die 2–3 realen Registrierungshürden pro Stadt.
3. **Erste Interview-Runde und erste monatliche Synthese** (Woche 3–6): Je 5 Interviews aus Leitfaden A, B, C durchführen, nach dem Tagging-Schema clustern und die erste „Weiter / Ändern / Stoppen"-Vorlage mit mindestens einer überprüfbaren Testhypothese ans Team geben. Stichprobengrößen, Dubletten und Gegenbelege dokumentieren (Abnahmekriterien).

---

*Erstellt nach AGENTS.md, SENIOR-STANDARD.md, voltage-user-research und voltage-evidence. Keine erfundenen Nutzerzitate, Messwerte oder Plattformfunktionen; alle Fragen sind Entwürfe, keine Aussagen über tatsächliches Nutzerverhalten.*
