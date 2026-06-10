# Grader 3 — Aggregate Report

**Run:** f204b6faaedc
**Proofs graded:** 2
**Verdicts:** PASS=0  REWRITE=1  UNVERIFIABLE=0  REWORK=1  UNKNOWN=0
**Acceptance threshold:** >=2 PASS
**Provisional acceptance:** NO — best-so-far written

## Per-proof verdicts

- **Stage 1 Solver 0** (score=3.0, bs_clean=None)
  - verdict: **REWRITE** (low)
  - reason: The proof has 2 SUPPORTS and 1 NOT FOUND verdict, with 1 unmatched step; total verified steps = 3, total steps = 4, coverage = 75%, meeting the threshold for a REWRITE.
  - n_unmatched: 1
  - findings: /data/output/prob-008_grader3/proof_stage1_solver0/verify/findings.md
  - feedback: /data/output/prob-008_grader3/proof_stage1_solver0/verify/feedback.md

- **Stage 1 Solver 3** (score=3.0, bs_clean=None)
  - verdict: **REWORK** (fatal)
  - reason: The proof contains a DOES NOT APPLY verdict in the verified set (3 verified steps, 2 unmatched), indicating a fundamental mismatch between the cited theorem's hypotheses and the proof's claim.
  - n_unmatched: 2
  - findings: /data/output/prob-008_grader3/proof_stage1_solver3/verify/findings.md
  - feedback: /data/output/prob-008_grader3/proof_stage1_solver3/verify/feedback.md
