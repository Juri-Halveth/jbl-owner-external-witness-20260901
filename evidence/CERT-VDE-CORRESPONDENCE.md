# CERT@VDE #642251 – Bestätigung und Meldungsverlauf

**Finder: Juri Janovski — HALVETH · GitHub: Juri-Halveth**

Diese Auszüge stammen aus dem vom Finder am 27. November 2026 bereitgestellten Text der Korrespondenz zu **„Harman: JBL QuantumENGINE Vulnerability Report [CERT@VDE#642251]“**. Sie ergänzen die separat veröffentlichten technischen Laufbelege. Private Empfängeradressen, Signaturen und wiederholte Kontaktdaten wurden ausgelassen; die nachstehenden Nachrichteninhalte sind wörtlich wiedergegeben, Zeilenumbrüche teilweise zusammengeführt.

## 2. September 2026: Eingang und Koordination

Absender laut vorgelegtem Verlauf: CERT@VDE. Angegebene Zeit: **02.09.2026, 12:43:23**; die Zeitzone ist in diesem Zitat nicht ausgewiesen.

> Hello Juri,
>
> Thank you for your report. I am writing to confirm that we have received it.
>
> We are coordinating the vulnerabilities and will contact Harman.
>
> I will get back to you as soon as the vulnerabilities have been confirmed.

Dies dokumentiert den Eingang und die Übernahme der Koordination. Die spätere Validierungsbestätigung steht in der Nachricht vom 24. September.

## 24. September 2026: Bestätigung durch das Engineering-Team

Absender laut vorgelegtem Verlauf: CERT@VDE. Angegebene Zeit: **24.09.2026, 11:35:50**; die Zeitzone ist im Textheader nicht ausgewiesen.

> Hello Juri,
>
> here is the Update:
>
> Affected versions: JBL QuantumENGINE version 2.7.8 has been confirmed as affected. Additional version impact analysis is ongoing.
>
> Severity assessment: The engineering team has reviewed the report, validated the issue, and agrees with the proposed severity assessment.
>
> Remediation plan: A corrective software update is under development and is currently planned for release in December 2026.
>
> An advisory is in the works. Would you like to be credited as the finder, and if so, under what name?

**Dokumentiert sind:** bestätigte Betroffenheit von **2.7.8**, Validierung des gemeldeten Problems durch das Engineering-Team, Zustimmung zur vorgeschlagenen Schweregradeinschätzung und ein damals für **Dezember 2026 geplantes** Korrekturupdate. Die konkrete CVSS-Zahl steht nicht in diesem Auszug. Die Planung ist kein Nachweis einer bereits ausgelieferten Behebung.

## 24. September 2026: Gewünschte Finder-Nennung

Juris Antwort ist im Verlauf mit **24.09.2026, 12:51:22** zitiert:

> Yes, I would like to be credited as the finder under:
>
> Juri Janovski — HALVETH
>
> Please also reference my public research / technical work where appropriate:
>
> GitHub: Juri-Halveth

## 19. Oktober 2026: Entscheidung über die Prämie

Absender laut vorgelegtem Verlauf: CERT@VDE. Angegebene Zeit: **19.10.2026, 11:16:30**.

> Hello Juri,
>
> Harman has concluded that this submission does not qualify for a reward under their bug bounty program.
>
> For further information regarding the program, including eligibility criteria and reward guidelines, please check the following pages:

Die Nachricht verweist anschließend auf die HARMAN-Programme für [Web Applications](https://yeswehack.com/business-units/harman-international/programs/harman-international-web-applications/details) und [Products](https://yeswehack.com/business-units/harman-international/programs/harman-international-public-bug-bounty/details).

**Die Nachricht lehnt eine Prämie unter dem Bug-Bounty-Programm ab. Sie widerruft die technische Bestätigung vom 24. September nicht.** Eine konkrete Ausschlussregel oder detaillierte Begründung für die Prämienentscheidung wird in der vorgelegten Nachricht nicht genannt.

## 19. Oktober 2026: Finder-Nennung zugesagt

Die weitergeleitete Nachricht trägt den Header **19.10.2026, 15:04** und nennt CERT@VDE als Absender. Sie wurde am 22. Oktober weitergeleitet.

> Hallo Juri,
>
> du wirst ja im Advisory und der Schwachstelle als Finder genannt. Das ist ja ein dokumentierter Nachweis.

Damit ist die vorgesehene Anerkennung als Finder schriftlich dokumentiert. Der Auszug ist noch kein bereits veröffentlichtes Advisory.

## Spätere Antwort: Advisory noch unveröffentlicht

Die oberste Antwort im bereitgestellten Verlauf folgt auf Juris zitierte Anfrage vom **22.10.2026, 13:15:19**. **Ein eigener Sendezeitpunkt dieser Antwort ist im Text nicht enthalten.**

> Hallo Juri,
>
> das Advisory ist noch nicht veröffentlicht und aktuell gibt es noch kein konkretes Datum.
>
> Sobald das Advisory veröffentlicht ist, bekommst du den Link zu dem Advisory und der CVE.

Der damalige Stand lautet damit: Veröffentlichung noch ausstehend, kein konkretes Datum genannt, Advisory- und CVE-Link für die Veröffentlichung angekündigt. Eine konkrete CVE-Kennung steht im vorgelegten Verlauf nicht.

## Technischer Gegenstand der koordinierten Meldung

Juris im Verlauf enthaltene Anfrage an CERT@VDE ist mit **02.09.2026, 11:43:15** zitiert. Sie beschreibt den lokalen Befund:

> The strongest reproduced result on JBL QuantumENGINE 2.7.8 is that a separately compiled, non-elevated local process with an arbitrary self-declared client name can open JBL's remote-control IPC service, read pairing and device metadata, reuse the owner pairing state, change one owner-headset setting, independently verify the changed value, restore the baseline and independently verify the restoration. A different existing nonadministrative Windows SID also read bounded pairing-state metadata and registered the FOTA namespace in no-command mode. Testing involved only reporter-owned systems and stopped before firmware, file, persistence, denial-of-service or code-execution effects.

Die gleiche Meldung grenzt die damalige Untersuchung von Version 2.8.6 ab:

> A later static comparison against the installed signed 2.8.6 release found the visible caller-authorization, FOTA and remote-control paths semantically unchanged. Separate native IPC robustness changes were observed. This is not a claim that 2.8.6 is dynamically vulnerable or that HARMAN's release was caused by the report; a clean 2.8.6 runtime retest remains open.

Die technische Beschreibung stammt aus der Meldung des Finders. Die darüber aufgeführte CERT@VDE-Antwort dokumentiert die spätere Validierung des gemeldeten Problems durch das Engineering-Team. Die zusätzlichen Tunnel- und TCP-Receipts im Repository sind getrennte Versuche und ersetzen diese lokale IPC-Untersuchung nicht.

## Quellenbindung

Der bereitgestellte Text umfasst **10.174 Byte**. Sein SHA-256 lautet:

`dfff8fadfd398b0833def99c0e20d199e2a38b48d1f7d3d9eb207105d6d0d1b0`

Dieser Hash identifiziert die eingereichte Textdatei. Die veröffentlichte Auswahl ist eine redigierte Textfassung, kein vollständiger EML-Export und keine kryptografische Prüfung des Mailtransports. Sie bewahrt die für Bestätigung, Version, Planung, Prämienentscheidung und Finder-Nennung maßgeblichen Aussagen.
