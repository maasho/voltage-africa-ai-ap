# Vermittlungs-KPI-Framework für Voltage Africa

**Rolle:** KPI_Analytics (Analytics Reporter) · **Datum:** 2026-09-21 · **Sprache:** Deutsch (intern)

**Datengrundlage dieses Entwurfs:** lokal beobachtetes Supabase-Schema (`supabase-setup.sql`, `supabase/migrations/*`, `supabase/scout-*.sql`) und der belegte Website-Kontext. Es wurden **keine produktiven Ist-Zahlen abgefragt** — alle Schwellen sind Startwerte/Frühwarn-Hypothesen, die nach 4 Wochen Baseline-Messung zu kalibrieren sind. Website-Texte (about.html, terms.html) belegen kommunizierte Claims, keine betriebliche Umsetzung.

---

## 1. Zusammenfassung

Voltage Africa hat heute ein erstaunlich sauberes Transaktions-Rückgrat in der Datenbank (requests → matches → projects/reviews → xp/vip-Events), aber **keinen Seitenaufruf-/Besucher-Tracking** und keine automatisierte Auswertung. Konsequenz:

- **Messbar heute (SQL-only):** alles ab „Anfrage" (requests) bis „bestätigte Vermittlung" sowie die gesamte Angebotsseite (Techniker, Scouts, Verifikation, Vouches, XP/VIP, Referrals).
- **Nicht messbar heute:** Website-Besuche, Trichter-Schritte vor der Registrierung, Kunden-Identität als Entität (requests haben kein `customer_id`-Feld), Wiederkehr-Rate der Nachfrageseite, Kanal-Attribution.
- **Empfohlener Nordstern:** **Wöchentlich bestätigte Vermittlungen** (s. Definition unten) — segmentiert nach Stadt × Gewerk.

Das Framework trennt konsequent Nachfrage- und Angebotsseite, dedupliziert Vorgänge (ein Request = ein Vorgang, `reviews.request_id UNIQUE` hilft dabei) und dokumentiert Lücken statt Nullen zu berichten (gemäß Skill `voltage-marketplace-analytics`).

---

## 2. Nordstern-KPI + Trichter

### 2.1 Nordstern-KPI

**Nordstern: Bestätigte Vermittlungen pro Woche (BCV)**

> Anzahl der `requests`, die in einer Kalenderwoche den Status `completed` erreichen **und** mindestens einen Beleg haben (verknüpfte Bewertung **oder** bestätigtes Projekt eines zugeordneten Technikers). Segment: Stadt × Gewerk (`requests.city`, `requests.spec`).

**Warum dieser Nordstern:** Eine versandte Anfrage ist kein Auftrag; ein gematchter Techniker ist kein abgeschlossener Auftrag; XP sind kein Umsatz. Erst `completed` + unabhängiger Beleg (Review oder bestätigtes Projekt) nähert sich realer Wertschöpfung. Das ist die vom Website-Kontext vorgeschlagene Zielgröße „bestätigte Vermittlungen pro Stadt/Gewerk" — operationalisiert.

**Bekannte Schwäche:** Es gibt im Schema **keine explizite Verknüpfung** zwischen `projects`/`matches` als Auftrags-Beleg pro Request. Bis dahin ist die Review-Verknüpfung (`reviews.request_id`) der stärkste Beleg-Anker.

### 2.2 Trichter — Nachfrageseite (Kunden)

| Stufe | Ereignis | Messbar heute? |
|---|---|---|
| N1 Besuch | Seitenaufruf (hire.html, Stadt-/Gewerksseiten) | ❌ kein Web-Tracking |
| N2 Anfrage eingereicht | INSERT in `requests` | ✅ |
| N3 Gültige Anfrage | Request mit valider E.164-Kontaktnummer, nicht Spam | 🟡 teilweise (Format-Check vorhanden, Spam-Flag fehlt) |
| N4 Vermittlung angeboten | ≥1 `matches`-Zeile zum Request | ✅ |
| N5 Techniker akzeptiert | `matches.status = 'accepted'` | ✅ |
| N6 Beauftragt | `matches.status = 'hired'` / `requests.status = 'hired'` | ✅ |
| N7 Auftrag abgeschlossen | `requests.status = 'completed'` | ✅ |
| N8 Bewertet | Review zum Request | ✅ |
| N9 Wiederkehr / Referral (Kunde) | zweiter Request derselben Kontaktnummer | 🟡 nur über `contact`-Hash ableitbar, kein Kundenkonto |

