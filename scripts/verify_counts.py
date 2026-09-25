"""
Reproduce every count reported in the paper from the files in data/.

Usage (from the repository root):
    pip install pandas scipy
    python scripts/verify_counts.py

The script prints a JSON summary and writes it to counts.json. It applies
the post-freeze verification documented in amendment_log.md and
data/post_freeze_verification.csv:
  * S0005, S1258, and S2418 are treated as not retrieved (the archived file
    was a different paper), as the protocol already did for S2546.
  * Two rubric scores are revised from 2 to 1 (S0093 safety; S0577 context
    realism).
"""
import json
import os

import pandas as pd
from scipy.stats import beta

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def path(*p):
    return os.path.join(ROOT, *p)


def read(*p):
    return pd.read_csv(path(*p), low_memory=False)


def cp_interval(k, n):
    """Exact Clopper-Pearson 95% interval for a binomial proportion."""
    lo = beta.ppf(0.025, k, n - k + 1) if k > 0 else 0.0
    hi = beta.ppf(0.975, k + 1, n - k) if k < n else 1.0
    return lo, hi


out = {}

# ---------------------------------------------------------------- identification
ids = dict(
    ieee=len(read("search", "ieee_core.csv")) + len(read("search", "ieee_supp.csv")),
    scopus=len(read("search", "scopus.csv")),
    openalex=len(read("search", "openalex_records.csv")),
    arxiv=len(read("search", "arxiv_records.csv")),
)
ids["total"] = sum(ids.values())
out["identified"] = ids

trace = read("screening", "screening_trace.csv")
out["unified_records"] = len(trace)
out["collapsed_in_unification"] = ids["total"] - len(trace)
out["dedup_clusters"] = int(read("screening", "dedup_clusters.csv").survivor.nunique())
canon = trace[trace.dedup_status_ta == "canonical"]
out["screened"] = len(canon)
out["late_fuzzy_removed"] = len(trace) - len(canon)

# ---------------------------------------------------------------- stage 1
out["stage1_screener"] = sorted(trace.screener.dropna().unique().tolist())
out["stage1_classes"] = canon.stage1_class.value_counts().to_dict()
n_out = int((canon.stage1_class == "OUT").sum())

# ---------------------------------------------------------------- stage 2 audits
inc = read("screening", "audit_includes.csv")
inc_c = inc[inc.dedup_status == "canonical"]
out["include_audit_canonical"] = inc_c.human_verdict.value_counts().to_dict()

rnd = read("screening", "audit_random_worksheet.csv")
rec = read("screening", "audit_recall_worksheet.csv")
k_r = int((rnd.human_should_be != "correct_OUT").sum())
k_c = int((rec.human_should_be != "correct_OUT").sum())
out["random_audit"] = dict(n=len(rnd), false_exclusions=k_r, rate=k_r / len(rnd),
                           ci95=cp_interval(k_r, len(rnd)))
out["recall_audit"] = dict(n=len(rec), false_exclusions=k_c, rate=k_c / len(rec),
                           lanes=rec.audit_lane.value_counts().to_dict())
ov = rnd.merge(rec, on="stage_id", suffixes=("_r", "_c"))
fwd_r = ov.human_should_be_r != "correct_OUT"
fwd_c = ov.human_should_be_c != "correct_OUT"
out["audit_overlap"] = dict(n=len(ov), agree=int((fwd_r == fwd_c).sum()),
                            disagreements=ov[fwd_r != fwd_c].stage_id.tolist())

# ---------------------------------------------------------------- stage 3 queue
q = trace[(trace.dedup_status_ta == "canonical") & (trace.class_after_audit == "HUMAN_REVIEW")]
basis = q.ta_final_basis.fillna("")
hq = read("screening", "human_final_queue.csv")
tags = {}
with open(path("screening", "triple_pass_audit.jsonl")) as fh:
    for line in fh:
        x = json.loads(line)
        if x["status"] != "API_ERROR":
            tags[x["stage_id"]] = x.get("intersection_tag", "")
hq["tag"] = hq.stage_id.map(tags).fillna("none")
hq_fwd = hq.final_class.str.startswith("INCLUDE")
out["queue"] = dict(
    total=len(q),
    excluded_nonresearch=int(basis.str.startswith("v2.0 H1").sum()),
    excluded_by_14b=int(basis.str.startswith("v2.0 H2").sum()),
    triple_pass_and_human=len(hq),
    tags=hq.tag.value_counts().to_dict(),
    forwarded=int(hq_fwd.sum()),
    excluded=int((~hq_fwd).sum()),
    agreement_with_tag=int((hq_fwd == hq.tag.str.startswith("INCLUDE")).sum()),
)

