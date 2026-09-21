# Vermittlungsversprechen an belegte Verfügbarkeit koppeln (Issue #1, Fokus Nairobi)

**Datum:** 2026-09-21
**Rolle:** Vermittlung und Aktivierung (Vermittlungs_Operator)
**Geprüfte Quellen (lokal, Stand 2026-09-21):** `index.html`, `hire.html`, `request.html`, `members.html`, `assets/website-copy.js`, `assets/i18n/en.js`, `assets/scout-copy.js`, `assets/network.js`, `electricians-nairobi.html`, `solar-installers-nairobi.html`, `rankings.html`, `profile.html`, `supabase-setup.sql`, `supabase/functions/instant-match/index.ts`, `supabase/migrations/20260724_instant_match_trigger.sql`
**Hinweis zu Zeilenangaben:** `index.html`, `hire.html`, `members.html` sind minifiziert (gesamtes Dokument in Zeile 1). Dort wird mit Element + `data-i18n`-Schlüssel zitiert; `request.html` ist mehrzeilig und wird mit echten Zeilen zitiert.

---

## 1. Zusammenfassung

Die aktuelle öffentliche Website (Rebuild, Asset-Version `v=20260915`) ist in ihren Fließtexten überraschend vorsichtig: Verfügbarkeits-Vorbehalte („Availability varies by location", „Coverage depends on the local network", „submitting a request does not guarantee a match") sind auf allen geprüften Seiten vorhanden; Mitglieder- und Ranking-Verzeichnisse sind bewusst unveröffentlicht (Pause-Seiten). **Das verbleibende Risiko liegt nicht in Einzelsätzen, sondern in der Versprechenskette:** Navigation („Find a technician"), Seitentitel, Hero-Aussage und 20+ Stadt-Gewerke-Seiten (z. B. „Electricians in Nairobi (2026)") suggerieren gemeinsam eine auffindbare, flächendeckende Abdeckung, für die es keine belegten Daten gibt. Technisch verschärft wird das durch drei Befunde: (1) Das Instant-Matching filtert nur auf **Land**, nicht auf Stadt; (2) `availability` ist ein **selbst gesetztes Profil-Flag mit Default „available"** (`profile.html:287`) ohne Verifikation oder Aktivitätsnachweis; (3) bei null Kandidaten bleibt die Anfrage kommentarlos auf Status `new` — kein Wartelisten-Pfad, keine automatisierte Eskalation. Konsequenz: Selbst die vorsichtigen Texte sind aktuell nicht an echte Verfügbarkeit gekoppelt. Dieser Bericht liefert Inventar, Risiko-Bewertung, Kopplungs-Konzept (Texte/Technik/Ops) und den Nairobi-Aktivierungsplan.

---

## 2. Versprechens-Inventar mit Code-Belegen

### A. Die vier Hauptseiten (12 Aussagen)

| # | Datei / Stelle | Wortlaut (EN, Original) | Versprechen-Typ |
|---|---|---|---|
| V1 | `index.html` Z. 1, `<title>` + og:title | „Find technical skills for your project \| Voltage Africa" | Auffindbarkeit |
| V2 | `index.html` Z. 1, meta description | „Request solar, electrical, network and IT support in Africa. A clear process for customers and technicians." | Geografische Breite („in Africa") |
| V3 | `index.html` Z. 1, Nav, `data-i18n="web_hire"` (auf allen Seiten) | „Find a technician" | Auffindbarkeit (produktdefinierend) |
| V4 | `index.html` Z. 1, Hero, `home_title` | „Good work starts with the right technician." | Implizit: der richtige Techniker ist erreichbar |
| V5 | `index.html` Z. 1, Hero, `home_desc` | „Connect with technical skills for your project in Africa. Tell us where you are and what needs doing." | Verbindungszusage („Connect with") |
| V6 | `index.html` Z. 1, Prozess, `step1_t`/`step1_d` | „We check the fit — Your request helps us assess skills, location and availability. Coverage depends on the local network." | Prüfzusage **mit** Abdeckungsvorbehalt |
| V7 | `index.html` Z. 1, `home_note` | „Free to submit · No customer account needed" | Kosten/Friction (sagbar) |
| V8 | `hire.html` Z. 1, `hire_desc` | „Start with your project. We use your location and the work required to check for a suitable connection." | Prüfzusage, weich („check for") |
| V9 | `hire.html` Z. 1, `hire_note` | „Availability varies by location. Your request is free; you agree the work and price directly with the technician." | Vorbehalt + Klarstellung (sagbar) |
| V10 | `request.html` Z. 8/16/21, meta/og/twitter description | „Describe your project, location and contact details to request a technician. Local availability varies." | Vorbehalt (sagbar) |
| V11 | `request.html` Z. 44, `rq_sub` | „Tell us the location and work required. Availability depends on the local network." | Vorbehalt (sagbar) |
| V12 | `request.html` Z. 86, `rq_success_d` | „Our team can now review your request. Availability and response times vary. Keep your project details for any follow-up." | Review-Zusage **ohne** Abdeckungssignal |

