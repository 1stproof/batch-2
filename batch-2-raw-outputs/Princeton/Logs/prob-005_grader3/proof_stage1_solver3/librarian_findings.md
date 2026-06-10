# Librarian Findings — grader3_150540d79081_proof_stage1_solver3_20260531_010543
**Generated:** 2026-05-31T01:09:09  
**Inputs:** notebook=7629 chars, proof=9436 chars, gap_report=4492 chars  
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
- [Book] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press — IDs: no ID — Canonical text demonstrating that upgrading an $L^2$ spectral gap to everywhere convergence strictly requires topological irreducibility and the Strong Feller property. — search: `da prato zabczyk ergodicity infinite dimensional pdf`
- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric Dirichlet form — Probability Theory and Related Fields — IDs: no ID — Rigorously constructs the Dirichlet form and invariant measure for an SPDE with a singular local-time drift, avoiding sloppy weak-limit generator arguments. — search: `zambotti reflected stochastic heat equation pdf`
- [Paper] Holley, R., Stroock, D. W. / 1987 — Logarithmic Sobolev Inequalities and Stochastic Ising Models — Communications in Mathematical Physics — IDs: no ID — Canonical source for the Holley-Stroock perturbation lemma (SNT-3), proving that bounded density perturbations preserve spectral gaps. — search: `holley stroock logarithmic sobolev ising pdf`
- [Paper] Hairer, M., Mattingly, J. C. / 2006 — Ergodicity of the 2D Navier-Stokes equations with degenerate forcing — Annals of Mathematics — IDs: no ID — Introduces the Asymptotic Strong Feller property, the canonical modern tool to deduce unique ergodicity when classical transition-density bounds blow up. — search: `hairer mattingly asymptotic strong feller pdf`
- [Monograph] Bakry, D., Gentil, I., Ledoux, M. / 2014 — Analysis and Geometry of Markov Diffusion Operators — Springer — IDs: no ID — Systematically details the specific functional inequalities required to upgrade a Poincaré $L^2$ gap to total variation or uniform convergence bounds. — search: `bakry gentil ledoux markov diffusion operators pdf`

## RELATED
- [Lecture notes] Hairer, M. / 2006 — Ergodic Properties of Markov Processes — University of Warwick — IDs: no ID — Provides explicit counterexamples demonstrating why $L^2$ convergence fails to evaluate limits of integrals with respect to mutually singular measures. — search: `hairer ergodic properties of markov processes pdf`
- [Paper] Albeverio, S., Bogachev, V. I., Röckner, M. / 1993 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics — IDs: no ID — Verifies SNT-4 and establishes that $L^2$ uniqueness does not inherently preclude the existence of other mutually singular invariant measures. — search: `albeverio bogachev rockner uniqueness invariant measures diffusions pdf`
- [Monograph] Bogachev, V. I., Krylov, N. V., Röckner, M., Shaposhnikov, S. V. / 2015 — Fokker-Planck-Kolmogorov Equations — American Mathematical Society — IDs: no ID — Provides convergence theorems for invariant measures under smooth drift approximations, emphasizing the necessity of common dominating measures for exchanging limits. — search: `bogachev krylov rockner fokker planck kolmogorov pdf`
- [Book] Ma, Z., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer — IDs: no ID — Details Mosco convergence and the exact weak topology conditions needed to rigorously pass invariant measures to the limit. — search: `schmuland dirichlet forms infinite dimensional pdf`
- [Book] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press — IDs: no ID — Covers the Bismut-Elworthy-Li formula, showing how Feller regularization constants blow up as the drift concentrates into a Dirac delta. — search: `bismut elworthy li formula spde pdf`
- [Monograph] Da Prato, G. / 2004 — Kolmogorov Equations for Stochastic PDEs — Birkhäuser — IDs: no ID — Details how to rigorously derive explicit invariant measures for gradient SPDEs and verify their reversibility. — search: `da prato kolmogorov equations for stochastic pdes pdf`
- [Monograph] Fukushima, M., Oshima, Y., Takeda, M. / 1994 — Dirichlet Forms and Symmetric Markov Processes — de Gruyter — IDs: no ID — Details the capacity conditions strictly required to upgrade $L^2$ Dirichlet form uniqueness to transition semigroup uniqueness. — search: `fukushima oshima takeda dirichlet forms pdf`

## SOMEWHAT RELATED
- [Monograph] Bogachev, V. I. / 1998 — Gaussian Measures — American Mathematical Society — IDs: no ID — Verifies SNT-2 (Cameron-Martin theorem), detailing its strict requirement for finite $L^2$ energy which is relevant to prior iterations of the proof. — search: `bogachev gaussian measures pdf`

## NOT MUCH
- *(None)*

---

# Stage 2 — Narrower (draw 0, canonical)

Here is the triage of the parametric memory list against the specific gaps identified by the graders.

## LOAD-BEARING
- [Book] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press — IDs: no ID
  - **Addresses:** Grader A Gap 1 (Fallacy: Conflating $L^2$ convergence with everywhere pointwise convergence) and Grader B Gap 5.
  - **Key piece:** Chapter 4 systematically establishes Doob's Theorem for SPDEs, detailing the exact Strong Feller and topological irreducibility requirements strictly necessary to upgrade an $L^2$ convergence route into pointwise transition semigroup convergence.
- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric Dirichlet form — Probability Theory and Related Fields — IDs: no ID
  - **Addresses:** Grader B Gap 7 (Fallacy: The limiting singular-drift semigroup is not shown to inherit reversibility, a spectral gap, or the proposed Dirichlet form).
  - **Key piece:** Sections 3 and 4 rigorously establish the integration by parts formula and Dirichlet form specific to an SPDE with a singular local-time drift, completely bypassing the flawed weak-limit generator arguments used in the proof.
- [Monograph] Bogachev, V. I., Krylov, N. V., Röckner, M., Shaposhnikov, S. V. / 2015 — Fokker-Planck-Kolmogorov Equations — American Mathematical Society — IDs: no ID
  - **Addresses:** Grader B Gap 4 (Slip: The passage of invariance to the limit needs a common-dominating-measure DCT argument) and Grader A Gap 2.
  - **Key piece:** Chapter 8 explicitly details the topological and common-domination requirements to rigorously pass invariant measures of approximating drifts to the limit without relying on blowing-up pointwise error constants.

## SUPPORTING
- [Lecture notes] Hairer, M. / 2006 — Ergodic Properties of Markov Processes — University of Warwick
  *Provides readable counterexamples demonstrating why $L^2$ convergence fails to evaluate limits of integrals for mutually singular measures (Grader A Gap 1, Grader B Gap 5).*
- [Paper] Holley, R., Stroock, D. W. / 1987 — Logarithmic Sobolev Inequalities and Stochastic Ising Models — Communications in Mathematical Physics
  *Canonical source needed to verify SNT-3, establishing the baseline $L^2$ gap the proof attempts to exploit.*
