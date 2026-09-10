# Fachliche Skill-Erprobung

Die Fälle in skill-eval-cases.json sind vorbereitete Prüfaufgaben, keine bereits bestandenen Leistungsnachweise.

Für die Erprobung einer Rolle:
1. Gib dem ausführenden Werkzeug nur den Auftrag aus prompt, den zugehörigen Skill und nötige Eingaben. Keine echten Kontodaten und keine externen Schreibaktionen.
2. Speichere die tatsächliche Antwort mit Datum, Skill-Commit und ausführendem Werkzeug.
3. Vergleiche danach mit expected_behavior und dem Abnahmeteil des Skills. Prüfe Aussagen gegen Belege.
4. Dokumentiere bestanden, Nacharbeit oder nicht prüfbar. Ein Lauf desselben Agenten ist Selbstprüfung.
5. Ergänze für eine Änderung einen neuen Fall, der den gleichen Fehler aufdecken könnte, und einen Gegenfall. Nutze reale Aufgaben für spätere Wirksamkeitsmessung.

Strukturvalidierung prüft nur auffindbare Dateien, Zuordnung und Metadaten. Sie bewertet keine Fachkompetenz. Geschäftswirkung und unabhängige fachliche Prüfung sind bei der initialen Einrichtung noch offen.
