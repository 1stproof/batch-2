## Strict referee report

### Overall verdict

The LaTeX file **passes the formal LaTeX contract**, but the mathematical solution is **not answer-ready**. The proof is a plausible conditional strategy, but it relies on an essential unproved identification between the ABLM Markov semigroup and the Bounebache–Zambotti Dirichlet-form process, and it also uses a pointwise absolute-continuity property for the resolvent that is not established for the semigroup \(P_t\) in the problem. These are not cosmetic gaps: they are central to the uniqueness argument.

### Literature and contract checks

- The bibliographic data for ABLM and Bounebache–Zambotti are essentially correct. ABLM’s paper treats distributional drifts including \(b=\delta_0\), but explicitly notes that the paper itself does **not** analyze Dirichlet boundary conditions; the problem statement separately assumes such an extension. ([arxiv.org](https://arxiv.org/pdf/2011.13498))  
- ABLM’s solution notion is a specific mild/construction notion requiring a decomposition \(u=P_tu_0+K+V\) and convergence of smooth drift approximations in the mild drift term. ([arxiv.org](https://arxiv.org/pdf/2011.13498))  
- Bounebache–Zambotti do construct a Dirichlet-form Markov solution for a skew heat equation with bounded-variation potential, with Gibbs-type invariant measure and an absolute-continuity resolvent statement. ([arxiv.org](https://arxiv.org/pdf/1105.2779))  
- I compiled `answer.tex` with `pdflatex`: it compiled successfully after the normal rerun, produced a 3-page PDF, uses exactly `\documentclass[12pt]{article}`, uses only the permitted `fullpage` package for layout, and contains no forbidden font-size or spacing changes. No LaTeX-contract violation was found.

---

## Paragraph-by-paragraph mathematical audit

### 1. “Problem statement and interpretation”

The distributional identity
\[
\delta_0=-\frac12\frac{d}{dr}(-2H_+)
\]
is correct, with the usual convention that \(H_+=\mathbf 1_{\{r>0\}}\). The sign of the proposed Gibbs density
\[
\pi(dv)\propto \exp\!\left(2\int_0^1\mathbf 1_{\{v(x)>0\}}\,dx\right)\gamma(dv)
\]
is also consistent with the regularized drift \(G_{1/n}=B_n'\).

However, the sentence saying that the Bounebache–Zambotti Dirichlet-form construction “gives a Markov solution with the same regularising approximations” and hence, by ABLM uniqueness, “is the same semigroup as \(P_t\)” is a major unproved assertion. Bounebache–Zambotti prove a weak/local-time Dirichlet-form solution and convergence of stationary regularized processes, not the full ABLM mild-solution identification for every deterministic initial condition in \(C_0([0,1])\). Their convergence statement is explicitly for stationary solutions. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

This is a fatal gap because the rest of the proof needs symmetry and resolvent absolute continuity for the actual semigroup \(P_t\), not merely for a possibly different Dirichlet-form process.

### 2. Definition of \(\pi\)

The construction of
\[
\Lambda(v)=\int_0^1 H_+(v(x))\,dx,\qquad
\pi(dv)=Z^{-1}e^{2\Lambda(v)}\gamma(dv)
\]
is fine. The density is bounded above and below because \(0\le \Lambda\le1\). The argument that the value of \(H_+(0)\) is \(\gamma\)-irrelevant is also correct: a Brownian bridge spends zero Lebesgue time at any fixed level almost surely.

Minor omission: the proof does not explicitly state measurability of \(v\mapsto\Lambda(v)\), but this is standard and easily repaired.

### 3. Lemma 1: reversibility and absolute continuity

This is the central weak point of the solution.

Bounebache–Zambotti do prove an absolute-continuity property for the resolvent of their Dirichlet-form semigroup. Their Proposition 2.5 states that there is a kernel \(\rho_\lambda(x,dy)\) representing the \(L^2(\nu)\)-resolvent \(\nu\)-a.e. and satisfying \(\rho_\lambda(x,\cdot)\ll\nu\). ([arxiv.org](https://arxiv.org/pdf/1105.2779)) But in Dirichlet-form theory, these objects are initially only specified up to exceptional sets, and the associated Fukushima decomposition is also stated for all starting points outside an exceptional set. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

The answer needs the much stronger statement
\[
R_\lambda^{P}(x,\cdot)\ll \pi\qquad\text{for every }x\in C_0([0,1]),
\]
where \(R_\lambda^{P}\) is the resolvent of the ABLM semigroup \(P_t\). That pointwise statement is not proved. This matters because the abstract uniqueness proof uses it to show that **every** invariant measure \(\eta\) satisfies \(\eta\ll\pi\). If absolute continuity were known only \(\pi\)-a.e. or only quasi-everywhere, an invariant measure could in principle charge an exceptional set, and the argument would fail.

### 4. Proof of Lemma 1: regularized equations

The formal calculation for the regularized generator and invariant measure \(\pi_n\) is essentially correct for smooth cylinder functions:
\[
\pi_n(dv)\propto \exp\!\left(2\int_0^1 B_n(v(x))\,dx\right)\gamma(dv).
\]
The convergence \(\pi_n\Rightarrow\pi\) follows from dominated convergence, indeed even in total variation after normalizing constants are handled.

However, this paragraph alone does not prove that \(\pi\) is invariant for the limiting ABLM semigroup \(P_t\). To pass invariance from \(\pi_n\) to \(\pi\), one would need a convergence theorem strong enough to handle initial distributions \(\pi_n\to\pi\), not merely pointwise weak convergence from fixed initial data. The answer instead switches to Bounebache–Zambotti, but then the identification issue above becomes essential.

### 5. Proof of Lemma 1: Dirichlet-form invocation

The use of Bounebache–Zambotti with \(f=-2H_+\) is natural and the sign is consistent: for smooth \(f_n=-2B_n\), the drift is
\[
-\frac12 f_n'(u)=G_{1/n}(u).
\]

But the proof says, without sufficient justification, that the Fukushima decomposition “is the weak form” of the ABLM SPDE and that weak uniqueness identifies the two processes. This is not enough. ABLM’s solution notion is a mild/construction definition involving convergence of regularized drift terms. ([arxiv.org](https://arxiv.org/pdf/2011.13498)) Bounebache–Zambotti’s process is formulated through a local-time weak equation and Dirichlet forms. ([arxiv.org](https://arxiv.org/pdf/1105.2779)) The answer must prove equivalence of these notions in this Dirichlet setting, or cite a theorem that does exactly this. It does neither.

This is a fatal missing lemma.

### 6. Lemma 2: abstract ergodic criterion

The abstract criterion is mostly correct, assuming its hypotheses really hold.

Minor details that should be expanded in a rigorous write-up:

- Symmetry on \(L^2(\pi)\) must be extended carefully to the \(L^1\)-duality argument for \(h=d\eta/d\pi\).
- The equality \(P_t h=h\) in \(L^1(\pi)\) should be derived by testing against bounded functions and using \(L^1\)-\(L^\infty\) duality.
- The final step “\(h\wedge a\) constant for all \(a\) implies \(h\) constant” is true but should be written out.

These are repairable and not the main problem. The main problem is that hypothesis (3), pointwise resolvent absolute continuity for the actual \(P_t\), has not been proved.

### 7. Spectral gap paragraph

The spectral-gap argument is mathematically sound **for the symmetric Dirichlet-form semigroup associated with \(\mathcal E\)**. The Brownian bridge Gaussian Poincaré inequality plus bounded perturbation of measure gives
\[
\operatorname{Var}_\pi(F)\le C\mathcal E(F,F).
\]
The factor \(1/2\) in the definition of \(\mathcal E\) only changes constants.

But this proves a spectral gap only after one has already shown that \(P_t\) is the semigroup associated with that symmetric form. Since Lemma 1’s identification is not established, the spectral gap is not proved for the semigroup \(P_t\) from the problem.

### 8. Final conclusion

The conclusion that every invariant probability measure equals \(\pi\) follows from the stated lemmas, but the crucial Lemma 1 is not rigorously established for the actual ABLM semigroup. The proof is therefore conditional on an additional strong theorem:

> The ABLM Dirichlet mild solution with drift \(\delta_0\) coincides, for every initial condition in \(C_0([0,1])\), with the Bounebache–Zambotti Dirichlet-form process for \(f=-2H_+\), and its resolvent kernels are pointwise absolutely continuous with respect to \(\pi\).

That theorem is neither proved nor cited in the answer.

---

## Required fixes before answer can be accepted

To make the solution answer-ready, the author must add a rigorous proof or precise citation establishing all of the following:

1. The Bounebache–Zambotti local-time/Dirichlet-form solution with \(f=-2H_+\) is an ABLM mild solution in the problem’s sense.
2. The identification holds for every deterministic initial condition \(u_0\in C_0([0,1])\), not only \(\pi\)-a.e. or quasi-everywhere.
3. The resolvent of the actual \(P_t\) satisfies \(R_\lambda(x,\cdot)\ll\pi\) for every \(x\in C_0([0,1])\).
4. The symmetry and spectral gap are properties of the actual \(P_t\), not merely of a related \(L^2(\pi)\)-Dirichlet-form semigroup.

Without these additions, the proof does not fully solve the problem.