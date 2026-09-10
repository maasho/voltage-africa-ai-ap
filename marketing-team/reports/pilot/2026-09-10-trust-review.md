# Voltage Africa: Vertrauens- und Claims-Pilot

Datum: 2026-09-10. Rolle: Bewertungen und Vertrauen. Status: lokale statische Prüfung abgeschlossen; Korrekturvorschläge nicht veröffentlicht.

## Umfang und Nachweisgrenze

Geprüft wurden about.html, faq.html, scout-guide.html, terms.html, rankings.html sowie nur die benötigten öffentlichen Texte und Funktionen in assets/i18n.js, assets/data.js und assets/app.js. Quellbasis: `J:/03_Voltage_Africa/Voltage_Afrika_Projects/Voltage-Africa B2/B2/voltage-africa-website`. Alle nachstehenden Fundstellen beziehen sich auf diesen lokalen Stand. Die i18n-Datei enthält die englischen Übersetzungen gemeinsam in Zeile 3; deshalb wird zusätzlich der genaue Schlüssel genannt.

Keine Aussage dieses Berichts bestätigt den aktuellen Live-Stand. Kein Browser-Funktionstest, kein Backendzugriff, keine Prüfung privater Profile oder Dokumente und keine Testanfrage wurden ausgeführt. Insbesondere wurden Konfigurationsdateien mit Zugangsdaten nicht gelesen. Website und Konten wurden nicht verändert. Dies ist eine Prüfung der kommunizierten Zusagen und der dazu sichtbaren statischen Umsetzung, keine rechtliche Bewertung und kein Nachweis fehlender betrieblicher Prozesse.

Geladene Grundlagen: AGENTS.md, README.md, TEAM.md, WEBSITE-CONTEXT.md, PILOT.md, SENIOR-STANDARD.md, Rollenprofil voltage-trust-review-lead sowie voltage-trust und voltage-evidence. memory/INDEX.md enthält bislang keine validierten Praxiserkenntnisse.

## Aussage und belegbare Umsetzung

| Aussage | Fundstelle | Beobachtbare Umsetzung / Grenze |
|---|---|---|
| Geprüfte Bewertungen und ein faires Ranking, das Arbeitsqualität belohnt | about.html:8; about.html:62; assets/i18n.js:3, en.ab_p1 und en.ab_s2_d | Rankings werden nach XP absteigend sortiert (assets/data.js:96,114,117). Die Anzeige enthält Rangnummer, Name, Gewerk und XP (assets/app.js:254–274). Eine Bewertung tatsächlicher Arbeitsqualität lässt sich daraus nicht ableiten. |
| Verifizierte Kundenbewertungen, Zertifikatsuploads und Vermittlungen erhalten feste XP; Algorithmen und manuelle Prüfungen sichern Fairness | faq.html:27; faq.html:72; assets/i18n.js:3, en.fq2a | Die statisch definierte Profilabfrage und Abbildung enthalten ein boolesches verified-Feld (assets/data.js:66,87); die Profilkarte kann ein Häkchen zeigen (assets/app.js:300). Prüfumfang, Prüfer, Datum und Ablauf sind in dieser Darstellung nicht enthalten. Upload, Identität, Zulassung und Arbeitsqualität bleiben ungetrennt. Die Backend-Vergabe von XP und Prüfprozesse sind hier nicht untersucht; deren Existenz wird weder bestätigt noch verneint. |
| VIP-Punkte wandeln sich in monatliche Provisionen um; Beträge ab $10 bis $100+ | scout-guide.html:73,79–83; assets/i18n.js:3, en.sg_a1_d und en.rw_1 bis en.rw_4; faq.html:28 | terms.html:70 sagt gleichzeitig, dass XP und VIP keinen Geldwert haben. Das kann bei einem getrennten Bonusprogramm vereinbar sein, ist jedoch ohne getrennte Anspruchsbedingungen widersprüchlich erklärt. Die Tabelle nennt einen Qualitätsmultiplikator; Auszahlung, Währung hinter dem Dollarzeichen, Länderberechtigung und Anspruchsbedingungen sind durch diese Dateien nicht belegt. |
| Monatliches Ranking, alle sechs Stunden aktualisiert; die besten Techniker | rankings.html:8,60; assets/i18n.js:3, en.rank_sub | assets/data.js:96,104 lädt höchstens 200 Profile nach XP; assets/data.js:131–138 startet den Abruf beim Seitenladen. Die lokale Umsetzung zeigt weder Monatsfilter noch Sechs-Stunden-Timer. Eine serverseitige Berechnung bleibt ungeprüft. Länderfilter folgen auf den begrenzten globalen Abruf (assets/data.js:117,128), daher ist Vollständigkeit je Land nicht zugesichert. |
| Höherer Rang und besseres Portfolio erhöhen die Sichtbarkeit | faq.html:29; assets/i18n.js:3, en.fq4a | Der geprüfte Ranking-Pfad sortiert nach XP. Ein eigenständiger Portfolio-Qualitätsfaktor ist dort nicht ersichtlich. Andere Such-/Partneransichten sind nicht Teil dieser Prüfung. |
| Scouts werden Teil internationaler Projekte und erhalten Herstellerzugang | scout-guide.html:74–75; assets/i18n.js:3, en.sg_a2_d und en.sg_a3_d | Öffentliche Nutzenversprechen, ohne in den geprüften Dateien belegte Partnerzusagen oder Teilnahmebedingungen. Nicht als gesicherte Gegenleistung für Registrierung wiederverwenden. |

