# Round 1 literature search: pointwise AC / uniqueness gap

## Executive recommendation

**No direct citation found.** The closest result is Bounebache--Zambotti (BZ) Proposition 2.5, but it is a Dirichlet-form resolvent statement: the representing kernel is identified with the \(L^2(\nu)\) resolvent only \(\nu\)-a.e.; on the exceptional set it is set to zero. BZ use it to pass from stationarity to **quasi-every** initial condition, not every deterministic initial condition. I found no theorem in ABLM 2024, ABLM weak/mild 2025, or Butkovsky--Mytnik 2024/2025 that identifies the BZ local-time process with the ABLM mild/regularized solution for every deterministic initial condition or proves
\[
R_\lambda^P(x,\cdot)\ll \pi,\qquad x\in C_0([0,1]).
\]

The missing step is likely a new lemma of one of the following forms:

1. **Strict-version lemma:** the ABLM all-starting-points Markov process is a strict version of the BZ quasi-regular Dirichlet-form process, and its resolvent equals BZ's absolutely continuous kernel for every \(x\).
2. **Entrance lemma:** if \(N\) is the BZ exceptional set, then \(P_s^P(x,N)=0\) for every deterministic \(x\) and every \(s>0\).
3. **Uniform-density lemma:** for the smooth approximants \(P_t^n\), obtain uniform integrability of \(dR_\lambda^n(x,\cdot)/d\pi_n\), or a stable capacity bound, strong enough to pass AC to the ABLM limit.

The most economical proof skeleton is the entrance lemma; see the last section below.

## Downloaded / inspected files

I downloaded PDFs and arXiv sources into:

| paper | PDF | source |
|---|---|---|
| Athreya--Butkovsky--Lê--Mytnik, *Well-posedness...*, arXiv:2011.13498v3 | `papers/pdf/2011.13498_ABLM2024.pdf` | `papers/src_extracted/2011.13498_ABLM2024/CPAM.tex` |
| Bounebache--Zambotti, *A skew stochastic heat equation*, arXiv:1105.2779v2 | `papers/pdf/1105.2779_BZ2014.pdf` | `papers/src_extracted/1105.2779_BZ2014/karim_lorenzo.tex` |
| ABLM, *Analytically weak and mild solutions...*, arXiv:2410.06599v3 | `papers/pdf/2410.06599_ABLM2025_weak_mild.pdf` | `papers/src_extracted/2410.06599_ABLM2025_weak_mild/mildweak_v2_space.tex` |
| Butkovsky--Mytnik, *Weak uniqueness for singular stochastic equations*, arXiv:2405.13780v2 | `papers/pdf/2405.13780_BM2024_weak_uniqueness.pdf` | `papers/src_extracted/2405.13780_BM2024/weakU_final_copy.tex` |

Search helper and raw page hits are in `code/search_pdf_pages.py` and `data/*_page_hits.txt`.

## BZ 2014: what it gives and what it does not give

BZ is the relevant Dirichlet-boundary paper. Their equation (1.6), p.3, is
\[
\partial_t u=\tfrac12\partial_{\theta\theta}u
-\tfrac12\int_\mathbb R f(da)\,\partial_\theta \ell^a_{t,\theta}+\dot W,
\quad u(t,0)=u(t,1)=0.
\]
Taking \(f=-2{\bf 1}_{(0,\infty)}\) gives \(f(da)=-2\delta_0(da)\), hence the singular term is \(+\partial_\theta\ell^0_{t,\theta}\), formally \(\delta_0(u)\). Their invariant/reference measure is
\[
\nu(dx)=Z^{-1}\exp\{-F(x)\}\mu(dx),\qquad F(x)=\int_0^1 f(x_r)\,dr
\]
(p.5, (2.1)), so for this \(f\),
\[
\nu(dx)=Z^{-1}\exp\left(2\int_0^1{\bf 1}_{x_r>0}\,dr\right)\mu(dx)=\pi(dx).
\]

Key statements:

- **Intro, p.3:** they explicitly say strong Feller is not available: "the process is not Strong-Feller, or at least a proof of this property is out of our reach"; instead they prove absolute continuity of the transition semigroup w.r.t. \(\nu\), referring to Proposition 2.5.
- **Proposition 2.5, p.8:** There is a measurable kernel \(\rho_\lambda(x,dy)\) such that
  \[
  R_\lambda\varphi(x)=\int\varphi(y)\rho_\lambda(x,dy),\quad \nu\text{-a.e. }x,\quad \varphi\in L^2(\nu),
  \]
  and \(\rho_\lambda(x,dy)\ll\nu(dy)\) for all \(\lambda>0\), all \(x\in H\).