- [Book] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press
  *Covers the Bismut-Elworthy-Li formula, confirming Grader A Gap 2 regarding why regularization constants blow up as the drift concentrates into a Dirac delta.*
- [Paper] Albeverio, S., Bogachev, V. I., Röckner, M. / 1993 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics
  *Canonical source for SNT-4 and clarifies the boundaries of uniqueness within absolute-continuity classes vs. mutually singular measures.*
- [Monograph] Bakry, D., Gentil, I., Ledoux, M. / 2014 — Analysis and Geometry of Markov Diffusion Operators — Springer
  *Details the specific functional inequalities (e.g., hypercontractivity) required to upgrade a Poincaré gap, addressing Grader B Gap 5.*
- [Book] Ma, Z., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer
  *Provides the strict Mosco convergence framework needed to pass Dirichlet forms to the limit (Grader B Gap 7).*
- [Paper] Hairer, M., Mattingly, J. C. / 2006 — Ergodicity of the 2D Navier-Stokes equations with degenerate forcing — Annals of Mathematics
  *Introduces Asymptotic Strong Feller, serving as a modern alternative when classical Feller constants blow up.*
- [Monograph] Fukushima, M., Oshima, Y., Takeda, M. / 1994 — Dirichlet Forms and Symmetric Markov Processes — de Gruyter
  *Provides the capacity condition background necessary for upgrading $L^2$ Dirichlet uniqueness.*
- [Monograph] Bogachev, V. I. / 1998 — Gaussian Measures — American Mathematical Society
  *Standard source for verifying SNT-2 (Cameron-Martin theorem) and its requirement for finite $L^2$ energy.*

## REDUNDANT
- [Monograph] Da Prato, G. / 2004 — Kolmogorov Equations for Stochastic PDEs — Birkhäuser
  *Overlaps heavily with Da Prato & Zabczyk (1996) regarding the verification of reversibility and derivation of invariant measures via generators (Grader B Gap 1).*

## PERIPHERAL
*(None)*

## UNFAMILIAR
*(None)*

---

# Stage 3 — Chapter Picker

## Ergodicity for Infinite Dimensional Systems (Da Prato, G., Zabczyk, J., Cambridge University Press, 1996)
_(IDs: no ID)_

Here are the specific chapters and sections from Da Prato & Zabczyk's *Ergodicity for Infinite Dimensional Systems* (1996) that address the core mathematical gaps in the proof:

*   **Chapter 4 (approx.) — Strong Feller Property and Irreducibility**
    *   **Which gap it addresses:** Grader A Gap 1 and Grader B Gap 2 (Conflating $L^2(\mu)$ convergence with everywhere pointwise convergence; asserting uniqueness without ergodicity mechanisms).
    *   **Why:** This chapter thoroughly details Doob's Theorem (SNT-1) in infinite dimensions. It explains exactly what smoothing mechanisms—specifically the Strong Feller property combined with topological irreducibility—are strictly required to upgrade $\mu$-almost everywhere convergence (from an $L^2$ spectral gap) into pointwise or total-variation convergence for *every* deterministic initial condition $x$.

*   **Chapter 8 (approx.) — Gradient Systems and Reversibility**
    *   **Which gap it addresses:** Grader B Gap 1 and 7 (Invariant measures for smooth approximations asserted without derivation; singular limit not shown to inherit reversibility).
    *   **Why:** This chapter provides the rigorous functional-analytic framework for SPDEs with gradient-type drifts. It uses Dirichlet forms and the generator to explicitly derive the invariant Gibbs measures (e.g., $e^{-2U(x)}\mu_0(dx)$) and proves the symmetry/reversibility of the associated transition semigroups, which the current proof skips via pure assertion.

*   **Chapter 10 (approx.) — Spectral Gap and Exponential Convergence**
    *   **Which gap it addresses:** Grader A Gap 1 and Grader B Gap 5 (Treating a Poincaré inequality directly as a supremum norm or total-variation bound).
    *   **Why:** This section formally defines the Poincaré inequality for infinite-dimensional Markov semigroups. It explicitly demonstrates that the spectral gap bounds the variance strictly in $L^2(\mu)$, and outlines the highly non-trivial uniform estimates (such as ultracontractivity or log-Sobolev conditions) needed to bridge the gap between $L^2$ mixing and uniform supremum-norm convergence.

## Fokker-Planck-Kolmogorov Equations (Bogachev, V. I., Krylov, N. V., Röckner, M., Shaposhnikov, S. V., American Mathematical Society, 2015)
_(IDs: no ID)_

Here are the specific chapters and sections from Bogachev, Krylov, Röckner, and Shaposhnikov's *Fokker-Planck-Kolmogorov Equations* (2015) that directly address the graders' identified gaps.

- **Chapter 10 (approx.): Infinite-Dimensional Fokker-Planck-Kolmogorov Equations**
  - **Which gap it addresses:** Grader B's gaps 1 and 2 (asserting the smooth invariant measures without proving reversibility or uniqueness in infinite dimensions).
  - **Why:** The problem requires establishing an invariant measure on the infinite-dimensional space $C_0([0,1])$. This chapter systematically develops FPK theory on locally convex spaces. It explains exactly how to rigorously verify that a proposed Gibbs measure is stationary by integrating the generator against cylinder test functions. Crucially, it covers the Albeverio-Bogachev-Röckner uniqueness theorems (SNT-4), which are needed to prove that the approximating gradient SPDEs possess *unique* invariant measures before attempting to take a limit.

- **Chapter 6 (approx.): Fokker-Planck-Kolmogorov Equations with Irregular Coefficients / Stability**
  - **Which gap it addresses:** Grader A's gap 2 and Grader B's gaps 4 and 6 (unjustified limit exchanges and taking $n \to \infty$ limits for singular drifts).
  - **Why:** The proof assumes that convergence of the invariant measures $\mu_n \to \mu$ and the semigroups $P_t^n \to P_t$ allows a naive exchange of limits $\lim_{t \to \infty} \lim_{n \to \infty}$. This chapter covers the weak stability of FPK solutions under coefficient approximations. It details the stringent uniform integrability and local Sobolev criteria required to rigorously pass to the limit without the error constants blowing up—criteria that specifically fail when a drift collapses into a singular Dirac delta. 

- **Chapter 4 (approx.): Stationary Fokker-Planck-Kolmogorov Equations (Section on Ergodicity)**
  - **Which gap it addresses:** Grader A's gap 1 and Grader B's gap 5 (conflating $L^2(\mu)$ spectral gap convergence with everywhere deterministic pointwise convergence).
  - **Why:** While Holley-Stroock (SNT-3) yields a Poincaré inequality and exponential convergence in $L^2(\mu)$, that convergence inherently excludes $\mu$-null sets. This chapter outlines the supplementary mechanisms (like transition density bounds, Harnack inequalities, or the Strong Feller property) that must be rigorously proven to upgrade $L^2(\mu)$ convergence into uniform total variation convergence from *every* deterministic starting point $x$.

