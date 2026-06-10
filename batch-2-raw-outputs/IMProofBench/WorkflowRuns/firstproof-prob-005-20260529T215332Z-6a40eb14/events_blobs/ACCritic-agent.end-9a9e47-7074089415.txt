## Referee report on the latest revised `answer.tex`

### Overall verdict

The revision is **not answer-ready**. It no longer leaves the exceptional-set issue explicitly open; instead it attempts to close it through a new fixed-time absolute-continuity argument. However, that argument depends on a new “local-time form of the drift” proposition which is not part of the problem hypotheses and is not proved rigorously. Several claims inside that proposition are substantial new theorems, and at least some are not justified by the cited ABLM results.

The previous conditional gap has therefore not been genuinely resolved; it has been replaced by an unproved all-starting-points local-time/Girsanov regularity theorem.

---

## LaTeX contract check

I compiled the supplied `answer.tex` twice with `pdflatex`. It compiled successfully and produced a 5-page PDF. The document uses exactly

```latex
\documentclass[12pt]{article}
```

uses the permitted `fullpage` package, and I found no forbidden margin, font-size, or line-spacing changes. So the LaTeX contract is satisfied. The negative verdict is mathematical.

---

## Literature cross-check

ABLM do treat stochastic heat equations with distributional drift and include finite non-negative Radon measure drifts and \(b=\delta_0\), but their paper defines the singular drift through an auxiliary \(K\) obtained as a limit of regularized drifts, not through an all-starting-points spatial-local-time representation. ABLM also explicitly state that their main settings are \(\mathbb R\), periodic boundary, and Neumann boundary, and that Dirichlet boundary conditions were not analyzed there. The problem assumes a Dirichlet extension of existence/uniqueness/approximation, but not the additional local-time and moment estimates introduced in this draft. ([arxiv.org](https://arxiv.org/pdf/2011.13498))

Bounebache–Zambotti do construct a Dirichlet-form Markov solution with a local-time-in-space term, but their statements are quasi-everywhere/allows exceptional sets, not all deterministic starting points. Their Proposition 3.5 explicitly has an exceptional set, and their resolvent-kernel construction also proceeds through zero-capacity exceptional sets. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

Mattingly–Romito–Su is relevant background for fixed-time Girsanov/time-shift ideas, but it concerns singular stochastic Burgers equations and does not supply the local-time estimates or absolute continuity theorem claimed here for the present skew stochastic heat equation. ([arxiv.org](https://arxiv.org/abs/2104.07492))

---

## What changed relative to the previous draft

### Addressed

1. **The draft now attempts an all-starting-points absolute-continuity proof.**  
   Previously the solution ended with conditional criteria. The new version tries to prove
   \[
   P_t(x,\cdot)\ll \gamma\sim\pi
   \]
   for every deterministic \(x\) and \(t>0\).

2. **The final invariant-measure argument is logically correct if fixed-time absolute continuity is available.**  
   Once \(P_t(x,\cdot)\ll\pi\) for all \(x\), any invariant \(\eta\) satisfies \(\eta\ll\pi\), and the spectral-gap/symmetry argument forces \(\eta=\pi\).

### Still unresolved / newly introduced

1. **The new local-time Proposition \(\ref{prop:lt}\) is not proved.**
2. **The fixed-time Girsanov lemma depends entirely on that proposition.**
3. **The proposition imports assumptions not present in the problem statement.**
4. **Several technical statements in the proposition are much stronger than what is cited from ABLM.**
5. **The proof no longer honestly records the remaining gap, but the gap remains.**

---

## Detailed audit

### 1. Problem statement and interpretation

The interpretation of the approximation convergence as
\[
P_t^n\Phi(x)\to P_t\Phi(x),\qquad \Phi\in C_b(E),
\]
is acceptable and was already present in prior drafts.

However, the paragraph now adds:

> “The proof uses the local-time identification of the ABLM solution for non-negative measure drifts recalled in Proposition \(\ref{prop:lt}\) below.”

This is a major additional input. The problem statement assumes Dirichlet existence, uniqueness, and approximation convergence. It does **not** assume an all-starting-points spatial-local-time representation of the ABLM drift, nor the moment estimate later used in (7). Therefore Proposition \(\ref{prop:lt}\) must be fully proved. It is not.

---

### 2. Reversible Gibbs measure section

This part is mostly sound.

The Gibbs measure
\[
\pi(dv)=Z^{-1}e^{2\int_0^1{\bf1}_{\{v(r)>0\}}\,dr}\gamma(dv)
\]
has the correct formal sign for drift \(+\delta_0\), and \(\pi\sim\gamma\) because the density is bounded above and below.

The total variation convergence \(\pi_n\to\pi\) is correct: \(B_n\to{\bf1}_{(0,\infty)}\) away from zero, and Brownian bridge paths spend zero Lebesgue time at zero.

The regularized reversibility argument is plausible for fixed \(n\), but still uses a broad “standard variational/mild theory” citation. In a final proof this should be supported by a precise theorem. This is a secondary issue compared to the local-time/Girsanov gap.

---

### 3. Proposition \(\ref{prop:gap}\): invariant \(\pi\), symmetry, spectral gap

The proof is essentially correct under the assumed pointwise convergence (A) and the regularized reversibility.

The passage
\[
\int P_t^n f\,d\pi_n\to \int P_t f\,d\pi
\]
is justified by bounded convergence plus total variation convergence. The symmetry passage is similar.

The Poincaré/spectral-gap argument is also correct in principle: Brownian bridge measure has a Gaussian Poincaré inequality, and bounded perturbations transfer it uniformly to \(\pi_n\). Passing the variance decay to the limit is valid for bounded continuous \(f\), then by \(L^2(\pi)\)-density.

No fatal issue here, modulo the standard but uncited regularized-SPDE identification.

---

### 4. Proposition \(\ref{prop:lt}\): local-time form of the drift

This is the fatal part of the draft.

The proposition claims that for the ABLM solution started from every deterministic \(x\in E\),
\[
K_t=\int_0^t S_{t-s}\mu_s\,ds,
\]
where \(\mu_s\) is the spatial local-time measure at level \(0\) of \(r\mapsto u_s(r)\), and moreover
\[
\int_0^t\|S_{(t-s)/2}\mu_s\|_H^2\,ds<\infty
\quad\text{a.s.}
\]

This is not a routine restatement of ABLM. It is a substantial new theorem.

Specific problems:

#### 4.1 The claimed spatial regularity is not justified

The proof says ABLM random-control estimates imply that
\[
S_sx+K_s
\]
is spatially \(C^\alpha\) for every \(\alpha<1\), locally uniformly for \(s>0\). The cited ABLM estimates control the drift remainder \(K_t-P_{t-s}K_s\) in a time/heat-semigroup sense, i.e. membership in their \(V(3/4)\)-type class; they do not directly imply almost-Lipschitz spatial regularity of \(K_s\). A heat convolution against finite spatial measures would naturally suggest at best much weaker spatial regularity near the terminal time unless further estimates are supplied.

This step is essential because the proof then treats \(u_s(\cdot)\) as a Brownian semimartingale plus a zero-quadratic-variation perturbation with exponent \(>1/2\). That conclusion is not established.

#### 4.2 Existence of spatial local time for all deterministic starts and all relevant times is not proved

The draft asserts that \(r\mapsto u_s(r)\) has spatial local time satisfying the occupation formula. This is not automatic for an arbitrary continuous perturbation of a Brownian bridge. BZ prove local-time existence in their Dirichlet-form setting only in a quasi-everywhere/a.e.-in-time framework, not for the all-starting-points ABLM solution used here. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

#### 4.3 The convergence
\[
G_{1/n}(u_s(r))\,dr \Rightarrow d_rL_s^0(r)
\]
is not enough as stated

Even if the spatial local time exists for each fixed \(s\), the proof needs a predictable family \(\mu_s\), joint measurability in \((s,\omega)\), and enough integrability to pass the limit through
\[
\int_0^t S_{t-s}(\cdot)\,ds.
\]
The draft does not prove these measurability or limiting statements.

#### 4.4 The moment estimate (7) is unsupported

The proof asserts
\[
\E[\mu_s([0,1])^m]\le C_{m,T}(1+s^{-m/4}).
\]
This is a strong instantaneous local-time moment estimate. It is not stated in the problem and is not derived from ABLM in the proof. The ABLM random-control estimates are estimates for integrated regularized drift terms and increments of \(K\), not directly for the instantaneous mass
\[
\int_0^1G_{1/n}(u_s(r))\,dr
\]
uniformly in \(n\).

The sentence claiming this is “first proved uniformly” in ABLM’s random-control argument is not a proof and is not backed by a precise theorem or citation.

#### 4.5 The Dirichlet transfer is not justified

ABLM explicitly did not analyze Dirichlet boundary conditions in the cited paper; the problem assumes an extension of existence/uniqueness/approximation, but the draft now needs much more: local nondeterminism estimates near the boundary, spatial local-time construction, and the moment bound (7). Those additional extensions are not part of the stated hypotheses and are not proved.

Therefore Proposition \(\ref{prop:lt}\) remains an unproved essential lemma.

---

### 5. Lemma \(\ref{lem:girs}\): time-shifted Girsanov

The algebraic time-shift identity is correct **if** Proposition \(\ref{prop:lt}\) is available. The calculation
\[
\int_0^t S_{t-s}\widehat F_s\,ds
=
\int_0^t S_{t-r}\mu_r\,dr
\]
is fine.

The idea of using an adapted \(H\)-valued drift
\[
\widehat F_s=2{\bf1}_{[t/2,t]}(s)S_{t-s}\mu_{2s-t}
\]
is also plausible: the smoothing \(S_{t-s}\) and the inequality \(2s-t\le s\) are precisely what make the time-shift trick adapted.

But the lemma is only as good as the unproved energy estimate
\[
\int_0^t\|\widehat F_s\|_H^2ds<\infty.
\]
Since that estimate comes entirely from Proposition \(\ref{prop:lt}\), the Girsanov lemma is not established.

There are also smaller technical omissions:

- The infinite-dimensional Girsanov theorem should be stated with the underlying cylindrical Brownian motion, filtration, localization, and direction of absolute continuity made precise.
- The proof asserts path-law absolute continuity and then terminal-time absolute continuity; this is standard but should be written carefully.
- The bibliography does not actually include a Feldman–Hájek reference. The item labeled `FH` is Fukushima–Oshima–Takeda, not Feldman–Hájek.

The OU comparison with Brownian bridge is mathematically correct: the covariance eigenvalue ratios tend exponentially to \(1\), and \(S_tx\in H_0^1\) for \(t>0\). This part is not the problem.

---

### 6. Conclusion section

The final invariant-measure argument is correct conditionally on Lemma \(\ref{lem:girs}\).

If indeed
\[
P_t(y,\cdot)\ll\pi\qquad\forall y\in E,\ t>0,
\]
then every invariant measure \(\eta\) satisfies \(\eta\ll\pi\). The spectral-gap and truncation argument then forces \(d\eta/d\pi\equiv1\).

But since Lemma \(\ref{lem:girs}\) is not rigorously proved, the conclusion does not follow.

---

## Main fatal gap

The proof requires the following theorem:

> For every deterministic initial condition \(x\in C_0([0,1])\), the ABLM solution with drift \(\delta_0\) admits an adapted spatial-local-time drift representation
> \[
> K_t=\int_0^tS_{t-s}\,d_rL_s^0(r)\,ds
> \]
> with the energy estimate
> \[
> \int_0^t\|S_{(t-s)/2}\,d_rL_s^0(r)\|_{L^2}^2\,ds<\infty
> \quad\text{a.s.}
> \]

This theorem is not part of the problem assumptions, is not contained in the cited ABLM results as stated, is stronger than the BZ quasi-everywhere local-time construction, and is not proved in the draft.

Thus the revised proof is still incomplete.

---

## Required work for answer readiness

To make the solution rigorous, the author would need to supply a full proof of Proposition \(\ref{prop:lt}\), including:

1. all-starting-points spatial local-time existence for \(u_s(\cdot)\);
2. predictable/jointly measurable construction of \(\mu_s=d_rL_s^0(r)\);
3. proof that \(G_{1/n}(u_s(r))\,dr\Rightarrow \mu_s\) in a form strong enough to identify \(K_t\);
4. the moment estimate (7), uniformly in the approximation;
5. the energy estimate (6);
6. a precise Dirichlet-boundary extension of all estimates used.

Without these, the fixed-time absolute-continuity argument is only a promising strategy, not a proof.