Zusätzlich festgestellt: `members.html` zeigt nur die Pause-Meldung „This section is not currently published. You can request a technician or create your profile." (`pause_desc`) — **kein** Mitgliederzähler, keine Verfügbarkeitsanzeige. Ebenso `rankings.html`. Auf keiner der vier Seiten existiert ein Live-Zähler oder eine Verfügbarkeits-Anzeige.

### B. Kontextfunde außerhalb der vier Seiten (relevant für Issue #1)

| # | Datei / Stelle | Wortlaut | Bewertung |
|---|---|---|---|
| K1 | `electricians-nairobi.html`, `solar-installers-nairobi.html` (+ 18 weitere Stadt-Gewerke-Seiten), `<h1>` | „Electricians in Nairobi (2026)" / „Solar Installers in Nairobi (Kenya)" | Seitentitel + schiere Existenz implizieren Anbieterpräsenz in Nairobi. Fließtext enthält Disclaimer: „submitting a request does not guarantee a match". |
| K2 | `assets/i18n/en.js` Z. 3 (Legacy-App-i18n) | „Africa's technicians. Ranked. Visible. Hired.", „🌍 Pan-African · Live rankings", „across 54 countries", „Verified technicians", „Free matching SLA", „get found by companies worldwide. Free for technicians, forever." | Starke, unbelegte Claims. Auf den geprüften öffentlichen Seiten aktuell **nicht gerendert** (rankings/members = Pause-Seiten), aber im Code lebendig → Risiko bei jeder Reaktivierung. „Verified technicians" als stat-Label ohne Verifikationsnachweis. |
| K3 | `assets/scout-copy.js` Z. 2 | „sc_free": „Free account · Local relationships · No guaranteed earnings" | Vorbildlich ehrlich; zeigt, dass der Ton im System bereits verankert ist. |

### C. Technische Belege (Anfrage- und Matching-Weg)

- `request.html` Z. 124: Netzwerk-Routing prüft `n.accepting` und deaktiviert das Formular bei unveröffentlichtem Netzwerk — ein ehrlicher Mechanismus, der aber nur für Scout-Netzwerk-Links greift, nicht für die normale Anfrage.
- `supabase/migrations/20260724_instant_match_trigger.sql` Z. 76–80: `AFTER INSERT`-Trigger auf `requests` ruft `instant-match` via `pg_net` auf.
- `supabase/functions/instant-match/index.ts` Z. 162–170: Kandidatenauswahl = gleiches Gewerk (`spec`), gleiches **Land** (`country`), `availability = 'available'`, Top 3 nach XP. **Kein Stadtfilter, kein Aktivitäts-/Verifikationsfilter.**
- Ebenda Z. 175–179: Bei null Kandidaten ehrliche Leermeldung `{ok:true, matched:0, reason:"no_candidates"}` — Request bleibt auf `new`. Kein Wartelisten-Eintrag, keine Eskalation, keine Kundeninformation.
- `supabase-setup.sql` Z. 7–17: Tabelle `profiles` hat **keine** Spalten `city`, `availability`, `verified`, `last_seen_at` (nur `country`, `spec`, `xp`, …). `profile.html` Z. 287/450/465 zeigt: `availability` wird clientseitig gepflegt, Default `"available"`.
- `requests`-Tabelle (Z. 73–96) hat `country` + `city` und Index `requests_country_idx (country, city)` — die Infrastruktur für Stadt-Level-Denken existiert auf der **Nachfrage**seite, nicht auf der **Angebots**seite.

---

## 3. Risiko-Bewertung je Aussage