## Ergodic Properties of Markov Processes (Hairer, M., University of Warwick
  *Provides readable counterexamples demonstrating why $L^2$ convergence fails to evaluate limits of integrals for mutually singular measures (Grader A Gap 1, Grader B Gap 5).*
- [Paper] Holley, R., Stroock, D. W. / 1987, 2006)
_(Logarithmic Sobolev Inequalities and Stochastic Ising Models — Communications in Mathematical Physics)_

Here are the specific sections from Hairer’s lecture notes that directly address the fatal conflation of $L^2$ convergence with topological uniqueness in the proof:

**Chapter 4 (approx.) — Spectral Gaps and $L^2$ Convergence**
* **Which gap it addresses:** Grader A Gap 1, Grader B Gap 5 (Conflating $L^2$ convergence with deterministic pointwise/TV convergence).
* **Why:** This section formally derives exponential $L^2(\mu)$ convergence from Poincaré inequalities but explicitly warns—often with readable counterexamples—that $L^2$ functions are only defined up to $\mu$-null sets. It demonstrates mathematically why you cannot evaluate the limit $\lim_{t \to \infty} P_t f(x)$ using a mutually singular measure $\nu$, because the spectral gap provides absolutely no information about the transition dynamics on $\mu$-measure zero sets without an independent smoothing mechanism.

**Chapter 3 (approx.) — Uniqueness of Invariant Measures / Strong Feller and Irreducibility**
* **Which gap it addresses:** Grader A Gap 1, Grader B Gap 2, Grader B Gap 5 (Missing smoothing mechanisms to upgrade $L^2$ convergence).
* **Why:** This chapter covers Doob's Theorem and precisely details the topological properties (like the Strong Feller property and topological irreducibility) required to bridge the gap between $\mu$-almost-everywhere convergence and uniform total variation convergence from *every* deterministic starting point $x$. It emphasizes why ruling out mutually singular invariant measures requires verifying these regularizing properties, which the current proof skips entirely. 

**Chapter 2 (approx.) — Existence and Invariant Measures**
* **Which gap it addresses:** Grader B Gap 6, Grader B Gap 7 (Interchange of limits and inheriting invariance).
* **Why:** It covers the Krylov-Bogoliubov theorem and the rigorous continuity conditions (such as the Feller property) necessary for a weak limit of measures to formally inherit stationary status for the limiting semigroup. This provides the exact framework needed to show why the proof's un-dominated exchange of $n \to \infty$ and $t \to \infty$ limits is invalid.

## Stochastic Equations in Infinite Dimensions (Da Prato, G., Zabczyk, J., Cambridge University Press
  *Covers the Bismut-Elworthy-Li formula, confirming Grader A Gap 2 regarding why regularization constants blow up as the drift concentrates into a Dirac delta.*
- [Paper] Albeverio, S., Bogachev, V. I., Röckner, M. / 1993, 1992)
_(On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics)_

Here are the specific chapters, sections, and theorems from the requested references that address the graders' identified gaps:

- **Chapter 9 (approx.) — "Transition Semigroups" / Bismut-Elworthy-Li Formula** *(Da Prato & Zabczyk)*
  - **Which gap it addresses:** Grader A Gap 2 (Unjustified limit exchange) and Grader A Scaffolding Q4.
  - **Why:** This chapter details the Bismut-Elworthy-Li formula, which provides explicit bounds for the spatial derivative of the transition semigroup $P_t f$. Because the gradient bounds depend exponentially on the supremum of the drift's derivative (its Lipschitz constant), these regularisation constants strictly blow up to infinity as the smooth approximations $G_{1/n}$ concentrate into a Dirac delta, proving why the uniform limit exchange $\lim_{n \to \infty}$ and $\lim_{t \to \infty}$ is mathematically invalid.

- **Chapter 11 (approx.) — "Invariant Measures" / Uniqueness and Ergodicity** *(Da Prato & Zabczyk)*
  - **Which gap it addresses:** Grader A Gap 1 (Conflating $L^2$ convergence with everywhere pointwise) and Grader B Gap 2.
  - **Why:** This section covers the application of Doob's Theorem (SNT-1) to infinite-dimensional SPDEs. It explicitly demonstrates that to upgrade an $L^2(\mu)$ spectral gap to everywhere pointwise/total variation convergence—and thereby rule out mutually singular invariant measures—one must rigorously prove both the Strong Feller property and topological irreducibility (e.g., via approximate null controllability), which the current proof entirely skipped.

- **Main Results (approx.) — "On uniqueness of invariant measures for finite- and infinite-dimensional diffusions"** *(Albeverio, Bogachev, Röckner)*
  - **Which gap it addresses:** Grader B Gap 7 (Limiting singular-drift semigroup not shown to inherit reversibility/Dirichlet form) and Grader B Gap 1.
  - **Why:** This paper establishes the strict criteria required to use Dirichlet form techniques for invariant measure uniqueness (SNT-4). It highlights that finding a pointwise limiting measure $\mu$ is insufficient; one must rigorously prove the limiting singular process is actually symmetric (reversible) with respect to $\mu$ and forms a quasi-regular Dirichlet form, neither of which are automatically inherited from the smooth approximations.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [Book] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press — IDs: no ID — Canonical text demonstrating that upgrading an $L^2$ spectral gap to everywhere convergence strictly requires topological irreducibility and the Strong Feller property. — search: `da prato zabczyk ergodicity infinite dimensional pdf`
  - **Gap Addressed:** Grader A critique 1 ("Fallacy: Conflating $L^2$ convergence with everywhere pointwise convergence") and Grader B critique 5 ("Fallacy: A Poincaré inequality is treated as pointwise or total-variation convergence...").
  - **Relevance:** Chapter 4 provides the strict topological irreducibility and Strong Feller prerequisites necessary to rigorously upgrade an $L^2$ spectral gap to everywhere convergence.

- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric Dirichlet form — Probability Theory and Related Fields — IDs: no ID — Rigorously constructs the Dirichlet form and invariant measure for an SPDE with a singular local-time drift, avoiding sloppy weak-limit generator arguments. — search: `zambotti reflected stochastic heat equation pdf`
  - **Gap Addressed:** Grader B critique 7 ("Fallacy: The limiting singular-drift semigroup is not shown to inherit reversibility, a spectral gap, or the proposed Dirichlet form").
  - **Relevance:** This paper details the exact construction of the symmetric Dirichlet form for the SHE with a local-time singular drift, directly contradicting and bypassing the proof's unjustified weak-limit generator assertions.

