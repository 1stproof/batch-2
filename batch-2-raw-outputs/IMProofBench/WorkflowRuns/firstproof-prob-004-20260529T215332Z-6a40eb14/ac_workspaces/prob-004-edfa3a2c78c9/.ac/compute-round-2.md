# Compute worker reply — round 2
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c1-6ad149/compute_workspace_round_2.zip

---

# Round 2 compute report: verification of the Guth-map counterexample

I could not read `/mnt/data/answer.tex` because `/mnt/data` is not mounted in this worker. I read the synced canonical copy at `problem_documents_readonly/answer.tex`.

## Files produced

- `notes/guth_ch8_2_round2_excerpts.md`: compact page references and quote snippets from Guth thesis Chapter 8.2.
- `code/check_round2_counterexample.py`: exact exponent/ratiocheck script.
- `data/round2_counterexample_check.txt`: output of that script.
- Page extracts already present/confirmed:
  - `data/pages/guth_area_contracting_thesis_2005/page_144.txt`
  - `data/pages/guth_area_contracting_thesis_2005/page_146.txt`
  - `data/pages/guth_area_contracting_thesis_2005/page_147.txt`
  - `data/page_images/thesis_page_146.pdf`
  - `data/page_images/thesis_page_147.pdf`
  - `data/page_images/thesis_page_148.pdf`

## Verdict

The counterexample in the current `answer.tex` is valid at the asymptotic level, assuming the intended convention that Guth's strict hypotheses may be replaced by non-strict hypotheses after fixed/small perturbations and universal-constant changes.

There is no substantive scaling error in the sequence
\[
(L^{-7},1,L,L)\to(L^{-6},L^{-3},L,L)
\to(L^{-13/2},L^{-13/2},L^{-13/2},L^{12})
\to(L^{-13/2},L^{-13/2},1,L^{11/2}).
\]

The only caveat is formal: Guth writes strict inequalities. The written sequence uses equality in two places:

1. In the pinching step,
\[
a^2b=L^{-13}L^{12}=L^{-1}=R_2R_3R_4.
\]
Guth's pinching map requires \(R_2R_3R_4>A^2B\).

2. In the final interpolated short-side/stretch-split step with parameter \(A=1\),
\[
A^4=1=R_2/R_1.
\]
Guth's technical remark writes \(A^4<R_2/R_1\).

These are harmless if the draft explicitly permits perturbing side lengths and constants. If the final proof wants literal strict compliance with the thesis statements, use the strict perturbation below.

## Exact Guth thesis references

Source: Lawrence Guth, *Area-contracting maps between rectangles*, MIT Ph.D. thesis, 2005. Local PDF: `papers/guth_area_contracting_thesis_2005.pdf`. MIT handle recorded in `data/guth_thesis_handle.html`: `http://hdl.handle.net/1721.1/31158`.

Chapter 8.2 starts on thesis p.144. The opening paragraph says the five maps in this section take boundary to boundary, have degree 1, and have \(2\)-dilation \(<C\). This directly supports the degree-one map-of-pairs use in `answer.tex`.

On thesis p.146, "A map that stretches the short side of the domain" takes
\[
R_1\times R_2\times R_3\times R_4
\to
AR_1\times A^{-3}R_2\times AR_3\times A^{-1}R_4,
\]
for \(A\ge 1\), \(A<(R_2/R_1)^{1/4}\), and \(A<(R_4/R_3)^{1/2}\).

The technical remark on the same page is the part used in `answer.tex`: taking instead a quasi-isometric embedding of
\[
A^{-2}R_2\times AR_3\times AR_4
\]
into \(R_2\times R_3\times R_4\) gives a map
\[
R\to AR_1\times A^{-3}R_2\times R_3\times R_4.
\]
It also says interpolation gives a map to
\[
AR_1\times A^{-3}R_2\times A\times B
\]
when \(A^4<R_2/R_1\), \(R_3<A<(R_3R_4)^{1/2}\), and \(R_3R_4=AB\).

On thesis p.147, "Pinching Map" takes
\[
R_1\times R_2\times R_3\times R_4\to A\times A\times A\times B
\]
provided \(R_1>A\) and \(R_2R_3R_4>A^2B\). Guth then explains that the pinch collapses the large-\(2\)-dilation region to a line, so the total \(2\)-dilation is \(<C\).