| # | Risiko ohne Abdeckungsdaten | Urteil |
|---|---|---|
| V3 „Find a technician" (Nav, alle Seiten) | Produktdefinierendes Versprechen eines **Ergebnisses** (finden), geliefert wird ein **Prozess** (anfragen). Bei unbekannter Abdeckung statistisch häufig uneinlösbar → Enttäuschung, Support-Last, Reputationsrisiko. | **Problematisch — riskanteste Einzelaussage** |
| V1 „Find technical skills…" (Titel) | Wie V3, zusätzlich SEO-/Social-Sichtbarkeit (og:title). | Problematisch |
| V4 „…the right technician." | Impliziert Verfügbarkeit des Passenden; ohne Abdeckung nicht einlösbar, aber als Werbe-Slogan vertretbar, wenn Umgebung ehrlich bleibt. | Mittel |
| V5 „Connect with technical skills … in Africa" | Verbindungszusage + Pan-Afrika-Breite; unbelegt. | Mittel |
| V2 „…support in Africa" | Geografische Breite ohne Einschränkung; durch Vorbehalte auf derselben Seite teilweise gedeckt. | Mittel (mit Vorbehalt sagbar) |
| K1 „Electricians in Nairobi (2026)" | Seitentitel ist eine Existenzbehauptung. Disclaimer im Fließtext mildert, aber: Wer keine Elektriker in Nairobi hat, sollte die Seite nicht wie ein Verzeichnis wirken lassen. SEO zieht genau die Nachfrage an, die man nicht bedienen kann. | **Problematisch (implizit)** |
| V6/V8 „We check the fit / check for a suitable connection" | Prüfzusage statt Ergebniszusage; mit Vorbehalt versehen. Sagbar, solange die Prüfung tatsächlich stattfindet (Ops-Playbook nötig, sonst Lippenbekenntnis). | Sagbar* |
| V9/V10/V11 Vorbehalte | Explizit ehrlich. | Sagbar |
| V12 Success-Message | Textlich vorsichtig, aber: Der Kunde erfährt nach dem Absenden nicht, ob in seiner Stadt überhaupt jemand ist. Prozessrisiko (Warten ins Leere), kein Textrisiko. | Sagbar, prozessual lückenhaft |
| V7 „Free to submit · No customer account needed" | Faktisch prüfbar und zutreffend laut Code (kein Account im Request-Flow). | Sagbar |
| K2 Legacy-i18n-Claims | „Ranked. Visible. Hired.", „54 countries", „Verified technicians", „Free matching SLA" wären ohne Datenlage **klar unzulässig**. Aktuell nicht gerendert — aber kein Schutzmechanismus verhindert die Reaktivierung. | Nicht live, sperren |
| K3 Scout-Copy | Ehrlich. | Sagbar |

**Zwischenfazit:** 12 inventarisierte Aussagen auf den Hauptseiten + 3 Kontextfunde. Die riskanteste **aktive** Zeile ist V3 „Find a technician", weil sie auf jeder Seite als primärer CTA das Ergebnis verspricht; die riskanteste **implizite** Aussage ist K1 (Stadt-Verzeichnisse). Kein einziger aktiver Text verspricht aktuell Geschwindigkeit („in minutes") — das ist gut und sollte so bleiben.

---

## 4. Kopplungs-Konzept

### 4a. Ehrliche Textalternativen (Englisch, einsetzbar)

| Ersetzt | Alternative (EN) |
|---|---|
| V3 Nav „Find a technician" | **„Request a technician"** — beschreibt die echte Handlung. (Primärempfehlung) |
| V1 Titel | „Request technical skills for your project \| Voltage Africa" |
| V4 Hero | „Good work starts with the right request. Tell us where and what — we'll check who's available." |
| V5 Hero-Sub | „We connect projects with technicians where our network is live — and tell you honestly where it isn't yet." |
| K1 Stadtseiten-Titel (dünn besetzt) | „Electricians in Nairobi — we're building this network" statt Verzeichnis-Anmutung |
| Neuer Verfügbarkeits-Badge (nur bei ≥ N Technikern) | „Live in Nairobi: electricians available now" (ohne erfundene Zahl; optional mit echter Zahl: „7 verified electricians in Nairobi") |
| Wartelisten-Modus Kunde | „We're still building {city}. Join the waitlist and we'll message you on WhatsApp as soon as a technician is available." |
| Wartelisten-Modus Techniker | „Be the first {trade} in {city} — create your free profile." |
| V12 Success-Message (dünne Stadt) | „Your request is saved. We're still growing in {city} — our team will message you within 2 working days, either with a technician or an honest update." |

### 4b. Technischer Vorschlag: Coverage-Gate mit Schwellwert N

