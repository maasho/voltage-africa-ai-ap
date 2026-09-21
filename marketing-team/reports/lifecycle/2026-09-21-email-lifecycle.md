# Lifecycle-E-Mail-System für Voltage Africa

**Rolle:** Lifecycle_Stratege (Mitglieder- und Anfrage-E-Mails)
**Datum:** 2026-09-21
**Status:** Entwurf zur fachlichen Prüfung — kein Versand autorisiert

---

## 1. Zusammenfassung

Dieses Dokument definiert das komplette Lifecycle-E-Mail-System für Voltage Africa:

- **13 fertige Sequenz-E-Mails** in 3 Sequenzen (Techniker-Onboarding 5, Kunden-Journey 4, Scout-Aktivierung 4), Englisch, plain-text-tauglich, mobil-optimiert (kurze Absätze, ein CTA pro Mail).
- **10 transaktionale Systemmails** als Liste mit Kurztext-Vorschlägen (Auth, Anfrage-Status, Matching).
- **Tool-Empfehlung: Brevo** — ein Tool für Auth-SMTP (Supabase Custom SMTP), transaktionale Mails und visuelle Sequenz-Automation, kostenlos bis 300 Mails/Tag (~9.000/Monat). Alternativen bewertet (Resend, AWS SES, Mailchimp).
- **Rechtliches Minimum**: Double-Opt-In, Impressum, 1-Klick-Abmeldung (RFC 8058), Trennung transaktional/marketing. Kein Rechtsrat — Verweis auf Prüfung durch Rechtsbeistand je Zielstaat.
- **Kennzahlen je Sequenz** mit Frühphasen-Zielen (CTR/CTOR-zentriert, Öffnungsraten post-Apple-MPP nur richtungsweisend).

**Leitplanken aus Skill und Senior-Standard eingehalten:** Keine Zusage garantierter Aufträge, keine erfundenen Einnahmen/Provisionen, XP/VIP-Punkte ohne Geldwert (gemäß terms.html), jede Sequenz mit Ein-/Austrittsregeln, Afrika nicht als Einheitsmarkt behandelt (Platzhalter für Land/Stadt/Sprache), WhatsApp als zentraler Kanal referenziert.

---

## 2. Sequenz A — Techniker-Onboarding (5 E-Mails)

### Design-Spec

- **Trigger:** Registrierung als Techniker abgeschlossen + E-Mail bestätigt (Supabase Auth `email_confirmed`).
- **Segment:** `role=technician`, `email_verified=true`; Sprachattribut (`LANGUAGE=EN`, weitere Templates je Land folgen); Ausschluss: `unsubscribed`, Hard Bounce.
- **Austrittsregeln:** (1) Profil 100 % vollständig → Wechsel in „aktive Techniker"-Kommunikation, (2) Abmeldung, (3) Hard Bounce / Beschwerde, (4) 90 Tage inaktiv → Win-back außerhalb dieser Sequenz.
- **Absender:** `Voltage Africa <hello@voltage-africa.com>` (Marketing-Stream, getrennt von Transaktional).

### A1 — Willkommen (Tag 0, sofort nach E-Mail-Bestätigung)

**Subject:** Welcome to Voltage Africa — your profile is live

```
Hi {{first_name}},

Welcome to Voltage Africa. Your account is confirmed and your
technician profile has been created.

Voltage Africa connects skilled technicians — electricians, solar
installers, IT specialists and more — with customers in your city.

Here's how it works:
1. Complete your profile (trade, city, experience, photo)
2. Get ranked and collect XP/VIP points for activity and good work
3. Receive job requests that match your trade and location

First step: complete your profile. It takes about 10 minutes.
Complete my profile: {{profile_url}}

Questions? Reply to this email or message us on WhatsApp:
{{whatsapp_link}}

— The Voltage Africa team
```

### A2 — Profil vervollständigen (Tag 2, nur wenn Profil < 100 %)

**Subject:** Customers can't find you yet — 3 things missing

```
Hi {{first_name}},

Your profile is {{profile_completion}}% complete. Customers in
{{city}} searching for a {{trade}} see complete profiles first.

Your profile is still missing:
{{missing_fields_list}}

Each missing item takes less than 3 minutes to add.

Finish my profile: {{profile_url}}

Tip: Profiles with a clear photo and a short description of past
work receive significantly more inquiries.

— The Voltage Africa team
```