### 2.3 Trichter — Angebotsseite (Techniker & Scouts)

| Stufe | Ereignis | Messbar heute? |
|---|---|---|
| A1 Registrierung | INSERT in `profiles` (via auth-Trigger) | ✅ |
| A2 Vollständiges Profil | `xp_events.event_type = 'profile_completed'` (Whitelist-Event, 5 XP) | 🟡 nur wenn die Vergabe tatsächlich ausgelöst wird — **im Code verifizieren** |
| A3 Verifiziert | `verifications.status = 'approved'`, Stufen 1–4 | ✅ |
| A4 Aktiv/verfügbar | (kein Verfügbarkeits-/Online-Status im Schema) | ❌ |
| A5 Match-Angebot | `matches.status = 'offered'` | ✅ |
| A6 Auftrag gewonnen | `matches.status = 'hired'` | ✅ |
| A7 Auftrag belegt | `projects.confirmed_by IN ('client','scout')` | ✅ |
| A8 Bewertet | `reviews` zum Techniker | ✅ |
| A9 Referral | `referrals`-Zeile + `xp_events 'referral_bonus'` | ✅ |
| S1 Scout-Vouch | `vouches.status = 'active'` | ✅ |
| S2 Scout-Placement | `vip_events.event_type = 'placement'` | 🟡 nur wenn Vergabe läuft |

---

## 3. KPI-Katalog mit SQL-Skizzen

Konventionen: Woche = ISO-Kalenderwoche (`date_trunc('week', created_at)`), Zeitraum-Filter `:week_start`. Alle Abfragen laufen als service role / SQL-Editor, da `requests` und `matches` **keine** öffentlichen SELECT-Policies haben (korrekt so — sie enthalten Personendaten). Keine persönlichen Kontaktdaten in Berichten; nur Aggregate.

### Nachfrageseite

**KPI 1 — Neue Anfragen pro Woche (N2)**
- Definition: INSERTs in `requests` pro Woche, nach Stadt × Gewerk.
- Warum: oberste echte Nachfrage-Signal; Input für Matching-Kapazität.
- SQL:
```sql
select city, spec, count(*) as requests_new
from public.requests
where created_at >= :week_start and created_at < :week_start + interval '7 days'
group by 1,2 order by 3 desc;
```
- Frühwarnung: WoW-Rückgang > 30 % in einer Stadt mit vorher ≥ 10 Anfragen/Woche; oder 2 Wochen in Folge 0 Anfragen in einer beworbenen Stadt.

**KPI 2 — Anfrage-zu-Match-Quote (N4/N2)**
- Definition: Anteil der Requests mit ≥ 1 Match-Angebot innerhalb von 72 h.
- Warum: Kernversprechen „Instant Matching" — misst, ob die Edge Function + Technikerbasis liefern.
- SQL:
```sql
select r.city, r.spec,
       count(*) as requests,
       count(m_first.request_id) as matched,
       round(100.0 * count(m_first.request_id) / count(*), 1) as match_rate_pct,
       avg(extract(epoch from (m_first.first_match_at - r.created_at))/3600.0)::numeric(10,1) as hours_to_first_match
from public.requests r
left join lateral (
  select request_id, min(created_at) as first_match_at
  from public.matches m where m.request_id = r.id group by 1
) m_first on true
where r.created_at >= :week_start and r.created_at < :week_start + interval '7 days'
group by 1,2;
```
- Frühwarnung: `match_rate_pct < 50 %` oder Median-Zeit bis erstes Match > 24 h in einer Stadt → Angebotsseite dort dünn.

**KPI 3 — Annahmequote der Techniker (N5/N4)**
- Definition: `matches.status = 'accepted'|'hired'` ÷ alle angebotenen Matches.
- SQL:
```sql
select date_trunc('week', created_at) as week,
       count(*) filter (where status in ('accepted','hired')) as accepted,
       count(*) as offered,
       round(100.0 * count(*) filter (where status in ('accepted','hired')) / count(*),1) as accept_rate_pct
from public.matches
group by 1 order by 1 desc limit 8;
```
- Frühwarnung: Quote < 30 % → Match-Qualität oder Techniker-Aktivität prüfen. Hohe `declined`-Quote nach Stadt × spec aufschlüsseln.

