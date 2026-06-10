# Compute worker reply — round 4
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/compute
zip: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/agents/Compute-c3-f225e0/compute_workspace_round_4.zip

---

# Round 4 report: pivot two-tail inequality

Artifacts:

- `code/round4_pivot_search.py`
- `data/round4_pivot_search_output.txt`

I found no counterexample.  The useful output is a sharper diagnosis of why the naive induction fails, plus finite MILP evidence that the pivot inequality is tight only through one-large-weight / pivot-plus-dust structures in the tested range.

## 1. Induction algebra and the right obstruction

Write
\[
\Phi_a(u)=\Pr[Y\ge p]-\lambda\Pr[Y<p-a],
\qquad
Y=\sum_i u_i v_i,\quad \lambda={p\over1-p},\quad \sum_i u_i=1-a.
\]
Expose one weight \(x\), and let \(Z\) be the remaining sum.  Put
\[
\begin{aligned}
A&=\Pr[Z\ge p],&
B&=\Pr[Z\ge p-x],\\
C&=\Pr[Z<p-a],&
D&=\Pr[Z<p-a-x].
\end{aligned}
\]
Then the exact one-step identity is
\[
\Phi_a(x,Z)
=(1-p)A+pB-\lambda\{(1-p)C+pD\}
=(1-p)\bigl(A+\lambda B-\lambda C-\lambda^2D\bigr).
\tag{1}
\]
This is the most useful two-threshold invariant I found:
\[
\boxed{\quad
\Psi_{a,x}(Z):=
A+\lambda B-\lambda C-\lambda^2D\ge0.
\quad}
\tag{2}
\]
It is exactly strong enough to close after exposing \(x\).  The original pivot inequality is the case \(x=0\), up to the factor \(1+\lambda\).

The one-parameter induction fails because applying the pivot inequality to the rest only gives \(A\ge\lambda D\), which discards surplus needed to compensate possible \(B<C\).  The naive coefficient-1 two-threshold comparison
\[
\Pr[Z\ge p-x]\ge \Pr[Z<p-a]
\]
is false, even in an exact one-weight example:
\[
p={3\over10},\quad a=x={1\over10},\quad Z={4\over5}v.
\]
Then
\[
\Pr[Z\ge p-x]={3\over10},\qquad
\Pr[Z<p-a]={7\over10}.
\]
Nevertheless the full exposed pivot inequality has equality, because the \(A-\lambda^2D\) surplus in (1) exactly cancels \(B-C\).  This example is a good warning: any successful induction must keep the four-tail quantity (2), or something morally equivalent, not just a scalar pivot surplus.

I also tested simpler candidate strengthenings such as
\[
\Pr[Z\ge p-\beta]+(1-\lambda)\Pr[Z<p-\alpha-\beta]\ge \Pr[Z<p-\alpha]
\]
and slackened variants \(\Pr[Z\ge p]\ge\lambda\Pr[Z<p-\alpha]\) for total \(1-\alpha-\beta\).  Both fail for spread-out weights when \(\beta\) is close to \(p-\alpha\).  Thus (2) currently looks like the minimal invariant that is not immediately falsified.

## 2. Finite chamber / MILP formulation

For fixed rational \(p,a,n\), a counterexample can be searched by threshold chambers.  Let \(w_i\ge0\), \(\sum_iw_i=1-a\).  For every subset \(S\subseteq[n]\), introduce binary labels:

- \(y_S=1\) means \(w(S)<p-a\) (lower bad set),
- \(z_S=1\) means \(w(S)\ge p\) (upper success set).

The objective for a violation is
\[
V=\lambda\sum_S \mu_p(S)y_S-\sum_S\mu_p(S)z_S.
\]
The script uses two versions:

- an equality-ambiguous outer relaxation, allowing threshold equality to be labeled in the violation-favorable direction;
- a strict chamber search with gap \(10^{-5}\), so any positive direct \(V\) would give an actual counterexample away from chamber walls.

The MILP includes the linear threshold constraints, monotonicity of \(y\) as a down-set and \(z\) as an up-set, \(y_S+z_S\le1\), and a symmetry break sorting the weights.  After solving, the script recomputes the actual pivot margin directly from the returned weights.

## 3. Computational results

Random \(n=8\) Dirichlet searches over
\[
p\in\{1/6,1/5,1/4,3/10,1/3\},\qquad
a\in\{0,p/4,p/2,3p/4\}
\]
found no negative pivot margin.  The best cases always collapsed to equality-like configurations with one dominant weight (or pivot plus dust).

