# GitHub-Recherche: Agenten und Skills für beide Projekte

Stand: 2026-09-10. Geprüft wurden Projektbeschreibungen und bei den priorisierten Kandidaten konkrete SKILL.md-Dateien. Popularität ist ein Orientierungssignal, kein Qualitäts- oder Sicherheitsnachweis. Installationszahlen stammen aus [skills.sh](https://www.skills.sh/); GitHub-Sterne aus den jeweils verlinkten Repositoryseiten, gerundet und als Momentaufnahme.

## Priorisierte Kandidaten

| Repository | Konkreter Nutzen für BESS-Market | Konkreter Nutzen für Voltage Africa | Auswahl / Grenzen |
|---|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Conversion von Fachartikeln und Tools zu qualifizierten Projektanfragen | Anmeldung, Profilaktivierung, lokale Anfrageformulare | Erste Priorität für gezielte Ergänzung. MIT; ca. 49,3k Sterne. seo-audit ca. 204,4k Installationen. Bestehende BESS-Skills decken SEO bereits ab; besonders cro, signup und onboarding prüfen. |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | UX-Prüfung von Astro-Seiten und React-Komponenten | Oberflächen-, Formular- und Mobilprüfung im HTML/JS-Projekt | web-design-guidelines passt zu beiden. MIT; ca. 31k Sterne; dieser Skill ca. 622,3k Installationen. React-Regeln nur bei tatsächlichen React-Komponenten, keine Next.js-Migration erforderlich. |
| [anthropics/skills](https://github.com/anthropics/skills) | Tests für Konfigurator und Anfragewege | Tests für Suche, Sprachen, Profile und Formulare | webapp-testing ist ein passender Testkandidat, ca. 153,5k Installationen. Python/Playwright erforderlich. Lizenz der konkreten Dateien prüfen; webapp-testing verweist auf Apache-2.0-Lizenzdatei. Repositoryweiter Sternwert hier nicht zuverlässig erhoben. |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | Nur bei beauftragter Supabase/Postgres-Arbeit; für die aktuelle statische Website nicht pauschal nötig | Hohe Passung zu Supabase, Profilzugriffen und Datenbankabfragen | supabase-postgres-best-practices. MIT; ca. 2,6k Sterne; ca. 394,4k Installationen. Referenzpaket vollständig prüfen; keine RLS-/Produktivmigration durch Installation. |
| [obra/superpowers](https://github.com/obra/superpowers) | Methodische Fehlersuche bei Website-Problemen | Ursachenanalyse für dynamische UI- und Backendfehler | Optional einzelne Debugging-/Verifikationsskills, kein Komplettframework. MIT; ca. 284,3k Sterne; systematic-debugging ca. 254,3k Installationen. Enthält weitreichende Prozessvorgaben, die mit bestehenden Abläufen überlappen können. |

## Konkrete Inhaltsprüfung

- [Marketing: cro/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/main/skills/cro/SKILL.md): prüft Seitenziel, Nutzenverständnis, Handlungsaufforderung und Formularhürden. Wichtig: v2 verwendet cro; page-cro und form-cro wurden zusammengeführt. Aktuelle Namen vor Übernahme prüfen.
- [Vercel: web-design-guidelines/SKILL.md](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md): lädt eine externe Richtliniendatei. Diese Abhängigkeit gehört zur Prüfung; der Skill allein enthält nicht alle Regeln.
- [Anthropic: webapp-testing/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md): beinhaltet lokale Browser-Tests und einen Server-Helfer. Vor späterem Einsatz auch Helferquellcode und Abhängigkeiten prüfen. Kein Testlauf fand während dieser Recherche statt.
- [Supabase: supabase-postgres-best-practices/SKILL.md](https://github.com/supabase/agent-skills/blob/main/skills/supabase-postgres-best-practices/SKILL.md): verweist auf eigene Referenzen für Datenmodell, Abfragen und Zugriffskontrolle. Fachlich gut passend zur lokal vorhandenen Voltage-Supabase-Struktur.
- [Superpowers: systematic-debugging/SKILL.md](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md): reproduzieren und Ursache eingrenzen vor Korrektur. Prozesszwang nicht ungeprüft auf reine Content-Aufträge übertragen.

## Enger Nischenkandidat

[adamgrgs/i18n-agent](https://github.com/adamgrgs/i18n-agent) bietet laut README Mehrsprachigkeits- und hreflang-Prüfungen. Inhaltlich interessant für Voltage Africa, MIT, aber nur zwei Sterne und sieben Commits zum Abrufzeitpunkt; Installationszahl nicht verlässlich erhoben. Noch keine Empfehlung zur direkten Übernahme: nur beobachten, Code und Prüffälle zuerst untersuchen. Der lokale voltage-localization-Skill deckt den unmittelbaren Bedarf ohne diese Abhängigkeit ab.

## Tatsächlich übernommen

Für Voltage Africa wurden aus der bereits vorhandenen MIT-Sammlung Agency Agents fünf zusätzliche Rollen übernommen: Support, Nutzerfeedback, Barrierefreiheit, Application Security und Community/Social. Drei eigene Rollen ergänzen Vermittlung, Lokalisierung und Vertrauensprüfung. Alle haben einen eigenen Voltage-Fachskill.

Die hier recherchierten weiteren Repositories sind noch nicht installiert. BESS-Market erhält diesen Recherchebericht; seine aktiven Rollen und Skills wurden durch die Recherche nicht ersetzt.

## Empfohlene Reihenfolge

1. Beide Projekte: gezielte Conversion- und UX-Erprobung an je einem vorhandenen Nutzerweg.
2. Voltage Africa: lokal/staging Testfälle für Profil, Suche und Anfrage sowie Supabase-Zugriffskontrolle.
3. Erst nach Ergebnissen weitere Spezialskills ergänzen; keine vollständigen Sammlungen allein wegen hoher Sternezahl laden.

Vor späterem Import konkrete Dateien und unterstützende Ressourcen lesen, Lizenz erhalten, Commit festhalten, eine lokale Kopie mit klarer Rolle zuordnen und an einem begrenzten Testfall prüfen. Installer, Hooks und automatische Updates wurden nicht ausgeführt.

Beispiel zur späteren Auswahl, nicht während dieser Recherche ausgeführt:

```text
npx skills add coreyhaines31/marketingskills --skill cro
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

Die Auswahl ergänzt die bestehenden projektspezifischen Skills; sie belegt keine Marktführerschaft oder garantierte Wirkung.

## Nachtrag: Installation

Die ausgewählten Pakete wurden inzwischen installiert. Der aktuelle Umfang und die Herkunftsnachweise stehen in [INSTALLED-SKILLS.md](INSTALLED-SKILLS.md); die obigen Nicht-installiert-Angaben beschreiben den früheren Recherchezeitpunkt.
