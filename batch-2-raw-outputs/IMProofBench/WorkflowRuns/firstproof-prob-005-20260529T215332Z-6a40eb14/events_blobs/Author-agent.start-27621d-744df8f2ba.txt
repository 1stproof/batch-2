### Council member: gpt-55-pro (models/openai/gpt-55-pro) ###
I would target a **local capacity–Krylov estimate**, rather than the global finite-energy inequality first. The finite-energy bound is elegant but probably too strong to get directly from stationarity.

A concrete sufficient lemma is:

\[
\tag{K}
\sup_{x\in K}\mathbf E_x\int_\varepsilon^T {\bf1}_O(u_t)\,dt
\le C_{\varepsilon,T,K}\,\operatorname{Cap}(O)^\alpha
\]
for every compact \(K\subset E\), \(0<\varepsilon<T\), and open \(O\subset E\).

Then, if \(\eta\) is invariant,
\[
\eta(O)=\frac1{T-\varepsilon}\int_\varepsilon^T\int P_t(x,O)\eta(dx)\,dt
\le C_K\operatorname{Cap}(O)^\alpha+\eta(K^c).
\]
Tightness of \(\eta\) lets \(K\uparrow E\). Hence \(\eta(O)=0\) for cap-zero open \(O\), and outer regularity gives \(\eta(N)=0\) for every BZ exceptional set. This is enough to combine with BZ q.e. resolvent absolute continuity and your spectral-gap argument.

The exact intermediate lemmas I would try to prove are:

1. **Capacity comparability.** Since \(d\pi_n/d\gamma\) and \(d\pi/d\gamma\) are uniformly bounded above/below,
   \[
   c\,\operatorname{Cap}_\gamma(A)\le \operatorname{Cap}_n(A),\operatorname{Cap}(A)
   \le C\,\operatorname{Cap}_\gamma(A).
   \]

2. **Uniform approximating Krylov estimate.** Prove (K) for \(P^n\), with constants independent of \(n\).

   A sufficient stronger estimate is an integrated \(L^2\)-density bound:
   \[
   \sup_{n}\sup_{x\in K}\int_\varepsilon^T
   \left\|\frac{dP_t^n(x,\cdot)}{d\pi_n}\right\|_{L^2(\pi_n)}dt<\infty.
   \]
   Then
   \[
   \int_\varepsilon^T P_t^n(x,O)dt
   \le C\,\pi_n(O)^{1/2}
   \le C'\operatorname{Cap}_n(O)^{1/2}
   \le C''\operatorname{Cap}(O)^{1/2}.
   \]

3. **Passage to the ABLM limit.** Use path/semigroup convergence and portmanteau for open \(O\):
   \[
   \mathbf E_x\int_\varepsilon^T{\bf1}_O(u_t)\,dt
   \le \liminf_n \mathbf E_x^n\int_\varepsilon^T{\bf1}_O(u_t^n)\,dt.
   \]

If one really wants your displayed finite-energy inequality, replace (K) by the stronger resolvent version
\[
\tag{FE-K}
\left|\int_\varepsilon^T P_t\varphi(x)\,dt\right|
\le C_{\varepsilon,T} W(x)\,\mathcal E_1(\varphi,\varphi)^{1/2},
\]
with \(W\in L^1(\eta)\). Stationarity then gives
\[
\left|\int \varphi\,d\eta\right|
\le C_\eta \mathcal E_1(\varphi,\varphi)^{1/2}.
\]

My assessment: ABLM plausibly supplies the convergence step and uniform control of the singular drift convolution, but not presently the key estimate (2). Their local-time/regularization estimates are tailored to observables like \(G_n(u)\) or heat-kernel convolutions, not arbitrary path-space equilibrium potentials. To get (2), one likely needs a new Malliavin/Bismut or Harnack-type argument exploiting the bounded primitive \(B_n\), not \(\|G_n\|_\infty\), since naive Girsanov blows up. Thus the route is viable, but the missing lemma is genuinely stronger than what ABLM seems to state.

### Council member: opus_47_max (models/anthropic/opus_47_max) ###
**Framing.** Your estimate (10) is exactly the Fukushima–Oshima–Takeda characterization of a "measure of finite energy integral" (FOT Lem. 2.2.3 and Thm. 2.2.4); any such measure is automatically smooth and charges no quasi-polar (in particular no properly exceptional) set, with $U_1\eta\in D(\mathcal{E})$. So the target is the right one, and you do not need full strong Feller.

