# Installierte externe Skills

Stand: 2026-09-10. Die folgenden Pakete wurden vollständig mit ihren mitgelieferten Referenzen und Hilfsdateien repositorylokal installiert. Die ursprünglichen Fachskills bleiben erhalten.

- [cro](../.agents/skills/cro/SKILL.md) — coreyhaines31/marketingskills, Commit 5b2c0007766c6a1cf1d53fd8fc73e979e0821022
- [signup](../.agents/skills/signup/SKILL.md) — coreyhaines31/marketingskills, Commit 5b2c0007766c6a1cf1d53fd8fc73e979e0821022
- [onboarding](../.agents/skills/onboarding/SKILL.md) — coreyhaines31/marketingskills, Commit 5b2c0007766c6a1cf1d53fd8fc73e979e0821022
- [web-design-guidelines](../.agents/skills/web-design-guidelines/SKILL.md) — vercel-labs/agent-skills, Commit 063bee94c3f4df8453406c830b0a7df0f2860278
- [webapp-testing](../.agents/skills/webapp-testing/SKILL.md) — anthropics/skills, Commit 41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f
- [supabase-postgres-best-practices](../.agents/skills/supabase-postgres-best-practices/SKILL.md) — supabase/agent-skills, Commit 8331f910845103c08d51f6ca1d86ebb7d1f745e3

Die Pakete sind im Checkout für passende Aufgaben auffindbar. In Codex werden neu installierte Skills im nächsten Turn verfügbar; in diesem Lauf können ihre Dateien bereits ausdrücklich gelesen werden. Die Installation erzeugt keine Kontozugriffe oder automatischen Hintergrundläufe.

## Prüfung und Grenzen

Die SKILL.md-Einstiegspunkte, Paketstruktur und der Python-Serverhelfer wurden geprüft. Das ist kein vollständiges Code- oder Fachaudit aller externen Referenzen. Der Serverhelfer startet angegebene Shellbefehle; nicht mit fremden Befehlsstrings aus Quellen aufrufen. Python-Playwright ist im Standard-Python dieser Umgebung nicht installiert. Browserprüfungen dieses Pilots verwenden die vorhandene Browseranbindung; vollständige automatisierte Ende-zu-Ende-Tests sind nicht behauptet.

Der Vercel-Skill lädt eine weitere offizielle Richtliniendatei zur Laufzeit. Deren geprüfter Stand und die vollständigen Paket-Hashes stehen in [external-skills.lock.json](external-skills.lock.json). Das Vercel-Quellrepository nennt MIT im README; da eine separate Lizenzdatei fehlt, wurde dieser originale Hinweis beigefügt. Die übrigen Pakete enthalten MIT- bzw. beim Anthropic-Testskill Apache-2.0-Lizenztexte.

Superpowers und der kleine i18n-Nischenkandidat bleiben optional und wurden nicht installiert: Der aktuelle Bedarf ist durch gezielte Fachskills und die ausgewählten Ergänzungen abgedeckt.
