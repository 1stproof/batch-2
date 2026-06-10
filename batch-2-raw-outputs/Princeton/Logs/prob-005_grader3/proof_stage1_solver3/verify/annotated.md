**Annotated Proof**

**Step 1: Approximating SPDE invariant measures**
*Claim:* The smoothed gradient SPDEs admit a unique invariant probability measure with an explicit Gibbs-type density.
*Citation:* [CONFIDENT] Da Prato, G. (2004), Kolmogorov Equations for Stochastic PDEs, Chapter 5, "Invariant measures for gradient systems"

**Step 2: Total variation convergence**
*Claim:* Pointwise convergence of potentials implies total variation convergence of $\mu_n$ to $\mu$ via DCT, as paths spend zero time at zero.
*Citation:* [APPROX] Bogachev, V. I. (1998), Gaussian Measures, Chapter 3, "Sample path properties and zero-level sets of Gaussian measures"

**Step 3: Limit measure invariance**
*Claim:* The limiting measure $\mu$ inherits invariance for the limiting transition semigroup via dominated convergence.
*Citation:* [CONFIDENT] Bogachev, Krylov, Röckner, Shaposhnikov (2015), Fokker-Planck-Kolmogorov Equations (arxiv draft), Chapter 8, "Weak convergence of stationary measures"

**Step 4: Holley-Stroock uniform spectral gap**
*Claim:* Because the densities are bounded strictly away from zero and infinity, the measures inherit a uniform Poincaré inequality.
*Citation:* [CONFIDENT] Holley, R., Stroock, D. W. (1987), "Logarithmic Sobolev Inequalities and Stochastic Ising Models", Section 1, "Bounded density perturbations preserve spectral gaps"

**Step 5: Ergodicity and global uniqueness**
*Claim:* The uniform spectral gap forces the transition semigroups to converge to $\mu$ for every deterministic initial condition, precluding other singular invariant measures.
*Citation:* [CONFIDENT] Da Prato, G., Zabczyk, J. (1996), Ergodicity for Infinite Dimensional Systems, Chapter 4, "Doob's theorem and upgrading $L^2$ convergence"

**Coverage Summary**
- Steps confidently cited: 4
- Steps approximately cited: 1
- Steps unable to locate: 0

**Notes**
- **Step 3** unrigorously exchanges $\lim_{n \to \infty}$ and $\lim_{t \to \infty}$. Passing invariance to the limit strictly requires common dominating measure bounds that often fail for singular local-time limits.
- **Step 5** is the fatal gap of the proof: it conflates exponential convergence in $L^2(\mu)$ with everywhere uniform convergence, completely glossing over the Strong Feller property required to actually force total variation collapse from arbitrary initial conditions.