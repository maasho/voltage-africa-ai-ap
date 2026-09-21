# AppSec-Review: Öffentliche Angriffsfläche Voltage Africa

**Datum:** 2026-09-21 · **Rolle:** AppSec_Engineer (Profil- und Zugriffsschutz)
**Scope:** Statische Website (HTML/JS unter `assets/` + Seiten) + Supabase-Backend-Artefakte im Repo (`supabase-setup.sql`, `supabase/migrations/`, `supabase/scout-*.sql`, `supabase/functions/`).
**Methode:** Statische Code-Analyse. **Kein Live-Zugriff auf das Supabase-Projekt** — alle Aussagen über den Ist-Zustand der Datenbank sind statische Befunde aus dem Repo und müssen vom Orchestrator live verifiziert werden (Checkliste unten). Keine Live-Angriffe, keine echten Datenzugriffe.

---

## 1. Zusammenfassung

Der Code ist ungewöhnlich sorgfältig gehärtet: kein Service-Key im Repo, Secrets über Supabase Vault, serverseitige XP/VIP-Vergabe mit Whitelist, Idempotenz und `service_role`-Grants, gehärteter Review-Pfad über `submit_review`, Netzwerk-Funktionen mit sauberen Definer-Funktionen und minimierten Grants. Alle Nutzerdaten-Renderpfade verwenden durchgehend `esc()`/`textContent`.

**Aber:** Drei kritische Befunde unterlaufen die Härtung an anderer Stelle:

1. **K1 — Die RLS-Update-Policy auf `profiles` erlaubt Voll-Update der eigenen Zeile.** Damit kann jeder registrierte Nutzer mit dem öffentlichen anon key direkt `xp`, `level`, `verified`, `rating`, `review_count`, `projects` und `role` selbst setzen — die komplette serverseitige Gamification-Härtung (`award_xp`/`award_vip`) wird umgangen.
2. **K2 — Öffentliche Inserts (`requests`, `waitlist`) ohne Captcha** — `request.html` hat kein Turnstile; jeder anonyme Insert feuert zusätzlich den Instant-Match-Trigger (pg_net → Edge Function mit Service Role) → Kosten-, Daten- und Ops-Spam-Vektor.
3. **K3 — View `verifications_public` ohne `security_invoker`** (Repo-Stand) — läuft als Definer und umgeht damit die RLS der Basistabelle; pending/rejected-Verifikationen wären öffentlich lesbar, entgegen dem dokumentierten Härtungsziel. Live-Stand zu prüfen.

Dazu kommen mittlere Befunde: ungeprüfte serverseitige Turnstile-Durchsetzung, Schema-Drift (`messages`, `waitlist`, `profile_private` fehlen komplett in den Repo-SQL-Dateien — deren RLS ist aus dem Repo nicht verifizierbar), Messaging-Spam ohne Beziehungs-/Rate-Limit, Self-Referral-Lücke, fehlende CSP/SRI als Tiefenverteidigung und eine breite öffentliche Profil-Datensicht.

| Schwere | Anzahl |
|---|---|
| Kritisch | 3 |
| Mittel | 7 |
| Niedrig/Hinweis | 4 |

---

## 2. Fundstellen mit Belegen

### K1 — KRITISCH: Eigenes Profil frei manipulierbar (XP, Level, Verifizierung, Rating, Rolle)

**Beleg:** `supabase-setup.sql` Z. 26–28:

```sql
create policy "profiles_own_update"
  on public.profiles for update using (auth.uid() = id);
```

Keine Spaltenbeschränkung. Postgres-RLS kann Spalten nicht einschränken — jeder authentifizierte Nutzer darf **jede Spalte** der eigenen Zeile schreiben. Der Client (`profile.html` Z. 511–513) sendet zwar nur harmlose Felder, aber mit dem öffentlichen anon key (`assets/supabase-config.js` Z. 10) genügt:

```js
supa.from("profiles").update({ xp: 999999, level: 5, verified: true, rating: 5, review_count: 500, role: "scout" }).eq("id", myId)
```

**Auswirkung:** Die gesamte serverseitige Härtung aus `20260724_track_e_hardening.sql` / `20260724_referrals.sql` (Punktewhitelist, Dedupe-Indizes, `service_role`-Grants) wird wirkungslos — der Angreifer braucht die Ledger-Funktionen gar nicht, er schreibt die denormalisierten Zähler direkt. `messages.html` Z. 68–69 selektiert `profiles.verified` (✅-Badge); `profile.html` Z. 464–465 liest `xp, level, projects` öffentlich; Rankings/FUT-Karten zeigen manipulierte Werte. `role: "scout"` öffnet zusätzlich Scout-Flüsse (VIP-Eligibility wird in `award-points/index.ts` Z. 195 an `role` geprüft).

**Fix (SQL, vom Orchestrator auszuführen):**

```sql
-- Variante A (empfohlen): Spaltenprivilegien
revoke update on public.profiles from authenticated;
grant update (name, headline, bio, country, region, spec, skills, languages, availability, interests)
  on public.profiles to authenticated;

-- Variante B (zusätzlich, Defense in Depth): Trigger, der geschützte Spalten sperrt
create or replace function public.protect_profile_columns() returns trigger
language plpgsql as $$
begin
  if new.xp is distinct from old.xp or new.level is distinct from old.level
     or new.projects is distinct from old.projects or new.rating is distinct from old.rating
     or new.review_count is distinct from old.review_count
     or new.verified is distinct from old.verified or new.role is distinct from old.role then
    raise exception 'protected profile column';
  end if;
  return new;
end $$;
create trigger trg_protect_profiles before update on public.profiles
  for each row execute function public.protect_profile_columns();
```

Hinweis: `award_xp` läuft als SECURITY DEFINER (Owner) und wird von Variante A nicht beeinträchtigt; bei Variante B muss der Trigger die Definer-Rolle ausnehmen (z. B. `if current_user = 'service_role' then return new; end if;` bzw. Trigger mit `when`-Bedingung auf Session-User), sonst blockiert er die legitime Server-Vergabe. Spaltenliste vorher gegen Live-Schema prüfen (Checkliste Q5/Q7).

---

### K2 — KRITISCH: Öffentliche Formular-Inserts ohne Bot-Schutz + Trigger-Kaskade

**Belege:**

- `request.html` — kein Turnstile auf der Seite (Widget existiert nur in `signup.html` Z. 90–98 und `login.html` Z. 68–81). Submit geht direkt: `request.html` Z. 211 `await window.supa.from("requests").insert(payload)`.
- `supabase-setup.sql` Z. 86–89: `create policy "requests_public_insert" on public.requests for insert to anon, authenticated with check (true);`
- `20260724_instant_match_trigger.sql` Z. 76–80: `AFTER INSERT`-Trigger ruft per pg_net die Edge Function `instant-match` (Service Role) auf; diese schreibt `matches`-Zeilen (`instant-match/index.ts` Z. 218–222).
- `assets/app.js` Z. 383–385 (`VA_WAITLIST.insertRow`): Client-Insert in `waitlist` ohne Captcha; der einzige Schutz ist ein Honeypot-Feld (Z. 439) — für Skript-Angreifer trivial umgehbar.

**Auswirkung:** Unbegrenzte anonyme Spam-Requests → Edge-Function-Invocations (Kosten), `matches`-Datenmüll, wa.me-Links mit gefälschten Kundendaten an das Ops-Team, Routing-Fälle in Scout-Dashboards (`va_route_request`). Waitlist ebenso flutbar. Die E.164-Check-Constraints begrenzen nur das Format, nicht die Menge.

**Fix:**

