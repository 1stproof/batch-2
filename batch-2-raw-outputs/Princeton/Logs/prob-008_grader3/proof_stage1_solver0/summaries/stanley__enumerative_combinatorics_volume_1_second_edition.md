<!-- Generated 2026-05-31T02:38:52 -->
<!-- Source PDF: stanley__enumerative_combinatorics_volume_1_second_edition.pdf (4628311 bytes) -->
<!-- Citation: Stanley, R. P. (2011). Enumerative Combinatorics, Volume 1 (Second Edition). Cambridge University Press. -->

# Enumerative Combinatorics, Volume 1 (Second Edition)

## Definitions
- **Definition 1.4.10.** Let w = w1 w2 · · · wn ∈ Sn . We say that the function f : [n] → N is
w-compatible if the following two conditions hold.

 (a) f (w1 ) ≥ f (w2 ) ≥ · · · ≥ f (wn )
 (b) f (wi) > f (wi+1) if wi > wi+1 (i.e., if i ∈ D(w))

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 1.1.8.** The infinite series P
                                       j≥0 Fj (x) converges if and only if
                                           lim deg Fj (x) = ∞.
  *Proof:* (no proof in this paper)

- **Proposition 1.1.9.** The infinite product Q
                                           j≥1 (1 + Gj (x)), where Gj (0) = 0, converges if
and only if limj→∞ deg Gj (x) = ∞.
  *Proof:* (no proof in this paper)

- **Proposition 1.2.1.** Let v = (a1 , . . . , ad ) ∈ Nd , and let ei denote the ith unit coordinate
vector in Zd . The number of lattice paths in Zd from the origin (0, 0, . . . , 0) to v with steps
e1 , . . . , ed is given by the multinomial coefficient aa1 1+···+a
                                                              ,...,ad
                                                                      d
                                                                        .
  *Proof:* Counts the sequence of steps to reach the target vector, reducing the problem to multiset permutations.

- **Proposition 1.3.1.** (a) The map Sn → Sn defined above is a bijection.
 (b) If w ∈ Sn has k cycles, then w
                                  b has k left-to-right maxima.
  *Proof:* Defines the fundamental bijection by inserting left parentheses before left-to-right maxima.

- **Proposition 1.3.2.** The number of permutations w ∈ SS of type (c1 , . . . , cn ) is equal to
n!/1c1 c1 !2c2 c2 ! · · · ncn cn !.
  *Proof:* Parenthesizes an arbitrary permutation into cycles of required lengths and divides by the number of equivalent disjoint cycle representations.

- **Theorem 1.3.3.** We have
                          X                                                    
                                   n              x2   x3
                              Zn x = exp t1 x + t2 + t3 + · · ·                   .             (1.26)
                          n≥0
                                                  2    3
  *Proof:* Expands the exponential generating function and compares coefficients with the enumeration from Proposition 1.3.2.

- **Lemma 1.3.6.** The numbers c(n, k) satisfy the recurrence
                  c(n, k) = (n − 1)c(n − 1, k) + c(n − 1, k − 1), n, k ≥ 1,
with the initial conditions c(n, k) = 0 if n < k or k = 0, except c(0, 0) = 1.
  *Proof:* Partitions permutations in Sn based on whether the element n forms a singleton cycle or is inserted into an existing cycle.

- **Proposition 1.3.7.** Let t be an indeterminate and fix n ≥ 0. Then
                        n
                        X
                              c(n, k)tk = t(t + 1)(t + 2) · · · (t + n − 1).            (1.28)
                        k=0
  *Proof:* Provides four proofs: using a recurrence relation, an exponential generating function, a bijection from subset-function pairs, and a sequential construction algorithm from bounded integer sequences.

- **Proposition 1.3.10.** Let n, k ∈ P. The number of integer sequences (a1 , . . . , an ) such that
0 ≤ ai ≤ n − i and exactly k values of ai equal 0 is c(n, k)
  *Proof:* (immediate from Proposition 1.3.7)

- **Corollary 1.3.11.** The number of w ∈ Sn with k left-to-right maxima is c(n, k).
  *Proof:* (immediate from Proposition 1.3.1)

