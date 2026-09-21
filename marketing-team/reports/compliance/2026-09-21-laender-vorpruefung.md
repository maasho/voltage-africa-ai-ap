# Länderspezifische Compliance-Vorprüfung – Tier-1-Märkte

**Rolle:** Compliance_Pruefer (Legal Compliance Checker, Voltage-Africa-Marketingteam)
**Datum:** 2026-09-21
**Geltungsbereich:** Nigeria, Kenia, Ghana, Südafrika (Tier 1) + DSGVO-Perspektive (Betreiber Deutschland, Hosting Supabase eu-central-1)
**Charakter:** Strukturierte Vorprüfung, **keine Rechtsberatung**. Jeder Befund ist mit Quelle, Unsicherheit und nächstem Schritt versehen. Verbindliche Aussagen erfordern Fachanwalt bzw. die zuständige Behörde im jeweiligen Land.

**Sachverhalt (vorgegeben):** Voltage Africa vermittelt Elektriker, Solarinstallateure, Techniker und IT-Fachkräfte in Afrika. Plattformbetreiber in Deutschland, Datenhaltung bei Supabase in eu-central-1 (EU), Nutzer in den Zielmärkten. Keine Plattform-Zahlungen; XP/Punkte ohne Geldwert (laut terms.html). Scout-Provisionen diskutiert, nicht implementiert.

---

## 1. Zusammenfassung

1. **Datenschutz-Registrierungspflichten sind das konkreteste Sofortthema.** Kenia (ODPC, Registrierung ist Straftatbestand bei Unterlassen) und Ghana (DPC, Registrierung vor Verarbeitungsbeginn, alle 2 Jahre erneuern) verlangen förmliche Registrierung; Nigeria verlangt Registrierung als DCPMI ab relativ niedrigen Schwellen (u. a. 200 Betroffene in 6 Monaten oder Sektorzuordnung, u. a. „e-commerce"/„electric power"); Südafrika verlangt stattdessen die Registrierung eines Information Officer + PAIA-Manual.
2. **Vermittlungsrecht ist der strukturell größte Klärungsbedarf.** Alle vier Märkte kennen Lizenz-/Registrierungspflichten für private Arbeitsvermittlung. Ob eine reine Marktplatz-/Matching-Plattform ohne Vertragspartei-Position darunter fällt, ist je Land unterschiedlich und nicht aus der Ferne abschließend zu beantworten — besonders heikel, sobald Scout-Provisionen oder erfolgsabhängige Vergütung ins Spiel kommen. Ghana § 7(7) Labour Act (50-%-Rückerstattungspflicht gegenüber Jobsuchenden) und das weit verbreitete Verbot, Jobsuchenden Gebühren zu berechnen (Südafrika § 15 ESA; Kenia), müssen vor jeder Monetarisierung geprüft werden.
3. **Gewerke-Zertifizierung ist gut kartierbar und sollte den „verified"-Prozess direkt prägen:** Nigeria NEMSA (Personenzertifizierung + Installationsabnahme), Kenia EPRA (Elektriker-Klassen A/B/C, Solar T1–T3, Firmen C1/V1/V2), Ghana CEWP/CEWI nach L.I. 2008 (Form A für Netzanschluss), Südafrika DoEL-registrierte Person (Wireman's Licence) + CoC nach SANS 10142-1. Alle vier Regulierer führen öffentlich prüfbare Register — Verifikation per Registerabgleich ist technisch machbar und sollte Pflichtbestandteil von „verified" werden.
4. **Werberecht:** Nigeria ist der kritischste Werbemarkt (ARCON-Vorab-Vettingpflicht inkl. Social Media/Influencer, Mindeststrafen ab ₦500.000, Local-Content-Vorgaben, Naira-Preisangabe). Südafrika: CPA §§ 29/41 + ARB-Code. Kenia: Consumer Protection Act § 12, Competition Act, CA-Standards. Ghana: kein zentrales Werbe-Vetting für Dienstleistungen, aber FDA-Vorabgenehmigung für regulierte Produkte; allgemeine Irreführungsverbote (u. a. Electronic Transactions Act § 110).
5. **DSGVO:** Als deutscher Verantwortlicher gilt die DSGVO voll (Art. 3 Abs. 1) — unabhängig vom Standort der Nutzer. EU-Hosting vermeidet Drittlandtransfer-Problematik auf EU-Seite; AVV mit Supabase nach Art. 28 ist Pflichtnachweis. Umgekehrt müssen die Zielmärkte den Transfer ihrer Inlandsdaten in die EU jeweils national rechtlich freigeben (Kenia §§ 48–49 DPA: Safeguards/Adequacy-Nachweis; Nigeria: GAID-Cross-Border-Regeln; Südafrika § 72 POPIA: Vertrag/Einwilligung; Ghana: überwiegend Einwilligungs-/Rechtmäßigkeitslogik).

**Kritischstes Einzelrisiko:** Betrieb als nicht registrierter/lizenzierter Datenverarbeiter und ggf. nicht lizenzierter Vermittler in Kenia und Nigeria — beides dort aktiv vollzogene Regime mit Geld- bzw. Strafschärfe (Kenia: Registrierungsverstoß strafbewehrt; Nigeria: NDPC-Bußgelder in dreistelliger Millionenhöhe bei Big Tech dokumentiert).

---

## 2. Datenschutz je Land

### 2.1 Nigeria — Nigeria Data Protection Act (NDPA) 2023 + GAID 2025