**Ziel:** Eine Verfügbarkeits-Anzeige erscheint nur, wenn **≥ N (empfohlen N = 3)** aktive Techniker in Stadt × Gewerk belegt existieren; darunter schaltet die Anfrage-Seite in den Wartelisten-Modus.

**1. Datenmodell erweitern (Migration):**

```sql
alter table public.profiles
  add column if not exists city text not null default '',
  add column if not exists verified boolean not null default false,
  add column if not exists last_seen_at timestamptz;
-- availability existiert clientseitig bereits; serverseitig absichern:
alter table public.profiles
  add column if not exists availability text not null default 'available'
  check (availability in ('available','unavailable'));
-- last_seen_at bei Login/Nachrichten-Action serverseitig setzen (nicht clientsetzbar)
```

**2. Aggregierte Coverage-View (k-anonym, keine Personendaten):**

```sql
create or replace view public.city_trade_coverage as
select country, city, spec,
       count(*) as active_technicians
from public.profiles
where role = 'tech'
  and availability = 'available'
  and city <> ''
  and last_seen_at > now() - interval '30 days'
group by country, city, spec
having count(*) >= 3;          -- Schwellwert N=3: Städte < N erscheinen gar nicht
```

**3. Abfrage-Logik (Edge Function `coverage-status`, öffentlich, nur Aggregate):**

```ts
// GET /coverage-status?country=KE&city=Nairobi&spec=electric
// Antwort: { status: "live", count: 7 }  |  { status: "building" }
// "building" wird zurückgegeben, wenn kein View-Treffer (< N) — die
// tatsächliche Zahl bleibt unter N absichtlich verborgen (kein "0 Techniker"-Signal).
```

**4. Frontend-Verhalten `request.html`:** Nach Auswahl Land/Stadt/Gewerk → `coverage-status` abfragen →
- `live`: Hinweisbadge „Technicians available in {city}", normales Formular.
- `building`: Formular wechselt zu Warteliste (Insert in neue Tabelle `waitlist(country, city, spec, contact, created_at)`) + Technician-CTA „Be the first…". **Kein** stiller Standard-Submit mehr.

**5. Instant-Match verschärfen:** Stadtfilter vor Landfilter (`city` match, Fallback `country`), zusätzlich `verified = true` und `last_seen_at > now() - interval '30 days'`; bei `matched:0` zusätzlich Wartelisten-Insert + Ops-Notification (wa.me an Ops-Dienstnummer, gleiches Muster wie bestehende Tech-Links).

### 4c. Ops-Playbook: Anfrage in dünn besetzter Stadt

| Schritt | Wer | Was | SLA (Vorschlag) |
|---|---|---|---|
| 1. Eingang | System | Anfrage in `requests`; Trigger feuert; `instant-match` → `matched:0`, Request bleibt `new`, Wartelisten-Eintrag | sofort |
| 2. Sichtung | Ops (tägliche Zero-Match-Liste, SQL: `status='new' and created_at < now() - interval '1 day'`) | Stadt × Gewerk bewerten: gibt es inaktive/unverifizierte Profile, die aktivierbar sind? | 1 Werktag |
| 3. Aktivierung | Ops → Scout der Stadt (WhatsApp) | Scout kontaktiert bekannte Techniker vor Ort, hilft bei Profil + Verfügbarkeits-Flag; parallele Neurekrutierung | 2 Werktage |
| 4a. Erfolg | Ops | Techniker wird gematcht (Re-Run `match_request` mit derselben `request_id` — Funktion ist idempotent), Kunde wird informiert | — |
| 4b. Kein Erfolg | Ops | Ehrliche Kunden-Nachricht (WhatsApp, Vorlage): „We couldn't find an available {trade} in {city} yet. We've saved your request and will message you as soon as someone is available. No cost, no obligation." Angebot: Warteliste oder Anfrage schließen | 5 Werktage |
| 5. Eskalation | Ops-Lead | ≥ 3 Zero-Match-Anfragen in derselben Stadt × Gewerk in 30 Tagen → Stadt offiziell auf „building" setzen (Coverage-Gate), Stadtseiten-Text anpassen, ggf. Scout-Priorität erhöhen | wöchentliche Review |

Prinzipien aus dem Matching-Skill bleiben verbindlich: Treffer ≠ Kontakt ≠ Antwort ≠ Annahme ≠ bestätigter Abschluss; keine Phantom-Anbieter; Lücke kommunizieren statt falscher Sofortzusage.

---

## 5. Nairobi-Aktivierungsplan (bis das Versprechen ehrlich sagbar ist)