- **Proposition 2.7, p.8:** \(P_t:L^2(\nu)\to L^2(\nu)\) is Hilbert-Schmidt and has an \(L^2(\nu\otimes\nu)\) density \(p_t(x,y)\), again only in the \(L^2\)/\(\nu\)-a.e. sense.
- **Proof of Proposition 2.5, p.9:** using FOT Theorem 7.2.1, they obtain a zero-capacity set \(N\) and a Markov kernel \(p_t(x,dy)\) only for \(x\in N^c\). They then extend the AC conclusion to \(N^c\) by quasi-continuity and set \(\rho_\lambda(x,dy)\equiv0\) on \(N\). This is the crucial limitation: the all-\(x\) AC kernel is not asserted to be the actual process resolvent at exceptional \(x\).
- **Proposition 3.1, p.9:** the Dirichlet form is quasi-regular and the associated Markov process is a weak solution of (1.6).
- Immediately after Proposition 3.1, p.10: the absolute-continuity condition "allows to pass from the stationary solution to quasi-every initial condition" (their words), citing FOT Theorem 4.1.2 and formula (4.2.9).
- **Proposition 3.5, p.13:** the Fukushima/local-time decomposition holds outside an exceptional set.
- **Proof of Proposition 3.1, p.15:** for \(x\in N^c\), they use AC of \(X_\varepsilon\) to transfer continuity from the stationary solution. The statement is explicitly restricted by "where \(N\) is exceptional".

BZ also prove convergence of regularized equations, but only for stationary laws: Proposition 4.8, p.17, says \(\mathbb P_{\nu_n}^n\Rightarrow \mathbb P_\nu\) in \(C([0,T]\times[0,1])\). I did not find deterministic-start convergence there.

Conclusion: BZ gives exactly the \(L^2(\pi)\)/q.e. Dirichlet-form result, but it does **not** by itself prove \(R_\lambda^P(x,\cdot)\ll\pi\) for every deterministic ABLM initial condition.

## ABLM 2024: well-posedness/stability, but no transition AC

ABLM 2024 is not a Dirichlet-boundary paper. On pp.6--7 they state that they "do not analyze" Dirichlet boundary conditions because the local nondeterminism bound degenerates near the boundary, while saying they expect the results to adapt. This matches the problem's assumption that a Dirichlet extension is available.

Relevant statements:

- **Definition 2.3, p.7:** defines the mild/regularized solution by convergence of smooth drift approximations.
- **Theorem 2.6, p.8:** existence and uniqueness in the class \(\mathcal V(3/4)\) under \(\beta-1/q\ge -1\), \(\beta>-1\).
- **Theorem 2.8, p.8:** if \(b\) is a finite non-negative Radon measure, then for every bounded initial condition \(u_0\) the equation has a unique strong solution.
- **Corollary 2.9, p.8:** for \(b=\kappa\delta_0\), the skew stochastic heat equation has a unique strong solution for every bounded measurable \(u_0\).
- **Theorem 2.10, p.9:** smooth approximations \(b^n\to b\) and \(u_0^n\to u_0\) yield convergence in probability, uniformly on compact time/space sets (in their non-Dirichlet settings), to the strong solution.

Searches for `absolute continuity`, `resolvent`, `capacity`, `exceptional`, `invariant`, `strong Feller`, and `transition` found no transition/resolvent AC theorem. The paper gives pathwise/strong well-posedness and approximation stability, not a density/irreducibility result for \(P_t(x,\cdot)\).

Theorem 2.10 is useful but insufficient for the present gap: weak convergence of absolutely continuous regularized transition laws does not preserve absolute continuity without a uniform density/capacity estimate.

## ABLM weak/mild 2025: equivalence of formulations, not BZ identification for every point

This paper also excludes Dirichlet boundary in its actual convention: Convention 2.1, p.4, covers \(\mathbb R\), periodic, and Neumann. The abstract/introduction says \(D=[0,1]\) or \(\mathbb R\), but the formal convention is periodic/Neumann on \([0,1]\).

Relevant statements:

- **Definition 2.4, p.4:** mild regularized solution.
- **Definition 2.6, p.5:** weak regularized solution.
- **Theorem 2.10, p.6:** for \(\alpha>-3/2\), \(b\in\mathcal C^\alpha\), \(u_0\in B(D)\), and \(u\in\mathcal V(5/8)\), weak regularized and mild regularized solutions are equivalent.
- **Theorem 2.11, p.6:** for \(b\in L_p\), all four notions (analytic weak, weak regularized, analytic mild, mild regularized) are equivalent.
- **Corollary 2.12, p.7:** for \(b\in L_p\), \(p\ge1\), unique analytic mild/weak solution.

