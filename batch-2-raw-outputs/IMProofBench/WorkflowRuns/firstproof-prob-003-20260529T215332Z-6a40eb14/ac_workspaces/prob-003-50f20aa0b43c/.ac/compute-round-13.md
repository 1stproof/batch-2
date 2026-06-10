# Compute worker reply — round 13
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/compute
zip: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/agents/Compute-c2-890d22/compute_workspace_round_13.zip

---

# Round 13 compute report

I read the current `answer.tex` and `research_notes.tex`.  I did not find a published theorem that directly proves the missing interval \(0<p\le 1/3\).  The closest exact formulation remains the Fokkink--Meester--Pelekis convex-combination Bernoulli tail problem, but their proved region still leaves the strict near-hypotenuse strip needed here.

New files from this round:

- `notes/round13_literature.md` -- theorem statements and literature conclusions.
- `data/round13/kellerer_1964_ocr.txt` -- OCR pulled from the GDZ page annotations for Kellerer 1964.
- `papers/round13/dance-2014-bounded-sum.pdf`, `data/round13/dance.txt` -- Dance's bounded-sum inequality.
- `code/round13_exposure.py`
- `data/round13/round13_exposure.json`
- `data/round13/round13_exposure_summary.md`

## Literature conclusions

### Fokkink--Meester--Pelekis is exactly adjacent, but not enough

Fokkink--Meester--Pelekis, *Optimizing stakes in simultaneous bets*, ALEA 20 (2023), 153--165, DOI `10.30757/ALEA.v20-07`, define
\[
  \pi(p,t)=\sup_\gamma \Pr(S_\gamma\ge t),
\]
where \(S_\gamma\) is a convex combination of iid Bernoulli(\(p\)) variables.  In complement notation the missing theorem is
\[
  \pi(q,t)\le q\qquad(q\ge 2/3,\ t>q). \tag{FMP-strip}
\]
Their Theorem 4.4 proves bold-play optimality when
\[
  {k\over k+1}<p\le {k+1\over k+2}<t,
\]
and Proposition 4.5 proves diagonal endpoints \(p=t=(k+1)/(k+2)\) for \(k>1\).  This leaves exactly
\[
  q<t\le {k+1\over k+2},\qquad {k\over k+1}<q<{k+1\over k+2},
\]
which is the near-hypotenuse strip needed here.  They explicitly state that an array of triangles along the hypotenuse remains open.

If (FMP-strip) were available, it would prove the missing interval immediately: for a fixed finite weight vector,
\[
\Pr_q\!\left[\sum_i w_i\eta_i>q\right]
= \Pr_q\!\left[\sum_i w_i\eta_i\ge t_w\right],
\]
where \(t_w\) is the smallest subset sum strictly larger than \(q\); then \(t_w>q\), so (FMP-strip) gives the desired upper bound \(\le q\).

### Kellerer does not supply the missing theorem

I pulled OCR for Kellerer, *Linearkombinationen zufälliger Größen und ihre gemeinsame Verteilung*, Math. Z. 84 (1964), 403--414, into `data/round13/kellerer_1964_ocr.txt`.  Satz 1 is an existence criterion for prescribed one-dimensional distributions of linear forms: arbitrary distributions for \(t\cdot X\), \(t\in T\), can be realized iff the vectors in \(T\) are linearly independent.  Satz 2--6 are uniqueness/recovery theorems for joint distributions from linear projections under algebraic/transcendence hypotheses.  I found no Bernoulli tail, halfspace-measure, or convex-combination inequality.

Kellerer, *Zur Existenz analoger Bereiche*, DOI `10.1007/BF00532495`, remains only conceptually related: it is an atomless analogous-region theorem.  It does not apply as a black box to finite cube down-sets.

### Other adjacent theorems are too weak or structurally mismatched

