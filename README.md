# Small Language Models for Offline Disaster Response: A PRISMA Systematic Review of Edge Deployment and Safety Evidence

**Authors:** Rahul, Aryan, Dhairya, Computer Science and Engineering, Sharda University, Greater Noida, India

This repository contains the protocol, amendment log, audit trail, and analysis script for the systematic review. The review asks whether disaster-response systems built on small or locally deployable language models demonstrate what motivates them: on-device execution, operation without connectivity, and measured safety.

## Key results

- 14 studies were included from 13,490 records identified in IEEE Xplore, Scopus, OpenAlex, and arXiv (2019 to September 2026).
- Models of 1.5 to 9 billion parameters, adapted with LoRA, QLoRA, and 4-bit quantization, reach competitive task performance.
- An offline Bluetooth-mesh retrieval system reached Recall@5 of 0.89, against 0.95 for a cloud service.
- One study ran its model on physical edge hardware and one on emulated edge hardware. Two tested operation under network loss.
- No study has yet evaluated a disaster-guidance task offline, and safety is described rather than measured.
- The paper proposes an evidence-grading framework and a **Deployment Evidence Card** for reporting.

## PRISMA 2020 flow

| Stage | n |
|---|---|
| Records identified (IEEE Xplore 474; Scopus 281; OpenAlex 3,243; arXiv 9,492) | 13,490 |
| Duplicates removed | 1,498 |
| Records screened (title/abstract) | 11,992 |
| Records excluded | 11,936 |
| Reports sought for retrieval | 56 |
| Not retrieved (4 no access, 4 wrong document) + 1 late duplicate | 9 |
| Full texts assessed | 47 |
| After the document check (E1, E2) | 45 |
| Excluded at the eligibility check (E4 6, E5 7, E7 5) | 18 |
| Quality-rubric candidates | 27 |
| Excluded on quality (<5/8) and by the provenance scan (E4) | 11 + 2 |
| **Studies included** | **14** |

**Full-text funnel: 47 → 27 → 14.** At the corpus freeze (v2.5d, 20 September 2026) the funnel was 48 → 28 → 15. The v2.6 verification then found that three archived full texts, including one included study (S2418), were a different paper from the record sought. These reports were reclassified as *not retrieved*. See [`amendment_log.md`](amendment_log.md).

## Screening pipeline

1. **Stage 1:** Qwen2.5-7B (local, temperature 0) screens every record with a fixed JSON schema.
2. **Stage 2:** A human audits the machine decisions: all includes, a random 5% sample, and a recall-focused sample. The audit design was locked in advance with seed 42.
3. **Stage 3:** Qwen2.5-14B-Instruct (Ollama, `qwen2.5:14b-instruct`, 4-bit Q4_K_M) adjudicates the human-review queue in three majority-vote passes, and a human finalizes every record.
4. **Full text:** An eligibility check with quotation verification, a four-criterion quality rubric (Rigour, Evaluation, Context realism, Safety; threshold 5/8), and a deterministic provenance scan for cloud-only systems.

## Repository contents

```
├── README.md              this file
├── protocol.md            locked protocol: questions, eligibility (axes A/B/C, codes E1-E7),
│                          exact search strings for all databases, screening, rubric, grading
├── amendment_log.md       every change after the protocol was locked (v1.8 to v2.6)
├── data/                  audit trail (see data/README.md)
│   ├── final_corpus_verified.csv     the 14 included studies with evidence grades
│   ├── rubric_worksheet.csv          rubric scores and notes for the 28 frozen candidates
│   ├── final_papers_info.csv         metadata of the 15-study frozen corpus
│   ├── final_corpus_frozen_v2.5d.csv
│   ├── post_freeze_verification.csv
│   ├── search/  screening/  fulltext/  amendments/
└── scripts/
    └── verify_counts.py   reproduces every count reported in the paper
```

## Reproducing the counts

```bash
pip install pandas scipy
python scripts/verify_counts.py
```

The script prints the full PRISMA reconciliation, including the audit rates, the 56 reports sought by route, the full-text outcomes, the verified rubric scores, and the screening-sensitivity estimate. It also writes the summary to `counts.json`.

## Citation

```
Rahul, Aryan, and Dhairya, "Small Language Models for Offline Disaster Response:
A PRISMA Systematic Review of Edge Deployment and Safety Evidence," 2026.
Data and protocol: https://github.com/Aryan-0042/slm-disaster-response-slr
```

## Licence

No licence file has been added yet. The authors should add one, such as CC BY 4.0 for the data and documents and MIT for the script.
