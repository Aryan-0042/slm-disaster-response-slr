# Review Protocol

**Small Language Models for Offline Disaster Response: A PRISMA Systematic Review of Edge Deployment and Safety Evidence**

Authors: Rahul, Aryan, Dhairya (Computer Science and Engineering, Sharda University, Greater Noida, India)

| Item | Value |
|---|---|
| Reporting guideline | PRISMA 2020 |
| Search registered and locked | 9 September 2026 (`data/search/search_registration.json`) |
| Audit design locked | 11 September 2026, before any audit result (`data/screening/audit_lock_v1.9.json`) |
| Corpus frozen | 20 September 2026 (amendment v2.5d) |
| Post-freeze verification | 25 September 2026 (amendment v2.6, see `amendment_log.md`) |
| Public registration | Not prospectively registered in a public registry; this repository is the public record |

This document restates the locked protocol. Steps that were added after the protocol was locked are marked **[Amendment]** and are explained in [`amendment_log.md`](amendment_log.md).

## 1. Review questions

- **RQ1.** Which small or locally deployable language-model systems have been proposed for civilian disaster response, and how are they built (models, adaptation, architecture, hardware, networking).
- **RQ2.** Where the models in these systems actually run, and whether operation under absent or degraded connectivity has been tested.
- **RQ3.** How the systems are evaluated (data, baselines) and how safety is reported.
- **RQ4.** Which reporting and research steps are needed to make deployment claims verifiable.

## 2. Eligibility criteria

| Code | Definition | Role |
|---|---|---|
| A | Model class: a small, quantized, distilled, on-device, or otherwise locally deployable language model (vision-language models included) | Required |
| B | Architecture: the model is embedded in an agentic, multi-agent, retrieval-augmented (RAG), tool-use, or state-machine pipeline | Recorded (used to label studies A+B+C or A+C) |
| C | Domain: civilian disaster, emergency response, mass-casualty, or humanitarian setting (including civilian humanitarian response in armed conflict) | Required |

Exclusion codes:

| Code | Reason |
|---|---|
| E1 | Non-English title/abstract or full text |
| E2 | Not a research document (front matter, editorial, software report) |
| E3 | Full text unavailable (reported as *not retrieved* in the PRISMA flow) |
| E4 | Axis A not met: only large or cloud-hosted models, with no smaller or local variant deployed or compared |
| E5 | No language-model component |
| E6 | Military or war-gaming application without a humanitarian component (title/abstract stage only) |
| E7 | Axis C not met: no disaster, emergency, or humanitarian domain |
| Q | Quality rubric total below 5/8 (Section 6) |

Routine settings without disaster grounding (for example hospital triage, traffic control, or grid maintenance) fail axis C. Preprints are eligible. No restriction on study design is applied beyond E2.

## 3. Information sources and search strategy

- Databases: IEEE Xplore, Scopus, OpenAlex, arXiv.
- Search date: 9 September 2026. Publication years: 2019 to 2026 (inclusive).
- Records returned by more than one query within a source are merged before counting.

| Source | Fields searched | Queries | Unique records |
|---|---|---|---|
| IEEE Xplore | All Metadata (document title, abstract, index terms) | 2 (core, supplementary) | 474 (180 + 294) |
| Scopus | TITLE-ABS-KEY | 1 | 281 |
| OpenAlex | API endpoint `https://api.openalex.org/works`; title, abstract, concepts | 48 | 3,243 (3,842 raw hits) |
| arXiv | arXiv API, `all:` field | 5 | 9,492 (9,842 raw hits) |
| **Total** | | **56** | **13,490** |

### 3.1 IEEE Xplore, core set (180 records)

```
("All Metadata":("language model*" OR LLM OR SLM) AND "All Metadata":("small" OR lightweight OR quantiz* OR distill* OR "on-device" OR "edge deploy*" OR offline OR local OR compact OR "open-weight*") AND "All Metadata":(agent* OR "multi-agent" OR RAG OR "retrieval-augmented" OR "state machine" OR "tool use" OR orchestrat*) AND "All Metadata":(disaster OR emergency OR crisis OR conflict OR war OR humanitarian OR "mass casualty" OR triage OR evacuation OR "first aid" OR flood OR earthquake OR wildfire OR cyclone OR rescue OR "search and rescue" OR refugee OR displaced OR "armed conflict" OR "humanitarian crisis"))
```

