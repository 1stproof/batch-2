# Compute worker reply — round 2
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-005-20260529T215332Z-6a40eb14/ac_workspaces/prob-005-d0645d92a902/compute
zip: /data/output/workflow_runs/firstproof-prob-005-20260529T215332Z-6a40eb14/agents/Compute-c1-c33810/compute_workspace_round_2.zip

---

# Round 2: all-starting-point resolvent absolute continuity

## Bottom line

I did **not** find a theorem in ABLM, Bounebache--Zambotti, Dirichlet-form texts, distorted Brownian motion papers, or singular-SPDE strong-Feller papers that proves
\[
R_\lambda^P(x,\cdot)\ll \pi,\qquad x\in C_0([0,1]),
\]
for the actual Dirichlet ABLM mild/regularized semigroup with drift \(\delta_0(u)\).

The current `answer.tex` is right to isolate this as a genuine remaining gap. BZ Proposition 2.5 is the closest result, but it does **not** identify its all-\(x\) kernel with the actual process resolvent on the exceptional set. I recommend not citing it as closing the all-starting-point gap.

New PDFs/texts downloaded this round:

| item | path |
|---|---|
| Baur--Grothaus--Stilgenbauer, \(L^p\)-strong Feller via Dirichlet forms | `papers/pdf/1112.4960_BaurGrothausStilgenbauer_Lp_strong_Feller.pdf`, `papers/text/1112.4960_BaurGrothausStilgenbauer_Lp_strong_Feller.txt` |
| Shin--Trutnau, stochastic regularity of distorted Brownian motions | `papers/pdf/1405.7585_ShinTrutnau_stochastic_regular_distorted_BM.pdf`, `papers/text/1405.7585_ShinTrutnau_stochastic_regular_distorted_BM.txt` |
| Hairer--Mattingly, strong Feller for singular SPDEs | `papers/pdf/1610.03415_HairerMattingly_strong_Feller_singular_SPDE.pdf`, `papers/text/1610.03415_HairerMattingly_strong_Feller_singular_SPDE.txt` |
| Grothaus--Wittmann, Mosco convergence for non-convex BV potentials | `papers/pdf/2105.05140_GrothausWittmann_Mosco_nonconvex.pdf`, `papers/text/2105.05140_GrothausWittmann_Mosco_nonconvex.txt` |
| Rockner--Trutnau, infinite-dimensional skew/reflected OU | `papers/pdf/1508.05824_RocknerTrutnau_skew_reflected_OU.pdf`, `papers/text/1508.05824_RocknerTrutnau_skew_reflected_OU.txt` |
| Kunze, perturbation of strong Feller semigroups | `papers/pdf/1101.2369_Kunze_perturbation_strong_Feller.pdf`, `papers/text/1101.2369_Kunze_perturbation_strong_Feller.txt` |
| Albeverio--Ma--Rockner, quasi-regular forms and stochastic quantization | `papers/pdf/1404.2757_AlbeverioMaRockner_quasi_regular_quantization.pdf`, `papers/text/1404.2757_AlbeverioMaRockner_quasi_regular_quantization.txt` |

## What BZ gives, exactly

In `papers/src_extracted/1105.2779_BZ2014/karim_lorenzo.tex`, BZ explicitly say the process is not known to be strong Feller:

- lines 250--270: "the process is not Strong-Feller, or at least a proof of this property is out of our reach"; they instead prove absolute continuity in Proposition 2.5.
- lines 555--642: Proposition 2.5 gives a measurable kernel \(\rho_\lambda(x,dy)\) with \(\rho_\lambda(x,\cdot)\ll\nu\) for all \(x\), but the identity
  \[
  R_\lambda\varphi(x)=\int \varphi(y)\rho_\lambda(x,dy)
  \]
  is only for \(\nu\)-a.e. \(x\).
- in the proof, they use FOT Theorem 7.2.1 to obtain a zero-capacity set \(N\) and a Markov kernel on \(N^c\). After proving AC on \(N^c\), they set \(\rho_\lambda(x,dy)\equiv0\) on \(N\). Thus the all-\(x\) kernel is not asserted to be the true resolvent from \(x\in N\).
- lines 642--725: after Proposition 3.1 they state that the absolute-continuity condition lets them pass from the stationary solution to quasi-every initial condition.
- lines 1000--1035: the continuity/nonstationary argument uses that for \(x\in N^c\), the law of \(X_\varepsilon\) is absolutely continuous with respect to \(\nu\).

So BZ proves the desired resolvent AC for the Dirichlet-form process outside an exceptional set, not for every deterministic ABLM initial condition.

## ABLM and later weak/mild papers

I rechecked the local sources from round 1:

