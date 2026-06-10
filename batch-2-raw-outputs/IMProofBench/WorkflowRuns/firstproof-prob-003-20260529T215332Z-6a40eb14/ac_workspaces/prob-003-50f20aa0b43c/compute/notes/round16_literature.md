# Round 16 literature notes

Target:
\[
q\,\Pr\!\left[\sum_i b_i(\zeta_i-p)\ge p\right]
\ge
p\,\Pr\!\left[\sum_i b_i(\zeta_i-p)<-q\right],
\quad 0<p\le 1/3,\ q=1-p,\ 0\le b_i\le1.
\]

Equivalently, in complement/FMP notation, for
\(T=\sum_i w_i\eta_i\), \(\eta_i\sim\mathrm{Bernoulli}(q)\),
\[
    \Pr(T>q)\le q,\qquad q\ge 2/3,\quad \sum_i w_i=1.
\]

## Closest exact framework: Fokkink--Meester--Pelekis

Robbert Fokkink, Ludolf Meester, Christos Pelekis, *Optimizing stakes in
simultaneous bets*, ALEA 20 (2023), 153--165, DOI `10.30757/ALEA.v20-07`.
Local files: `papers/fokkink-meester-pelekis-2023.txt` and
`papers/fokkink_meester_pelekis_optimizing_stakes_2023.pdf`.

They define
\[
  \pi(p,t)=\sup_\gamma \Pr\!\left(\sum_i c_i\beta_i\ge t\right),
\]
where \(\beta_i\) are iid Bernoulli(\(p\)) and \(\gamma=(c_i)\) ranges over
nonnegative convex combinations.  Our complement theorem would follow from
\[
  \pi(q,t)\le q\qquad(q\ge2/3,\ t>q),
\]
because for a fixed finite coefficient vector the strict event \(T>q\) is
\(T\ge t_*\), where \(t_*\) is the smallest attainable subset sum above \(q\).

FMP prove several adjacent bold-play regions, but not this whole strip:

- Their Theorem 4.4 proves bold play in rectangles of the form
  \[
    {k\over k+1}<p\le {k+1\over k+2}<t.
  \]
- Their Proposition 4.5 proves diagonal endpoints
  \(p=t=(k+1)/(k+2)\) for \(k>1\), with a special exceptional case at \(k=1\).
- Immediately after Proposition 4.6 they state that an array of triangles along
  the hypotenuse remains open, and numerical results suggest bold play in those
  triangles except the one touching \(1/2\le p=t\le2/3\).

Thus FMP is the right language, but it does not provide a black-box proof of
CTC.  The missing CTC region is exactly the strict near-hypotenuse strip
\[
  q<t\le {k+1\over k+2},\qquad {k\over k+1}<q<{k+1\over k+2},
\]
for \(q\ge2/3\).

## Intersecting-family references

FMP quote Fishburn--Frankl--Freed--Lagarias--Odlyzko, *Probabilities for
intersecting systems and random subsets of finite sets*, SIAM J. Algebraic
Discrete Methods 7 (1986), 73--79.  The relevant quoted theorem maximizes
\(\mu_p(\mathcal F)\) over intersecting families: for \(p\le1/2\), a star is
maximal; for \(p\ge1/2\) and odd \(n\), the upper half family is maximal.
This helps FMP for thresholds \(t>1/2\), but it does not handle our
complement threshold \(q\ge2/3\) because the weighted-threshold family is
3-wise intersecting, not merely intersecting, and arbitrary 3-wise
intersecting families are too large above bias \(2/3\).

Frankl/Tokushige/Filmus-style biased-measure theorems for \(r\)-wise or
\(t\)-intersecting families explain reciprocal endpoints, but I found no
statement incorporating the additional same-weight threshold/quota structure
\(\{A:w(A)>q\}\) strongly enough to yield \(\mu_q\le q\) for every \(q\ge2/3\).

## Pinelis/Bentkus/Dzindzalieta/Hoeffding/Samuels

Pinelis, *Optimal binomial, Poisson, and normal left-tail domination for sums of
nonnegative random variables*, EJP 21 (2016), gives optimal left-tail
domination from first and second moments for sums of independent nonnegative
variables.  It bounds one left tail of a nonnegative sum; it does not compare
the two CTC tails with the exact factor \(p/q\), and moment-only bounds remain
too weak near the pivot-plus-dust equality regime.

Bentkus--Dzindzalieta and Dzindzalieta--Juskevicius--Sileikis give sharp
comparison inequalities for Rademacher/symmetric bounded sums and related
Littlewood--Offord problems.  The centered Bernoulli increments here are
asymmetric \((+qb_i,-pb_i)\), and I found no asymmetric counterpart with the
needed sharp two-tail ratio.

Samuels/Feige concern upper-tail probabilities for sums of arbitrary
nonnegative independent variables with prescribed means.  They are adjacent to
FMP's motivation but point in the wrong extremal direction for CTC; even
assuming Samuels does not immediately give \(\Pr_q(T>q)\le q\) for convex
combinations of iid Bernoulli(\(q\)) variables.

## Kellerer

The Kellerer references already downloaded in earlier rounds remain
conceptually related to analogous regions/marginals.  I found no finite-cube
down-set convex-hull theorem or biased halfspace inequality in those papers
that implies CTC.  I would not cite Kellerer as proving the missing theorem
without a new derivation.
