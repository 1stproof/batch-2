**Annotated Proof**

**Step 1: Gibbs measures for approximated SPDEs**
*Claim:* For the approximated reversible gradient SPDE, the unique invariant probability measure is given by the explicitly normalized Gibbs density with respect to the Brownian bridge measure $P_0$.
*Citation:* [APPROX] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions, Chapter 11, "covers the construction and uniqueness of invariant measures for infinite-dimensional gradient SPDEs with smooth drifts"

**Step 2: Brownian bridge zero-level set**
*Claim:* Under the Brownian bridge measure $P_0$, the set of zeros $\{x \in [0,1] : u(x) = 0\}$ has Lebesgue measure zero almost surely, allowing the integrated heat kernel to converge to $\text{sgn}(u(x))$ almost everywhere.
*Citation:* [CONFIDENT] Revuz, D., Yor, M. / 1999 — Continuous Martingales and Brownian Motion, Chapter XI, "furnishes the canonical occupation-time and Fubini arguments proving that the zero-level set of a Brownian path has zero Lebesgue measure"

**Step 3: Weak limit exchange for invariance**
*Claim:* The weak convergence $u^n(t) \to u(t)$ combined with pointwise convergence of densities bounded by $e^1$ allows the invariance of $\mu_n$ to pass safely to the limiting measure $\mu$.
*Citation:* [CONFIDENT] Ethier, S. N., Kurtz, T. G. / 1986 — Markov Processes: Characterization and Convergence, Chapter 4, Section 9, "details the tightness and uniform Feller conditions strictly required to rigorously pass invariance to a weak limit"

**Step 4: Uniqueness via topological irreducibility**
*Claim:* A topologically irreducible Markov process on a connected state space that is reversible with respect to a full-support measure can possess at most one invariant measure.
*Citation:* [CONFIDENT] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems, Chapter 4, "details Doob's Theorem in infinite dimensions, mathematically demonstrating that uniqueness strictly requires the Strong Feller property alongside irreducibility"

**Coverage Summary**
- Steps confidently cited: 3
- Steps approximately cited: 1
- Steps unable to locate: 0

**Notes**
- **Step 3 Flag:** The proof attempts a naive weak limit exchange ($P^n_t f \to P_t f$) inside the integral. It entirely glosses over the required uniform-in-time Feller continuity and Krylov-Bogoliubov tightness bounds.
- **Step 4 Flag:** The final step hinges on a critical fallacy. In infinite dimensions, topological irreducibility alone does not prevent the existence of multiple mutually singular invariant measures; the Strong Feller property is mandatory. Additionally, the singular drift violently violates the infinite-dimensional Novikov conditions needed to legitimately claim irreducibility via additive noise.