- `papers/src_extracted/2011.13498_ABLM2024/CPAM.tex`: Theorem 2.6/2.8/2.10 give existence, uniqueness, and convergence of smooth approximations in the ABLM settings. Lines 490--496 explicitly say Dirichlet boundary conditions are not analyzed in the paper. Searches for "absolute continuity", "resolvent", "capacity", "invariant", and "strong Feller" produced no transition/resolvent AC theorem.
- `papers/src_extracted/2410.06599_ABLM2025_weak_mild/mildweak_v2_space.tex`: Theorem 2.10 proves weak-regularized/mild-regularized equivalence, but the formal convention is periodic/Neumann, not Dirichlet, and there is no all-starting-point transition density or resolvent theorem.
- `papers/src_extracted/2405.13780_BM2024/weakU_final_copy.tex`: this gives weak uniqueness/convergence for singular stochastic equations in periodic/Neumann SHE settings, but no invariant-measure or transition AC result.

Grothaus--Wittmann 2024/2025 extends the Mosco-convergence framework for the same non-convex BV-potential class and explicitly summarizes the BZ skew heat equation as giving weak solutions for all starting values except a capacity-zero set. It reinforces, rather than removes, the q.e. limitation.

## Positive theorems found, and why they do not apply

### 1. Strong Feller / resolvent strong Feller

FOT, p.165, defines the absolute-continuity condition as
\[
p_t(x,\cdot)\ll m,\qquad t>0,\ x\in X,
\]
and notes that it is useful for upgrading quasi-everywhere statements to everywhere ones. The same page has the standard exercise that strong Feller plus full support implies this condition.

This is exactly the reduction already in `answer.tex`: if \(P_t:B_b(E)\to C_b(E)\), or \(R_\lambda:B_b(E)\to C_b(E)\), then null-set avoidance follows for every \(x\). I found no source proving this property for the ABLM/BZ skew heat equation.

### 2. \(L^p\)-strong Feller Dirichlet-form construction

Baur--Grothaus--Stilgenbauer prove a very relevant abstract theorem, but in a locally compact finite-dimensional framework. Their Theorem 1.3 constructs a diffusion on a locally compact separable metric space \(E_1\) whose semigroup is \(L^p\)-strong Feller. Their Theorem 2.8 gives
\[
P_t(x,dy)=p_t(x,y)\,\mu(dy),\qquad x\in E_1,\ t>0.
\]
Their proof also shows directly that if \(\mu(U)=0\), then \(R_1{\bf1}_U(x)=0\) for every \(x\in E_1\).

This would close the gap if available for \(E=C_0([0,1])\). But their hypotheses use local compactness and finite-dimensional elliptic regularity. The paper's applications are elliptic diffusions on subsets of \(\mathbb R^d\), not Gaussian path-space forms.

### 3. Shin--Trutnau strict Fukushima machinery

Shin--Trutnau is useful mainly as a warning. In the introduction they say that even if the \(L^2\)-semigroup is strong Feller, a Hunt process obtained abstractly from the Dirichlet form is unique only q.e., and the absolute-continuity condition may fail at capacity-zero points. Their tools then construct Hunt processes satisfying the AC condition under explicit heat-kernel assumptions on locally compact spaces, especially distorted Brownian motions in \(\mathbb R^d\) with Muckenhoupt weights.

This is philosophically the right technology, but it is not directly applicable: \(C_0([0,1])\) is not locally compact and no comparable pointwise heat-kernel estimates for the BZ/ABLM path-space form are established there.

### 4. Kunze bounded-drift strong Feller theorem

Kunze proves that for
\[
dX=(AX+F(X))dt+G\,dW
\]
on a Banach space, bounded measurable \(F:E\to E\) preserves strong Feller under strong assumptions on the linear OU semigroup. Theorem 6.2 covers a one-dimensional Dirichlet stochastic heat equation on \(C_0(0,1)\) with bounded measurable function-valued drift \(F:C_0(0,1)\to C_0(0,1)\), yielding strong Feller and a unique invariant measure.

This applies to each fixed smooth regularization \(F_n(u)=G_{1/n}(u)\) (bounded, continuous, \(C_0\)-valued), but not uniformly in \(n\), and not to the limiting distribution-valued drift \(\delta_0(u)\). The theorem does not give a limiting strong-Feller or density estimate.

### 5. Hairer--Mattingly strong Feller for singular SPDEs

Hairer--Mattingly prove strong Feller for a broad class of regularity-structure singular SPDEs, and use it to prove uniqueness of invariant measures when a full-support invariant measure is known. But their assumptions are on the solution map in a regularity-structure model, with differentiable local nonlinearities and a nondegenerate noise coefficient \(G\). I do not see a way to encode the Nemytskii distribution \(u\mapsto \delta_0(u)\) in their framework. This is a useful analogy, not a citation for the present equation.

### 6. BV/distorted OU and stochastic quantization

Fukushima's "BV functions and distorted Ornstein Uhlenbeck processes over the abstract Wiener space" constructs quasi-regular distorted OU processes for BV densities on abstract Wiener space and gives Fukushima decompositions involving the BV surface measure. This is close in spirit but again quasi-regular/q.e.; I found no all-starting-point transition or resolvent AC theorem there.