So Lemma 1 in `answer.tex` is a faithful consequence of these constructions, except that it should say explicitly that its weak inequalities are obtained by perturbation/absorbing constants. To reduce ambiguity, I would also say that item (1)'s first target \(AR_1\times A^{-3}R_2\times R_3\times R_4\) is from the technical remark, not from the displayed main "stretches the short side" map.

## Hypothesis check for the displayed sequence

Step 1:
\[
R^0=(L^{-7},1,L,L),\quad A=L.
\]
The technical-remark short-side map gives
\[
(L^{-7},1,L,L)\to(L^{-6},L^{-3},L,L)
\]
because
\[
A^4=L^4<L^7=R_2/R_1
\]
for \(L>1\).

Step 2:
\[
a=L^{-13/2},\quad b=L^{12}.
\]
The pinching map gives
\[
(L^{-6},L^{-3},L,L)\to
(L^{-13/2},L^{-13/2},L^{-13/2},L^{12})
\]
in the non-strict/perturbed sense, since
\[
a<L^{-6},\qquad a^2b=L^{-1}=L^{-3}LL=R_2R_3R_4.
\]

Step 3:
Apply the interpolated technical-remark map with \(A=1\):
\[
(L^{-13/2},L^{-13/2},L^{-13/2},L^{12})
\to
(L^{-13/2},L^{-13/2},1,L^{11/2}).
\]
The inequalities are
\[
R_3=L^{-13/2}<1,\qquad
1<(R_3R_4)^{1/2}=L^{11/4},
\]
and the only non-strict point is \(A^4=1=R_2/R_1\). Also
\[
B=R_3R_4/A=L^{-13/2}L^{12}=L^{11/2}.
\]

## Bad ratios after scaling

Let \(C_0\) be the bounded \(2\)-dilation constant for the composed map and set \(\lambda=C_0^{1/2}\). Scaling the domain to
\[
R=\lambda(L^{-7},1,L,L)
\]
gives \(\Dil_2\le 1\). For
\[
S=(L^{-13/2},L^{-13/2},1,L^{11/2}),
\]
the three ratios are
\[
\frac{R_1}{S_1}=\lambda L^{-1/2},
\]
\[
\frac{R_3R_4}{S_3S_4}
=\frac{\lambda^2L^2}{L^{11/2}}
=\lambda^2L^{-7/2},
\]
and
\[
\frac{\operatorname{Vol}(R)}
{S_1S_2^{1/2}S_3^{3/2}S_4}
=
\frac{\lambda^4L^{-5}}
{L^{-13/2}L^{-13/4}L^{11/2}}
=\lambda^4L^{-3/4}.
\]
All tend to zero. Hence for any proposed \(\kappa>0\), taking \(L\) large gives \(R_1<\kappa S_1\) while both proposed alternatives fail.

## Literal strict-inequality version

If the Author wants to avoid relying on closed-condition language, use fixed constants \(0<\alpha<1\), \(\mu>1\). After step 1, use pinching with
\[
a=\alpha L^{-13/2},\qquad b=L^{12}.
\]
Then
\[
a^2b=\alpha^2L^{-1}<L^{-1}=R_2R_3R_4.
\]
Insert the bounded linear map
\[
(a,a,a,L^{12})\to(a,\mu a,a,L^{12}/\mu),
\]
which has \(2\)-dilation at most \(\mu\). Now apply the final technical-remark map with \(A=1\). Its strict condition \(1<R_2/R_1\) holds because \(R_2/R_1=\mu\). The final target is
\[
S'=(\alpha L^{-13/2},\mu\alpha L^{-13/2},1,\alpha\mu^{-1}L^{11/2}).
\]
The bad ratios after the same fixed domain scaling are
\[
(\lambda/\alpha)L^{-1/2},\qquad
(\lambda^2\mu/\alpha)L^{-7/2},\qquad
\lambda^4\alpha^{-5/2}\mu^{1/2}L^{-3/4},
\]
so they still go to zero. For example \(\alpha=1/2,\mu=2\) gives a completely explicit strict version with only fixed constant changes.

## Suggested wording changes for final draft

1. In Lemma 1, add: "Guth states these with strict inequalities; throughout we use the corresponding weak form after replacing side lengths by fixed arbitrarily close perturbations and absorbing the resulting factors into the universal constant."

2. In item (1), clarify source: "The first displayed target is the first technical-remark variant on p.146; the second displayed target is the interpolated variant in the same remark."

3. In the counterexample proof, either keep the current sequence and explicitly invoke the weak-form convention, or replace it by the \((\alpha,\mu)\)-perturbed strict sequence above.
