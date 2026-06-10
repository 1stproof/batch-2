# Librarian Findings — grader3_aba8b48b7ecb_proof_stage1_solver5_20260531_014720
**Generated:** 2026-05-31T01:56:22  
**Inputs:** notebook=8996 chars, proof=4209 chars, gap_report=3106 chars  
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
- [Paper] Hoeffding / 1956 — On the distribution of the number of successes in independent trials — The Annals of Mathematical Statistics — no ID — Justifies why a uniform probability configuration forms the absolute worst-case minimizer for Bernoulli sums, structurally enabling the missing necessity counterexample (Grader A Q1). — search: hoeffding on the distribution of the number of successes pdf
- [Paper] Anderson, Samuels / 1967 — Some inequalities for binomial and Poisson probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — no ID — SNT-2; rigorously establishes the strict monotonicity of binomial tails needed to evaluate the explicit uniform weight counterexample polynomial and prove it drops below $p$. — search: anderson samuels binomial poisson berkeley pdf
- [Book] Alon, Spencer / 2016 — The Probabilistic Method (4th Edition) — Wiley — no ID — Formalizes the probabilistic trick of applying union bounds over dependent but identically distributed marginals (cyclic coupling) without requiring joint independence (Grader B Q2). — search: matousek vondrak probabilistic method pdf
- [Book] Marshall, Olkin, Arnold / 2011 — Inequalities: Theory of Majorization and Its Applications (2nd Edition) — Springer Series in Statistics — no ID — The canonical text for Schur-convexity on the simplex, mathematically required to close OC-2 and validate the assumed weight reduction (IPT-54). — search: steele cauchy schwarz master class majorization pdf
- [Book] Feller / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 (3rd Edition) — Wiley — no ID — Supplies the exact algebraic polynomial expansions of binomial bounds required to explicitly construct the omitted "only if" necessity proof requested by Grader A. — search: feller introduction to probability theory vol 1 pdf

## RELATED
- [Paper] Slud / 1977 — Distribution inequalities for the binomial law — The Annals of Probability — no ID — SNT-3; secures strict discrete lower bounds for intermediate binomial tails to escape the weak continuous bounds that otherwise natively fail in PS-C. — search: slud distribution inequalities for the binomial law pdf
- [Paper] Feige / 2006 — On sums of independent random variables with unbounded variance and estimating the average degree in a graph — SIAM Journal on Computing — no ID — Demonstrates active coupling and majorization techniques applied directly to finding global probability minimums over the unconstrained weight simplex (OC-2). — search: feige sums independent random variables pdf
- [Book] Thorisson / 2000 — Coupling, Stationarity, and Regeneration — Springer — no ID — Extensively details the valid construction of dependent copies that perfectly preserve marginal distributions while enforcing rigid deterministic summation relationships across them. — search: coupling stationarity and regeneration thorisson pdf

## SOMEWHAT RELATED
- [Book] Williams / 1991 — Probability with Martingales — Cambridge University Press — no ID — Develops rigorous discrete-time martingale theory and valid stopping times over natural filtrations required to approach the alternative PS-D proof track (OC-4). — search: probability with martingales david williams pdf
- [Book] Boucheron, Lugosi, Massart / 2013 — Concentration Inequalities: A Nonasymptotic Theory of Independence — Oxford University Press — no ID — Provides alternative nonasymptotic tail bounding techniques for binomials, though exact polynomial limits (Feller) are strictly preferred for the narrow threshold gap here. — search: lugosi concentration measure inequalities lecture notes pdf

## NOT MUCH
- [Paper] Hoeffding / 1963 — Probability inequalities for sums of bounded random variables — Journal of the American Statistical Association — no ID — SNT-1; while generic continuous bounded-sum exponential bounds are cited conceptually, they are too loose and inherently fail the sharp discrete threshold required by this exact probability mapping. — search: ramon van handel probability in high dimension pdf

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [Paper] Anderson, Samuels / 1967 — Some inequalities for binomial and Poisson probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — no ID
  - **Gap:** Grader A Q3
  - **Relevance:** Theorem 1 establishes the exact strict monotonicity of binomial tails with respect to the number of trials, which is mathematically necessary to rigorously prove the explicit uniform weight counterexample polynomial evaluates strictly below $p$.

- [Book] Alon, Spencer / 2016 — The Probabilistic Method (4th Edition) — Wiley — no ID
  - **Gap:** Grader B Q2
  - **Relevance:** Chapter 1 (The Basic Method) formally demonstrates that the union bound strictly requires only identical marginal distributions and explicitly applies without any assumption of joint independence among the cyclic coupled copies.

## SUPPORTING