### A3 — Erstes Ranking/XP (Tag 4, nur wenn Ranking/XP erstmals sichtbar)

**Subject:** You're ranked — here's your starting XP

```
Hi {{first_name}},

Your profile is now listed in the {{city}} {{trade}} rankings.

Your current status:
- Rank: {{rank_position}} ({{city}}, {{trade}})
- XP points: {{xp_points}}

How XP and VIP points work:
You earn points for a complete profile, fast replies to customer
requests, and confirmed completed jobs with good reviews. Points
reflect activity and reliability — they are not money and have no
cash value.

The fastest way to climb: reply to every customer request within
24 hours, even if you have to decline.

See my ranking: {{rankings_url}}

— The Voltage Africa team
```

### A4 — Reaktivierung (Tag 7, nur wenn keine Anfrage beantwortet und keine Aktivität seit Tag 3)

**Subject:** A customer in {{city}} might be looking for you

```
Hi {{first_name}},

We noticed you haven't been active since you joined. No problem —
but customers in {{city}} are submitting requests for {{trade}}
work, and inactive profiles drop in the rankings.

Two quick things you can do in under 5 minutes:
1. Log in and check open requests: {{requests_url}}
2. Make sure your availability status is set to "available"

If you're no longer interested, you can pause your profile here:
{{pause_url}} — or unsubscribe below.

— The Voltage Africa team

Unsubscribe: {{unsubscribe_url}}
```

### A5 — So bekommst du deinen ersten Auftrag (Tag 10)

**Subject:** How to land your first job on Voltage Africa

```
Hi {{first_name}},

Technicians who get their first job quickly usually do five things
differently:

1. Reply fast — aim for under 24 hours
2. Write 2-3 sentences about a real past job in your profile
3. Set a realistic rate — check what the calculator suggests for
   your city: {{calculator_url}}
4. Ask every satisfied customer for a review on the platform
5. Keep your availability up to date

None of this guarantees a job — matches depend on customer demand
in your city and trade. But these steps are what you control.

Open requests near you: {{requests_url}}

— The Voltage Africa team

Unsubscribe: {{unsubscribe_url}}
```

---

## 3. Sequenz B — Kunden-Journey (4 E-Mails)

### Design-Spec

- **Trigger:** Anfrage über request.html/hire.html abgesendet (Status `request_created` im Backend).
- **Segment:** `role=customer`, `request_status != cancelled`; Sprachattribut; Ausschluss: Abmeldung, Bounce.
- **Austrittsregeln:** (1) Anfrage storniert → nur transaktionale Storno-Mail, (2) Abmeldung, (3) Beschwerde/Bounce, (4) Referral-Mail versendet = Sequenzenende.
- **Wichtig:** Statusangaben in den Mails nur aus bestätigten Backend-Statusdaten, keine erfundenen Fortschritte.

### B1 — Anfrage erhalten / Bestätigung (sofort)

**Subject:** We received your request — what happens next

```
Hi {{first_name}},

Thank you — we received your request:

Trade: {{trade}}
City: {{city}}
Description: {{request_summary}}
Reference: {{request_id}}

What happens next:
1. We match your request with available, ranked technicians in
   {{city}}
2. Suitable technicians receive your request and can respond
3. You get notified as soon as a technician accepts

You can track the status anytime: {{request_status_url}}

Fastest contact: WhatsApp {{whatsapp_link}}

— The Voltage Africa team
```

### B2 — Vermittlung unterwegs (Trigger: Status `technician_assigned` / erste positive Antwort)

**Subject:** Good news — a technician is on it

```
Hi {{first_name}},

Your request {{request_id}} ({{trade}}, {{city}}) has been picked
up by a technician:

Name: {{technician_name}}
Trade: {{trade}}
Ranking: {{technician_rank}} ({{city}})

Next step: agree on scope, timing and price directly with the
technician. Voltage Africa facilitates the match; the work contract
is between you and the technician.

View the match: {{request_status_url}}

— The Voltage Africa team
```

### B3 — „Wie lief es?" / Review-Anfrage (7 Tage nach Status `completed`)

**Subject:** How did it go with {{technician_name}}?