**Definition „ehrlich sagbar":** Für mindestens ein Gewerk in Nairobi gilt ≥ N = 3 verifizierte, als verfügbar markierte, in den letzten 30 Tagen aktive Techniker, und eine Probe-Anfrage wurde innerhalb von 2 Werktagen mit echter Antwort bedient.

1. **Ist-Datenlage messen (Tag 1–2).** SQL gegen Supabase: `select spec, availability, count(*) from profiles where country='KE' group by 1,2;` plus Prüfung, ob Nairobi überhaupt als `city`/Region erfasst ist (aktuell keine Stadt-Spalte → Ergebnis dokumentieren, auch wenn es „unbekannt" lautet).
2. **Datenmodell nachrüsten (Tag 3–7).** Migration wie 4b (city, verified, last_seen_at, availability serverseitig); Backfill: bestehende KE-Profile manuell/per Formular der Stadt zuordnen; `last_seen_at` initial auf `created_at`, danach bei Login setzen.
3. **Coverage-View + Gate deployen (Woche 2).** View und `coverage-status`-Function wie 4b; request.html-Gate aktivieren — ab diesem Punkt ist die Website technisch an echte Verfügbarkeit gekoppelt (für alle Städte, nicht nur Nairobi).
4. **Scout-Aktivierung Nairobi (Woche 2–4).** 1 verantwortlichen Scout für Nairobi benennen (Netzwerk-Feature `va_public_network` existiert bereits in request.html). Rekrutierungsziel: ≥ 5 Elektriker + ≥ 3 Solarinstallateure mit vollständigem Profil (Name, Stadt, Gewerk, Projektfotos, Telefon in `profile_private`), jeden mit eigener E-Mail registriert.
5. **Verifizierung (parallel).** Pro Profil: Identitätssichtung, mindestens eine Referenz/ein Projektbeleg; für Elektriker in Kenia die einschlägige lokale Berufszulassung (z. B. EPRA-Lizenz) **anhand amtlicher Quelle prüfen lassen** — keine Pauschalbehauptung „verified" ohne diesen Schritt. Erst danach `verified = true`.
6. **Probebetrieb (Woche 5).** 3–5 interne Testanfragen über request.html (Stadt Nairobi, beide Gewerke); messen: Match erzeugt? WhatsApp-Link beim Ops-Team? Antwortzeit des Technikers? Ergebnis nach Trennung Treffer/Kontakt/Antwort/Annahme dokumentieren.
7. **Freischaltung (Woche 5–6).** Erst bei erfülltem Kriterium: Coverage-Badge „Live in Nairobi" sichtbar, Stadtseiten-Text von „we're building" auf „live" umstellen, SEO-Titel beibehalten (jetzt belegt).
8. **Dauer-Monitoring.** Wöchentliche Coverage-Abfrage; fällt Nairobi < N, Badge automatisch aus und Wartelisten-Modus an (Gate macht das ohne manuellen Eingriff). Erkenntnisse nach `voltage-learning` dokumentieren.

---

## 6. Die 3 nächsten Maßnahmen

1. **Ist-Abdeckung messen (diese Woche):** Coverage-SQL aus 5.1 gegen Supabase ausführen (Kenya + Top-10-Städte), Ergebnis als Beleg-Anhang zu Issue #1 kommentieren — danach ist bekannt, welche Versprechen wo haltbar sind.
2. **Text-Patch (klein, sofort umsetzbar):** `web_hire` „Find a technician" → „Request a technician" in `website-copy.js` (alle 5 Sprachen analog), Seitentitel `index.html`/`hire.html` entsprechend; Legacy-Claims in `assets/i18n/en.js` (K2) als „nicht reaktivieren ohne Abdeckungsdaten" markieren oder entfernen.
3. **Coverage-Gate spezifizieren und bauen (Sprint):** Migration + View + `coverage-status`-Function + request.html-Wartelisten-Modus wie 4b umsetzen; damit entsteht der technische Rahmen, in dem das Nairobi-Versprechen nach Plan (Abschnitt 5) ehrlich freigeschaltet werden kann.

---

*Erstellt nach docs/SENIOR-STANDARD.md. Alle Aussagen über Code belegen Datei und Stelle; Aussagen über tatsächliche Verfügbarkeit wurden nicht behauptet, da keine Abdeckungsdaten abgefragt wurden (kein Backend-Zugriff in diesem Lauf). Das GitHub-Issue #1 selbst wurde nicht remote gelesen; Grundlage ist das Briefing.*