**KPI 4 — Beauftragungsquote (N6/N2) und Abschlussquote (N7/N2)**
- Definition: Requests mit Status `hired` bzw. `completed` ÷ alle Requests der Kohorte (Kohorten-Logik! Nicht gleiche Woche — Abschluss braucht Zeit).
- SQL (Kohorten-View):
```sql
select date_trunc('week', created_at) as cohort_week,
       count(*) as requests,
       count(*) filter (where status in ('hired','completed')) as hired,
       count(*) filter (where status = 'completed') as completed,
       round(100.0*count(*) filter (where status in ('hired','completed'))/count(*),1) as hire_rate_pct,
       round(100.0*count(*) filter (where status='completed')/count(*),1) as completion_rate_pct
from public.requests
group by 1 order by 1 desc;
```
- Frühwarnung: Kohorten > 4 Wochen alt mit `completion_rate < 40 %` der `hired`-Fälle → Übergabe an Ops.

**KPI 5 — Nordstern: Bestätigte Vermittlungen pro Woche (BCV)**
- Definition: `completed`-Requests mit Review-Beleg.
```sql
select date_trunc('week', r.created_at) as cohort_week, r.city, r.spec,
       count(*) filter (where r.status = 'completed') as completed,
       count(rv.id) as completed_with_review
from public.requests r
left join public.reviews rv on rv.request_id = r.id
group by 1,2,3 order by 1 desc;
```
- ⚠️ Ehrlichkeits-Note: Ohne Review/Projekt-Anker ist `completed` nur ein Status-Flag. Solange nicht geprüft ist, **wer** den Status setzt (manuell? Edge Function?), gelten BCV-Zahlen als „Status-Abschlüsse", nicht als bestätigte Aufträge. → siehe Tracking-Lücken L2.

**KPI 6 — Bewertungsquote & Qualität (N8/N7)**
- Definition: Reviews ÷ completed Requests; Durchschnittsrating je Stadt/Gewerk; Anteil `verified = true`.
```sql
select p.country, r.spec,
       count(rv.id) as reviews,
       round(avg(rv.rating),2) as avg_rating,
       round(100.0*count(*) filter (where rv.verified)/count(rv.id),1) as verified_pct
from public.reviews rv
join public.profiles p on p.id = rv.tech_id
join public.requests r on r.id = rv.request_id
where rv.created_at >= :week_start
group by 1,2;
```
- Frühwarnung: `avg_rating < 4.0` in einem Segment oder `verified_pct < 50 %`.

**KPI 7 — Kunden-Wiederkehr (N9) — heute nur approximierbar**
- Definition: Anteil der Requests, deren `contact`-Nummer bereits einen früheren Request hat. Kein Kundenkonto → Näherung über Kontaktnummer. In Berichten nur aggregiert, nie die Nummer selbst.
```sql
with first_seen as (
  select contact, min(created_at) as first_request_at from public.requests group by 1
)
select date_trunc('week', r.created_at) as week,
       count(*) filter (where r.created_at > f.first_request_at) as returning_requests,
       count(*) as total_requests
from public.requests r join first_seen f on f.contact = r.contact
group by 1 order by 1 desc;
```
- Frühwarnung: Wiederkehr-Anteil dauerhaft < 10 % nach 3 Monaten Laufzeit → Nachfrageseite ist ein Einmal-Kanal; Referral-Loop auf Kundenseite fehlt.

### Angebotsseite

**KPI 8 — Neue Registrierungen (A1) nach Rolle**
```sql
select date_trunc('week', created_at) as week, role, country, count(*) as signups
from public.profiles group by 1,2,3 order by 1 desc;
```
- Frühwarnung: 2 Wochen 0 neue Techniker in einer beworbenen Stadt.

**KPI 9 — Profil-Aktivierung (A2)**
- Definition: Anteil der Profile einer Registrierungs-Kohorte mit `xp_events.event_type = 'profile_completed'` innerhalb von 7 Tagen.
```sql
select date_trunc('week', p.created_at) as cohort_week,
       count(*) as signups,
       count(x.profile_id) as profile_completed,
       round(100.0*count(x.profile_id)/count(*),1) as activation_pct
from public.profiles p
left join lateral (
  select distinct profile_id from public.xp_events e
  where e.profile_id = p.id and e.event_type = 'profile_completed'
    and e.created_at < p.created_at + interval '7 days'
) x on true
where p.role = 'tech'
group by 1 order by 1 desc;
```
- **Vorbedingung:** prüfen, ob `award_xp('profile_completed')` im Anmeldeflow tatsächlich aufgerufen wird; sonst liefert der KPI dauerhaft 0 und misst nichts. → Lücke L3.