- [Paper] Holley, R., Stroock, D. W. / 1987 — Logarithmic Sobolev Inequalities and Stochastic Ising Models — Communications in Mathematical Physics — IDs: no ID — Canonical source for the Holley-Stroock perturbation lemma (SNT-3), proving that bounded density perturbations preserve spectral gaps. — search: `holley stroock logarithmic sobolev ising pdf`
  - **Gap Addressed:** CANONICAL-CITATION VERIFICATION REQUEST (SNT-3 - Holley-Stroock perturbation lemma).
  - **Relevance:** Section 1 of this paper is the canonical source verifying that a probability measure inheriting a bounded density perturbation from a reference measure preserves its spectral gap, which is heavily relied upon in Step 4.

- [Monograph] Bogachev, V. I., Krylov, N. V., Röckner, M., Shaposhnikov, S. V. / 2015 — Fokker-Planck-Kolmogorov Equations — American Mathematical Society — IDs: no ID — Provides convergence theorems for invariant measures under smooth drift approximations, emphasizing the necessity of common dominating measures for exchanging limits. — search: `bogachev krylov rockner fokker planck kolmogorov pdf`
  - **Gap Addressed:** Grader A critique 2 ("Fallacy: Unjustified limit exchange") and Grader B critique 4 ("Slip: The passage of invariance to the limit needs a common-dominating-measure DCT argument...").
  - **Relevance:** The text establishes the rigorous theorems required to pass invariant measures through smooth drift approximations using common dominating measures and uniform bounds.

## SUPPORTING

- [Monograph] Bakry, D., Gentil, I., Ledoux, M. / 2014 — Analysis and Geometry of Markov Diffusion Operators — Springer — IDs: no ID — Systematically details the specific functional inequalities required to upgrade a Poincaré $L^2$ gap to total variation or uniform convergence bounds. — search: `bakry gentil ledoux markov diffusion operators pdf`
  *Note: Useful background detailing the exact functional inequalities to evaluate Grader A's scaffolding questions regarding spectral gaps.*

- [Paper] Hairer, M., Mattingly, J. C. / 2006 — Ergodicity of the 2D Navier-Stokes equations with degenerate forcing — Annals of Mathematics — IDs: no ID — Introduces the Asymptotic Strong Feller property, the canonical modern tool to deduce unique ergodicity when classical transition-density bounds blow up. — search: `hairer mattingly asymptotic strong feller pdf`
  *Note: Provides background on alternative methods like the Asymptotic Strong Feller property when transition-density regularizations blow up.*

- [Lecture notes] Hairer, M. / 2006 — Ergodic Properties of Markov Processes — University of Warwick — IDs: no ID — Provides explicit counterexamples demonstrating why $L^2$ convergence fails to evaluate limits of integrals with respect to mutually singular measures. — search: `hairer ergodic properties of markov processes pdf`
  *Note: Provides intuition for why $L^2$ convergence fails for evaluating limits with mutually singular measures.*

- [Paper] Albeverio, S., Bogachev, V. I., Röckner, M. / 1993 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics — IDs: no ID — Verifies SNT-4 and establishes that $L^2$ uniqueness does not inherently preclude the existence of other mutually singular invariant measures. — search: `albeverio bogachev rockner uniqueness invariant measures diffusions pdf`
  *Note: Establishes context for SNT-4 and the distinction between $L^2$ uniqueness and global uniqueness against mutually singular measures.*

- [Book] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press — IDs: no ID — Covers the Bismut-Elworthy-Li formula, showing how Feller regularization constants blow up as the drift concentrates into a Dirac delta. — search: `bismut elworthy li formula spde pdf`
  *Note: Excellent for understanding how regularization constants blow up as a drift approaches a Dirac delta (Grader A critique 2).*

- [Monograph] Da Prato, G. / 2004 — Kolmogorov Equations for Stochastic PDEs — Birkhäuser — IDs: no ID — Details how to rigorously derive explicit invariant measures for gradient SPDEs and verify their reversibility. — search: `da prato kolmogorov equations for stochastic pdes pdf`
  *Note: Useful for rigorously verifying the derivation of invariant measures via generators (Grader B critique 1).*

- [Monograph] Fukushima, M., Oshima, Y., Takeda, M. / 1994 — Dirichlet Forms and Symmetric Markov Processes — de Gruyter — IDs: no ID — Details the capacity conditions strictly required to upgrade $L^2$ Dirichlet form uniqueness to transition semigroup uniqueness. — search: `fukushima oshima takeda dirichlet forms pdf`
  *Note: Provides background on the capacity conditions required to upgrade $L^2$ Dirichlet form uniqueness.*

## REDUNDANT

- [Book] Ma, Z., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer — IDs: no ID — Details Mosco convergence and the exact weak topology conditions needed to rigorously pass invariant measures to the limit. — search: `schmuland dirichlet forms infinite dimensional pdf`
  *Overlap: Largely overlaps with Zambotti 2001 and Fukushima et al. 1994 regarding Dirichlet form inheritance and weak topology limits.*

## PERIPHERAL

- [Monograph] Bogachev, V. I. / 1998 — Gaussian Measures — American Mathematical Society — IDs: no ID — Verifies SNT-2 (Cameron-Martin theorem), detailing its strict requirement for finite $L^2$ energy which is relevant to prior iterations of the proof. — search: `bogachev gaussian measures pdf`
  *Reason: While it covers SNT-2, the Cameron-Martin theorem is not utilized in this specific round's proof attempt.*

## UNFAMILIAR

*(None)*

## Narrower draw 2
## LOAD-BEARING

- [Book] Da Prato, G., Zabczyk, J. / 1996 — Ergodicity for Infinite Dimensional Systems — Cambridge University Press
  - **Gap addressed:** Grader A, Area for Improvement 1 (Conflating $L^2$ convergence with everywhere pointwise convergence) and Grader B, Area for Improvement 5.
  - **Load-bearing piece:** The chapters detailing Doob's theorem and the Strong Feller property for SPDEs explicitly demonstrate that upgrading a Poincaré $L^2$ spectral gap to everywhere convergence strictly requires topological irreducibility and strong Feller smoothing, proving the proof's unconditional pointwise limit exchange invalid.

- [Book] Da Prato, G., Zabczyk, J. / 1992 — Stochastic Equations in Infinite Dimensions — Cambridge University Press
  - **Gap addressed:** Grader A, Area for Improvement 2 (Unjustified limit exchange) and Grader A, Scaffolding Question 4.
  - **Load-bearing piece:** The chapter covering the Bismut-Elworthy-Li formula explicitly derives how Feller transition density regularization bounds scale with the supremum/Lipschitz norms of the drift, proving that these uniform constants blow up as the drift converges to a singular Dirac delta.

- [Paper] Zambotti, L. / 2001 — A reflected stochastic heat equation as symmetric Dirichlet form — Probability Theory and Related Fields
  - **Gap addressed:** Grader B, Area for Improvement 7 (Limiting singular-drift semigroup not shown to inherit reversibility or the Dirichlet form).
  - **Load-bearing piece:** The core construction rigorously establishes the symmetric Dirichlet form and reversibility specifically for SPDEs driven by singular local-time drifts, directly addressing the gap caused by the proof asserting these properties bypassably via weak limits.