- **Rechtsrahmen/Behörde:** NDPA 2023 (Präsidialassent 12.06.2023), Nigeria Data Protection Commission (NDPC); operative Durchführungsrichtlinie GAID 2025 (erlassen 20.03.2025, wirksam ab 19.09.2025; ersetzt NDPR 2019). [Quelle: DLA Piper Data Protection Laws of the World – Nigeria, Stand 17.03.2026; regulations.ai, 13.06.2026]
- **Extraterritorialität/Targeting:** GAID erfasst auch Controller/Prozessoren ohne Sitz in Nigeria, wenn sie Betroffene in Nigeria „targeten". Eine deutsch betriebene Plattform mit nigerianischen Nutzern fällt grundsätzlich in den Anwendungsbereich. [Quelle: DLA Piper, 17.03.2026; Unsicherheit: Einzelfall-Auslegung „targeting" durch NDPC]
- **Registrierung (DCPMI):** Registrierungspflicht für „Data Controllers/Processors of Major Importance"; Schwellen u. a. 200+ Betroffene in 6 Monaten (OHL-Einstiegsstufe; EHL 1.000–4.999; UHL 5.000+) oder Zugehörigkeit zu 14 designierten Sektoren (u. a. „electric power", „e-commerce", „communication"). Registrierung innerhalb von 6 Monaten nach erstmaligem Qualifizieren; Gebühren laut Sekundärquellen ₦25.000 (Small Business) bis ₦250.000 (Major). [Quelle: recordinglaw.com Nigeria-Guide, 20.05.2026; ndprtoolkit.com.ng, 01.04.2026 — Sekundärquellen, Schwellen/Gebühren gegen GAID-Original und NDPC-Portal verifizieren]
- **DPO:** Alle DCPMIs müssen einen qualifizierten DPO benennen (intern oder extern), Berichtslinie an oberste Leitungsebene. [Quelle: recordinglaw.com, 20.05.2026]
- **Audits/CAR:** Jährliche Compliance Audit Returns (UHL/EHL über lizenzierte DPCO), Frist 31.03. bzw. verlängert; Verspätungszuschlag 50 %. [Quelle: SHQ Legal, 12.05.2026; recordinglaw.com, 20.05.2026]
- **Betroffenenrechte:** Auskunft, Berichtigung, Löschung, Widerspruch, Einschränkung; Beschwerdeweg SNAG. Breach-Meldung an NDPC binnen 72 h, bei hohem Risiko unverzüglich an Betroffene. [Quelle: SHQ Legal, 12.05.2026]
- **Datenlokalisierung:** Kein generelles Lokalisierungsgebot für diesen Plattformtyp gefunden; Cross-Border-Transfers an NDPC-Mechanismen (SCCs/BCRs/Adequacy) gebunden — alte „Whitelist"-Logik nicht mehr auf Bestand verlassen. [Quelle: recordinglaw.com, 20.05.2026; Unsicherheit: sektorale Ausnahmen möglich]
- **Bedeutung für Voltage Africa:** Plattform verarbeitet Profile/Identitäts-/Qualifikationsdaten → bei >200 nigerianischen Nutzern in 6 Monaten oder E-Commerce-Einordnung Registrierung + DPO + ggf. CAR. Verarbeitung von Zertifikatsdaten (NEMSA) ist personenbezogen und sensibilitätsnah (berufliche Identität).
- **Nächster Schritt:** DCPMI-Einstufung mit nigerianischem Datenschutzpraktiker bestätigen; EU-basiertes Transfermodell (GAID-SCCs) dokumentieren.

### 2.2 Kenia — Data Protection Act 2019 (No. 24 of 2019)

