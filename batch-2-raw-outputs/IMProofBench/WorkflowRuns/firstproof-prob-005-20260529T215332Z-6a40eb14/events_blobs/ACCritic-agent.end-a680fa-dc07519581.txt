## Referee report on `answer.tex`

### Overall verdict

The proposed proof is promising and contains a clever dyadic adapted-control argument, but I do **not** regard it as a complete rigorous solution under the stated problem assumptions. The main obstruction is that the proof’s key fixed-time absolute-continuity lemma depends on the estimate labelled **(B)**, a \(V(3/4)\)-type drift regularity estimate for the **Dirichlet** problem. ABLM do prove the corresponding \(V(3/4)\) statement for finite non-negative measure drifts in their covered settings, and their definition of \(\mathcal V(\kappa)\) matches the drift-increment estimate used in the draft. However, ABLM explicitly state that they do **not** treat Dirichlet boundary conditions, and explain that the relevant local nondeterminism degenerates near the boundary. The problem statement assumes extension of existence, uniqueness, and approximation results to Dirichlet, but it does not explicitly assume the \(V(3/4)\) drift estimate. Since (B) is essential to the proof and is not proved in `answer.tex`, this is a material gap. ABLM’s definition of \(\mathcal V(\kappa)\), the relation to \(K_t-P_{t-s}K_s\), and Proposition 3.8 are as the author says, but only in ABLM’s stated settings; ABLM also explicitly exclude Dirichlet from their paper. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))

### LaTeX contract check

I compiled `answer.tex` with `pdflatex` twice. It compiles successfully and produces a 4-page PDF. The document uses exactly `\documentclass[12pt]{article}`, uses `fullpage`, and I did not find prohibited margin/layout packages, line-spacing changes, or explicit in-document font-size changes. The LaTeX contract appears satisfied.

### Literature cross-check

- ABLM indeed study stochastic heat equations with generalized/distributional drift, including measure drifts and \(b=\delta_0\), and prove strong well-posedness in their framework. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))
- ABLM’s class \(\mathcal V(\kappa)\) is defined through the quantity
  \[
  u_t-V_t-P_{t-s}(u_s-V_s),
  \]
  which, for a mild decomposition \(u_t=P_tu_0+K_t+V_t\), becomes \(K_t-P_{t-s}K_s\). This validates the author’s interpretation of (B) in ABLM notation. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))
