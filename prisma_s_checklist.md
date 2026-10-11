# PRISMA-S Checklist

This checklist reports the literature search against the PRISMA-S extension (Rethlefsen et al., *Systematic Reviews* 10:39, 2021, doi:10.1186/s13643-020-01542-z). The descriptions below are summaries written for this review.

| # | Item | How this review reports it | Location |
|---|---|---|---|
| 1 | Database name | IEEE Xplore (IEEE Xplore platform), Scopus (Elsevier Scopus platform), OpenAlex (OpenAlex API, `https://api.openalex.org/works`), arXiv (arXiv API). | `protocol.md` Sec. 3; paper Sec. III-A |
| 2 | Multi-database searching | Not applicable: each database was searched separately on its own platform. | `protocol.md` Sec. 3 |
| 3 | Study registries | No study registries were searched. | This checklist |
| 4 | Online resources and browsing | No websites, tables of contents, or print sources were browsed. | This checklist |
| 5 | Citation searching | Backward and forward citation searching was not performed. It is planned for the review update. | Paper Sec. V-C |
| 6 | Contacts | No authors, experts, or organizations were contacted to identify studies. | This checklist |
| 7 | Other methods | No other search methods were used. | This checklist |
| 8 | Full search strategies | The exact strings for all 56 queries (IEEE Xplore 2, Scopus 1, OpenAlex 48, arXiv 5), as run. | `protocol.md` Sec. 3.1-3.5; `data/search/*_search_log.json` |
| 9 | Limits and restrictions | Publication years 2019-2026 (inclusive). The search strings contain no language or document-type limits; non-English reports and non-research documents were excluded at screening (codes E1, E2). | `protocol.md` Sec. 2-3 |
| 10 | Search filters | No published search filters were used. | This checklist |
| 11 | Prior work | The search strategies were developed for this review and piloted before the locked search (`01_search/pilot` in the review archive). No strategy from another review was reused. | `protocol.md` Sec. 3 |
| 12 | Updates | No update searches have been run. | Paper Sec. V-C |
| 13 | Dates of searches | All searches were run on 9 September 2026. | `data/search/search_registration.json`; paper Sec. III-A |
| 14 | Peer review | No formal peer review of the search strategies (for example PRESS) is documented. | This checklist |
| 15 | Total records | IEEE Xplore 474 (core 180; supplementary 294); Scopus 281; OpenAlex 3,243 (3,842 raw hits); arXiv 9,492 (9,842 raw hits); total 13,490. | Paper Sec. III-A and Fig. 1; `data/search/` |
| 16 | Deduplication | Two passes with custom scripts. First, records were grouped into cross-database clusters by DOI, arXiv or OpenAlex identifier, or normalized title (1,241 duplicate copies removed across 979 clusters). Second, fuzzy title matching with rule-based and manual adjudication of candidate pairs removed 257 more. | `protocol.md` Sec. 4; `data/screening/dedup_clusters.csv`; `amendment_log.md` #1, #3, #4 |