- **Proposition 1.3.12.** Let

          Tn = {(a1 , . . . , an ) : 0 ≤ ai ≤ n − i} = [0, n − 1] × [0, n − 2] × · · · × [0, 0].

The map I : Sn → Tn that sends each permutation to its inversion table is a bijection.
  *Proof:* Constructs the unique permutation corresponding to a valid inversion table by sequentially inserting elements based on the table's entries.

- **Corollary 1.3.13.** Let inv(w) denote the number of inversions of the permutation w ∈ Sn .
Then          X
                  q inv(w) = (1 + q)(1 + q + q 2 ) · · · (1 + q + q 2 + · · · + q n−1). (1.30)
                 w∈Sn
  *Proof:* Rewrites the sum over permutations as an iterated sum over the independent ranges of inversion table entries.

- **Proposition 1.3.14.** For any w = w1 w2 · · · wn ∈ Sn we have inv(w) = inv(w −1).
  *Proof:* Observes that (i, j) is an inversion of w if and only if (wj, wi) is an inversion of w^{-1}.

- **Proposition 1.4.1.** Let S = {s1 , . . . , sk }< ⊆ [n − 1]. Then
                                                                           
                                                    n
                       α(S) =                                              .              (1.35)
                                  s1 , s2 − s1 , s3 − s2 , . . . , n − sk
  *Proof:* Selects the strictly increasing elements between consecutive descent positions using multinomial coefficients.

- **Proposition 1.4.3.** The number of permutations w ∈ Sd with k excedances, as well as the
number with k + 1 weak excedances, is equal to the Eulerian number A(d, k + 1).
  *Proof:* Relates weak excedances to descents using the fundamental bijection and permutation reversal.

- **Proposition 1.4.4.** For every d ≥ 0 we have
                                     X                 Ad (x)
                                           md xm =              .                              (1.37)
                                     m≥0
                                                     (1 − x)d+1
  *Proof:* Differentiates the induction hypothesis to derive a recurrence relation for Eulerian numbers, which is then verified combinatorially by considering where to insert the maximum element.

- **Proposition 1.4.5.** We have
                                X               td      1−x
                                       Ad (x)      =              .                    (1.40)
                                 d≥0
                                                d!   1 − xe(1−x)t
  *Proof:* Multiplies the generating function from Proposition 1.4.4 by t^d/d! and sums over d, simplifying the result.

- **Proposition 1.4.6.** We have
                                       X
                                              q maj(w) = (n)!.                         (1.42)
                                       w∈Sn
  *Proof:* Recursively constructs a bijection that transforms the major index into the inversion statistic by cyclically shifting compartments formed around the next inserted element.

- **Theorem 1.4.8.** Let ϕ be the bijection defined in the proof of Proposition 1.4.6. Then for
all w ∈ Sn , ID(w) = ID(ϕ(w)). In other words, ϕ preserves the inverse descent set.
  *Proof:* Shows by induction that the reading words of the elements greater than the inserted letter remain unchanged under the compartment shifts.

- **Corollary 1.4.9.** The three pairs of statistics (inv, maj), (inv, imaj), and (maj, imaj) have
symmetric joint distributions.
  *Proof:* Combines the bijection's preservation of the inverse descent set and transformation of major index to inversions with permutation reversal symmetry.

- **Lemma 1.4.11.** Given f : [n] → N, there is a unique permutation w ∈ Sn for which f is
w-compatible.
  *Proof:* Groups elements into an ordered partition of sets on which the function is constant, then orders each set increasingly.

- **Lemma 1.4.12.** (a) For w ∈ Sd and m ≥ 0 we have
                                                                
                           m + d − 1 − des(w)      m − des(w)
              #Am (w) =                        =                                               (1.45)
                                   d                   d
and
                                  X                               x1+des(w)
                                         #Am (w) · xm =                     .                  (1.46)
                                 m≥1
                                                                 (1 − x)d+1
                                               
(If 0 ≤ m < des(w), then we set m−des(w)d
                                                = 0.)
                                P
