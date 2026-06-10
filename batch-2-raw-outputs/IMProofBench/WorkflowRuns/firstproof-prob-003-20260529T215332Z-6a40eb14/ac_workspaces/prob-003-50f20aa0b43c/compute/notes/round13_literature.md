# Round 13 Literature Notes

No directly applicable theorem was found for
\[
  \Pr\!\left[\sum_i w_i v_i\ge p\right]\ge p,\qquad 0<p\le 1/3,
\]
or for the centered HUG form
\[
  q\Pr(X\ge p)\ge p\Pr(X<-q),\qquad
  X=\sum_i b_i(\zeta_i-p),\quad 0\le b_i\le 1.
\]

## Closest results checked

1. Fokkink--Meester--Pelekis, *Optimizing stakes in simultaneous bets*,
   ALEA 20 (2023), 153--165, DOI `10.30757/ALEA.v20-07`.
   Local files: `papers/fokkink_meester_pelekis_optimizing_stakes_2023.pdf`,
   `data/round13/fmp.txt`.
   They define
   \[
     \pi(p,t)=\sup_\gamma\Pr(S_\gamma\ge t),
   \]
   over convex combinations of iid Bernoulli(p)'s.  In complement notation
   the desired theorem is the strict near-hypotenuse assertion
   \[
     \pi(q,t)\le q\qquad(q\ge 2/3,\ t>q).
   \]
   Theorem 4.4 proves bold play only when
   \[
     {k\over k+1}<p\le {k+1\over k+2}<t.
   \]
   Proposition 4.5 handles diagonal endpoints
   \(p=t=(k+1)/(k+2)\) for \(k>1\), but the strict strip
   \(q<t\le (k+1)/(k+2)\) with \(q\) inside the interval is not covered.
   Their text explicitly says the array of triangles along the hypotenuse
   remains open.

2. H. G. Kellerer, *Linearkombinationen zufälliger Größen und ihre gemeinsame
   Verteilung*, Math. Z. 84 (1964), 403--414.
   I pulled OCR from the GDZ page annotations into
   `data/round13/kellerer_1964_ocr.txt`.  Satz 1 is an existence criterion for
   prescribed one-dimensional distributions of linear forms: arbitrary
   prescribed distributions for \(t\cdot X\), \(t\in T\), can be realized iff
   the vectors in \(T\) are linearly independent.  Satz 2--6 are uniqueness
   theorems for recovering a joint distribution from linear projections under
   algebraic/transcendence hypotheses.  This is not a Bernoulli tail or
   halfspace-measure inequality.

3. Kellerer, *Zur Existenz analoger Bereiche*, Z. Wahrscheinlichkeitstheorie 1
   (1963), 240--246, DOI `10.1007/BF00532495`.
   Local OCR: `papers/kellerer-analogous-areas.txt`.
   This gives analogous/equal-measure regions for finite families of atomless
   measures, with Satz 4 giving analogous regions of the form `{a in G}`.
   It does not apply as a black box to finite discrete cube down-sets.

4. Pinelis, *Optimal binomial, Poisson, and normal left-tail domination for
   sums of nonnegative random variables*, EJP 21 (2016), arXiv:1503.06482.
   Local file: `data/round13/pinelis_left_tail.txt`.
   Theorem 2.4 gives sharp domination of \(E f(S_n)\) for nonnegative sums
   under first/second moment constraints and \(f\) in decreasing generalized
   moment classes; Corollary 2.7 gives left-tail upper bounds.  These are
   moment-constraint bounds and do not compare the two HUG tails with the exact
   factor \(p/q\).  They are too weak in the pivot-plus-dust equality regime.

5. Christopher R. Dance, *An inequality for the sum of independent bounded
   random variables*, J. Theoret. Probab. 27 (2014), 358--369,
   DOI `10.1007/s10959-012-0460-1`, arXiv:1210.6484.
   Downloaded as `papers/round13/dance-2014-bounded-sum.pdf`; text at
   `data/round13/dance.txt`.
   Theorem 1: if \(S=\sum_{i=1}^n X_i\), \(0\le X_i\le1\) independent, and
   \(ES=\lambda\), then
   \[
   \Pr(S\le1)\le
   \max\left\{(1+\lambda-\lambda/n)(1-\lambda/n)^{n-1},
   \left(1-\frac{\lambda-1}{n-1}\right)(1-\lambda/n)^{n-1}\right\}.
   \]
   After scaling a capped Bernoulli sum to mean \(\lambda=1\), this gives an
   upper bound tending to \(2/e\approx0.736\), not enough for the target
   \(q=2/3\) near \(p=1/3\); moreover the theorem allows arbitrary bounded
   variables, a much larger class.

6. Paulin, *On some conjectures of Samuels and Feige*, arXiv:1703.05152.
   Local file: `data/round13/samuels_feige.txt`.
   The paper records Feige's and Samuels' conjectures for
   \(Z=\sum_i\mu_i X_i\), \(EX_i=1\), and thresholds \(T=1+\delta\), and proves
   Samuels implies Feige.  The problem is above-mean small deviation for
   arbitrary nonnegative variables, not the exact mean-threshold Bernoulli
   halfspace bound.

7. Filmus, *The weighted complete intersection theorem*, JCTA 151 (2017),
   84--101, DOI `10.1016/j.jcta.2017.04.008`.
   Gives the maximum \(\mu_p\)-measure of \(t\)-intersecting families.  It is
   pairwise \(t\)-intersection, not the 3-wise threshold structure here.

8. Tokushige, *The maximum measure of 3-wise t-intersecting families*, EJC 110
   (2023), 103703, DOI `10.1016/j.ejc.2023.103703`.
   The paper records that for 3-wise 1-intersecting families the arbitrary
   family bound is \(\mu_p(\mathcal F)\le p\) only for \(p\le2/3\), while for
   \(p>2/3\) examples have measure tending to 1.  Thus the complement family's
   plain 3-wise intersection property is insufficient at \(q\ge2/3\); a proof
   must use weighted-threshold/quota structure.

