## Referee report on the revised draft

### Overall verdict

The revised draft is clearer and more precise than the previous version, but it is **still not a complete proof** of the stated problem. It explicitly proves only a **conditional uniqueness theorem**, conditional on the unresolved pointwise smoothing/absolute-continuity property
\[
R_\lambda^P(x,\cdot)\ll \pi \qquad \text{for every deterministic }x\in C_0([0,1]).
\]
The final section itself states that this remains unproved from the hypotheses of the problem. Under the instructions, a solution with a “Remaining open issues” section and a missing essential lemma is not answer-ready.

---

## LaTeX contract check

I compiled `answer.tex` with `pdflatex` twice. It compiles successfully and produces a 5-page PDF. The document uses exactly

```latex
\documentclass[12pt]{article}
```

and uses only the permitted `fullpage` package for layout. I found no forbidden margin changes, line-spacing changes, or in-document font-size changes. Thus there is **no First Proof LaTeX contract violation**.

---

## Literature validation

The literature checks support the author’s diagnosis of the remaining gap.

- ABLM’s 2024 paper treats stochastic heat equations with distributional drift and includes \(b=\delta_0\), but the paper itself explicitly does **not** analyze Dirichlet boundary conditions; it treats \(\mathbb R\), periodic boundary conditions, and Neumann boundary conditions, while saying that Dirichlet should be adaptable but is not handled there. This is consistent with the problem statement separately assuming a Dirichlet extension. ([arxiv.org](https://arxiv.org/pdf/2011.13498))

- Bounebache–Zambotti construct a Dirichlet-form Markov solution with Gibbs invariant measure and associated Dirichlet form. Their setup indeed uses a Gibbs measure of the form
  \[
  \nu(dx)\propto \exp\!\left(-\int_0^1 f(x_r)\,dr\right)\mu(dx),
  \]
  so \(f=-2H_+\) gives the candidate \(\pi\) in the draft. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

- Bounebache–Zambotti Proposition 2.5 gives a resolvent kernel \(\rho_\lambda(x,dy)\) with \(\rho_\lambda(x,\cdot)\ll\nu\) for all \(x\), but the representation
  \[
  R_\lambda\varphi(x)=\int \varphi(y)\rho_\lambda(x,dy)
  \]
  is asserted only \(\nu\)-a.e. in \(x\). In the proof, the kernel is extended over a zero-capacity exceptional set by definition. This confirms the author’s concern that the BZ result does not automatically give the actual ABLM semigroup’s resolvent for every deterministic initial condition. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

- Bounebache–Zambotti explicitly pass from the stationary solution to quasi-every initial condition, not to every deterministic initial condition. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

- The cited 2025 ABLM weak/mild-equivalence result is relevant background, but its stated settings are \(\mathbb R\), periodic boundary conditions, and Neumann boundary conditions, not Dirichlet. ([link.springer.com](https://link.springer.com/article/10.1007/s40072-025-00392-x))

---

## Previous concerns: addressed vs. still remaining

### Addressed or improved

1. **The proof no longer falsely claims full BZ–ABLM identification.**  
   The previous version asserted that the BZ Dirichlet-form process and the ABLM semigroup coincide for all deterministic initial data. The revised draft now correctly identifies this as an unresolved issue.

2. **The candidate invariant measure is handled carefully.**  
   The definition
   \[
   \pi(dv)=Z^{-1}\exp\!\left(2\int_0^1\mathbf 1_{\{v(x)>0\}}\,dx\right)\gamma(dv)
   \]
   is correct, and the measurability and zero-occupation arguments are now included.

3. **The regularized reversible measures \(\pi_n\) and their convergence to \(\pi\) are treated more rigorously.**  
   The total-variation convergence \(\pi_n\to\pi\) is valid.

4. **The uniqueness argument is now cleanly separated from the missing smoothing input.**  
   Lemma 2 correctly proves uniqueness if one assumes pointwise resolvent absolute continuity.

5. **The strong-Feller and entrance lemmas are useful reductions.**  
   These are valid conditional tools: either strong Feller/resolvent strong Feller, or entrance from the exceptional set, would indeed imply the needed pointwise absolute continuity.

### Still unresolved

The fatal unresolved issue remains:

\[
R_\lambda^P(x,\cdot)\ll\pi
\quad\text{for every deterministic }x\in C_0([0,1]).
\]

Without this, the proof excludes invariant measures absolutely continuous with respect to \(\pi\), but it does not exclude a hypothetical invariant probability concentrated on a \(\pi\)-null exceptional set. A symmetric \(L^2(\pi)\) semigroup with a spectral gap does not by itself rule out such additional invariant measures on sets invisible to \(\pi\).

---

## Detailed mathematical audit

### 1. Problem statement and interpretation

The gradient identity
\[
\delta_0=-\frac12\frac{d}{dr}(-2H_+)
\]
has the correct sign. The Gibbs measure \(\pi\) is also the correct formal reversible candidate.

The section is honest that the proof is conditional on a pointwise smoothing input. However, because the problem asks to prove or disprove uniqueness, this already signals that the document will not be a complete solution unless the final missing input is supplied.

### 2. Consequences of the smooth approximations

The total-variation convergence \(\pi_n\to\pi\) is correct. The Brownian bridge spends zero Lebesgue time at level \(0\), so
\[
\int_0^1 B_n(v(x))\,dx\to \int_0^1\mathbf 1_{\{v(x)>0\}}\,dx
\]
for \(\gamma\)-a.e. \(v\), and dominated convergence applies.

The reversibility calculation for \(P_t^n\) is standard and essentially correct. One minor technical overstatement is the claim that the Nemytskii map \(v\mapsto G_{1/n}(v)\) is “smooth” as an \(L^2\)-map. It is bounded and Lipschitz \(L^2\to L^2\), which is enough for the SPDE; full Fréchet smoothness \(L^2\to L^2\) is more delicate and generally false for Nemytskii maps beyond first-order statements. This does not destroy the proof, but the wording should be weakened.

The invocation of the “standard gradient SPDE/Dirichlet-form theorem” is acceptable as a standard result, but a final rigorous solution should cite a precise theorem or state the needed result explicitly.

### 3. Proposition 1: invariance, symmetry, spectral gap

Under assumption (4),
\[
P_t^n\Phi(x)\to P_t\Phi(x)
\]
for every bounded continuous \(\Phi\), every \(x\), and every \(t>0\), the passage of invariance and symmetry from \((P_t^n,\pi_n)\) to \((P_t,\pi)\) is valid.

However, note that (4) is a semigroup-level strengthening of the approximation assumption. The original problem statement says weak convergence of \(u^n(t)\to u(t)\), but it is somewhat ambiguous whether this is meant uniformly for every deterministic starting point or only for a fixed initial condition. The draft explicitly assumes the stronger semigroup form, so the proof is conditional on that interpretation.

The spectral-gap passage is also basically sound: Gaussian Poincaré for \(\gamma\), uniformly bounded perturbations \(d\pi_n/d\gamma\), and reversibility give a uniform \(L^2\) exponential decay estimate, which passes to the limit for bounded continuous \(f\) and then extends by density.

### 4. Lemma 2: uniqueness from pointwise resolvent absolute continuity

This lemma is correct. If every invariant \(\eta\) satisfies \(\eta\ll\pi\), then the \(L^2(\pi)\) spectral gap and symmetry force the density \(d\eta/d\pi\) to be constant.

The truncation argument with \(h_a=h\wedge a\) is standard and valid.

### 5. Lemma 3: strong Feller or resolvent strong Feller implies (8)

This lemma is correct, provided strong Feller is meant with respect to the topology of \(E=C_0([0,1])\). Since Brownian bridge measure has full support on \(E\) and \(\pi\sim\gamma\), a nonnegative continuous function with zero \(\pi\)-integral is identically zero.

But this remains only a sufficient condition. The draft does not prove strong Feller or resolvent strong Feller for this singular SPDE. Bounebache–Zambotti themselves state that the process is not known to be strong Feller, or at least that proving it is out of reach in their framework. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

### 6. “What Bounebache–Zambotti gives”

This section is mostly accurate and is an improvement over earlier drafts. It correctly distinguishes the \(L^2(\pi)\)/quasi-everywhere Dirichlet-form information from the desired pointwise all-starting-points assertion.

One overstatement remains: the sentence saying that combining BZ with ABLM weak/mild uniqueness identifies the constructions quasi-everywhere is not fully justified as written. To make that precise, one would still need to verify that the BZ local-time solution satisfies the hypotheses of the ABLM weak/mild equivalence theorem in the Dirichlet setting, including the relevant regularity class. The cited 2025 theorem does not itself include Dirichlet boundary conditions. ([link.springer.com](https://link.springer.com/article/10.1007/s40072-025-00392-x))

This is not the main fatal issue, since the draft does not rely on this as a completed proof of all-starting-points uniqueness, but it should be toned down.

### 7. Entrance lemma

The entrance lemma is mathematically valid as a conditional reduction: if the ABLM process immediately avoids the BZ exceptional set, then the quasi-everywhere absolute-continuity information upgrades to all starting points.

A minor technical point: BZ’s Dirichlet form is naturally formulated on \(H=L^2(0,1)\), whereas the present semigroup is on \(E=C_0([0,1])\). To make the entrance statement fully rigorous, the relationship between the exceptional set \(N\subset H\) and the \(E\)-valued process must be specified.

Again, this is conditional and not a complete proof of (8).

### 8. Remaining open issues

This section is fatal for readiness. The draft explicitly says that the desired statement is proved only once an additional smoothing/absolute-continuity property is known, and that this property remains unproved from the hypotheses of the problem.

Therefore the document does not prove or disprove the original uniqueness statement.

---

## New issues introduced or made explicit in this revision

1. **The solution is now explicitly conditional.**  
   This is honest and mathematically useful, but it fails the task of giving a complete proof or disproof.

2. **The semigroup convergence assumption (4) is stronger than the original wording may provide.**  
   The proof should either justify that the problem’s approximation assumption implies (4), or explicitly state that it is adding an assumption beyond the problem.

3. **The Nemytskii smoothness claim should be weakened.**  
   Bounded Lipschitz is enough; full \(L^2\)-smoothness is not generally true.

4. **The BZ–ABLM quasi-everywhere identification is still not fully proved.**  
   It is plausible but requires verification of hypotheses, especially in the Dirichlet setting.

---

## Required fixes before acceptance

To become answer-ready, the author must remove the conditional “Remaining open issues” by proving or citing a theorem establishing at least one of the following for the actual ABLM Dirichlet semigroup:

1. pointwise resolvent absolute continuity:
   \[
   R_\lambda^P(x,\cdot)\ll\pi
   \quad\forall x\in C_0([0,1]);
   \]
2. strong Feller or resolvent strong Feller;
3. entrance into the BZ non-exceptional set:
   \[
   P_s(x,N)=0,\qquad x\in E,\ s>0;
   \]
4. strict all-starting-points identification of the ABLM semigroup with a BZ Dirichlet-form process whose resolvent kernel represents the true resolvent at every \(x\).

Without one of these, the proof establishes only conditional uniqueness, not the statement in the problem.