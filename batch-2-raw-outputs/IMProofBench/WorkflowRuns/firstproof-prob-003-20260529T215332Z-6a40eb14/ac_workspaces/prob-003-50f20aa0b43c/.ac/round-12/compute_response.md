# Round 12 compute report: rational cyclic expectation inequality

I read the current `answer.tex` and `research_notes.tex`.  I did not find a
published theorem that directly proves the remaining assertion.  I did find
that the requested cyclic inequality is exactly the same finite weighted
Bernoulli lower-tail inequality, so any proof of one is a proof of the other:
for fixed \(j\), the indicators that item \(i\) falls in \([j,j+r)\) are iid
\(\mathrm{Bernoulli}(r/b)\).  Thus
\[
 \frac1b\mathbb E\#\{j:L_j<r/b\}
 =\Pr\Big[\sum_i w_i X_i<r/b\Big],
\]
and the cyclic claim is equivalent to
\[
\Pr\Big[\sum_i w_iX_i<p\Big]\le 1-p,\qquad p=r/b\le 1/3.
\]

## Literature search

Detailed notes are in `notes/round12_literature.md`.  Closest hits:

- Fokkink--Meester--Pelekis, *Optimizing stakes in simultaneous bets*, ALEA 20
  (2023), 153--165, DOI `10.30757/ALEA.v20-07`; local files
  `papers/fokkink-meester-pelekis-2023.txt` and
  `papers/fokkink_meester_pelekis_optimizing_stakes_2023.pdf`.  This is the
  closest match.  In complement form our target is
  \[
   \Pr\Big[\sum_i w_i\eta_i>q\Big]\le q,\qquad q=1-p\ge2/3,
  \]
  i.e. the strict hypotenuse \(t\downarrow q\) for their \(\pi(q,t)\).  Their
  Theorem 4.4 proves rectangles above the hypotenuse, and Proposition 4.5 proves
  some boundary points \(q=t=(k+1)/(k+2)\), but it does not cover the
  near-hypotenuse strip \(q<t<(k+1)/(k+2)\).
- Kellerer, *Zur Existenz analoger Bereiche*, Z. Wahrscheinlichkeitstheorie 1
  (1963), 240--246, DOI `10.1007/BF00532495`, and Kellerer,
  *Linearkombinationen zufälliger Größen und ihre gemeinsame Verteilung*, Math.
  Z. 84 (1964), 403--414.  These are relevant to analogous regions and linear
  combinations, but I found no theorem implying the discrete Bernoulli halfspace
  bound.
- Filmus, *The weighted complete intersection theorem*, JCTA 151 (2017), 84--101,
  is relevant to biased-measure extremal families, but it treats intersecting
  families, not the special weighted-threshold family needed here.
- FMP quote the Chaundy--Bullard/Jogdeo--Samuels binomial-tail monotonicity:
  \(P(\mathrm{Bin}(ka,1/a)\ge k)\) is maximal at \(k=1\).  This supports
  reciprocal boundary points under Csóka/stability assumptions, but FMP explicitly
  say the natural generalization appears unknown.

Bottom line: I found adjacent literature, not an exact black-box theorem.

## Computations

Code and output:

- `code/round12_cyclic_expectation.py`
- `data/round12/round12_results.json`
- `data/round12/round12_summary.md`
- `data/round12/strict_capped_n7_n8.json`

The MILP maximizes the \(p\)-biased mass of subsets forced to satisfy
\(w(A)\le p-\varepsilon\).  With \(\varepsilon=0\), it is a closed-tail upper
relaxation for the strict problem.  For \(p=2/7,3/10,4/13\), the closed
relaxation for all supports \(n\le6\) has optimum exactly \(1-p\), attained only
by trivial boundary/one-big-atom configurations returned by the solver.

For the capped nontrivial search \(w_i\le p-10^{-5}\), the \(n\le7\) MILP
optimum is the same four-effective-block chamber:
three weights just below \(p\), plus a residual block near \(1-3p\) (zeros or
splittings of the residual do not change the event).  The light event is
essentially “at most one effective block succeeds,” with mass
\[
 q^4+4pq^3,\qquad q=1-p.
\]

| \(p\) | target \(q\) | capped MILP max, \(n\le7\) | gap \(q-\max\) | expected gap |
|---:|---:|---:|---:|---:|
| \(2/7\) | \(5/7\) | \(1625/2401=0.6768013328\) | \(90/2401\) | \(90/343\) |
| \(3/10\) | \(7/10\) | \(6517/10000=0.6517\) | \(483/10000\) | \(483/1000\) |
| \(4/13\) | \(9/13\) | \(18225/28561=0.6381079094\) | \(1548/28561\) | \(1548/2197\) |

The \(n=8\) capped MILPs hit the same incumbent values but timed out before
formal solver optimality; see `data/round12/strict_capped_n7_n8.json`.

Exact grid enumeration over positive weights summing to 1 gave:

- without cap, the grid maximum is \(1-p\), attained by the one-atom vector
  `[1]`;
- with strict cap \(w_i<p\):
  - \(p=2/7\), denominator 14: max \(9375/16807\), weights
    \([1/7,3/14,3/14,3/14,3/14]\);
  - \(p=3/10\), denominator 20: max \(6517/10000\), weights
    \([1/4,1/4,1/4,1/4]\);
  - \(p=4/13\), denominator 26: max \(18225/28561\), weights
    \([5/26,7/26,7/26,7/26]\).

Direct cyclic allocation enumeration checks matched \(b\Pr(S<p)\).  Examples:

| \(b,r\) | weights | \(\mathbb E\#\) light | target |
|---:|---|---:|---:|
| \(7,2\) | seven \(1/7\)'s | \(296875/117649\approx2.524\) | 5 |
| \(10,3\) | four \(1/4\)'s | \(6517/1000=6.517\) | 7 |
| \(13,4\) | four \(1/4\)'s | \(18225/2197\approx8.296\) | 9 |

## FMP cyclic/injection adaptation

The FMP argument represents Bernoulli variables by uniform cyclic placements and
then proves a pointwise bound on the number \(J(\omega)\) of intervals reaching
threshold in certain parameter rectangles.  For our short-interval lower-tail
version, that pointwise bound is false in exactly the way the draft notes.

I reproduced pointwise deterministic excess examples by LP:

- \(b=7,r=2\): 6 light intervals, target 5;
- \(b=10,r=3\): 8 light intervals, target 7;
- \(b=13,r=4\): 10 light intervals, target 9.

These are in `data/round12/round12_summary.md`.  The excess examples form
positive-dimensional load cones, not just the all-loads-equal exceptional case
handled in FMP Proposition 4.5.  Therefore an FMP-style proof cannot be a simple
pointwise injection from excess \(J=b-r+1\) configurations to deficit
configurations by moving the last one or two weights; it would need a genuine
averaged discharging over pairs \((\omega,j)\).

The promising intermediate lemma suggested by the computations is:

> For fixed small support and all weights \(<p\), the extremal chamber is the
> four-block chamber with light mass \(q^4+4pq^3\).  Larger-support near-equality
> should then come only from the pivot-plus-dust mechanism already described in
> the notes.

I do not yet have a proof turning this dichotomy into the full inequality.
The most precise obstruction is that the expected inequality must use the
random allocation/product-measure structure; deterministic cyclic interval
counts and FMP's existing pointwise interval bound both fail in the
near-hypotenuse region.