### 3.2 IEEE Xplore, supplementary set (294 records)

```
("All Metadata":("large language model*" OR LLM) AND "All Metadata":("small language model*" OR SLM OR lightweight OR quantiz* OR distill* OR "on-device" OR offline OR local OR compact) AND "All Metadata":(disaster OR emergency OR crisis OR conflict OR war OR humanitarian OR "mass casualty" OR triage OR evacuation OR "first aid" OR flood OR earthquake OR wildfire OR cyclone OR rescue OR refugee OR displaced OR "armed conflict" OR "humanitarian crisis"))
```

### 3.3 Scopus (281 records)

```
TITLE-ABS-KEY ( ( "language model*" OR LLM OR SLM OR Llama* OR Qwen* OR Gemma OR Phi OR Mistral* ) AND ( small OR lightweight OR quantiz* OR distill* OR distil* OR "on-device" OR "edge deploy*" OR offline OR local OR compact OR "open-weight*" ) AND ( agent* OR "multi-agent" OR RAG OR "retrieval-augmented" OR "state machine" OR "tool use" OR orchestrat* ) AND ( disaster OR emergency OR crisis OR conflict OR war OR humanitarian OR "mass casualty" OR triage OR evacuation OR "first aid" OR flood OR earthquake OR wildfire OR cyclone OR rescue OR "search and rescue" OR refugee OR displaced ) )
```

### 3.4 arXiv (5 queries; raw hits in the last column)

| ID | Query | Hits |
|---|---|---|
| AX_q1 | `(all:"small language model" OR all:"on-device LLM" OR all:"offline LLM" OR all:"lightweight LLM" OR all:"quantized language model" OR all:"edge LLM") AND (all:disaster OR all:emergency OR all:crisis OR all:humanitarian OR all:triage OR all:evacuation OR all:"first aid" OR all:"mass casualty")` | 168 |
| AX_q2 | `(all:"small language model" OR all:"on-device LLM" OR all:"offline LLM") AND (all:conflict OR all:war OR all:"armed conflict" OR all:refugee OR all:displaced)` | 21 |
| AX_q3 | `(all:RAG OR all:"retrieval-augmented generation" OR all:agentic OR all:"multi-agent LLM") AND (all:disaster OR all:emergency OR all:"emergency response" OR all:"search and rescue")` | 7191 |
| AX_q4 | `all:"small language model" AND (all:hallucination OR all:safety)` | 109 |
| AX_q5 | `(all:"large language model" AND (all:"small language model" OR all:quantized OR all:distilled)) AND (all:disaster OR all:emergency OR all:efficiency)` | 2353 |

### 3.5 OpenAlex (48 queries; raw hits in the last column)

