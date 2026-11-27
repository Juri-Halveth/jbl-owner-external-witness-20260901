[Deutsch](README.md) · [English](README.en.md) · [Русский](README.ru.md)

# JBL QuantumENGINE: bestätigte Schwachstelle – Juri Janovski / HALVETH

**Finder: Juri Janovski — HALVETH · Vorgang: CERT@VDE #642251 · Stand: 27. November 2026**

**Laut dem vom Finder bereitgestellten Korrespondenztext teilte CERT@VDE am 24. September 2026 mit, dass das Engineering-Team den gemeldeten Fehler validiert hat und JBL QuantumENGINE 2.7.8 betroffen ist.** Die vorgeschlagene Schweregradeinschätzung wurde akzeptiert. Ein Korrekturupdate war damals in Entwicklung und für Dezember 2026 geplant.

**[Vollständiger Forschungsbericht](REPORT.md)** · **[Bestätigung und Korrespondenz](evidence/CERT-VDE-CORRESPONDENCE.md)** · [Korrektur der ersten Fassung](ERRATUM-20261127.md)

## Der Schwachstellenkern

Die koordinierte Meldung beschreibt einen lokalen Prozess ohne erhöhte Rechte, der mit einem frei angegebenen Clientnamen JBLs Remote-Control-IPC öffnen, Pairing- und Gerätemetadaten lesen und den vorhandenen Pairing-Zustand des Eigentümers zur Änderung einer Headset-Einstellung verwenden konnte. Änderung, Rücklesen, Wiederherstellung und erneutes Rücklesen sind Bestandteil des gemeldeten Befunds.

## Anerkennung und Prämie

Am **19. Oktober 2026** sagte CERT@VDE die Finder-Nennung im Advisory zu. Die separate Nachricht desselben Tages lehnt eine Belohnung unter HARMANs Bug-Bounty-Programm ab. **Die Prämienentscheidung widerruft die technische Bestätigung nicht.**

Eine spätere undatierte Antwort nach Juris Anfrage vom 22. Oktober bezeichnet das Advisory als noch unveröffentlicht, ohne konkreten Termin. Ein Advisory- und CVE-Link wurde für die Veröffentlichung angekündigt; eine konkrete CVE-Nummer steht nicht in der vorgelegten Kette.

## Ergänzende technische Belege

Die vorhandenen Tunnel-/TCP-Skripte untersuchen zusätzliche Fragen: Ein Tunnelversuch mit bereitgestellten Pairingdaten dokumentiert `microphone.gain` als **75 → 74 → 75** mit separaten Leseabfragen. Ein direkter TCP-Versuch auf Port 57120 endet nach **8009 ms im Timeout**. Diese Ergebnisse ersetzen die lokale IPC-Untersuchung nicht.

- [Vier erhaltene Laufbelege und Quellenindex](evidence/index.json).
- `external_witness.py`: zusätzlicher Tunnelversuch mit bereitgestelltem Pairing-Material.
- `direct_wan_witness.py`: einzelne direkte TCP-Verbindungsprobe.
- [Ergänzender WAN-Workflow](https://github.com/Juri-Halveth/jbl-wan-proof).

**Version 2.7.8 ist bestätigt betroffen.** Für 2.8.6 beschreibt die Meldung lediglich einen statischen Vergleich; ein Runtime-Retest blieb offen. Die aktuellen Herstellerhinweise nennen 2.9.4, ohne in den gelesenen Quellen einen diesem Fall eindeutig zugeordneten Fix zu benennen. Der [Bericht](REPORT.md) trennt bestätigte Betroffenheit, damalige Fixplanung und aktuellen ungeprüften Versionsstand.