1. **Kurzfristig (DB-seitig, ohne Frontend-Änderung wirksam):** Rate-Limit-Trigger auf `requests`/`waitlist`, z. B. max. 3 Inserts je `contact` und Tag:
   ```sql
   create or replace function public.requests_rate_limit() returns trigger
   language plpgsql security definer set search_path = public as $$
   begin
     if (select count(*) from public.requests
         where contact = new.contact and created_at > now() - interval '24 hours') >= 3 then
       raise exception 'rate_limited';
     end if;
     return new;
   end $$;
   create trigger trg_requests_ratelimit before insert on public.requests
     for each row execute function public.requests_rate_limit();
   ```
2. **Mittelfristig (echte Bot-Prüfung):** Turnstile in `request.html` einbauen und den Insert über eine Edge Function leiten (`turnstile-verify` → Token gegen `https://challenges.cloudflare.com/turnstile/v0/siteverify` mit Secret aus Vault → erst dann Insert mit Service Role). Direkter PostgREST-Insert kann Turnstile nicht prüfen — solange `requests_public_insert` besteht, bleibt der Client-Captcha kosmetisch. Analog für `waitlist`.

---

### K3 — KRITISCH (Live-Stand zu prüfen): `verifications_public` ohne `security_invoker`

**Beleg:** `supabase-setup.sql` Z. 225–228:

```sql
drop view if exists public.verifications_public;
create view public.verifications_public as
  select tech_id, level, status
  from public.verifications;
```

Kein `with (security_invoker = true)` — im Gegensatz zu `vouch_counts` (Z. 254–260, korrekt). Views sind per Default SECURITY DEFINER: die RLS-Policy `verifications_public_read` (`using (status = 'approved')`, Z. 219–223) wird als View-Owner ausgewertet → der Owner umgeht RLS → **alle** Zeilen inkl. `pending`/`rejected` sind öffentlich lesbar. Der Client-Filter in `profile.html` Z. 412 (`.eq("status","approved")`) schützt nicht vor direkten API-Aufrufen ohne Filter. `evidence_url` ist nicht in der View (gut), aber der Prüfstatus einzelner Techniker (inkl. Ablehnungen) ist personenbezogen und vertraulich.

**Hinweis:** Das Briefing nennt „Views mit security_invoker" als bekannten Härtungsstand — möglicherweise wurde dies im Dashboard bereits korrigiert; **im Repo ist es nicht korrigiert.** Orchestrator muss den Live-Stand prüfen (Q3).

**Fix (falls live noch defekt):**

```sql
create or replace view public.verifications_public
with (security_invoker = true) as
  select tech_id, level, status
  from public.verifications
  where status = 'approved';
```

---

### M1 — MITTEL: Serverseitige Turnstile-Durchsetzung ungeprüft

**Beleg:** Client-Verdrahtung ist vollständig und korrekt: `signup.html` Z. 185–205 (`captchaToken` an `signInWithOtp`, Pflicht bei konfiguriertem Site-Key), `login.html` Z. 93–106 und Z. 125–141, Site-Key in `assets/supabase-config.js` Z. 25. ABER: Supabase prüft das Token nur, wenn im Dashboard unter **Authentication → Attack Protection → Captcha** der Turnstile-Secret hinterlegt ist. Der Kommentar in `supabase-config.js` Z. 18–21 warnt selbst davor. Ohne Dashboard-Konfiguration ist der gesamte Bot-Schutz wirkungslos (Token wird ignoriert).

**Fix (Orchestrator, Dashboard):** Captcha protection aktivieren (Anbieter Cloudflare Turnstile, Secret aus Cloudflare-Dashboard). **Verifikationstest:** `signInWithOtp` ohne `captchaToken` gegen das Projekt → muss mit Captcha-Fehler abgelehnt werden. Ergebnis dokumentieren.

### M2 — MITTEL: Schema-Drift — `messages`, `waitlist`, `profile_private` fehlen in allen Repo-SQL-Dateien

