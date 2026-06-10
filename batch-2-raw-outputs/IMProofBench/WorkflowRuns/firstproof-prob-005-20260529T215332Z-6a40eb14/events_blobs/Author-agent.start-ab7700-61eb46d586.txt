### Council member: gpt-55-pro (models/openai/gpt-55-pro) ###
Yes — I would try to close the gap via **capacity/smooth-measure regularity of invariant laws**, rather than pointwise transition AC.

The useful target is:

> **Lemma A (invariant laws are smooth).** Every invariant probability \(\eta\) of the all-starting-points ABLM semigroup charges no \(\mathcal E\)-exceptional set for the BZ Dirichlet form.

Then the q.e. BZ absolute continuity is enough. Indeed, let \(N\) be the exceptional set outside which ABLM and BZ are identified and \(R_\lambda(y,\cdot)\ll\pi\). If \(\eta(N)=0\), then for \(\pi(A)=0\),
\[
\eta(A)=\lambda\int R_\lambda^P(y,A)\,\eta(dy)=0,
\]
so \(\eta\ll\pi\), and your spectral-gap argument finishes uniqueness.

A concrete sufficient estimate for Lemma A is the finite-energy/capacity bound
\[
\left|\int \varphi\,d\eta\right|
   \le C_\eta\,\mathcal E_1(\varphi,\varphi)^{1/2},
   \qquad \varphi\in D(\mathcal E)\cap C_b(E),              \tag{FEI}
\]
or even just
\[
\eta(O)\le C_\eta\,{\rm Cap}_{\mathcal E}(O)^\alpha
\]
for open \(O\). FEI implies this by testing with equilibrium potentials, hence \(\eta\) is smooth in the Dirichlet-form sense. This is exactly the non-pointwise replacement for resolvent AC.

How to prove FEI? I would formulate the missing analytic input as a **stationary Krylov-capacity estimate**. For the ABLM process, or first uniformly for the regularized processes,
\[
\mathbf E_\mu\int_0^T \varphi(X_s^n)\,ds
 \le C_T\Bigl(1+\int V\,d\mu\Bigr)\,
      \mathcal E_{1,n}(\varphi,\varphi)^{1/2},              \tag{K}
\]
with constants independent of \(n\). Here \(V\) is a Lyapunov function controlled by invariant laws. Since \(d\pi_n/d\gamma\) are uniformly bounded above/below, the capacities/energies \(\mathcal E_{1,n}\) are comparable to the limiting one. Passing \(n\to\infty\), starting from \(\mu=\eta\), and using stationarity gives
\[
T\int \varphi\,d\eta
 =\mathbf E_\eta\int_0^T\varphi(X_s)\,ds
 \le C_{\eta,T}\mathcal E_1(\varphi,\varphi)^{1/2},
\]
which is FEI.

The hard part is proving (K) without constants involving
\(\|G_{1/n}\|_\infty\) or \(\|G_{1/n}\|_{L^2}\), which blow up. The estimate must exploit the bounded primitive \(0\le B_n\le1\), or the local-time formulation, not naive Girsanov.

