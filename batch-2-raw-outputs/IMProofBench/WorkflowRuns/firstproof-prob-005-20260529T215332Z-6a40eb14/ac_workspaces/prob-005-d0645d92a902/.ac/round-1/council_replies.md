### Council member: gpt-55-pro (models/openai/gpt-55-pro) ###
My preferred way to close this is not via BZ exceptional-set bookkeeping, but via a **resolvent strong-Feller upgrade**.

Key observation: since \(\pi\) is invariant and has full support, for any \(\pi(A)=0\),
\[
\int R_\lambda^P{\bf1}_A\,d\pi=\lambda^{-1}\pi(A)=0,
\]
so \(R_\lambda^P{\bf1}_A=0\) \(\pi\)-a.e. If you can prove that the **actual ABLM resolvent maps bounded Borel functions to continuous functions**, then nonnegativity plus full support forces
\[
R_\lambda^P{\bf1}_A(x)=0\qquad\forall x.
\]
That gives exactly the desired pointwise AC, without BZ. So I would look hard for a resolvent strong-Feller estimate from ABLM/Zvonkin-type regularization estimates, uniform in the mollifier in a Besov/distributional norm of \(\delta_0\), not in \(\|G_{1/n}\|_\infty\).

On your four proposed routes:

1. **ABLM stability \(\Rightarrow\) strict BZ version.** Ordinary stability on \(C_b\) is not enough: it cannot detect modifications on a \(\pi\)-null exceptional set. But there is a clean conditional route. If BZ’s resolvent kernel \(\rho_\lambda\) is genuinely continuous on \(C_b\), and ABLM gives Feller continuity of \(R_\lambda^P f\) for \(f\in C_b\), then the two resolvents agree \(\pi\)-a.e. as \(L^2(\pi)\) resolvents, hence everywhere by full support. Equality on \(C_b\) then identifies the measures \(R_\lambda^P(x,\cdot)=\rho_\lambda(x,\cdot)\), giving AC. If BZ only gives quasi-continuity, you still need entrance or strong Feller.

2. **Entrance from exceptional sets.** This is viable but needs a quantitative smoothing input. If \(N\) is the BZ exceptional set and you prove
\[
P_s^P(x,N)=0\quad\forall x,\ s>0,
\]
then q.e. AC plus Markov property gives all-start resolvent AC: for \(\pi(A)=0\), \(P_{s+t}(x,A)=0\) for \(t>0\), and the initial interval contributes at most \(s\) to the resolvent, then let \(s\downarrow0\). Additive white noise strongly suggests this, but it is not automatic; one needs a capacity/Harnack estimate.

3. **Uniform estimates for \(P^n\).** A useful sufficient estimate would be: for each \(\tau>0,x\), some \(\alpha>0\),
\[
P_\tau^n(x,O)\le C_{\tau,x}\,\pi_n(O)^\alpha
\]
for all open \(O\), uniformly in \(n\). Then weak convergence plus \(\pi_n\to\pi\) in TV gives \(P_\tau(x,\cdot)\ll\pi\). A capacity version,
\[
P_\tau^n(x,O)\le C_{\tau,x}\operatorname{Cap}_\gamma(O)^\alpha,
\]
would at least give entrance from BZ polar sets, since the \(\pi_n\)-capacities are uniformly comparable to Gaussian capacity. I would avoid Girsanov constants depending on \(\int G_n^2\): those likely blow up like an approximate \(\delta_0^2\). Estimates depending only on the bounded potential oscillation are the right target.

4. **Stationary solutions avoid exceptional sets.** Abstractly, stationarity plus the \(L^2(\pi)\) spectral gap is insufficient: one can alter a Markov version on a \(\pi\)-null absorbing set. So this route must use the actual SPDE/noise. A possible route is stationary Fokker–Planck/Galerkin: prove finite-dimensional stationary projections have densities with uniform Gaussian Fisher/entropy bounds, then pass to \(\eta\ll\gamma\sim\pi\). Promising, but probably harder than resolvent strong Feller.

So my recommendation: first try the resolvent strong-Feller trick; second, formulate a uniform \(L^p\)/capacity estimate for \(P_\tau^n(x,\cdot)\).