**Beleg:** Grep über alle `.sql` im Repo: kein `create table` für `messages`, `profile_private`, `waitlist`. Der Client nutzt alle drei (`messages.html` Z. 56–60/83–84, `profile.html` Z. 475/515, `assets/app.js` Z. 383–385). Ihre RLS-Policies sind aus dem Repo **nicht verifizierbar** — sie existieren nur als manueller Dashboard-Zustand.

**Auswirkung:** Unkontrollierbarer Sicherheitszustand. Erwartete Mindest-Policies: `messages` (Select nur eigene, Insert nur `sender_id = auth.uid()`, Update nur Empfänger für `read_at`), `profile_private` (nur eigene Zeile), `waitlist` (Insert-only für anon, kein Select).

**Fix:** Live-Policies erfassen (Q1/Q2) und als versionierte Migration ins Repo überführen.

### M3 — MITTEL: Messaging ohne Beziehungs- oder Rate-Limit

**Beleg:** `messages.html` Z. 161: `insert({sender_id: ME, recipient_id: recipient, body})` — `recipient` ist eine beliebige UUID aus dem URL-Parameter (`?to=`, Z. 64–66). Kein Beziehungsnachweis (Match/Netzwerk), kein Rate-Limit, kein Captcha. Jeder registrierte Nutzer kann jedes Mitglied unbegrenzt anschreiben. Lesen ist korrekt auf eigene Konversationen beschränkt (Z. 58).

**Fix:** Insert-Policy/Check: Empfänger muss existieren; optional gemeinsames Netzwerk/Match oder Kontakt-Freigabe; DB-Rate-Limit (z. B. Trigger: max. 20 neue Konversationen/Tag je Sender).

### M4 — MITTEL: Referral-Sybil-/Self-Referral-Lücke

**Beleg:** `20260724_referrals.sql` Z. 41–46 — kein `check (referrer_id <> referred_id)`; Insert-Policy Z. 60–65 prüft nur `auth.uid() = referred_id`, `referrer_id` ist frei wählbar. Signup übernimmt `?ref=` aus localStorage (`signup.html` Z. 139–142, Z. 158–160). Abschwächung: Bonus erst bei `activate_check` (Profil vollständig + Projekt + **verifizierte** Bewertung, `award-points/index.ts` Z. 372–379) und Dedupe-Unique-Index.

**Fix:** `alter table public.referrals add constraint referrals_no_self check (referrer_id <> referred_id);` + in `activate_check` zusätzlich E-Mail-Domain-/Erstellungszeit-Heuristik erwägen (Multi-Account-Farming bleibt über Turnstile-E-Mail-Signup theoretisch möglich).

### M5 — MITTEL: Öffentliche Profil-Datensicht zu breit (Datenminimierung)

**Beleg:** `profiles_public_read` `using (true)` (`supabase-setup.sql` Z. 22–24) erlaubt anon den vollen `SELECT *` über **alle** Profilzeilen — inkl. `interests`, `availability`, `created_at`, `role`. `profile.html` Z. 464–465 selektiert zwar nur unkritische Spalten, aber die API liefert alles. Öffentlich ohne Login abrufbar: Name, Headline, Bio, Land, **Stadt/Region**, Skills, Sprachen, Verfügbarkeit, **geschäftliche Interessen** („buying/selling equipment", „subcontracting"), XP, Level, Projekte, Erstellungsdatum — plus Reviews mit Bewertername und Projekthistorie (`profile.html` Z. 411–415). Massen-Scraping der gesamten Mitgliederbasis ist damit trivial.

**Bewertung Datenschutz vs. Vertrauen:** Name/Land/Fachrichtung/XP/Verifizierungsbadge sind für das Vertrauensmodell vertretbar (öffentliches Verzeichnis). Stadt, Verfügbarkeit und geschäftliche Interessen sind es nicht ohne explizite Einwilligung — sie ermöglichen Wettbewerbs- und Preis-Profiling einzelner Techniker.