- **Rechtsrahmen/Behörde:** DPA 2019 + drei Verordnungen von 2021 (Registration, General, Complaints/Enforcement); Office of the Data Protection Commissioner (ODPC). [Quelle: DLA Piper – Kenia, 23.03.2026]
- **Registrierung:** § 18 — Registrierung aller Controller/Prozessoren beim ODPC **vor Verarbeitungsbeginn**; Zertifikat 24 Monate gültig, Erneuerung nötig. Ausnahme nur bei < KES 5 Mio. Umsatz UND < 10 Mitarbeitern — aber bestimmte Zweck-/Sektorkategorien registrierungspflichtig unabhängig von Schwellen. **Nichtregistrierung ist Straftat** (bis KES 3 Mio. bzw. Freiheitsstrafe bei Individuen laut Sekundärquelle). Extraterritorial: gilt auch für ausländische Anbieter mit Nutzern in Kenia. [Quellen: DLA Piper, 23.03.2026; ODPC Statement „Commencement of Registration", 14.07.2022; isols.io, o. D.; dimeri.ai, 17.04.2026]
- **DPO:** Nicht generell Pflicht; erforderlich je nach Verarbeitungsumfang/-art (u. a. large-scale processing). Für eine Profilplattform mit Bewertungen/Rankings ist die DPO-Benennung realistischerweise anzunehmen. [Quelle: Bowmans Africa Guide 2024/2025; flexyconsent.com, 10.07.2026; Unsicherheit: konkrete Schwellen aus General Regulations gegenlesen]
- **Datenlokalisierung:** Kein generelles Gebot; Cabinet Secretary kann sektoral Lokalisierung anordnen (bisher u. a. Bildung/Gesundheit). Für den Plattformtyp derzeit keine Lokalisierungspflicht erkennbar. [Quelle: Bowmans Guide 2025]
- **Betroffenenrechte:** Auskunft, Berichtigung, Löschung, Widerspruch, Portabilität (§ 35); DSAR-Praxis i. d. R. 30 Tage. Breach: 72 h an ODPC bei „real risk of harm". [Quellen: dimeri.ai, 17.04.2026; isols.io]
- **Cross-Border (Kenia → EU):** § 48 — Transfer nur mit Nachweis geeigneter Garantien/Adequacy oder Einwilligung/Notwendigkeit; sensible Daten verschärft. EU-Hosting ist ein starkes Argument, der **Nachweis** (Vertrag/Safeguards-Dokumentation) muss trotzdem geführt werden. [Quelle: scanner.bdemerson.com, o. D. (2026)]
- **Bußgeldrahmen:** bis KES 5 Mio. oder 1 % Jahresumsatz (Controller), strafbewehrt bis 10 Jahre für bestimmte Delikte; ODPC vollzieht sichtbar (Namensnennung, Penalty Notices). [Quellen: DLA Piper; bdemerson.com]
- **Nächster Schritt:** ODPC-Registrierung über Portal (odpc.go.ke) vorbereiten; Transfer-Dokumentation (Safeguards für EU-Transfer) erstellen; DPO-Frage anwaltlich festnageln.

### 2.3 Ghana — Data Protection Act 2012 (Act 843)

- **Rechtsrahmen/Behörde:** Act 843 (in Kraft seit 16.10.2012); Data Protection Commission (DPC), Accra. Ein Nachfolgegesetz (Data Protection Bill 2025) ist in Arbeit, bislang nicht verabschiedet — Act 843 bleibt maßgeblich. [Quellen: DLA Piper – Ghana, 18.03.2026; recordinglaw.com Ghana-Guide, 20.05.2026]
- **Registrierung:** Jeder Controller muss sich **vor Verarbeitungsbeginn** beim DPC registrieren; nicht in Ghana inkorporierte Controller registrieren sich als „external company". Zertifikat 2 Jahre gültig, Erneuerungspflicht; öffentliches Register. Verarbeitung ohne Registrierung ist Straftat (bis 250 Penalty Units ≈ GHS 3.000 bzw. bis 2 Jahre Haft). [Quellen: DLA Piper, 18.03.2026; Wikipedia/Gesetzestext §§ 46–56; Ndowuona & Company]
- **DPO/DPS:** Gesetzlich kein DPO-Zwang; DPC verlangt praktisch von großen Controllern einen zertifizierten „Data Protection Supervisor"; bei Erneuerung Gap-Analysis-Bericht inkl. DPIA, Retention Policy, Incident/Breach Report; jährliche Pflichtschulung aller datenberührenden Mitarbeiter. [Quellen: DLA Piper, 18.03.2026; aosphere Rulefinder Ghana]
- **Betroffenenrechte:** Zugang, Berichtigung, Widerspruch gegen Direktmarketing, Rechte bei automatisierter Entscheidung, Schadensersatz bei Verstoß; Antwortfristen teils 40 Tage. Breach: Meldung an DPC und Betroffene „as soon as reasonably practicable" (§ 31). [Quellen: Lexology/Gesetzestext; recordinglaw.com]
- **Datenlokalisierung:** Keine expliziten Lokalisierungspflichten; Cross-Border über allgemeine Rechtmäßigkeits-/Einwilligungslogik. [Quelle: Grokipedia-Zusammenfassung (Autorität C — gegen Gesetzestext zu verifizieren)]
- **Bedeutung für Voltage Africa:** Registrierung als „external company" ist der konkrete erste Pflichtschritt für Ghana-Nutzer; Schulungs- und Gap-Analysis-Dokumentation aufsetzen.
- **Nächster Schritt:** DPC-Registrierung (Enhanced Registration Portal) einleiten; Penalty-Unit-Stand (GHS 12/Einheit, 17.03.2026) bei Budgetierung beachten.

### 2.4 Südafrika — POPIA (Act 4 of 2013) + PAIA

- **Rechtsrahmen/Behörde:** POPIA, voll vollzogen seit 01.07.2021; Information Regulator (South Africa). Ergänzend PAIA (Promotion of Access to Information Act). [Quellen: sitegrade.io, 20.04.2026; termsbox.com, 30.07.2026]
- **Anwendbarkeit:** Gilt für „responsible parties" mit Sitz in SA **oder** bei Nutzung von Verarbeitungsmitteln in SA (Server, Cookies auf SA-Geräten etc.). Eine reine EU-Verarbeitung ohne SA-Mittel liegt grenznah außerhalb — **Unsicherheit:** Auslegung bei aktivem SA-Marketing/Cookies anwaltlich klären. [Quelle: sitegrade.io, 20.04.2026]
- **Registrierung:** Keine Controller-Registrierung; stattdessen **Information Officer** (Default: Unternehmensleitung) beim Information Regulator registrieren (kostenlos, Online-Portal) + **PAIA-Manual** öffentlich bereitstellen. Beides aktiv durchgesetzte Standardverstöße. [Quellen: clearcomply.co.za, 26.05.2026; termsbox.com]
- **Betroffenenrechte:** Zugang, Berichtigung/Löschung, Widerspruch; Antwortfristen nach PAIA (i. d. R. 30 Tage); Direktmarketing elektronisch nur mit Opt-in (§ 69, „Form 4"-Einwilligung) — relevant für Scout-/Nutzer-Kampagnen. Breach: Meldung an Regulator + Betroffene; seit 2025 über verbindliches E-Portal. [Quellen: vucense.com, 29.07.2026; biscotti-cmp.com, 07.07.2026]
- **Cross-Border (§ 72):** Transfer außerhalb SA nur mit vergleichbarem Schutzniveau, bindender Vereinbarung oder informierter Einwilligung. EU-Hosting erfüllt das Niveau-Kriterium faktisch, dokumentiert werden muss es trotzdem. [Quelle: sitegrade.io]
- **Sanktionen:** bis R10 Mio. bzw. bis 10 Jahre Haft; bisher zwei R5-Mio.-Bußgelder; Schwerpunkte 2025/26: Direktmarketing und Breach-Management. [Quelle: clearcomply.co.za, 26.05.2026]
- **Nächster Schritt:** Anwendbarkeitsfrage (means in SA) klären; falls ja: IO-Registrierung, PAIA-Manual, Opt-in-Prozess für elektronisches Direktmarketing.

### 2.5 DSGVO-Perspektive (Betreiber Deutschland)

- **Anwendbarkeit:** DSGVO gilt kraft Art. 3 Abs. 1 für den deutschen Verantwortlichen — auch für Verarbeitung von Daten afrikanischer Nutzer. Betroffene in Afrika haben volle DSGVO-Rechte (Art. 12–22). [Quelle: DSGVO-Gesetzestext — allgemein]
- **Auftragsverarbeitung:** Supabase (Projekt in eu-central-1/Frankfurt) als Auftragsverarbeiter → AVV nach Art. 28 Pflicht; Unterauftragsverarbeiter und etwaige US-Muttergesellschafts-Zugriffe (Supabase Inc., USA) prüfen — hier kann indirekt ein Drittlandbezug entstehen (SCC/TOMs). [Quelle: DSGVO Art. 28, 44 ff.; Unsicherheit: konkrete Supabase-DPA-Konfiguration des Projekts nicht eingesehen — Nachweis einholen]
- **EU-seitige Transferproblematik entfällt weitgehend:** Erhebung von Daten direkt bei Betroffenen in Drittländern in die EU ist kein „Transfer" i. S. d. Kapitel V; kritisch sind umgekehrt die Ausfuhr-Regeln der Herkunftsländer (s. o.).
- **Weitere deutsche Pflichten:** Verarbeitungsverzeichnis (Art. 30), TOMs (Art. 32), ggf. DSB nach § 38 BDSG (regelmäßig ab 20 Personen mit personenbezogener Datenverarbeitung), Betroffenenrechte-Prozess binnen 1 Monat, Meldepflicht 72 h (Art. 33).
- **Nächster Schritt:** AVV mit Supabase dokumentiert archivieren; Verarbeitungsverzeichnis um länderspezifische Verarbeitungszwecke (Verifikation, Ranking, Scouts) ergänzen.

---

## 3. Vermittlungsrecht (Abgrenzung Vermittlung vs. Werkvertrag/Marktplatz)

> Vorbehalt: Ob eine reine Online-Matching-Plattform ohne Vertragspartei-Position und ohne Gebühren gegenüber Jobsuchenden als „private employment agency / recruiter" gilt, ist je Land auslegungsbedürftig. Alle vier Rechtsordnungen kennen Erlaubnisregime; Auslöser sind typischerweise „Vermittlung gegen Entgelt" bzw. „employment services for gain".

### Nigeria
- **Regime:** Labour Act Cap L1 LFN 2004, §§ 23–26, 71: Rekrutierung nigerianischer Bürger nur mit Employer's Permit bzw. Recruiter's Licence des Federal Ministry of Labour and Employment (Antrag über NELEX-Portal). Zwei Kategorien: Employment Agency (Matching, ohne Vertragspartei zu werden) und Labour Contractor; jeweils Domestic/International. Lizenz 2 Jahre (Neu), 1 Jahr (Verlängerung). [Quellen: nelex.gov.ng „Recruiter's License"; Gesetzestext labour.gov.ng; Mondaq, 27.02.2020]
- **Bewertung:** Der Wortlaut der Kategorie „Employment Agency" (Matching von Angeboten und Bewerbungen **ohne** Vertragspartei zu werden) beschreibt ziemlich genau das Voltage-Modell. Registrierungsbedarf daher wahrscheinlich, sobald die Plattform aktiv Nigerianer in Arbeit vermittelt — insb. bei entgeltlicher Ausgestaltung (Scout-Provisionen).
- **Unsicherheit/nächster Schritt:** Keine gefundene Rechtsprechung zu reinen Online-Marktplätzen ohne Inlandsniederlassung; nigerianische Arbeitsrechtskanzlei fragen, ob/ausländische Plattform ohne CAC-Entity lizenzieren kann/muss (Voraussetzung: CAC-Registrierung mit „labour recruitment" im MemArt).

### Kenia
- **Regime:** Labour Institutions Act 2007 §§ 54A–60 + National Employment Authority Act 2016: Private Employment Agencies benötigen NEA-Registrierung (NEAIMS-Portal). Anforderungen u. a. kenianische Gesellschaft, Mindeststammkapital KES 5 Mio., Büro ≥ 225 sq ft, Steuer-Compliance, Jahresgebühren KES 250.000 (lokal) / KES 500.000 (international), bei Auslandsvermittlung KES 1,5 Mio. Security Bond. **Gebührenverbot gegenüber Jobsuchenden.** [Quellen: hudumaglobal.com, 20.02.2026; inc.co.ke, 18.09.2026; Hansard 20.11.2024; diaspora.go.ke Verify-Portal]
- **Bewertung:** Ohne kenianische Entity ist NEA-Registrierung faktisch nicht darstellbar → Geschäftsmodell-Frage (lokale Tochter/Partner vs. reine Informationsplattform). Grenze „Recruitment vs. Werkvertrag": Sobald Voltage auftragsbezogene Dienstleistungserbringung (Werkvertrag mit Endkunden, Einsatz von Technikern) anbietet, rückt das Modell Richtung Labour Contractor — in allen vier Märkten lizenzschärfer.
- **Nächster Schritt:** Modellentscheidung (Marktplatz ohne Placement-Gebühren vs. registrierte PEA via kenianischer Entity) als Eskalationspunkt.

### Südafrika
- **Regime:** Employment Services Act 4 of 2014 (ESA), Kapitel 3: Registrierung privater Arbeitsvermittlungen beim Registrar (Dept. of Employment and Labour); Definition „any person who provides employment services **for gain**" — erfasst Labour Broker und Recruitment Agencies. **§ 15: Verbot von Gebühren gegenüber Jobsuchenden**; Verbot, Original-IDs/Qualifikationsurkunden einzubehalten (§ 14(d)) — relevant für Verifikations-Workflow (nur Kopien/Nachweise verarbeiten). Übergang: PEA-Registrierungen laufen praktisch (Zertifikate z. B. gültig 2024–2026). [Quellen: SAFLII ESA-Text, geprüft 28.03.2025; Gazette-Registrierungsformular 2018; Quest-Beispielzertifikat 2024]
- **Bewertung:** „for gain" ist der Hebel: kostenlose reine Matching-Plattform ohne Vergütung für Vermittlungsleistung ist argumentativ außerhalb; Scout-Provisionen/Vermittlungsgebühren ziehen die Registrierungspflicht wahrscheinlich nach sich. Achtung: s 13 ESA war zeitweise „not in force" markiert; praktischer Vollzug erfolgt über Übergangsregelungen/Skills Development Act — aktuellen Stand anwaltlich bestätigen lassen.
- **Nächster Schritt:** Status § 13 ESA + Registrierungspraxis des Registrars 2026 verifizieren; Gebührenverbot in Terms spiegeln.

### Ghana
- **Regime:** Labour Act 2003 (Act 651) § 7: Betrieb einer Private Employment Agency nur als Körperschaft mit Ministeriallizenz (12 Monate, erneuerbar). Pflichten: vierteljährliche Returns; **50-%-Rückerstattung an Jobsuchende, wenn nach 3 Monaten keine Platzierung** (§ 7(7)); Lizenzentzug bei Meldeverstößen. Labour Regulations 2007 (L.I. 1833): Lizenzgebühr + USD 20.000 Sicherheitsleistung (für Auslandsvermittlung). [Quellen: GhaLII Act 651; FAOLEX-Gesetzestext; dennislawgh.com, 18.01.2026]
- **Bewertung:** § 7 zielt auf gebührenpflichtige Vermittlung gegenüber Jobsuchenden/Arbeitgebern. Ein provisionsbasiertes Scout-Modell mit Rückfluss an Vermittelnde muss die Rückerstattungs- und Gebührenskalen-Logik (§ 175(h)) beachten. Reine unentgeltliche Plattform: Grauzone, Behördenauskunft empfohlen.
- **Nächster Schritt:** Auskunft Chief Labour Officer / Ministerium; ggf. ghanaische Körperschaft als Lizenzträger.

**Länderübergreifende Trennung (Senior-Standard):** „Vermittlung" (Matching, Kontaktaufnahme) ≠ „Werkvertrag" (Voltage schuldet Werkleistung, Techniker als Erfüllungsgehilfen) ≠ „Arbeitnehmerüberlassung" (Labour Contractor). Je weiter das Modell Richtung Werkvertrag/Überlassung wandert, desto mehr Lizenz-, Haftungs- und Sozialversicherungspflichten in allen vier Märkten. Diese Grenzziehung gehört verbindlich in die Nutzungsbedingungen — und muss zur tatsächlichen Betriebspraxis passen.

---

## 4. Gewerke-Zertifizierungen (Prüfstandard für „verified")

| Markt | Elektro | Solar | Register/Verifikation | Quelle (Stand) |
|---|---|---|---|---|
| **Nigeria** | NEMSA-Kompetenzzertifizierung für Elektroinstallations-Contractor/Techniker (Electricity Act 2023, vorm. NEMSA Act 2015); jede Installation muss von NEMSA inspiziert/zertifiziert werden, bevor sie energiert wird | NEMSA-Zertifizierungsprogramm „renewable energy installers"; seit 04/2026 verbindliche Dach-Solar-Sicherheitsleitlinien: Installation nur durch NEMSA-zertifizierte Contractor, Abnahme vor Inbetriebnahme | Zertifikatsprüfung über nemsa.gov.ng (Verifikationssektion, öffentliches Contractor-Verzeichnis) | Vanguard, 28.04.2026; Punch, 08.05.2025; bizwatchnigeria.ng, 20.04.2026; infraforceafrica.com, 20.07.2026 |
| **Kenia** | EPRA-Lizenz als Electrical Contractor (Klassen A/B/C) nach Energy Act 2019; Voraussetzung: certified electrical worker | EPRA Solar-PV-Techniker T1/T2/T3 (Bearbeitung ≤ 60 Tage); Firmen: C1 (Contractor), V1 (Vendor), V2 (Hersteller/Import); Betrieb ohne Lizenz strafbewehrt (bis KES 1 Mio.) | EPRA-Online-Lizenzportal; öffentliche Lizenzregister | EPRA-Notice 22.06.2026 (kenyans.co.ke, nairobileo.co.ke); UJ/EconStor-Studie; surgepv.com, 25.04.2026 |
| **Ghana** | Energy Commission: CEWP (Domestic/Commercial/Industrial) nach Electrical Wiring Regulations 2011 (L.I. 2008); Installationen nur durch CEWP, Prüfung durch CEWI; „Form A" (Installation Completion Certificate) Pflicht für Netzanschluss (ECG/NEDCo) | Kein separates Solar-Installateur-Regime gefunden — **offener Punkt**; Elektroanteil von PV-Anlagen fällt unter CEWP-Logik (GS 1009) | CEWP-Register auf energycom.gov.gh (Zertifikat + ID prüfbar) | open-exam-prep.com (CEWP-Examensinfos), 01/2026; ghanawiring.com; ECG, 23.07.2025; escatechafrica.com, 15.07.2026 |
| **Südafrika** | „Registered Person" beim Dept. of Employment and Labour nach Electrical Installation Regulations 2009 (OHS Act): Single-Phase Tester / Installation Electrician / Master Installation Electrician (Wireman's Licence); CoC-Ausstellung (SANS 10142-1) nur durch registrierte Personen | PV-Anlagen: Installation durch ET unter Kontrolle IE/MIE; CoC muss Solar explizit umfassen; SSEG-Registrierung bei Kommune/Eskom für netzgekoppelte Anlagen bis 50 kW; Regelverschärfung DoL/ECSA 10/2025 (ECSA-Registrierung, Detail unsicher) | DoEL-Registrierungsnummer + ECB-Register (Electrical Contracting Board) | electriciancalloutrate.co.za, 18.07.2026; dvh.law.za, 11.11.2025; Renkalec/JFa2-Trainingsmaterial; surgepv.com (ECSA-Hinweis, 25.04.2026) |

**Konsequenz für die Plattform („verified"-Logik):**
1. Vier Verifikationsstufen sauber trennen (Senior-Standard): Selbstauskunft ≠ Identität ≠ Dokumentenprüfung ≠ **behördliche Lizenz** ≠ Arbeitsqualität.
2. „Verified" für Elektro/Solar sollte als Minimalstandard den **Registerabgleich** gegen das jeweilige öffentliche Register (NEMSA, EPRA, Energy Commission CEWP, DoEL/ECB) bedeuten — Lizenznummer + Inhaber + Gültigkeit dokumentieren.
3. Südafrika: **keine** Original-Qualifikationsurkunden einbehalten/verlangen (ESA § 14(d)); nur Sicht-/Kopienachweise.
4. Offene Punkte: Ghana-Solar-Spezifikregime; SA-ECSA-Detailregelung 10/2025; Nigeria: Verhältnis NEMSA-COREN (COREN = Ingenieursregister, keine Handwerkerlizenz).

---

## 5. Werberecht (knapp, typische Stolpersteine)

- **Nigeria (kritischster Markt):** ARCON Act 2022 + Nigerian Code of Advertising Practice: **Vorab-Vetting sämtlicher Werbung** (inkl. Social Media, Google/Meta Ads, Influencer) durch Advertising Standards Panel; Betrieb ohne ASP-Certificate of Approval: Mindeststrafe ₦500.000 je Verstoß, Werbeverbot, Advertising Offences Tribunal. Ausländische Unternehmen müssen über **ARCON-registrierte nigerianische Agenturen** einreichen; Local-Content-Regeln (nigerianische Models/Talente, Waiver gegen Gebühr); **Preisangaben in Naira**; Substantiation-Pflicht für Claims (Art. 26). [Quellen: advertcouncil.gov.ng; Premium Times, 05.05.2025; kabbizlegal.com, 30.06.2025; lawcarenigeria.com, 18.09.2026]
- **Südafrika:** Consumer Protection Act 68/2008 §§ 29/41 (Irreführungsverbot inkl. Weglassen/Korrekturpflicht), § 30 Bait Marketing; ARB (Selbstregulierung, Code of Advertising Practice + Social Media Code: #ad-Kennzeichnung, Substantiation) — wirkt auch gegen Nicht-Mitglieder (Bliss Brands, SCA 2022). POPIA § 69 Opt-in für elektronisches Direktmarketing. [Quellen: Springer-Aufsatz, 26.03.2025; Webber Wentzel, 10.09.2026; INTA-Report]
- **Kenia:** Consumer Protection Act 2012 § 12 (false representation, Straftat); Competition Act (Irreführung, vergleichende Werbung nur wahrheitsgemäß); Kenya Information and Communications Act (CA-Standards, Kinderschutz); Selbstregulierung via Advertising Standards Body of Kenya. [Quelle: ADR Journal Vol. 22, 05/2024]
- **Ghana:** Kein zentrales Werbe-Vetting für Dienstleistungswerbung; Irreführungsverbote u. a. Electronic Transactions Act 2008 (Act 772) § 110 („charlatanic advertisement"), AAG-Selbstregulierungskodex; FDA-Vorabgenehmigung nur für regulierte Produkte (für Voltage nicht einschlägig). Kein umfassendes Verbraucherschutzgesetz verabschiedet (Stand Recherche). [Quellen: Integrated Legal Consultants Länderkapitel; USDA FAS GH2025-0010]
- **Querschnitt für Voltage:** „verified"-, Einkommens- und Ranking-Claims sind überall substantiationspflichtig — nur belegen, was tatsächlich geprüft wurde (vgl. WEBSITE-CONTEXT: Website-Text belegt keine betriebliche Umsetzung). XP/Punkte „ohne Geldwert" konsequent so bewerben; keine Einkommensversprechen ohne Quelle, Währung, Zeitraum, Bedingungen.

---

## 6. Risiko-Matrix (Top 10)

Skala: EW = Eintrittswahrscheinlichkeit (niedrig/mittel/hoch), Schaden (gering/mittel/hoch/sehr hoch). Einschätzungen sind Expertenheuristik der Vorprüfung, keine statistische Messung.

| # | Risiko | Land/Ebene | EW | Schaden | Konkrete Gegenmaßnahme | Verantwortlichkeit |
|---|---|---|---|---|---|---|
| 1 | Betrieb ohne Datenschutz-Registrierung (ODPC / DPC Ghana / NDPC-DCPMI) | KE, GH, NG | hoch | hoch (Strafbarkeit KE/GH; Bußgelder NG) | Registrierungs-Roadmap je Land; Schwellenmonitoring (Betroffenenanzahl/6 Monate); Nachweise archivieren | Geschäftsführung + externer DPO |
| 2 | Einordnung als nicht lizenzierte private Arbeitsvermittlung | NG, KE, ZA, GH | mittel | sehr hoch (Betriebsverbot, Strafe) | Anwaltliche Einordnung je Land vor Skalierung; Terms auf „Marktplatz ohne Placement-Gebühren" ausrichten; Modellentscheidung KE-Entity | Geschäftsführung |
| 3 | Scout-Provisionen kollidieren mit Gebührenverboten/Rückerstattungspflichten (ZA § 15 ESA; GH § 7(7); KE Gebührenverbot) | ZA, GH, KE | hoch (bei Einführung) | hoch | Provisionen ausschließlich arbeitgeberseitig konzipieren; anwaltliches Konzept vor Implementierung; bis dahin nicht live schalten | Produkt + Geschäftsführung |
| 4 | Fehlende AVV-/Transfer-Dokumentation (Art. 28 DSGVO mit Supabase; KE § 48, ZA § 72, NG-GAID Cross-Border) | EU + alle | mittel | hoch | AVV prüfen/archivieren; Transfer-Dossier je Land (Safeguards, Einwilligungstexte); TOMs dokumentieren | Externer DPO |
| 5 | „Verified"-Claim ohne behördlichen Registerabgleich (irreführende Werbung + Haftung bei Schaden durch nicht lizenzierte „Elektriker") | alle | mittel | sehr hoch (Personenschaden + Vertrauensverlust) | Verifikationsstufen trennen; Registerabgleich (NEMSA/EPRA/CEWP/DoEL) als Pflicht für Elektro/Solar-„verified"; Claim-Texte anwaltlich freigeben | Plattform-Betrieb + Compliance |
| 6 | ARCON-Verstoß durch unvet­tete Werbung/Local-Content-Regeln (Nigeria) | NG | mittel | hoch (₦500.000+/Verstoß, Kampagnenstopp) | Nigeria-Kampagnen nur über ARCON-registrierte Agentur; Vetting-Zeit (2–3 Wochen) einplanen; Naira-Preisangaben | Marketing-Lead |
| 7 | POPIA-Anwendbarkeit ungeklärt; fehlender IO/PAIA-Manual; Direktmarketing ohne Opt-in (§ 69) | ZA | mittel | mittel–hoch (R10 Mio. Rahmen) | Anwendbarkeit klären; ggf. IO registrieren, PAIA-Manual, Form-4-Opt-in-Prozess | Externer DPO |
| 8 | Betroffenenrechte-Prozesse nicht landestauglich (Fristen 30–40 Tage, Sprachen, SNAG in NG) | alle | mittel | mittel | Einheitlicher DSAR-Workflow mit Länder-Fristen-Mapping; Melde- und Löschprozesse testen | Support + DPO |
| 9 | Breach-Response nicht 72-h-fähig (NDPC/ODPC/DSGVO; POPIA-E-Portal) | alle | niedrig–mittel | hoch | Incident-Response-Plan, Benachrichtigungs-Templates je Behörde, Übung | IT/Security + DPO |
| 10 | Werbliche Einkommens-/Provisionsclaims ohne Beleg (Substantiation-Pflichten; XP „ohne Geldwert") | alle | mittel | mittel | Claim-Register mit Quelle/Währung/Zeitraum/Bedingungen; Freigabeprozess; XP-Kommunikation konsistent | Marketing-Lead |

---

## 7. Eskalationsliste — vor Skalierung zwingend anwaltlich zu prüfen

1. **Vermittlungslizenz-Bedarf je Land (NG + KE vorrangig):** Verbindliche Einordnung des Plattformmodells (Marktplatz/Matching vs. Employment Agency vs. Labour Contractor) durch lokale Arbeitsrechtskanzlei — inkl. Frage, ob eine ausländische Plattform ohne lokale Entity registrierungspflichtig/-fähig ist, und Modellentscheidung Kenia (lokale Tochter vs. Einschränkung des Leistungsumfangs). **Behörden:** Federal Ministry of Labour and Employment (NG), National Employment Authority (KE), Registrar PEA/DoEL (ZA), Chief Labour Officer (GH).
2. **Scout-/Provisionsmodell:** Rechtsgutachten zur Vereinbarkeit erfolgsabhängiger Vergütungen mit Gebührenverboten (ZA § 15 ESA, KE-Praxis), Rückerstattungspflicht (GH § 7(7)) und nigerianischem Recruiter-Regime — vor jeder Implementierung; bis dahin dokumentiert „nicht implementiert" belassen.
3. **Datenschutz-Registrierungen + Cross-Border-Konstrukt:** Fachanwalt/Datenschutzpraktiker je Land: DCPMI-Einstufung + Registrierung (NG), ODPC-Registrierung + DPO-Frage + §-48-Safeguards (KE), DPC-Registrierung als external company (GH), POPIA-Anwendbarkeit/IO/PAIA (ZA), sowie AVV-/Drittlandbezug der Supabase-Konfiguration (EU/DE). **Behörden:** NDPC, ODPC, DPC Accra, Information Regulator (SA), deutsche Aufsicht (LfD des Sitzlandes).

---

## 8. Quellen (Auswahl, mit Abruf-/Standdatum)

**Datenschutz**
- DLA Piper, Data Protection Laws of the World — Nigeria (17.03.2026), Kenia (23.03.2026), Ghana (18.03.2026); dlapiperdataprotection.com
- NDPC, General Application and Implementation Directive (GAID) 2025, erlassen 20.03.2025; ndpc.gov.ng
- Recording Law, Nigeria & Ghana Privacy Guides (20.05.2026); recordinglaw.com
- ODPC, Statement on Registration Commencement (14.07.2022); odpc.go.ke
- Bowmans, Africa Guide to Data Protection (2024/2025); bowmanslaw.com
- SHQ Legal, Data Security Obligations NDPA/GAID (12.05.2026); shqlegal.com
- aosphere Rulefinder Data Privacy — Ghana; aosphere.com (o. D., abgerufen 21.09.2026)
- ClearComply, POPIA Information Officer Registration (26.05.2026); clearcomply.co.za
- SiteGrade, POPIA Website Requirements (20.04.2026); sitegrade.io

**Vermittlungsrecht**
- Labour Act (Nigeria) Cap L1 LFN 2004, §§ 23–26; labour.gov.ng / nelex.gov.ng („Recruiter's License"-FAQ)
- Employment Services Act 4/2014 (SA), Gesetzestext; saflii.org (geprüft 28.03.2025); PEA-Registrierungsformular Gazette 42140 (28.12.2018); Quest-PEA-Zertifikat (18.09.2024, Beleg praktischen Vollzugs)
- Labour Institutions Act 2007 §§ 54A ff. + NEA Act 2016 (Kenia); Hansard 20.11.2024; neaims.go.ke; hudumaglobal.com (20.02.2026); inc.co.ke (18.09.2026)
- Labour Act 2003 (Act 651) § 7 + Labour Regulations 2007 L.I. 1833 (Ghana); ghalii.org; faolex.fao.org; dennislawgh.com (18.01.2026)

**Gewerke**
- NEMSA/Electricity Act 2023 (Nigeria): Vanguard (28.04.2026); Punch (08.05.2025); bizwatchnigeria.ng (20.04.2026); infraforceafrica.com (20.07.2026)
- EPRA/Energy Act 2019 (Kenia): EPRA-Lizenznotice 22.06.2026 (kenyans.co.ke; nairobileo.co.ke); surgepv.com (25.04.2026); UJ/EconStor-Studie
- Energy Commission Ghana / L.I. 2008: open-exam-prep.com (01/2026); ghanawiring.com; ecg.com.gh (23.07.2025)
- DoEL/CoC (Südafrika): electriciancalloutrate.co.za (18.07.2026); dvh.law.za (11.11.2025); renkalec.com

**Werberecht**
- ARCON: advertcouncil.gov.ng (Vetting-Verfahren); Premium Times (05.05.2025); kabbizlegal.com (30.06.2025); lawcarenigeria.com (18.09.2026)
- SA: Springer J Consum Policy (26.03.2025); Webber Wentzel (10.09.2026); INTA Influencer-Marketing-Report
- KE: ADR Journal Vol. 22 (05/2024) — CPA § 12, Competition Act, KICA
- GH: Integrated Legal Consultants, Ghana Advertising Chapter; USDA FAS GAIN GH2025-0010 (19.03.2025)

**Hinweis zur Quellenlage:** Mehrere Detailangaben (Gebühren, Schwellenwerte) stammen aus Sekundärquellen mittlerer Autorität; verbindliche Werte sind vor jeder Handlung gegen die Primärquellen (Gesetzestexte, Behördenportale) zu verifizieren. Gesetzestexte selbst (Labour Act NG, ESA SA, Act 651 GH, ESA-Text) wurden direkt eingesehen.

---

## 9. Drei nächste Maßnahmen

1. **Registrierungs-Roadmap Datenschutz erstellen und starten (Frist: 30 Tage):** ODPC- (KE) und DPC-Registrierung (GH, „external company") vorbereiten; DCPMI-Schwellen-Monitoring (NG) einrichten; AVV mit Supabase und POPIA-Anwendbarkeit dokumentiert klären. Verantwortlich: Geschäftsführung + externer DPO.
2. **Lokale Rechtsgutachten einholen (Frist: 60 Tage):** Vermittlungseinordnung je Land (Eskalationspunkt 1) und Scout-Provisionsmodell (Eskalationspunkt 2) durch Fachanwälte in NG/KE vorrangig, ZA/GH danach. Bis zur Klärung: keine erfolgsabhängige Monetarisierung, Terms-Disclaimer auf Marktplatz-Charakter ausrichten.
3. **„Verified"-Standard nachrüsten (Frist: 90 Tage):** Verifikationsstufen dokumentieren, behördlichen Registerabgleich (NEMSA/EPRA/CEWP/DoEL-ECB) als Pflichtkriterium für Elektro-/Solar-Profile definieren, Claim-Register für alle Marketingaussagen anlegen (Substantiation), ARCON-Workflow für Nigeria-Kampagnen etablieren. Verantwortlich: Plattform-Betrieb + Marketing-Lead.

---

*Dieser Bericht ist eine strukturierte Compliance-Vorprüfung des Marketingteams und ersetzt keine Rechtsberatung. Alle markierten Unsicherheiten sind Gegenstand der Eskalationsliste.*
