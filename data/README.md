# Data dictionary

All files are UTF-8 CSV, JSON, or JSON Lines. `stage_id` (for example `S0460`) is the record identifier used throughout the review and the paper. Abstracts and full texts are not redistributed, for copyright reasons, but every record can be located through its DOI, arXiv ID, or OpenAlex ID.

## Core files (start here)

| File | Contents |
|---|---|
| `final_corpus_verified.csv` | **The 14 included studies** after verification: models, hardware, evidence grades (A, X, O, C), baseline types, and verified rubric scores. |
| `rubric_worksheet.csv` | Quality-rubric worksheet for the 28 candidates scored at freeze (v2.5d): machine draft scores with quotations, human scores, and human notes. |
| `final_papers_info.csv` | Metadata of the 15 studies in the frozen corpus (v2.5d), before verification. |
| `final_corpus_frozen_v2.5d.csv` | Full screening record of the 15-study frozen corpus, with human rubric scores. |
| `post_freeze_verification.csv` | The five changes made by the v2.6 verification and the reason for each. |

## `search/`

| File | Contents |
|---|---|
| `ieee_core.csv`, `ieee_supp.csv`, `scopus.csv` | Database exports from 9 September 2026 (abstract column removed). |
| `openalex_records.csv`, `arxiv_records.csv` | Unique records per source, with the IDs of the queries that returned them (`search_id`). |
| `openalex_search_log.json`, `arxiv_search_log.json` | Every executed query and its raw hit count. |
| `search_registration.json`, `session_manifest.json` | Search registration (date, year range, sources) and SHA-256 checksums of the original exports. The checksums apply to the files before the abstract column was removed. |

## `screening/`

| File | Contents |
|---|---|
| `screening_trace.csv` | One row per unified record (12,249). Includes deduplication status, the Stage 1 verdict of the 7B screener, the class after audit, the final title/abstract decision and its basis, full-text retrieval status, and full-text class. |
| `dedup_clusters.csv` | Cross-database duplicate clusters. |
| `audit_lock_v1.9.json` | Locked audit design (seed, samples, decision bands). |
| `audit_includes.csv` | Human check of all machine includes. |
| `audit_random_worksheet.csv` | Random-sample audit of machine exclusions (575 canonical records). |
| `audit_recall_worksheet.csv` | Recall-focused audit of machine exclusions (1,209 records in five lanes). |
| `h2_adjudication.csv` | 14B-model adjudication of the human-review queue. |
| `triple_pass_audit.jsonl` | Three-pass majority-vote adjudication (all passes, votes, and quotations). |
| `human_final_queue.csv` | Human finalization of the 353 queue records. |

## `fulltext/`

| File | Contents |
|---|---|
| `acquisition_manifest.csv` | Retrieval status of the 56 reports sought. |
| `fulltext_verification.csv` | Eligibility check: machine verdicts with quotations, suggested class, and the human's final class for each report. |
| `k1_results.csv` | Raw machine output of the eligibility check. |
| `l1_scores.csv` | Machine draft rubric scores. |

## `amendments/`

Machine-readable amendment records (v1.8 to v2.5d). See `../amendment_log.md` for the readable log, including the v2.6 verification.

## Not included

Full-text PDFs and text files, and the evidence packs built from them, are not redistributed because they contain copyrighted text. They can be rebuilt from the DOIs and arXiv IDs.