**Empfehlung:** Öffentliche Sicht als View mit Mindestspalten (`id, name, country, spec, xp, level, verified`) und Tabelle für anon sperren; Stadt/Interessen/Verfügbarkeit nur nach Login oder mit Opt-in-Flag (`public_profile boolean`, Default false). Einwilligungstext in `privacy.html`/`signup.html` entsprechend präzisieren. DSGVO-Relevanz (EU-Projekt, personenbezogene Daten afrikanischer Nutzer).

### M6 — MITTEL: Keine Tiefenverteidigung gegen XSS (CSP fehlt, CDN ohne SRI)

**Belege:** Alle geprüften Renderpfade mit Nutzerdaten verwenden `esc()`/`textContent` (`profile.html` Z. 322–335/395–406, `messages.html` Z. 106–122, `assets/network.js` Z. 7/27–81) — gut. Aber: kein Content-Security-Policy-Header (statisches Hosting; in keiner Datei konfiguriert), und supabase-js wird von jsDelivr ohne Subresource Integrity geladen (`assets/supa-auth.js` Z. 54, gepinnt `@2.116.0`). Session-Tokens liegen in localStorage (supabase-js Default) — **ein einziges XSS reicht für Kontodiebstahl**, CSP wäre der Schutzwall dahinter.

**Fix:** CSP via Hosting-Header (z. B. `default-src 'self'; script-src 'self' https://challenges.cloudflare.com https://cdn.jsdelivr.net; connect-src 'self' https://fkswmzndqfxntnzcmstw.supabase.co https://challenges.cloudflare.com; frame-src https://challenges.cloudflare.com; img-src 'self' data: https://api.qrserver.com; style-src 'self' 'unsafe-inline'` — Inline-Styles werden aktuell genutzt) und supabase-js lokal ausliefern oder SRI-Hash ergänzen.

### M7 — MITTEL: `profile_private` — Telefon ohne serverseitige Validierung; Policy unbekannt

**Beleg:** `profile.html` Z. 515: `upsert({ id:user.id, phone })` — `phone` ist freier Text ohne E.164-Check (clientseitig wie DB-seitig unbekannt; Tabelle nicht im Repo, siehe M2). `instant-match` Z. 111–117 normalisiert tolerant — bei Müllnummern schlägt die Ops-Benachrichtigung fehl (`phone_missing`).

**Fix:** Check-Constraint `phone ~ '^\+[1-9][0-9]{6,14}$'` analog `requests.contact`; Policies verifizieren (nur eigene Zeile lesbar/schreibbar, kein anon-Zugriff).

### Niedrig / Hinweise

- **L1 — Latente XSS-Falle in `futCardHTML`:** `assets/app.js` Z. 301 `${initials(t.n)}` und Z. 298 `${flag}` sind **nicht** escaped (im Gegensatz zu `${esc(t.n)}` Z. 302). Aktuell nur mit statischen Demo-Daten (`VA_DATA`) gefüttert — sobald Live-Profildaten einfließen, stored XSS über Name/Stadt. Fix: `esc(initials(t.n))`, `esc(flag)`.
- **L2 — `review.html` ohne Captcha:** `submit_review` für anon ausführbar (`20260724_track_e_hardening.sql` Z. 251–252). Durch Match-Anker (Z. 62–71) auf bekannte Review-Links begrenzt; UUID-Raten unpraktisch. Optional: Turnstile ergänzen, wenn Review-Links öffentlich geteilt werden.
- **L3 — Client-seitige Route-Guards sind nur UX:** `data-protected`-Weiterleitung (`assets/supa-auth.js` Z. 66–68) schützt nichts — korrekt, solange RLS trägt. Kein Fix nötig; als Architektur-Annahme dokumentieren.
- **L4 — Client-gesetzte Rolle im Signup:** `role: suRole` wird in `user_metadata` geschrieben (`signup.html` Z. 201) und vom Trigger in `profiles.role` übernommen (`supabase-setup.sql` Z. 41–48) — Nutzer wählt „scout" selbst. VIP-Vergabe erfordert zusätzlich aktiven Vouch (serverseitig) → Restrisiko gering; mit K1-Fix (role nicht updatebar) weitgehend entschärft. Optional: `role` nur über Backend-Flow setzen.

