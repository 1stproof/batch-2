# Round 11 compute report: homogeneous unit-gap inequality

I read the current `answer.tex`/`research_notes.tex` formulations and focused on
\[
 \Pr[S\ge p(B+h)]\ge {p\over 1-p}\Pr[S<p(B+h)-h],
 \quad S=\sum_i b_i\zeta_i,\quad 0\le b_i\le h .
\]
All computations below normalize \(h=1\), which is equivalent by scaling.

## 1. Literature search

I did **not** find an exact published statement of HUG.  The closest references remain adjacent rather than directly proving it.

Useful downloaded/local files:

- `papers/fokkink_meester_pelekis_optimizing_stakes_2023.pdf`  
  Fokkink--Meester--Pelekis, *Optimizing stakes in simultaneous bets*, ALEA 20 (2023), 153--165, DOI `10.30757/ALEA.v20-07`.  They define
  \[
  \pi(p,t)=\sup_{\sum c_i=1,c_i\ge0}\Pr\!\left[\sum_i c_i\beta_i\ge t\right].
  \]
  The complement form of the original problem asks for
  \[
  \Pr\!\left[\sum_i w_i\eta_i>q\right]\le q,\qquad q=1-p\ge 2/3,
  \]
  i.e. the strict hypotenuse \(t\downarrow q\) of their problem with Bernoulli parameter \(q\).  FMP prove several bold-play regions, including Theorem 12 and endpoint Proposition 13, but explicitly leave zigzag hypotenuse triangles.  Those omitted triangles are exactly where the strict threshold can lie when the next attainable subset sum above \(q\) is very close to \(q\).  So FMP is highly relevant but does not close HUG.

- `papers/tokushige-2022-applications-pbiased.pdf` / `.txt`  
  Tokushige, *Application of hypergraph Hoffman's bound to intersecting families*.  Theorem 1.3 says that a 3-wise intersecting family has \(\mu_{\mathbf p}\)-measure at most \(p_1\) under hypotheses including \(p_2<2/3\); in the equal-bias case this recovers the star bound below \(2/3\).  Our complement family is 3-wise intersecting when \(p_{\rm orig}\le 1/3\), but it is measured at \(q=1-p_{\rm orig}\ge2/3\), just outside this theorem except at the endpoint.  This explains why plain 3-wise intersection is insufficient.

- `papers/filmus_weighted_complete_intersection_2017.pdf`  
  Filmus, *The weighted complete intersection theorem*, JCTA 151 (2017), 84--101.  Relevant to biased-measure extremal intersecting families, but it does not use the weighted-threshold/quota structure needed here.

- `papers/pinelis_left_tail_domination_2016_arxiv.pdf`  
  Pinelis, *Optimal binomial, Poisson, and normal left-tail domination for sums of nonnegative random variables*, EJP 21 (2016), DOI `10.1214/16-EJP4474`.  Gives sharp left-tail domination from first/second moment data for broad function classes.  I do not see a way to extract the exact two-tail constant \(p/(1-p)\); moment-only bounds are too weak near pivot-plus-dust examples.

- Existing local files `papers/kellerer-analogous-areas.*` and `problem_documents_readonly/references.bib` cover Kellerer's analogous-regions theorem.  It is an atomless splitting result, not a discrete Bernoulli halfspace inequality.  I would not cite it as proving HUG without a new derivation.

Project Euclid/SIAM direct downloads for Samuels/Jogdeo--Samuels/Fishburn et al. were blocked in this sandbox, but the citations and statements are available through FMP and the existing notes.

## 2. Proof attempts / useful reformulations

The cleanest equivalent centered form is this.  With \(q=1-p\) and
\[
X=\sum_i b_i(\zeta_i-p),
\]
HUG is exactly
\[
\Pr[X\ge ph]\ge {p\over q}\Pr[X<-qh],
\]
where each summand has mean zero and takes values \(q b_i\) and \(-p b_i\), with \(0\le b_i\le h\).  So HUG is a bounded-jump asymmetric two-tail inequality.

