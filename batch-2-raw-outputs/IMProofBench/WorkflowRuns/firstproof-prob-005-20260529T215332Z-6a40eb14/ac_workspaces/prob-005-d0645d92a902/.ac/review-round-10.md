## Referee report on the revised `answer.tex`

### LaTeX contract

I compiled the revised `answer.tex` twice with `pdflatex`. It compiles successfully, with no undefined references or LaTeX warnings in my run, and the resulting PDF has 7 pages. The document uses exactly `\documentclass[12pt]{article}`, uses only the permitted `fullpage` layout package, and I found no forbidden margin, line-spacing, or in-document font-size changes. Thus the **LaTeX contract is satisfied**.

### Literature check

The cited ABLM paper is a real 2024 CPAM article on stochastic heat equations with distributional drift, including measure-valued drifts such as \(\delta_0\), and it uses stochastic sewing methods. ([cris.technion.ac.il](https://cris.technion.ac.il/en/publications/well-posedness-of-stochastic-heat-equationwith-distributional-dri/?utm_source=openai)) Lê’s Banach-space stochastic sewing paper and the earlier stochastic sewing lemma paper are also real and correctly identified. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/196312/?utm_source=openai)) Bounebache–Zambotti’s paper is real and concerns a stochastic heat equation with singular drift, local time, an explicit Gibbs-type invariant measure, and a Dirichlet-form construction. ([ideas.repec.org](https://ideas.repec.org/a/spr/jotpro/v27y2014i1d10.1007_s10959-012-0421-8.html?utm_source=openai))

However, these literature checks do **not** validate the new Dirichlet-boundary uniform Hilbert estimate or the all-starting-point absolute-continuity argument; those are original arguments in the draft and must stand on their own.

---

## Changes relative to the previous draft

The revision addresses several earlier objections:

1. **The problem interpretation is clearer.**  
   The approximation assumption is now explicitly stated as weak convergence on \(E=C_0([0,1])\) against all \(\Phi\in C_b(E)\).

2. **The uniform Hilbert drift estimate is more detailed.**  
   The author added heat-kernel estimates, Gaussian convolution estimates, an explanation of the sewn-integral identification, and a direct sketch of the Hilbert-valued semigroup sewing lemma.

3. **The reversibility section is improved.**  
   The previous purely formal generator computation has been replaced by a Galerkin/cylinder-potential approximation argument.

4. **The fixed-time absolute-continuity proof is improved.**  
   The author now explicitly works on the Polish state space \(E\), proves that the deterministic controlled convolution is \(E\)-valued, and uses entropy lower semicontinuity on \(E\).

These are real improvements. Nevertheless, several essential gaps remain.

---

## Detailed mathematical audit

### 1. Problem statement and interpretation

This section is acceptable. The draft records the adopted interpretation of the approximation assumption and uses a faithful version of the problem’s stipulated Dirichlet extension of ABLM. No major issue here.

---

### 2. Lemma: uniform regularized drift estimate

The revised proof is much stronger than the previous version, but it is still not fully rigorous at the level required for a complete solution.

#### 2.1 Heat-kernel estimates

The estimate
\[
p_a(y,y)\asymp a^{-1/2}\bigl(1\wedge d(y)^2/a\bigr)
\]
and the consequence
\[
\rho_\tau(y)\asymp \sqrt{\tau}\wedge d(y)
\]
are plausible and standard in one dimension, at least with constants depending on the time horizon. The weighted estimates
\[
\sup_z\int_0^1p_a(z,y)\rho_\tau(y)^{-1/2}\,dy
\le C(a^{-1/4}+\tau^{-1/4})
\]
and
\[
\|\rho_\tau^{-1}S_\tau f\|_2\le C\tau^{-1/2}\|f\|_2
\]
are also plausible.

But these estimates are central to the proof and are still only sketched. In particular, the boundary convolution with \(d(y)^{-1/2}\) is summarized by “near the boundary” after a change of variables. A strict proof should split the interval into boundary/interior regions and handle the dependence on \(z,a,\tau\) carefully. This is probably fixable, but as written it remains a nontrivial unproved analytic lemma.

#### 2.2 Sewn-integral identification

The earlier gap in identifying \(D^n\) as the sewn limit of \(A^n\) has mostly been addressed. The estimate
\[
\left\|A^n_{a,b}-\int_a^b S_{b-r}b_n(u_r^n)\,dr\right\|_{L^2H}
\le \operatorname{Lip}(b_n)\|b_n\|_\infty(b-a)^2
\]
is correct for fixed \(n\), because the unfrozen remainder is bounded by the bounded regularized drift. The constant depends on \(n\), but this is enough for the fixed-\(n\) convergence of Riemann sums.

This part is now acceptable.

#### 2.3 Conditional Gaussian estimates

The estimates
\[
\E_s b_n(Z_r(y))b_n(Z_q(z))
\le C\rho_{r-s}(y)^{-1/2}\rho_{q-r}(z)^{-1/2}
\]
and
\[
\left|\E_u\{b_n(Z_r(y))-b_n(Z_r(y)+h(y))\}\right|
\le C\rho_{r-u}(y)^{-1}|h(y)|
\]
are now sufficiently explained in outline. They rely on \(b_n\) being a probability density and on the derivative bound for Gaussian convolution. This part is largely fixed.

#### 2.4 Semigroup stochastic sewing lemma

The proof still contains an essential lemma in proof-sketch form. The stated sewing fact is a semigroup-modified, Hilbert-valued version of stochastic sewing. The author gives the right idea: compare dyadic refinements, sum conditional means, and use orthogonality of centered martingale increments. But a complete proof should explicitly specify:

- the filtration and measurability hypotheses on \(A_{s,t}\);
- the precise dyadic refinement notation;
- why the centered terms are orthogonal after applying \(S_{t-b}\);
- how the estimate for consecutive refinements gives convergence of the full sequence and the final bound;
- whether the result is only for dyadic partitions or for the sewn limit used in (7).

The argument is plausible, but the lemma is essential and is not fully proved. This was one of the previous concerns; it is improved but not completely resolved.

#### 2.5 Bootstrap

Assuming the sewing lemma, the bootstrap
\[
Y_n(h)\le C+Ch^{1/2}Y_n(h)
\]
is reasonable, and the passage from small intervals to longer intervals is acceptable after adjusting the constant depending on \(T\). No major issue here.

**Verdict on Lemma 1:** plausible but not fully rigorous. The remaining weak point is the semigroup sewing lemma plus the weighted heat-kernel estimates.

---

### 3. Reversibility and spectral gap

This section remains the most serious source of unresolved gaps.

#### 3.1 Total variation convergence \(\pi_n\to\pi\)

This part is essentially correct. Since \(0\le B_n\le1\), \(B_n(a)\to\mathbf 1_{\{a>0\}}\) away from \(a=0\), and Brownian bridge spends zero Lebesgue time at a fixed level, dominated convergence gives total variation convergence.

#### 3.2 Galerkin/cylinder-potential approximation

The new Galerkin argument is an improvement, but it is not complete.

The draft asserts:

> The Lipschitz property of \(b_n\) gives convergence of the approximating mild solutions to \(u^n\) in \(L^2(\Omega;C([0,T];H))\), and at each positive time in \(E\).

This is a substantial convergence statement. It is plausible for bounded Lipschitz Nemytskii drift, but the proof is not supplied. One needs to control the approximation error
\[
\Pi_m b_n(\Pi_m v)-b_n(v)
\]
in the mild equation, including the projection error and the passage from \(H\)-convergence to \(E\)-convergence at positive time. This is fixable, but currently asserted rather than proved or cited.

#### 3.3 Overclaim for bounded Borel functions

The draft says that passing \(m\to\infty\) gives, for bounded Borel \(f,g\),
\[
\int P_t^n f\,d\pi_n=\int f\,d\pi_n,\qquad
\int gP_t^n f\,d\pi_n=\int fP_t^n g\,d\pi_n.
\]
The convergence arguments described only justify passage to the limit for bounded continuous test functions, not arbitrary bounded Borel functions. Weak convergence and convergence in probability do not allow direct passage for discontinuous test functions. This is a new overstatement introduced by the revision.

It may be possible to recover the bounded Borel statement later by monotone-class arguments after constructing equality of kernels as finite measures, but that is not shown here.

#### 3.4 Identification with the Dirichlet form

The proof still asserts that \(P_t^n\) is the symmetric semigroup generated by
\[
{\cal E}_n(F,G)=\frac12\int_E\langle DF,DG\rangle_H\,d\pi_n.
\]
This is standard for sufficiently regular stochastic quantization equations, but it is not proved. The Galerkin approximation argument shows, at most, a route to reversibility; it does not by itself establish that the limiting infinite-dimensional semigroup has precisely this closed Dirichlet form as its generator.

This matters because the spectral-gap decay
\[
\Var_{\pi_n}(P_t^n f)\le e^{-2t/C}\Var_{\pi_n}(f)
\]
is derived from the Poincaré inequality for \({\cal E}_n\). Without a rigorous generator/form identification, this step is not justified.

This was a previous concern. The revision partially addresses it but does not fully close it.

---

### 4. Proposition: invariance, symmetry, spectral gap for \(P_t\)

If one grants the regularized reversibility and spectral gap, the passage to the limit using \(P_t^n\Phi(x)\to P_t\Phi(x)\) and \(\pi_n\to\pi\) is mostly correct for bounded continuous \(f,g\). The extension to \(L^2(\pi)\) by density is also standard, using invariance and Jensen contraction.

But because the regularized spectral gap and form identification remain underproved, Proposition 1 remains conditional on an unproved essential input.

---

### 5. Fixed-time absolute continuity

This section is substantially improved and is the strongest part of the revised proof.

#### 5.1 Dyadic adapted control

The adapted control
\[
F_s^n=\sum_{k\ge0}\Delta_{k+1}^{-1}\mathbf 1_{(r_{k+1},r_{k+2}]}(s)
S_{s-r_{k+1}}D_k^n
\]
is correctly designed: \(D_k^n\) is known at time \(r_{k+1}\), so the control is adapted/predictable. The energy estimate follows from Lemma 1, and the telescoping identity
\[
\int_0^t S_{t-s}F_s^n\,ds=K_t^n
\]
is correct.

#### 5.2 State-space issue

The previous state-space concern is mostly addressed. The proof that
\[
\int_0^tS_{t-s}F_s\,ds\in H_0^\alpha(0,1)\subset E
\]
for \(\alpha>1/2\) is correct. This justifies treating the terminal variables as \(E\)-valued.

#### 5.3 Girsanov/entropy

The Girsanov step is plausible but still compressed. The statement

> Hilbert-space Girsanov says that the law on the noise path space of \(W+\int F^{n,N}\) has entropy at most \(\frac12\E\int\|F^{n,N}\|^2\)

is a standard adapted-shift entropy bound, but for cylindrical Brownian motion one should specify the actual canonical path space, or embed the cylindrical Brownian motion in a larger Hilbert space. This is probably fixable by citing an appropriate Hilbert-space Girsanov theorem, but it is still an essential technical step not fully formulated.

The localization by \(\tau_N\), convergence \(X_N\to u_t^n\) in probability in \(E\), and entropy lower semicontinuity on \(E\) are otherwise sound.

#### 5.4 Feldman–Hájek comparison

The Feldman–Hájek comparison \(\nu_t^x\sim\gamma\) is correctly argued. The covariance eigenvalue ratios are bounded away from zero and differ from \(1\) by a square-summable sequence, and \(S_tx\in H_0^1\), the Cameron–Martin space of Brownian bridge.

**Verdict on fixed-time absolute continuity:** this section is close to rigorous, but it still depends crucially on Lemma 1 and on a precisely stated adapted-shift Girsanov theorem for cylindrical noise.

---

### 6. Conclusion and uniqueness argument

Assuming all previous inputs, the final uniqueness argument is correct.

- Fixed-time absolute continuity gives \(\eta\ll\pi\) for every invariant \(\eta\).
- Symmetry gives \(P_t h=h\) in \(L^1(\pi)\).
- Jensen applied to \(h_a=h\wedge a\) gives \(P_t h_a\le h_a\).
- Equality of integrals forces \(P_t h_a=h_a\).
- The spectral gap forces \(h_a\) to be constant.
- Letting \(a\to\infty\) gives \(h=1\).

This part is mathematically sound, modulo the earlier unresolved issues.

---

## Overall verdict

The revised proof is significantly better than the previous draft. In particular, the fixed-time absolute-continuity strategy is promising, and many earlier objections have been partially addressed.

However, `answer.tex` is still **not a complete rigorous solution**. The remaining essential gaps are:

1. the semigroup-valued stochastic sewing lemma is still only sketched;
2. the weighted Dirichlet heat-kernel estimates are central but not fully proved or cited;
3. the Galerkin-to-regularized-SPDE reversibility argument is incomplete;
4. the claim of regularized reversibility for bounded Borel functions is not justified by the stated convergence;
5. the identification of \(P_t^n\) with the symmetric semigroup generated by \({\cal E}_n\), needed for the spectral gap, remains asserted rather than proved;
6. the cylindrical Hilbert-space Girsanov/entropy step should be stated on a precise path space or cited.

These are not merely cosmetic issues; they affect the mathematical validity of the proof. Therefore the answer is not yet answer-ready.