| ID | Query | Hits |
|---|---|---|
| OA_q1 | `"small language model" disaster` | 18 |
| OA_q2 | `"small language model" emergency` | 39 |
| OA_q3 | `"small language model" crisis` | 14 |
| OA_q4 | `"small language model" war` | 4 |
| OA_q5 | `"small language model" humanitarian` | 0 |
| OA_q6 | `"small language model" conflict` | 70 |
| OA_q7 | `"local LLM" disaster` | 0 |
| OA_q8 | `"local LLM" emergency` | 8 |
| OA_q9 | `"local LLM" conflict` | 30 |
| OA_q10 | `"local language model" disaster` | 1 |
| OA_q11 | `"local language model" emergency` | 1 |
| OA_q12 | `"offline LLM" disaster` | 0 |
| OA_q13 | `"offline LLM" emergency` | 2 |
| OA_q14 | `"offline language model" disaster` | 0 |
| OA_q15 | `"offline language model" emergency` | 0 |
| OA_q16 | `"on-device LLM" disaster` | 2 |
| OA_q17 | `"on-device LLM" emergency` | 0 |
| OA_q18 | `"on-device language model" emergency` | 0 |
| OA_q19 | `"edge LLM" disaster` | 0 |
| OA_q20 | `"edge LLM" emergency` | 2 |
| OA_q21 | `"quantized LLM" disaster` | 0 |
| OA_q22 | `"quantized LLM" emergency` | 1 |
| OA_q23 | `"lightweight LLM" disaster` | 4 |
| OA_q24 | `"lightweight LLM" emergency` | 4 |
| OA_q25 | `"distilled LLM" disaster` | 1 |
| OA_q26 | `"distilled LLM" emergency` | 0 |
| OA_q27 | `"distilled language model" humanitarian` | 0 |
| OA_q28 | `LLM RAG disaster response` | 37 |
| OA_q29 | `LLM RAG emergency` | 161 |
| OA_q30 | `LLM RAG conflict` | 495 |
| OA_q31 | `LLM RAG humanitarian` | 13 |
| OA_q32 | `LLM agent disaster` | 201 |
| OA_q33 | `LLM agent emergency` | 293 |
| OA_q34 | `LLM agent conflict` | 1518 |
| OA_q35 | `"multi-agent LLM" disaster` | 7 |
| OA_q36 | `"multi-agent LLM" emergency` | 14 |
| OA_q37 | `"language model" "state machine" emergency` | 3 |
| OA_q38 | `"language model" "state machine" disaster` | 0 |
| OA_q39 | `"language model" "tool use" disaster` | 17 |
| OA_q40 | `"LLM" "tool use" emergency` | 17 |
| OA_q41 | `"large language model" "small language model" disaster` | 3 |
| OA_q42 | `"large language model" "small language model" emergency` | 15 |
| OA_q43 | `"large language model" quantized disaster` | 3 |
| OA_q44 | `"large language model" distilled emergency` | 9 |
| OA_q45 | `LLM distillation disaster` | 7 |
| OA_q46 | `"small language model" hallucination` | 288 |
| OA_q47 | `LLM hallucination disaster` | 44 |
| OA_q48 | `LLM safety emergency` | 496 |

The executed queries and their hit counts are logged in `data/search/openalex_search_log.json` and `data/search/arxiv_search_log.json`.

## 4. Deduplication

1. Record unification: records merged into cross-database clusters by DOI, arXiv or OpenAlex identifier, or normalized title (1,241 records collapsed into 979 clusters; `data/screening/dedup_clusters.csv`).
2. Late fuzzy title matching with rule-based and manual adjudication of candidate pairs (257 further duplicates removed; amendments v1.8 to v1.8b). Result: 11,992 unique records.

## 5. Title and abstract screening

**Stage 1: machine screen.** Every record is screened by Qwen2.5-7B, run locally at temperature 0 with a fixed JSON schema (configuration tag `qwen2.5:7b_temp0_schema_v1`). For each axis the model answers yes, no, or unsure, sets exclusion flags E1, E2, E4, E5, E6, and E7, and quotes supporting text from the title or abstract. Output classes: include (A+B+C or A+C), human review, or exclude.

**Stage 2: human audit (design locked 11 September 2026).**

- Random seed: 42.
- A false exclusion is a Stage 1 exclusion that, under the locked rules, should have been an include or a human-review record.
- Decision bands: false-exclusion rate <2% proceed; 2% to <5% expand the sample by 5%; >=5% stop and rescreen.
- Worksheets: (i) all machine includes; (ii) a pre-drawn simple random sample of 5% of the unified records, restricted to canonical Stage 1 exclusions (`data/screening/audit_random_worksheet.csv`); (iii) a recall-focused sample in five query-based lanes (`data/screening/audit_recall_worksheet.csv`):
  - strict lanes: 100% of OUTs;
  - AX_q5: 15% random;
  - AX_q3: 100 random;
  - OpenAlex q28 to q40: 10% random;
  - OpenAlex q46 to q48 and AX_q4: 5% random (secondary safety).
- Rescued records are forwarded to full-text retrieval or to the Stage 3 queue.

**Stage 3: human-review queue.** Records flagged for human review and audit rescues routed to the queue are:

1. checked for document type;
2. adjudicated by Qwen2.5-14B-Instruct, run locally through Ollama (`qwen2.5:14b-instruct`, 4-bit Q4_K_M weights);
3. adjudicated in three passes with a majority vote per axis (`data/screening/triple_pass_audit.jsonl`);
4. finalized by the human reviewer (`data/screening/human_final_queue.csv`).

## 6. Full-text assessment

1. **Retrieval.** Open-access and institutional sources are used. Reports without accessible full text are recorded as *not retrieved*, and so is a retrieved file that turns out to be a different document.
2. **Document check.** E1 and E2 are applied at the document level.
3. **Eligibility check.** Each full text is reduced to an evidence pack (title, abstract, and keyword-targeted verbatim extracts on model size, architecture, deployment, domain, comparisons, and large-model identifiers; about 6,000 to 6,900 characters). The 14B model proposes an eligibility class with a verbatim quotation for every verdict, and each quotation is checked automatically against the pack. The human reviewer assigns the final class for every report (`data/fulltext/fulltext_verification.csv`).
4. **Quality rubric.** Each remaining candidate is scored 0 to 2 on four criteria. Machine drafts (`data/fulltext/l1_scores.csv`) set the reading order, and every final score is assigned by the human reviewer (`data/rubric_worksheet.csv`). Inclusion threshold: total at least 5/8.

| Criterion | Score 1 | Score 2 |
|---|---|---|
| Rigour (R) | Method described; reproducibility gaps | Detailed method with configuration and reproducibility information |
| Evaluation (E) | Small-scale or own test set; weak or absent baselines | Established benchmark or dataset, or user study, against baselines |
| Context realism (CR) | Disaster context as motivation only | Offline or disconnected conditions actually tested or simulated |
| Safety (S) | Limitations mentioned | Systematic treatment of risks, guardrails, or failure modes |

A score of 0 means the score-1 description is not met. Hard rule for CR: a score of 2 requires evidence that offline or disconnected conditions were tested or simulated. Language that only motivates offline use is capped at 1.

5. **[Amendment v2.5b to v2.5d] Provenance scan.** The full text of each retained candidate is scanned for cloud-model names and inference-API services, and for evidence of a small or local model (named models with parameter counts, local runtimes, quantization). A candidate with cloud models and no small- or local-model evidence is recoded E4.

## 7. Data extraction

For each included study, the following items are extracted:

- bibliographic data and publication type;
- task and disaster context;
- each language model, with its size and numerical precision;
- adaptation method and architecture;
- the hardware used for the reported results;
- network setting and protocol;
- evaluation data, baselines, and reported results;
- offline conditions tested;
- safety content.

## 8. Evidence grading and synthesis [added for the analysis, 25 September 2026]

The grading framework is an analysis tool and was not an eligibility rule. Each included study is graded on four dimensions:

| Dimension | Levels |
|---|---|
| Model provenance (A) | A1 named model of stated size up to 10B produces the main outputs; A2 local execution but model unnamed, or open-weights model above 10B; A3 small model present but core reasoning on a large remote model; A4 model not identified |
| Execution hardware (X) | X3 physical edge-class device; X2 emulated edge device; X1 workstation, laptop, or server GPU; X0 cloud, simulation only, or not stated |
| Offline evaluation (O) | O3p offline or degraded operation tested with measurements; O3s such a test only cited from other work; O2 local inference on realistic hardware, network not varied; O1 discussed only; O0 not considered |
| Disaster evaluation (C) | C1 disaster-specific data or tasks; C2 disaster one of several domains; C3 disaster as motivation only |

Studies are grouped by the role of the model's output: communication and edge infrastructure; decision support and coordination; information access; perception and geospatial analysis. Results are synthesized in narrative and tables. Counts are descriptive, and no meta-analysis is performed.

**Screening-sensitivity estimate.** The number of includable studies among Stage 1 exclusions is estimated as N_out x k / n from the random audit sample, with an exact Clopper-Pearson 95% interval. Here N_out is the number of Stage 1 exclusions, n the random-sample size, and k the number of sampled exclusions that ended as included studies.
