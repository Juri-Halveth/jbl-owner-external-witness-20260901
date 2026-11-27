# JBL QuantumENGINE: bestätigte Schwachstelle und ergänzende Prüfbelege

**Finder: Juri Janovski — HALVETH · GitHub: Juri-Halveth**  
**Koordination: CERT@VDE #642251 · Stand: 27. November 2026**

**CERT@VDE teilte am 24. September 2026 mit, dass das Engineering-Team den gemeldeten Fehler validiert hat und JBL QuantumENGINE 2.7.8 als betroffen bestätigt ist.** Das Team stimmte außerdem der vorgeschlagenen Schweregradeinschätzung zu. Ein Korrekturupdate war zu diesem Zeitpunkt in Entwicklung und für Dezember 2026 geplant. Am 19. Oktober wurde Juri die Finder-Nennung im Advisory zugesagt. [Korrespondenz mit maßgeblichen Auszügen](evidence/CERT-VDE-CORRESPONDENCE.md)

Die erste Fassung dieses Berichts stützte die Gesamtdarstellung zu eng auf zwei ergänzende GitHub-Netzwerkversuche. Dadurch fehlten die bereits erfolgte Bestätigung und der lokale Schwachstellenkern. **Diese Darstellung ist korrigiert.** Die Änderung ist im [Erratum](ERRATUM-20261127.md) dokumentiert.

## Der bestätigte Fall: lokaler Zugriff auf Pairing-Zustand über IPC

Die an CERT@VDE übermittelte Meldung beschreibt für QuantumENGINE 2.7.8 einen **separat kompilierten lokalen Prozess ohne erhöhte Rechte**, der mit einem frei angegebenen Clientnamen JBLs Remote-Control-IPC öffnen konnte. Er konnte Pairing- und Gerätemetadaten lesen, den vorhandenen Pairing-Zustand des Eigentümers wiederverwenden, eine Einstellung des eigenen Headsets ändern, den geänderten Wert zurücklesen und anschließend den Ausgangswert wiederherstellen und erneut zurücklesen.

Die relevante Zugriffsgrenze betrifft damit **die Autorisierung lokaler IPC-Clients und den Zugang zum vorhandenen Pairing-Zustand**. Der gemeldete Client bekam diesen Zustand über die untersuchte lokale Schnittstelle. Das ist der entscheidende Unterschied zum zusätzlichen Tunnelversuch, bei dem das Pairing-Material bereits als Eingabe bereitgestellt wurde.

Die Meldung beschreibt außerdem, dass eine andere vorhandene nichtadministrative Windows-SID begrenzte Pairing-Metadaten lesen und den FOTA-Namensraum ohne Kommandoausführung registrieren konnte. Für diese zweite SID wird in der vorgelegten Meldung keine vollständige Einstellungsänderung behauptet. Firmware-, Datei-, Persistenz-, DoS- und Codeausführungseffekte wurden ausdrücklich nicht getestet.

Diese technische Beschreibung stammt aus Juris Meldung vom 2. September. Die Antwort vom 24. September dokumentiert die nachfolgende Engineering-Validierung des gemeldeten Problems. Die lokalen Originalprogramme und vollständigen IPC-Rohmitschnitte sind von den hier erhaltenen Tunnel-/TCP-Skripten zu unterscheiden. [Technischer Gegenstand und Bestätigung](evidence/CERT-VDE-CORRESPONDENCE.md)

## Was die Korrespondenz bestätigt

| Punkt | Dokumentierter Stand |
| --- | --- |
| Vorgang | **CERT@VDE #642251** |
| Eingang und Koordination | CERT@VDE bestätigt am **02.09.2026** den Eingang und die Übernahme der Koordination mit HARMAN. |
| Technische Bewertung | Am **24.09.2026** wird die Validierung des gemeldeten Fehlers durch das Engineering-Team mitgeteilt. |
| Betroffene Version | **JBL QuantumENGINE 2.7.8 bestätigt betroffen.** Weitere Versionsprüfung war laut Nachricht noch im Gang. |
| Schweregrad | Das Engineering-Team stimmt der vorgeschlagenen Einschätzung zu. Der konkrete CVSS-Wert beziehungsweise die Kategorie ist im vorgelegten Mailtext nicht genannt. |
| Behebung | Am **24.09.2026**: Korrekturupdate in Entwicklung, Veröffentlichung für **Dezember 2026 geplant**. Dies ist ein datierter Plan. |
| Prämie | Am **19.10.2026** teilt CERT@VDE HARMANs Entscheidung mit, dass die Einreichung nicht für eine Belohnung unter dessen Bug-Bounty-Programm qualifiziert. |
| Finder-Nennung | Am **19.10.2026** sagt CERT@VDE die Nennung im Advisory und bei der Schwachstelle zu. Gewünschter Name: **Juri Janovski — HALVETH**. |
| Advisory / CVE | Eine spätere, im vorgelegten Text **undatierte** Antwort nach Juris Anfrage vom 22. Oktober sagt: Advisory noch nicht veröffentlicht, kein konkretes Datum; Advisory- und CVE-Link werden nach Veröffentlichung mitgeteilt. Eine konkrete CVE-Nummer steht nicht im Verlauf. |

