# Round 14 literature notes

I did not find a theorem that directly proves either of the two requested
routes.

## Fokkink--Meester--Pelekis

Robbert Fokkink, Ludolf Meester, Christos Pelekis, *Optimizing stakes in
simultaneous bets*, ALEA 20 (2023), 153--165, DOI `10.30757/ALEA.v20-07`.

They define
\[
  \pi(p,t)=\sup_\gamma \Pr(S_\gamma\ge t)
\]
over convex combinations of iid Bernoulli(p)'s.  In the complement notation of
the present problem, the missing assertion would follow from
\[
  \pi(q,t)\le q,\qquad q\ge 2/3,\quad t>q.
\]

Their Theorem 4.4 proves bold-play optimality in the region
\[
  {k\over k+1}<p\le {k+1\over k+2}<t,
\]
and Proposition 4.5 proves the diagonal points
\[
  p=t={k+1\over k+2}\quad (k>1).
\]
They explicitly state that an array of triangles along the hypotenuse remains
open.  The desired strict strip \(q<t\le (k+1)/(k+2)\) with \(q\) inside the
same interval is exactly in this missing region.

Their Section 6 includes an unfavorable-odds theorem at threshold \(1/3\), but
it is of the form \(p\le 1/3\le t\) for the Bernoulli parameter \(p\).  This is
not the complement problem \(q\ge2/3\), \(t>q\).

## Fokkink--Papavassiliou--Pelekis monotonicity paper

Robbert Fokkink, Symeon Papavassiliou, Christos Pelekis, *On the monotonicity of
tail probabilities*, Probability and Mathematical Statistics 42(1) (2022),
133--141, DOI `10.37190/0208-4147.00050`.

The abstract and theorem setup concern integer-valued independent random
variables \(S,X\) with integer means and conditions implying
\(\Pr(S\ge ES)\ge\Pr(S+X\ge E(S+X))\), especially when the mean of \(S\) is a
mode.  This does not apply to arbitrary weighted Bernoulli convex combinations
at a real threshold.

## Kellerer

Hans G. Kellerer, *Zur Existenz analoger Bereiche*, Z. Wahrscheinlichkeitstheorie
verw. Gebiete 1 (1963), 240--246, DOI `10.1007/BF00532495`.

This remains an atomless analogous-region theorem.  I found no finite-cube
down-set convex-hull statement or biased-measure threshold inequality in it.
Later Kellerer marginal-duality results are general transport/marginal duality
theorems; they do not supply the needed numerical inequality.

## Search conclusion

Searches for “p-biased measure downset convex hull”, “fractional matching biased
measure down-set”, and “weighted threshold biased measure p<=1/3” did not turn up
a primary theorem implying
\[
  \Pr_q\!\left(\sum_i w_i\eta_i>q\right)\le q
\]
for all \(q\ge2/3\), nor the equivalent down-set convex-hull theorem.
