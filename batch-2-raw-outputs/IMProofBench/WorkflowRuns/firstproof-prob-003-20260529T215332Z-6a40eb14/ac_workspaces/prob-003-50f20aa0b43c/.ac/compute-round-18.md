# Compute worker reply — round 18
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/compute
zip: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/agents/Compute-c2-862dd2/compute_workspace_round_18.zip

---

# Round 18 response: complement inequality \(\Phi_q(w)\le q\)

I did not find a full proof for all \(q\ge 2/3\).  I did find one clean proof that should be added to `answer.tex`, plus a useful bootstrapping lemma and several diagnostics showing which natural auxiliary lemmas are too weak or circular.

## 1. Rigorous endpoint proof at \(q=2/3\)

This is short and self-contained.

Let
\[
  \mathcal H=\{A\subseteq[n]:w(A)>2/3\}.
\]
Then \(\mathcal H\) is 3-wise intersecting: if \(A,B,C\in\mathcal H\) had empty triple intersection, every coordinate would be counted in at most two of \(w(A)+w(B)+w(C)\), so
\[
  w(A)+w(B)+w(C)\le 2,
\]
contradicting \(w(A)+w(B)+w(C)>2\).

Now couple three \(\mu_{2/3}\)-random sets \(A_1,A_2,A_3\) by, independently for each coordinate, choosing uniformly one of the three sets to omit and putting the coordinate in the other two.  Each \(A_j\) has law \(\mu_{2/3}\), and \(A_1\cap A_2\cap A_3=\varnothing\).  Hence the events \(E_j=\{A_j\in\mathcal H\}\) cannot all occur.  Since the \(E_j\)'s have the same probability \(\Phi_{2/3}(w)\),
\[
  3\Phi_{2/3}(w)=\mathbb E\sum_{j=1}^3{\bf1}_{E_j}\le 2.
\]
Thus \(\Phi_{2/3}(w)\le2/3\).

## 2. A useful bootstrap lemma, but it does not close the interval

For integer \(m\ge2\), suppose \(q\ge (m-1)/m\), and put
\[
  \alpha=mq-(m-1).
\]
Couple \(m\) random sets \(A_1,\dots,A_m\) as follows.  For each coordinate, put it in all \(m\) sets with probability \(\alpha\); otherwise, choose one \(j\) and omit it from \(A_j\), with probability \(p=1-q\) for each \(j\).  Then each \(A_j\sim\mu_q\), and the common core \(C=\bigcap_j A_j\) has law \(\mu_\alpha\).

If \(w(A_j)>q\) for every \(j\), then
\[
  \sum_{j=1}^m w(A_j)>mq.
\]
Coordinates outside \(C\) are counted at most \(m-1\) times, while coordinates in \(C\) are counted \(m\) times, so
\[
  \sum_{j=1}^m w(A_j)\le (m-1)+w(C).
\]
Thus \(w(C)>\alpha\).  Therefore
\[
  m\Phi_q(w)-(m-1)\le \Pr(E_1\cap\cdots\cap E_m)\le \Phi_\alpha(w).
\]
Consequently, if the complement inequality is known at \(\alpha\), then
\[
  \Phi_q(w)\le {m-1+\alpha\over m}=q.
\]

Taking \(\alpha=2/3\) proves the isolated values \(q=1-\frac1{3m}\).  This is a nice partial theorem, but it does not handle \(q\in(2/3,5/6)\), since the corresponding \(\alpha\) values are below \(2/3\), where the analogous upper-tail-at-mean bound is false in general.

## 3. Literature search status

No theorem found directly implies \(\Phi_q(w)\le q\) for all \(q\ge2/3\).

Closest probability framework: Fokkink--Meester--Pelekis, *Optimizing stakes in simultaneous bets*, ALEA 20 (2023), 153--165, DOI `10.30757/ALEA.v20-07`, PDF `https://alea.impa.br/articles/v20/20-07.pdf`.  They define
\[
  \pi(p,t)=\sup_\gamma \Pr\!\left(\sum_i c_i\beta_i\ge t\right)
\]
over convex combinations of iid Bernoulli\((p)\)'s.  Our desired statement would follow from \(\pi(q,t)\le q\) for all \(q\ge2/3\) and all strict attainable \(t>q\).  Their proved rectangles leave exactly the near-hypotenuse strip \(q<t\le (k+1)/(k+2)\), \(k/(k+1)<q<(k+1)/(k+2)\), that we need.

Closest intersecting-family endpoint theorem: Frankl--Tokushige, *Weighted multiply intersecting families*, Studia Sci. Math. Hungar. 40 (2003), 287--291, DOI `10.1556/sscmath.40.2003.3.2`, gives \(\mu_p(\mathcal F)\le p\) for arbitrary \(r\)-wise intersecting families when \(p\le(r-1)/r\).  This proves/explains the endpoint \(q=2/3\) for 3-wise intersecting families, but arbitrary 3-wise families are too large for \(q>2/3\).

