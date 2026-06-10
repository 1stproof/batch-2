<!-- Generated 2026-05-31T02:03:57 -->
<!-- Source PDF: slud__distribution_inequalities_for_the_binomial_law.pdf (289184 bytes) -->
<!-- Citation: Slud, E. V. (1977). Distribution Inequalities for the Binomial Law. The Annals of Probability. -->

# Distribution Inequalities for the Binomial Law. Slud, E. V. (1977). The Annals of Probability.

## Definitions
- **Definition 3.1.** Define
                                        9n + 1
                              l(n) = −            ,
                                      3n(12n + 1)
                                        18n − 1
                             u(n) = −             .
                                      12n(6n + 1)

- **Definition 3.5.** For any η, k ∈ Z+ with 2η ≤ k, define
                                             k−η
                                             X      1
                                  ψη (k) =       p         .
                                             j=η  j(k − j)

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1.** When n is odd and p < 1/2,
                                                                                                 (n−1)/2   
                                                                                                   X   2j 2j
(1.2)              P[B(p, n) ≥ n/2] = p − (1/2 − p)                σ
                                                                                                 j=1
                                                                                                        j
                                                                                                X  2j  
(1.3)                                 = (1/2 − p)                σ 2j .
                                                                                                     j
                                                                                              j≥(n+1)/2
  *Proof:* Combines the finite sum expression from Lemma 2.2 and the infinite sum expression from Lemma 2.3.

- **Lemma 2.1.** When n is odd,
                                                                       
                                                               n+1
   P[B(p, n + 2) ≥ (n + 2)/2] − P[B(p, n) ≥ n/2] = (p − 1/2)           σ n+1 .
                                                             (n + 1)/2
  *Proof:* Uses a random walk interpretation to track the net change in probability mass from paths changing sign in two steps.

- **Lemma 2.2.** When n is odd,
                                                           (n−1)/2       
                                                            X        2j 2j
                 P[B(p, n) ≥ n/2] = p − (1/2 − p)                        σ .
                                                            j=1
                                                                      j
  *Proof:* Telescopes the difference of binomial tails by iteratively summing the step changes provided by Lemma 2.1.

- **Lemma 2.3.** When n is odd and p < 1/2,
                                                                       
                                                          X          2j 2j
                  P[B(p, n) ≥ n/2] = (1/2 − p)                          σ .
                                                                      j
                                                        j≥(n+1)/2
  *Proof:* Combines the Taylor expansion of $(1 - 4\sigma^2)^{-1/2}$ with the finite sum representation from Lemma 2.2.

- **Theorem 3.3.** When n is odd and p ∈ (0, 1/2),

                                 (1 − 2p)el(n+1) (2σ)n−1                 
(3.3)       P[B(p, n) ≥ n/2] ≥        p                  − ln(1 − 4σ 2 ) ,
                                         2π(n + 1)
                                       (2σ)n+1
(3.4)       P[B(p, n) ≥ n/2] ≤           p          .
                                 (1 − 2p) 2π(n + 1)
  *Proof:* Upper-bounds the $j^{-1/2}$ factor by 1 and lower-bounds it by $j^{-1}$ inside the infinite sum representation, then applies a Taylor expansion.

- **Theorem 3.4.** When p < 1/2 and n is odd,
                                        (1 − 2p)el(n+1) (2σ)n+1
(3.5)       P[B(p, n) ≥ n/2] ≥          p                   p           .
                                1 − 4σ 2 (n + 1)/(n + 3)      2π(n + 1)
  *Proof:* Lower-bounds the $j^{-1/2}$ term using an exponential fit and evaluates the resulting geometric series.

- **Lemma 3.6.** For any η, k ∈ Z+ with 2η ≤ k, ψη (k) ≤ ψη (k + 1) ≤ π.
  *Proof:* Interprets the sum as a Riemann approximation to the integral of $(1 - x^2)^{-1/2}$ and uses the monotonicity of Riemann sums for convex decreasing functions.

