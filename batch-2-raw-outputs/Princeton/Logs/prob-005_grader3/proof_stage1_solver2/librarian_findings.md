# Librarian Findings — grader3_150540d79081_proof_stage1_solver2_20260531_010543
**Generated:** 2026-05-31T01:09:32  
**Inputs:** notebook=7629 chars, proof=8146 chars, gap_report=4286 chars  
**Date restriction:** none (FP v2 — recent works allowed)  

---

## Citation IDs (aggregator-only)
```json
{
  "arxiv": [],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

## Citation IDs (union: aggregator + all draws)
```json
{
  "arxiv": [],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

---

# Stage 1 — Gauntlet (aggregator output)

## VERY RELATED
- [Monograph] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press — IDs: no ID — Proves that Doob's Theorem in infinite dimensions strictly requires the Strong Feller property to deduce unique ergodicity, directly refuting the proof's central fallacy. — search: hairer ergodic properties of markov processes pdf
- [Monograph] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press — IDs: no ID — Details the infinite-dimensional Novikov conditions required for Girsanov's theorem, showing why a singular delta drift fails the integrability bounds needed to establish topological irreducibility. — search: hairer introduction to stochastic pdes pdf
- [Book] Ethier, S. N., Kurtz, T. G. / 1986 — Markov Processes: Characterization and Convergence — Wiley — IDs: no ID — Details the tightness and uniform Feller conditions required to rigorously pass invariant measures to a weak limit, addressing the invalid limit-exchange step. — search: eberle markov processes lecture notes pdf
- [Monograph] Ma, Z.-M., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer — IDs: no ID — Develops the foundational framework for rigorously deriving invariant measures and verifying reversibility for singular drifts via Dirichlet forms. — search: rockner dirichlet forms infinite dimensional pdf
- [Paper] Albeverio, S., Bogachev, V., Röckner, M. / 1999 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics — IDs: no ID — Demonstrates that infinite-dimensional diffusions can admit multiple mutually singular invariant measures despite having full topological support, debunking the proof's final uniqueness claim. — search: albeverio bogachev rockner uniqueness invariant measures diffusions pdf
- [Paper] Zambotti, L. / 2001 — A reflected one-dimensional stochastic heat equation as symmetric Dirichlet process — Probability Theory and Related Fields — IDs: no ID — Constructs the transition semigroup for an SPDE with a singular delta-type drift, showing how to handle local time when standard Girsanov arguments fail. — search: zambotti spdes with reflection pdf
- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric dynamics with respect to the 3-d Bessel bridge — Journal of Functional Analysis — IDs: no ID — Establishes rigorous integration-by-parts formulas on path space for singular SPDEs, providing the exact machinery needed to justify the invariant measure of the approximating equations. — search: zambotti reflected stochastic heat equation bessel bridge pdf

## RELATED
- [Paper] Hairer, M. / 2002 — Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling — Probability Theory and Related Fields — IDs: no ID — Introduces asymptotic coupling techniques to bypass the Strong Feller requirement and establish unique ergodicity when non-Lipschitz singular drifts break classical smoothing. — search: hairer exponential mixing asymptotic coupling pdf
- [Paper] Jona-Lasinio, G., Mitter, P. K. / 1985 — On the stochastic quantization of field theory — Communications in Mathematical Physics — IDs: no ID — The foundational paper establishing integration-by-parts formulas for constructing formal Gibbs measures as invariant distributions for gradient stochastic evolutions. — search: jona-lasinio mitter stochastic quantization pdf
- [Lecture notes] Hairer, M. / 2006 — Ergodic properties of Markov processes — Author's webpage — IDs: no ID — Outlines how the Strong Feller property forces a contradiction between mutually singular stationary measures, answering the grader's specific scaffolding question. — search: hairer ergodic properties of markov processes pdf
- [Monograph] Revuz, D., Yor, M. / 1999 — Continuous Martingales and Brownian Motion — Springer — IDs: no ID — Provides the canonical Fubini argument proving that the zero-level set of a Brownian path has Lebesgue measure zero almost surely. — search: morters peres brownian motion pdf

## SOMEWHAT RELATED
- [Book] Karatzas, I., Shreve, S. E. / 1991 — Brownian Motion and Stochastic Calculus — Springer — IDs: no ID — Offers alternative coverage of local time and sample path properties, verifying the zero-level set of a Brownian path has zero Lebesgue measure. — search: morters peres brownian motion pdf
- [Book] Mörters, P., Peres, Y. / 2010 — Brownian Motion — Cambridge University Press — IDs: no ID — A modern textbook rigorously detailing the local properties and fractal dimension of the zero-level set of Brownian paths. — search: morters peres brownian motion pdf

## NOT MUCH
- (None)

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [Monograph] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press — IDs: no ID — Proves that Doob's Theorem in infinite dimensions strictly requires the Strong Feller property to deduce unique ergodicity, directly refuting the proof's central fallacy. — search: hairer ergodic properties of markov processes pdf
  - Addresses: Grader A Gap 1 ("Uniqueness False Premise (Fallacy)") and Grader B Gap 8 ("Fallacy: The final uniqueness criterion is invalid without stronger hypotheses").
  - Chapter 4 formally details Doob's theorem for infinite-dimensional systems, establishing that the Strong Feller condition is strictly necessary to rule out mutually singular measures.

- [Paper] Albeverio, S., Bogachev, V., Röckner, M. / 1999 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics — IDs: no ID — Demonstrates that infinite-dimensional diffusions can admit multiple mutually singular invariant measures despite having full topological support, debunking the proof's final uniqueness claim. — search: albeverio bogachev rockner uniqueness invariant measures diffusions pdf
  - Addresses: Grader B Gap 9 ("Fallacy: Showing one invariant measure exists does not address possible invariant measures singular to it.").
  - The main theorems construct explicit infinite-dimensional counterexamples showing that fully supported, topologically irreducible diffusions can possess mutually singular invariant measures.

- [Paper] Zambotti, L. / 2001 — A reflected one-dimensional stochastic heat equation as symmetric Dirichlet process — Probability Theory and Related Fields — IDs: no ID — Constructs the transition semigroup for an SPDE with a singular delta-type drift, showing how to handle local time when standard Girsanov arguments fail. — search: zambotti spdes with reflection pdf
  - Addresses: Grader B Gap 7 ("Fallacy: Reversibility of the limiting singular SPDE with respect to the displayed measure is not proved.").
  - Section 3 uses Dirichlet form techniques to construct the reversible transition semigroup for the SPDE with a singular delta drift, providing the rigorous alternative to invalid Girsanov assumptions.

- [Monograph] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press — IDs: no ID — Details the infinite-dimensional Novikov conditions required for Girsanov's theorem, showing why a singular delta drift fails the integrability bounds needed to establish topological irreducibility. — search: hairer introduction to stochastic pdes pdf
  - Addresses: Grader A Gap 2 ("Topological Irreducibility for Singular Drift (Fallacy)") and Grader B Gap 6.
  - Chapter 10 covers the infinite-dimensional Girsanov theorem and Novikov conditions, mathematically formalizing why a singular distributional drift fails the necessary integrability bounds to deduce strict positivity.

## SUPPORTING

- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric dynamics with respect to the 3-d Bessel bridge — Journal of Functional Analysis — IDs: no ID — Establishes rigorous integration-by-parts formulas on path space for singular SPDEs, providing the exact machinery needed to justify the invariant measure of the approximating equations. — search: zambotti reflected stochastic heat equation bessel bridge pdf
  - Addresses Grader B Gap 1 by providing the precise integration-by-parts machinery needed for the Gibbs calculation involving local times.

- [Book] Ethier, S. N., Kurtz, T. G. / 1986 — Markov Processes: Characterization and Convergence — Wiley — IDs: no ID — Details the tightness and uniform Feller conditions required to rigorously pass invariant measures to a weak limit, addressing the invalid limit-exchange step. — search: eberle markov processes lecture notes pdf
  - Provides the rigorous tightness and martingale problem framework required to safely pass invariance properties to a weak limit.

- [Monograph] Revuz, D., Yor, M. / 1999 — Continuous Martingales and Brownian Motion — Springer — IDs: no ID — Provides the canonical Fubini argument proving that the zero-level set of a Brownian path has Lebesgue measure zero almost surely. — search: morters peres brownian motion pdf
  - Offers the standard Fubini theorem argument needed to resolve Grader B Gap 4 concerning the Lebesgue measure of the Brownian bridge zero-set.

- [Paper] Jona-Lasinio, G., Mitter, P. K. / 1985 — On the stochastic quantization of field theory — Communications in Mathematical Physics — IDs: no ID — The foundational paper establishing integration-by-parts formulas for constructing formal Gibbs measures as invariant distributions for gradient stochastic evolutions. — search: jona-lasinio mitter stochastic quantization pdf
  - Serves as the classic reference for using integration-by-parts to formally construct Gibbs measures for smoothed gradient SPDEs.

- [Paper] Hairer, M. / 2002 — Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling — Probability Theory and Related Fields — IDs: no ID — Introduces asymptotic coupling techniques to bypass the Strong Feller requirement and establish unique ergodicity when non-Lipschitz singular drifts break classical smoothing. — search: hairer exponential mixing asymptotic coupling pdf
  - Useful as an alternative technique to establish unique ergodicity when classical Strong Feller smoothing fails.

- [Monograph] Ma, Z.-M., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer — IDs: no ID — Develops the foundational framework for rigorously deriving invariant measures and verifying reversibility for singular drifts via Dirichlet forms. — search: rockner dirichlet forms infinite dimensional pdf
  - Lays out the background foundational theory for the Dirichlet form approach applied in the Zambotti paper.

## REDUNDANT

- [Lecture notes] Hairer, M. / 2006 — Ergodic properties of Markov processes — Author's webpage — IDs: no ID — Outlines how the Strong Feller property forces a contradiction between mutually singular stationary measures, answering the grader's specific scaffolding question. — search: hairer ergodic properties of markov processes pdf
  - Overlaps heavily with Da Prato & Zabczyk (1996) regarding Doob's theorem and the Strong Feller prerequisite.

- [Book] Karatzas, I., Shreve, S. E. / 1991 — Brownian Motion and Stochastic Calculus — Springer — IDs: no ID — Offers alternative coverage of local time and sample path properties, verifying the zero-level set of a Brownian path has zero Lebesgue measure. — search: morters peres brownian motion pdf
  - Redundant with Revuz & Yor (1999) for establishing the Lebesgue measure of Brownian zero-level sets.

- [Book] Mörters, P., Peres, Y. / 2010 — Brownian Motion — Cambridge University Press — IDs: no ID — A modern textbook rigorously detailing the local properties and fractal dimension of the zero-level set of Brownian paths. — search: morters peres brownian motion pdf
  - Redundant with Revuz & Yor (1999) regarding standard sample path properties of Brownian motion.

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

---

# Stage 3 — Chapter Picker

## Ergodicity for Infinite Dimensional Systems (Da Prato, G., Zabczyk, J., Cambridge University Press, 1996)
_(Proves that Doob's Theorem in infinite dimensions strictly requires the Strong Feller property to deduce unique ergodicity, directly refuting the proof's central fallacy. — search: hairer ergodic properties of markov processes pdf)_

Here are the specific chapters and sections from Da Prato & Zabczyk's *Ergodicity for Infinite Dimensional Systems* (1996) that directly address the gaps in the proof. 

**Chapter 4 (approx.) — Ergodicity and Uniqueness of Invariant Measures**
*   **Which gap it addresses:** Grader A's "Uniqueness False Premise" and Grader B's gap #8 (Invalid uniqueness criterion).
*   **Why:** This chapter formally details **Doob's Theorem** for infinite-dimensional Markov semigroups. It explicitly demonstrates why topological irreducibility alone is fundamentally insufficient for uniqueness: in infinite dimensions, you can easily have mutually singular transition kernels that both have full topological support. The text shows how the **Strong Feller property** is strictly required to regularize the kernels, forcing them to be mutually absolutely continuous and thereby preventing multiple singular invariant measures.

**Chapter 2 (approx.) — General Properties of Invariant Measures**
*   **Which gap it addresses:** Grader B's gap #9 ("Showing one invariant measure exists does not address possible invariant measures singular to it").
*   **Why:** This section covers the structure of the space of invariant measures, specifically the **Ergodic Decomposition Theorem**. It proves that the extremal points of the convex set of invariant measures are mutually singular, cleanly explaining why successfully constructing one limiting Gibbs measure (as the proof does) provides zero mathematical leverage against the existence of distinct, singular stationary measures elsewhere in the state space. 

**Chapter 7 (approx.) — Stochastic Reaction-Diffusion Equations / Irreducibility**
*   **Which gap it addresses:** Grader A's gap #2 and Grader B's gap #6 (Topological Irreducibility for Singular Drift).
*   **Why:** This chapter translates the abstract theory into concrete SPDEs, detailing how to actually prove topological irreducibility using **approximate controllability** and **Girsanov's theorem**. It shows that while additive noise on all Fourier modes is helpful, you must satisfy strict integrability/Novikov conditions to handle the drift—proving why the author's assumption that additive noise automatically overpowers a highly singular, non-Lipschitz $\delta_0(u)$ drift is a fatal fallacy.

## Stochastic Equations in Infinite Dimensions (Da Prato, G., Zabczyk, J., Cambridge University Press, 1992)
_(Details the infinite-dimensional Novikov conditions required for Girsanov's theorem, showing why a singular delta drift fails the integrability bounds needed to establish topological irreducibility. — search: hairer introduction to stochastic pdes pdf)_

Here are the specific chapters and sections from Da Prato and Zabczyk (1992) that directly address the mathematical gaps identified by the graders.

**Chapter 11 (approx.) — Ergodicity / Uniqueness of Invariant Measures**
*   **Which gap it addresses:** Grader A's Gap 1 and Grader B's Gap 8 (Uniqueness False Premise / Fallacy). 
*   **Why:** This chapter details the conditions for uniqueness of invariant measures in infinite-dimensional Hilbert spaces. It explicitly covers Doob’s Theorem, demonstrating that topological irreducibility is mathematically insufficient to rule out mutually singular invariant measures unless it is paired with a strong regularizing condition like the Strong Feller property.

**Chapter 10 — Absolute Continuity of Measures / Equivalence of Transition Probabilities**
*   **Which gap it addresses:** Grader A's Gap 2, Grader B's Gap 6 (Topological Irreducibility for Singular Drift), and Scaffolding Q2.
*   **Why:** This chapter establishes the infinite-dimensional Girsanov theorem for SPDEs. It explains how topological irreducibility is standardly proven by showing equivalence to the linear equation's transition kernels, which strictly requires the nonlinear drift to satisfy Novikov’s condition (finite energy in the Cameron-Martin space). It provides the exact mechanism for why a non-Lipschitz, distributional drift like $\delta_0(u)$ violently fails the required integrability bounds.

**Chapter 6 (approx.) — Stationary Solutions for Linear Equations**
*   **Which gap it addresses:** Grader B's Scaffolding Q1 and Gap 5 (Full support and invariance of the reference Gaussian measure).
*   **Why:** This chapter rigorously covers the invariant probability measures associated with infinite-dimensional Ornstein-Uhlenbeck processes. It supplies the foundational integration-by-parts identities and spectral conditions required to prove that the baseline Gaussian measure (from the unperturbed stochastic heat equation) is invariant and possesses full topological support.

## Markov Processes: Characterization and Convergence (Ethier, S. N., Kurtz, T. G., Wiley, 1986)
_(Details the tightness and uniform Feller conditions required to rigorously pass invariant measures to a weak limit, addressing the invalid limit-exchange step. — search: eberle markov processes lecture notes pdf)_

Here are the specific chapters and sections from Ethier & Kurtz (1986) that address the invalid limit-exchange steps and tightness fallacies identified in the grader reports:

**Chapter 4, Section 9 (approx.): Invariant Measures / Stationary Distributions**
- **Which gap it addresses:** Grader B #4 ("How can one pass invariance to a limit when both the invariant measures and transition kernels vary?") and IPT-70 (Unjustified Weak Limit Exchange).
- **Why:** This section contains the rigorous functional analysis required to pass invariant measures to a weak limit (e.g., Theorem 4.9.3). It explicitly shows that weak limit exchange $\mu_n \to \mu$ requires corresponding convergence of the generators $A_n \to A$ acting on a core of test functions, and that the limiting semigroup must possess sufficient Feller continuity to guarantee $\mu$ is actually invariant for $P_t$. 

**Chapter 4, Section 8 (approx.): Tightness for Markov Processes**
- **Which gap it addresses:** IPT-70 ("Bypassing... uniform-in-time Krylov-Bogoliubov tightness strictly invalidates the assumption..."). 
- **Why:** It details the uniform bounds and Krylov-Bogoliubov tightness criteria necessary to extract a weakly convergent subsequence from $\{\mu_n\}$. It provides the exact Lyapunov or compact-containment conditions required to prevent mass from escaping to infinity, a step the proof entirely glosses over when assuming bounded densities automatically yield a valid limiting probability measure.

**Chapter 2: Operator Semigroups / Feller Semigroups**
- **Which gap it addresses:** Grader A #1 and Grader B #8 (Failure to establish Strong Feller / invoking uniqueness via topological irreducibility alone).
- **Why:** This chapter defines the hierarchy of Feller, Strong Feller, and strongly continuous semigroups. Reviewing it will demonstrate why weak convergence of approximated processes does not automatically confer the Strong Feller smoothing required to safely apply Doob's Theorem to mutually singular competing measures. 

**Chapter 8, Section 2 (approx.): Stochastic Differential Equations and Martingale Problems**
- **Which gap it addresses:** Grader B #2 (Asserting uniqueness/ergodicity of the approximating SPDEs without a valid argument) and Grader A #2.
- **Why:** This section establishes the link between well-posedness of martingale problems, non-degenerate noise, and the strict positivity/irreducibility of transition kernels. It clarifies the integrability conditions (e.g., localized Girsanov/Novikov prerequisites) needed to rigorously claim that the smoothed Gaussian drifts actually result in unique invariant measures for the approximating sequence.

## Continuous Martingales and Brownian Motion (Revuz, D., Yor, M., Springer, 1999)
_(Provides the canonical Fubini argument proving that the zero-level set of a Brownian path has Lebesgue measure zero almost surely. — search: morters peres brownian motion pdf)_

Here are the specific chapters and sections from Revuz & Yor's *Continuous Martingales and Brownian Motion* that address the critical gaps in the proof:

**Chapter II: Brownian Motion, Section 2 (approx.) — "Some Properties of the Paths"**
* **Which gap it addresses:** Grader B's slip #4 (The Brownian-bridge zero-set claim needs a proof).
* **Why:** This section provides the canonical Fubini theorem argument confirming that the zero-level set of a Brownian path has Lebesgue measure zero almost surely (by showing $\mathbb{E}[\int_0^t \mathbb{1}_{\{B_s = 0\}} ds] = \int_0^t \mathbb{P}(B_s = 0) ds = 0$). This directly patches the slip regarding the $P_0$-almost everywhere well-definedness of the signum function.

**Chapter VIII: Girsanov's Theorem and First Applications, Section 1 — "Girsanov's Theorem"**
* **Which gap it addresses:** Grader A's fallacy #2 (Topological Irreducibility for Singular Drift / Novikov's condition).
* **Why:** The grader correctly points out that standard topological irreducibility via additive noise requires the drift to satisfy integrability bounds (Novikov's condition). This section explicitly details Novikov's criterion for continuous martingales, showing exactly why applying Girsanov to the highly singular $\delta_0(u)$ fails to yield the mutually absolutely continuous transition kernels the solver is hallucinating.

**Chapter VI: Local Times, Section 1 — "Tanaka's Formula and Continuous Local Times"**
* **Which gap it addresses:** (beyond grader's named gaps / Notebook IPT-72: Fabricated Spatial Hölder Regularity).
* **Why:** The SPDE's distributional drift $\delta_0(u)$ formally evaluates to the local time of the process at zero. This chapter rigorously defines local time via Tanaka's formula as a singular, non-decreasing continuous process rather than a process with a valid Lebesgue density. Reviewing this will force the solver to abandon attempts to treat the singular drift as a bounded or regular perturbation.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [Monograph] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press — IDs: no ID — Proves that Doob's Theorem in infinite dimensions strictly requires the Strong Feller property to deduce unique ergodicity, directly refuting the proof's central fallacy. — search: hairer ergodic properties of markov processes pdf
  * **Gap addressed:** Grader A, Gap 1 ("Uniqueness False Premise (Fallacy)") and Grader B, Gap 8 ("Fallacy: The final uniqueness criterion is invalid without stronger hypotheses").
  * **Load-bearing piece:** Chapter 4 establishes the precise infinite-dimensional formulations of Doob's Theorem and the absolute necessity of the Strong Feller condition to guarantee a unique invariant measure for Markov semigroups.

- [Paper] Albeverio, S., Bogachev, V., Röckner, M. / 1999 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics — IDs: no ID — Demonstrates that infinite-dimensional diffusions can admit multiple mutually singular invariant measures despite having full topological support, debunking the proof's final uniqueness claim. — search: albeverio bogachev rockner uniqueness invariant measures diffusions pdf
  * **Gap addressed:** Grader B, Gap 9 ("Fallacy: Showing one invariant measure exists does not address possible invariant measures singular to it") and Grader A, Gap 1.
  * **Load-bearing piece:** The core theorems and counterexamples section showing how infinite-dimensional diffusions can simultaneously support mutually singular invariant measures despite having full topological support.

- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric dynamics with respect to the 3-d Bessel bridge — Journal of Functional Analysis — IDs: no ID — Establishes rigorous integration-by-parts formulas on path space for singular SPDEs, providing the exact machinery needed to justify the invariant measure of the approximating equations. — search: zambotti reflected stochastic heat equation bessel bridge pdf
  * **Gap addressed:** Grader B, Gap 1 ("Fallacy: The invariant measures for the approximating SPDEs are asserted without proving the integration-by-parts/Gibbs calculation") and Grader B, Gap 7 ("Fallacy: Reversibility of the limiting singular SPDE with respect to the displayed measure is not proved").
  * **Load-bearing piece:** The section explicitly constructing the infinite-dimensional integration-by-parts formulas involving local time and the 3-d Bessel bridge measure to define reversibility for this exact singular drift.


## SUPPORTING

- [Monograph] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press — IDs: no ID — Details the infinite-dimensional Novikov conditions required for Girsanov's theorem, showing why a singular delta drift fails the integrability bounds needed to establish topological irreducibility. — search: hairer introduction to stochastic pdes pdf
  * *Note:* Provides the theoretical background to address Grader A, Gap 2 ("Topological Irreducibility for Singular Drift") showing where the Girsanov/Novikov applications break down.

- [Paper] Zambotti, L. / 2001 — A reflected one-dimensional stochastic heat equation as symmetric Dirichlet process — Probability Theory and Related Fields — IDs: no ID — Constructs the transition semigroup for an SPDE with a singular delta-type drift, showing how to handle local time when standard Girsanov arguments fail. — search: zambotti spdes with reflection pdf
  * *Note:* Supplements the JFA paper above, offering the specific Dirichlet form construction for the SPDE's transition semigroup.

- [Monograph] Revuz, D., Yor, M. / 1999 — Continuous Martingales and Brownian Motion — Springer — IDs: no ID — Provides the canonical Fubini argument proving that the zero-level set of a Brownian path has Lebesgue measure zero almost surely. — search: morters peres brownian motion pdf
  * *Note:* Provides the canonical proof to fix Grader B, Gap 4 ("Slip: The Brownian-bridge zero-set claim needs a proof").

- [Book] Ethier, S. N., Kurtz, T. G. / 1986 — Markov Processes: Characterization and Convergence — Wiley — IDs: no ID — Details the tightness and uniform Feller conditions required to rigorously pass invariant measures to a weak limit, addressing the invalid limit-exchange step. — search: eberle markov processes lecture notes pdf
  * *Note:* Addresses Scaffolding Question 4 from Grader B on passing invariant measures to a limit when both the measure and transition kernels vary.

- [Monograph] Ma, Z.-M., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer — IDs: no ID — Develops the foundational framework for rigorously deriving invariant measures and verifying reversibility for singular drifts via Dirichlet forms. — search: rockner dirichlet forms infinite dimensional pdf
  * *Note:* Essential foundational theory for constructing Dirichlet forms and verifying reversibility (Grader B, Gap 7) in infinite dimensions.

- [Paper] Hairer, M. / 2002 — Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling — Probability Theory and Related Fields — IDs: no ID — Introduces asymptotic coupling techniques to bypass the Strong Feller requirement and establish unique ergodicity when non-Lipschitz singular drifts break classical smoothing. — search: hairer exponential mixing asymptotic coupling pdf
  * *Note:* Offers an alternative pathway to unique ergodicity using asymptotic coupling when Strong Feller is unavailable.


## REDUNDANT

- [Lecture notes] Hairer, M. / 2006 — Ergodic properties of Markov processes
  * *Overlap:* Redundant with Da Prato & Zabczyk 1996 for establishing how the Strong Feller property forces uniqueness.

- [Book] Karatzas, I., Shreve, S. E. / 1991 — Brownian Motion and Stochastic Calculus
  * *Overlap:* Redundant with Revuz & Yor 1999 for addressing the zero-level set properties of Brownian paths.

- [Book] Mörters, P., Peres, Y. / 2010 — Brownian Motion
  * *Overlap:* Redundant with Revuz & Yor 1999 for proving properties of Brownian zero-level sets.


## PERIPHERAL

- [Paper] Jona-Lasinio, G., Mitter, P. K. / 1985 — On the stochastic quantization of field theory
  * *Note:* While a classic for proving formal Gibbs measures as invariants via integration-by-parts, it applies to smooth polynomial drifts (like stochastic quantization) rather than providing the specialized Bessel bridge/local time machinery needed for a singular Dirac delta drift.


## UNFAMILIAR

*(None)*

## Narrower draw 2
## LOAD-BEARING

- [Monograph] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press — IDs: no ID — Proves that Doob's Theorem in infinite dimensions strictly requires the Strong Feller property to deduce unique ergodicity, directly refuting the proof's central fallacy. — search: hairer ergodic properties of markov processes pdf
  - **Gap:** Grader A, Area 1 ("Uniqueness False Premise (Fallacy)") and Grader B, Area 8 ("Fallacy: The final uniqueness criterion is invalid without stronger hypotheses...").
  - **Load-bearing piece:** Chapter 4 details Doob's Theorem in infinite dimensions, explicitly proving why the Strong Feller property is mathematically mandatory to deduce unique ergodicity from topological irreducibility.

- [Paper] Zambotti, L. / 2001 — A reflected one-dimensional stochastic heat equation as symmetric Dirichlet process — Probability Theory and Related Fields — IDs: no ID — Constructs the transition semigroup for an SPDE with a singular delta-type drift, showing how to handle local time when standard Girsanov arguments fail. — search: zambotti spdes with reflection pdf
  - **Gap:** Grader B, Area 1 ("Fallacy: The invariant measures for the approximating SPDEs are asserted without proving the integration-by-parts/Gibbs calculation.")
  - **Load-bearing piece:** Section 3 derives the explicit infinite-dimensional integration-by-parts formulas on path space required to rigorously justify the formal Gibbs calculation for this exact singular SPDE.

- [Paper] Albeverio, S., Bogachev, V., Röckner, M. / 1999 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics — IDs: no ID — Demonstrates that infinite-dimensional diffusions can admit multiple mutually singular invariant measures despite having full topological support, debunking the proof's final uniqueness claim. — search: albeverio bogachev rockner uniqueness invariant measures diffusions pdf
  - **Gap:** Grader B, Area 9 ("Fallacy: Showing one invariant measure exists does not address possible invariant measures singular to it.")
  - **Load-bearing piece:** The main theorems provide rigorous explicit counterexamples of infinite-dimensional diffusions that simultaneously admit multiple mutually singular invariant measures despite possessing full topological support.

- [Monograph] Revuz, D., Yor, M. / 1999 — Continuous Martingales and Brownian Motion — Springer — IDs: no ID — Provides the canonical Fubini argument proving that the zero-level set of a Brownian path has Lebesgue measure zero almost surely. — search: morters peres brownian motion pdf
  - **Gap:** Grader B, Area 4 ("Slip: The Brownian-bridge zero-set claim needs a proof, for example by integrating pointwise zero probabilities over space.")
  - **Load-bearing piece:** Chapter XI (Local Times) furnishes the canonical occupation-time and Fubini limit arguments needed to prove rigorously that the zero-level set of a standard Brownian path has zero Lebesgue measure almost surely.

## SUPPORTING

- [Monograph] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press — Details infinite-dimensional Novikov conditions and Girsanov bounds, crucial for seeing why the singular drift fails standard irreducibility bounds (addresses Grader A, Area 2).
- [Monograph] Ma, Z.-M., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer — Supplies the foundational functional analysis framework to rigorously establish reversibility for singular drifts (addresses Grader B, Area 7).
- [Book] Ethier, S. N., Kurtz, T. G. / 1986 — Markov Processes: Characterization and Convergence — Wiley — Provides the required martingale problem and tightness theorems to rigorously justify passing invariance to weak limits.
- [Paper] Hairer, M. / 2002 — Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling — Probability Theory and Related Fields — Offers asymptotic coupling as a rigorous alternative to bypass the absent Strong Feller property for non-Lipschitz drifts.
- [Paper] Jona-Lasinio, G., Mitter, P. K. / 1985 — On the stochastic quantization of field theory — Communications in Mathematical Physics — Provides necessary historical framing and structural methodology for constructing formal Gibbs measures via stochastic quantization.

## REDUNDANT

- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric dynamics with respect to the 3-d Bessel bridge — Overlaps entirely with the LOAD-BEARING Zambotti (2001) PTRF entry on resolving integration-by-parts for delta drifts.
- [Lecture notes] Hairer, M. / 2006 — Ergodic properties of Markov processes — Overlaps with the LOAD-BEARING Da Prato & Zabczyk (1996) entry in refuting uniqueness claims strictly by explaining the Strong Feller requirements.
- [Book] Karatzas, I., Shreve, S. E. / 1991 — Brownian Motion and Stochastic Calculus — Overlaps with the LOAD-BEARING Revuz & Yor (1999) entry regarding the local times and zero-level set measurements of Brownian paths.
- [Book] Mörters, P., Peres, Y. / 2010 — Brownian Motion — Overlaps with the LOAD-BEARING Revuz & Yor (1999) entry on properties of the Brownian zero-level set.

## PERIPHERAL
*(None — all listed works map directly to the specific measure-theoretic or PDE-theoretic critiques logged by the graders.)*

## UNFAMILIAR
*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and topic-keyed open-access substitutes that address the specific mathematical gaps identified by the graders. I have focused heavily on the texts that rigorously differentiate between topological irreducibility and the Strong Feller property in infinite dimensions, as that is the primary fallacy collapsing the proof.

**1. Da Prato, G. and Zabczyk, J. / 1996**
- **Title:** Ergodicity for Infinite Dimensional Systems
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 4 covers Doob's Theorem in infinite dimensions, proving that a Markov semigroup requires *both* topological irreducibility and the Strong Feller property to guarantee that an invariant measure is unique.
- **Topic needed for this proof:** The strict necessity of the Strong Feller property (or an equivalent smoothing condition) to rule out mutually singular stationary measures in infinite dimensions.
- **Open-access substitute for that topic:** (open-access for topic: Doob's theorem and Strong Feller for Markov semigroups) — M. Hairer / 2008 / Ergodic Properties of Markov Processes / lecture notes on author webpage
- **Connection:** Directly invalidates the proof’s core claim (Grader A, gap 1; Grader B, gap 8) that topological irreducibility and reversibility alone are sufficient for global uniqueness.
- **Web search query:** `hairer ergodic properties markov processes pdf`
- **Confidence (bibliographic):** HIGH

**2. Da Prato, G. and Zabczyk, J. / 1992 (2nd ed. 2014)**
- **Title:** Stochastic Equations in Infinite Dimensions
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 10 and 11 cover infinite-dimensional Novikov conditions, Girsanov's theorem for cylindrical Wiener processes, and the construction of invariant measures for gradient SPDEs.
- **Topic needed for this proof:** The infinite-dimensional Novikov condition bounds required to validly apply Girsanov's theorem to establish transition kernel positivity.
- **Open-access substitute for that topic:** (open-access for topic: Girsanov theorem and Novikov condition for SPDEs) — M. Hairer / 2009 / An Introduction to Stochastic PDEs / arxiv preprint or author webpage
- **Connection:** Explains why Grader A flagged the topological irreducibility deduction (gap 2) as a fallacy; the singular $\delta_0(u)$ drift categorically fails the integrability bounds needed for the standard Girsanov shift to establish strict positivity.
- **Web search query:** `hairer introduction to stochastic pdes pdf`
- **Confidence (bibliographic):** HIGH

**3. Hairer, M. / 2002**
- **Title:** Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling
- **Type:** paper
- **Venue:** Probability Theory and Related Fields
- **Main result or relevant chapter/section:** Introduces asymptotic coupling techniques to prove unique ergodicity for SPDEs where the classical Strong Feller property fails (e.g., due to degenerate noise or non-Lipschitz singular drifts).
- **Topic needed for this proof:** Bypassing the Strong Feller requirement using a synchronous coupling argument to force solutions together asymptotically in total variation.
- **Open-access substitute for that topic:** (open-access for topic: asymptotic coupling ergodicity SPDE) — M. Hairer / 2002 / Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling / author webpage draft
- **Connection:** Provides the specific, modern fallback scaffolding requested by Grader A ("or use a coupling argument") to repair the uniqueness claim when the singular drift breaks classical smoothing.
- **Web search query:** `hairer exponential mixing asymptotic coupling pdf`
- **Confidence (bibliographic):** HIGH

**4. Mörters, P. and Peres, Y. / 2010**
- **Title:** Brownian Motion
- **Type:** book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 2 covers the precise local properties and fractal dimension of the zero-level set of Brownian paths, proving it has Lebesgue measure zero almost surely.
- **Topic needed for this proof:** Rigorous proof that the spatial zero-set of a Brownian bridge is Lebesgue measure zero.
- **Open-access substitute for that topic:** (open-access for topic: Brownian zero set properties) — P. Mörters, Y. Peres / 2008 / Brownian Motion (book draft) / author webpage
- **Connection:** Fills the slip identified by Grader B (gap 4) where the proof asserts without derivation that the Brownian bridge's zero-set has Lebesgue measure zero.
- **Web search query:** `morters peres brownian motion pdf`
- **Confidence (bibliographic):** HIGH

**5. Jona-Lasinio, G. and Mitter, P. K. / 1985**
- **Title:** On the stochastic quantization of field theory
- **Type:** paper
- **Venue:** Communications in Mathematical Physics
- **Main result or relevant chapter/section:** The foundational paper establishing integration-by-parts formulas and using them to rigorously construct formal Gibbs measures as invariant distributions for infinite-dimensional gradient stochastic evolutions.
- **Topic needed for this proof:** The specific integration-by-parts derivation required to prove a constructed Gibbs measure is actually invariant for the associated SPDE semigroup.
- **Open-access substitute for that topic:** (open-access for topic: Gibbs measures for gradient SPDEs) — J. C. Mourrat / 2022 / Gibbs measures for stochastic PDEs / lecture notes on author webpage
- **Connection:** Addresses Grader B's gap 1 (the invariant measures for the approximating SPDEs are asserted without actually proving the integration-by-parts / Gibbs calculation).
- **Web search query:** `jona-lasinio mitter stochastic quantization pdf`
- **Confidence (bibliographic):** HIGH

**6. Albeverio, S., Bogachev, V., and Röckner, M. / 1999**
- **Title:** On uniqueness of invariant measures for finite- and infinite-dimensional diffusions
- **Type:** paper
- **Venue:** Communications on Pure and Applied Mathematics
- **Main result or relevant chapter/section:** Establishes conditions under which irreducible, quasi-regular Dirichlet forms over infinite-dimensional state spaces possess at most one invariant probability measure within a specific absolute continuity class.
- **Topic needed for this proof:** Uniqueness of invariant measures for infinite-dimensional systems via symmetric Dirichlet forms rather than semigroup transitions.
- **Open-access substitute for that topic:** (open-access for topic: uniqueness of invariant measures via infinite-dimensional Dirichlet forms) — M. Röckner / 1998 / Dirichlet Forms on Infinite Dimensional State Spaces and Applications / CIME Summer School lecture notes (often hosted on author webpages).
- **Connection:** The notebook references the "Albeverio-Bogachev-Röckner Uniqueness Theorem" (SNT-4). If the proof is to be salvaged without the Strong Feller property, reformulating the limiting singular SPDE as a quasi-regular Dirichlet form using this theorem's framework is the most viable path.
- **Web search query:** `bogachev rockner uniqueness invariant measures diffusions pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and open-access substitutes that directly address the gaps and fallacies identified by the graders, particularly focusing on the prerequisites for Doob's theorem, the existence of mutually singular invariant measures in infinite dimensions, and the integration-by-parts machinery required for singular SPDEs.

- **Authors / Year:** Da Prato, G., Zabczyk, J. / 1996
- **Title:** Ergodicity for Infinite Dimensional Systems
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 4 covers invariant measures for infinite-dimensional Markov semigroups, specifically formulating Doob's Theorem and proving that the Strong Feller property (alongside topological irreducibility) is an absolute prerequisite to deduce uniqueness.
- **Topic needed for this proof:** Doob's Theorem in infinite dimensions and the strict requirement to establish the Strong Feller property to deduce invariant measure uniqueness.
- **Open-access substitute for that topic:** (open-access for topic: Doob's theorem and Strong Feller for SPDEs) — Hairer, M. / 2006 / Ergodic properties of Markov processes / Author's webpage lecture notes
- **Connection:** Refutes the central logical fallacy of the proof (Grader A, Critique 1; Grader B, Critique 8) that topological irreducibility and reversibility alone are sufficient to prove uniqueness for infinite-dimensional systems.
- **Web search query:** `hairer ergodic properties of markov processes pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Hairer, M. / 2006
- **Title:** Ergodic properties of Markov processes
- **Type:** lecture notes
- **Venue:** Author's webpage (University of Warwick / Imperial College London)
- **Main result or relevant chapter/section:** Provides a highly readable, modern exposition of ergodic theory for infinite-dimensional Markov processes, detailing how Strong Feller, asymptotic Strong Feller, or Harris coupling conditions physically force transition kernels to overlap.
- **Topic needed for this proof:** The exact structural conditions (Strong Feller or topological coupling) required to mathematically force a contradiction between two hypothetically mutually singular invariant measures.
- **Open-access substitute for that topic:** (Self is open-access)
- **Connection:** Directly answers Grader A's first scaffolding question about how Strong Feller operates to collapse mutually singular measures, outlining the exact machinery the proof is missing.
- **Web search query:** `hairer ergodic properties of markov processes pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Albeverio, S., Bogachev, V. I., Röckner, M. / 1999
- **Title:** On uniqueness of invariant measures for finite- and infinite-dimensional diffusions
- **Type:** paper
- **Venue:** Communications on Pure and Applied Mathematics
- **Main result or relevant chapter/section:** Investigates conditions for uniqueness of invariant measures and rigorously constructs examples of infinite-dimensional diffusions that admit multiple mutually singular invariant measures, even when the reference measure has full topological support.
- **Topic needed for this proof:** The phenomenon in infinite dimensions where explicitly constructing one full-support invariant measure does not preclude the coexistence of other mutually singular invariant measures.
- **Open-access substitute for that topic:** (open-access for topic: non-uniqueness and mutually singular measures for singular diffusions) — Eberle, A. / 1999 / Uniqueness and non-uniqueness of semigroups generated by singular diffusion operators / Springer Lecture Notes in Mathematics 1718 (drafts on author webpage)
- **Connection:** Answers Grader B's fifth question and ninth critique, formally debunking the proof's final leap which assumes that finding one invariant measure excludes all others.
- **Web search query:** `albeverio bogachev rockner uniqueness invariant measures diffusions pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Da Prato, G., Zabczyk, J. / 1992
- **Title:** Stochastic Equations in Infinite Dimensions
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 10 covers the infinite-dimensional Girsanov theorem, defining the Cameron-Martin space and Novikov's condition for infinite-dimensional Wiener processes.
- **Topic needed for this proof:** The requirement that a drift must satisfy Novikov's integrability condition within the Cameron-Martin space to legitimately apply Girsanov's theorem to deduce transition kernel positivity.
- **Open-access substitute for that topic:** (open-access for topic: Girsanov theorem and Novikov condition for SPDEs) — Hairer, M. / 2009 / An Introduction to Stochastic PDEs / Author's webpage lecture notes
- **Connection:** Addresses Grader A's second critique by showing why topological irreducibility cannot be deduced "by fiat" from additive noise when the singular drift $\delta_0(u)$ violently violates Novikov's condition.
- **Web search query:** `hairer introduction to stochastic pdes pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Zambotti, L. / 2001
- **Title:** A reflected stochastic heat equation as symmetric dynamics with respect to the 3-d Bessel bridge
- **Type:** paper
- **Venue:** Journal of Functional Analysis
- **Main result or relevant chapter/section:** Constructs the invariant measure for a highly singular SPDE (reflection/singular drift) by establishing rigorous integration-by-parts formulas on path space involving the Brownian and Bessel bridges.
- **Topic needed for this proof:** The precise infinite-dimensional integration-by-parts identity on path space required to verify that a singular Gibbs density is actually invariant for a gradient stochastic evolution.
- **Open-access substitute for that topic:** (open-access for topic: integration by parts for SPDEs with singular drift) — Zambotti, L. / 2004 / Integration by parts formulae on convex sets of paths and applications to SPDEs with reflection / arxiv
- **Connection:** Answers Grader B's second scaffolding question and first critique, showing the highly non-trivial mathematical machinery required to justify the invariant measure of the approximating (and limiting) SPDEs.
- **Web search query:** `zambotti reflected stochastic heat equation bessel bridge pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Ma, Z.-M., Röckner, M. / 1992
- **Title:** Introduction to the Theory of (Non-Symmetric) Dirichlet Forms
- **Type:** monograph
- **Venue:** Springer (Universitext)
- **Main result or relevant chapter/section:** Provides the foundational theory for associating a quasi-regular Dirichlet form with a formal Gibbs measure to rigorously construct a reversible Markov process.
- **Topic needed for this proof:** Using the Dirichlet form framework to rigorously establish the reversibility of a limiting singular SPDE with respect to a target reference measure.
- **Open-access substitute for that topic:** (open-access for topic: Dirichlet forms and reversible SPDEs) — Röckner, M. / 1999 / Lp-analysis of finite and infinite dimensional diffusion operators / Lecture Notes in Mathematics 1715
- **Connection:** Addresses Grader B's seventh critique by outlining the missing structural machinery required to prove that the limiting singular SPDE is indeed reversible with respect to the constructed measure.
- **Web search query:** `rockner lp analysis infinite dimensional diffusion operators pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Revuz, D., Yor, M. / 1999
- **Title:** Continuous Martingales and Brownian Motion
- **Type:** monograph
- **Venue:** Springer (Grundlehren der mathematischen Wissenschaften)
- **Main result or relevant chapter/section:** Chapter XI rigorously covers local times and the zero set of Brownian paths, proving via Fubini's theorem that the zero-level set of a Brownian motion (and by extension the Brownian bridge) has Lebesgue measure zero almost surely.
- **Topic needed for this proof:** The pointwise integration argument establishing that the zero set of a Brownian bridge has zero Lebesgue measure.
- **Open-access substitute for that topic:** (open-access for topic: zero set of Brownian motion Lebesgue measure zero) — Mörters, P., Peres, Y. / 2010 / Brownian Motion / Cambridge University Press (draft on author webpage)
- **Connection:** Closes the "slip" identified in Grader B's fourth critique by providing the canonical proof needed to rigorously define the $\text{sgn}(u(x))$ functional $P_0$-almost everywhere without assuming it.
- **Web search query:** `morters peres brownian motion pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed open-access substitutes that address the specific gaps in the proof, particularly regarding infinite-dimensional ergodicity, singular drifts, and limit-exchange justifications.

- **Authors / Year:** Giuseppe Da Prato, Jerzy Zabczyk / 1996
- **Title:** Ergodicity for Infinite Dimensional Systems
- **Type:** Book
- **Venue:** Cambridge University Press + 1996
- **Main result or relevant chapter/section:** Chapter 4 (and Chapter 7) rigorously develops Doob's Theorem for infinite-dimensional SPDEs, proving that uniqueness of the invariant measure requires *both* topological irreducibility and a smoothing condition like the Strong Feller property.
- **Topic needed for this proof:** Doob's Theorem and the necessity of the Strong Feller property for infinite-dimensional Markov semigroups.
- **Open-access substitute for that topic:** (open-access for topic: Doob's Theorem and Strong Feller in infinite dimensions) — M. Hairer / 2009 / An Introduction to Stochastic PDEs / University of Warwick author webpage
- **Connection:** Directly resolves Grader A's Critique 1 and Grader B's Critique 8. The proof’s fatal fallacy is assuming reversibility and irreducibility alone are sufficient for uniqueness, which is false in infinite dimensions without a Strong Feller or coupling argument to prevent mutually singular invariant measures.
- **Web search query:** `hairer introduction stochastic pdes pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Lorenzo Zambotti / 2001
- **Title:** A reflected one-dimensional stochastic heat equation as symmetric Dirichlet process
- **Type:** Paper
- **Venue:** Probability Theory and Related Fields
- **Main result or relevant chapter/section:** Demonstrates how to rigorously construct and analyze the transition semigroup for an SPDE with a singular delta-type drift (which acts as a reflection measure) using Dirichlet forms, completely bypassing the failure of Girsanov's theorem.
- **Topic needed for this proof:** Rigorous construction of topological irreducibility and transition kernels for SPDEs with singular, distribution-valued drifts.
- **Open-access substitute for that topic:** (open-access for topic: SPDEs with singular reflection/delta drifts) — L. Zambotti / 2017 / Random obstacles and SPDEs with reflection / arxiv preprint
- **Connection:** Addresses Grader A's Critique 2 and Grader B's Critique 6. The proof falsely assumes that additive noise trivially implies strictly positive transition kernels for a $\delta_0(u)$ drift; this paper shows why standard Novikov/Girsanov arguments fail here and how local time must be handled instead.
- **Web search query:** `zambotti spdes with reflection pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Stewart N. Ethier, Thomas G. Kurtz / 1986
- **Title:** Markov Processes: Characterization and Convergence
- **Type:** Book
- **Venue:** Wiley + 1986
- **Main result or relevant chapter/section:** Chapter 4 provides theorems detailing exactly what is required to pass invariant measures to the weak limit when a sequence of Markov processes (and their generators) converges, heavily utilizing tightness and specific Feller conditions.
- **Topic needed for this proof:** The necessary tightness and uniform Feller conditions to rigorously pass invariant measures to a weak limit.
- **Open-access substitute for that topic:** (open-access for topic: weak convergence of invariant measures for Markov processes) — A. Eberle / 2017 / Markov Processes / University of Bonn lecture notes
- **Connection:** Addresses Grader B's Critique 4. The proof attempts a naive weak limit exchange ($P^n_t f \to P_t f$) inside the integral without justifying uniform-in-time Feller continuity or tightness of the invariant measures, which is a severe gap.
- **Web search query:** `eberle markov processes lecture notes pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Ioannis Karatzas, Steven E. Shreve / 1991
- **Title:** Brownian Motion and Stochastic Calculus
- **Type:** Book
- **Venue:** Springer + 1991
- **Main result or relevant chapter/section:** Chapter 2 covers the local time and sample path properties of Brownian motion, proving that the zero-level set of a Brownian path (and by extension, a Brownian bridge) has Lebesgue measure zero almost surely.
- **Topic needed for this proof:** The almost-sure zero Lebesgue measure of the zero-level set of Brownian paths.
- **Open-access substitute for that topic:** (open-access for topic: zero set of Brownian paths) — P. Mörters, Y. Peres / 2010 / Brownian Motion / Author's personal webpage draft
- **Connection:** Resolves Grader B's Critique 4. The proof asserts the zero-set of the Brownian bridge has Lebesgue measure zero as a fact to define the limit of the integrated heat kernel drift almost everywhere; this provides the missing canonical citation for that claim.
- **Web search query:** `morters peres brownian motion pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Zhi-Ming Ma, Michael Röckner / 1992
- **Title:** Introduction to the Theory of (Non-Symmetric) Dirichlet Forms
- **Type:** Book
- **Venue:** Springer + 1992
- **Main result or relevant chapter/section:** Develops the fundamental framework for defining Markov processes associated with singular Dirichlet forms and rigorously deriving their invariant measures via integration-by-parts formulas on infinite-dimensional spaces.
- **Topic needed for this proof:** Verifying infinite-dimensional integration-by-parts identities and reversibility for singular drifts using Dirichlet forms.
- **Open-access substitute for that topic:** (open-access for topic: Dirichlet forms and invariant measures for SPDEs) — M. Röckner / 1998 / Dirichlet forms on infinite dimensional state space and applications / CIME Summer School (author webpage)
- **Connection:** Addresses Grader B's Critiques 1 and 7. The proof declares reversibility and writes down a Gibbs measure for a singular SPDE by fiat; this monograph is the canonical framework for actually proving those integration-by-parts assertions when standard calculus breaks down.
- **Web search query:** `rockner dirichlet forms infinite dimensional pdf`
- **Confidence (bibliographic):** HIGH