The natural one-coordinate induction has a precise obstruction.  Write \(S=R+c\zeta\), \(0\le c\le h\), \(T=p(B+h)\).  Then
\[
U=q\Pr(R\ge T)+p\Pr(R\ge T-c),
\]
and
\[
L=q\Pr(R<T-h)+p\Pr(R<T-h-c).
\]
Applying HUG to \(R\) with gap \(h+c\) controls
\[
\Pr(R\ge T)\quad\text{against}\quad \Pr(R<T-h-c),
\]
while applying HUG with gap \(h\) controls a threshold \(T-pc\), not \(T-c\), and leaves exactly the interval mass
\[
\Pr(T-h-pc\le R<T-h)
\]
uncontrolled.  This is the same interval-mass obstruction noted in the draft, but the centered form makes clear that a successful induction needs either a two-shift Bellman value or an additional buffer term.

A direct product-shadow injection also cannot work in the obvious way.  Let
\[
L=\{A:b(A)<p(B+h)-h\},\quad U=\{A:b(A)\ge p(B+h)\}.
\]
Since each \(b_i\le h\), adding one coordinate to a set in \(L\) still cannot reach \(U\).  Thus the usual one-step \(p/q\) shadow injection is structurally unavailable; any shadow proof must use multi-step expansion with enough multiplicity to compensate for the extra factor \(p/q\).

The most viable rigorous route I see is a finite-chamber/minimal-counterexample proof.  For fixed \(p,n\), the HUG difference is constant on chambers cut out by the affine hyperplanes
\[
b(A)=p(B+1),\qquad b(A)=p(B+1)-1.
\]
Thus a counterexample can be searched by linear feasibility over sign patterns; at a minimal counterexample with \(\max b_i=1\), one expects many tight subset-sum/cap constraints.  This is exactly what the MILP checker below implements.

## 3. Computational checks

Code and output:

- `code/hug_check.py`
- `data/hug_results.json`
- `data/hug_targeted_milp.json`
- `data/hug_capped_milp.json`
- `data/hug_capped_milp_summary.md`

The checker uses exact enumeration of all \(2^n\) subsets for a given coefficient vector.  For fixed \(p,n\), it also solves a mixed-integer linear search over threshold chambers.  Binary variables encode membership in the upper and lower events.  The default MILP is a **closed-boundary relaxation**: it can only make the objective smaller than the true HUG difference, because it may undercount the upper closed event and overcount the lower strict event at boundaries.  Therefore a nonnegative relaxed optimum certifies no violation for that fixed \(p,n\).

To avoid the degenerate all-zero equality case, I also ran the normalized capped search with \(b_1=1\), equivalent by symmetry/scaling to \(\max_i b_i=h\).

Selected capped MILP results for \(n\le6\):

| \(p\) | min relaxed HUG difference | \(n\) attaining min | comment |
|---:|---:|---:|---|
| \(1/6\) | 0.115869341564 | 6 | certified nonnegative |
| 0.2 | 0.0784 | 4 | certified nonnegative |
| 0.25 | 0.015625 | 3 | certified nonnegative |
| 0.30 | 0.069 | 5 | certified nonnegative |
| 0.31 | 0.081127 | 6 | certified nonnegative |
| 0.32 | 0.093696 | 6 | certified nonnegative |
| \(1/3\) | 0.111111111111 | 4 | epsilon-interior search; endpoint also follows from the known reciprocal proof |

Random enumeration/search over coefficient lists up to length 9 also found no violation for \(p\le1/3\).  For \(p>1/3\), violations appear immediately.

## 4. Explicit counterexamples for \(p>1/3\)

For every \(1/3<p<1/2\), take \(n=2\), \(b_1=b_2=h\).  Then \(B=2h\), the upper threshold is \(3ph\), and the lower threshold is \((3p-1)h\).  Hence
\[
\Pr[S\ge 3ph]=p^2,\qquad \Pr[S<(3p-1)h]=q^2,
\]
so HUG would require \(p^2\ge pq\), i.e. \(p\ge1/2\).  Thus it fails on the whole interval \((1/3,1/2)\).

Concrete exact example at \(p=2/5\), \(h=1\), \(b=(1,1)\):
\[
U=\frac4{25},\qquad L=\frac9{25},\qquad {p\over q}={2\over3},
\]
so
\[
U-{p\over q}L=\frac4{25}-{2\over3}{9\over25}=-{2\over25}.
\]

For every \(1/2<p<1\), take \(n=1\), \(b_1=h\).  Then the upper threshold \(2ph\) exceeds \(h\), so \(U=0\), while the lower event contains \(\zeta=0\) and has probability \(q\).  The RHS is \(p>0\), so HUG fails.

Bottom line: no counterexample was found for \(p\le1/3\) in the global \(n\le6\) chamber searches, and the expected post-\(1/3\) failure is exact and very small.