### Council member: opus_47_max (models/anthropic/opus_47_max) ###
**My take.** Of the four routes, I would invest in **Route 3 supported by Route 1**, treat **Route 2 as essentially equivalent to strong-Feller** (so as hard as the original problem), and view **Route 4 as appealing but with hidden regularity costs**. A reframing that I think clarifies the target:

\[
(\ast)\qquad P_t(x,\cdot)\ll\gamma\ \text{for every }x\in C_0([0,1]),\ t>0.
\]

Because $\pi\sim\gamma$ with two‑sided bounded density, $(\ast)$ is equivalent to (8), and is easier to attack because $\gamma$ is Gaussian. You never have to identify a "strict version" of the BZ process: $(\ast)$ kills the exceptional set automatically.

**Why Route 3 reduces to short‑time AC.** Conditioning on $\mathcal F_{t-\epsilon}$ and using independence of $W|_{[t-\epsilon,t]}$ from the past, $(\ast)$ for arbitrary $t$ reduces to
\[
(\ast)_\epsilon\qquad P_\epsilon(y,\cdot)\ll\gamma\ \text{for every }y\in C_0,\ \epsilon>0,
\]
which is a clean, purely short‑time question. For the OU/linear part alone this is true by Feldman–Hájek: the centred Gaussian with covariance $\int_0^\epsilon S_{2s}\,ds = \tfrac12(-\Delta_D)^{-1}(I-e^{2\epsilon\Delta_D})$ differs from $\gamma$'s covariance $\tfrac12(-\Delta_D)^{-1}$ by a trace‑class perturbation, and the mean $S_\epsilon y$ lies in $H^1_0$, the Cameron–Martin space. So you really do only need to control the *drift contribution*.

**Where Route 1 enters.** A clean criterion that passes to the limit: for some $p>1$,
\[
\sup_n \bigl\| dP_\epsilon^n(y,\cdot)/d\gamma\bigr\|_{L^p(\gamma)}<\infty.
\]
Any weak limit point then has $L^p$ density, hence $(\ast)_\epsilon$. The natural attempt is Girsanov from OU, but the naive density $\exp(\int G_{1/n}(u^n)\,dW - \tfrac12\int G_{1/n}(u^n)^2\,ds)$ has the variance term diverging like local‑time of $u^n$ at $0$ times $\sqrt n$. So one wants a *renormalized* Girsanov in which $\int G_{1/n}^2$ is replaced by the symbol of the singular bilinear form — this is exactly what ABLM's stochastic‑sewing/Krylov estimates control. I would translate their Krylov bound \(\mathbb E\int_0^T |b_n(u^n_s)|\,ds \lesssim \|b_n\|_{B^{-1+\kappa}}\) into a fixed‑time entropy bound and then a Pinsker‑type $L^1$ density bound. This is technical but, I think, the right shape.

**On Route 4.** Stationarity does give the formal representation
\[ u_0 = \int_{-\infty}^0 S_{-s}\,dW_s + \int_{-\infty}^0 S_{-s}\delta_0(u_s)\,ds,\]
and you would *like* the drift integral to be a.s. in the CM space $H^1_0$ to get $\eta\ll\gamma$ for free. But the integrand $\delta_0(u_s)$ has regularity $\sim H^{-1-\kappa}$ in space, and $\int_{-\infty}^0 S_{-s}\cdot ds$ smooths by two derivatives in time‑average but only borderline in fixed‑time — formally producing a process of $\partial_\theta\ell^0$ type, which is not obviously in $H^1_0$. So I don't see a soft proof here; you'd be reproving Route 1‑level estimates in stationary guise.

**Adjacent literature worth mining.**
- *Da Prato–Debussche / Maslowski–Seidler* — Bismut‑Elworthy‑Li for SPDEs with bounded drift; the cleanest source for strong Feller of $P^n_t$.
- *Zhang, Bogachev–Da Prato–Röckner* — strong Feller for SDEs/SPDEs with $L^p_tL^q_x$ or distributional drift, sometimes via density estimates uniform in regularization.
- *Hairer–Mattingly*, "Spectral gaps in Wasserstein..." — for reversible processes with gap, asymptotic strong Feller already implies a strong uniqueness statement; might let you weaken $(\ast)$.
- *Zambotti*, *Random Obstacle Problems* monograph — finer description of BZ‑type capacities and the exceptional sets you need to escape.
- ABLM 2025 weak/mild equivalence: their compactness argument in path space should let you upgrade convergence of regularized AC densities once you have an *a priori* $L^p$ bound.