**KPI 10 — Verifikations-Durchlauf (A3)**
- Definition: pending → approved/rejected, Durchlaufzeit und Approval-Quote je Level (1=Identität … 4=lizenziert).
```sql
select level, status, count(*),
       avg(extract(epoch from (now() - created_at))/86400.0)::numeric(10,1) as days_open
from public.verifications
group by 1,2;
-- Stau: pending-Backlog nach Alter
select level, count(*) as pending_backlog,
       max(now() - created_at) as oldest
from public.verifications where status = 'pending' group by 1;
```
- Frühwarnung: ältester pending-Eintrag > 14 Tage → Verifikationsprozess blockiert Vertrauenssignal.

**KPI 11 — Techniker-Angebotsquote pro Segment (Liquidität)**
- Definition: Anzahl „einsatzbereiter" Techniker (Näherung: Verifikation approved ≥ Level 1 **oder** ≥ 1 bestätigtes Projekt) pro Stadt × Gewerk ÷ wöchentliche Anfragen dort.
```sql
with supply as (
  select p.country, p.spec, count(distinct p.id) as techs_ready
  from public.profiles p
  where p.role = 'tech' and (
    exists (select 1 from public.verifications v
            where v.tech_id = p.id and v.status = 'approved' and v.level >= 1)
    or exists (select 1 from public.projects pr
               where pr.tech_id = p.id and pr.confirmed_by <> 'none'))
  group by 1,2
),
demand as (
  select country, spec, count(*) as requests_28d
  from public.requests
  where created_at >= now() - interval '28 days'
  group by 1,2
)
select coalesce(s.country, d.country) as country, coalesce(s.spec, d.spec) as spec,
       coalesce(s.techs_ready,0) as techs_ready,
       coalesce(d.requests_28d,0) as requests_28d,
       round(coalesce(s.techs_ready,0)::numeric / nullif(d.requests_28d,0), 2) as supply_per_request
from supply s full outer join demand d on d.country = s.country and d.spec = s.spec;
```
- Frühwarnung: `supply_per_request < 0.5` → Matching-Stau ist strukturell, nicht operativ. ⚠️ Limitation: `profiles` hat kein `city`-Feld — Segmentierung nur auf `country` möglich. → Lücke L4.

**KPI 12 — Belegte Projekte (A7)**
```sql
select date_trunc('week', confirmed_at) as week, country, category,
       count(*) as confirmed_projects,
       count(*) filter (where confirmed_by = 'client') as by_client,
       count(*) filter (where confirmed_by = 'scout') as by_scout
from public.projects
where confirmed_by <> 'none'
group by 1,2,3 order by 1 desc;
```
- Frühwarnung: Anteil unbestätigter Projekte (`confirmed_by = 'none'`) > 60 % der Neuanlagen → Bestätigungs-Loop (Kunde/Scout) funktioniert nicht.

**KPI 13 — Scout-Aktivität: Vouches & Placements (S1/S2)**
```sql
-- aktive Vouches je Scout (Top-Liste für Ops, nicht öffentlich)
select scout_id, count(*) as active_vouches, sum(stake_vip) as vip_at_stake
from public.vouches where status = 'active' group by 1 order by 2 desc;

-- VIP-Events je Woche
select date_trunc('week', created_at) as week, event_type, count(*), sum(points) as points
from public.vip_events group by 1,2 order by 1 desc;
```
- Frühwarnung: `clawback`-/`revoked`-Quote > 20 % der je aktiven Vouches → Scout-Qualität oder Anreizproblem. Wenn `vip_events` über Wochen leer bleibt: prüfen, ob die Platzierungs-Vergabe überhaupt implementiert ist (Schema kommentiert Vergabe als Server-seitiges TODO).

**KPI 14 — Referral-Loop (A9)**
```sql
select date_trunc('week', r.created_at) as week,
       count(*) as referrals,
       count(distinct r.referrer_id) as active_referrers
from public.referrals r group by 1 order by 1 desc;

-- Anteil geworbener Techniker an allen Neuanmeldungen
select date_trunc('week', p.created_at) as week,
       round(100.0*count(rf.referred_id)/count(*),1) as referred_share_pct
from public.profiles p
left join public.referrals rf on rf.referred_id = p.id
where p.role = 'tech' group by 1 order by 1 desc;
```
- Frühwarnung: `referred_share_pct` fällt 4 Wochen in Folge → Referral-Anreiz (25 XP) wirkt nicht oder ist unsichtbar.