### Positiv-Befunde (geprüft, in Ordnung)

- Kein Service-Role-Key, kein `VA_FUNCTION_SECRET` im Repo (Grep über `*.js/html/ts/md`); Secret-Handling über Supabase Vault (`20260724_instant_match_trigger.sql` Z. 48–52) und `supabase secrets` (Edge Functions Z. 477–485 / Z. 256–264). anon key im Frontend ist zulässig.
- Edge Functions: Shared-Secret-Auth, keine permissiven CORS-Origins, keine internen Fehlerdetails nach außen, serverseitige Punktewhitelist mit DB-Re-Check, Idempotenz + Unique-Dedupe-Indizes.
- `submit_review`: Match-Anker, Einmaligkeit, Race-Guard (unique_violation), Definer mit gepinntem `search_path`.
- Netzwerk-SQL (`scout-networks.sql`): `revoke all` vor selektiven Grants, Operator-Checks serverseitig, Routing-Trigger mit Advisory-Lock, Consent-Pflicht, kein Kundenkontakt-Zugriff ohne Zuständigkeit.
- Reviews/Verifikationen: kein Client-Update/Delete; Verifikation nur eigene `pending`-Inserts (Z. 211–217).
- OTP/Magic-Link erzwingt E-Mail-Besitz inhärent; Fehlermeldungen im Login generisch (kein User-Enumeration über Fehlertext, `login.html` Z. 107/143).

---

## 3. Bot-/Spam-Lage (Turnstile)

| Fläche | Client-Token verdrahtet? | Serverseitige Prüfung | Status |
|---|---|---|---|
| Signup (`signup.html`) | Ja (Z. 185–205) | Supabase Auth Captcha — **Dashboard-Konfiguration ungeprüft** | ⚠️ Orchestrator-Check |
| Login + Magic-Link (`login.html`) | Ja (Z. 93–106, 125–141) | dto. | ⚠️ Orchestrator-Check |
| Anfrage (`request.html`) | **Nein** | Keine möglich bei direktem PostgREST-Insert | ❌ Lücke (K2) |
| Waitlist (`assets/app.js`) | Nein (nur Honeypot) | Keine | ❌ Lücke (K2) |
| Review (`review.html`) | Nein | Match-Anker statt Captcha | ⚠️ akzeptables Restrisiko (L2) |
| Messages | n/a (Auth) | Kein Rate-Limit | ⚠️ M3 |

**Konkrete Anweisung serverseitig:**

1. **Supabase Dashboard → Authentication → Sign In / Providers → Captcha protection:** aktivieren, Anbieter *Cloudflare Turnstile*, Secret-Key aus dem Cloudflare-Dashboard eintragen (Site-Key `0x4AAAAAAEImQOfHgtvvEXs0uF2v7dWRUzo` gehört dazu). Test: OTP-Anforderung ohne Token muss scheitern.
2. **Neue Edge Function `submit-request`:** Turnstile-Token via `siteverify` prüfen (Secret aus Vault/`Deno.env`), dann Insert mit Service Role; danach Policy `requests_public_insert` auf authentifizierte Nutzer einschränken oder ganz entfernen. Gleiches Muster für `waitlist`. Bis dahin greift der Rate-Limit-Trigger aus K2 als Sofortmaßnahme.

---

## 4. Datenminimierung (öffentliche Profilsicht)