(b) For f : [n] → N write |f | = ni=1 f (i). Then for w ∈ Sn we have
                              X                             q maj(w)
                                       q |f | =                                      .         (1.47)
                                                  (1 − q)(1 − q 2 ) · · · (1 − q n )
                             f ∈A(w)
  *Proof:* Converts strictly decreasing conditions to weakly decreasing sequences by subtracting the number of rightward descents, then counts the results.

- **Proposition 1.5.1.** Let S132 (n) denote the set of 132-avoiding w ∈ Sn . Then
                                  X                X
                                        q inv(w) =   q |λ| ,
                                    w∈S132 (n)            λ


     λ ranges over all integer sequences λ1 ≥ · · · ≥ λn ≥ 0 satisfying λi ≤ n − i, and where
whereP
|λ| = λi .
  *Proof:* Characterizes 132-avoiding permutations as having Ferrers diagrams bounded by n-i in the ith row.

- **Proposition 1.5.3.** (a) The number of increasing binary trees with n vertices is n!.

 (b) The number of such trees for which exactly k vertices have left successors is the Eulerian
     number A(n, k + 1).

 (c) The number of complete (i.e., every vertex is either an endpoint or has two successors)
     increasing binary trees with 2n + 1 vertices is equal to the number E2n+1 of alternating
     permutations in S2n+1 .
  *Proof:* Maps elements of a permutation to tree vertices and deduces the structural properties via the increasing binary tree bijection.

- **Proposition 1.5.5.** (a) The number of unordered increasing trees on n + 1 vertices is n!.

 (b) The number of such trees for which the root has k successors is the signless Stirling
     number c(n, k).

 (c) The number of such trees with k endpoints is the Eulerian number A(n, k).
  *Proof:* Deduces the properties from the unordered increasing tree bijection by identifying root successors as left-to-right minima and endpoints as descents.

- **Proposition 1.6.1.** We have
     X xn
         En    = sec x + tan x
     n≥0
            n!
                              x2    x3  x4   x5   x6    x7     x8
                 = 1+x+          + 2 + 5 + 16 + 61 + 272 + 1385 + · · · .
                              2!    3!  4!   5!   6!    7!     8!
  *Proof:* Splits a chosen subset to form alternating and reverse alternating permutations, yielding a differential equation solved by secant and tangent.

- **Proposition 1.6.2.** We have f (n) = En (an Euler number).
  *Proof:* Derives a differential equation by decomposing increasing (1,2)-trees at the root, matching the Euler number generating function.

- **Theorem 1.6.3.** The ab-index Ψn can be written as a polynomial Φn in the variables c = a+b
and d = ab + ba. This polynomial is a sum of En monomials.
  *Proof:* Groups the ab-index terms by M-equivalence classes, each containing exactly one alternating permutation and yielding a valid cd-polynomial.

- **Proposition 1.6.4.** Let S, T ⊆ [n − 1]. If ω(S) ⊂ ω(T ), then βn (S) < βn (T ).
  *Proof:* Evaluates the positive cd-index coefficients and constructs a distinguishing word to demonstrate strict inequality.

- **Corollary 1.6.5.** Let S ⊆ [n − 1]. Then βn (S) ≤ En , with equality if and only if S =
{1, 3, 5, . . . } ∩ [n − 1] or S = {2, 4, 6, . . . } ∩ [n − 1].
  *Proof:* (immediate from Proposition 1.6.4)

- **Proposition 1.7.1.** Let M = {1a1 , . . . , mam } be a multiset of cardinality n = a1 + · · · + am .
Then                                                              
                            X                           n
                                     inv(w)
                                  q         =                     .                         (1.68)
                           w∈S
                                                 a1 , . . . , a m
                                      M
  *Proof:* Provides a proof using recurrences for the inversion polynomial, and a second proof standardizing multiset permutations to set permutations to apply the known symmetric group identity.

- **Proposition 1.7.2.** The number of k-dimensional subspaces of Fnq is n    k
                                                                            .
  *Proof:* Equates two methods of counting linearly independent k-tuples of vectors to isolate the number of k-dimensional subspaces.

