<!-- Generated 2026-05-31T02:04:14 -->
<!-- Source PDF: slud__distribution_inequalities_for_the_binomial_law.pdf (289184 bytes) -->
<!-- Citation: Slud (1977). Distribution inequalities for the binomial law. The Annals of Probability. -->

```markdown
# Distribution inequalities for the binomial law. Slud (1977). The Annals of Probability.

## Definitions
- **Definition 3.1.** Define 9n + 1 l(n) = − , 3n(12n + 1) 18n − 1 u(n) = − . 12n(6n + 1)
- **Definition 3.5.** For any η, k ∈ Z+ with 2η ≤ k, define k−η X 1 ψη (k) = p . j=η j(k − j)

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1.** When n is odd and p < 1/2, (n−1)/2 X 2j 2j (1.2) P[B(p, n) ≥ n/2] = p − (1/2 − p) σ j=1 j X 2j (1.3) = (1/2 − p) σ 2j . j j≥(n+1)/2
  *Proof:* Combines the finite sum from Lemma 2.2 and the infinite sum from Lemma 2.3.

- **Lemma 2.1.** When n is odd, n+1 P[B(p, n + 2) ≥ (n + 2)/2] − P[B(p, n) ≥ n/2] = (p − 1/2) σ n+1 . (n + 1)/2
  *Proof:* Tracks the probability mass of random walks shifting toward the origin over two steps.

- **Lemma 2.2.** When n is odd, (n−1)/2 X 2j 2j P[B(p, n) ≥ n/2] = p − (1/2 − p) σ . j=1 j
  *Proof:* Telescopes the two-step random walk probability differences derived in Lemma 2.1.

- **Lemma 2.3.** When n is odd and p < 1/2, X 2j 2j P[B(p, n) ≥ n/2] = (1/2 − p) σ . j j≥(n+1)/2
  *Proof:* Applies the Taylor expansion of (1 - 4σ^2)^{-1/2} to rewrite the finite summation from Lemma 2.2.

- **Theorem 3.3.** When n is odd and p ∈ (0, 1/2), (1 − 2p)el(n+1) (2σ)n−1 (3.3) P[B(p, n) ≥ n/2] ≥ p − ln(1 − 4σ 2 ) , 2π(n + 1) (2σ)n+1 (3.4) P[B(p, n) ≥ n/2] ≤ p . (1 − 2p) 2π(n + 1)
  *Proof:* Applies Stirling's approximation to the infinite summation and bounds the j^{-1/2} terms trivially.

- **Theorem 3.4.** When p < 1/2 and n is odd, (1 − 2p)el(n+1) (2σ)n+1 (3.5) P[B(p, n) ≥ n/2] ≥ p p . 1 − 4σ 2 (n + 1)/(n + 3) 2π(n + 1)
  *Proof:* Fits an exponential bound to the j^{-1/2} term and applies the geometric sequence formula.

- **Lemma 3.6.** For any η, k ∈ Z+ with 2η ≤ k, ψη (k) ≤ ψη (k + 1) ≤ π.
  *Proof:* Interprets the summation as Riemann sums lower bounding an integral that evaluates to π.

- **Theorem 3.7.** When n is odd and p < 1/2, (2σ)n+1 el(n+1) (2σ)n+1 (3.7) p ≤ P[B(p, n) ≥ n/2] ≤ . 2π(n + 1) 2
  *Proof:* Rearranges the summation algebraically and applies the sequence bounds from Lemma 3.6.

- **Theorem 3.8.** When n is odd and p < 1/2, p 2σ 2 eu(n−1) (1 − (2σ)2n−4 )ψ1 (n − 1) (3.8) P[B(p, n) ≥ n/2] ≥ p − √ , π p 2σ 2 el(2) 1 − (2σ)n−1 (3.9) P[B(p, n) ≥ n/2] ≤ p − √ . π
  *Proof:* Replicates the Riemann sum bound strategy of Theorem 3.7, applied to the finite summation from Lemma 2.2.

- **Theorem 5.1.** Let n odd and p ∈ (0, 1/2) be given, and set p 2 1 − Φ( −(n + 1) ln(4σ 2 )) (2σ)n+1 Υ= p , ∆= p ; 2 − ln(4σ ) 2π(n + 1) then (5.1) (1/2 − p)el(n+1) (Υ + ∆) ≤ P[B(p, n) ≥ n/2] ≤ (1/2 − p)(Υ + ∆(1 + R)), where 1 1 2 R ≤ min 1, − ln(4σ ) . 4 n+1
  *Proof:* Uses the first-order Euler-Maclaurin formula to replace the infinite summation with an integral. Evaluates the integral using Lemma 5.2 and bounds the fractional remainder term to yield R.

- **Lemma 5.2.** When σ ∈ (0, 1/2), p Z ∞ 2j 2 1 − Φ( −(n + 1) ln(4σ 2 )) (2σ) √ dj = p . (n+1)/2 πj − ln(4σ 2 )
  *Proof:* Evaluates the integral exactly using a Gaussian change of variables.

- **Theorem 6.1 (Slud [4]).** Let n, k be nonnegative integers with k ≤ n, and p ∈ [0, 1]. When either (a) p ≤ 1/4 and np ≤ k ≤ n, or (b) np ≤ k ≤ n(1 − p), then k − np (6.1) P[B(p, n) ≥ k] ≥ 1 − Φ √ . σ n
  *Proof:* (no proof in this paper)

- **Theorem 8.1.** When n is odd, k ∈ Z ∩ [0, n/2), and p ∈ (0, 1/2), k (n−1)/2 X 1 n p k 2j (8.1) P[B(p, n) ≥ + k] = p2k+1 − −p− σ 2j 2 1−p 2 2j j+k j=k+1 k X p 1 k 2j (8.2) = −p− σ 2j . 1−p 2 2j j+k j≥(n+1)/2 Furthermore (n−1)/2 X k 2j n (8.3) P[B(1/2, n) ≥ + k] = 2−2k−1 + 4−j 2 2j j+k j=k+1 1 X k 2j (8.4) = − 4−j . 2 2j j+k j≥(n+1)/2
  *Proof:* Extends the step analysis to asymmetric tails via generalized telescoping sums. Simplifies the resulting summations using binomial generating function identities.

- **Lemma A.1.** When n is odd and k ∈ Z ∩ [−n/2, n/2], h i n+2 n P B(p, n + 2) ≥ + k − P B(p, n) ≥ + k 2 2 1 k n+1 = p− + p(n+1)/2+k (1 − p)(n+1)/2−k . 2 n+1 (n + 1)/2 + k
  *Proof:* Adapts the random walk step difference logic of Lemma 2.1 to paths terminating at off-center coordinates.

- **Theorem B.1.** When n is odd and 0 ≤ p ≤ 1/2 + 1/2 1 − p 4( n(n+1)−1) 4n+2 1/2 , (n + 1)/2 − np (B.1) P[B(p, n) ≥ n/2] ≥ 1 − Φ √ . σ n When m is even and 0 ≤ p ≤ 1/2 + 1/6 (el(m) /m)1/3 , √ (1/2 − p) m (B.2) P[B(p, m/2) ≥ m/2] ≥ 1 − Φ . σ
  *Proof:* Reduces the conditions to the standard normal bounds of Theorem 5.1. Splits the proof into four cases, using secant and tangent function approximations to weaken the bounds.

- **Lemma C.1.** When p ∈ (0, 1/2) and n odd, l(n+1) (n + 1)/2 − np (n + 1)/2 − np p 2 2σe √ √ − −(n + 1) ln(4σ ) + 1 ≥ 1. σ n σ n
  *Proof:* Lower bounds the algebraic expression by replacing (1-4r)^{-1/2} with linear approximations. Shows the function's derivative with respect to r is negative and checks boundary cases.

- **Lemma C.2.** When 1/2 < p < 1/2 + 1/2 1 − p 4( n(n+1)−1) 4n+2 1/2 and n is odd, 2p − 1 p np − (n + 1)/2 √ ≤ −(n + 1) ln(4σ 2 ) − √ . n+1 σ n
  *Proof:* Rearranges the conditions algebraically using the Taylor expansion of y^{-1/2}.

- **Lemma C.3.** When m is even and p ∈ [p̄, 1/2], el(m) (3/2 − p)(2σ)m φ(β) 1 √ ≥ (1 − 2el(m) σ) min{ , }, 2πm β 2 √ p where β = ((1/2 − p) m)/σ and p̄ = 3/4 − 1/(2el(m) ).
  *Proof:* Takes the derivative to show the left side is decreasing on the target interval. Compares the boundary values using secant and tangent approximations.

- **Theorem D.1.** The following inequalities relate the performance of these bounds: m/2 3m(1/2 − p)2 [4p(1 − p)] ≤ exp − ≤ exp[−m(1 − 2p)2 /2] if p ∈ [0, 1/4]; 3m(1/2 − p)2 [4p(1 − p)]m/2 ≤ exp[−m(1 − 2p)2 /2] ≤ exp − if p ∈ [1/4, 1/2]. (1 + 4p)(1 − p)
  *Proof:* Compares the bounds by algebraically analyzing their exponents and finding their intersection points.

- **Lemma E.1.** Let intervals (a, b] ⊆ (c, d], integers n < m with (d−c)/m ≤ (b−a)/n, and a function f convex and decreasing on (c, d] be given. Let R(f ; (t, u], v) denote R u the Riemann sum approximation of t f consisting of v equal pieces, whose height is f evaluated at their right endpoint. Then R(f ; (a, b], n) ≤ R(f ; (c, d], m).
  *Proof:* Uses the convexity of the function to geometrically compare the block areas of nested Riemann sum partitions.
```