A finite-dimensional Fokker–Planck route would need essentially the same strength: if \(\eta_m=(\Pi_m)_\#\eta\), finite-dimensional ellipticity may give \(\eta_m\ll \pi_m\), but that alone is useless in infinite dimension. One needs
\[
\sup_m H(\eta_m\mid \pi_m)<\infty,
\]
then projective entropy gives \(\eta\ll\pi\). I would target entropy relative to \(\pi_m\), not Fisher relative to \(\gamma_m\), since the BV potential makes Fisher estimates suspect.

I would not rely on Markov uniqueness or \(L^2(\pi)\) spectral gap plus Feller irreducibility alone; those do not exclude invariant measures living on exceptional sets. Asymptotic strong Feller plus an accessible point would prove uniqueness without AC, but that is a different major estimate.

### Council member: opus_47_max (models/anthropic/opus_47_max) ###
**TL;DR.** Yes. The route I would bet on is **asymptotic strong Feller + topological irreducibility** (Hairer–Mattingly 2006). It is purpose-built to *bypass* pointwise transition AC. Markov uniqueness is clean but does not by itself exclude η ⊥ π. The finite-dim stationary-FP / Fisher-info route is the most direct attack on η ≪ π but is technically the heaviest because of the distributional drift.

**(i) Asymptotic strong Feller (ASF) + topological irreducibility.** HM06 Thm. 3.16 (and HM11 Thm. 3.4): if P_t is ASF at every x and topologically irreducible, the invariant probability is unique. ASF is a quantitative gradient bound that *can* blow up as t→0, so it's genuinely weaker than strong Feller. The input you need:

— A uniform-in-n Bismut–Elworthy–Li gradient bound for the regularized P_t^n,
|D P_t^n f(x)[h]|² ≤ C(t) ||f||_∞² ||h||_E²,
with C(t) depending only on the *bounded potential* (0 ≤ B_n ≤ 1, B_n' ≥ 0 monotone ramp), **not** on ||G_{1/n}||_∞ or ||G_{1/n}||_2. This is the technical heart.
— It's enough to obtain the weaker "approximate gradient bound" |∇P_t f|_E ≤ ε||f||_∞ + δ(t)||∇f||_E (with δ(t)→0 quickly enough), uniformly in n; pass to the limit.

Topological irreducibility should be cheap: approximate controllability of ∂_t v = ½Δ_D v + bounded forcing on [0,1] is classical, and the noise has full Cameron–Martin support.

**(ii) Asymptotic coupling** (HM "Yet another look at Harris", Glatt-Holtz–Mattingly–Richards). Equivalent in spirit but constructive. Couple (u^x, ũ^y) using a Girsanov shift g so Δ_t = u^x_t − ũ^y_t → 0 in C_0. Specific lemmas:
(L1) Continuous dependence x ↦ u^x in C([0,T], C_0) in probability (from ABLM 2024 stability — verify their estimates are uniform on bounded initial data).
(L2) Novikov-type bound 𝔼 exp(½∫₀^T ||g_s||² ds) ≤ C on compacts.
(L3) Δ_t → 0 in probability under the shifted measure.
The reason this should work: gradient of *bounded* potential ⇒ controllable Girsanov entropy; Dirichlet spectral gap π² gives linear contraction in the absence of drift mismatch.

**(iii) Markov uniqueness** (Eberle 1999 Lect. Notes; Albeverio–Röckner; Stannat 1999 Mem. AMS). The BZ form on smooth cylinders FC_b^∞ should be **essentially m-dissipative** ⇒ unique Markovian L²(π) extension ⇒ ABLM and BZ generate the same L²(π) semigroup. But this still gives only "π-AC invariant measure is unique" — exactly the round-1 conclusion. To eliminate η ⊥ π you need (i), (ii), or (iv).

**(iv) Finite-dim FP + Fisher info** (Bogachev–Krylov–Röckner–Shaposhnikov "FPK Equations" AMS 2015; Da Prato–Röckner–Stannat 2003). For any invariant η, project η_N onto first N Dirichlet–Fourier modes; aim for I(η_N | π_N) ≤ C uniformly in N, then η ≪ π in the projective limit. Obstruction: the projected stationary FP equation
∫ L_N^* F dη_N = 0 for cylinder F
contains δ_0(u(x_*)) tested against derivatives of F; you need a *robust* interpretation of this against an arbitrary invariant η. The bounded-potential gradient structure is in your favor (write δ_0 = ½(2H_+)' and integrate by parts at the level of η in cylinder coordinates), but I am uncertain how clean this becomes.

**(v) Weak Feller + L² gap + topological irreducibility is NOT enough.** Classical Doob needs strong Feller (or a small set / minorization). The standard replacement *is* (i).

**Concrete recommendation.** Push hard on (i). The bounded-potential structure is precisely the mechanism that made your uniform Poincaré (5) survive the limit; it should *also* make a Bismut-type gradient bound survive the limit because the relevant quantity is the *energy* of B_n, not the sup-norm of G_{1/n}. Useful template: HM 2018 "Strong Feller for singular SPDEs" — their parabolic-Anderson-style argument is the closest analogue. Also worth a look: Komorowski–Peszat–Szarek (Ann. Probab. 2010) **e-property** framework, often easier to verify than ASF.

### Council member: gemini-31-pro (models/gemini/gemini-31-pro) ###
This is an excellent setup. You have already done the heavy lifting by securing the $L^2(\pi)$ spectral gap without relying on quasi-everywhere Dirichlet form abstractions. 

To close the uniqueness gap **without** proving pointwise transition or resolvent absolute continuity, you should lean on topological and dynamical arguments. Here are the three most promising routes, along with a warning about Route 1.

### A Warning on Route 1 (Uniform Densities)
I advise against trying to prove uniform $L^p(\pi_n)$ density bounds for $P_t^n(x, \cdot)$. In infinite dimensions, Gaussian reference measures do not support ultracontractivity (i.e., local Sobolev inequalities fail, so there is no $L^2 \to L^\infty$ smoothing). The transition probabilities simply do not have $L^2$ densities with respect to the invariant measure, so uniform bounds will blow up. 

### Route A: The Topological Upgrade (The e-property)
You can completely sidestep absolute continuity and exceptional sets by upgrading your $L^2(\pi)$ convergence to pointwise convergence using equicontinuity. 

**The missing lemma:** 
Assume $P_t f \to \pi(f)$ in $L^2(\pi)$ for any bounded Lipschitz $f$. Suppose the semigroup has the *e-property*: for such $f$, the family of functions $\{P_t f\}_{t \ge 1}$ is equicontinuous on compacts of $E$. Then $P_t f(x) \to \pi(f)$ for **every** $x \in E$.

*Proof sketch:* Fix $x$. By equicontinuity, any sequence $t_k \to \infty$ has a subsequence where $P_{t_k} f$ converges uniformly on compacts to a continuous function $g$. Since convergence also holds in $L^2(\pi)$, we must have $g = \pi(f)$ for $\pi$-a.e. $y$. Because $\pi$ is equivalent to Brownian bridge, it has full topological support in $E$. A continuous function equal to a constant on a dense, full-support set must equal that constant everywhere. Thus, $g(x) = \pi(f)$, forcing everywhere pointwise convergence. 

If $P_t f(x) \to \pi(f)$ everywhere, the Dominated Convergence Theorem guarantees that any invariant measure $\eta$ satisfies $\eta(f) = \int P_t f \,d\eta = \pi(f)$, yielding unique ergodicity directly. 

**What you need:** You only need to extract a continuous dependence estimate from the ABLM (2024) strong well-posedness proof. If the pathwise distance between solutions $\mathbb{E}\|u^x(t) - u^y(t)\| \le C_t \|x-y\|$ doesn't blow up too violently, tightness gives the e-property. 

### Route B: Stationary Fokker–Planck and Capacity
If you prefer to leverage the Bounebache–Zambotti (BZ) Dirichlet form, use the structure of stationary solutions to avoid exceptional sets.

Let $\eta$ be an arbitrary invariant measure, and $u(t)$ be the stationary process with marginal $\eta$. Because $u(t)$ weakly solves the mild equation, it decomposes as $u(t) = Z(t) + V(t)$, where $Z(t)$ is the stationary OU process (law $\gamma$) and $V(t) = \int_{-\infty}^t S_{t-s} d\ell_s$. 
Because the local time $\ell_s$ is a positive additive functional, $V(t)$ enjoys much higher spatial regularity (e.g., $H_0^1$) than the Gaussian noise. By using the Cameron–Martin shift or by testing the stationary martingale problem against standard cylinder functions (the "Markov Uniqueness" approach of Bogachev–Krylov–Röckner), one can show that the convolution-like structure of $Z(t) + V(t)$ forces $\eta$ to have finite zero-order Dirichlet energy. By Fukushima's theory, finite-energy measures absolutely cannot charge sets of zero Gaussian capacity, meaning $\eta(N) = 0$. This instantly links you to your Lemma 4.

### Route C: Asymptotic Coupling
Since ABLM establishes strong pathwise well-posedness without Girsanov or Zvonkin transformations, they likely construct a robust synchronous coupling. If you can show that two solutions driven by the same noise satisfy $\mathbb{P}(\|u^x(t) - u^y(t)\| > \epsilon) \to 0$ as $t \to \infty$, you get unique ergodicity immediately (Hairer–Mattingly–Scheutzow 2011). This relies only on the dissipativity of the Dirichlet Laplacian outside the origin, using the bounded potential to control the origin-crossings.

**Recommendation:** Look closely at Route A. You already possess the $L^2(\pi)$ gap and full support; marrying them with standard continuous-dependence estimates is usually the path of least resistance.