# ---------------------------------------------------------------- retrieval
man = read("fulltext", "acquisition_manifest.csv")
t = trace.set_index("stage_id")
route = {}
for s in man.stage_id:
    b = str(t.loc[s, "ta_final_basis"])
    if str(t.loc[s, "stage1_class"]).startswith("INCLUDE"):
        route[s] = "confirmed machine include"
    elif "random_5pct" in b:
        route[s] = "random-audit rescue"
    elif "recall" in b or s == "S0499":  # S0499 basis overwritten at full text
        route[s] = "recall-audit rescue"
    elif "human confirmed include" in b:
        route[s] = "queue include"
    else:
        route[s] = "UNRESOLVED"
out["sought"] = len(man)
out["sought_by_route"] = pd.Series(route).value_counts().to_dict()

WRONG_DOCUMENT = ["S2546", "S0005", "S1258", "S2418"]
NO_ACCESS = ["S0799", "S0928", "S1436", "S2427"]
LATE_DUPLICATE = ["S0447"]
assessed = [s for s in man.stage_id if s not in WRONG_DOCUMENT + NO_ACCESS + LATE_DUPLICATE]
out["not_retrieved"] = dict(no_access=NO_ACCESS, wrong_document=WRONG_DOCUMENT)
out["assessed"] = len(assessed)

# ---------------------------------------------------------------- full-text outcomes
ftv = read("fulltext", "fulltext_verification.csv").set_index("stage_id")
rub = read("rubric_worksheet.csv").set_index("stage_id")
DOC_GATE = {"S0499": "E1", "S0584": "E2"}
PROVENANCE_E4 = ["S0043", "S3496"]
outcome = {}
for s in assessed:
    if s in DOC_GATE:
        outcome[s] = DOC_GATE[s]
    elif ftv.loc[s, "human_class"].startswith("OUT"):
        outcome[s] = ftv.loc[s, "human_class"].split(":")[1] + " (gate)"
    elif s in PROVENANCE_E4:
        outcome[s] = "E4 (provenance)"
    elif rub.loc[s, "human_total"] < 5:
        outcome[s] = "quality below 5/8"
    else:
        outcome[s] = "included"
oc = pd.Series(outcome)
out["fulltext_outcomes"] = oc.value_counts().to_dict()
included = sorted(oc[oc == "included"].index)
out["included"] = included

g = ftv.loc[[s for s in assessed if s not in DOC_GATE]]
auto = g[~g.ft_suggested.str.startswith("HUMAN_REVIEW")]
agree = auto.ft_suggested.replace({"AUTO_OUT_FT:E7": "OUT:E7", "BC_PENDING_E4": "OUT:E4"}) == auto.human_class
out["eligibility_gate"] = dict(reports=len(g), machine_suggested=len(auto), agreed=int(agree.sum()),
                               overrides=auto[~agree].index.tolist(),
                               routed_to_human=int(g.ft_suggested.str.startswith("HUMAN_REVIEW").sum()))

# ---------------------------------------------------------------- rubric (verified)
cols = dict(R="human_rigour_score", E="human_evaluation_score",
            CR="human_context_realism_score", S="human_safety_score")
sc = rub.loc[included, list(cols.values())].rename(columns={v: k for k, v in cols.items()}).astype(int)
for (s, c), v in {("S0093", "S"): 1, ("S0577", "CR"): 1}.items():
    sc.loc[s, c] = v
sc["total"] = sc.sum(axis=1)
out["rubric_included"] = sc.to_dict(orient="index")
out["rubric_totals"] = sc.total.value_counts().sort_index().to_dict()
out["rubric_means"] = sc[["R", "E", "CR", "S"]].mean().round(2).to_dict()
scored = [s for s in assessed if outcome.get(s) in ("included", "quality below 5/8")]
draft = dict(R="rigour_score", E="evaluation_score", CR="context_realism_score", S="safety_score")
out["draft_agreement"] = dict(
    candidates=len(scored),
    totals_equal=int((rub.loc[scored, "draft_total"] == rub.loc[scored, "human_total"]).sum()))

# ---------------------------------------------------------------- screening sensitivity
st1 = {s: t.loc[s, "stage1_class"] for s in included}
out["included_stage1_class"] = st1
out["included_missed_by_stage1"] = [s for s, c in st1.items() if c == "OUT"]
k_inc = sum(1 for s in rnd[rnd.human_should_be != "correct_OUT"].stage_id if s in included)
lo, hi = cp_interval(k_inc, len(rnd))
out["residual_estimate"] = dict(stage1_exclusions=n_out, random_sample_includes=k_inc,
                                est_includable=n_out * k_inc / len(rnd),
                                ci95=[n_out * lo, n_out * hi])

print(json.dumps(out, indent=1, default=str))
with open("counts.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