Tokushige, *Application of hypergraph Hoffman's bound to intersecting families*, Algebraic Combinatorics 5 (2022), 537--557, `https://www.numdam.org/item/ALCO_2022__5_3_537_0.pdf`, extends biased-measure results, including a nonuniform 3-wise theorem under \(p_2<2/3\).  It does not cover the uniform \(q>2/3\) regime.

Tokushige, *The maximum measure of 3-wise \(t\)-intersecting families*, EJC 110 (2023), arXiv `2112.08685`, records the broader 3-wise \(t\)-intersecting landscape.  For \(t=1\), plain 3-wise intersection alone cannot prove the desired \(q>2/3\) strip.

Kellerer/Samuels/Feige searches again found adjacent but not directly usable results.  Paulin `arXiv:1703.05152` records Samuels/Feige implications for sums of arbitrary nonnegative variables above shifted means; it does not yield the exact Bernoulli convex-combination mean-threshold inequality.

## 4. Computation and auxiliary-lemma diagnostics

Artifacts:

- `code/round18_complement_experiments.py`
- `code/round18_threshold_lp.py`
- `code/round18_capped_residual.py`
- `data/round18/complement_experiments.json`
- `data/round18/threshold_lp_n5.json`
- `data/round18/capped_residual_fast.json`

Main checks:

1. Random search plus differential evolution over \(2\le n\le8\) and representative \(q\)'s found no violation.  The optimized maximum of \(\Phi_q(w)-q\) was \(1.1\cdot10^{-16}\), always dictatorship/star-type.

2. Exact LP enumeration of all threshold up-families for \(n\le5\), at
\[
q\in\{2/3,.67,.68,.70,.72,.75,.80,.85,.90\},
\]
found the best representable family is always a star.  Maximum \(\mu_q(U)-q\) was numerical zero.  Feasible threshold up-family counts were:

| \(n\) | feasible count range over checked \(q\)'s | best \(\mu_q(U)-q\) |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 3 | 0 |
| 3 | 10 | \(1.1\cdot10^{-16}\) |
| 4 | 53 | 0 |
| 5 | 596--646 | 0 |

3. The range is sharp from below.  At \(q=0.65\), weights \((0.33,0.335,0.335)\) give
\[
\Phi_{0.65}=\Pr[\mathrm{Bin}(3,0.65)\ge2]=0.71825>0.65.
\]

4. A naive threshold-flow lemma saying the between-breakpoint derivative is always \(\le1\) is false.  Example:
\[
q=0.95,\quad
w=(0.85975408,0.04872226,0.03662089,0.03655690,0.01834587).
\]
Here \(\Phi_q(w)=0.9366821875<q\), but between subset-sum breakpoints
\[
  {d\over dq}\Phi_q(w)=1.50040625.
\]
The next breakpoint is only \(0.00127774\) away, so the function still does not cross \(q\).  A flow proof must account for jump locations/sizes, not only derivative sign.

5. Largest-weight induction is not false, but it is essentially the same missing theorem.  Conditioning on a largest coordinate of weight \(a\) gives the needed residual inequality
\[
  p\Pr[R>q]\le q\Pr[R\le q-a].
\]
With \(Y=R-q(1-a)\), this is exactly
\[
  q\Pr[Y\le -pa]\ge p\Pr[Y>qa],
\]
the CTC/HUG inequality at scale \(h=a\) for the residual increments.  The subcritical shifted-HUG proposition proves this only when \(a\ge p\), where the residual right tail is already empty/trivial.  The real case \(a<p\) is the original missing case.

6. Pivot-plus-dust examples show this residual inequality is sharp.  For \(w_0=p-\varepsilon\) and \(N\) equal dust weights \((q+\varepsilon)/N\), \(\Phi_q(w)\to q\).  Numerics:

| \(q\) | \(\varepsilon\) | \(N\) dust | \(\Phi_q-q\) | residual slack |
|---:|---:|---:|---:|---:|
| \(2/3\) | \(0.003333\) | 500 | \(-1.5\cdot10^{-14}\) | \(1.5\cdot10^{-14}\) |
| 0.70 | 0.003 | 500 | \(-6.6\cdot10^{-10}\) | \(6.6\cdot10^{-10}\) |
| 0.75 | 0.0025 | 500 | \(-1.2\cdot10^{-5}\) | \(1.2\cdot10^{-5}\) |
| 0.90 | 0.001 | 10000 | \(-1.44\cdot10^{-4}\) | \(1.44\cdot10^{-4}\) |

## 5. Recommended next edit to `answer.tex`

Add the endpoint \(q=2/3\) proposition and the \(m\)-set bootstrap lemma as rigorous partial progress.  Then explicitly state that FMP/Csóka would imply the full result but current published FMP regions do not cover the strict near-hypotenuse strip.  Also add a warning that the largest-weight residual induction is equivalent to HUG/CTC in the nontrivial capped case, and that a derivative-only threshold-flow lemma is false by the example above.