- Pinelis, *Optimal binomial, Poisson, and normal left-tail domination...*, arXiv:1503.06482: Theorem 2.4 and Corollary 2.7 give sharp left-tail domination from first/second moments for nonnegative sums and decreasing generalized moment functions.  They do not compare the two HUG tails with exact factor \(p/q\), and moment-only information is too weak near pivot-plus-dust equality.
- Dance, *An inequality for the sum of independent bounded random variables*, JTP 27 (2014), DOI `10.1007/s10959-012-0460-1`: Theorem 1 bounds \(\Pr(S\le1)\) for arbitrary independent \(0\le X_i\le1\), \(ES=\lambda\).  Scaling a capped Bernoulli sum to \(\lambda=1\) gives a bound tending to \(2/e\approx0.736\), not enough for \(q=2/3\).
- Paulin/Samuels/Feige concerns \(T=1+\delta\) above-mean small deviations for arbitrary nonnegative variables, not the exact mean-threshold Bernoulli halfspace problem.
- Filmus weighted complete intersection is for pairwise \(t\)-intersecting families.  Tokushige's 3-wise measure results show that arbitrary 3-wise 1-intersecting families are controlled only up to bias \(2/3\); for \(q>2/3\) such families can have measure tending to 1.  Thus the weighted-threshold/quota structure is essential.

## Exposure identity investigation

For any deterministic ordering,
\[
\Pr(S_m<p)=1-pH,\qquad
H:=\sum_i \Pr(p-w_i\le S_{i-1}<p). \tag{E}
\]
The missing theorem is exactly \(H\ge1\).

I computed exact exposure profiles in `code/round13_exposure.py`.  Representative outputs:

| \(p\) | weights | \(\Pr(S<p)\) | \(H\) | exposure contributions |
|---:|---|---:|---:|---|
| \(3/10\) | \(1/4,1/4,1/4,1/4\) | \(6517/10000=0.6517\) | \(1161/1000=1.161\) | \(0,\ .3,\ .42,\ .441\) |
| \(2/7\) | \(1/7,3/14,3/14,3/14,3/14\) | \(9375/16807\) | \(3716/2401=1.5477\) | \(0,\ .2857,\ .4082,\ .4373,\ .4165\) |
| \(4/13\) | \(5/26,7/26,7/26,7/26\) | \(18225/28561\) | \(2584/2197=1.1761\) | \(0,\ .3077,\ .4260,\ .4424\) |
| \(3/10\) | pivot \(29/100\) plus 60 dusts \(71/6000\) | \(\approx0.686298\) | \(\approx1.045673\) | many small terms after the pivot |

The pivot-plus-dust example is the sharpness warning in exposure language: \(H\) can be very close to 1 while the pathwise opportunity count has a large atom at 0.  For the displayed 60-dust example, the predictable opportunity-count distribution has
\[
\Pr(O=0)\approx0.67949,\qquad E O=H\approx1.04567.
\]
So no pathwise statement like “every path has an opportunity” can work.

Two stronger local discharging lemmas fail:

1. Termwise \(h_i\ge w_i\) in decreasing order fails at \(p=1/3\), weights \((3/10,3/10,2/5)\): the first contribution is \(0<3/10\).
2. Prefix contribution dominates prefix weight once the deterministic prefix reaches \(p\) fails for \(p=3/10\), weights \((1/4)^4\): after two weights, contribution is \(3/10<1/2\).

Thus a proof of (E) cannot be a simple itemwise or prefixwise charging argument.

## Most promising proof target

The cleanest remaining target is the strict FMP-strip theorem:

> For every \(q\ge2/3\), every convex combination \(S=\sum_i w_i\eta_i\) of iid Bernoulli(\(q\)) variables, and every \(t>q\), one has \(\Pr(S\ge t)\le q\).

This is exactly the missing theorem in complement form, but it matches an existing literature framework and a cyclic-allocation method.  A proof should likely be an averaged discharging over random cyclic placements, not a pointwise interval-count proof; previous deterministic interval counts fail.

For a Bellman/local-time route, the right state seems to be the pair \((\text{current sum},\text{predictable crossing local time})\), not just the current sum or remaining variance.  The scalar Bellman recurrence from earlier rounds,
\[
W_R(x)=\inf_b\{qW_{R-b}(x+pb)+pW_{R-b}(x-qb)\},
\]
has a rigorous barrier only in the subcritical region \(R\le q/p\).  The exposure computations show why: in the hard region, the proof must compensate a large probability of zero opportunities by a long tail of missed opportunities.  That compensation is invisible to a purely pointwise barrier.

I did not find a complete proof, but the next concrete lemma to try is:

> In the FMP cyclic model for \(q=a/b\ge2/3\), the expected number of heavy intervals of length \(a\) is at most \(a\), even though fixed load vectors can have \(a+1\) or more heavy intervals.

This is precisely the averaged statement that would prove the rational strict complement inequality.

