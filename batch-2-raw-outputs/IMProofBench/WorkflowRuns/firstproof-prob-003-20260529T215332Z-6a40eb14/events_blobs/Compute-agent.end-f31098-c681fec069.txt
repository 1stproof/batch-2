# Round 14 compute report

I read the current `answer.tex` and `research_notes.tex`.  New files:

- `code/round14_downset_hull.py`
- `data/round14/downset_hull_summary.md`
- `data/round14/downset_hull_results.json`
- `code/round14_coloring_3_10.py`
- `data/round14/coloring_3_10_summary.md`
- `data/round14/coloring_3_10_results.json`
- `notes/round14_literature.md`

## 1. Down-set convex-hull theorem

For a down-set \(\mathcal D\), its ordinary convex hull is already coordinatewise down-closed.  I computed
\[
r(\mathcal D)=\max\{t:t{\bf1}\in\operatorname{conv}\{1_A:A\in\mathcal D\}\}
\]
by LP for every down-set on \(m\le5\).  The tested statement is exactly:
\[
\mu_p(\mathcal D)>1-p\implies r(\mathcal D)\ge p.
\]

No counterexample was found.

| \(m\) | # down-sets | \(p=1/3\) violations | \(p=3/10\) violations | \(p=1/4\) violations | \(p=1/5\) violations |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 0 | 0 | 0 | 0 |
| 2 | 6 | 0 | 0 | 0 | 0 |
| 3 | 20 | 0 | 0 | 0 | 0 |
| 4 | 168 | 0 | 0 | 0 | 0 |
| 5 | 7581 | 0 | 0 | 0 | 0 |

The maximum \(\mu_p(\mathcal D)\) among separated families \(r(\mathcal D)<p\) is always exactly \(1-p\), attained by dictatorship-type equality examples, e.g. a down-set whose maximal set omits one coordinate.  Thus the strict premise \(\mu_p>1-p\) is essential and survives the exhaustive checks.

The best positive-diagonal separated examples are more informative:

| \(m\) | \(p\) | max \(\mu_p\) with \(0<r<p\) | \(r\) | gap to \(1-p\) | maximals |
|---:|---:|---:|---:|---:|---|
| 4 | \(1/3\) | \(16/27=0.5925926\) | \(1/4\) | \(2/27\) | four singletons |
| 4 | \(3/10\) | \(6517/10000=0.6517\) | \(1/4\) | \(483/10000\) | four singletons |
| 5 | \(1/3\) | \(16/27=0.5925926\) | \(1/4\) | \(2/27\) | cone over four singletons |
| 5 | \(3/10\) | \(6517/10000=0.6517\) | \(1/4\) | \(483/10000\) | cone over four singletons |

I also ran a separate \(m=6\) MILP over separated threshold down-sets with margin \(10^{-6}\).  This is not a full all-down-set enumeration, but any strict separated counterexample with margin at least \(10^{-6}\) would be found by this search after enlarging to the full threshold down-set.  It found only equality/sharpness configurations:

| \(p\) | max strict light mass found | target \(1-p\) | representative separator weights |
|---:|---:|---:|---|
| \(1/3\) | \(0.666666666667\) | \(0.666666666667\) | essentially one atom of weight \(1\) |
| \(3/10\) | \(0.700000000000\) | \(0.700000000000\) | \(0.299999,0.700001\) |
| \(1/4\) | \(0.750000000000\) | \(0.750000000000\) | \(0.249999,0.750001\) |
| \(1/5\) | \(0.800000000000\) | \(0.800000000000\) | \(0.199999,0.800001\) |

### Induction state

Let the two slices of a down-set on \([n+1]\) be \(\mathcal E=\mathcal D_0\) and \(\mathcal F=\mathcal D_1\subseteq\mathcal E\).  The scalar state \(r(\mathcal D)\) has the lower bound
\[
r(\mathcal D)\ge {r(\mathcal E)\over 1+r(\mathcal E)-r(\mathcal F)}.
\]
This comes from mixing the diagonal points of the two slices.  It is not exact: in the exhaustive data the exact value exceeded this scalar bound for 63 down-sets at \(m=4\) and 5072 down-sets at \(m=5\).  Example:
\[
\max(\mathcal D)=\{\{1\},\{2\},\{3,4\}\}
\]
has \(r(\mathcal D)=1/3\), while \(r(\mathcal D_0)=1/3\), \(r(\mathcal D_1)=0\), and the scalar lower bound gives only \(1/4\).  Thus \(r\) alone loses the cross-coordinate complementarity needed exactly in the problematic case \(p{\bf1}\in P(\mathcal D_0)\) but not \(P(\mathcal D_1)\).

