# Librarian Findings — grader3_aba8b48b7ecb_proof_stage1_solver0_20260531_014720
**Generated:** 2026-05-31T01:52:21  
**Inputs:** notebook=8996 chars, proof=4135 chars, gap_report=2503 chars  
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
- [Book] Feller, W. / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 — Wiley — IDs: no ID — Provides the foundational algebraic evaluations for exact discrete binomial tail probabilities needed to explicitly calculate the necessity counterexamples requested by Graders A and B. — search: `feller introduction probability theory vol 1 pdf`
- [Monograph] Marshall, A. W., Olkin, I., Arnold, B. C. / 2011 — Inequalities: Theory of Majorization and Its Applications — Springer — IDs: no ID — Resolves OC-2 and directly addresses IPT-54 by providing the Schur-convexity theorems required to rigorously collapse the unconstrained problem simplex into symmetric uniform weights. — search: `marshall olkin inequalities theory majorization pdf`
- [Book] Alon, N., Spencer, J. H. / 2016 — The Probabilistic Method — Wiley — IDs: no ID — Directly addresses Grader B's slip by explaining how the Union Bound can be unconditionally applied to families of heavily dependent sets, legally justifying the cyclic coupling step. — search: `alon spencer probabilistic method pdf`
- [Paper] Anderson, T. W., Samuels, S. M. / 1967 — Some Inequalities for Binomial and Poisson Probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — IDs: no ID — Verifies SNT-2, supplying the strict monotonic machinery necessary to track how binomial tail probabilities shift across dimensions for intermediate interval counterexamples. — search: `anderson samuels inequalities binomial poisson probabilities pdf`

## RELATED
- [Paper] Hoeffding, W. / 1956 — On the distribution of the number of successes in independent trials — Annals of Mathematical Statistics — IDs: no ID — Directly complements majorization by mathematically proving that extrema for functions of sums of independent Bernoulli variables are achieved at "collapsed" or symmetric discrete configurations (proves OC-2). — search: `hoeffding distribution number successes independent trials pdf`
- [Paper] Slud, E. V. / 1977 — Distribution Inequalities for the Binomial Law — The Annals of Probability — IDs: no ID — Verifies SNT-3, providing the specific standard normal bounds necessary for rigorously restricting discrete binomial tails from below when $p \le 1/2$. — search: `slud distribution inequalities binomial law pdf`
- [Book] Thorisson, H. / 2000 — Coupling, Stationarity, and Regeneration — Springer — IDs: no ID — Closes Grader B's dependency gap by providing the formal proof that deterministic-sum joint couplings perfectly maintain the strictly independent marginal distributions of their constituent variables. — search: `thorisson coupling stationarity regeneration pdf`