**Die Ablehnung einer Prämie ist keine Rücknahme der technischen Bestätigung.** In der vorgelegten Prämiennachricht wird keine konkrete Ausschlussregel oder fallbezogene Begründung genannt. [Wortlaut der Nachrichten](evidence/CERT-VDE-CORRESPONDENCE.md)

## Versions- und Fixstatus

| Version / Gegenstand | Belegstand |
| --- | --- |
| **QuantumENGINE 2.7.8** | Durch die CERT@VDE-Nachricht vom 24. September als betroffen bestätigt. |
| **QuantumENGINE 2.8.6** | Juris Meldung beschreibt einen statischen Vergleich der installierten signierten Fassung: sichtbare Autorisierungs-, FOTA- und Remote-Control-Pfade semantisch unverändert; separate IPC-Robustheitsänderungen beobachtet. Die Meldung schließt ausdrücklich eine Behauptung dynamisch nachgewiesener Betroffenheit von 2.8.6 aus. |
| **QuantumENGINE 2.9.4** | In den am 27. November gelesenen offiziellen Release-Notes mit Datum **03.11.2026** aufgeführt. In dieser Dokumentationsprüfung kein Runtime-Retest durchgeführt. |
| **Korrekturupdate** | Am 24. September für **Dezember 2026 geplant**. Die Korrespondenz enthält keine bereits ausgelieferte Fixversion. |