**Aktuell öffentlich (ohne Login, via API und `profile.html?id=`):** Name, Headline, Bio, Land, Stadt/Region, Fachrichtung, Skills, Sprachen, Verfügbarkeit, geschäftliche Interessen, XP, Level, Projektanzahl, Erstellungsdatum, Verifizierungsstatus, Reviews (inkl. Bewertername), bestätigte Projekte (Titel, Ort). `members.html`/`rankings.html` sind derzeit nur Weiterleitungs-Platzhalter („Continue with Voltage Africa") — die Exposition läuft faktisch über `profile.html?id=<uuid>` und die offene `profiles`-Tabelle.

**Bewertung:** Vertrauensrelevant und vertretbar: Name, Land, Fachrichtung, XP/Level, Verifizierungsbadge, bestätigte Projekte, Reviews. Datenschutzkritisch: **Stadt** (feiner Standort), **Verfügbarkeit** (Erreichbarkeitsprofil), **Interessen** (Geschäftsabsichten wie „selling equipment") — ohne dokumentierte Einwilligung problematisch; DSGVO (EU-Hosting) verlangt Zweckbindung und Minimierung. Telefon/E-Mail sind sauber getrennt (`profile_private`/`auth.users`) — gut.

**Empfehlung:** Öffentliche View `profiles_public` mit Mindestspalten; `profiles`-Tabelle für anon nur noch über die View; Opt-in-Flag für erweiterte Sichtbarkeit; Datenschutzerklärung um konkrete Aufzählung der öffentlichen Felder ergänzen; Bewerternamen in Reviews auf Vornamen + Initial kürzen.

---

## 5. Orchestrator-Checkliste (im Supabase-Projekt ausführen)

Reihenfolge = Priorität. Q1–Q3 verifizieren die kritischen Befunde live.

```sql
-- Q1) ALLE RLS-Policies (Soll-Ist-Abgleich gegen diesen Bericht)
select schemaname, tablename, policyname, permissive, roles, cmd, qual, with_check
from pg_policies where schemaname = 'public'
order by tablename, policyname;

-- Q2) RLS aktiviert/forciert? Erwartet: relrowsecurity = true für ALLE Tabellen
select relname, relrowsecurity, relforcerowsecurity
from pg_class
where relnamespace = 'public'::regnamespace and relkind = 'r'
order by relname;

-- Q3) Views: security_invoker gesetzt? Erwartet: reloptions enthaelt
-- {security_invoker=true} fuer verifications_public, vouch_counts, xp_totals, vip_totals
select relname, reloptions
from pg_class
where relnamespace = 'public'::regnamespace and relkind = 'v';

-- Q4) Offene Tabellen-Grants an anon/authenticated (Erwartung: nur durch
-- RLS abgesicherte Tabellen; va_*-Tabellen duerfen NICHT auftauchen)
select grantee, table_name, string_agg(privilege_type, ',') as privs
from information_schema.role_table_grants
where table_schema = 'public' and grantee in ('anon','authenticated')
group by grantee, table_name order by table_name;

-- Q5) Spalten-Grants auf profiles (nach K1-Fix: nur Whitelist-Spalten)
select grantee, column_name, privilege_type
from information_schema.column_privileges
where table_schema = 'public' and table_name = 'profiles'
order by column_name;

-- Q6) EXECUTE-Grants: award_xp / award_vip / notify_instant_match /
-- va_escalate_overdue duerfen NICHT fuer public/anon/authenticated auftauchen
select p.proname, r.rolname
from pg_proc p
join pg_namespace n on n.oid = p.pronamespace
cross join lateral (
  select rolname from pg_roles
  where has_function_privilege(rolname, p.oid, 'execute')
) r
where n.nspname = 'public'
  and r.rolname in ('public','anon','authenticated')
order by p.proname, r.rolname;

-- Q7) Live-Spalten der profiles-Tabelle (welche sensiblen Spalten existieren?
-- z. B. verified, rating, review_count, role, xp, level, projects)
select column_name, data_type
from information_schema.columns
where table_schema = 'public' and table_name = 'profiles'
order by ordinal_position;

-- Q8) Existenz + Policies der Nicht-Repo-Tabellen (messages, waitlist,
-- profile_private) — ueber Q1/Q2 abgedeckt, hier nur Existenznachweis
select tablename from pg_tables
where schemaname = 'public'
  and tablename in ('messages','waitlist','profile_private');

-- Q9) Aktive Trigger (Erwartung: on_auth_user_created,
-- trg_requests_instant_match, va_route_new_request; nach Fixes:
-- trg_protect_profiles, trg_requests_ratelimit)
select tgname, tgrelid::regclass as table_name
from pg_trigger where not tgisinternal order by tgname;

-- Q10) Vault-Secret vorhanden? (Name reicht, Wert NICHT ausgeben)
select name, created_at from vault.decrypted_secrets
where name = 'va_function_secret';

-- Q11) Manipulationstest K1 (als normaler authentifizierter Nutzer,
-- NICHT service_role): muss nach dem Fix fehlschlagen
-- update public.profiles set xp = xp + 1000 where id = auth.uid();

-- Q12) Spam-Test K2: anonymer Insert ohne Auth
-- insert into public.requests (name, contact, country, city, spec, message)
-- values ('test', '+254700000000', 'Kenya', 'Nairobi', 'solar', 'rate-limit-test-20-chars');
-- Erwartung nach Fix: rate_limited bzw. 401/403
```

**Dashboard-Checks (kein SQL):**

- Q13) Authentication → Attack Protection → **Captcha protection** aktiv + Turnstile-Secret hinterlegt (M1); Funktionstest ohne Token.
- Q14) Edge Functions → Secrets: `VA_FUNCTION_SECRET` gesetzt; `verify_jwt`-Konfiguration der beiden Functions dokumentieren (Aufruf erfolgt per `x-va-secret`, nicht per User-JWT).
- Q15) Authentication → Email: Confirm email aktiviert (OTP-Flow setzt dies faktisch voraus — verifizieren).

