# JBL QuantumENGINE / QuantumServer: Sicherheitsforschung und Prüfbelege

**Forschung: Juri (Juri-Halveth). Dokumentationsstand: 27. November 2026.**

Diese Dokumentation veröffentlicht die verfügbaren technischen Unterlagen zu Juris Untersuchung der Netzwerksteuerung im Umfeld von JBL QuantumENGINE / QuantumServer. Sie verbindet den Quellcode mit den erhaltenen Laufbelegen, dem berichteten Meldungsverlauf und einem aktuellen Abgleich der öffentlichen Herstellerhinweise.

## Ergebnis der erhaltenen Versuche

Am **1. September 2026** protokollierte ein auf GitHub gestarteter Prüfclient über einen **vom Eigentümer eingerichteten temporären Tunnel** und mit **bereitgestelltem Pairing-Material** folgende Änderung des Protokollwerts `microphone.gain`:

**75 → 74 → 75.** Sowohl die Änderung auf 74 als auch die Wiederherstellung auf 75 wurden jeweils mit einer weiteren Leseabfrage desselben Clients bestätigt. Der erfolgreiche Lauf meldete keine Fehler.

Ein **separater direkter TCP-Verbindungsversuch zu Port 57120** endete dagegen nach **8009 ms im Timeout**, ohne aufgebauten TCP-Kanal und ohne gesendete Anwendungspayload. Tunnelzugriff und direkte Internet-Erreichbarkeit sind deshalb getrennte Befunde.

Juri meldete den weitergehenden Verdacht als Sicherheitsproblem. Die hier erhaltenen Belege zeigen eine kontrollierte Fernsteuerungsfunktion unter den genannten Voraussetzungen. **Eine Umgehung des Pairings oder eine Verletzung der vorgesehenen Rechte eines bereits gepairten Clients ist durch dieses Paket allein nicht nachgewiesen.** Die Originalbeobachtung bleibt damit sichtbar und nachprüfbar, einschließlich ihrer Voraussetzungen und der noch offenen Sicherheitsfrage.

## Die vier erhaltenen September-Läufe

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

Der [Witness-Client](external_witness.py) erhält `TUNNEL_URL`, `PAIR_FRAME_B64` und `WITNESS_MODE` aus seiner Umgebung. Er öffnet die WebSocket-Verbindung, sendet das bereitgestellte Pairing-Frame und erwartet eine Antwort mit genau einem Gerät. Anschließend vergleicht er den Gain aus dieser Antwort mit einer eigenen Leseabfrage. Im Modus `readonly` endet der Versuch dort. Im Modus `reversible-write` verändert er den Wert um einen Schritt, liest ihn erneut und versucht im `finally`-Block die Wiederherstellung einschließlich weiterer Leseabfrage.

Die erforderlichen Pairingdaten werden durch diesen Client **nicht beschafft**. Er führt keine Suche nach fremden Geräten durch. Die Belegfelder mit dem Wort `IndependentReadback` meinen eine zusätzliche RPC-Abfrage im selben Client; sie bezeichnen keine unabhängige zweite Implementierung oder physische Audiomessung. Das Feld `subprotocol` ist im Receipt vorgegeben; ein gesonderter Mitschnitt des tatsächlich ausgehandelten Subprotokolls liegt hier nicht vor.

Der [direkte Witness](direct_wan_witness.py) versucht einmalig einen TCP-Verbindungsaufbau mit einem Zeitlimit. Er sendet keine Anwendungspayload. Ein Timeout benennt die beobachtete Zeitüberschreitung; daraus folgt keine Diagnose, ob Firewall, Routing, Zielsystem oder eine andere Ursache verantwortlich war.

Die vorhandenen [Actions-Workflows](.github/workflows) dokumentieren die damalige Startumgebung. Für einen eigenen Wiederholungsversuch benötigt man ein eigenes Testsystem, die konkret dokumentierte Produktversion, dessen Pairing-Material und die passende Verbindung. Die erhaltenen Skripte installieren keinen JBL-Server und erzeugen keinen Tunnel. Die damaligen Secrets sind kein Bestandteil dieser Dokumentation.

### August-Workflow und präzisierte Ausgabetexte

