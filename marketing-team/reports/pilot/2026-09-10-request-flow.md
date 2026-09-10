# Pilot: Anfrageweg und Formular

Datum: 2026-09-10. Ausführende Rolle: Vermittlung/Qualitätsprüfung im Hauptagenten. Status: statische Prüfung ausgeführt; eigener Live-Aufruf des Anfrageformulars wegen zweimaliger Browser-Zeitüberschreitung nicht abgeschlossen. Keine Formulareingaben, Nachrichten, Backendzugriffe oder Websiteänderungen.

## Methode

Gelesen: voltage-matching, voltage-quality, der neu installierte cro-Skill samt Form-Referenz und die offiziellen Vercel-Web-Interface-Guidelines (Commit e3d624baaf29dc1fc645aff3e38f03e564d2d6b1). Lokale Quelle: request.html im vorhandenen Voltage-Website-Ordner. Der lokale Code ist kein Nachweis des aktuell ausgerollten Backends. Pauschale Conversion-Prozentwerte in der externen Form-Referenz wurden nicht als Projektdaten verwendet.

## Befunde

| Priorität | Beobachtung und Fundstelle | Konsequenz / konkrete Empfehlung |
|---|---|---|
| P1 | request.html:244–254 versucht eine Anfrage zu speichern und ruft bei einem Ergebnis ohne gemeldeten Speicherfehler danach match_technicians auf. Fehler der Treffervorschläge werden abgefangen; done(matches) zeigt den Ergebnisbereich auch ohne Treffer. | Anfrageeingang und Vermittlung sind unterschiedliche Zustände. Ergebnistext und Analytics müssen gespeichert, keine Treffer, Treffervorschläge und bestätigter Abschluss getrennt beschreiben. Der Prüflauf hat keinen Backendfehler nachgewiesen. |
| P1 | request.html:264–271 enthält einen Demo-Fallback: lokale Speicherung, WhatsApp-Weiterleitung und done([]). | Lokales Speichern oder Öffnen eines WhatsApp-Links beweist keinen Versand. Ein gesonderter Hinweis muss die noch ausstehende Handlung benennen. Ob der Fallback live aktiv ist, wurde nicht geprüft. |
| P2 | Der im SEO-Pilot beobachtete Nairobi-CTA führt generisch auf request.html. request.html:167 übernimmt getCountry(), während Gewerkoptionen aus CATS kommen; der betrachtete Code übernimmt keinen Nairobi-/Solar-Kontext aus dem Einstiegslink. | Stadt, Land und Gewerk als ausdrücklich überprüfbare Vorauswahl übergeben. Der Nutzer muss sie ändern können. Abnahme durch tatsächlichen Browserlauf mit Nairobi-Solareinstieg; die aktuelle Vorauswahl wurde nicht live getestet. |
| P2 | rq-name, rq-city und weitere Felder besitzen keine name-Attribute; Name/Stadt haben keine passenden autocomplete-Angaben (request.html:75,98–101). Das Skript liest per ID. | Name/autocomplete sinnvoll ergänzen; fehlende name-Attribute bedeuten bei dieser JavaScript-Verarbeitung nicht automatisch einen kaputten Versand. Feldzweck und Autofill verbessern. |
| P2 | Mehrere Labels und der Submit-Text sind im lokalen HTML leer und werden übersetzt eingefügt (request.html:75,77,98,100–103). | Verständliche englische Fallbacktexte hinterlegen. Die Agenten haben auf der Nairobi-Seite korrekt gerenderte CTAs gesehen; ein Laufzeitfehler auf request.html ist damit weder belegt noch ausgeschlossen. |

Positiv im Code: Labels verweisen auf Feld-IDs; Telefonnummern haben type=tel und autocomplete; clientseitige Fehler markieren aria-invalid und fokussieren das erste betroffene Feld; der Button wird während des Speicheraufrufs deaktiviert und bei Fehler wieder freigegeben (request.html:178–214,221–259). Das ist eine statische Beobachtung, keine vollständige Zugänglichkeits- oder Servervalidierungsprüfung.

## Drei nächste Aufgaben

1. Eindeutige Ergebniszustände für Speicherung, Treffer, WhatsApp-Übergabe und Abschluss spezifizieren; mit kontrollierten lokalen/Staging-Testdaten prüfen. Keine echten Anfragen an Techniker.
2. Kontextübergabe Nairobi/Kenia/Solar vom Einstiegslink bis zum Formular nachweisen; Fehler- und Leerzustände zusammen mit den Claims der Startseite prüfen.
3. Fallbacktexte und Autofill ergänzen, danach Tastatur-/Mobil-/Sprachprüfung durchführen. Kein Conversion-Uplift ohne Messdaten behaupten.

## Grenzen

Kein erfolgreicher Browser-/Ende-zu-Ende-Test des Anfrageformulars, keine Prüfung von Datenbankberechtigungen und keine bestätigte Anbieterabdeckung. Der installierte Python-Testskill ist methodisch verfügbar; Python-Playwright ist nicht installiert. Vor automatisierten Tests ist eine geeignete Laufzeit notwendig. Dieser Bericht ist eine Selbstprüfung des Hauptagenten; eine gesonderte Prüfung der Aussagen kann die zugrundeliegenden Grenzen nicht aufheben.

Gegenprüfung: Der Trust-Fachagent hat diesen Bericht gegen den lokalen Anfrage-Code geprüft; die Speicherformulierung wurde präzisiert. Dies ersetzt keinen Live- oder Backendtest.