## SUPPORTING

- [Paper] Holley, R., Stroock, D. W. / 1987 — Logarithmic Sobolev Inequalities and Stochastic Ising Models — Communications in Mathematical Physics
  - Useful to explicitly verify SNT-3 (Holley-Stroock Perturbation Lemma) and check its strict assumptions regarding bounded density perturbations.
- [Paper] Albeverio, S., Bogachev, V. I., Röckner, M. / 1993 — On uniqueness of invariant measures for finite- and infinite-dimensional diffusions — Communications on Pure and Applied Mathematics
  - Verifies SNT-4 and directly answers Grader A, Scaffolding Question 2 by showing $L^2$ uniqueness does not inherently preclude other mutually singular invariant measures.
- [Lecture notes] Hairer, M. / 2006 — Ergodic Properties of Markov Processes — University of Warwick
  - Provides essential counterexamples for Grader A, Scaffolding Question 2, showing why $L^2$ bounds fail to handle mutually singular measure evaluations.
- [Monograph] Bogachev, V. I., Krylov, N. V., Röckner, M., Shaposhnikov, S. V. / 2015 — Fokker-Planck-Kolmogorov Equations — American Mathematical Society
  - Provides the rigorous dominating-measure tools needed to address Grader B, Area for Improvement 4 regarding passing invariant measures to the limit.
- [Book] Ma, Z., Röckner, M. / 1992 — Introduction to the Theory of (Non-Symmetric) Dirichlet Forms — Springer
  - Details the Mosco convergence topology required to rigorously pass Dirichlet forms and reversibility to weak limits (relevant to Grader B, Area for Improvement 7).
- [Monograph] Fukushima, M., Oshima, Y., Takeda, M. / 1994 — Dirichlet Forms and Symmetric Markov Processes — de Gruyter
  - Details the capacity conditions required to rigorously upgrade $L^2$ uniqueness (via Dirichlet forms) to transition semigroup uniqueness (relevant to Grader B, Area for Improvement 2).
- [Monograph] Bogachev, V. I. / 1998 — Gaussian Measures — American Mathematical Society
  - Necessary to verify SNT-2 (Cameron-Martin Theorem) and its $L^2$ energy constraints, tracking back to the historical failures of the proof attempt (IPT-66).

## REDUNDANT

- [Monograph] Bakry, D., Gentil, I., Ledoux, M. / 2014 — Analysis and Geometry of Markov Diffusion Operators — Springer
  - Overlaps heavily with Da Prato & Zabczyk (1996) regarding the functional inequalities required to upgrade a spectral gap to uniform bounds, but lacks the specific infinite-dimensional SPDE focus of DPZ.
- [Monograph] Da Prato, G. / 2004 — Kolmogorov Equations for Stochastic PDEs — Birkhäuser
  - Overlaps heavily with Da Prato & Zabczyk (1996) in deriving invariant measures and verifying reversibility for smooth gradient SPDEs.

## PERIPHERAL

- [Paper] Hairer, M., Mattingly, J. C. / 2006 — Ergodicity of the 2D Navier-Stokes equations with degenerate forcing — Annals of Mathematics
  - While it introduces the Asymptotic Strong Feller property, this technique is predominantly tailored for systems with degenerate forcing; our SPDE features additive space-time white noise where standard (or explicitly failed) Strong Feller properties are more directly relevant.

## UNFAMILIAR