```
Hi {{first_name}},

Your job {{request_id}} ({{trade}}, {{city}}) with
{{technician_name}} was marked as completed a week ago.

How did it go? Your honest review takes 2 minutes and helps other
customers in {{city}} choose well. It also helps good technicians
climb the rankings.

Leave a review: {{review_url}}

If something went wrong, please tell us directly first so we can
help: {{support_url}} — or WhatsApp {{whatsapp_link}}

— The Voltage Africa team
```

### B4 — Referral-Einladung (30 Tage nach Review oder 45 Tage nach Abschluss)

**Subject:** Know someone who needs a good technician?

```
Hi {{first_name}},

You recently found a {{trade}} in {{city}} through Voltage Africa.

If you know someone — a neighbour, a business, a family member —
who needs a reliable electrician, solar installer or IT specialist,
you can send them your personal link:

{{referral_link}}

When they submit their first request, you'll both be notified.

Thank you for trusting Voltage Africa.

— The Voltage Africa team

Unsubscribe: {{unsubscribe_url}}
```

---

## 4. Sequenz C — Scout-Aktivierung (4 E-Mails)

### Design-Spec

- **Trigger:** Registrierung als Scout + E-Mail bestätigt.
- **Segment:** `role=scout`, `email_verified=true`; Ausschluss: Abmeldung, Bounce.
- **Austrittsregeln:** (1) Abmeldung, (2) Hard Bounce/Beschwerde, (3) 90 Tage inaktiv.
- **Compliance-Hinweis:** Keine konkreten Provisionsbeträge in den Texten — Konditionen sind laut Website-Kontext nicht verifiziert. Texte verweisen auf scout-guide.html als Quelle der jeweils aktuellen Bedingungen. Vor Versand müssen die tatsächlichen Konditionen eingesetzt oder der Verweis geprüft werden.

### C1 — Willkommen (Tag 0)

**Subject:** Welcome, Scout — here's your toolkit

```
Hi {{first_name}},

Welcome to Voltage Africa as a Scout. Scouts connect skilled
technicians with the platform — and help good work get found.

Your starting toolkit:
1. Your personal referral link: {{scout_link}}
2. The Scout guide with current terms: {{scout_guide_url}}
3. Your Scout dashboard: {{scout_dashboard_url}}

Your first goal: refer one technician you personally know and can
vouch for. Quality beats quantity — referred technicians reflect
on your Scout reputation.

— The Voltage Africa team
```

### C2 — So funktioniert Vermitteln (Tag 3)

**Subject:** How scouting works, step by step

```
Hi {{first_name}},

Here's how a successful referral works:

1. Share your link with a technician you know: {{scout_link}}
2. They register and complete their profile
3. When their profile goes live, it counts as your referral
4. You track every referral in your dashboard:
   {{scout_dashboard_url}}

What makes a good referral:
- Technicians with real, verifiable experience
- Trades in demand in their city (electricians, solar, IT)
- People who will actually respond to customer requests

Current terms and conditions are always in the Scout guide:
{{scout_guide_url}}

— The Voltage Africa team
```

### C3 — Erste Vermittlung feiern (Trigger: erster Referral mit live geschaltetem Profil)

**Subject:** Your first referral just went live 🎉

```
Hi {{first_name}},

Congratulations — {{technician_first_name}}, referred by you, just
completed their profile and is now live on Voltage Africa in
{{city}}.

You can follow their progress in your dashboard:
{{scout_dashboard_url}}

What happens from here: when your referred technicians become
active and complete jobs, you can see it in your Scout statistics.
Check the Scout guide for the current conditions that apply:
{{scout_guide_url}}

Ready for the next one? {{scout_link}}

— The Voltage Africa team
```

### C4 — Monats-Recap (monatlich, am 1., nur bei ≥ 1 Aktivität im Vormonat)

**Subject:** Your Scout recap for {{month}}

```
Hi {{first_name}},

Your Scout activity for {{month}}:

- New referrals registered: {{referrals_registered}}
- Referrals with live profiles: {{referrals_live}}
- Active referred technicians: {{referrals_active}}
- Your Scout rank: {{scout_rank}}

Full details: {{scout_dashboard_url}}

{{#if referrals_live_eq_0}}
Tip: Your referrals are registered but haven't completed their
profiles yet. A quick personal nudge often helps — profiles that
go live start receiving requests.
{{/if}}

Keep connecting good people with good work.

— The Voltage Africa team

Unsubscribe: {{unsubscribe_url}}
```