**Route I would try first (stationary smoothing of $P_t$).** The strongest, cleanest sufficient condition is the energy-to-$L^\infty$ smoothing
$$
\|P_t\varphi\|_\infty\le K(t)\,\mathcal E_1(\varphi,\varphi)^{1/2},\qquad t\ge t_0,
$$
for $\varphi\in D(\mathcal{E})$ (q.c. versions). Then by stationarity $\eta(\varphi)=\eta(P_t\varphi)\le K(t)\mathcal{E}_1(\varphi,\varphi)^{1/2}$, which is (10) for every invariant $\eta$ simultaneously. This sidesteps having to localize a constant $C_\eta$ depending on $\eta$, and removes the circularity of "absolute continuity ⇒ finite energy".

The pieces such a route would need:
1. *(Regularized smoothing.)* For each $n$, a Bismut/Mehler bound
$\|P_t^n\varphi\|_\infty\le K_n(t)\,\mathcal E_n^1(\varphi,\varphi)^{1/2}.$
For Lipschitz drift this is standard, but the naive constant blows up like $\|G_{1/n}\|_\infty$. The honest version must depend on the *primitive* $B_n$ (uniformly bounded), not on $G_{1/n}$. This is the same cancellation needed to dominate the Novikov term in your notes.
2. *(Uniformity in $n$.)* $K_n(t)\le K(t)$ uniformly. With your bounded-density observation ($d\pi_n/d\gamma$ comparable), this would reduce to a Gaussian (Brownian-bridge) calculation modulated by the bounded potential $B_n$.
3. *(Passage to the limit.)* Combine with (A) and Fatou.

This is essentially asking for the same "asymptotic strong Feller in energy norm" that Hairer–Mattingly use in the singular SPDE setting (their 2018 paper). The technique transports.

**Route II (stationary Krylov via ABLM sewing).** Use Lê's stochastic sewing to get a uniform-in-$n$ Krylov estimate for the regularized SPDE,
$$
\sup_n \mathbb{E}^x\!\int_0^T \varphi(u^n_s)\,ds\ \le\ C(T)(1+\|x\|^p)\,\|\varphi\|_{\mathcal{C}^{-\sigma}},
$$
for $\sigma$ small. By stationarity under any invariant $\eta$ and Lyapunov $\int\|v\|^p d\eta<\infty$,
$\eta(\varphi)\le \tilde C(\eta)\|\varphi\|_{\mathcal{C}^{-\sigma}}.$
Then identify $\|\varphi\|_{\mathcal{C}^{-\sigma}}\le C\,\mathcal E_1(\varphi,\varphi)^{1/2}$ on $D(\mathcal E)$ via Brownian-bridge Sobolev embedding (this works because $\sigma$ can be chosen small enough that $\mathcal{C}^\sigma$ supports of $\gamma$-quasi-continuous things have natural energy).

Intermediate lemmas needed:
- **(L1)** Moment bound for any invariant $\eta$. This is the standard dissipativity argument; the bounded $|H_+|$ adds an $L^\infty$ term to the energy estimate, harmless.
- **(L2)** ABLM-uniform sewing Krylov bound for $u^n$ with polynomial-in-$\|x\|$ constant. Looking at ABLM 2024 Sec. 5, their sewing constants do come out polynomial in path moments (which give polynomial-in-$\|x\|$ after taking expectations).
- **(L3)** Negative-Besov–to–energy embedding on $\gamma$. Concretely, $\|\varphi\|_{B^{-\sigma}_{2,2}(\gamma)}\lesssim \mathcal E_1(\varphi,\varphi)^{1/2}$ for $\sigma<1/2$ via spectral expansion in the Dirichlet basis.

**My honest assessment.** Route I is conceptually cleaner and more powerful, but the *cancellation* in step (1) — replacing $G_{1/n}$ by $B_n$ in a Bismut-formula constant — is exactly the technical heart of ABLM and is *not* a black-box consequence of their statements. You'd be replicating their sewing in a smoothing-of-$P_t^n$ form. Route II reuses ABLM more directly but requires you to chase polynomial-in-$\|x\|$ behaviour through the sewing constants and verify the Besov–energy embedding.