Albeverio--Ma--Rockner emphasize the same issue in stochastic quantization: quasi-regular Dirichlet forms produce processes properly associated with the \(L^2\) semigroup, but identities and martingale problems are normally on a large invariant set, outside exceptional sets.

## Abstract Dirichlet-form question

For
\[
\pi=\rho\gamma,\qquad 0<c\le \rho\le C,\qquad
\mathcal E(F,F)=\frac12\int\|DF\|^2\,d\pi,
\]
I found no theorem saying that every properly associated continuous-path Markov process which is merely Feller has \(P_t(x,\cdot)\ll\pi\) or \(R_\lambda(x,\cdot)\ll\pi\) for every \(x\).

The obstacle is structural. Feller means \(P_t:C_b(E)\to C_b(E)\). Absolute continuity requires testing indicators of arbitrary \(\pi\)-null Borel sets. Without strong Feller, resolvent strong Feller, \(L^p\)-strong Feller, or an explicit heat kernel/capacity estimate, Feller continuity on continuous observables does not control null sets. Weak convergence from AC measures also does not preserve AC: singular measures can be weak limits of absolutely continuous ones.

The clean positive abstract statement remains:

```tex
\begin{lemma}[Sufficient \(L^p\)-strong Feller input]
Let \(m\) have full support on a Polish space \(E\), and let \(R_\lambda\)
be the resolvent of a Markov process with invariant measure \(m\).
If, for some \(p\ge1\), \(R_\lambda\) maps \(L^p(m)\) to continuous
functions on \(E\), then \(R_\lambda(x,\cdot)\ll m\) for every \(x\in E\).
\end{lemma}
\begin{proof}
If \(m(A)=0\), then \({\bf1}_A=0\) in \(L^p(m)\). Hence
\(R_\lambda{\bf1}_A\) is a continuous version of the zero \(L^p\)-class.
It has zero \(m\)-integral and, since \(m\) has full support, it must vanish
identically. Thus \(R_\lambda(x,A)=0\) for every \(x\).
\end{proof}
```

But this \(L^p\)-strong Feller hypothesis is exactly not known for the BZ/ABLM semigroup.

## Bounded-density perturbations and capacities

The bounded density \(\pi\sim\gamma\) does give useful uniform comparability:
\[
c\,\mathcal E_\gamma(F,F)\le \mathcal E_\pi(F,F)\le C\,\mathcal E_\gamma(F,F),
\qquad
c'\operatorname{Cap}_\gamma(A)\le \operatorname{Cap}_\pi(A)\le C'\operatorname{Cap}_\gamma(A).
\]
The same holds uniformly for the regularized \(\pi_n\)'s because their densities are bounded above and below uniformly.

This identifies the polar sets and gives spectral-gap/compactness information, but it does not give pointwise transition estimates. BZ's Hilbert-Schmidt estimate gives \(p_t\in L^2(\pi\otimes\pi)\), i.e. density information integrated over the starting point. It says nothing at a fixed deterministic \(x\) in a \(\pi\)-null exceptional set.

For the smooth equations, \(P_t^n(x,\cdot)\ll\pi_n\) for every \(x\), but I found no uniform estimate strong enough to pass to the limit. A naive Girsanov route degenerates: the drift \(G_{1/n}\) has size growing like \(n^{1/2}\), and the Novikov/entropy term involves
\[
\int_0^t\|G_{1/n}(u_s)\|_{L^2(0,1)}^2\,ds,
\]
whose natural expectation blows up at least on the order of \(n^{1/2}\). Any successful proof would need to exploit the bounded primitive/potential, not the drift norm.

## Suggested insertion

No unconditional LaTeX insertion closing the proof is justified by the literature I found. The most accurate insertion is a cautionary one:

```tex
\paragraph{Status of the pointwise absolute-continuity input.}
Bounebache--Zambotti, Proposition 2.5, proves an absolutely continuous
resolvent kernel for the \(L^2(\pi)\) Dirichlet-form semigroup, but the
representing identity is only \(\pi\)-a.e. in the starting point; in the proof
the kernel is extended over the exceptional set by setting it equal to zero.
Thus their result yields \(R_\lambda(x,\cdot)\ll\pi\) only outside a properly
exceptional set for the associated process. The standard Dirichlet-form
absolute-continuity condition, strong Feller property, or an \(L^p\)-strong
Feller resolvent would upgrade this to every \(x\), but no such theorem is
presently available for the Dirichlet ABLM mild/regularized semigroup with
drift \(\delta_0(u)\). Consequently the uniqueness argument below remains
conditional on the all-starting-point resolvent absolute continuity
assumption.
```

The most promising route remains the entrance lemma from round 1:
\[
P_s^P(x,N)=0,\qquad x\in C_0([0,1]),\ s>0,
\]
where \(N\) is the BZ exceptional set. A uniform \(L^p\)-density bound, a uniform capacity hitting estimate, or a strict-version theorem identifying the ABLM process with a BZ kernel satisfying the AC condition would prove it. I found no existing source that supplies any of these for this equation.