For \(b=\delta_0\), Theorem 2.10 is relevant at the level of weak-regularized vs mild-regularized formulations. However, BZ's local-time Dirichlet-form solution is not directly shown in this paper to satisfy Definition 2.6 for every deterministic initial point. At best, combining BZ with ABLM weak/mild equivalence and uniqueness identifies the BZ and ABLM laws for **q.e.** \(x\), assuming the Dirichlet extension and verifying the local-time term matches the weak-regularized drift. It still does not remove the exceptional set.

## Butkovsky--Mytnik 2024/2025: weak uniqueness, no invariant/resolvent AC

Relevant statements:

- **Convention 2.1, p.8:** the SPDE part covers \([0,1]\) with periodic or Neumann boundary conditions, not Dirichlet.
- **Definition 2.3, p.8:** mild solution with distributional drift by regularized approximation.
- **Remark 2.4, p.9:** they restrict to PDE-mild solutions and point to ABLM weak/mild equivalence under technical conditions.
- **Theorem 2.6, p.9:** for \(\alpha>-3/2\), weak uniqueness holds for solutions to SHE\((u_0;b)\) in class \(\mathcal V_{\rm SHE}(5/8)\), and smooth approximants converge weakly in \(C([0,T],C(D))\) to the unique weak solution.

This is a strong well-posedness/weak-uniqueness input, but not an invariant-measure uniqueness or transition-density theorem. The introduction also cautions that in infinite dimensions transition probabilities \(P_t(x,\cdot)\) and \(P_t(y,\cdot)\) are often orthogonal (p.4), so it should not be read as a smoothing/AC result.

## Can BZ Proposition 2.5 plus ABLM stability close the all-starting-points gap?

I do not see a complete assembly from existing statements.

What can likely be assembled:

1. For \(f=-2H_+\), BZ's \(\nu\) equals the proposed \(\pi\).
2. BZ gives a quasi-regular symmetric process with \(R_\lambda^{BZ}(x,\cdot)\ll\pi\) for \(x\in N^c\), where \(N\) is exceptional, and with local-time weak formulation q.e.
3. Assuming Dirichlet extensions of ABLM 2024/2025, the BZ q.e. process should be identifiable with the ABLM regularized/mild solution for \(x\in N^c\).

What remains missing:

- The actual ABLM semigroup started from \(x\in N\) is not identified with BZ's artificial \(\rho_\lambda(x,\cdot)\equiv0\).
- ABLM stability gives weak convergence of approximants, but weak limits of AC measures can be singular.
- No uniform \(L^p(\pi_n)\) density bound or capacity estimate for \(P_t^n(x,\cdot)\) was found.
- No theorem found saying arbitrary invariant measures of a strict all-starting-points SPDE cannot charge the Dirichlet-form exceptional set. In general this cannot be inferred from quasi-regularity alone; behavior on exceptional points is invisible to the \(L^2(\pi)\) form.

## Proposed proof skeleton for the missing lemma

The cleanest lemma to prove is:

**Entrance lemma.** Let \(N\) be a properly exceptional set for the BZ Dirichlet-form process. For the ABLM Dirichlet mild solution \(P_t\), prove
\[
P_t(x,N)=0,\qquad x\in C_0([0,1]),\ t>0.
\]

Then, if \(A\) is Borel with \(\pi(A)=0\), BZ plus identification gives \(R_\lambda^P(y,A)=0\) for \(y\in N^c\). For arbitrary \(x\),
\[
R_\lambda^P(x,A)
=\int_0^s e^{-\lambda t}P_t(x,A)\,dt
 + e^{-\lambda s}P_s R_\lambda^P(\cdot,A)(x).
\]
The second term is zero by \(P_s(x,N)=0\). The first term is bounded by \(s\), so letting \(s\downarrow0\) gives \(R_\lambda^P(x,A)=0\). Hence \(R_\lambda^P(x,\cdot)\ll\pi\) for all \(x\).

Possible ways to prove the entrance lemma:

1. Establish a short-time density/capacity estimate for ABLM from deterministic starts:
   \[
   P_t(x,B)\le C_{t,x}\operatorname{Cap}(B)^\alpha
   \quad\text{or}\quad
   P_t(x,\cdot)\ll\pi
   \]
   first for regularized equations, uniformly enough to pass to the singular limit.
2. Prove ABLM is the strict quasi-regular version of the BZ form and that BZ's resolvent kernel can be chosen to represent the strict resolvent at all points, not just q.e.
3. Prove a strong-resolvent/strong-Feller-type property for \(R_\lambda^P{\bf1}_A\) when \(\pi(A)=0\); this would extend the q.e. zero statement to every deterministic \(x\). BZ explicitly lacks strong Feller, so this would need a new weaker substitute tailored to null sets.

My recommendation for the Author draft: state uniqueness conditional on this entrance/strict-version lemma, and do **not** cite BZ Proposition 2.5 as proving all-starting-points AC for the ABLM semigroup. It proves the needed statement only q.e. unless supplemented by a new argument.
