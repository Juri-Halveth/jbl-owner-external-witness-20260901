[Deutsch](README.md) · [English](README.en.md) · [Русский](README.ru.md)

# JBL QuantumENGINE / QuantumServer security research

**Research and finder credit: Juri Janovski — HALVETH**  
Documentation updated: 27 November 2026 · **CERT@VDE case #642251**

[Full report, German](REPORT.md) · [Documented correspondence](evidence/CERT-VDE-CORRESPONDENCE.md) · [Technical evidence index](evidence/index.json)

## Main finding and vendor coordination

The core report concerns **local IPC access by a non-elevated Windows process and reuse of existing owner pairing state**. It is distinct from the supplementary external tunnel and direct TCP experiments preserved in this repository.

The supplied CERT@VDE correspondence records:

- **24 September 2026:** CERT@VDE relayed that engineering had validated the issue, confirmed **QuantumENGINE 2.7.8** as affected and agreed with the proposed severity assessment. The supplied text contains **no numerical severity score**. Analysis of additional versions was ongoing.
- The same message described a corrective update under development, then **planned for December 2026**. This is the historical release plan, not confirmation that a fix shipped.
- **19 October 2026:** CERT@VDE relayed HARMAN's decision that the submission did not qualify for a reward under its bounty program. A separate reply confirmed that Juri would be named as the finder in the advisory.
- **Latest supplied reply:** undated and following the 22 October exchange, it says the advisory was still unpublished and had no concrete publication date. Advisory and CVE links were to follow publication. No assigned CVE identifier or published advisory link appears in the supplied text.

## Supplementary technical records

A GitHub-hosted client recorded **75 → 74 → 75** for `microphone.gain`, including readback after the change and restoration, using an owner-created tunnel and supplied pairing material. A separate direct TCP attempt to port **57120** timed out after **8009 ms**, without a connection or application payload.

These logs document those particular experiments. Their limitations must not be generalized into a rejection of the separately reported, engineering-validated local IPC finding. They do not establish an unpaired Internet attack or a physical microphone measurement.

The correspondence reports a static comparison with 2.8.6, while explicitly leaving a clean runtime retest open. No new device or network test was performed for this documentation update; current-release impact and fix status are not inferred from the September logs.