Das ergänzende Repository [jbl-wan-proof](https://github.com/Juri-Halveth/jbl-wan-proof) enthält einen älteren externen TCP-/HTTP-Prüfablauf. Die beiden August-Runs werden von GitHub als erfolgreich geführt. Ihre Joblogs waren am 27. November jedoch mit HTTP 410 nicht mehr abrufbar. Zudem beendet der damalige Workflow auch einen fehlgeschlagenen TCP-Verbindungsaufbau mit Exitcode 0. **Ein grüner Workflow ist hier kein Beleg für eine erfolgreiche Verbindung.**

[PR #2](https://github.com/Juri-Halveth/jbl-wan-proof/pull/2) präzisiert deshalb die Ausgaben. Ein TCP-Fehler wird als nicht aufgebaute Verbindung bezeichnet. Eine beobachtete HTTP-Statuszeile 101 wird als solche ausgegeben, ohne einen vollständig validierten WebSocket-Handshake oder die Identität eines JBL-Dienstes zu behaupten. Diese Quellkorrektur ist keine neue Netzwerkbeobachtung.

## Versionen und aktueller Herstellerstatus

Die erhaltenen September-Receipts enthalten **keine konkrete QuantumENGINE-Version, QuantumServer.exe-Buildnummer, Headset-Firmware oder gebundene Hashes der Herstellerbinary**. Die Zuordnung zu Juris JBL-Testsystem stammt aus dem Untersuchungskontext. Eine genaue betroffene Versionsliste lässt sich aus diesen zwei Repositories daher nicht erstellen.

Die am 27. November gelesenen [offiziellen JBL-Release-Notes](https://support.jbl.com/us/en/howto/jbl-quantum-engine-software-release-notes-us/000018780.html) nennen unter anderem:

| QuantumENGINE-Version | Datum | Relevante Herstellerangabe |
| --- | --- | --- |
| 2.7.8 | 30.06.2026 | Fernsteuerungsunterstützung über die Quantum App |
| 2.8.6 | 21.08.2026 | Funktionsupdates und allgemein bezeichnete Fehlerbehebungen |
| 2.9.4 | 03.11.2026 | Funktionsupdates und allgemein bezeichnete Fehlerbehebungen; oberster Eintrag der gelesenen Seite |

In diesen Hinweisen und in der gelesenen [CERT@VDE-HARMAN-Liste](https://certvde.com/en/advisories/vendor/harman/) wurde keine eindeutig diesem QuantumServer-Befund zugeordnete Fixbestätigung gefunden. **Ob QuantumENGINE 2.9.4 den gemeldeten Fehler enthält oder behebt, wurde hier nicht praktisch geprüft.** Allgemeine Bugfixhinweise entscheiden diese Frage nicht. Die anderen dort aufgeführten JBL-Advisories betreffen Bluetooth-Produkte und dürfen nicht auf QuantumServer übertragen werden.

## Gemeldeter Verlauf und Anerkennung

Juri stellt seine Forschung mit diesem Paket öffentlich zur Nachprüfung bereit. Der bereitgestellte Betriebsbericht nennt folgenden Verlauf:

| Datum | Berichteter Vorgang | Quellenstatus |
| --- | --- | --- |
| 09.08.2026 | Erstmeldung an HARMAN | Angabe aus der bereitgestellten Betriebsakte; Originalkorrespondenz nicht in diesen Repositories |
| 01.09.2026 | Folgemeldung an HARMAN und Koordinationsmeldung an CERT@VDE, laut Betriebsakte mit sichtbaren Empfangsbestätigungen | Angabe aus der bereitgestellten Betriebsakte; Originalversandbelege hier nicht veröffentlicht |
| 01.09.2026 | Vier oben ausgewertete Prüfungen | Erhaltene GitHub-Actions-Logs und gebundener Quellcode |
| 27.11.2026 | Quellenprüfung und Aufbereitung der vorhandenen technischen Unterlagen zur Veröffentlichung | Dieser Bericht und sein [Quellenindex](evidence/index.json) |

Juri gibt an, bislang **keine Vergütung** für diese Meldung erhalten zu haben und den Befund weiterhin für offen zu halten. Der Zahlungsstatus wird hier als seine Angabe dokumentiert. Eine Ticketnummer, eine diesem Fall zugeordnete CVE oder eine herstellerseitige Bestätigung des behaupteten Sicherheitsimpacts sind in den hier geprüften Repository-Unterlagen nicht enthalten.

## Welche Sicherheitsfrage noch entschieden werden muss

Die konkrete offene Frage lautet: **Welche vorgesehene Zugriffsgrenze kann ein Client ohne die dafür erforderliche Berechtigung überschreiten?** Der erhaltene Tunnelversuch beginnt bereits mit vom Eigentümer bereitgestelltem Pairing-Material. Für eine weitergehende Aussage braucht es einen an Version und Konfiguration gebundenen Nachweis, wie ein unberechtigter Client Zugang erhält oder welche Rechte eines berechtigten Clients überschritten werden. Die von JBL selbst dokumentierte Fernsteuerungsfunktion ist dabei als mögliche Erklärung des beobachteten Verhaltens zu berücksichtigen.

Die vorhandenen Logs zeigen eine Änderung eines Protokollwerts. Sie belegen keine Audioaufnahme, beliebige Codeausführung, Persistenz oder praktische Wirkung auf die physische Mikrofonverstärkung. Auch ein konkreter UDP-Angriff ist in diesem Paket nicht dokumentiert.

Für den eigenen Betrieb kann eine gezielte Einschränkung der Netzwerkerreichbarkeit sinnvoll sein. Bei der im Betriebsbericht beschriebenen Windows-Installation waren die angelegten Windows-Regeln jedoch als `Inactive / CategoryDisabled` gemeldet, während Kaspersky die Firewallfilterung übernahm. Das Speichern dieser Windows-Regeln war deshalb kein Nachweis einer wirksamen Sperre. Ein bestätigter Produktfix oder eine praktisch geprüfte Ersatzmaßnahme wird hier nicht behauptet.

## Dateien und Nachvollziehbarkeit

- [Quellen- und Belegindex](evidence/index.json): Run-IDs, ausgeführte Commits, Extraktionsstatus und Dateihashes.
- [Vier erhaltene Receipts](evidence): erfolgreiche und fehlgeschlagene Versuche gemeinsam.
- [Witness-Quellcode](external_witness.py) und [direkter TCP-Witness](direct_wan_witness.py).
- [Ergänzender WAN-Workflow](https://github.com/Juri-Halveth/jbl-wan-proof).

Die extrahierten JSON-Dateien sind ausdrücklich als abgeleitete Fassungen gekennzeichnet. Ihre Hashes binden diese veröffentlichten Dateien, nicht nachträglich die Authentizität eines gesamten historischen Experiments. Historische Quellstände und die ursprünglichen Run-Links bleiben im Index auffindbar.
