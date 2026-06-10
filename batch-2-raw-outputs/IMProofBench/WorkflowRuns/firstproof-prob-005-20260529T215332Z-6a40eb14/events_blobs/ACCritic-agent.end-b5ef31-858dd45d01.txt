## Referee report on `answer.tex`

### LaTeX contract audit

I compiled `answer.tex` with `pdflatex` twice. It compiles successfully, resolves references on the second run, and produces an 8-page PDF. The document uses exactly `\documentclass[12pt]{article}`, uses the permitted `fullpage` package, and I found no prohibited margin/layout changes, line-spacing changes, or in-document font-size changes. The auxiliary `references.bib` is unused but harmless because `answer.tex` is standalone.

### Literature cross-check

The cited ABLM paper indeed studies stochastic heat equations with distributional drift, including measure drifts such as \(b=\delta_0\), and uses stochastic sewing methods. Its published setup covers \(D=\mathbb R\), periodic \([0,1]\), and Neumann \([0,1]\), and explicitly says Dirichlet boundary conditions are not analyzed there; thus the problem’s extra assumption that ABLM results extend to the Dirichlet case is essential, and `answer.tex` correctly records its adopted interpretation. ([arxiv.org](https://arxiv.org/abs/2011.13498))

The answer’s use of approximation/stability ideas is consistent with ABLM’s Theorem 2.10, which states convergence of smooth-drift solutions and a \(V(3/4)\)-type estimate in the non-Dirichlet settings. The answer does not simply cite this for Dirichlet; it supplies a separate Dirichlet \(L^2\)-estimate, which is appropriate. ([archive.wias-berlin.de](https://archive.wias-berlin.de/servlets/MCRFileNodeServlet/wias_derivate_00003518/2011.13498.pdf))

The stochastic sewing references are correctly identified: Lê 2020 introduces a stochastic sewing lemma giving convergence in moments of adapted random Riemann sums, and Lê 2023 extends stochastic sewing to Banach-valued processes. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/198430/)) The Bounebache–Zambotti citation is also consistent with the background: their paper studies a skew stochastic heat equation with singular local-time drift, an explicit Gibbs invariant measure, and a Dirichlet-form construction. ([arxiv.org](https://arxiv.org/abs/1105.2779))

### Mathematical audit

#### Problem interpretation

The interpretation section is necessary and acceptable. The original problem statement’s weak convergence assumption is slightly ambiguous: it could mean convergence only for one fixed initial condition, but uniqueness of invariant measures for a Markov semigroup requires convergence for all deterministic starting points. The answer explicitly adopts the stronger semigroup-level interpretation
\[
P_t^n\Phi(x)\to P_t\Phi(x),\qquad x\in C_0([0,1]),\ t>0,\ \Phi\in C_b(E),
\]
and then uses exactly that. This is not a hidden assumption; it is stated.

#### Lemma 1: uniform estimate on the regularized drift

This is the most technical part of the proof. I checked the heat-kernel estimates, the boundary compensation via
\[
\rho_\tau(y)=\int_0^\tau p_{2r}(y,y)\,dr\asymp \sqrt{\tau}\wedge d(y),
\]
the weighted estimates (5) and (6), and the use of Hardy’s inequality. These are valid, with constants depending on \(T\). The proof correctly handles the degeneracy of the Dirichlet kernel near the boundary.

The frozen-increment argument is also sound. For fixed \(n\), the convergence of dyadic sums of \(A^n_{a,b}\) to \(D^n_{s,t}\) follows because \(b_n\) is bounded and Lipschitz, and the accumulated drift on a small interval has \(H\)-norm \(O_n(b-a)\). The Gaussian conditioning estimate (9) is valid: conditioning first at time \(r\) and then at time \(s\) gives the two density factors
\[
\rho_{r-s}(y)^{-1/2}\rho_{q-r}(z)^{-1/2}.
\]
The scaling in (10) gives \(|t-s|^{3/2}\) for the second moment, hence \(|t-s|^{3/4}\) in \(L^2(\Omega;H)\).

The conditional sewing-defect estimate (11) is justified by the Gaussian derivative bound
\[
\|(b_n*\varphi_\sigma)'\|_\infty\lesssim \sigma^{-2}
\]
uniformly in \(n\), followed by estimate (6). The dyadic stochastic sewing lemma is proved directly in the text; the martingale-orthogonality argument for the centered pieces is correct. The bootstrap
\[
Y_n(h)\le C+Ch^{1/2}Y_n(h)
\]
then gives the desired uniform estimate. I found no fatal gap in this lemma.

#### Reversible reference measure and spectral gap

The Gibbs measures
\[
\pi_n(dv)\propto \exp\!\left(2\int_0^1 B_n(v(r))\,dr\right)\gamma(dv)
\]
and
\[
\pi(dv)\propto e^{2\int_0^1{\bf1}_{\{v(r)>0\}}\,dr}\gamma(dv)
\]
are correctly normalized and have densities uniformly bounded above and below relative to Brownian bridge measure. Total variation convergence \(\pi_n\to\pi\) follows from bounded convergence and the fact that Brownian bridge spends zero Lebesgue time at level \(0\).

The finite-dimensional Galerkin/cylinder-potential argument for reversibility is valid. The factor \(2\) in the density is correct for the SPDE
\[
du=\frac12\Delta u\,dt+b_n(u)\,dt+dW.
\]
The uniform spectral gap follows from Gaussian Poincaré plus bounded perturbation. Passing \(m\to\infty\) and then \(n\to\infty\) is justified by bounded convergence and total variation convergence of the densities. The extension from \(C_b(E)\) to \(L^2(\pi)\) is standard because \(E=C_0([0,1])\) is Polish and \(C_b(E)\) is dense in \(L^2(\pi)\).

#### Fixed-time absolute continuity

The adapted-control construction is the key new idea. The dyadic definition of \(F_s^n\) is predictable because each \(D_k^n\) is known at the left endpoint \(r_{k+1}\) of the interval on which it is used. The energy estimate
\[
\E\int_0^t\|F_s^n\|_2^2\,ds<\infty
\]
follows exactly from the \(3/4\)-increment estimate. The telescoping identity reproducing \(K_t^n\) is correct.

The entropy form of Girsanov is used in the correct direction: an adapted finite-energy shift of cylindrical Brownian motion has terminal law absolutely continuous with respect to the unshifted OU terminal law, with entropy bounded by half the expected energy. The localization by \(\tau_R\), convergence in probability of the controlled terminal variable to \(u_t^n\), and lower semicontinuity of relative entropy are all valid. Passing \(n\to\infty\) by the assumed weak convergence gives
\[
P_t(x,\cdot)\ll \nu_t^x.
\]
Finally, \(\nu_t^x\sim\gamma\) by the Feldman–Hájek criterion: the covariance eigenvalue ratios are \(1-e^{-\lambda_j t}\), bounded away from \(0\), and their deviations from \(1\) are square-summable; also \(S_tx\in H_0^1\). This proves \(P_t(x,\cdot)\ll\pi\) for every deterministic \(x\) and \(t>0\).

#### Final uniqueness argument

The conclusion is rigorous. Fixed-time absolute continuity implies every invariant probability \(\eta\) is absolutely continuous with respect to \(\pi\). Writing \(d\eta=h\,d\pi\), symmetry gives \(P_t h=h\) in \(L^1(\pi)\). Truncations \(h_a=h\wedge a\) satisfy \(P_t h_a=h_a\), and the spectral gap forces each \(h_a\) to be constant. Letting \(a\to\infty\) yields \(h\equiv1\), hence \(\eta=\pi\). This proves uniqueness of the invariant probability measure.

### Overall verdict

I found no mathematical error, missing essential assumption, unresolved open issue, or LaTeX-contract violation. The proof is dense and contains several nontrivial arguments, but the essential lemmas are proved rather than merely asserted. The answer is ready.