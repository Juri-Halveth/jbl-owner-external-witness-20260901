[Deutsch](README.md) · [English](README.en.md) · [Русский](README.ru.md)

# JBL QuantumENGINE / QuantumServer – Forschung von Juri

**Juri (Juri-Halveth) · Stand 27. November 2026**

Hier liegen Quellcode und erhaltene Prüfbelege zu Juris Untersuchung der Netzwerksteuerung im Umfeld von JBL QuantumENGINE / QuantumServer.

## Einstieg

**[Vollständiger Forschungsbericht](REPORT.md)** · **[Belege und Quellenindex](evidence/index.json)** · [Ergänzender WAN-Prüfablauf](https://github.com/Juri-Halveth/jbl-wan-proof)

Ein GitHub-Prüfclient protokollierte am 1. September 2026 den Gain-Verlauf **75 → 74 → 75**, einschließlich separater Leseabfragen nach Änderung und Wiederherstellung. Er verwendete einen vom Eigentümer eingerichteten Tunnel und bereitgestelltes Pairing-Material. Ein separater direkter TCP-Versuch zu Port **57120** endete nach **8009 ms im Timeout**.

Das Paket enthält den erfolgreichen Lauf, einen reinen Leseversuch, einen fehlgeschlagenen Zwischenlauf und die direkte Verbindungsprobe. Die Skripte sind vorhanden; ihre historischen Aufzeichnungen wurden für diesen Bericht gelesen und nicht erneut gegen ein Gerät ausgeführt.

## Sicherheitsstatus

Der gemeldete Sicherheitsverdacht wird zusammen mit seinen tatsächlichen Versuchsbedingungen veröffentlicht. Die erhaltenen Belege weisen allein keinen Zugriff ohne Pairing und keine standardmäßige Internet-Erreichbarkeit nach. Eine genaue betroffene QuantumENGINE-/QuantumServer-Version fehlt in den historischen Receipts.

Die am 27. November geprüften Herstellerhinweise nennen **QuantumENGINE 2.9.4 vom 3. November 2026**. Eine ausdrücklich diesem Befund zugeordnete Fixbestätigung wurde darin nicht gefunden; die aktuelle Version wurde hier nicht praktisch geprüft. Der [Bericht](REPORT.md) dokumentiert diesen offenen Status und den von Juri bereitgestellten Meldungsverlauf.

## Inhalt

- `external_witness.py`: Leseversuch sowie begrenzte Änderung und Wiederherstellung mit bereitgestelltem Pairing-Material.
- `direct_wan_witness.py`: einzelner TCP-Verbindungsversuch ohne Anwendungspayload.
- `.github/workflows/`: vorhandene manuell gestartete Prüfabläufe.
- `evidence/`: vier aus den historischen Logs extrahierte Receipts und Quellenindex. Die markierte Redaktion betrifft den Pairing-Fingerprint; Ziel- und Pairingwerte werden nicht ergänzt.

Die vollständige Einordnung, Quellstände, Grenzen und Herstellerlinks stehen im [Forschungsbericht](REPORT.md).