---

## 6. Priorisierte Maßnahmenliste

**P0 — kritisch, sofort:**

1. **K1:** `profiles`-UPDATE auf Whitelist-Spalten beschränken (Spalten-Grants + Schutz-Trigger, SQL in §2 K1). Danach Q11-Test: Selbst-Update von `xp` muss scheitern. Ohne diesen Fix sind Rankings, Level und Verifizierungsbadge öffentlich fälschbar.
2. **K3:** Live-Stand von `verifications_public` prüfen (Q3); falls ohne `security_invoker`: View neu erstellen (SQL in §2 K3).
3. **K2:** Rate-Limit-Trigger auf `requests`/`waitlist` als Sofortmaßnahme (SQL in §2 K2); danach Turnstile-Edge-Function für beide Formulare.

**P1 — mittel, 30 Tage:**

4. M1: Captcha-Enforcement im Dashboard aktivieren und per Test ohne Token belegen (Q13).
5. M2: Live-Schema und Policies von `messages`, `waitlist`, `profile_private` als versionierte Migration ins Repo überführen (Schema-Drift schließen).
6. M5: Öffentliche Profil-View mit Mindestspalten + Opt-in für erweiterte Felder; Datenschutztext präzisieren.
7. M3: Rate-Limit + optional Beziehungs-Check für Message-Inserts.
8. M4: `check (referrer_id <> referred_id)` auf `referrals`.

**P2 — Härtung, 90 Tage:**

9. M6: CSP-Header + supabase-js lokal/mit SRI ausliefern.
10. M7: E.164-Check-Constraint auf `profile_private.phone`.
11. L1: `futCardHTML` — `initials()`/`flag` escapen, bevor Live-Daten angebunden werden.
12. L2: Turnstile auf `review.html` erwägen, sobald Review-Links breit geteilt werden.

---

*Statischer Befund ohne Live-Zugriff; alle SQL-Fixes vor Produktiv-Anwendung in Staging testen und als Migration mit Rückweg ablegen. Keine pauschale Sicherheitsfreigabe.*
