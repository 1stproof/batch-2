## Referee report on `answer.tex`

### 1. LaTeX contract check

I compiled `answer.tex` with `pdflatex` twice. It compiles successfully, resolves references on the second pass, and produces a **7-page** PDF. The document uses exactly `\documentclass[12pt]{article}`, uses `fullpage`, and I did not find forbidden margin, spacing, or in-document font-size changes. So I find **no First Proof LaTeX contract violation**.

### 2. Literature validation

The bibliographic data for the main cited ABLM paper is accurate: it appears as *Communications on Pure and Applied Mathematics* 77(5), 2708–2777, 2024, and its abstract confirms treatment of stochastic heat equations with distributional drifts including measure drifts such as \(b=\delta_0\). ([cris.technion.ac.il](https://cris.technion.ac.il/en/publications/well-posedness-of-stochastic-heat-equationwith-distributional-dri/)) The cited K. Lê stochastic sewing paper is also real and appears as EJP 28, article 26, 2023. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/196312/)) Bounebache–Zambotti’s “A skew stochastic heat equation” is also correctly identified; its abstract confirms an explicit Gibbs invariant measure and Dirichlet-form Markov construction. ([arxiv.org](https://arxiv.org/abs/1105.2779))

However, these sources do **not** directly validate several new technical steps in `answer.tex`, especially the all-starting-point fixed-time absolute continuity and the Dirichlet-boundary uniform \(3/4\)-drift estimate. Those are essentially proved from scratch in the answer and must stand on their own.

---

## 3. Mathematical audit

### A. “Problem statement and interpretation”

The answer correctly records an interpretation of the weak convergence assumption as
\[
P_t^n\Phi(x)\to P_t\Phi(x),\qquad \Phi\in C_b(E),\ x\in E,\ t>0.
\]
This is a reasonable strengthening/clarification of the problem’s “weakly” language. But it should be noted that the original statement phrases convergence as \(u^n(t)\to u(t)\) weakly and does not explicitly quantify over all deterministic initial states \(x\). The proof later needs convergence for every \(x\in E\), not merely for one fixed initial condition. The “Problem statement and interpretation” section should explicitly state that this is an adopted assumption, not “exactly” the original wording.

### B. Lemma 1: uniform estimate on the regularized drift

This lemma is central to the whole proof. It is also the most technically delicate part.

The heat-kernel estimates (3)–(6) are plausible, but they are not proved at the level needed for a standalone solution. In particular:

- The diagonal estimate for the Dirichlet kernel and the consequence
  \[
  \rho_\tau(y)\asymp \sqrt{\tau}\wedge d(y)
  \]
  are stated with only a brief explanation. A complete proof should specify the range of \(\tau\), how constants depend on \(T\), and handle both boundary and interior regimes carefully.

- The weighted estimate
  \[
  \sup_z\int_0^1p_a(z,y)\rho_\tau(y)^{-1/2}\,dy
  \le C(a^{-1/4}+\tau^{-1/4})
  \]
  is sketched but not fully justified for all boundary configurations. It is likely true, but the proof is compressed.

- The Hardy inequality step in (6) is plausible, but the proof should explicitly verify \(S_\tau f\in H^1_0\) and track the Dirichlet generator normalization.

The stochastic estimate for the frozen increment \(A^n_{s,t}\) is also only partially justified. The conditional Gaussian estimate (9) is plausible, but a complete proof needs to spell out the conditional law of
\[
Z_q(z)\mid \mathcal F_r
\]
and show that the future variance is indeed bounded below by the stated \(\rho_{q-r}(z)\), uniformly near the boundary.

The passage from (10) and (11) to the sewing bound has several missing details:

- The sewing lemma is stated with conditional expectations \(\mathbb E_a\delta A_{a,u,b}\), but the derived estimate (11) is for \(\mathbb E_u\delta A_{s,u,t}\). This can likely be repaired by the tower property and Jensen, but the answer does not say so.

- The “centered bound \(C(b-a)^{3/4}\)” is asserted from (10), but \(\delta A\) contains three terms. One needs to show explicitly that
  \[
  \|\delta A_{a,u,b}-\mathbb E_a\delta A_{a,u,b}\|_{L^2H}
  \lesssim (b-a)^{3/4}
  \]
  uniformly in \(n\).

- The identification of the sewn limit with \(D^n_{s,t}\) depends on (8), but (8) is proved only by a fixed-\(n\) error estimate. That is probably enough, but the proof should explicitly connect the dyadic sewing limit with the arbitrary-partition convergence.

- The final bootstrap
  \[
  Y_n(h)\le C+Ch^{1/2}Y_n(h)
  \]
  is plausible, but the constants and the extension from small to arbitrary intervals are not fully written. Since this estimate is later used to obtain uniform entropy bounds independent of \(n\), this is an essential gap unless expanded.

Verdict on Lemma 1: the strategy is promising, but the proof is too compressed to certify as a complete rigorous proof of the key uniform estimate.

### C. Reversible reference measure and spectral gap

The definition
\[
\pi(dv)=Z^{-1}e^{2\int_0^1\mathbf1_{\{v(r)>0\}}dr}\,\gamma(dv)
\]
is natural and the total variation convergence \(\pi_n\to\pi\) is plausible, using bounded convergence and the fact that Brownian bridge spends zero Lebesgue time at a fixed level.

The Galerkin proof of reversibility for \(P_t^n\) is plausible but not complete. Specific issues:

1. The proof says \(u_t^{n,m}\to u_t^n\) in probability in \(E\) and gives only a sketch. This convergence is essential for passing reversibility and spectral gap from \(P^{n,m}\) to \(P^n\).

2. The claim that the contribution over \([t-\varepsilon,t]\) is “uniformly small because \(b_n\) is bounded” is not literally sufficient for the projected drift \(\Pi_m b_n(\Pi_m u)\), since \(\Pi_m\) is not an \(L^\infty\)-contraction. One can probably fix this using \(L^2\to C\) heat smoothing and \(L^2\)-boundedness of \(\Pi_m\), but the answer does not provide that argument.

3. The Holley–Stroock perturbation argument is invoked without spelling out the relevant Dirichlet form, domain, and Gaussian Poincaré inequality with the \(H=L^2\)-gradient. This is standard but still needed in a rigorous solution because it supplies the uniform spectral gap.

4. Passing (16) from \(m\) to \(\infty\), and then from \(n\) to \(\infty\), requires careful dominated-convergence arguments with changing measures. The answer indicates the idea but does not fully verify it.

The proposition passing invariance, symmetry, and spectral gap to the limiting \(P_t\) is structurally correct if all previous convergence statements are valid. But because Lemma 2 is not fully justified, Proposition 3 is not fully established.

### D. Fixed-time absolute continuity

This is the other essential part of the proof. The dyadic adapted-control idea is clever and likely the intended way to avoid exceptional-set issues. However, several steps require more precision.

The telescoping identity
\[
\int_0^t S_{t-s}F_s^n\,ds=K_t^n
\]
is plausible, but it should be written as a limit of finite sums and should explicitly use \(H\)-continuity of \(K^n_t\). As written, equality of an infinite series is asserted without proof.

The entropy/Girsanov step is a major technical point. The answer states a “standard Girsanov theorem on \(C([0,t];U)\)” and then applies data processing. This is not enough for a complete standalone proof, because:

- The driving noise is cylindrical in \(H\), realized in a larger space \(U=H^{-\beta}\). One must specify the exact Cameron–Martin space, filtration, and sign convention.

- The terminal stochastic convolution is not a naive continuous deterministic functional of an arbitrary \(U\)-valued path. A rigorous data-processing argument should be formulated either at the level of the full stochastic convolution process or via a canonical measurable construction.

- The entropy inequality
  \[
  \operatorname{Ent}(\Law(X_N)\mid\nu_t^x)
  \le \frac12\E\int_0^t\|F_s^{n,N}\|_2^2\,ds
  \]
  is standard but nontrivial in this infinite-dimensional adapted setting. It needs a precise theorem or proof.

The lower semicontinuity step from \(P_t^n(x,\cdot)\) to \(P_t(x,\cdot)\) is valid assuming the stated weak convergence and the uniform entropy bound. The Feldman–Hájek comparison between \(\nu_t^x\) and \(\gamma\) is also essentially correct: the covariance eigenvalues differ by square-summable ratios, and \(S_t x\) lies in the Cameron–Martin space. But the fixed-time absolute continuity lemma depends critically on the previous unfilled Girsanov/control details.

### E. Final uniqueness argument

The final argument is sound **provided** the two major inputs are established:

1. \(P_t(x,\cdot)\ll\pi\) for every deterministic \(x\) and every \(t>0\);
2. \(P_t\) is reversible with a genuine \(L^2(\pi)\) spectral gap.

Given those, the proof that every invariant \(\eta\) satisfies \(\eta\ll\pi\), then \(d\eta/d\pi=h\), then \(P_t h=h\), and finally \(h\equiv1\) by truncation and the spectral gap is correct. The Jensen/concavity inequality is in the correct direction:
\[
P_t(h\wedge a)\le (P_t h)\wedge a.
\]

So the conclusion is logically fine, but it rests on earlier technical results that are not rigorously established in the submitted text.

---

## 4. Overall verdict

The LaTeX contract is satisfied. The bibliography is broadly accurate. The proof strategy is coherent and may be repairable.

However, `answer.tex` is **not yet a complete rigorous solution**. The two essential pillars — the uniform Dirichlet-boundary \(3/4\)-drift estimate and the all-starting-point fixed-time absolute continuity via adapted Girsanov control — contain substantial compressed arguments and unstated technical assumptions. The Galerkin reversibility/spectral-gap passage also needs more detail. These are not cosmetic omissions; they are essential to the validity of the uniqueness proof.

Therefore I cannot certify the answer as answer-ready.