- [Book] Feller / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 (3rd Edition) — Wiley — no ID
  - Provides the fundamental, exact algebraic expansions of the binomial distribution necessary to construct the baseline polynomial requested in Grader A Q2.

- [Paper] Hoeffding / 1956 — On the distribution of the number of successes in independent trials — The Annals of Mathematical Statistics — no ID
  - While technically addressing non-identical probabilities rather than non-identical weights, its core extreme-point theorems conceptually justify why the uniform configuration forms the minimum tail bound, motivating the specific setup in Grader A Q1.

## REDUNDANT

- [Book] Thorisson / 2000 — Coupling, Stationarity, and Regeneration — Springer — no ID
  - Overlaps heavily with Alon & Spencer regarding the valid construction of dependent copies and the reliance on identical marginals over joint independence (Grader B Q2).

## PERIPHERAL

- [Book] Marshall, Olkin, Arnold / 2011 — Inequalities: Theory of Majorization and Its Applications (2nd Edition) — Springer Series in Statistics — no ID
- [Paper] Slud / 1977 — Distribution inequalities for the binomial law — The Annals of Probability — no ID
- [Paper] Feige / 2006 — On sums of independent random variables with unbounded variance and estimating the average degree in a graph — SIAM Journal on Computing — no ID
- [Book] Williams / 1991 — Probability with Martingales — Cambridge University Press — no ID
- [Book] Boucheron, Lugosi, Massart / 2013 — Concentration Inequalities: A Nonasymptotic Theory of Independence — Oxford University Press — no ID
- [Paper] Hoeffding / 1963 — Probability inequalities for sums of bounded random variables — Journal of the American Statistical Association — no ID

## UNFAMILIAR

(None)

---

# Stage 3 — Chapter Picker

## The Probabilistic Method (4th Edition) (Alon, Spencer, Wiley, 2016)
_(no ID)_

I do not believe this reference actually addresses any of the named gaps.

**Why:** The missing step required to close the necessity gap (as outlined by both graders) relies on explicitly constructing a uniform-weight counterexample and proving a strict, exact algebraic inequality for the tail of a Binomial distribution (e.g., showing that $\Pr(\text{Bin}(n+1, p) \ge 2) < p$ for $p \in (\frac{1}{n+1}, \frac{1}{n})$). Alon and Spencer’s *The Probabilistic Method* focuses heavily on asymptotic combinatorial bounds (such as the Lovász Local Lemma, Martingale concentrations, and random graph theory); while it covers large deviations and Chernoff bounds (typically in Appendix A), these asymptotic tools are famously too loose to securely resolve the exact polynomial bounds required for these tight, non-asymptotic boundary intervals. The gap requires elementary calculus and algebraic root analysis of the Binomial PMF, not advanced probabilistic combinatorial methods.

## An Introduction to Probability Theory and Its Applications, Vol. 1 (3rd Edition) (Feller, Wiley, 1968)
_(no ID)_

Here are the specific chapters and sections from Feller's *An Introduction to Probability Theory and Its Applications, Vol. 1* that directly address the gaps and scaffolding questions:

- **Chapter VI: The Binomial and the Poisson Distributions, Section 2: The Binomial Distribution**
  - **Which gap it addresses:** Grader A's scaffolding questions 1 & 2 (Formulating the necessity counterexample).
  - **Why:** Provides the foundational formulas for $n$ independent Bernoulli trials. This allows the solver to explicitly translate the uniform weight condition ($m = n+1$, $w_i = \frac{1}{n+1}$) into a discrete binomial variable, establishing that exceeding the threshold $p$ requires at least 2 successes, evaluated exactly as $1 - (1-p)^{n+1} - (n+1)p(1-p)^n$.

- **Chapter VI: The Binomial and the Poisson Distributions, Section 3: The Central Term and the Tails** *(approx.)*
  - **Which gap it addresses:** Grader A's scaffolding question 3 (Rigorously bounding the binomial expression).
  - **Why:** Details the analytical properties, monotonicity, and bounds of binomial tail probabilities. This section provides the groundwork for analytically proving that the discrete tail probability for the counterexample is strictly less than $p$ for intermediate values $p \in (1/(n+1), 1/n)$.

