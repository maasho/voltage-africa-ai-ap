---
name: voltage-appsec
description: Prüft beauftragte Voltage-Africa-Code- und Datenzugriffe mit Fokus auf Supabase und Mitgliederdaten.
---

# Profil- und Zugriffsschutz

Lies den [Website-Kontext](../../../docs/WEBSITE-CONTEXT.md) und das konkrete Briefing. Verfügbare Daten und Werkzeuge vor Verwendung prüfen.

## Vorgehen

Erfasse Datenklassen, Rollen und erlaubte Zugriffe auf Profile, Nachrichten, Uploads, Bewertungen und Punktevergabe. Prüfe Autorisierung serverseitig einschließlich RLS und Storage; UI-Verbergen genügt nicht. Verwende zwei getrennte Testkonten und verweigerte Zugriffe im autorisierten lokalen/Staging-Umfeld. Keine Live-Angriffe oder echten fremden Datenzugriffe. Geheimnisse nicht ausgeben; offene Befunde privat behandeln. Datenbankänderungen nur mit Auftrag, Migration und Rückweg. Ohne Backendzugriff statischen Befund als solchen markieren.

## Abnahme

Erlaubte und verbotene Zugriffe haben Nachweise; keine pauschale Sicherheitsfreigabe.

Aktuelle Aussagen mit [Quellenprüfung](../voltage-evidence/SKILL.md) belegen. Substanzielle Erkenntnisse nach [Lernprozess](../voltage-learning/SKILL.md) dokumentieren. Keine Hintergrundausführung oder gemessene Wirkung ohne tatsächlichen Nachweis behaupten.
