<!-- Generated 2026-05-31T02:11:47 -->
<!-- Source PDF: macdonald__symmetric_functions_and_hall_polynomials_2nd_editi.pdf (6276911 bytes) -->
<!-- Citation: I. G. Macdonald (1995). Symmetric Functions and Hall Polynomials (2nd Edition). Oxford University Press. -->

# Symmetric Functions and Hall Polynomials (2nd Edition), I. G. Macdonald (1995)

## Definitions

## Lemmas, Theorems, Propositions, Corollaries
- **(1.7).** Let A be a partition and let m > A n > A,. Then the m + n numbers

          Ai+n-i (1<i<n),                  n-1+j-Aj (1<j<m)
are a permutation of (0, 1, 2,..., m + n - 1).
  *Proof:* Traces boundaries of the partition diagram to establish a bijection of index lengths.

- **(1.8).**                                (AUtk)'=A'+
                               (A X µ)' = A'µ'.
  *Proof:* Evaluates conjugate operations by directly counting nodes in the reassembled columns of the partition diagrams.

- **(1.9).** Let k, µ E.9',,. Then

                     (A, µ)EL',, (A',A')EL,,.
  *Proof:* Compares the first differing index to demonstrate that lexicographical dominance reverses under conjugation.

- **(1.10).** Let A, µ E-cP,,. Then
                               A> 1- L   (.A, µ) E Ln n En .
  *Proof:* Examines the cumulative sums of the partitions to establish strict lexicographic ordering.

- **(1.11).** Let A, µ E.pn. Then
                               A>µpµ'>A'.
  *Proof:* Sums nodes right of columns to bound partial row sums, equating sequence dominances.

- **(1.12).** Let a E Z". Then
                         aEP"pa>wa for all wES".
  *Proof:* Assesses permutation operations cumulatively to verify the components are in descending order.

- **(1.13).** Let a E Pn. Then for each w E Sn we have (a + S - wS)+> a.
  *Proof:* Extends the fundamental domain permutation inequality transitively to the shifted parameters.

- **(1.14).** Let a E Z" and let R be a raising operator. Then
                                            Ra>a.
  *Proof:* Reduces to a single adjacent raising operator where the coordinate inequality is immediate.

- **(1.15).** Let a, b E Z" be such that a < b and al + ... +an = bl + ... +b, .
Then there exists a raising operator R such that b = Ra.
  *Proof:* Constructs a sequential product of raising operators from cumulative coordinate differences.

- **(1.16).** If A, µ are partitions of n such that A > µ, and if A, µ are adjacent for
the natural ordering (so that A > v > µ implies either v = A or v = µ), then
A = Rij µ for some i <j.
  *Proof:* Identifies the first differing element to match adjacent ordered partitions via a single raising operator step.

- **(2.3).** Let A be a partition, A' its conjugate. Then

                              eA' = MA + E aAµmµ


where the aAµ are non-negative integers, and the sum is over partitions µ < A
in the natural ordering.
  *Proof:* Places indices down the diagram's columns to upper bound the row sums against the partition.

- **(2.4).** We have
                                  A = Z[e1, e2,...]
and the e, are algebraically independent over Z.
  *Proof:* Translates basis expansions to show any symmetric function is uniquely polynomial in elementary ones.

- **(2.7).** w is an involution, i.e. w2 is the identity map.
  *Proof:* Relies on the perfect symmetry of the relations between complete and elementary symmetric functions.

- **(2.8).** We have
                                 A = Z[hl,h2,...]
and the h,. are algebraically independent over Z.
  *Proof:* Transfers algebraic independence from the elementary basis using the established symmetric involution.

- **(2.12).** We have

                           AQ=A(&z Q=Q[Pl,P2,...]
and the pr are algebraically independent over Q.
  *Proof:* Relies on Newton's formulas to establish a polynomial basis equivalence over the rationals.

- **(3.2).** The Schur functions sA(xl, .... xn), where 1(,1) < n, form a Z-basis
of An.
  *Proof:* Uses multiplication by the Vandermonde determinant to define an isomorphism from skew-symmetric polynomials.

- **(3.3).** The sA form a Z-basis of A, and for each k > 0 the sA such that IAI = k
form a Z-basis of Ak.
  *Proof:* Projects the finite mappings to an inverse limit extending the basis to infinite variables.

- **(3.6).** For any a = (a1, ... , an) E Nn, let
                       Aa = (x70,         Ha = (ha;-n+j)
(n x n matrices). Then Aa = Ha M.
  *Proof:* Equates the coefficients of generating polynomials to the corresponding symmetric matrix products.

- **(4.6).** For each n > 0, let (uA), (VA) be Q-bases of AQ, indexed by the
partitions of n. Then the following conditions are equivalent:
(a) (uA, vµ) = SAµ for all A, µ;
(b) EA uA(x)vA(y) = IIi.i(1-xiy;)-1.
  *Proof:* Compares polynomial coefficients directly via the established dual basis relations.

- **(4.9).** The bilinear form <u, v) is symmetric and positive definite.
  *Proof:* (immediate from (4.8))

- **(4.10).** The involution w is an isometry, i. e. < w u, w v) _ (u, v ).
  *Proof:* Evaluates the involution on power sum bases which differ only by a sign.

- **(5.7).** The skew Schur function sa/µ is zero unless d 3 µ, in which case it
depends only on the skew diagram A - A. If 0. are the components (§1) of
A-µ, we have sa/µ= II se,.
  *Proof:* Observes the determinant matrix's block triangular structure which forces it to vanish or factorize based on diagram overlaps.

- **(5.8).** We have sa/µ(xt, ... , xn) = 0 unless 0 < Xi - µ, < n for all i > 1.
  *Proof:* Confirms that rectangular blocks of zeros in the determinant force the entire matrix to evaluate to zero.

- **(5.10).** SA/µ(X, Y) _ ESA/y(X)SV/µ(y)
                                                 V


summed over partitions v such that A D v J A.
  *Proof:* Equates terms algebraically by expanding scalar product coefficients over three independent sets of variables.

- **(5.12).** SA/, =         xT
                                           T

summed over all tableaux T of shape A - µ.
  *Proof:* Translates single variable evaluations of skew Schur functions directly into monomial sums over valid tableaux.

- **(5.16).** (Pieri's formula)      sµh, _          sA
                                           A


summed over all partitions A such that A - µ is a horizontal r-strip.
  *Proof:* Evaluates tableau weights explicitly to derive the horizontal sum relations.

- **(5.17).** S,. e, _ E sA
                                           A


summed over all partitions A such that A - µ is a vertical r-strip.
  *Proof:* Filters valid diagram structures directly from determinant generating polynomials to isolate vertical strips.