- **Proposition 1.7.3.** Fix j, k ∈ N. Then
                                    X                            
                                                      n     j+k
                                          p(j, k, n)q =                 .
                                    n≥0
                                                                 j
  *Proof:* Establishes a bijection between partitions fitting in a box and row-reduced echelon matrices over finite fields.

- **Proposition 1.8.1.** For each i ∈ P, fix a set Si ⊆ N. Let S = (S1 , S2 , . . . ), and define P (S)
to be the set of all partitions λ such that if the part i occurs mi = mi (λ) times, then mi ∈ Si .
Define the generating function in the variables q = (q1 , q2 , . . . ),
                                             X m (λ) m (λ)
                                 F (S, q) =        q1 1 q2 2 · · · .
                                            λ∈P (S)


Then                                                                      !
                                                 Y X j
                                      F (S, q) =    qi                        .                 (1.78)
                                                    i≥1    j∈Si
  *Proof:* Directly forms the generating function by making independent term selections for each part multiplicity from the allowed sets.

- **Corollary 1.8.2.** Preserve the notation of the previous proposition, and let p(S, n) denote
the number of partitions of n belonging to P (S), that is,

                                   p(S, n) = #{λ ⊢ n : λ ∈ P (S)}.

Then                                                                              !
                                   X                     Y X
                                          p(S, n)q n =                    q ij        .
                                    n≥0                  i≥1       j∈Si
  *Proof:* (immediate from Proposition 1.8.1)

- **Proposition 1.8.3.** For any partition λ = (λ1 , λ2 , . . . ) we have
                              X                X  λ′  
                                                           i
                                   (i − 1)λi =               .                                  (1.79)
                               i≥1              i≥1
                                                          2
  *Proof:* Sums the row index minus one across all squares of the Young diagram by rows and by columns to establish the equality.

- **Proposition 1.8.4.** Let c(n) denote the number of self-conjugate partitions λ of n, i.e.,
λ = λ′ . Then          X
                          c(n)q n = (1 + q)(1 + q 3 )(1 + q 5 ) · · · .          (1.80)
                             n≥0
  *Proof:* Maps the diagonal hooks of the Ferrers diagram of a self-conjugate partition to a partition of n into distinct odd parts.

- **Proposition 1.8.5.** Let q(n) denote the number of partitions of n into distinct parts and
podd (n) the number of partitions of n into odd parts. Then q(n) = podd (n) for all n ≥ 0.
  *Proof:* Provides three proofs: manipulating infinite product generating functions, a binary expansion bijection for multiplicities, and a diagram-cutting bijection using shifted hooks.

- **Proposition 1.8.6.**        (a) We have

                                   1         X             xk q k
                               Y           =                 2              k
                                                                               .                        (1.82)
                                (1 − xq i ) k≥0 (1 − q)(1 − q ) · · · (1 − q )
                               i≥1


 (b) We have

                           1                 X                         xk q k
                                                                               2

                   Y                     =                            k )(1 − xq) · · · (1 − xq k )
                                                                                                    .
                         (1 − xq i )         k≥0
                                                 (1 − q) · · · (1 − q
                   i≥1


 (c) We have
                                                                             k+1
                               Y              X                    xk q ( 2 )
                                (1 + xq i ) =                                                .          (1.83)
                               i≥1                    k≥0
                                                          (1 − q)(1 − q 2 ) · · · (1 − q k )
  *Proof:* Bijectively relates the terms of the products to partitions by analyzing the length of the partition, the rank and Durfee square size, and the length of a partition with distinct parts.

- **Proposition 1.8.7.** We have
          Y              X
             (1 − xk ) =   (−1)n xn(3n−1)/2                                                 (1.88)
            k≥1                n∈Z
                                     X                                      
                          = 1+             (−1)n xn(3n−1)/2 + xn(3n+1)/2                    (1.89)
                                     n≥1

                          = 1 − x − x2 + x5 + x7 − x12 − x15 + x22 + x26 − · · · .
  *Proof:* Defines a sign-reversing involution on the Ferrers diagrams of partitions into distinct parts by moving dots between the last row and a diagonal set, identifying the two exceptional un-pairable shapes.