- **Chapter IX: Random Variables; Expectation, Sections on Joint Distributions and Independence** *(approx.)*
  - **Which gap it addresses:** Grader B's scaffolding question 2 (Clarifying the coupling argument's reliance on identical marginals vs. independence).
  - **Why:** Formalizes the mathematical distinction between the marginal distributions of individual variables and their joint distribution. Reviewing this will resolve the solver's implicit handling of dependence in the cyclic coupling matrix, clarifying why the union bound strictly relies on marginals while the sum's almost-sure structural guarantee relies on their specific joint dependence.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [Paper] Anderson, Samuels / 1967 — Some inequalities for binomial and Poisson probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — no ID — SNT-2; rigorously establishes the strict monotonicity of binomial tails needed to evaluate the explicit uniform weight counterexample polynomial and prove it drops below $p$. — search: anderson samuels binomial poisson berkeley pdf
  - **Gap addressed:** Grader A Q3
  - **Justification:** The core Monotonicity Theorem (Theorem 1) for binomial tails provides the exact analytical bounds required to rigorously prove that the probability evaluation of the specified $(n+1)$-uniform counterexample strictly drops below $p$ on the intermediate intervals.

- [Book] Alon, Spencer / 2016 — The Probabilistic Method (4th Edition) — Wiley — no ID — Formalizes the probabilistic trick of applying union bounds over dependent but identically distributed marginals (cyclic coupling) without requiring joint independence (Grader B Q2). — search: matousek vondrak probabilistic method pdf
  - **Gap addressed:** Grader B Q2
  - **Justification:** The opening chapters on the First Moment Method and union bounds formally codify which fundamental probability steps (like linearity of expectation and bounds over marginals) perfectly operate under cyclic couplings without requiring joint independence across the copies.

## SUPPORTING

- [Book] Feller / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 (3rd Edition) — Wiley — no ID — Supplies the exact algebraic polynomial expansions of binomial bounds required to explicitly construct the omitted "only if" necessity proof requested by Grader A. — search: feller introduction to probability theory vol 1 pdf
  - *Note:* Chapter VI provides the foundational, exact binomial sum formulas needed to express the probability of achieving the minimum number of successes (Grader A Q2).
  
- [Book] Thorisson / 2000 — Coupling, Stationarity, and Regeneration — Springer — no ID — Extensively details the valid construction of dependent copies that perfectly preserve marginal distributions while enforcing rigid deterministic summation relationships across them. — search: coupling stationarity and regeneration thorisson pdf
  - *Note:* Serves as a comprehensive verification reference for the valid construction of dependent copies preserving marginals (Grader B Q2).

## REDUNDANT

*(None)*

## PERIPHERAL

- [Paper] Hoeffding / 1956 — On the distribution of the number of successes in independent trials — The Annals of Mathematical Statistics — no ID — *While the aggregator suggests this for Grader A Q1, the theorem concerns the Poisson binomial distribution (variable probabilities, uniform weights). The gap deals with i.i.d. variables and varying weights. A single explicitly evaluated counterexample is sufficient for Grader A; a global worst-case minimizer proof over the simplex is unnecessary.*
- [Book] Marshall, Olkin, Arnold / 2011 — Inequalities: Theory of Majorization and Its Applications (2nd Edition) — Springer Series in Statistics — no ID — *Majorization and Schur-convexity on the simplex are required for the sufficiency of the continuous domain (OC-2), but the graders are exclusively critiquing the omitted necessity direction for the discrete set.*
- [Paper] Slud / 1977 — Distribution inequalities for the binomial law — The Annals of Probability — no ID — *Provides lower bounds, whereas the necessity counterexample gap fundamentally requires proving an upper bound drops strictly below $p$.*
- [Paper] Feige / 2006 — On sums of independent random variables with unbounded variance and estimating the average degree in a graph — SIAM Journal on Computing — no ID 
- [Book] Williams / 1991 — Probability with Martingales — Cambridge University Press — no ID 
- [Book] Boucheron, Lugosi, Massart / 2013 — Concentration Inequalities: A Nonasymptotic Theory of Independence — Oxford University Press — no ID 
- [Paper] Hoeffding / 1963 — Probability inequalities for sums of bounded random variables — Journal of the American Statistical Association — no ID 

## UNFAMILIAR

*(None)*

## Narrower draw 2
## LOAD-BEARING

- [Paper] Anderson, Samuels / 1967 — Some inequalities for binomial and Poisson probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — no ID — SNT-2; rigorously establishes the strict monotonicity of binomial tails needed to evaluate the explicit uniform weight counterexample polynomial and prove it drops below $p$. — search: anderson samuels binomial poisson berkeley pdf
  - **Gap:** Grader A Scaffolding Question 3
  - **Load-bearing piece:** Section 2 rigorously establishes the exact monotonicity inequalities of binomial distributions necessary to mathematically prove that the adversarial uniform-weight polynomial drops strictly below the required probability threshold $p$.

- [Book] Feller / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 (3rd Edition) — Wiley — no ID — Supplies the exact algebraic polynomial expansions of binomial bounds required to explicitly construct the omitted "only if" necessity proof requested by Grader A. — search: feller introduction to probability theory vol 1 pdf
  - **Gap:** Grader A Scaffolding Question 2 and Grader B Fallacy 1
  - **Load-bearing piece:** Chapter VI supplies the classical algebraic formulation of the discrete binomial distribution required to explicitly instantiate the missing necessity counterexample using uniform weights.