The clean exact state is the nonnegative support function
\[
h_{\mathcal D}(c)=\max_{A\in\mathcal D}\sum_{i\in A}c_i,\qquad c\ge0.
\]
For slices,
\[
h_{\mathcal D}(u,z)=\max\{h_{\mathcal E}(u),\,z+h_{\mathcal F}(u)\}.
\]
Equivalently, for fixed \(p\), with \(\Delta_{\mathcal H}(u)=h_{\mathcal H}(u)-p\sum_i u_i\),
\[
\Delta_{\mathcal D}(u,z)=
\max\{\Delta_{\mathcal E}(u)-pz,\ \Delta_{\mathcal F}(u)+(1-p)z\}.
\]
This is an exact recurrence for convex-hull membership by separation, but it is infinite-dimensional.  I did not find a scalar compression such as \(r\), \(h({\bf1})\), or a one-variable deficit function that was both sharp enough and closed under the slice recurrence.

## 2. Averaged coloring for \(p=3/10\)

For \(p=a/b\), if original weights \(w_i\) are randomly colored into \(b\) colors and \(X_j\) is the load of color \(j\), then
\[
\mathbb E\#\{J\in{[b]\choose a}:\sum_{j\in J}X_j\ge a/b\}
= {b\choose a}\Pr_{a/b}\!\left(\sum_i w_i v_i\ge a/b\right).
\]
So the desired averaged coloring inequality is exactly equivalent to the original Bernoulli inequality:
\[
\mathbb E\#\{\text{heavy }a\text{-sets}\}\ge {b-1\choose a-1}.
\]

For \(a/b=3/10\), the deterministic vector \((1/7,\ldots,1/7,0,0,0)\) has only \(\binom73=35\) heavy triples, below the target \(36\).  But the corresponding random-coloring examples are safely above target:

| original weights | \(\Pr(S\ge0.3)\) | expected heavy triples | gap over 36 |
|---|---:|---:|---:|
| seven atoms \(1/7\) | \(0.3529305\) | \(42.35166\) | \(6.35166\) |
| four atoms \(1/4\) | \(0.3483\) | \(41.796\) | \(5.796\) |
| \(0.29\) plus 60 equal dust atoms | \(0.3137020\) | \(37.64424\) | \(1.64424\) |
| one atom \(1\) | \(0.3\) | \(36\) | \(0\) |

The pivot-plus-dust examples show why no uniformly stronger averaged bound can be true: with \(0.29\) plus \(N\) equal dust atoms, the expected heavy count tends down to \(36\) as \(N\to\infty\).

Exact grid searches for \(p=3/10\), with all weights on denominator \(d\le40\), found no violation.  Without the cap \(w_i<p\), the maximum light probability is exactly \(0.7\), attained by the one-atom vector.  With strict cap \(w_i<0.3\), the grid maximum through \(d=40\) is \(6517/10000\), i.e. expected heavy count \(41.796\), attained by four-effective-block configurations such as \((1/4)^4\) or perturbations/splittings of it.  Capped MILPs for support sizes \(n=6,7\) proved the same optimum \(0.6517\) in those chambers.

I did not find a finite LP/dual certificate proving the arbitrary-support \(3/10\) case.  The averaged statement is exactly the original problem, and the near-equality pivot-plus-dust family suggests that any certificate must allow limiting support size.

## 3. Literature search

No direct theorem was found.

Closest source: Fokkink--Meester--Pelekis, *Optimizing stakes in simultaneous bets*, ALEA 20 (2023), DOI `10.30757/ALEA.v20-07`.  In complement notation, the missing theorem would be
\[
\pi(q,t)\le q,\qquad q\ge2/3,\quad t>q,
\]
where \(\pi\) is their supremal tail probability for convex combinations of iid Bernoulli variables.  Their Theorem 4.4 proves bold play for
\[
{k\over k+1}<q\le {k+1\over k+2}<t,
\]
and Proposition 4.5 proves diagonal endpoints \(q=t=(k+1)/(k+2)\) for \(k>1\).  The strict near-hypotenuse strip \(q<t\le(k+1)/(k+2)\) remains outside their theorem; they explicitly say an array of triangles along the hypotenuse remains open.

Fokkink--Papavassiliou--Pelekis, *On the monotonicity of tail probabilities*, Probability and Mathematical Statistics 42(1) (2022), DOI `10.37190/0208-4147.00050`, concerns integer-valued sums with integer means and a mode condition.  I found no way to apply it to arbitrary real weighted Bernoulli convex combinations.

Kellerer, *Zur Existenz analoger Bereiche*, DOI `10.1007/BF00532495`, remains only conceptually adjacent: it is an atomless analogous-region theorem, not a finite discrete-cube down-set convex-hull theorem.  Searches around Kellerer marginal duality likewise found general transport/marginal duality, not the required numerical biased-measure inequality.

Bottom line: the down-set theorem survived all \(m\le5\) exhaustive checks, but I found no published result that proves it, and the exact support-function recurrence is the most precise induction state I found this round.
