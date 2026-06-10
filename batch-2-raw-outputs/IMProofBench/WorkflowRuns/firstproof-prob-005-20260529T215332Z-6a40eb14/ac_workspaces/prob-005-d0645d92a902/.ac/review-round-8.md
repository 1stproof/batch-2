## Referee report on revised `answer.tex`

### Overall verdict

The revision is a significant improvement: it removes the previously false pointwise Dirichlet bridge inequality and replaces it with a more plausible \(L^2(0,1)\)-based Hardy-inequality argument. Conditional on the new Hilbert-space drift estimate, the dyadic Girsanov argument and the final invariant-measure uniqueness argument are mostly sound.

However, the proof is **still not answer-ready**. The central Lemma “Hilbert drift estimate” is not yet established rigorously enough for a complete solution. In particular:

1. The passage from the regularized estimates for \(K^n\) to the limiting drift \(K\) uses an unstated stronger approximation of the full mild decomposition, not merely the weak one-time convergence assumed in the problem.
2. The proof invokes a “Hilbert-valued stochastic sewing lemma in semigroup form” without stating it precisely, citing it, or verifying its assumptions. ABLM’s paper does contain stochastic sewing lemmas and \(V(3/4)\)-type results, but ABLM explicitly do not treat Dirichlet boundary conditions because their local nondeterminism estimate degenerates at the boundary. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))
3. A Banach-space stochastic sewing lemma does exist in the literature, but `answer.tex` neither cites it nor explains the semigroup reduction and martingale-type assumptions needed to apply it in \(H=L^2(0,1)\). ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/196312/))

Thus the revised proof still has essential gaps in the main new technical lemma.

---

## LaTeX contract check

I compile-checked the supplied `answer.tex` with `pdflatex`. After a second run, cross-references resolved and the document compiled successfully to a 6-page PDF. The file uses exactly

```latex
\documentclass[12pt]{article}
```

uses `fullpage`, and I found no prohibited margin/layout changes, line-spacing changes, or in-document font-size changes. The LaTeX contract appears satisfied.

---

## Literature cross-check

ABLM’s paper indeed proves well-posedness for stochastic heat equations with distributional drift, including measure drifts such as \(\delta_0\), using stochastic sewing methods. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf)) Their Definition 2.4 identifies the \(\mathcal V(3/4)\) condition with control of
\[
u_t-V_t-P_{t-s}(u_s-V_s),
\]
which corresponds to \(K_t-P_{t-s}K_s\) in a mild decomposition. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf)) ABLM Proposition 3.8 states that every solution with non-negative finite measure drift belongs to \(\mathcal V(3/4)\), but this is in ABLM’s non-Dirichlet setting. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf)) ABLM explicitly say they do not analyze Dirichlet boundary conditions because the uniform local nondeterminism estimate degenerates near the boundary. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))

ABLM Theorem 2.10 also gives strong approximation by smooth drifts and a \(V(3/4)\)-type estimate in their setting. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf)) But the problem statement here only explicitly assumes weak convergence of \(u^n(t)\) to \(u(t)\) at fixed times, not convergence of the full drift decomposition \(K^n\to K\).

---

## Detailed audit

### 1. Problem statement and interpretation

The setup \(E=C_0([0,1])\), \(H=L^2(0,1)\), and \(S_t\) as the Dirichlet heat semigroup is appropriate.

The author now explicitly says the proof needs only the Hilbert estimate
\[
\|K_t-S_{t-s}K_s\|_{L^2(\Omega;H)}\le C_T|t-s|^{3/4}.
\]
This is a sensible weakening of the earlier pointwise \(V(3/4)\) estimate.

However, the statement

> “the limit follows by lower semicontinuity along the ABLM approximation of the mild decomposition”

is not justified. To make this step rigorous, one needs at least joint convergence, on a common probability space or in law with sufficient tightness, of
\[
K_t^n-S_{t-s}K_s^n
\]
to
\[
K_t-S_{t-s}K_s
\]
as \(H\)-valued random variables. The problem statement only explicitly assumes weak convergence of \(u^n(t)\) to \(u(t)\) for fixed \(t\). That does not imply convergence of the drift components \(K^n\), since \(K^n\) also involves the driving noise and the mild decomposition.

This is an essential missing assumption or missing proof.

### 2. Hilbert drift estimate

The new Hardy-based idea is much better than the previous pointwise bridge inequality. The bound
\[
\|\rho_\tau^{-1}S_\tau f\|_2\lesssim \tau^{-1/2}\|f\|_2
\]
is plausible: \(\rho_\tau^{-1}\lesssim \tau^{-1/2}+d^{-1}\), and Hardy’s inequality plus the heat-gradient estimate gives the \(d^{-1}\) part.