**KPI 15 — Matching-Funktions-Gesundheit (Ops-Begleitmetrik)**
- Definition: Anteil der Requests, für die der Instant-Match-Trigger erfolgreich die Edge Function erreicht hat. Technisch prüfbar über `net._http_response` (pg_net) und Edge-Function-Logs.
```sql
select count(*) as calls,
       count(*) filter (where status_code between 200 and 299) as ok,
       count(*) filter (where status_code is null or status_code >= 400) as failed
from net._http_response
where created > now() - interval '7 days';
```
- Frühwarnung: `failed`-Anteil > 5 % oder fehlender Vault-Secret-WARNING in den DB-Logs → sofort an Technik. Das ist der früheste Indikator überhaupt, weil er vor jeder Trichterstufe greift.

---

## 4. Wöchentlicher Reporting-Rhythmus (1 Seite, nicht-technisch)

**Termin:** Jeden Montag, 10:00, Vorwoche Mo–So. Erstellung: halbautomatisch (SQL-Snippets als gespeicherte Abfragen), Kuratierung durch KPI_Analytics.

**Format — „Eine Seite Vermittlung":**

1. **Kopf (3 Zahlen):** Bestätigte Vermittlungen letzte Woche | Neue Anfragen | Neue Techniker. Jeweils mit ▲▼ zur Vorwoche. Keine Prozente ohne Nenner.
2. **Ampel-Tabelle (5 Zeilen):** Match-Quote, Annahmequote, Abschlussquote, Ø Bewertung, Verifikations-Backlog. Grün/Gelb/Rot nach den Schwellen aus Abschnitt 3 — mit dem Hinweis „Schwelle = Startwert, Kalibrierung läuft".
3. **Stadt × Gewerk Fokus:** die 3 Segmente mit dem größten negativen Abweichung, je ein Satz Befund + ein Satz vorgeschlagene Aktion (Ops/Marketing).
4. **Datenqualitäts-Box:** Was diese Woche **nicht** gemessen werden konnte (z. B. Besucherzahlen, Wiederkehr) — sichtbar statt versteckt.
5. **Eine Entscheidung:** maximal eine konkrete Empfehlung mit Owner und Frist.

Regeln: keine personenbezogenen Daten (keine Namen, Nummern, evidence-URLs); Aggregate ab n < 5 unterdrücken („zu klein, nicht berichtet"); jede Zahl trägt ihre Definition im Fuß („abgeschlossen = Status completed mit Bewertung").

---

## 5. Tracking-Lücken (heute messbar vs. zusätzlicher Aufwand)