If I had to bet on one concrete attack, it is $(\ast)_\epsilon$ via renormalized Girsanov plus ABLM Krylov estimates.

### Council member: gemini-31-pro (models/gemini/gemini-31-pro) ###
I recommend bypassing the Bounebache–Zambotti (BZ) capacity analysis entirely. Instead of attempting to identify the ABLM semigroup with the strict BZ Dirichlet process, you can achieve your exact goal (resolvent absolute continuity for *all* starting points) by exploiting the structure of the ABLM construction directly. 

The most robust route is a powerful version of your Option 3, achieved by showing that the ABLM semigroup is **Strong Feller** and/or has **mutually absolutely continuous transition laws**. 

Here is how you can lay out the argument:

**1. The Zvonkin Transform:**
The ABLM (2024) well-posedness relies on a Zvonkin-type transform. This provides a pathwise homeomorphism $\Theta: C_0([0,1]) \to C_0([0,1])$ such that $v_t = \Theta(u_t)$ solves a modified SPDE with a tame (functionally regular) drift and additive space-time white noise.

**2. Mutual Absolute Continuity (The Girsanov Route):**
Because $v$ has a regular drift, its transition laws are locally equivalent to the linear Stochastic Heat Equation (SHE), $dZ = \frac{1}{2}\Delta Z + \dot{W}$, via Girsanov's theorem. 
For the linear SHE, it is a classic fact that $P_t^{SHE}(y_1, \cdot) \sim P_t^{SHE}(y_2, \cdot)$ for *all* $y_1, y_2 \in C_0$. This holds because the deterministic smoothing $e^{t\Delta/2}(y_1 - y_2)$ maps into $C^\infty$, firmly landing in the Cameron-Martin space of the stochastic convolution (which is $H_0^1([0,1])$).
Therefore, $P_t^v(y_1, \cdot) \sim P_t^v(y_2, \cdot)$. Since $\Theta$ is a homeomorphism, this pulls back perfectly to your ABLM process:
\[ P_t(x_1, \cdot) \sim P_t(x_2, \cdot) \quad \text{for all } x_1, x_2 \in C_0([0,1]). \]
Because $\pi = \int P_t(x, \cdot)\pi(dx)$, this mutual equivalence trivially forces $P_t(x, \cdot) \sim \pi$ for *every* deterministic $x$. This gives you (8) instantly.

**3. Strong Feller + Full Support (The Topological Route):**
Even without mutual equivalence, standard Bismut-Elworthy-Li arguments ensure $v_t$ is Strong Feller. Because $\Theta$ is a homeomorphism, $u_t$ is also Strong Feller: for any bounded measurable $f$, $P_t^u f = (P_t^v(f \circ \Theta^{-1})) \circ \Theta$ is continuous.
If you have a set $A$ with $\pi(A) = 0$, the function $\varphi(x) = P_t(x, A)$ is continuous. By invariance, $\int \varphi(x) \pi(dx) = 0$, so $\varphi = 0$ $\pi$-almost everywhere. Because $\pi \sim \gamma$, it has full topological support in $C_0([0,1])$. A continuous function that is zero $\pi$-a.e. must be identically zero. Thus $P_t(x, A) = 0$ for all $x$. 

**Assessment of your options:**
*   **Option 1 (Uniform $P_t^n$ estimates):** Notoriously difficult. The approximations $G_{1/n}$ blow up in $L^\infty$, making uniform heat-kernel bounds hard to pass to the limit. 
*   **Option 2 & 3 (Strict BZ & Entrance):** The mutual absolute continuity argument above completely solves the entrance problem. You enter the measure class of $\pi$ instantly from *any* initial condition, obliterating the exceptional sets.
*   **Option 4 (Stationarity):** Insufficient. Uniqueness of invariant measures inherently requires a transition statement for fixed, non-random initial conditions to rule out hypothetical ergodic measures living entirely on a BZ exceptional set.

Using the ABLM Zvonkin transform to transfer standard SHE properties completely closes your gap.