- ABLM Proposition 3.8 states that every solution with non-negative finite measure drift belongs to \(\mathcal V(3/4)\), but again this is in their non-Dirichlet settings. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))
- Bounebache–Zambotti’s paper is correctly described as involving a singular/local-time SPDE with an explicit Gibbs-type invariant measure and a Dirichlet-form construction. ([ideas.repec.org](https://ideas.repec.org/a/spr/jotpro/v27y2014i1d10.1007_s10959-012-0421-8.html))

## Paragraph-by-paragraph mathematical audit

### 1. “Problem statement and interpretation”

The setup \(E=C_0([0,1])\), \(H=L^2(0,1)\), and \(S_t\) as the Dirichlet heat semigroup is appropriate.

The semigroup convergence assumption (A) is a reasonable reformulation of weak convergence of \(u^n(t)\) to \(u(t)\), provided this convergence is meant for every deterministic initial condition \(x\in E\) and every bounded continuous observable. This should be stated explicitly, but it is not a serious issue.

The major issue is the additional estimate (B). The proof later relies crucially on
\[
\|K_t(r)-S_{t-s}K_s(r)\|_{L^m}=O(|t-s|^{3/4})
\]
uniformly in \(r\in[0,1]\). This is not among the assumptions stated in the problem. It is true in ABLM’s settings for non-negative finite measure drift, but ABLM explicitly do not treat Dirichlet boundary conditions, and they point out that an ingredient used in their arguments degenerates near the Dirichlet boundary. Thus `answer.tex` either needs to prove the Dirichlet version of (B), or the problem statement must explicitly include it as an assumption. Merely saying “I shall also use” it is not enough for a rigorous solution.

### 2. “The reversible Gibbs measure”

The proposed Gibbs measure
\[
\pi(dv)=Z^{-1}\exp\left(2\int_0^1{\bf1}_{\{v(r)>0\}}\,dr\right)\gamma(dv)
\]
has the correct formal sign and factor for drift \(+\delta_0\), because the symmetric perturbation of the OU generator by a potential \(\Phi(v)=\int B(v(r))\,dr\) gives drift \(+\nabla\Phi\) when the density is \(e^{2\Phi}\,d\gamma\).

The convergence \(\pi_n\to\pi\) in total variation is essentially correct: \(B_n\to{\bf1}_{(0,\infty)}\) away from zero, and Brownian bridge paths spend zero Lebesgue time at zero. This last fact is standard and can be justified by Fubini from non-atomic one-point marginals in the interior.

The integration-by-parts computation for \(L_n\) is formally correct. However, the line “standard variational/mild theory … therefore gives \(P_t^n\) is \(\pi_n\)-invariant and reversible” compresses a nontrivial identification: one must know that the mild SPDE semigroup with bounded smooth reaction drift is the Markov semigroup associated with the symmetric Dirichlet form generated by that integration-by-parts formula. This is standard, but the proof should cite or state it more precisely.

### 3. Proposition on invariance, reversibility, and spectral gap

The passage of invariance and symmetry from \((P_t^n,\pi_n)\) to \((P_t,\pi)\) is basically valid, assuming (A) and total-variation convergence of \(\pi_n\). The bounded-convergence argument works after decomposing the varying-measure integrals.

The uniform Poincaré inequality for \(\pi_n\) via Holley–Stroock is also correct: the densities \(d\pi_n/d\gamma\) are bounded above and below uniformly in \(n\).

The passage of the spectral-gap inequality to the limit is plausible. However, the proof should be slightly more explicit about the functional-analytic step: the exponential decay for \(P_t^n\) follows from the closed symmetric Dirichlet form plus Poincaré inequality, not merely from reversibility alone. This is fillable and not the main fatal gap.

### 4. “Fixed-time absolute continuity”

This is the most important section.

The dyadic construction itself is elegant and, conditional on (B), mostly correct:

- \(D_k=K_{r_{k+1}}-S_{\Delta_k}K_{r_k}\) is adapted at time \(r_{k+1}\).
- The estimate
  \[
  \mathbb E\|D_k\|_H^2\lesssim \Delta_k^{3/2}
  \]
  follows from (B).
- The control
  \[
  F_s=\sum_{k\ge0}{\bf1}_{(r_{k+1},r_{k+2}]}(s)\Delta_{k+1}^{-1}S_{s-r_{k+1}}D_k
  \]
  is predictable/adapted and has finite \(L^2([0,t];H)\)-energy.
- The telescoping identity reproducing \(K_t\) at the terminal time is algebraically correct.

But several technical details are missing:

1. **Unproved Dirichlet \(V(3/4)\) estimate.** This is the fatal issue. Without (B), the entire absolute-continuity lemma collapses.

2. **State-space issue in Girsanov.** The argument naturally gives absolute continuity of terminal laws in an \(H\)-valued or path-space formulation. Since the desired law is on \(E=C_0([0,1])\), the proof should explicitly explain why the \(H\)-law absolute continuity transfers to the \(E\)-Borel law. This can likely be fixed using the continuous injection \(E\hookrightarrow H\) and the fact that the Gaussian laws are supported on \(E\), but it is not written.

3. **Controlled convolution regularity.** For general \(F\in L^2([0,t];H)\), the controlled convolution is naturally \(H\)-valued; it is not automatically a continuous spatial function. Since the proof only needs terminal equality with \(u_t\), this is probably manageable, but again the state-space formulation needs care.

4. **Weak-solution filtration.** The proof uses Girsanov with a drift \(F\) built from \(K\). This is acceptable if \(W\) is Brownian with respect to the full filtration to which \(K\) is adapted, but the proof should state this. It is not a fatal flaw, but it is a missing technical hypothesis/justification.

The Feldman–Hájek comparison of the OU one-time law with Brownian bridge measure is correct: the covariance eigenvalues are
\[
q_k(t)=\frac{1-e^{-k^2\pi^2t}}{k^2\pi^2},
\]
while Brownian bridge has eigenvalues \((k^2\pi^2)^{-1}\), and the ratios differ from \(1\) by a square-summable sequence.

### 5. “Conclusion: uniqueness”

Assuming the fixed-time absolute-continuity lemma, the uniqueness argument is essentially correct.

There is one technical omission: the proof says invariance of \(\eta\) and symmetry of \(P_t\) in \(L^2(\pi)\) give \(P_t h=h\) in \(L^1(\pi)\). Since \(h=d\eta/d\pi\) need only be in \(L^1\), this requires extending the symmetry/detailed-balance identity from bounded continuous functions to bounded Borel functions and then to \(L^1\) densities. This can be done by a monotone-class argument once one has a genuine transition kernel and detailed balance, but it is not written.

The truncation argument with \(h_a=h\wedge a\), Jensen’s inequality, and the spectral gap is correct once \(P_t h=h\) is justified.

## Main issues requiring correction

1. **Essential missing proof/assumption:** the Dirichlet-boundary version of ABLM’s \(V(3/4)\) estimate (B). This is the central gap.
2. **Girsanov/state-space rigor:** the proof should carefully formulate the Hilbert-space Girsanov step and explain transfer of absolute continuity to the \(E=C_0\) state space.
3. **Extension of symmetry to \(L^1\) densities:** needed for the invariant-density argument.
4. **Identification of regularized reversible semigroups:** standard, but should be cited or stated as a theorem.

Because issue 1 is essential and not merely cosmetic, `answer.tex` is not yet a complete rigorous solution under the stated assumptions.