- *(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here is a curated list of canonical literature and topic-keyed substitutes that address the specific gaps identified by the graders, particularly the illegal leap from $L^2$ convergence to pointwise/total-variation convergence, and the missing rigorous construction of the generator for singular drifts.

### 1. The Canonical Text on SPDE Ergodicity (Addresses the $L^2$ vs Pointwise Gap)
- **Authors / Year:** G. Da Prato, J. Zabczyk / 1996
- **Title:** Ergodicity for Infinite Dimensional Systems
- **Type:** Book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 4 and Chapter 7 establish Doob's Theorem for SPDEs, detailing exactly how the Strong Feller property and topological irreducibility are required to force mutually singular measures to be identical. 
- **Topic needed for this proof:** The theorem proving that a spectral gap ($L^2$ convergence) requires a topological smoothing mechanism (like the Strong Feller property) to be upgraded to uniqueness of invariant measures from arbitrary deterministic initial conditions.
- **Open-access substitute for that topic:** (open-access for topic: Upgrading $L^2$ convergence to total variation via Strong Feller) — M. Hairer / 2010 (approx.) / Convergence of Markov Processes / Warwick lecture notes.
- **Connection:** This directly addresses **Grader A's Fallacy 1** and **Grader B's Fallacy 5**. The proof fatally assumes that exponential convergence in $L^2(\mu)$ applies uniformly to everywhere pointwise limits. This reference proves that without Strong Feller, $L^2$ convergence only gives uniqueness $\mu$-almost everywhere, leaving open the possibility of mutually singular stationary measures.
- **Web search query:** `hairer convergence of markov processes pdf`
- **Confidence (bibliographic):** HIGH

### 2. Transition Density Bounds and Singular Limits
- **Authors / Year:** G. Da Prato, J. Zabczyk / 1992
- **Title:** Stochastic Equations in Infinite Dimensions
- **Type:** Book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 9 covers the Bismut-Elworthy-Li formula, which provides explicit bounds on the spatial derivatives of the transition semigroup $P_t f(x)$ in terms of the Lipschitz constant and supremum of the drift.
- **Topic needed for this proof:** The Bismut-Elworthy-Li formula and how gradient bounds on transition semigroups scale with the supremum of the drift.
- **Open-access substitute for that topic:** (open-access for topic: Bismut-Elworthy-Li formula and gradient bounds for SPDEs) — F. Flandoli / 2008 / An Introduction to 3D Stochastic Fluid Dynamics / CIME Lecture Notes.
- **Connection:** Answers **Grader A's Scaffolding Q4** and addresses **Fallacy 2**. Because the proof's approximations $G_{1/n}$ concentrate into a Dirac delta, their suprema and Lipschitz constants blow up as $n \to \infty$. This implies the Strong Feller regularization constants blow up, strictly invalidating the uniform convergence required to exchange $\lim_{n \to \infty}$ and $\lim_{t \to \infty}$ in Step 4.
- **Web search query:** `bismut elworthy li formula spde pdf`
- **Confidence (bibliographic):** HIGH

### 3. Rigorous Construction of Singular-Drift Semigroups via Dirichlet Forms
- **Authors / Year:** L. Zambotti / 2001
- **Title:** A reflected stochastic heat equation as symmetric dynamics with respect to the 3-d Bessel bridge measure
- **Type:** Paper
- **Venue:** Journal of Functional Analysis
- **Main result or relevant chapter/section:** Demonstrates how to rigorously construct the generator and invariant measure for an SPDE with a singular (non-function) drift corresponding to reflection/delta-potentials by building a quasi-regular Dirichlet form.
- **Topic needed for this proof:** Identifying the invariant measure and reversible dynamics for an SPDE with a singular infinite drift using Dirichlet forms rather than classical generator limits.
- **Open-access substitute for that topic:** (open-access for topic: Dirichlet form construction for SPDEs with singular reflection/drifts) — L. Zambotti / 2004 / Occupation densities for SPDEs with reflection / arxiv preprint.
- **Connection:** Directly targets **Grader B's Fallacies 1, 4, and 7**. The proof attempts a sloppy weak-limit approach to pass invariance and reversibility to the limit measure $\mu$. Zambotti's work shows the rigorous Dirichlet-form machinery actually required to prove that the singular-drift limit inherits reversibility and spectral properties.
- **Web search query:** `zambotti reflected stochastic heat equation pdf`
- **Confidence (bibliographic):** HIGH

### 4. Bounded Perturbations of Spectral Gaps
- **Authors / Year:** R. Holley, D. Stroock / 1987
- **Title:** Logarithmic Sobolev Inequalities and Stochastic Ising Models
- **Type:** Paper
- **Venue:** Communications in Mathematical Physics
- **Main result or relevant chapter/section:** The main theorem proves that if a measure satisfies a Log-Sobolev (or Poincaré) inequality, any equivalent measure whose density is bounded above and below retains the inequality, with the new gap scaled by the bounds of the density.
- **Topic needed for this proof:** The Holley-Stroock perturbation lemma for Poincaré inequalities under bounded potential perturbations.
- **Open-access substitute for that topic:** (open-access for topic: Holley-Stroock perturbation lemma) — D. Bakry, I. Gentil, M. Ledoux / 2013 / Analysis and Geometry of Markov Diffusion Operators / Springer (Author's draft version).
- **Connection:** Supports the *verification* of the specific named theorem (SNT-3) used in Step 4. The grader critiques correctly recognize that while the Holley-Stroock lemma *does* guarantee a uniform $L^2$ spectral gap (because the antiderivative of the delta drift is a bounded Heaviside step), the proof illegally extends this to uniform supremum-norm convergence.
- **Web search query:** `bakry gentil ledoux markov diffusion pdf`
- **Confidence (bibliographic):** HIGH

### 5. Overcoming the Loss of Strong Feller in Singular SPDEs
- **Authors / Year:** M. Hairer, J. C. Mattingly / 2006
- **Title:** Ergodicity of the 2D Navier-Stokes equations with degenerate forcing
- **Type:** Paper
- **Venue:** Annals of Mathematics
- **Main result or relevant chapter/section:** Introduces the "Asymptotic Strong Feller" property, demonstrating how to prove unique ergodicity when classical transition-density bounds (Strong Feller) blow up or fail completely due to singular/degenerate noise.
- **Topic needed for this proof:** Asymptotic Strong Feller property as a substitute for classical Strong Feller when transition density bounds blow up.
- **Open-access substitute for that topic:** (open-access for topic: Asymptotic Strong Feller property and unique ergodicity) — M. Hairer / 2008 / Ergodic Properties of Markov Processes / Lecture notes.
- **Connection:** Bears heavily on **Grader A's Fallacy 2** and **Grader B's Scaffolding Q5**. Since the drift $G_{1/n}$ approaches a singular Dirac delta, classical topological smoothing fails in the limit. The Asymptotic Strong Feller property is the canonical modern technique the author *should* have used to bypass the blowing-up constants and legitimately force total variation collapse.
- **Web search query:** `hairer mattingly asymptotic strong feller pdf`
- **Confidence (bibliographic):** HIGH

### 6. Dominated Convergence and Weak Topologies for Invariance
- **Authors / Year:** Z. Ma, M. Röckner / 1992
- **Title:** Introduction to the Theory of (Non-Symmetric) Dirichlet Forms
- **Type:** Book
- **Venue:** Springer
- **Main result or relevant chapter/section:** Chapter IV (and specifically the sections on Mosco convergence) details the exact requirements for a sequence of invariant measures and their corresponding Markov semigroups to pass to a well-defined limit semigroup.
- **Topic needed for this proof:** Rigorous limit exchanges for invariant measures of approximating Markov semigroups using Mosco convergence of Dirichlet forms.
- **Open-access substitute for that topic:** (open-access for topic: Mosco convergence of Dirichlet forms for SPDE approximations) — B. Schmuland / 1995 / Dirichlet forms: Some infinite-dimensional examples / Survey paper.
- **Connection:** Addresses **Grader B's Slip 4 and Fallacy 6**. The proof writes $\int P_t^n f d\mu_n - \int P_t f d\mu$ and claims pointwise plus TV convergence is enough for the limit exchange. This text provides the rigorous "common domination" and Mosco-convergence arguments actually required to take limits of stationary infinite-dimensional Markov processes.
- **Web search query:** `schmuland dirichlet forms infinite dimensional pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the prior works and canonical references that directly address the gaps identified by the graders, particularly the invalid assumption that an $L^2$ spectral gap automatically upgrades to pointwise or total-variation convergence for deterministic initial conditions, and the missing rigorous treatment of singular drifts.

- **Authors / Year** — Da Prato, G. & Zabczyk, J. / 1996
- **Title** — Ergodicity for Infinite Dimensional Systems
- **Type** — book
- **Venue** — Cambridge University Press
- **Main result or relevant chapter/section** — Chapter 4 develops the core Doob/Khasminskii theory for SPDEs, proving that to conclude uniqueness of an invariant measure from $L^2$ properties, one requires topological irreducibility and either the Strong Feller property or a rigorous smoothing mechanism.
- **Topic needed for this proof** — The theorem establishing that the Strong Feller property is strictly necessary to deduce everywhere pointwise/total-variation convergence from $L^2(\mu)$ convergence.
- **Open-access substitute for that topic** — (open-access for topic: Strong Feller and unique ergodicity for infinite-dimensional Markov processes) — Hairer, M. / 2006 (approx.) / Ergodic Properties of Markov Processes / University of Warwick lecture notes.
- **Connection** — Directly addresses Grader A's Fallacy 1 and Grader B's Fallacy 2/5. The proof falsely assumes a Poincaré inequality implies exponential convergence from *every* deterministic start $x \in C_0([0,1])$, which fails without the Strong Feller property explicitly proven here.
- **Web search query** — `hairer ergodic properties markov processes pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Bakry, D., Gentil, I., & Ledoux, M. / 2014
- **Title** — Analysis and Geometry of Markov Diffusion Operators
- **Type** — monograph
- **Venue** — Springer (Grundlehren der mathematischen Wissenschaften)
- **Main result or relevant chapter/section** — Chapters 4 and 5 systematically detail how a Poincaré inequality yields $L^2$ convergence, but explicitly show that upgrading this to supremum norm or total variation convergence requires uniform ultracontractivity bounds (e.g., Nash or Sobolev inequalities).
- **Topic needed for this proof** — The specific functional inequalities required to upgrade an $L^2(\mu)$ spectral gap into $L^\infty$ or total variation convergence.
- **Open-access substitute for that topic** — (open-access for topic: upgrading Poincare inequalities to uniform convergence bounds) — The authors' pre-publication manuscript of the same book, widely hosted on author web pages.
- **Connection** — Addresses Grader B's Fallacy 5 and Grader A's Scaffolding Question 3. The proof asserts that a bounded potential and a spectral gap force TV convergence across the entire space; this work shows exactly what extra smoothing constants must be bounded to make that leap.
- **Web search query** — `bakry gentil ledoux markov diffusion operators pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Holley, R., & Stroock, D. W. / 1987
- **Title** — Logarithmic Sobolev Inequalities and Stochastic Ising Models
- **Type** — paper
- **Venue** — Communications in Mathematical Physics, Vol. 115
- **Main result or relevant chapter/section** — Contains the original "Holley-Stroock perturbation lemma," which proves that bounded perturbations of a potential preserve the Log-Sobolev (and Poincaré) inequalities, with the new gap degraded by a factor of $e^{-\text{Oscillation}(V)}$.
- **Topic needed for this proof** — The Holley-Stroock perturbation lemma for probability measures.
- **Open-access substitute for that topic** — (open-access for topic: Holley-Stroock lemma and perturbation of spectral gaps) — Guionnet, A., & Zegarlinski, B. / 2003 / Lectures on Logarithmic Sobolev Inequalities / Seminaire de Probabilites XXXVI.
- **Connection** — The near-miss proof explicitly invokes this lemma in Step 4. While the application to finite $n$ is valid, Grader A's critique on limit exchange (Fallacy 2) requires checking whether the Holley-Stroock uniform constants survive the $n \to \infty$ singular limit where the state space topology shifts.
- **Web search query** — `holley stroock logarithmic sobolev ising pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Zambotti, L. / 2001
- **Title** — A reflected stochastic heat equation as symmetric Dirichlet form
- **Type** — paper
- **Venue** — Probability Theory and Related Fields, Vol. 121
- **Main result or relevant chapter/section** — Constructs the invariant measure and transition semigroup for an SPDE with a singular local-time drift (reflection) by rigorously identifying the associated symmetric Dirichlet form and proving its quasi-regularity.
- **Topic needed for this proof** — The rigorous construction of a Dirichlet form and generator for an SPDE driven by a singular (local time/delta) drift, avoiding fabricated everywhere-convergence arguments.
- **Open-access substitute for that topic** — (open-access for topic: Dirichlet form approach to SPDEs with singular drifts) — Zambotti, L. / 2001 / same title / arxiv preprint.
- **Connection** — Directly addresses Grader B's Fallacy 1 and 7. The near-miss proof bypasses the generator entirely; Zambotti shows the canonical way to pass the invariant measure to the singular limit by establishing reversibility via the Dirichlet form.
- **Web search query** — `zambotti reflected stochastic heat equation pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Hairer, M., & Mattingly, J. C. / 2006
- **Title** — Ergodicity of the 2D Navier-Stokes equations with degenerate forcing
- **Type** — paper
- **Venue** — Annals of Mathematics, Vol. 164
- **Main result or relevant chapter/section** — Introduces the "Asymptotic Strong Feller" property, which bridges the gap when the classical Strong Feller property fails (common in singular/degenerate infinite-dimensional systems), allowing one to still deduce unique ergodicity.
- **Topic needed for this proof** — The Asymptotic Strong Feller property as a substitute for Strong Feller to prove global uniqueness of invariant measures.
- **Open-access substitute for that topic** — (open-access for topic: Asymptotic Strong Feller property for infinite dimensional Markov processes) — Hairer, M. / 2009 (approx.) / An Introduction to Stochastic PDEs / Arxiv survey preprint.
- **Connection** — Because the singular skew-SHE might lack the classical Strong Feller property due to non-Lipschitz singularities (mentioned in the notebook's "Atomic Conclusion"), Asymptotic Strong Feller is the modern, canonical mechanism to close Grader A's Gap 1.
- **Web search query** — `hairer mattingly asymptotic strong feller pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Fukushima, M., Oshima, Y., & Takeda, M. / 1994
- **Title** — Dirichlet Forms and Symmetric Markov Processes
- **Type** — monograph
- **Venue** — de Gruyter
- **Main result or relevant chapter/section** — Chapter 4 details the exact conditions (quasi-regularity, absolute continuity with respect to capacity) under which a Dirichlet form corresponds to a uniquely defined symmetric Markov process.
- **Topic needed for this proof** — The capacity conditions required to link an $L^2$ Dirichlet form to a pointwise-defined Markov transition semigroup.
- **Open-access substitute for that topic** — (open-access for topic: quasi-regular Dirichlet forms and Markov processes) — Ma, Z. M., & Röckner, M. / 1992 / Introduction to the Theory of (Non-Symmetric) Dirichlet Forms / Springer Universitext (often available via institutional drafts) OR Röckner's various survey papers on SPDEs and Dirichlet forms.
- **Connection** — Explains Grader B's Fallacy 7. The proof takes the limit measure $\mu$, but Fukushima's theory shows that one must prove the set of exceptional starting points has zero capacity, not just zero measure, to legitimately upgrade $L^2$ convergence to transition semigroup uniqueness.
- **Web search query** — `fukushima oshima takeda dirichlet forms pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and openly hosted topic-keyed substitutes that verify the named theorems and address the fatal gaps identified by the graders.

**1. Ergodicity for Infinite Dimensional Systems**
- **Authors:** Da Prato, G. / Zabczyk, J. / 1996
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 4 ("Invariant Measures") and Chapter 7 ("Ergodicity") formalize Doob's Theorem in infinite dimensions, proving that strong convergence from every deterministic initial condition requires both topological irreducibility and the Strong Feller property.
- **Topic needed for this proof:** Upgrading an $L^2$ spectral gap to everywhere convergence in total variation via the Strong Feller property.
- **Open-access substitute for that topic:** (open-access for topic: Upgrading $L^2$ convergence to everywhere convergence using Strong Feller) — Hairer, M. / 2006 / Ergodic Properties of Markov Processes / University of Warwick lecture notes
- **Connection:** Addresses Grader A's Fallacy 1 and Grader B's Fallacy 5. The proof falsely assumes an $L^2$ spectral gap automatically yields exponential convergence from *every* starting point $x$, which is strictly false without a regularizing mechanism like Strong Feller.
- **Web search query:** `da prato zabczyk ergodicity infinite dimensional pdf`
- **Confidence (bibliographic):** HIGH

**2. Ergodic Properties of Markov Processes**
- **Authors:** Hairer, M. / 2006 (approx.)
- **Type:** lecture notes
- **Venue:** University of Warwick / author's personal webpage
- **Main result or relevant chapter/section:** Provides a concise, modern exposition separating $L^2$ methods (Poincaré inequalities) from topological methods, explicitly demonstrating why a spectral gap only implies convergence for $\mu$-almost every initial condition.
- **Topic needed for this proof:** The failure of $L^2$ convergence to guarantee convergence from singular deterministic initial conditions.
- **Open-access substitute for that topic:** (None needed; the canonical reference is openly hosted).
- **Connection:** Directly answers Grader A's scaffolding question #1 and critiques the leap in Step 4. Hairer provides explicit counterexamples showing why you cannot evaluate limits of integrals with respect to a mutually singular measure $\nu$ just because the semigroup converges in $L^2(\mu)$.
- **Web search query:** `hairer ergodic properties of markov processes pdf`
- **Confidence (bibliographic):** HIGH

**3. Logarithmic Sobolev inequalities and stochastic Ising models**
- **Authors:** Holley, R. A. / Stroock, D. W. / 1987
- **Type:** paper
- **Venue:** Journal of Statistical Physics
- **Main result or relevant chapter/section:** Proves that if a probability measure satisfies a logarithmic Sobolev or Poincaré inequality, any equivalent measure with a density bounded strictly away from 0 and $\infty$ also satisfies it.
- **Topic needed for this proof:** Transfer of spectral gaps under bounded density perturbations.
- **Open-access substitute for that topic:** (open-access for topic: Holley-Stroock perturbation lemma for spectral gaps) — Guionnet, A., & Zegarlinski, B. / 2003 / Lectures on Logarithmic Sobolev Inequalities / Séminaire de Probabilités XXXVI (Springer, but often hosted on authors' pages).
- **Connection:** Canonical citation for the Holley-Stroock Perturbation Lemma (SNT-3) explicitly used in Step 4.
- **Web search query:** `holley stroock logarithmic sobolev inequalities pdf`
- **Confidence (bibliographic):** HIGH

**4. Fokker-Planck-Kolmogorov Equations**
- **Authors:** Bogachev, V. I. / Krylov, N. V. / Röckner, M. / Shaposhnikov, S. V. / 2015
- **Type:** monograph
- **Venue:** American Mathematical Society (Mathematical Surveys and Monographs)
- **Main result or relevant chapter/section:** Contains comprehensive convergence theorems for invariant measures of diffusions when the drift coefficients are approximated by smooth functions, emphasizing the necessity of uniform integrability and common dominating measures.
- **Topic needed for this proof:** Rigorous justification of passing invariance to the limit for a sequence of approximating drifts using a common-dominating-measure DCT argument.
- **Open-access substitute for that topic:** (open-access for topic: Passing invariant measures to the limit via dominating measures) — Bogachev, V. I., et al. / 2013 / Fokker-Planck-Kolmogorov equations / arxiv preprint of book draft chapters
- **Connection:** Resolves Grader A's Fallacy 2 and Grader B's Slip 4. Step 3 glosses over the limit exchange ($\lim_{n \to \infty}$ vs $\lim_{t \to \infty}$) using a flawed dominated convergence argument; this work shows exactly what bounds are required to stop the constants from blowing up as the drift approaches a Dirac delta.
- **Web search query:** `bogachev krylov rockner fokker planck kolmogorov pdf`
- **Confidence (bibliographic):** HIGH

**5. Kolmogorov Equations for Stochastic PDEs**
- **Authors:** Da Prato, G. / 2004
- **Type:** monograph
- **Venue:** Birkhäuser
- **Main result or relevant chapter/section:** Details how to formally define gradient SPDEs and rigorously derive their explicit invariant measures of the form $\exp(2\Phi)d\mu_0$, alongside proofs of their reversibility and symmetry.
- **Topic needed for this proof:** Rigorous derivation of invariant measures for gradient SPDEs using the generator and verifying reversibility.
- **Open-access substitute for that topic:** (open-access for topic: Invariant measures and reversibility for gradient SPDEs) — Hairer, M. / 2009 / An Introduction to Stochastic PDEs / lecture notes
- **Connection:** Addresses Grader B's Fallacy 1 and Fallacy 7. The proof merely asserts the invariant measures for the smooth approximations without deriving them via the generator or proving reversibility.
- **Web search query:** `da prato kolmogorov equations for stochastic pdes pdf`
- **Confidence (bibliographic):** HIGH

**6. On uniqueness of invariant measures for finite- and infinite-dimensional diffusions**
- **Authors:** Albeverio, S. / Bogachev, V. I. / Röckner, M. / 1993
- **Type:** paper
- **Venue:** Communications on Pure and Applied Mathematics
- **Main result or relevant chapter/section:** Establishes uniqueness conditions for invariant measures using Dirichlet forms and quasi-regularity, showing that $L^2$ uniqueness does not inherently block the existence of other mutually singular invariant measures.
- **Topic needed for this proof:** Uniqueness of invariant measures for infinite-dimensional gradient systems via Dirichlet forms.
- **Open-access substitute for that topic:** (open-access for topic: Dirichlet forms and uniqueness of invariant measures for SPDEs) — Eberle, A. / 1999 / Uniqueness and Non-Uniqueness of Semigroups Generated by Singular Diffusion Operators / Lecture Notes in Mathematics 1718 (author webpage draft)
- **Connection:** Canonical citation for the Albeverio-Bogachev-Röckner Uniqueness Theorem (SNT-4) and directly addresses Grader B's Point 7 regarding the failure to prove that the limiting singular-drift semigroup actually inherits a Dirichlet form.
- **Web search query:** `albeverio bogachev rockner uniqueness invariant measures diffusions pdf`
- **Confidence (bibliographic):** HIGH

**7. Gaussian Measures**
- **Authors:** Bogachev, V. I. / 1998
- **Type:** monograph
- **Venue:** American Mathematical Society
- **Main result or relevant chapter/section:** The definitive text on Gaussian measures on infinite-dimensional spaces, providing the rigorous formulation of the Cameron-Martin theorem.
- **Topic needed for this proof:** The Cameron-Martin theorem and its strict requirement for finite $L^2$ energy.
- **Open-access substitute for that topic:** (open-access for topic: Cameron-Martin theorem in infinite dimensions) — Hairer, M. / 2009 / An Introduction to Stochastic PDEs / lecture notes
- **Connection:** Verifies SNT-2 (Cameron-Martin). While the near-miss proof avoided it directly, the notebook's anchor verdict and IPT-66 heavily cite infinite Cameron-Martin energy as the fundamental block to establishing global uniqueness via mutual absolute continuity. 
- **Web search query:** `bogachev gaussian measures pdf`
- **Confidence (bibliographic):** HIGH