Strict MILP checks were stronger.  For
\[
p\in\{1/6,1/5,1/4,2/7,3/10,1/3\},\qquad
a\in\{0,p/2,3p/4\},
\]
the \(n=7\) strict MILPs all solved to optimality with max violation at numerical zero (largest displayed positive value was about \(1.8\cdot10^{-15}\), solver tolerance scale).  Selected \(n=8\) strict MILPs also solved to optimality:

| \(p\) | \(a\) | strict MILP max \(V\) | direct \(V\) from weights | status |
|---:|---:|---:|---:|---|
| \(1/6\) | \(1/12\) | \(1.15\cdot10^{-17}\) | \(0\) | optimal |
| \(1/4\) | \(1/8\) | \(0\) | \(0\) | optimal |
| \(2/7\) | \(1/7\) | \(4.34\cdot10^{-15}\) | \(0\) | optimal |
| \(3/10\) | \(0\) | \(1.76\cdot10^{-15}\) | \(5.55\cdot10^{-17}\) | optimal |
| \(3/10\) | \(3/20\) | \(3.75\cdot10^{-16}\) | \(5.55\cdot10^{-17}\) | optimal |
| \(1/3\) | \(0\) | \(-4.43\cdot10^{-15}\) | \(0\) | optimal |
| \(1/3\) | \(1/6\) | \(1.79\cdot10^{-18}\) | \(0\) | optimal |

No exact rational counterexample was found.  The strict optima usually sit at one large coordinate \(1-p+O(10^{-5})\) plus small coordinates at chamber gaps, giving equality \(\Pr[Y\ge p]=p\), \(\Pr[Y<p-a]=1-p\).

One caution: the outer relaxation can show artificial positive values at equality walls, e.g. \(p=1/3,a=0\) with three weights \(1/3\).  That is not a counterexample, because actual success uses the closed threshold \(w(S)\ge p\).  The strict MILP and direct recomputation remove this artifact.

## 4. Pivot plus dust check

The near-extremal family remains exactly as expected.  With one weight \(p-\varepsilon\) and \(N\) equal dust weights, for \(\varepsilon=0.01\):

| \(p\) | \(N\) | tail \(\Pr[X\ge p]\) | tail minus \(p\) |
|---:|---:|---:|---:|
| \(0.3\) | 20 | 0.379092647215 | \(7.91\cdot10^{-2}\) |
| \(0.3\) | 100 | 0.302777452181 | \(2.78\cdot10^{-3}\) |
| \(0.3\) | 500 | 0.300000002028 | \(2.03\cdot10^{-9}\) |
| \(1/3\) | 20 | 0.394496940105 | \(6.12\cdot10^{-2}\) |
| \(1/3\) | 100 | 0.333612894055 | \(2.80\cdot10^{-4}\) |
| \(1/3\) | 500 | 0.333333333333 | \(6.05\cdot10^{-14}\) |

So any proposed stronger lower bound with a fixed positive gap over \(p\) is impossible.

## 5. Complement-form literature check

The complement target is
\[
q\ge {2\over3},\qquad
\Pr\!\left[\sum_i w_i\eta_i>q\right]\le q.
\]
This is the strict hypotenuse version of the Fokkink--Meester--Pelekis quantity
\(\pi(q,t)=\sup_\gamma\Pr(S_\gamma\ge t)\), with \(t>q\) and \(t\downarrow q\).  Their paper `papers/fokkink-meester-pelekis-2023.pdf/.txt` defines this problem and proves adjacent bold-play regions: Theorem 4.4 covers upper-right rectangles away from the hypotenuse, Proposition 4.5 covers diagonal points \((q,t)=((k+1)/(k+2),(k+1)/(k+2))\), and Proposition 4.6 covers one nearby family.  The paper explicitly says an array of triangles along the hypotenuse remains unfilled.  Our desired \(q\ge2/3,\ t>q\) includes exactly those near-hypotenuse gaps, so FMP does not prove the needed strict statement.

Csoka's `papers/csoka-2015-limit-theory.pdf/.txt` formulates the limiting weighted Bernoulli tail problem (Problems 4.3 and 4.8) and gives conjectural/numerical structure, but not a theorem covering this case.  Kellerer's analogous-region theorem remains atomless measure-splitting and does not directly imply the finite \(q\)-biased halfspace inequality.

The quota family \(\{S:w(S)>q\}\) is intersecting for \(q>1/2\), but ordinary \(q\)-biased intersecting-family theorems are not enough: for \(q>1/2\), arbitrary intersecting families can have measure much larger than \(q\).  The linear-threshold/quota structure is essential.

## Bottom line

No counterexample emerged.  The cleanest proof route I see is to work with the four-tail invariant (2), not the one-parameter pivot alone.  The finite MILP evidence up to \(n=7\) on a rational grid and selected \(n=8\) cases supports the pivot inequality sharply, with equality approached by one-large-weight / pivot-plus-dust configurations. 