- **Theorem 3.7.** When n is odd and p < 1/2,
                  (2σ)n+1 el(n+1)                      (2σ)n+1
(3.7)              p              ≤ P[B(p, n) ≥ n/2] ≤         .
                     2π(n + 1)                            2
  *Proof:* Rearranges the $j^{-1/2}$ term into a double sum using Definition 3.5 and applies the corresponding bounds from Lemma 3.6.

- **Theorem 3.8.** When n is odd and p < 1/2,
                                                  p
                                   2σ 2 eu(n−1)    (1 − (2σ)2n−4 )ψ1 (n − 1)
(3.8)     P[B(p, n) ≥ n/2] ≥ p −                       √                     ,
                                                         π
                                                p
                                   2σ 2 el(2)    1 − (2σ)n−1
(3.9)     P[B(p, n) ≥ n/2] ≤ p −                 √           .
                                                   π
  *Proof:* Similar to Theorem 3.7, but applies the bounds on $\psi_\eta(k)$ to the finite sum representation from Lemma 2.2.

- **Theorem 5.1.** Let n odd and p ∈ (0, 1/2) be given, and set
                    p                    
           2 1 − Φ( −(n + 1) ln(4σ 2 ))                   (2σ)n+1
       Υ=           p                     ,         ∆= p            ;
                             2
                      − ln(4σ )                           2π(n + 1)
then
(5.1)   (1/2 − p)el(n+1) (Υ + ∆) ≤ P[B(p, n) ≥ n/2] ≤ (1/2 − p)(Υ + ∆(1 + R)),
where                                                
                                    1   1        2
                         R ≤ min 1,       − ln(4σ )   .
                                    4 n+1
  *Proof:* Applies the first-order Euler-Maclaurin summation formula to replace the infinite sum with an integral and bounds the remainder terms.

- **Lemma 5.2.** When σ ∈ (0, 1/2),
                                               p                      
                Z ∞            2j     2  1 − Φ(  −(n + 1)  ln(4σ 2 ))
                           (2σ)
                            √    dj =          p                       .
                   (n+1)/2    πj                − ln(4σ 2 )
  *Proof:* Evaluates the integral via a change of variables to match the standard normal density.

- **Theorem 6.1 (Slud [4]).** Let n, k be nonnegative integers with k ≤ n, and p ∈ [0, 1].
When either (a) p ≤ 1/4 and np ≤ k ≤ n, or (b) np ≤ k ≤ n(1 − p), then
                                                        
                                                k − np
(6.1)                 P[B(p, n) ≥ k] ≥ 1 − Φ       √      .
                                                 σ n
  *Proof:* (no proof in this paper)

- **Theorem 8.1.** When n is odd, k ∈ Z ∩ [0, n/2), and p ∈ (0, 1/2),
                                            k (n−1)/2
                                                X  1                       
                    n                   p                     k     2j
(8.1) P[B(p, n) ≥     + k] = p2k+1 −                    −p−                σ 2j
                    2                  1−p            2      2j    j+k
                                               j=k+1
                                     k X                           
                                 p               1      k      2j
(8.2)                      =                       −p−             σ 2j .
                               1−p               2      2j   j+k
                                       j≥(n+1)/2
Furthermore
                                             (n−1)/2               
                           n                   X       k      2j
(8.3)      P[B(1/2, n) ≥     + k] = 2−2k−1 +                        4−j
                           2                           2j   j+k
                                              j=k+1
                                                                
                                    1      X        k      2j
(8.4)                             = −                            4−j .
                                    2              2j     j+k
                                        j≥(n+1)/2
  *Proof:* Rewrites the generalized tail probability as a telescoping series by invoking a generalized random walk lemma to compute boundary terms. Evaluates and simplifies the remaining infinite sums using generating function identities.