---

## 5. Transaktionale Mails (Systemmails)

**Absender-Regel:** Eigener Absender/Stream `no-reply@voltage-africa.com`, getrennt vom Marketing-Absender. Keine Marketing-Inhalte in transaktionalen Mails. Keine Abmeldepflicht für rein transaktionale Mails, aber Impressum/Identität bleibt.

| # | Mail | Trigger | Kurztext-Vorschlag (Betreff + Kernzeile) |
|---|------|---------|------------------------------------------|
| T1 | E-Mail-Bestätigung (Signup) | Supabase Auth `signup` | „Confirm your Voltage Africa account" — „Confirm your email address to activate your account: {{confirmation_url}}" |
| T2 | Magic Link / OTP Login | Auth `magiclink`/`recovery` | „Your Voltage Africa sign-in link" — „Sign in here (link valid for 1 hour): {{magic_url}}" |
| T3 | Passwort zurücksetzen | Auth `recovery` | „Reset your password" — „Reset your password here: {{reset_url}}. If you didn't request this, ignore this email." |
| T4 | E-Mail-Änderung | Auth `email_change` | „Confirm your new email address" — an alte + neue Adresse, beide Links |
| T5 | Anfrage eingegangen | `request_created` | = B1 (doppelt als transaktional; bei Trennung: kurze Version ohne Marketing-CTA) |
| T6 | Anfrage-Status geändert | `request_status_changed` | „Update on your request {{request_id}}" — „New status: {{status}}. Details: {{request_status_url}}" |
| T7 | Matching-Benachrichtigung an Techniker | `request_matched` | „New {{trade}} request in {{city}}" — „A customer request matches your profile. Respond within 24h to protect your ranking: {{request_url}}" |
| T8 | Techniker hat angenommen (an Kunde) | `technician_accepted` | = B2 (transaktionale Kurzversion ohne Werbesprache) |
| T9 | Anfrage storniert | `request_cancelled` | „Your request {{request_id}} was cancelled" — Grund + Link zum Neu-Erstellen |
| T10 | Review-Erinnerung (Fallback) | `completed` + 14 Tage ohne Review | „Reminder: review {{technician_name}}" — ein Satz + {{review_url}} |

**Umsetzung T1–T4:** über Supabase Auth — entweder Custom SMTP (einfachste Variante) oder Send-Email-Hook + Edge Function (eigene Templates, React Email möglich) [Quelle: Supabase Docs „Send emails with custom SMTP" und „Send Email Hook", abgerufen 2026-09-21].

**Umsetzung T5–T10:** Database Webhook bzw. Edge Function auf Statusänderung → ESP-API.

---

## 6. Tool-Empfehlung: Brevo

### Optionenbewertung (Quellen jeweils mit Abrufstand 2026-09-21)