- [Book] Alon, Spencer / 2016 — The Probabilistic Method (4th Edition) — Wiley — no ID — Formalizes the probabilistic trick of applying union bounds over dependent but identically distributed marginals (cyclic coupling) without requiring joint independence (Grader B Q2). — search: matousek vondrak probabilistic method pdf
  - **Gap:** Grader B Scaffolding Question 2
  - **Load-bearing piece:** The foundational material in Chapters 1 and 2 completely formalizes the validity of applying union bounds over identically distributed but dependent random variables without requiring joint independence.

## SUPPORTING

- [Paper] Hoeffding / 1956 — On the distribution of the number of successes in independent trials — The Annals of Mathematical Statistics — no ID — Justifies why a uniform probability configuration forms the absolute worst-case minimizer for Bernoulli sums, structurally enabling the missing necessity counterexample (Grader A Q1). — search: hoeffding on the distribution of the number of successes pdf
  - *Note:* Provides the theoretical justification (via Theorem 3) for why a uniform weight distribution forms an absolute worst-case bound, contextualizing the explicit parameterized counterexample families the grader requested.

## REDUNDANT

- [Book] Thorisson / 2000 — Coupling, Stationarity, and Regeneration — Springer — no ID — Extensively details the valid construction of dependent copies that perfectly preserve marginal distributions while enforcing rigid deterministic summation relationships across them. — search: coupling stationarity and regeneration thorisson pdf
  - *Overlap:* Overlaps heavily with Alon & Spencer in detailing how dependent coupling constructions validly preserve marginal distributions for union bounds.

## PERIPHERAL

- [Book] Marshall, Olkin, Arnold / 2011 — Inequalities: Theory of Majorization and Its Applications (2nd Edition) — Springer Series in Statistics — no ID — The canonical text for Schur-convexity on the simplex, mathematically required to close OC-2 and validate the assumed weight reduction (IPT-54). — search: steele cauchy schwarz master class majorization pdf
- [Paper] Slud / 1977 — Distribution inequalities for the binomial law — The Annals of Probability — no ID — SNT-3; secures strict discrete lower bounds for intermediate binomial tails to escape the weak continuous bounds that otherwise natively fail in PS-C. — search: slud distribution inequalities for the binomial law pdf
- [Paper] Feige / 2006 — On sums of independent random variables with unbounded variance and estimating the average degree in a graph — SIAM Journal on Computing — no ID — Demonstrates active coupling and majorization techniques applied directly to finding global probability minimums over the unconstrained weight simplex (OC-2). — search: feige sums independent random variables pdf
- [Book] Williams / 1991 — Probability with Martingales — Cambridge University Press — no ID — Develops rigorous discrete-time martingale theory and valid stopping times over natural filtrations required to approach the alternative PS-D proof track (OC-4). — search: probability with martingales david williams pdf
- [Book] Boucheron, Lugosi, Massart / 2013 — Concentration Inequalities: A Nonasymptotic Theory of Independence — Oxford University Press — no ID — Provides alternative nonasymptotic tail bounding techniques for binomials, though exact polynomial limits (Feller) are strictly preferred for the narrow threshold gap here. — search: lugosi concentration measure inequalities lecture notes pdf
- [Paper] Hoeffding / 1963 — Probability inequalities for sums of bounded random variables — Journal of the American Statistical Association — no ID — SNT-1; while generic continuous bounded-sum exponential bounds are cited conceptually, they are too loose and inherently fail the sharp discrete threshold required by this exact probability mapping. — search: ramon van handel probability in high dimension pdf

## UNFAMILIAR
*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and texts that bear directly on the requested SNTs (Standard Named Theorems) and the specific gaps identified by the graders. I have focused particularly on the algebraic properties of binomial tails, the required majorization arguments, and the coupling mechanics.

### 1. Canonical Citations for Named Theorems & Coupling