Positiv: rankings.html:147–159 und assets/app.js:258–262 sehen einen expliziten Leerzustand vor. Dieser ist ehrlicher als erfundene Teilnehmerdaten. Er beweist weder reale Verfügbarkeit noch die Live-Funktion. terms.html:83 enthält außerdem einen sichtbaren Vorlagenhinweis; das Dokument sollte nicht als abschließend geprüfte Vertragsgrundlage bezeichnet werden.

## Drei priorisierte Maßnahmen

### 1. P1 — Scout-Vergütung verständlich und belegbar machen

Verantwortlich: Community/Scouts gemeinsam mit Betreiber und Compliance. Vor weiterer Verwendung der Einnahmenwerbung ein freigegebenes Vergütungsblatt verlangen: teilnahmeberechtigte Länder, eindeutige Währung, gültiger Zeitraum, Punkte-/Bonusbeziehung, Berechnung und Qualitätsprüfung, Auszahlungstermin, Mindestbetrag und Ausschlussbedingungen. Ohne Nachweise Beträge und garantierte monatliche Einnahmen in Scout Guide, FAQ, Metadaten und allen Übersetzungen durch eine neutrale Einladung ersetzen. Die Backend-Auszahlung wird durch dieses Audit nicht bewertet.

**English replacement proposal (pending owner review, not published):**

> Scouts help technicians build profiles and stay active in their local community. Before joining for paid work, contact Voltage Africa to confirm whether a paid scout programme is available in your country and request its written eligibility and payment terms. VIP points alone do not guarantee a payment.

**Abnahme:** Vergütungsblatt belegt jede verbleibende Zahl; FAQ, sichtbare Texte, Social-Metadaten und Terms beschreiben dieselbe Punkte-/Bonusbeziehung. Keine internationale Projekt- oder Herstellerpartnerschaft als garantierte Leistung ohne Beleg.

### 2. P1 — Verifikation in präzise Nachweise aufteilen

Verantwortlich: Vertrauen mit Plattformverantwortlichen. Für jedes öffentliche Vertrauenslabel definieren: Selbstauskunft, Identitätsprüfung, Dokumentprüfung, konkrete lokale Berufszulassung oder auftragsbezogene Bewertung. Benötigt werden Prüfumfang, Datum, Ablauf und verantwortlicher Prozess; öffentlich nur die nötigen nicht privaten Angaben anzeigen. Ein Häkchen oder Zertifikatsupload darf keine umfassende Qualifikationsprüfung suggerieren. Claims zu manuellen Kontrollen und Anti-Cheating erst nach betrieblichem Nachweis erneuern.

**English replacement proposal (pending owner review, not published):**

> Profiles present information about technicians and their work. Before hiring, ask for evidence of relevant qualifications, any licence required for your project, references and current availability. XP scores do not establish professional qualifications or guarantee work quality.

**Abnahme:** Jeder verbleibende verified-Claim besitzt eine eindeutige Definition und prüfbare Prozessgrundlage. Änderungen an faq.html müssen sowohl en.fq2a als auch das FAQ-JSON-LD in faq.html:27 einschließen. Backend- und Prozessprüfung gesondert beauftragen; keine privaten Belege ins AI-Repository kopieren.

### 3. P2 — Ranking als XP-Reihenfolge mit klarer Datenabdeckung beschreiben

Verantwortlich: Plattform/Qualität und Content. Die geprüfte Sortierung präzise beschreiben; monatlichen Zeitraum, Sechs-Stunden-Rhythmus und Qualitätsurteil nur behalten, wenn dafür ein eigener Nachweis vorliegt. Bei Umsetzung vollständiger Länderlisten die Abfragebegrenzung von 200 globalen Profilen berücksichtigen. Leere Listen nicht als fehlende Fachkräfte im Land interpretieren.

**English replacement proposal (pending owner review, not published):**

> Community XP rankings. Profiles returned by the directory are ordered by XP. This list may not include every technician in the selected country. XP is not a measure of professional licensing or a guarantee of work quality.

**Abnahme:** Ranking-Metadaten und en.rank_sub enthalten keine unbelegten Aktualisierungs- oder Qualitätszusagen. Eine spätere Funktionsprüfung bestätigt Datenumfang und Aktualisierungsverhalten; diese statische Prüfung bestätigt beides nicht.

## Ergebnis und Lernstatus

Der erste Vertrauenspilot liefert sechs belegte Claim-Prüfpunkte und drei umsetzbare Maßnahmen. Keine Änderungen veröffentlicht; keine Tests von Vermittlung, Verifizierung oder Auszahlungen behauptet. Übertragbare Erkenntnis als Kandidat: Vertrauens- und Einkommensclaims müssen gleichzeitig in HTML-Metadaten, JSON-LD, Übersetzungen und sichtbarer Darstellung geprüft werden. Dieser Bericht allein macht daraus noch keine validierte allgemeine Lernregel.