**Option 1: Supabase Auth Hooks + Edge Function + Resend**
- Resend: Free Tier 3.000 Mails/Monat (100/Tag), danach ab ~20 USD/Monat (50.000 Mails) [Quelle: Venture Harbour „The Best Transactional Email Services in 2026", Stand 2026-07; TrueAbility/MailerToGo-Vergleich 2026-06].
- Offizielle Supabase-Integration (Custom SMTP oder Send-Email-Hook), gute DX [Quelle: Supabase Partner-Katalog Resend; Supabase Docs, 2026-09].
- Nachteil: Lifecycle-Sequenzen müssen komplett selbst gebaut werden (DB-Tabellen, Cron, Edge Functions). Kein visueller Automation-Builder. Für ein kleines Team = hoher laufender Engineering-Aufwand.

**Option 2: AWS SES**
- Günstigster Stückpreis: ~0,10 USD / 1.000 Mails [Quelle: mehrere Vergleiche, Stand 2026].
- Aber: SES-Free-Tier für Neukunden am 21.07.2026 eingestellt [Quelle: Dreamlit-Vergleich, 2026-08]; hohes Setup (IAM, Sandbox-Freischaltung, DKIM/SPF manuell, Bounce-Handling selbst bauen). Für kleines Team ungeeignet.

**Option 3: Brevo (ehem. Sendinblue)** ✅ Empfehlung
- Free Tier: 300 Mails/Tag (~9.000/Monat), dauerhaft, ohne Kreditkarte; danach ab ~25 USD/Monat (20.000 Mails) [Quelle: Venture Harbour 2026-07; cloudserverforemail-Vergleich 2026-04; tinysend-Vergleich 2026-03].
- Deckt **alle drei Anforderungen in einem Tool ab**: (a) SMTP für Supabase Auth (Brevo ist in der offiziellen Supabase-SMTP-Liste) [Quelle: Supabase Docs „Send emails with custom SMTP", 2026-09-21], (b) Transaktionale Mails via API mit eigenem Stream, (c) visueller Automation-Builder für die 3 Sequenzen inkl. Wenn/Dann-Logik und Austrittsregeln — **kein eigener Sequenz-Code nötig**.
- EU-Anbieter (Frankreich), DSGVO-freundlich, AVV verfügbar [Quelle: cloudserverforemail, 2026-04 — „EU-based; GDPR-friendly"].
- Volumen- statt Kontaktpreis (Mailchimp: kontaktbasiert ab ~13 USD/Monat für 500 Kontakte, wird bei wachsender Liste schnell teuer [Quelle: cloudserverforemail, 2026-04]).

**Kostenabschätzung Frühphase (grob):**
- < 9.000 Mails/Monat (≈ 300/Tag): **0 EUR**. Bei 13 Sequenz-Mails + ~10 Transaktional reicht das für ca. 300–700 neue Nutzer/Monat je nach Mix.
- Wachstum: Brevo Starter ~25 USD/Monat (20.000 Mails).
- Tageslimit beachten: 300/Tag kann bei Launch-Spitzen eng werden → Transaktionale Mails ggf. auf Resend Free (100/Tag) als zweiten Stream auslagern. Beide Tools parallel sind free-tier-kompatibel.

**Aufwand:** ~1 Tag Setup (Domain verifizieren, SPF/DKIM, Supabase-SMTP eintragen, 3 Automationen bauen, Attribute mappen). Kein Engineering-Dauerauftrag.

### Minimale technische Architektur

```
Supabase Auth ──(Custom SMTP)──► Brevo ──► T1–T4 (Auth-Mails)
DB-Statusänderung ──(Webhook/Edge Fn)──► Brevo API ──► T5–T10
Nutzer-Event (Signup/Status) ──► Brevo Kontakt-Attribut ──► Automation A/B/C
```

---

## 7. Rechtliches Minimum

**Kein Rechtsrat.** Die folgenden Punkte sind Umsetzungs-Minimum und müssen je Zielstaat (Betreiber-Sitz und Kundenländer) von Rechtsbeistand geprüft werden.

1. **Double-Opt-In für Marketing-Mails:** Die Supabase-E-Mail-Bestätigung bestätigt die Adresse, ist aber **keine** dokumentierte Marketing-Einwilligung. Sequenz-Mails mit Marketing-Charakter (A4, A5, B4, C2–C4) benötigen eine separate, protokollierte Einwilligung (Datum, Zeit, Methode, Quelle, Umfang — DSGVO Art. 7) oder eine geprüfte andere Rechtsgrundlage. Rein transaktionale/vertragsnotwendige Mails (T1–T10, B1–B3) sind davon grundsätzlich getrennt zu beurteilen.
2. **Abmeldung:** 1-Klick-Unsubscribe (RFC 8058) + `List-Unsubscribe`-Header in jeder Marketing-Mail; Abmeldung muss technisch tatsächlich funktionieren und sofort greifen (vor erstem Versand testen — Skill-Vorgabe).
3. **Impressum/Absender:** Vollständige Anbieterkennzeichnung (Name, Anschrift, Kontakt) in jeder Mail; Absenderdomain verifiziert (SPF/DKIM/DMARC — Google/Yahoo/Microsoft erzwingen dies seit 2024/2025).
4. **Trennung der Streams:** Transaktional und Marketing über getrennte Absenderadressen/IP-Pools; keine Werbung in transaktionalen Mails.
5. **Datenminimierung:** Nur erforderliche Attribute an den ESP übertragen; AVV mit Brevo abschließen; Lösch-/Anonymisierungsregel für inaktive Kontakte (z. B. 12–24 Monate ohne Engagement) dokumentieren.
6. **Zielstaaten:** Kunden und Techniker sitzen in verschiedenen afrikanischen Staaten mit jeweils eigenem Datenschutzrecht (z. B. POPIA Südafrika, NDPR Nigeria, Kenia DPA 2019). Je Land prüfen lassen — kein „Afrika-Pauschalurteil".

---

## 8. Kennzahlen je Sequenz (Frühphasen-Ziele)

Messgrundsatz: Post-Apple-MPP sind Öffnungsraten nur richtungsweisend. Primär: CTR, CTOR, Zielaktion. Quellen der Benchmarks: Persona-Standardwerte (Branchenbenchmarks 2025/2026), **nicht** gemessene Voltage-Daten.

### Sequenz A — Techniker-Onboarding
| Kennzahl | Frühphase „gut" | Alarm |
|----------|------------------|-------|
| Zielaktion: Profil 100 % nach A2 | ≥ 40 % der Empfänger | < 20 % |
| CTR gesamt | > 3 % | < 1,5 % |
| CTOR | > 10 % | < 5 % |
| A4-Reaktivierung (Login ≤ 72 h) | ≥ 15 % | < 5 % |
| Abmelderate Sequenz | < 0,5 % | > 1 % |

### Sequenz B — Kunden-Journey
| Kennzahl | Frühphase „gut" | Alarm |
|----------|------------------|-------|
| B1→B2 Rate (Anfrage → Match) | ≥ 60 % | < 30 % (Angebotsproblem, kein Mail-Problem) |
| B3 Review-Rate | ≥ 10 % | < 3 % |
| B4 Referral-Klickrate | > 2 % CTR | < 0,5 % |
| Beschwerderate | < 0,05 % | > 0,10 % |

### Sequenz C — Scout-Aktivierung
| Kennzahl | Frühphase „gut" | Alarm |
|----------|------------------|-------|
| C1→erster Referral-Link-Klick | ≥ 30 % | < 10 % |
| Scouts mit ≥ 1 live-Referral (30 Tage) | ≥ 15 % | < 5 % |
| C4 CTR | > 5 % | < 2 % |

### System-Kennzahlen (alle Sequenzen)
- Hard Bounces < 1 %, sofort entfernen; Soft Bounces nach 3–5 Fehlversuchen suppressen.
- Beschwerderate < 0,10 % Ziel, 0,30 % hartes Limit (Google/Yahoo-Enforcement).
- Inbox-Placement > 95 %; Google Postmaster Tools einrichten.

---

## 9. Drei nächste Maßnahmen

1. **Tool-Setup (Woche 1):** Brevo-Konto anlegen, voltage-africa.com verifizieren (SPF/DKIM/DMARC), Brevo-SMTP in Supabase Auth eintragen, Auth-Templates T1–T4 anpassen, Testversand an 3 Testadressen (Gmail, Outlook, Apple Mail) inkl. Abmelde-Test.
2. **Consent- und Rechtsprüfung (Woche 1–2):** Klären, welche Rechtsgrundlage für die Marketing-Mails je Zielland gilt (Betreiber-Sitz + erste Zielländer), DOI-Protokollierung definieren (Feld `marketing_consent_at` + Quelle), Impressumsblock finalisieren — mit Rechtsbeistand, nicht intern.
3. **Sequenz A live, Messbasis (Woche 2–3):** Nur Techniker-Onboarding in Brevo-Automation bauen (Trigger: `role=technician` + `email_verified`), Platzhalter-Mapping aus Supabase prüfen (`{{city}}`, `{{trade}}`, `{{profile_completion}}` müssen real befüllbar sein), nach 14 Tagen erste CTR/Profilvollständigkeits-Auswertung — dann B und C nachziehen.

---

*Erstellt von Lifecycle_Stratege. E-Mail-Texte sind Entwürfe; Versand nur nach autorisierter Freigabe, funktionierender Abmeldung und Rechtsprüfung. Keine Backend-Daten, Zustellraten oder Provisionskonditionen wurden verifiziert; alle Platzhalter müssen vor Versand gegen echte Datenquellen geprüft werden.*
