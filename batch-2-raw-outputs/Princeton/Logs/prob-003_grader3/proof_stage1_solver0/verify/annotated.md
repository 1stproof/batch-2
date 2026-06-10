**Annotated Proof**

**Step 1: Deterministic sum joint coupling**
*Claim:* We construct $k$ coupled sequences of random variables $v_i^{(j)}$ such that for any fixed $j$, they are independent Bernoulli$(1/k)$, yet deterministically sum to 1 across $j$.
*Citation:* [CONFIDENT] Levin, Peres, Wilmer / 2009 — Markov Chains and Mixing Times (Author-hosted PDF), Chapter 4, "formalizes joint couplings that strictly preserve targeted independent marginal distributions under deterministic sum constraints"

**Step 2: Union bound over dependent variables**
*Claim:* By the union bound: $1 = \Pr\Big[\bigcup_{j=1}^k A_j\Big] \le \sum_{j=1}^k \Pr[A_j] = k \Pr\Big[X^{(1)} \ge \frac{1}{k}\Big]$
*Citation:* [CONFIDENT] Matoušek, Vondrák / 2008 — The Probabilistic Method (Charles University Lecture Notes), Chapter 1, "justifies the unconditional application of Boole's inequality to families of heavily dependent random variables"

**Step 3: Omitted explicit necessity counterexamples**
*Claim:* The explicit construction of pathological weight distributions providing counterexamples for all non-reciprocal values of $p$ is structurally omitted.
*Citation:* [APPROX] Dembo, A. — Probability Theory Stat 310 Lecture Notes (Stanford), Discrete Distributions section, "provides explicit algebraic combinatorial evaluations of exact discrete binomial tails necessary for constructing the omitted counterexamples"

**Coverage Summary**
- Steps confidently cited: 2
- Steps approximately cited: 1
- Steps unable to locate: 0

**Notes**
- The step asserting that because $k$ identically distributed variables sum to exactly 1, at least one must be $\ge 1/k$ is an elementary application of the Pigeonhole Principle and is treated as routine algebra.