- **Lemma A.1.** When n is odd and k ∈ Z ∩ [−n/2, n/2],
                                   h                i
                    n+2                       n
    P B(p, n + 2) ≥      + k − P B(p, n) ≥ + k
                      2                       2
                                          
              1     k          n+1
       = p− +                             p(n+1)/2+k (1 − p)(n+1)/2−k .
              2 n+1        (n + 1)/2 + k
  *Proof:* Computes the net change in probability mass from random walks that end exactly at coordinates adjacent to the origin after $n$ steps.

- **Theorem B.1.** When n is odd and 0 ≤ p ≤ 2 + 2 1 −     4n+2          ,
                                                                    
                                                  (n + 1)/2 − np
(B.1)              P[B(p, n) ≥ n/2] ≥ 1 − Φ             √              .
                                                       σ n
When m is even and 0 ≤ p ≤ 12 + 61 (el(m) /m)1/3 ,
                                                           √  
                                                  (1/2 − p) m
(B.2)          P[B(p, m/2) ≥ m/2] ≥ 1 − Φ                      .
                                                        σ
  *Proof:* Relaxes the integral bounds from Theorem 5.1 to prove Slud's inequality. Uses tangent and secant approximations to the standard normal distribution and density functions across different intervals of $p$.

- **Lemma C.1.** When p ∈ (0, 1/2) and n odd,
                                                                                  
      l(n+1)        (n + 1)/2 − np           (n + 1)/2 − np p              2
2σe                       √                        √       − −(n + 1) ln(4σ ) + 1 ≥ 1.
                         σ n                      σ n
  *Proof:* Verifies the inequality by manually checking small values of $n$. For $n \ge 5$, lower-bounds the expression and proves its derivative with respect to $\sigma^2$ is negative.

- **Lemma C.2.** When 21 < p < 12 + 21        1−     4n+2          and n is odd,

                  2p − 1  p                     np − (n + 1)/2
                  √      ≤ −(n + 1) ln(4σ 2 ) −       √        .
                   n+1                              σ n
  *Proof:* Isolates $p$ in the given sufficient condition. Applies Taylor series lower bounds to the terms $(1 - 4\sigma^2)^{-1/2}$ and $-\ln(4\sigma^2)$.

- **Lemma C.3.** When m is even and p ∈ [p̄, 1/2],
               el(m) (3/2 − p)(2σ)m                       φ(β) 1
                       √            ≥ (1 − 2el(m) σ) min{     , },
                         2πm                               β 2
                      √              p
where β = ((1/2 − p) m)/σ and p̄ = 3/4 − 1/(2el(m) ).
  *Proof:* Establishes that the left side of the inequality is decreasing on the target interval. Shows that its minimum at $p=1/2$ exceeds the analytically bounded maximum of the right side.

- **Theorem D.1.** The following inequalities relate the performance of these bounds:
                                         
            m/2          3m(1/2 − p)2
[4p(1 − p)]     ≤ exp −                   ≤ exp[−m(1 − 2p)2 /2]      if p ∈ [0, 1/4];
                        (1 + 4p)(1 − p)
                                                                 
                                                 3m(1/2 − p)2
[4p(1 − p)]m/2 ≤ exp[−m(1 − 2p)2 /2] ≤ exp −                      if p ∈ [1/4, 1/2].
                                                (1 + 4p)(1 − p)
  *Proof:* Compares the exponential arguments of the Hoeffding, Bernstein, and Chernoff bounds using simple algebraic simplification and concavity properties.

- **Lemma E.1.** Let intervals (a, b] ⊆ (c, d], integers n < m with (d−c)/m ≤ (b−a)/n,
and a function f convex and decreasing
                                     R u on (c, d] be given. Let R(f ; (t, u], v) denote
the Riemann sum approximation of t f consisting of v equal pieces, whose height
is f evaluated at their right endpoint. Then R(f ; (a, b], n) ≤ R(f ; (c, d], m).
  *Proof:* Matches each block of the coarser Riemann sum with corresponding blocks of the finer sum and leverages the convexity of $f$ to bound the resulting area differences.