If forced to bet: Route II via uniform ABLM sewing is more likely to be writable today; Route I gives a stronger conclusion but is closer to "do the singular ergodicity theory from scratch". Either way, the BZ paper itself does not supply these; they need to be extracted from a careful re-reading of ABLM's stochastic-sewing pages.

### Council member: gemini-31-pro (models/gemini/gemini-31-pro) ###
Here is how I would approach closing this gap. I recommend pivoting away from using ABLM’s local-time estimates to prove finite energy (Route 4), and instead pursuing **Route 2 (Eventual equicontinuity)** via an Asymptotic Strong Feller (ASF) coupling. If you prefer to stick to Route 4, you should bypass ABLM’s estimates entirely and use the stationary Fokker-Planck equation.

### Why ABLM’s Krylov bounds fall short for Route 4
You asked if ABLM’s local-time/regularization estimates supply the lemmas for a capacity bound. They likely do not, due to a dimensional mismatch. 

The ABLM Krylov bounds (e.g., $\mathbb{E} \int_0^t \int_0^1 f(u_s(x))\,dx\,ds \le C\|f\|_{L^p}$) prove that the *one-dimensional spatial projections* of the measure are absolutely continuous. However, the Bounebache–Zambotti exceptional set $N$ is a capacity-zero subset of the infinite-dimensional path space $E = C_0([0,1])$. Knowing that one-dimensional marginals have densities is far too weak to prove that a measure avoids all infinite-dimensional Gaussian-capacity-zero sets. 

### The Recommended Strategy: Route 2 via ASF Coupling
Your Lemma 3 (Eventual equicontinuity) is extremely powerful because it completely bypasses the BZ exceptional set. The condition $\lim_{t\to\infty} |P_t f(x) - P_t f(y)| = 0$ is exactly the Asymptotic Strong Feller (ASF) property, which can be proved without relying on infinite-dimensional Girsanov transformations.

**Strategy (High/Low frequency coupling):**
1. **Decomposition:** Split the SPDE into a finite number of low Fourier modes $u_{low}$ and the remaining high modes $u_{high}$. 
2. **High-mode synchronous coupling:** Couple two solutions $u^x$ and $u^y$ using the exact same noise. The difference $w = u^x - u^y$ satisfies $\partial_t w = \Delta w + \delta_0(u^x) - \delta_0(u^y)$. While $\delta_0$ is singular, its primitive $H_+$ is bounded. This means the "anti-dissipative" energy injected by the drift difference is globally bounded. On the high modes, the strong dissipation of the Laplacian ($\lambda_k \sim k^2$) will easily overwhelm this bounded perturbation, forcing $w_{high}$ to contract exponentially.
3. **Low-mode shift coupling:** Because the low-mode subspace is finite-dimensional and the effective primitive potential is bounded, you can use a standard Girsanov shift (or reflection coupling) on the noise of $u^y$ to force $w_{low}$ to zero with high probability. 
4. **Conclusion:** This is the exact asymptotic coupling machinery developed in Hairer–Mattingly (2011, and HM 2018 in your references). It yields $\mathbb{E} |f(u_t^x) - f(u_t^y)| \to 0$, satisfying your Lemma 3 and immediately proving uniqueness.

### Alternative Backup: Route 4 via Infinitesimal Invariance
If you strongly prefer to prove the finite-energy bound $|\int \varphi\,d\eta| \le C_\eta \mathcal E_1(\varphi,\varphi)^{1/2}$, do it analytically via the generator.

1. **Stationary Equation:** Any invariant measure $\eta$ for the ABLM semigroup must satisfy the stationary Fokker-Planck equation $\int (L_0 \varphi + \langle \delta_0(u), D\varphi \rangle) d\eta = 0$ for cylinder functions.
2. **Gauge Transformation:** As you noted, the singular drift is exactly the gradient of a bounded potential: $\delta_0 = \nabla U$ with $U(u) = \int_0^1 H_+(u(x))dx$. 
3. **Elliptic Regularity:** By standard uniqueness results for infinitesimally invariant measures of gradient systems (e.g., Bogachev, Röckner, et al., *Comm. Pure Appl. Math. 1999*), any probability measure satisfying this equation for a bounded $U$ must inherently possess finite energy (specifically, a density in $H^1(\gamma)$). This yields $\eta \ll \pi$ purely analytically, completely independently of ABLM's Krylov bounds.