## SOMEWHAT RELATED
- [Paper] Hoeffding, W. / 1963 — Probability Inequalities for Sums of Bounded Random Variables — Journal of the American Statistical Association — IDs: no ID — Verifies SNT-1 (Hoeffding's Inequality), serving as a standard fallback concentration bound, though generally too loose for the exact explicit boundary probabilities required for the counterexamples here. — search: `hoeffding probability inequalities bounded random variables pdf`
- [Book] Motwani, R., Raghavan, P. / 1995 — Randomized Algorithms — Cambridge University Press — IDs: no ID — Frames the proof's deterministic parallel coupling trick as a standard derandomization/randomized rounding method, providing algorithmic intuition for the discrete construction. — search: `motwani raghavan randomized algorithms pdf`

## NOT MUCH
- (None; all retrieved sources natively map to specific named theorems, open conjectures, or explicit grader gaps within the proof evaluation).

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- **[Book] Feller, W. / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 — Wiley — IDs: no ID**
  - **Addresses:** Grader A Area for Improvement 1 (and Scaffolding 2 & 3) / Grader B Area for Improvement 1.
  - **Load-bearing piece:** Chapter VI ("The Binomial and Poisson Distributions") provides the explicit, elementary discrete formulas for exact binomial tail probability calculations required to construct and evaluate the $m=k+1$ equal-weight counterexamples for non-reciprocal values of $p$.

- **[Book] Alon, N., Spencer, J. H. / 2016 — The Probabilistic Method — Wiley — IDs: no ID**
  - **Addresses:** Grader B Area for Improvement 4 ("explicitly clarify that dependence among the $X^{(j)}$ is harmless").
  - **Load-bearing piece:** Chapter 1 ("The Basic Method") explicitly establishes that the Union Bound (Boole's Inequality) holds universally regardless of any extreme structural dependence between the underlying constituent events.

## SUPPORTING

- **[Paper] Anderson, T. W., Samuels, S. M. / 1967 — Some Inequalities for Binomial and Poisson Probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — IDs: no ID**
  - Useful machinery for proving the exact strict monotonic step-downs in cumulative binomial threshold probabilities when scaling the equal-weights dimension for counterexamples.

- **[Paper] Hoeffding, W. / 1956 — On the distribution of the number of successes in independent trials — Annals of Mathematical Statistics — IDs: no ID**
  - Extremely relevant background literature for the broader problem (resolves OC-2), proving that expected value extrema for independent Bernoulli sums are globally achieved at symmetric, discrete points.

- **[Paper] Slud, E. V. / 1977 — Distribution Inequalities for the Binomial Law — The Annals of Probability — IDs: no ID**
  - Provides rigorous analytical bounds for discrete binomial tails, useful if the necessity counterexamples require strict bounding rather than direct calculation.

- **[Monograph] Marshall, A. W., Olkin, I., Arnold, B. C. / 2011 — Inequalities: Theory of Majorization and Its Applications — Springer — IDs: no ID**
  - Essential reference for the broader problem's requirement of Schur-convexity to justify weight-collapsing (OC-2), though not strictly required to plug the immediate "necessity/counterexample" gap identified by the graders.

## REDUNDANT

- **[Book] Thorisson, H. / 2000 — Coupling, Stationarity, and Regeneration — Springer — IDs: no ID**
  - Overlaps with *Alon & Spencer* regarding the harmlessness of structural dependence within couplings; the probabilistic method text is more direct for justifying a basic union bound.

## PERIPHERAL

- **[Paper] Hoeffding, W. / 1963 — Probability Inequalities for Sums of Bounded Random Variables — Journal of the American Statistical Association — IDs: no ID**
  - General concentration bounds are too loose to securely identify the exact mathematical probability boundary violations needed for the counterexamples.

- **[Book] Motwani, R., Raghavan, P. / 1995 — Randomized Algorithms — Cambridge University Press — IDs: no ID**
  - While it covers derandomization conceptually similar to the coupling, it is strictly algorithmic and does not provide the exact analytical probability bounding needed here.

## UNFAMILIAR
*(None)*

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [Book] Feller, W. / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 — Wiley — IDs: no ID — Provides the foundational algebraic evaluations for exact discrete binomial tail probabilities needed to explicitly calculate the necessity counterexamples requested by Graders A and B. — search: `feller introduction probability theory vol 1 pdf`
  - **Gap Addressed:** Grader A's Area for Improvement 1 (and Scaffolding Questions 2 & 3); Grader B's Area for Improvement 1 and 2.
  - **The Load-Bearing Piece:** Chapter VI ("The Binomial and the Poisson Distributions") provides the exact combinatorial formulas necessary to algebraically evaluate the $m=k+1$ equal weight counterexample and rigorously prove its threshold probability is strictly less than $p$.

- [Book] Alon, N., Spencer, J. H. / 2016 — The Probabilistic Method — Wiley — IDs: no ID — Directly addresses Grader B's slip by explaining how the Union Bound can be unconditionally applied to families of heavily dependent sets, legally justifying the cyclic coupling step. — search: `alon spencer probabilistic method pdf`
  - **Gap Addressed:** Grader B's Area for Improvement 4 ("Slip: The proof should explicitly clarify that dependence among the $X^{(j)}$ is harmless").
  - **The Load-Bearing Piece:** Chapter 1 ("The Basic Method") explicitly establishes the principle that the Union Bound (Boole's Inequality) holds unconditionally regardless of arbitrary dependence among the constituent events, mathematically securing the lower bound step despite the deterministic sum constraint.

## SUPPORTING

- [Paper] Anderson, T. W., Samuels, S. M. / 1967 — Some Inequalities for Binomial and Poisson Probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — IDs: no ID — Verifies SNT-2, supplying the strict monotonic machinery necessary to track how binomial tail probabilities shift across dimensions for intermediate interval counterexamples. — search: `anderson samuels inequalities binomial poisson probabilities pdf`
  - *Note:* Useful for tracking strict cumulative binomial monotonicity when generalizing the necessity counterexamples across different non-reciprocal interval gaps.

- [Book] Thorisson, H. / 2000 — Coupling, Stationarity, and Regeneration — Springer — IDs: no ID — Closes Grader B's dependency gap by providing the formal proof that deterministic-sum joint couplings perfectly maintain the strictly independent marginal distributions of their constituent variables. — search: `thorisson coupling stationarity regeneration pdf`
  - *Note:* Provides the formal measure-theoretic background on deterministic-sum joint couplings maintaining independent marginal distributions to safely back up the probabilistic construction.

## REDUNDANT

(None)

## PERIPHERAL

- [Monograph] Marshall, A. W., Olkin, I., Arnold, B. C. / 2011 — Inequalities: Theory of Majorization and Its Applications — Springer — IDs: no ID — Resolves OC-2 and directly addresses IPT-54 by providing the Schur-convexity theorems required to rigorously collapse the unconstrained problem simplex into symmetric uniform weights. — search: `marshall olkin inequalities theory majorization pdf`
  - *Note:* While highly relevant to solving the continuous domain sufficiency (OC-2), it does not address the specific grader gaps for *this* proof, which strictly target the missing discrete necessity counterexamples.
- [Paper] Hoeffding, W. / 1956 — On the distribution of the number of successes in independent trials — Annals of Mathematical Statistics — IDs: no ID — Directly complements majorization by mathematically proving that extrema for functions of sums of independent Bernoulli variables are achieved at "collapsed" or symmetric discrete configurations (proves OC-2). — search: `hoeffding distribution number successes independent trials pdf`
  - *Note:* Addresses related extrema principles (OC-2) for non-identically distributed variables, but does not resolve the specific uniform counterexample construction demanded by the graders.
- [Paper] Slud, E. V. / 1977 — Distribution Inequalities for the Binomial Law — The Annals of Probability — IDs: no ID — Verifies SNT-3, providing the specific standard normal bounds necessary for rigorously restricting discrete binomial tails from below when $p \le 1/2$. — search: `slud distribution inequalities binomial law pdf`
  - *Note:* Provides normal approximations which are inappropriate for the exact discrete evaluations demanded for the counterexamples.
- [Paper] Hoeffding, W. / 1963 — Probability Inequalities for Sums of Bounded Random Variables — Journal of the American Statistical Association — IDs: no ID — Verifies SNT-1 (Hoeffding's Inequality), serving as a standard fallback concentration bound, though generally too loose for the exact explicit boundary probabilities required for the counterexamples here. — search: `hoeffding probability inequalities bounded random variables pdf`
  - *Note:* The general concentration bounds supplied are too loose for calculating the strict necessity failure thresholds.
- [Book] Motwani, R., Raghavan, P. / 1995 — Randomized Algorithms — Cambridge University Press — IDs: no ID — Frames the proof's deterministic parallel coupling trick as a standard derandomization/randomized rounding method, providing algorithmic intuition for the discrete construction. — search: `motwani raghavan randomized algorithms pdf`
  - *Note:* The algorithmic derandomization context is tangential to providing the formal probability measure bounds required by Grader B.

## UNFAMILIAR

(None)

## Narrower draw 2
## LOAD-BEARING

- [Book] Alon, N., Spencer, J. H. / 2016 — The Probabilistic Method — Wiley — IDs: no ID — Directly addresses Grader B's slip by explaining how the Union Bound can be unconditionally applied to families of heavily dependent sets, legally justifying the cyclic coupling step.
  - **Addresses:** Grader B Area 4 (Slip: The proof should explicitly clarify that dependence among the $X^{(j)}$ is harmless).
  - **Justification:** Chapter 1 ("The Basic Method") provides the canonical mathematical justification that the Union Bound (Boole's inequality) applies unconditionally to bound the maximum of variables, completely bypassing any need for independence among the coupled sequences.

- [Paper] Anderson, T. W., Samuels, S. M. / 1967 — Some Inequalities for Binomial and Poisson Probabilities — Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability — IDs: no ID — Verifies SNT-2, supplying the strict monotonic machinery necessary to track how binomial tail probabilities shift across dimensions for intermediate interval counterexamples.
  - **Addresses:** Grader A Area 1 (The "only if" necessity direction is missing) and Grader B Area 2 (The "if and only if" theorem relies on an unproved existential claim).
  - **Justification:** The main monotonicity theorem supplies the exact analytical inequality machinery needed to rigorously bound the discrete binomial tail probability of the uniform weight counterexamples strictly below $p$.

- [Book] Feller, W. / 1968 — An Introduction to Probability Theory and Its Applications, Vol. 1 — Wiley — IDs: no ID — Provides the foundational algebraic evaluations for exact discrete binomial tail probabilities needed to explicitly calculate the necessity counterexamples requested by Graders A and B.
  - **Addresses:** Grader A Area 1 (The "only if" necessity direction is missing) and Grader B Area 1.
  - **Justification:** Chapter VI supplies the foundational probability definitions required to explicitly compute and algebraically evaluate the $m=k+1$ uniform weight binomial counterexamples requested in the grader's scaffolding questions.

## SUPPORTING

- [Book] Thorisson, H. / 2000 — Coupling, Stationarity, and Regeneration — Springer — IDs: no ID — Closes Grader B's dependency gap by providing the formal proof that deterministic-sum joint couplings perfectly maintain the strictly independent marginal distributions of their constituent variables.
  - *Note:* Useful formal background for justifying the deterministic sum coupling's validity in maintaining identical marginals, though Alon & Spencer is more direct for the Union Bound dependency gap itself.

## REDUNDANT

(None)

## PERIPHERAL

- [Monograph] Marshall, A. W., Olkin, I., Arnold, B. C. / 2011 — Inequalities: Theory of Majorization and Its Applications — Springer — IDs: no ID — Resolves OC-2 and directly addresses IPT-54 by providing the Schur-convexity theorems required to rigorously collapse the unconstrained problem simplex into symmetric uniform weights.
  - *Note:* Addresses continuous sufficiency via simplex collapse (OC-2), which is not part of the missing necessity direction or specific slips flagged by the graders here.
- [Paper] Hoeffding, W. / 1956 — On the distribution of the number of successes in independent trials — Annals of Mathematical Statistics — IDs: no ID — Directly complements majorization by mathematically proving that extrema for functions of sums of independent Bernoulli variables are achieved at "collapsed" or symmetric discrete configurations (proves OC-2).
  - *Note:* Addresses sufficiency constraint bounds (OC-2) rather than the required non-reciprocal counterexamples.
- [Paper] Slud, E. V. / 1977 — Distribution Inequalities for the Binomial Law — The Annals of Probability — IDs: no ID — Verifies SNT-3, providing the specific standard normal bounds necessary for rigorously restricting discrete binomial tails from below when $p \le 1/2$.
  - *Note:* Exact algebraic limits (not normal approximations) are required to fulfill the specific counterexamples demanded by the graders.
- [Paper] Hoeffding, W. / 1963 — Probability Inequalities for Sums of Bounded Random Variables — Journal of the American Statistical Association — IDs: no ID — Verifies SNT-1 (Hoeffding's Inequality), serving as a standard fallback concentration bound, though generally too loose for the exact explicit boundary probabilities required for the counterexamples here.
  - *Note:* The concentration bounds are too loose to securely prove the required binomial tail failure for intermediate counterexamples.
- [Book] Motwani, R., Raghavan, P. / 1995 — Randomized Algorithms — Cambridge University Press — IDs: no ID — Frames the proof's deterministic parallel coupling trick as a standard derandomization/randomized rounding method, providing algorithmic intuition for the discrete construction.
  - *Note:* Conceptually adjacent to the coupling step, but offers no concrete resolution to the logical necessity/dependency gaps flagged.

## UNFAMILIAR

(None)

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical published sources for the standard named theorems used in the notebook, alongside primary monographs and literature needed to close the explicit necessity and coupling gaps identified by the graders.

**1. Anderson / Samuels / 1967**
- **Title**: Some Inequalities for Binomial and Poisson Probabilities
- **Type**: Conference paper
- **Venue**: Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1 (University of California Press)
- **Main result**: Proves that the cumulative probability for the binomial distribution, $\Pr[X_k \le c]$, strictly monotonically decreases to the Poisson limit as the number of trials $k$ increases while the mean is held fixed.
- **Topic needed for this proof**: Strict monotonicity of binomial tail probabilities as dimension changes under a fixed mean.
- **Connection**: Directly verifies the notebook’s **SNT-2**. It provides the analytic machinery needed for Grader A’s Question 3 to show how the explicit probability behaves when transitioning dimensions for counterexamples in intermediate domains $p \in (1/(k+1), 1/k)$.
- **Web search query**: `anderson samuels binomial poisson berkeley symposium pdf`
- **Confidence (bibliographic)**: HIGH

**2. Slud / 1977**
- **Title**: Distribution Inequalities for the Binomial Law
- **Type**: Paper
- **Venue**: The Annals of Probability, Vol. 5, No. 3
- **Main result**: Secures the exact discrete tail probability of a binomial random variable between tight standard normal cumulative distribution bounds for $p \le 1/2$.
- **Topic needed for this proof**: Bounding exact discrete binomial tail sums analytically using the standard normal CDF.
- **Connection**: Directly verifies the notebook’s **SNT-3**. Useful for evaluating the uniform-weight counterexamples demanded by Grader A, securing the algebraic proof that the required binomial tail strictly drops below $p$ for non-reciprocal values.
- **Web search query**: `slud distribution inequalities binomial law pdf`
- **Confidence (bibliographic)**: HIGH

**3. Hoeffding / 1963**
- **Title**: Probability Inequalities for Sums of Bounded Random Variables
- **Type**: Paper
- **Venue**: Journal of the American Statistical Association, Vol. 58, No. 301
- **Main result**: Establishes the canonical concentration inequality (now known as Hoeffding's Inequality) bounding the tail probabilities of sums of independent, strictly bounded random variables.
- **Topic needed for this proof**: Exponential tail bounds for sums of bounded independent random variables.
- **Connection**: Verifies **SNT-1** from the notebook. 
- **Web search query**: `hoeffding probability inequalities bounded random variables pdf`
- **Confidence (bibliographic)**: HIGH

**4. Marshall / Olkin / Arnold / 2011 (2nd Edition)**
- **Title**: Inequalities: Theory of Majorization and Its Applications
- **Type**: Monograph
- **Venue**: Springer
- **Main result**: Chapter 12 provides a comprehensive treatment of majorization and Schur-convexity as applied to probability distributions, proving that symmetric uniform distributions globally minimize/maximize specific classes of tail events.
- **Topic needed for this proof**: Using majorization to rigorously prove that uniform symmetric weights globally minimize the tail probability for sums of independent bounded variables.
- **Open-access substitute for that topic**: (open-access for topic: majorization bounds and Schur-convexity in probability) — I. Pinelis / 2006 / Binomial upper bounds on uniformly bounded martingales / arxiv
- **Connection**: Directly addresses **OC-2** (which failed previously in IPT-54 for lacking majorization) and answers Grader A's scaffolding regarding equal weights. To disprove the global claim for a specific $p$, one must know which weight distribution yields the worst-case probability minimum; this text provides the structural majorization proof that $w_i = 1/k$ is the canonical worst case.
- **Web search query**: `marshall olkin inequalities theory majorization pdf`
- **Confidence (bibliographic)**: HIGH

**5. Feller / 1968 (3rd Edition)**
- **Title**: An Introduction to Probability Theory and Its Applications, Volume 1
- **Type**: Book
- **Venue**: Wiley
- **Main result**: Chapter VI extensively develops the rigorous algebraic evaluation and bounding of exact discrete binomial tail events, devoid of continuous approximation assumptions.
- **Topic needed for this proof**: Explicit algebraic calculation of binomial probabilities for low-dimensional counterexamples.
- **Open-access substitute for that topic**: (open-access for topic: elementary binomial distribution tail evaluations) — Dembo / Probability Theory Stat 310 Lecture Notes / Stanford
- **Connection**: Answers Grader A's Fallacy 1 and Scaffolding Questions 1-2. By taking $p=2/3, m=2$ and $w=(1/2, 1/2)$, the counterexample collapses cleanly to evaluating $\Pr[\text{Binomial}(2, 2/3) \ge 2]$. Feller provides the foundational text for formalizing these "equal weights convert the problem into a binomial-tail calculation" bounds.
- **Web search query**: `feller introduction probability theory volume 1 pdf`
- **Confidence (bibliographic)**: HIGH

**6. Alon / Spencer / 2016 (4th Edition)**
- **Title**: The Probabilistic Method
- **Type**: Book
- **Venue**: Wiley
- **Main result**: Chapter 1 details the canonical union bound (Boole's inequality) and demonstrates how coupling parallel randomized constructions allows the deduction of structural bounds over heavily dependent variables.
- **Topic needed for this proof**: Applying the union bound across deterministically coupled (dependent) parallel events to force a lower probability bound.
- **Open-access substitute for that topic**: (open-access for topic: basic probabilistic method and union bound over dependent events) — Matousek, Vondrak / 2008 / The Probabilistic Method / Lecture Notes, Charles University
- **Connection**: Directly responds to Grader B's Scaffolding Question 2 and Slip 4. The proof relies on a sophisticated cyclic coupling of $k$ sequences that sum to $1$ to force the sub-conclusion. Grader B notes the proof fails to justify why the dependence of the $X^{(j)}$ variables does not invalidate the union bound. This text provides the canonical framework showing that the union bound fundamentally does not require independence. 
- **Web search query**: `alon spencer probabilistic method pdf`
- **Confidence (bibliographic)**: HIGH

## Gauntlet draw 1
Here are the canonical references and topic-keyed substitutes that address the specific theorems invoked in the notebook, as well as the structural gaps identified by the graders (specifically regarding binomial tail bounds, majorization for uniform weights, and the dependent coupling).

**1. Anderson, T. W. / Samuels, S. M. (1967)**
- **Title:** Some Inequalities for Binomial and Poisson Probabilities
- **Type:** Paper
- **Venue:** Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Statistics
- **Main result or relevant section:** Proves that for a fixed mean $\lambda$, the probability $\Pr[X \le c]$ for a binomial random variable $X$ monotonically decreases as the number of trials $k$ increases, approaching the Poisson limit from above.
- **Topic needed for this proof:** Monotonicity of the cumulative binomial probability as the dimension increases while the mean is held constant.
- **Open-access substitute for that topic:** (open-access for topic: Monotonic convergence of binomial probabilities) — Jogdeo and Samuels (1968), "Monotone convergence of binomial probabilities and a generalization of Ramanujan's equation" (often openly hosted in university repositories).
- **Connection:** Identified directly in the notebook as SNT-2. This is crucial for formalizing Grader A's counterexample: to show the necessity direction across all intermediate intervals, one must track how the binomial tail probability $\Pr[\text{Binomial}(k+1, p) \ge 2]$ shifts as $k$ varies.
- **Web search query:** `anderson samuels inequalities binomial poisson probabilities pdf`
- **Confidence (bibliographic):** HIGH

**2. Slud, E. V. (1977)**
- **Title:** Distribution Inequalities for the Binomial Law
- **Type:** Paper
- **Venue:** Annals of Probability, Vol. 5, No. 2
- **Main result or relevant section:** Establishes rigorous bounds bridging exact discrete binomial tail probabilities with the standard normal CDF, specifically for regimes where $p \le 1/2$.
- **Topic needed for this proof:** Normal approximations bounding the discrete binomial tail probability strictly from below or above.
- **Open-access substitute for that topic:** (open-access for topic: Strict bounds on the binomial tail via normal approximation) — Lecture notes covering Slud's inequality and the de Moivre-Laplace theorem.
- **Connection:** Identified in the notebook as SNT-3. Necessary for closing the algebraic gap in the continuous domain (OC-3 / Grader A's Question 3) by strictly evaluating whether the counterexample probability evaluates to $< p$.
- **Web search query:** `slud distribution inequalities binomial law pdf`
- **Confidence (bibliographic):** HIGH

**3. Marshall, A. W. / Olkin, I. / Arnold, B. C. (2011)**
- **Title:** Inequalities: Theory of Majorization and Its Applications
- **Type:** Monograph
- **Venue:** Springer (2nd Edition; originally published 1979)
- **Main result or relevant section:** Chapter 11 (on probabilities and random variables) covers Schur-convexity and how functions of probability vectors (like the tail probabilities of weighted sums of i.i.d. random variables) are minimized or maximized at symmetric extreme points of the simplex.
- **Topic needed for this proof:** Schur-convexity of symmetric multivariate distributions to justify reducing an unconstrained probability simplex to uniform weights on a subset.
- **Open-access substitute for that topic:** (open-access for topic: Introduction to majorization and Schur-convexity in probability) — survey preprints or author-hosted draft chapters on majorization (e.g., E. Jorswieck's openly hosted materials on majorization).
- **Connection:** The notebook explicitly notes (IPT-54) that assuming the extreme points occur at uniform weights without majorization is a fallacy. Grader A asks to explicitly construct the $m=k+1$ equal weights counterexample; this monograph provides the structural theorem (Schur-concavity/convexity) required to legally collapse the general weights $w_i$ to uniform weights in the first place (resolving OC-2).
- **Web search query:** `marshall olkin inequalities theory majorization pdf`
- **Confidence (bibliographic):** HIGH

**4. Alon, N. / Spencer, J. H. (2016)**
- **Title:** The Probabilistic Method
- **Type:** Book
- **Venue:** Wiley (4th Edition)
- **Main result or relevant section:** Chapter 1 (The Basic Method) and Chapter 5 (Correlation Inequalities) meticulously detail how the Union Bound applies to arbitrary families of sets/events regardless of underlying dependencies.
- **Topic needed for this proof:** The unconditional application of the union bound over highly correlated (or deterministically coupled) random variables.
- **Open-access substitute for that topic:** (open-access for topic: Dependent union bounds and basic probabilistic methods) — Author-hosted drafts of earlier editions or standard discrete math lecture notes covering the probabilistic method.
- **Connection:** Grader B's Question 2 and critique point #4 demand explicit clarification on why the dependence among the $X^{(j)}$ variables (which deterministically sum to 1) is harmless when claiming the lower bound. This text provides the canonical justification that the union bound fundamentally ignores dependence geometry.
- **Web search query:** `alon spencer probabilistic method pdf`
- **Confidence (bibliographic):** HIGH

**5. Hoeffding, W. (1963)**
- **Title:** Probability Inequalities for Sums of Bounded Random Variables
- **Type:** Paper
- **Venue:** Journal of the American Statistical Association
- **Main result or relevant section:** Provides foundational exponential bounds for the deviation of sums of independent bounded random variables from their expected value. 
- **Topic needed for this proof:** Exponential tail bounds for sums of independent, bounded random variables.
- **Open-access substitute for that topic:** (open-access for topic: Hoeffding's inequality for bounded independent variables) — Almost universal coverage in openly hosted machine learning or probability concentration lecture notes.
- **Connection:** Identified as SNT-1. If the solver moves beyond exact combinatorial calculation for large dimensions $m$, Hoeffding's is the canonical tool to prove that the tail probability of the uniformly weighted sum drops precipitously below $p$, fulfilling Grader A's necessity constraint.
- **Web search query:** `hoeffding probability inequalities bounded random variables pdf`
- **Confidence (bibliographic):** HIGH

**6. Feller, W. (1968)**
- **Title:** An Introduction to Probability Theory and Its Applications, Vol. 1
- **Type:** Book
- **Venue:** Wiley (3rd Edition)
- **Main result or relevant section:** Chapter 6 covers the binomial and Poisson distributions, detailing explicit combinatorial limits and the exact evaluation of the central and tail terms.
- **Topic needed for this proof:** Exact combinatorial evaluation of the binomial terms $\Pr[X \ge 2]$ to manually verify strict bounds against a parameter $p$.
- **Open-access substitute for that topic:** (open-access for topic: Exact binomial tail term calculations) — Standard university lecture notes on discrete probability distributions.
- **Connection:** Addresses Grader A's Question 3. To build the necessity counterexample for equal weights $w_i = 1/(k+1)$, the solver MUST explicitly calculate $\Pr[\text{Binomial}(k+1, p) \ge 2] = 1 - (1-p)^{k+1} - (k+1)p(1-p)^k$ and show it is strictly less than $p$ for the interval $(1/(k+1), 1/k)$.
- **Web search query:** `feller introduction probability theory vol 1 pdf`
- **Confidence (bibliographic):** HIGH

**7. Motwani, R. / Raghavan, P. (1995)**
- **Title:** Randomized Algorithms
- **Type:** Book
- **Venue:** Cambridge University Press
- **Main result or relevant section:** The chapters on derandomization (conditional expectation) and randomized rounding showcase techniques where dependent coupling of variables is used to force constraint satisfaction (e.g., forcing variables to sum to exactly 1).
- **Topic needed for this proof:** Constructing cyclic/dependent couplings of random variables to satisfy deterministic sum constraints while preserving marginal distributions.
- **Open-access substitute for that topic:** (open-access for topic: Derandomization and dependent rounding couplings) — Author-hosted lecture notes for randomized algorithms courses.
- **Connection:** The core logic of "PS-B Step 1" (constructing $k$ sequences that deterministically sum to 1 to force a maximal element) is a classic discrete dependent coupling trick. Citing this methodology addresses Grader B's Question 2 by anchoring the "magic step" in standard algorithmic probability practice.
- **Web search query:** `motwani raghavan randomized algorithms pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed substitutes to verify the named theorems, rigorously frame the counterexamples for the omitted necessity direction, and mathematically justify the exact coupling techniques used in the proof.

**1. Verification for SNT-1 (Hoeffding's Inequality)**
- **Authors / Year:** Wassily Hoeffding / 1963
- **Title:** Probability Inequalities for Sums of Bounded Random Variables
- **Type:** paper
- **Venue:** Journal of the American Statistical Association
- **Main result:** Establishes the canonical exponentially decaying upper bounds on the tail probability that the sum of independent bounded random variables strictly exceeds its expected value.
- **Topic needed for this proof:** The canonical Hoeffding concentration inequality for sums of independent bounded variables.
- **Connection:** Confirms the canonical citation for SNT-1 referenced in the notebook.
- **Web search query:** `hoeffding probability inequalities sums bounded pdf`
- **Confidence:** HIGH

**2. Verification for SNT-2 (Anderson-Samuels Monotonicity Theorem)**
- **Authors / Year:** T. W. Anderson, S. M. Samuels / 1967
- **Title:** Some Inequalities for Binomial and Poisson Probabilities
- **Type:** paper
- **Venue:** Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability
- **Main result:** Proves that for a fixed mean and fixed boundary threshold, the cumulative probability of a binomial distribution monotonically decreases as the number of trials increases, approaching the Poisson limit from above.
- **Topic needed for this proof:** Monotonicity bounds for cumulative binomial probabilities as the dimension increases.
- **Connection:** Verifies SNT-2. Provides the theoretical groundwork for structurally comparing tail boundaries of binomial sums across different dimensions $k$, necessary for bounding the generalized counterexamples.
- **Web search query:** `anderson samuels inequalities binomial poisson probabilities pdf`
- **Confidence:** HIGH

**3. Verification for SNT-3 (Slud's Inequality)**
- **Authors / Year:** Eric V. Slud / 1977
- **Title:** Distribution inequalities for the binomial law
- **Type:** paper
- **Venue:** The Annals of Probability
- **Main result:** Derives rigorous analytical lower bounds for the right discrete tail of the binomial distribution $\Pr[\text{Binomial}(n, p) \ge c]$ securely using the standard normal cumulative distribution function. 
- **Topic needed for this proof:** Exact algebraic lower-bounding techniques for discrete binomial tail distributions via standard normal approximation.
- **Connection:** Verifies SNT-3. Necessary for the continuous domain sufficiency attempts (PS-C) aiming to securely bound the discrete binomial tail from below for $p \le 1/2$.
- **Web search query:** `slud distribution inequalities binomial law pdf`
- **Confidence:** HIGH

**4. Closing the Necessity Gap: Binomial Tail Calculations**
- **Authors / Year:** William Feller / 1968
- **Title:** An Introduction to Probability Theory and Its Applications, Volume 1 (3rd Edition)
- **Type:** book
- **Venue:** John Wiley & Sons
- **Main result:** Chapter VI provides exhaustive derivations of exact algebraic formulas, partial sum bounds, and explicit low-order evaluations for binomial distributions. 
- **Topic needed for this proof:** Exact low-order polynomial expansions for small-threshold discrete binomial tail probabilities (specifically $\Pr[\text{Binomial}(k+1, p) \ge 2]$).
- **Open-access substitute for that topic:** (open-access for topic: Exact bounds and combinatorial calculations for binomial tail probabilities) — Mitzenmacher, Upfal / 2005 / Probability and Computing / Cambridge University Press (pre-publication drafts are widely hosted on academic pages)
- **Connection:** Directly addresses Grader A's scaffolding questions 2/3 and Grader B's question 3. Utilizing Feller's exact expansions formally proves that for $p \in (1/(k+1), 1/k)$, the symmetric extreme setup $w_i = 1/(k+1)$ creates a counterexample where the resulting discrete binomial tail strictly evaluates to $\Pr \le p$, structurally sealing the missing necessity direction.
- **Web search query:** `feller introduction to probability theory volume 1 pdf`
- **Confidence:** HIGH

**5. Closing the Independence Slip: Coupling Formalism**
- **Authors / Year:** Hermann Thorisson / 2000
- **Title:** Coupling, Stationarity, and Regeneration
- **Type:** book
- **Venue:** Springer
- **Main result:** Exhaustively develops the theoretical foundations for defining random variables on a joint space (couplings) that deterministicically satisfy structural sum constraints while strictly maintaining targeted independent marginal distributions.
- **Topic needed for this proof:** The formal justification that deterministic-sum joint couplings perfectly preserve marginal probability constraints.
- **Open-access substitute for that topic:** (open-access for topic: Formal definitions of couplings and strict preservation of marginal distributions) — Levin, Peres, Wilmer / 2009 / Markov Chains and Mixing Times / American Mathematical Society (author-hosted PDF available)
- **Connection:** Answers Grader B's Slip #4, which requests explicit clarification that the dependence among the $X^{(j)}$ sequence partitions is mathematically harmless and structurally allows the Union Bound. 
- **Web search query:** `thorisson coupling stationarity regeneration pdf`
- **Confidence:** HIGH

**6. Closing the Assumed Simplex Collapse (OC-2 & IPT-54)**
- **Authors / Year:** Wassily Hoeffding / 1956
- **Title:** On the distribution of the number of successes in independent trials
- **Type:** paper
- **Venue:** Annals of Mathematical Statistics
- **Main result:** Strictly proves that the extrema of expected values for nonlinear functions of sums of independent Bernoulli variables (subject to fixed mean conditions) are globally achieved at extreme "collapsed" probability configurations (e.g., matching symmetric clusters or 0/1 values).
- **Topic needed for this proof:** Rigorous reduction of probability minimum problems over unconstrained continuous simplices to structurally symmetric extreme configurations.
- **Connection:** Provides the missing theoretical engine to decisively prove Open Conjecture 2 (OC-2). By porting Hoeffding's generalized extremum technique for Bernoullis, the proof can overcome the failure identified in IPT-54 ("Assuming Simplex Collapse Without Majorization") and natively reduce the global minimum search to symmetric weights $w_i = 1/k$.
- **Web search query:** `hoeffding distribution number successes independent trials pdf`
- **Confidence:** HIGH
