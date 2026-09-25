# Amendment Log

This log records every change made after the search and protocol were locked on 9 September 2026. Each entry has a type:

- **Rule**: a decision rule was added or changed.
- **Process**: a pre-specified step was carried out and recorded.
- **Verification**: a quality-control check was run after the corpus was frozen.

The machine-readable records for v1.8 to v2.5d are in `data/amendments/`.

| # | Version | Date (2026) | Type | Change and effect |
|---|---|---|---|---|
| 1 | v1.8 | 11 Sep | Process | Late fuzzy deduplication run over the full record set: 259 candidate pairs (10 resolved automatically, 4 flagged for review). |
| 2 | v1.9 | 11 Sep | Rule | **Audit design locked before any result was seen**: random seed 42; pre-drawn 5% random sample; recall lanes; decision bands (<2% proceed, 2-5% expand, >=5% rescreen). |
| 3 | v1.8c | 12 Sep | Process | Duplicate-pair adjudication: 175 pairs by rule, 108 by manual verdict. |
| 4 | v1.8b | 12 Sep | Process | Deduplication finalized: 257 late duplicates removed; 11,992 unique records. |
| 5 | v2.0 (H1-H3) | 15 Sep | Process | Human-review queue pre-filter and 14B adjudication (Qwen2.5-14B-Instruct via Ollama, 4-bit Q4_K_M). One non-research document excluded (S0594). Six records excluded by the 14B model as outside the disaster domain; one further record sampled for human check. |
| 6 | v2.1 | 15 Sep | Process | Audit rescues merged into the screening state: 7 from the random audit and 28 from the recall audit. The random-audit false-exclusion rate of 1.22% fell in the "proceed" band. |
| 7 | v2.2 / v2.2b | 15 Sep | Process | Queue finalized by the human reviewer after three-pass majority-vote adjudication: 353 records, of which 24 were forwarded and 329 excluded. Labels normalized (EXCLUDE to OUT; 247 records; no decision changed). |
| 8 | v2.3 | 18 Sep | Process | Retrieval closed. S0447 removed as a late duplicate (extended version of S0002). S0499 excluded E1 and S0584 excluded E2 at the document check. S0799, S0928, S1436, and S2427 not retrieved (no accessible full text). S2546 not retrieved (wrong document). |
| 9 | v2.4 | 19 Sep | Process | Eligibility check closed. The human reviewer assigned final classes: 25 A+B+C, 3 A+C, 8 E4, 7 E5, 5 E7. This left 28 rubric candidates. |
| 10 | v2.5 | 20 Sep | Process | Quality rubric applied (threshold 5/8): 11 excluded, 17 retained. Corpus frozen. |
| 11 | v2.5b-c | 20 Sep | Rule | **Deterministic provenance scan introduced.** S3496 (SafeMate; reasoning on o3-mini-high, compared with GPT-4o and GPT-3.5, no small or local model) recoded E4 and its rubric scores voided. Corpus: 16. |
| 12 | v2.5d | 20 Sep | Rule | **Provenance scan (V4) applied to every retained candidate.** Full texts were scanned for cloud-model names and inference APIs and for evidence of a small or local model. S0043 (wildfire risk framework; LLM stage on GPT-4.1 and GPT-5.2) recoded E4. S3510 retained (no cloud-model identifiers). Corpus refrozen: 15. |
| 13 | v2.6 | 25 Sep | Verification | **Retrieval-integrity check.** Every archived full text was matched against its record's title and authors. Three files were a different paper from the record sought: S0005 (a 1999 tornado survey report), S1258 (a 2011 review on crowdsourcing and citizen sensing), and S2418 (Kagai et al., *Voice Over LoRa*, ICOIN 2024, which contains no language model). These three were reclassified as *not retrieved*, following the rule already applied to S2546. S2418 is listed as awaiting classification until its full text (Amirkhanov et al., Nazarbayev University Repository, 2025) is obtained. S0005 and S1258 had been excluded as E4, so the included set is unaffected. |
| 14 | v2.6 | 25 Sep | Verification | **Re-check of every score of 2 on context realism (CR) and safety (S) among included studies.** S0577 CR lowered from 2 to 1: its only disconnection test is attributed to a cited source. S0093 S lowered from 2 to 1: its archived quotation concerned latency, and the paper only describes design choices to limit hallucination. Both studies remain included (totals 5 and 6). Details: `data/post_freeze_verification.csv`. |
| 15 | v2.6 | 25 Sep | Verification | **Documentation corrections.** Axis B is described in the manuscript as it was applied in screening (architecture: agentic, multi-agent, RAG, tool-use, or state-machine pipeline). Comparative evaluation entered eligibility only through the E4 rule. S0610's landing-page pack was supplemented with its arXiv full text (v2) for data extraction. |

## Effect on the PRISMA counts

| Stage | Frozen (v2.5d) | After verification (v2.6) |
|---|---|---|
| Reports sought | 56 | 56 |
| Not retrieved (plus late duplicate) | 5 (+1) | 8 (+1) |
| Full texts assessed | 50 | 47 |
| After the document check (E1, E2) | 48 | 45 |
| Quality-rubric candidates | 28 | 27 |
| Studies included | 15 | **14** |

The central finding does not change between the two states: no included study combines a measured offline test with a disaster-specific evaluation.