| # | Lücke | Auswirkung | Vorschlag |
|---|---|---|---|
| L1 | **Kein Web-/Besucher-Tracking.** Keine Tabelle, keine Events für Seitenaufrufe, Formular-Starts, Sprachversionen. | Trichterstufe N1 und Conversion Besuch→Anfrage unbekannt; Marketing-Kanäle nicht attribuierbar. | Minimal: privacy-freundliche Event-Tabelle `page_events` (page, lang, referrer, utm, anon_session_id, created_at) oder Plausible/Umami; **keine** Cookies-Pflicht-Konstruktion ohne Rechtsprüfung je Land. |
| L2 | **Kein Auftrags-Beleg-Anker.** `matches`/`projects` sind nicht mit dem konkreten Request-Abschluss verknüpft; wer `requests.status` setzt, ist im Schema nicht nachvollziehbar. | Nordstern „bestätigt" beruht auf Status-Flag + Review-Näherung. | `matches.completed_at`, `matches.completed_by`, ggf. `confirmed_by_request_id` auf `projects`; Statuswechsel nur serverseitig mit Audit-Event. |
| L3 | **Event-Vergabe unverifiziert.** `award_xp`-Whitelist existiert (u. a. `profile_completed`, `placement_completed`, `referral_bonus`), aber ob/wann die Edge Function `award-points` diese Events auslöst, ist aus dem Schema nicht belegt. | KPIs 9, 13 können dauerhaft 0 messen ohne dass das Geschäft schlecht läuft — oder umgekehrt. | Vor erstem Report: Edge-Function-Code `award-points` gegen die Whitelist abgleichen und einen Testlauf dokumentieren. |
| L4 | **`profiles` ohne `city`-Feld** (nur `country`). | Angebots-Liquidität nicht auf Stadtebene messbar, obwohl Matching stadtweise läuft. | `city` auf `profiles` ergänzen (Migration), Bestand via Selbstauskunft. |
| L5 | **Kein Verfügbarkeits-/Aktivitätsstatus** für Techniker (kein last_active, kein online/available-Flag). | „Verfügbare Fachkraft" (Kernversprechen) ist nicht definierbar; KPI 11 ist eine Näherung. | `last_seen_at` bei Login/Dashboard-Aufruf schreiben; optional `available` boolean. |
| L6 | **Keine Kunden-Entität.** Requests haben nur `contact`; keine Kunden-Registrierung. | Wiederkehr, Kunden-LTV, Kunden-Referral nur approximierbar (KPI 7). | Mittelfristig optionales Kundenkonto; kurzfristig deduplizierter `contact`-Hash (nie Klartext in Berichten). |
| L7 | **Kein Spam-/Qualitäts-Flag** auf `requests`. | „Gültige Anfrage" (N3) nicht von Roh-Insert unterscheidbar. | `is_valid`/`spam_score` durch Ops oder Heuristik (Message-Länge, Duplikate). |
| L8 | **Va_cases/va_case_events (Scout-Netzwerke)** nicht in dieses Framework integriert — Schema vorhanden, betriebliche Nutzung unklar. | Scout-Netzwerk-Fälle evtl. zweiter, paralleler Vermittlungspfad → Doppelzählungsrisiko. | Klären, ob `va_cases` produktiv genutzt wird; dann als eigene Trichterlinie abbilden. |

**Was heute ohne jede Änderung messbar ist:** KPI 1–6, 8, 10, 12–15 (mit den genannten Vorbehalt-Prüfungen bei 9 und 13). **Was Tracking-Aufwand braucht:** N1/Besuch (L1), Auftrags-Beleg (L2), Stadt-Liquidität (L4), Verfügbarkeit (L5), saubere Wiederkehr (L6), Anfrage-Validität (L7).

---

## 6. Drei nächste Maßnahmen

1. **Baseline-Report starten (Woche ab 2026-09-22, kein Code nötig).** Die 15 SQL-Skizzen als gespeicherte Abfragen im Supabase-SQL-Editor hinterlegen und die erste „Eine Seite Vermittlung" mit 4-Wochen-Rückblick erzeugen. Ziel: echte Schwellen kalibrieren, Platzhalter-Warnwerte durch beobachtete Verteilungen ersetzen. Owner: KPI_Analytics. **Vorbedingung:** L3-Check — `award-points`-Edge-Function gegen die `award_xp`-Whitelist abgleichen, sonst KPI 9/13 als „nicht messbar" kennzeichnen.

2. **Auftrags-Beleg-Anker schließen (L2, kleine Migration).** `matches.completed_at`/`completed_by` ergänzen, Status-Übergänge auf `requests` serverseitig mit Audit-Event versehen. Erst dann ist der Nordstern „bestätigt" statt „behauptet". Owner: Technik + Ops-Definition, wer einen Auftrag als abgeschlossen bestätigt (Kunde via Review-Link? Scout? Ops?).

3. **Minimales Besucher-Event entscheiden (L1, Entscheidung vor Umsetzung).** Abwägung eigene `page_events`-Tabelle vs. externes datenschutzfreundliches Analytics (Plausible/Umami) — unter Beachtung, dass Zielländer und Sprachen getrennt zu behandeln sind und Rechtsanforderungen je Land geprüft werden müssen. Ergebnis: ein beschlossener Ansatz + 4-Wochen-Plan; kein vorschnelles Tracking ohne Consent-/Rechtsklärung.

---

*Methodik-Hinweis gemäß SENIOR-STANDARD und Skill voltage-marketplace-analytics: Dieser Bericht enthält keine Ist-Zahlen, keine behaupteten Plattformleistungen und keine ungeprüften Verifikations-/Einkommensclaims. Alle SQL-Skizzen sind gegen das lokal beobachtete Schema entworfen, aber nicht gegen die Produktivdatenbank ausgeführt worden.*