The moment estimate for \(A^n_{s,t}\) is also plausible. The sequential conditioning argument using the fact that \(b_n\) is a probability density is standard in this context.

But the proof still compresses several essential steps:

- The “Hilbert-valued stochastic sewing lemma in semigroup form” is not stated or cited. ABLM state stochastic sewing lemmas for their setting, and Lê has a Banach-space stochastic sewing paper, but `answer.tex` does not cite the latter or verify the assumptions needed for \(H\)-valued increments. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))
- The semigroup version is not written out. One expects to reduce it to ordinary sewing by fixing a terminal time \(T\) and applying ordinary sewing to \(S_{T-t}A_{s,t}\), but this reduction is not shown.
- The displayed derivative estimate
  \[
  \left|\mathbb E_u\{b_n(Z_r(y))-b_n(Z_r(y)+h(y))\}\right|
      \le C\rho_{r-u}(y)^{-1}h(y)
  \]
  is false as written when \(h(y)<0\). It should have \(|h(y)|\) on the right. This is fixable, but currently the displayed inequality is incorrect.
- The proof that \(D^n\) is the semigroup-sewn integral of \(A^n\) is summarized as “immediate.” For fixed \(n\) this is believable, but a complete proof should show convergence of the Riemann sums in the topology needed by the sewing lemma.

The Hilbert estimate may well be true, but as written it is not a complete rigorous proof.

### 3. Reversible Gibbs measure

This section is essentially sound.

The Gibbs measure
\[
\pi(dv)=Z^{-1}\exp\left(2\int_0^1\mathbf 1_{\{v(r)>0\}}\,dr\right)\gamma(dv)
\]
has the correct formal sign and factor for drift \(+\delta_0\).

The total-variation convergence \(\pi_n\to\pi\) is valid, using that Brownian bridge paths spend zero Lebesgue time at zero.

The regularized reversibility argument is standard for smooth bounded gradient drifts. It remains somewhat terse, but the identification of the SPDE semigroup with the symmetric Dirichlet-form semigroup is a standard result and is not the main problem.

### 4. Spectral gap and passage to the limit

The passage of invariance, reversibility, and the uniform spectral gap from \((P_t^n,\pi_n)\) to \((P_t,\pi)\) is mostly correct, assuming the pointwise convergence \(P_t^n\Phi(x)\to P_t\Phi(x)\) for bounded continuous \(\Phi\).

The Holley–Stroock perturbation argument is appropriate because \(d\pi_n/d\gamma\) is bounded above and below uniformly in \(n\).

This section no longer contains a serious gap.

### 5. Fixed-time absolute continuity

Conditional on the Hilbert drift estimate, the dyadic adapted-control construction is sound:

- The dyadic increments \(D_k=K_{r_{k+1}}-S_{\Delta_k}K_{r_k}\) satisfy the needed \(L^2(\Omega;H)\) estimate.
- The adapted control \(F\) has finite energy.
- The telescoping identity reproduces \(K_t\) at the terminal time.
- Localized Hilbert-space Girsanov then gives absolute continuity relative to the Ornstein–Uhlenbeck terminal law.
- Feldman–Hájek gives equivalence of the OU terminal law and Brownian bridge measure.

This section is now much clearer than in earlier versions. Its validity still depends entirely on the unresolved Hilbert drift estimate for the limiting singular equation.

### 6. Final uniqueness argument

Assuming fixed-time absolute continuity and the spectral gap, the uniqueness argument is essentially correct.

The monotone-class extension of detailed balance to bounded Borel functions is now explicitly mentioned. The truncation argument with \(h_a=h\wedge a\) is valid.

---

## Summary of previous concerns

### Addressed

- The previously false pointwise boundary bridge inequality has been removed.
- The Girsanov/state-space absolute-continuity argument is now much more explicit.
- The \(L^1\)-density argument in the final uniqueness proof is now included.
- The reversible Gibbs measure and spectral-gap passage are better formulated.

### Still unresolved

- The Dirichlet \(V(3/4)\)-type input remains the central issue, now in Hilbert form.
- The passage from \(K^n\) to \(K\) requires stronger convergence of the mild decomposition than the problem explicitly assumes.
- The stochastic sewing step is invoked in a form not stated, not cited in the bibliography, and not fully verified.

### New issues introduced

- The displayed derivative estimate in the Hilbert sewing-defect argument has the wrong sign/absolute-value form.
- The proof now depends on a Banach/Hilbert-valued stochastic sewing result, but the bibliography still contains no reference to Lê’s Banach-space stochastic sewing paper.

---

## Final verdict

The proof is close in overall strategy, but `answer.tex` does not yet provide a complete rigorous solution. The main technical lemma remains insufficiently justified, and the limit passage from regularized drift estimates to the singular limiting drift is not established under the stated assumptions.