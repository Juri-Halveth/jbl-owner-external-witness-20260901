[Deutsch](README.md) · [English](README.en.md) · [Русский](README.ru.md)

# JBL QuantumENGINE / QuantumServer research by Juri

**Juri (Juri-Halveth) · Updated 27 November 2026**

[Full research report, German](REPORT.md) · [Evidence and source index](evidence/index.json) · [Related WAN workflow](https://github.com/Juri-Halveth/jbl-wan-proof)

This repository contains the existing test clients and retained records from Juri's investigation of network control associated with JBL QuantumENGINE / QuantumServer.

On 1 September 2026, a GitHub-hosted client recorded `microphone.gain` changing **75 → 74 → 75**, with separate read requests confirming both the change and restoration. The client used an **owner-created temporary tunnel and supplied pairing material**. A separate direct TCP connection attempt to port **57120** timed out after **8009 ms**, without a connection or application payload.

The evidence includes the successful write-and-restore run, a read-only run, a failed intermediate run and the direct TCP test. The retained logs were reviewed for this publication; the tests were not rerun against a device.

These records alone do not establish a pairing bypass, default Internet exposure or a breach of the intended privileges of a paired client. They do not identify an exact affected QuantumENGINE or QuantumServer build. Separate readback means another RPC in the same client, not a physical microphone measurement.

JBL's release notes reviewed on 27 November list **QuantumENGINE 2.9.4, dated 3 November 2026**. No fix statement specifically matching this report was found in the reviewed release notes or CERT@VDE's HARMAN list. Whether version 2.9.4 is affected was not tested. The full report preserves this distinction and attributes the supplied disclosure chronology and payment statement to Juri.

`external_witness.py` implements the paired read/write-and-restore experiment. `direct_wan_witness.py` attempts one TCP connection without application payload. The `evidence/` files are extracted historical receipts with an explicitly marked pairing-fingerprint redaction and links to their source runs.