Die [offiziellen Release-Notes](https://support.jbl.com/us/en/howto/jbl-quantum-engine-software-release-notes-us/000018780.html) nennen für 2.8.6 und 2.9.4 allgemeine Fehlerbehebungen. In den gelesenen Hinweisen und der [CERT@VDE-HARMAN-Liste](https://certvde.com/en/advisories/vendor/harman/) wurde keine eindeutig diesem Fall zugeordnete Fixbestätigung gefunden. Der bestätigte Befund in 2.7.8 bleibt davon unberührt. Ob eine neuere Fassung das Problem enthält oder bereits behebt, ist anhand dieser Quellen nicht entschieden.

Die ergänzenden September-Tunnel-/TCP-Receipts enthalten keine gebundene QuantumServer.exe-Buildnummer oder Hashes der Herstellerbinary. **Diese Lücke der einzelnen Laufbelege hebt die Versionsbestätigung für den koordinierten Fall nicht auf.**

## Ergänzende Versuche: Tunnel und direkte Verbindung

Am **1. September 2026** protokollierte ein GitHub-Prüfclient über einen vom Eigentümer eingerichteten temporären Tunnel und mit bereitgestelltem Pairing-Material den Protokollwert `microphone.gain` als **75 → 74 → 75**. Zusätzliche Leseabfragen desselben Clients bestätigten Änderung und Wiederherstellung.

Ein separater direkter TCP-Versuch zu Port **57120** endete nach **8009 ms im Timeout**, ohne aufgebaute Verbindung und ohne gesendete Anwendungspayload. Das begrenzt die Aussage dieses direkten Netzwerkversuchs; es widerlegt den bestätigten lokalen IPC-Befund nicht.

### Die vier erhaltenen September-Läufe


Alle Uhrzeiten in dieser Tabelle sind UTC. Die JSON-Dateien sind aus den vorhandenen Actions-Logs extrahierte Fassungen. Bei den Tunnel-Läufen ist ausschließlich der Fingerprint des Pairing-Materials als Redaktion gekennzeichnet.

| Lauf am 01.09.2026 | Beobachtung | Beleg |
| --- | --- | --- |
| 16:55:26–16:55:28, nur Lesen | Pairingantwort akzeptiert, ein Gerät, Gain 75 gelesen; keine Änderung versucht | [Leseversuch](evidence/33534671737.json) · [Originaljob](https://github.com/Juri-Halveth/jbl-owner-external-witness-20260901/actions/runs/33534671737/job/99945968622) |
| 16:56:00–16:56:02, Zwischenlauf | Verbindung aufgebaut, anschließend `ValueError`; kein Schreibversuch. Die genaue Fehlerursache steht nicht im Log. | [Fehlgeschlagener Zwischenlauf](evidence/33534747697.json) · [Originaljob](https://github.com/Juri-Halveth/jbl-owner-external-witness-20260901/actions/runs/33534747697/job/99946209604) |
| 16:57:19–16:57:22, begrenzte Änderung | Baseline 75, Kandidat 74 zurückgelesen, Rollback auf 75 zurückgelesen; `terminalBaselineRestored=true`, `errors=[]` | [Änderung und Wiederherstellung](evidence/33534876671.json) · [Originaljob](https://github.com/Juri-Halveth/jbl-owner-external-witness-20260901/actions/runs/33534876671/job/99946634748) |
| 17:20:35–17:20:43, direkte Verbindung | `TIMEOUT_WITHIN_BOUND_WINDOW`, `tcpConnected=false`, `payloadBytesSent=0`, ein Versuch | [Direkter TCP-Versuch](evidence/33537188510.json) · [Originaljob](https://github.com/Juri-Halveth/jbl-owner-external-witness-20260901/actions/runs/33537188510/job/99954266602) |

Beim reinen Leseversuch ist `terminalBaselineRestored=false` kein gescheiterter Rollback: Dort wurde überhaupt kein Schreibversuch durchgeführt. Der fehlgeschlagene Zwischenlauf belegt weder eine bestimmte falsche Eingabe noch eine bestimmte Schutzmaßnahme, weil nur der Exception-Typ protokolliert ist.

Die erneute Prüfung am 27. November bestand im Lesen der vorhandenen Quellen und Logs. Sie war **keine erneute Netzwerkausführung** dieser Versuche.

## Versuchsaufbau und vorhandener Code

Die drei Tunnel-Läufe verwendeten den Quellstand [`6fc23a74977e2cf964eea65fa0d2529d0226963b`](https://github.com/Juri-Halveth/jbl-owner-external-witness-20260901/tree/6fc23a74977e2cf964eea65fa0d2529d0226963b), der direkte Versuch [`c83ede734c1498da3fc468d540f405d3799db722`](https://github.com/Juri-Halveth/jbl-owner-external-witness-20260901/tree/c83ede734c1498da3fc468d540f405d3799db722).

Der zusätzliche [Tunnel-Witness-Client](external_witness.py) erhält `TUNNEL_URL`, `PAIR_FRAME_B64` und `WITNESS_MODE` aus seiner Umgebung. Er öffnet die WebSocket-Verbindung, sendet das bereitgestellte Pairing-Frame und erwartet eine Antwort mit genau einem Gerät. Anschließend vergleicht er den Gain aus dieser Antwort mit einer eigenen Leseabfrage. Im Modus `readonly` endet der Versuch dort. Im Modus `reversible-write` verändert er den Wert um einen Schritt, liest ihn erneut und versucht im `finally`-Block die Wiederherstellung einschließlich weiterer Leseabfrage.

Die erforderlichen Pairingdaten werden durch diesen zusätzlichen Tunnel-Client **nicht beschafft**. Der lokale IPC-Befund der koordinierten Meldung behandelt gerade den davorliegenden Zugriff auf den vorhandenen Pairing-Zustand. Er führt keine Suche nach fremden Geräten durch. Die Belegfelder mit dem Wort `IndependentReadback` meinen eine zusätzliche RPC-Abfrage im selben Client; sie bezeichnen keine unabhängige zweite Implementierung oder physische Audiomessung. Das Feld `subprotocol` ist im Receipt vorgegeben; ein gesonderter Mitschnitt des tatsächlich ausgehandelten Subprotokolls liegt hier nicht vor.

Der [direkte Witness](direct_wan_witness.py) versucht einmalig einen TCP-Verbindungsaufbau mit einem Zeitlimit. Er sendet keine Anwendungspayload. Ein Timeout benennt die beobachtete Zeitüberschreitung; daraus folgt keine Diagnose, ob Firewall, Routing, Zielsystem oder eine andere Ursache verantwortlich war.

Die vorhandenen [Actions-Workflows](.github/workflows) dokumentieren die damalige Startumgebung. Für einen eigenen Wiederholungsversuch benötigt man ein eigenes Testsystem, die konkret dokumentierte Produktversion, dessen Pairing-Material und die passende Verbindung. Die erhaltenen Skripte installieren keinen JBL-Server und erzeugen keinen Tunnel. Die damaligen Secrets sind kein Bestandteil dieser Dokumentation.

### August-Workflow und präzisierte Ausgabetexte

Das ergänzende Repository [jbl-wan-proof](https://github.com/Juri-Halveth/jbl-wan-proof) enthält einen älteren externen TCP-/HTTP-Prüfablauf. Die beiden August-Runs werden von GitHub als erfolgreich geführt. Ihre Joblogs waren am 27. November jedoch mit HTTP 410 nicht mehr abrufbar. Zudem beendet der damalige Workflow auch einen fehlgeschlagenen TCP-Verbindungsaufbau mit Exitcode 0. **Ein grüner Workflow ist hier kein Beleg für eine erfolgreiche Verbindung.**

[PR #2](https://github.com/Juri-Halveth/jbl-wan-proof/pull/2) präzisiert deshalb die Ausgaben. Ein TCP-Fehler wird als nicht aufgebaute Verbindung bezeichnet. Eine beobachtete HTTP-Statuszeile 101 wird als solche ausgegeben, ohne einen vollständig validierten WebSocket-Handshake oder die Identität eines JBL-Dienstes zu behaupten. Diese Quellkorrektur ist keine neue Netzwerkbeobachtung.

## Meldungsverlauf und Quellen

Die eigene Meldung nennt den **9. August 2026** als Erstmeldung über das HARMAN-Formular und einen weiteren berichteten Kontakt am 12. August. Die nun vorgelegte Mailkette datiert die konkrete Koordinationsanfrage an CERT@VDE und dessen Eingangsbestätigung auf den **2. September 2026**. Die frühere Zusammenfassung mit einer CERT-Bestätigung vom 1. September wird für diese Mailkette damit berichtigt.

Am **24. September** folgt die technische Bestätigung samt Versions- und Behebungsplanung. Am **19. Oktober** folgen die getrennten Entscheidungen zur Prämie und zur Finder-Nennung. Die Nachricht mit der Finderzusage vom 19. Oktober wird am **22. Oktober** an eine andere Adresse weitergeleitet. Die darüber stehende Antwort zum noch ausstehenden Advisory hat im gelieferten Text kein eigenes Datum und wird nicht auf den 22. Oktober umdatiert.

Die aktuelle Dokumentation verbindet drei Arten von Belegen: den technischen Inhalt der Meldung, die durch CERT@VDE übermittelten Engineering- und Koordinationsentscheidungen sowie die erhaltenen ergänzenden Actions-Läufe. Für diese Fortschreibung wurden Unterlagen gelesen; ein neuer Gerätetest wurde nicht durchgeführt.

## Dateien und Nachvollziehbarkeit

- [CERT@VDE-Korrespondenz: ausgewählte Nachrichten mit Datum und Quellenbindung](evidence/CERT-VDE-CORRESPONDENCE.md).
- [Erratum zur ersten öffentlichen Fassung](ERRATUM-20261127.md).
- [Quellen- und Belegindex](evidence/index.json).
- [Vier unverändert erhaltene ergänzende Receipts](evidence).
- [Zusätzlicher Tunnel-Witness](external_witness.py), [direkter TCP-Witness](direct_wan_witness.py) und [ergänzender WAN-Workflow](https://github.com/Juri-Halveth/jbl-wan-proof).

Die veröffentlichten Mailauszüge und extrahierten Receipts sind als abgeleitete Fassungen gekennzeichnet. Hashes binden diese Dateien; sie sind keine nachträgliche kryptografische Beglaubigung der gesamten Korrespondenz oder der historischen Experimente. Die fachlichen Bestätigungen und die Grenzen der einzelnen technischen Versuche sind jeweils ihrer Quelle zugeordnet.