**Hoeffding / 1963**
- **Title:** Probability inequalities for sums of bounded random variables
- **Type:** paper
- **Venue:** Journal of the American Statistical Association
- **Main result:** Establishes exponential upper bounds on the tail probabilities of sums of independent bounded random variables, relying only on their domain intervals.
- **Topic needed for this proof:** Concentration bounds for weighted sums of independent Bernoulli variables (Hoeffding's inequality).
- **Open-access substitute for that topic:** (open-access for topic: Hoeffding's inequality and concentration of measure) — Ramon van Handel / 2014 / Probability in High Dimension / Princeton University lecture notes
- **Connection:** This is the canonical citation requested for **SNT-1**.
- **Web search query:** `ramon van handel probability in high dimension pdf`
- **Confidence (bibliographic):** HIGH

**Slud / 1977**
- **Title:** Distribution inequalities for the binomial law
- **Type:** paper
- **Venue:** The Annals of Probability
- **Main result:** Proves that for $p \le 1/2$ and $c \ge kp$, the discrete binomial tail probability $\Pr[\text{Bin}(k, p) \ge c]$ is strictly lower-bounded by the corresponding standard normal continuous probability $1 - \Phi$.
- **Topic needed for this proof:** Normal approximation lower bounds for exact discrete binomial tails.
- **Connection:** This is the canonical citation for **SNT-3**, which the notebook attempts to use for the continuous lower domain boundaries. 
- **Web search query:** `slud distribution inequalities for the binomial law pdf`
- **Confidence (bibliographic):** HIGH

**Alon, Spencer / 2016**
- **Title:** The Probabilistic Method (4th Edition)
- **Type:** book
- **Venue:** Wiley
- **Main result:** The foundational text on applying probability to deterministic combinatorial structures. Chapter 1 introduces the basic probabilistic method (Union Bound), and later chapters formalize dependency and coupling.
- **Topic needed for this proof:** The cyclic dependent coupling trick and union bounds over identically distributed marginals.
- **Open-access substitute for that topic:** (open-access for topic: Dependent coupling and union bounds over identical marginals) — J. Matoušek, J. Vondrák / 2008 / The Probabilistic Method / Charles University lecture notes
- **Connection:** Bears directly on **Grader B's Question 2** regarding the near-miss proof's sufficiency step. The proof couples $n$ variables such that their sum is strictly 1, applying a union bound to infer $\Pr[X^{(j)} \ge 1/n] \ge 1/n$. Alon & Spencer formalizes exactly which probabilistic conclusions require joint independence versus which (like linearity of expectation and simple union bounds) only require identical marginal distributions.
- **Web search query:** `matousek vondrak probabilistic method pdf`
- **Confidence (bibliographic):** HIGH

### 2. Literature for the Grader Gaps: Majorization & Binomial Tails

**Marshall, Olkin, Arnold / 2011**
- **Title:** Inequalities: Theory of Majorization and Its Applications (2nd Edition)
- **Type:** book
- **Venue:** Springer Series in Statistics
- **Main result:** The definitive reference on how functions that preserve ordering (Schur-convexity) behave on the probability simplex, detailing how to move from arbitrary weight distributions to symmetric extreme points.
- **Topic needed for this proof:** Using Schur-convexity/majorization to prove that the minimum of a symmetric function over the probability simplex occurs at specific symmetric extreme points.
- **Open-access substitute for that topic:** (open-access for topic: Majorization and Schur-convexity on the simplex) — J. M. Steele / 2004 / The Cauchy-Schwarz Master Class (Chapter 13: Majorization and Schur Convexity) / author webpage manuscript
- **Connection:** Addresses **IPT-54** ("Assuming Simplex Collapse Without Majorization") and **OC-2**. The notebook attempts to map unconstrained continuous weights natively over to symmetric discrete subsets ($w_i = 1/k$). This requires rigorous majorization proofs.
- **Web search query:** `steele cauchy schwarz master class majorization pdf`
- **Confidence (bibliographic):** HIGH

**Feller / 1968**
- **Title:** An Introduction to Probability Theory and Its Applications, Vol. 1 (3rd Edition)
- **Type:** book
- **Venue:** Wiley
- **Main result:** Chapter VI provides exhaustive algebraic properties, tail expansions, and monotonicity behaviors for the discrete Binomial distribution.
- **Topic needed for this proof:** Exact algebraic polynomial expansions for low-degree binomial tails.
- **Connection:** Closes the direct gap flagged by **Grader A**. To prove necessity for $p \in (1/(n+1), 1/n)$, you must evaluate the polynomial $1 - (1-p)^{n+1} - (n+1)p(1-p)^n$ (which represents exactly 2 or more successes out of $n+1$ trials) and rigorously prove it is strictly less than $p$. Feller covers the canonical methods for these explicit threshold polynomials.
- **Web search query:** `feller introduction to probability theory vol 1 pdf`
- **Confidence (bibliographic):** HIGH

**Hoeffding / 1956**
- **Title:** On the distribution of the number of successes in independent trials
- **Type:** paper
- **Venue:** The Annals of Mathematical Statistics
- **Main result:** Proves that the expected value of any convex function of a sum of independent Bernoulli variables (subject to a fixed total mean) is maximized when the underlying success probabilities are extreme (i.e., 0 and 1) and minimized when they are uniform.
- **Topic needed for this proof:** Extremal configurations for sums of independent Bernoulli variables subject to a summation constraint.
- **Connection:** While Hoeffding applies this to heterogeneous Bernoulli probabilities, by duality it deeply informs the structural logic of **OC-2**, answering Grader B's question on why parameterizing extreme bounds forces the worst-case counterexamples into specific discrete configurations.
- **Web search query:** `hoeffding on the distribution of the number of successes pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references that validate the named theorems from the notebook and provide the rigorous machinery needed to close the gaps identified by the graders, particularly the missing necessity proof and the structural majorization/coupling steps.

**1. Anderson, T. W., & Samuels, S. M. / 1967**
- **Title:** Some inequalities for binomial and Poisson probabilities
- **Type:** paper
- **Venue:** Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1, University of California Press
- **External IDs:** 
- **Main result or relevant chapter/section:** Proves strict monotonicity properties for the cumulative distribution function of the binomial distribution, specifically establishing how $\Pr[\text{Binomial}(k, p) \le c]$ behaves as the number of trials $k$ increases under fixed-mean constraints.
- **Topic needed for this proof:** Monotonicity and algebraic bounding of exact binomial tail probabilities over specific intermediate fractional intervals.
- **Open-access substitute for that topic:** (open-access for topic: Monotonicity of binomial tails) — Jog, V., & Loh, P.-L. / 2015 / On concentration of binomial and Poisson variables / arxiv preprint
- **Connection:** Validates **SNT-2** in the notebook. Crucial for answering Grader A’s scaffolding questions 2 and 3: provides the analytical tools needed to evaluate the uniform weight counterexample and rigorously prove that $\Pr[\text{Binomial}(n+1, p) \ge 2] < p$ for $p \in (1/(n+1), 1/n)$.
- **Web search query:** `some inequalities for binomial and poisson probabilities anderson samuels pdf`
- **Confidence (bibliographic):** HIGH

**2. Slud, E. V. / 1977**
- **Title:** Distribution inequalities for the binomial law
- **Type:** paper
- **Venue:** The Annals of Probability, 5(3)
- **External IDs:** 
- **Main result or relevant chapter/section:** Provides exact lower bounds for the tail of the binomial distribution using the standard normal cumulative distribution function, strictly applicable when $p \le 1/2$ and the evaluation boundary is within the bulk of the distribution.
- **Topic needed for this proof:** Strict discrete lower bounds for binomial tails evaluated at integer boundaries to escape weak continuous bounds.
- **Open-access substitute for that topic:** (open-access for topic: Binomial tail lower bounds) — Short survey or lecture notes on binomial distribution inequalities.
- **Connection:** Validates **SNT-3**. It provides the alternative heavy machinery needed for active proof skeletons PS-C and PS-D (OC-3/OC-4) where continuous bounds natively fail, and helps secure the failure conditions in the intermediate domains $p \in (1/3, 1/2)$ referenced by the graders.
- **Web search query:** `distribution inequalities for the binomial law slud pdf`
- **Confidence (bibliographic):** HIGH

**3. Hoeffding, W. / 1956**
- **Title:** On the distribution of the number of successes in independent trials
- **Type:** paper
- **Venue:** Annals of Mathematical Statistics, 27(3)
- **External IDs:** 
- **Main result or relevant chapter/section:** Establishes that the maximum and minimum of the expected value of a structurally convex function of a sum of independent Bernoulli variables (given a fixed overall mean) occurs precisely when the success probabilities are either identical (uniform) or forced to 0/1 extremes.
- **Topic needed for this proof:** The extremal principle justifying why uniform weight allocations form the worst-case configuration for sums of Bernoulli random variables.
- **Open-access substitute for that topic:** (open-access for topic: Extremal distributions for independent Bernoulli sums) — Authors' webpage drafts covering properties of Poisson binomial distributions.
- **Connection:** Directly addresses Grader A's question 1 and the problem's necessity proof by theoretically justifying why $w_i = \frac{1}{n+1}$ is the exact adversarial sequence needed to minimize the success probability across the weight simplex.
- **Web search query:** `on the distribution of the number of successes in independent trials hoeffding pdf`
- **Confidence (bibliographic):** HIGH

**4. Thorisson, H. / 2000**
- **Title:** Coupling, Stationarity, and Regeneration
- **Type:** book
- **Venue:** Springer
- **External IDs:** 
- **Main result or relevant chapter/section:** A comprehensive treatment of coupling theory (Chapters 1-3), explicitly detailing how to construct joint probability distributions that perfectly preserve desired marginal distributions while forcing rigid deterministic relationships (such as global sums or permutations) across the dependent copies.
- **Topic needed for this proof:** The valid construction of dependent copies that maintain identical marginals while strictly satisfying a global sum constraint.
- **Open-access substitute for that topic:** (open-access for topic: Coupling construction with identical marginals) — Levin, D. A., Peres, Y., & Wilmer, E. L. / 2009 / Markov Chains and Mixing Times / AMS (Draft online)
- **Connection:** Resolves Grader B's Question 2 by rigorously justifying the "continuous cyclic coupling" step in the proof. It confirms that identical marginals are fully sufficient for the final union bound application, effectively insulating the proof from the heavy dependence among the $n$ coupled vectors.
- **Web search query:** `coupling stationarity and regeneration thorisson pdf`
- **Confidence (bibliographic):** HIGH

**5. Marshall, A. W., Olkin, I., & Arnold, B. C. / 2011**
- **Title:** Inequalities: Theory of Majorization and Its Applications
- **Type:** book
- **Venue:** Springer
- **External IDs:** 
- **Main result or relevant chapter/section:** Chapter 3 covers Schur-convex functions and majorization on the simplex, proving how such functions attain global extrema strictly at the uniform distribution or symmetric boundary extreme points.
- **Topic needed for this proof:** Using majorization to rigorously prove that minimums over the weight simplex collapse to symmetric extreme points.
- **Open-access substitute for that topic:** (open-access for topic: Schur-convexity and majorization on the simplex) — Open-access lecture notes on majorization inequalities.
- **Connection:** Closes the severe "Simplex Collapse Without Majorization" fallacy (IPT-54) and provides the structural framework demanded in the notebook's Next Priority to rigorously prove the global simplex reduction in **OC-2**.
- **Web search query:** `inequalities theory of majorization and its applications pdf`
- **Confidence (bibliographic):** HIGH

**6. Williams, D. / 1991**
- **Title:** Probability with Martingales
- **Type:** book
- **Venue:** Cambridge University Press
- **External IDs:** 
- **Main result or relevant chapter/section:** Chapters 4 through 10 develop rigorous discrete-time martingale theory, specifically detailing the construction of stopping times on natural filtrations of i.i.d. variables and evaluating probabilities conditional on a halting event.
- **Topic needed for this proof:** Defining valid stopping times on natural filtrations to compute exact conditional halting probabilities.
- **Open-access substitute for that topic:** (open-access for topic: Discrete stopping times and natural filtrations) — Varadhan, S.R.S. / Probability Theory / Courant Institute Lecture Notes
- **Connection:** Provides the foundational machinery needed for **OC-4** (active in skeleton PS-D), where the pipeline attempts to construct a valid stopping time $\tau$ over the filtration $\mathcal{F}_k$ to prove sufficiency for the continuous lower domain.
- **Web search query:** `probability with martingales david williams pdf`
- **Confidence (bibliographic):** HIGH

**7. Hoeffding, W. / 1963**
- **Title:** Probability inequalities for sums of bounded random variables
- **Type:** paper
- **Venue:** Journal of the American Statistical Association, 58(301)
- **External IDs:** 
- **Main result or relevant chapter/section:** Establishes exponentially decaying tail bounds for sums of independent, bounded random variables.
- **Topic needed for this proof:** Generic upper tail bounds for sums of bounded independent variables.
- **Open-access substitute for that topic:** (open-access for topic: Tail bounds for bounded independent random variables) — Concentration inequalities survey papers on arxiv.
- **Connection:** Formal canonical citation for **SNT-1** (Hoeffding's Inequality). While current skeletons bypass it in favor of exact discrete bounds, it remains the baseline hypothesis-check citation for any continuous bounded sum in this domain.
- **Web search query:** `probability inequalities for sums of bounded random variables hoeffding pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the prior works and reference materials that directly bear on the cyclic coupling proof, the omitted necessity construction, and the specific binomial tail bounds requested by the graders.

- **Authors / Year:** T. W. Anderson, S. M. Samuels / 1967
- **Title:** Some Inequalities for Binomial and Poisson Probabilities
- **Type:** Conference paper (Proceedings)
- **Venue:** Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Statistics
- **Main result or relevant chapter/section:** Proves that for a fixed expectation, the cumulative probability of a Binomial distribution strictly decreases as the number of trials increases, approaching the Poisson limit monotonically from above.
- **Topic needed for this proof:** Monotonicity and explicit bounds of binomial tail probabilities as dimension scales.
- **Open-access substitute for that topic:** (open-access for topic: original proceedings are open-access) — Project Euclid hosts the full Fifth Berkeley Symposium openly.
- **Connection:** This is the canonical source for "SNT-2" in the notebook. It directly answers Grader A’s Question 3: analyzing the exact Binomial expression for the uniform-weight adversarial case ($w_i = \frac{1}{n+1}$) and rigorously demonstrating that the probability of achieving the necessary number of successes strictly drops below $p$ on the intermediate intervals $p \in (1/(n+1), 1/n)$.
- **Web search query:** `anderson samuels binomial poisson berkeley pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** E. V. Slud / 1977
- **Title:** Distribution inequalities for the binomial law
- **Type:** Paper
- **Venue:** The Annals of Probability, Vol. 5, No. 3
- **Main result or relevant chapter/section:** Establishes explicit, rigorous lower bounds for the discrete tail probabilities of binomial distributions in terms of the standard normal cumulative distribution function.
- **Topic needed for this proof:** Secure analytic bounds for exact discrete binomial tail probabilities near the mean.
- **Open-access substitute for that topic:** (open-access for topic: original paper is open-access) — Project Euclid hosts pre-2000 *Annals of Probability* openly.
- **Connection:** This is the canonical source for "SNT-3" in the notebook. When evaluating Grader A's scaffolding questions 1 and 2, the threshold number of Bernoulli successes becomes an integer boundary. Slud’s inequality provides the rigorous foundation for bounding $\Pr[\text{Binomial}(n+1, p) \ge \lceil p(n+1) \rceil]$ explicitly.
- **Web search query:** `slud distribution inequalities binomial law pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** N. Alon, J. H. Spencer / 2016 (4th ed., approx.)
- **Title:** The Probabilistic Method
- **Type:** Book
- **Venue:** John Wiley & Sons
- **Main result or relevant chapter/section:** Chapter 1 covers foundational probability bounds (Union Bound), and Chapter 8 ("The Poisson Paradigm" / "Dependent Random Variables") covers symmetric configurations, identical marginals, and cyclic coupling structures.
- **Topic needed for this proof:** Rigorous justification of coupling arguments requiring only identical marginals, and evaluating the max over symmetric event covers.
- **Open-access substitute for that topic:** (open-access for topic: identical marginals coupling and union bounds) — J. Matoušek, J. Vondrák / 2008 / The Probabilistic Method / Lecture notes, Charles University.
- **Connection:** Addresses Grader B's Question 2. The near-miss proof currently skips lightly over why identical marginals (without full independence across the $X^{(j)}$ copies) are entirely sufficient to assert $\max X^{(j)} \ge 1/n$. This reference secures that structural leap.
- **Web search query:** `matousek vondrak probabilistic method pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** U. Feige / 2006
- **Title:** On sums of independent random variables with unbounded variance and estimating the average degree in a graph
- **Type:** Paper
- **Venue:** SIAM Journal on Computing, Vol. 35, No. 4
- **Main result or relevant chapter/section:** Proves the related foundational threshold lower bound: for any sequence of independent non-negative random variables with expectation $E[X] = 1$, $\Pr[X \ge 1] \ge 1/13$.
- **Topic needed for this proof:** Coupling and majorization techniques to find global probability minimums over the unconstrained simplex.
- **Open-access substitute for that topic:** (open-access for topic: original author preprint) — U. Feige / 2004 / On sums of independent random variables with unbounded variance / Weizmann Institute technical report.
- **Connection:** While this proof tackles a specific bounded Bernoulli case rather than unbounded variables, Feige's approach to minimizing $\Pr[\sum w_i X_i \ge p]$ by actively collapsing arbitrary unconstrained weight sequences to symmetric extreme points ($w_i = 1/k$) is the exact technique needed to resolve "OC-2" in the notebook. 
- **Web search query:** `feige sums independent random variables pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** S. Boucheron, G. Lugosi, P. Massart / 2013
- **Title:** Concentration Inequalities: A Nonasymptotic Theory of Independence
- **Type:** Book
- **Venue:** Oxford University Press
- **Main result or relevant chapter/section:** Chapter 2 handles basic concentration inequalities, detailing Hoeffding's inequality (SNT-1) and exact nonasymptotic binomial tail behaviors when evaluating symmetric bounded sums.
- **Topic needed for this proof:** Nonasymptotic tail bounds for binomial and bounded random sums.
- **Open-access substitute for that topic:** (open-access for topic: Nonasymptotic concentration bounds for sums of bounded variables) — G. Lugosi / 2004 / Concentration-of-measure inequalities / Lecture notes.
- **Connection:** To close the necessity proof (Grader A and B's primary critique), the student must prove $\Pr[\sum w_i v_i \ge p] < p$ using adversarial uniform weights. Nonasymptotic concentration bounds are mathematically necessary here to trap the uniform sum away from $p$ strictly inside the open intervals between $1/(n+1)$ and $1/n$.
- **Web search query:** `lugosi concentration measure inequalities lecture notes pdf`
- **Confidence (bibliographic):** HIGH
