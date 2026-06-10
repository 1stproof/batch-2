<!-- Generated 2026-05-31T02:10:05 -->
<!-- Source PDF: haglund__ordered_set_partitions_generalized_coinvariant_alg.pdf (601320 bytes) -->
<!-- Citation: J. Haglund, B. Rhoades, M. Shimozono (2018). Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture. Advances in Mathematics. -->

```markdown
# Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture (Haglund, Rhoades, & Shimozono, 2018)

## Definitions
- **Definition 1.1.** Given two positive integers k ≤ n, let In,k ⊆ Q[xn ] be the ideal In,k := hxk1 , xk2 , . . . , xkn , en (xn ), en−1 (xn ), . . . , en−k+1 (xn )i. Let Rn,k be the corresponding quotient ring: Rn,k := Q[xn ] / In,k .
- **Definition 3.2.** Let S = {s1 < · · · < sm } ⊆ [n] be a set. (1) The skip monomial x(S) ∈ Q[xn ] is the monomial x(S) := xss11 xss22 −1 · · · xssm m −m+1 . (2) The skip composition γ(S) = (γ1 , . . . , γn ) is the weak composition of length n defined by γi := 0 i∈/S sj − j + 1 i = sj ∈ S.
- **Definition 4.1.** Fix distinct rational numbers α1 , . . . , αk ∈ Q. Let Yn,k ⊂ Qn be the set of points with coordinates occurring in {α1 , . . . , αk } such that each αi appears at least once. In other words, Yn,k := {(y1 , . . . , yn ) ∈ Qn : {α1 , . . . , αk } = {y1 , . . . , yn }}.
- **Definition 4.4.** Let k ≤ n. A monomial m ∈ Q[xn ] is (n, k)-nonskip if (1) x(S) - m for all S ⊆ [n] with |S| = n − k + 1 and (2) xki - m for all 1 ≤ i ≤ n. Let Mn,k denote the set of all (n, k)-nonskip monomials in Q[xn ].
- **Definition 4.12.** The (n, k)-Artin monomials An,k are those monomials in Q[xn ] whose exponent vectors fit under at least one (n, k)-staircase.
- **Definition 5.2.** Let k ≤ n be positive integers. The (n, k)-Garsia-Stanton monomials GS n,k are given by GS n,k := {gsπ ·xiπ11 xiπ22 · · · xπn−k n−k : π ∈ Sn , des(π) < k, and (k−des(π)) > i1 ≥ i2 ≥ · · · ≥ in−k ≥ 0}.
- **Definition 6.1.** Let s ≤ k ≤ n be positive integers. Define In,k,s ⊆ Q[xn ] to be the ideal In,k,s := hxk1 , xk2 , . . . , xkn , en (xn ), en−1 (xn ), . . . , en−s+1 (xn )i. Let Rn,k,s := Q[xn ] / In,k,s be the corresponding quotient ring.
- **Definition 6.2.** Let Yn,k,s ⊆ Qn+k−s be the set of points (y1 , . . . , yn , yn+1 , . . . , yn+k−s ) such that • {y1 , . . . , yn , yn+1 , . . . , yn+k−s } = {α1 , . . . , αk }, and • yn+i = αs+i for all 1 ≤ i ≤ k − s.

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 3.1.** Let k ≤ n, let α1 , . . . , αk ∈ Q be distinct rational numbers, and let β1 , . . . , βn ∈ Q be rational numbers with the property that {β1 , . . . , βn } = {α1 , . . . , αk }. For any n − k + 1 ≤ r ≤ n we have Xr j=0 (−1)j er−j (β1 , . . . , βn )hj (α1 , . . . , αk ) = 0.
  *Proof:* Calculates the coefficient of $t^r$ in a rational function whose denominator perfectly cancels with the numerator.
- **Theorem 3.3.** [14, Thm. 6.1, λ = (1d )] Let γ = (γ1 , . . . , γn ) be a weak composition and d ≥ 0. We have ed (xn )κγ (xn ) = X |ρ|=d κ(γ∪ρ) (xn ), where the sum is over all RB collections of cells ρ of size d.
  *Proof:* (no proof in this paper)
- **Lemma 3.4.** Let k ≤ n and let S ⊆ [n] with |S| = n − k + 1. Let γ(S) be the corresponding skip monomial and consider the reversal γ(S)∗ and the decremented reversal γ(S)∗ . We have the identity κγ(S)∗ (xn ) = X λ (−1)|λ| κγ(S)∗ −λ (xn )en−k+1+|λ| (xn ), where the sum is over all LL collections λ for γ. Reversing variables and applying the symmetry of er (xn ) we get κγ(S)∗ (x∗n ) = X λ (−1)|λ| κγ(S)∗ −λ (x∗n )en−k+1+|λ| (xn ).
  *Proof:* Defines a sign-reversing involution on the set of combinatorial objects called "partisan skylines" to verify the identity. Maps non-frozen columns by toggling labels between top-justified and right-justified collections while preserving column heights and avoiding totally frozen skylines.
- **Lemma 3.5.** Let k ≤ n and let S ⊆ [n] satisfy |S| = n − k + 1. Let < be lexicographic order. We have in< (κγ(S)∗ (x∗n )) = x(S). Moreover, for any 1 ≤ i ≤ n we have max(S)−n+k+1 xi - m for any monomial m appearing in κγ(S)∗ (x∗n ). Finally, if T ⊆ [n] satisfies |T | = n − k + 1 and T 6= S, then x(S) - m for any monomial m appearing in κγ(T )∗ (x∗n ).
  *Proof:* Analyzes the unique lexicographically largest reverse content vector among semistandard skyline fillings.
- **Lemma 3.6.** Let F (x), G(x) ∈ Λ be symmetric functions with equal constant terms. We have F (x) = G(x) if and only if ej (x)⊥ F (x) = ej (x)⊥ G(x) for all j ≥ 1.
  *Proof:* Relies on the self-adjointness of the Hall inner product applied to combinations of elementary symmetric functions.
- **Lemma 3.7.** We have ej (x)⊥ Dn,k (x; q) = q ( j 2 ) k j q X m=max(1,k−j) min(k,n−j) q (k−m)·(n−j−m) j k−m q Dn−j,m (x; q).
  *Proof:* Expresses the scalar product combinatorially via shuffles of reverse reading words and counts coinversions amongst partitioned elements.
- **Lemma 4.2.** We have In,k ⊆ T(Yn,k ).
  *Proof:* Extracts the top degree components of polynomials proven to structurally vanish on $Y_{n,k}$ by Lemma 3.1.
- **Lemma 4.3.** Let k ≤ n. For any S ⊆ [n] of size |S| = n − k + 1, the reverse Demazure character κγ(S)∗ (x∗n ) satisfies κγ(S)∗ (x∗n ) ∈ In,k . In particular, we have x(S) ∈ in< (In,k ). Moreover, for 1 ≤ i ≤ n we have xki ∈ in< (In,k ).
  *Proof:* Takes the lexicographic leading term of the reverse Demazure character identity established in Lemma 3.4.
- **Lemma 4.5.** Let m ∈ Q[xn ] be a monomial and let S, T ⊆ [n]. If x(S) | m and x(T ) | m, then x(S ∪ T ) | m.
  *Proof:* Compares the exponent of each variable in the individual skip monomials to show limits are maintained upon taking the set union.
- **Lemma 4.6.** Let m ∈ Q[xn ] be a monomial and let r be a positive integer such that x(S) | m for some S ⊆ [n] with |S| = r but there does not exist T ⊆ [n] with |T | > r such that x(T ) | m. Then there exists a unique S ⊆ [n] with |S| = r such that x(S) | m.
  *Proof:* Applies Lemma 4.5 to show that two distinct valid subsets would naturally generate a larger skip monomial constraint.
- **Lemma 4.7.** Let k ≤ n and let m ∈ Mn,k . There exists a unique set S ⊆ [n] with |S| = n − k such that (1) x(S) | (m(S) · m), and (2) x(U ) - (m(S) · m) for all U ⊆ [n] with |U | = n − k + 1.
  *Proof:* Proves uniqueness by contradiction using the properties of skip subsets and existence by selecting the lexicographically final available set.
- **Lemma 4.8.** The above procedure gives a well-defined function Ψ : OP n,k → Mn,k .
  *Proof:* Verifies recursively that the monomial output does not contain any $n-k+1$ skips and thus correctly remains within $M_{n,k}$.
- **Theorem 4.9.** The function Ψ : OP n,k → Mn,k is a bijection with the property that coinv(σ) = deg(Ψ(σ)) for all σ ∈ OP n,k . In particular, we have Pn,k (q) = Mn,k (q) and |OP n,k | = |Mn,k |.
  *Proof:* Recursively constructs an inverse map $\Phi: M_{n,k} \to OP_{n,k}$ by branching on whether removing the highest-indexed variable requires factoring out a unique skip monomial. The degrees of the monomials are shown to exactly match the coinversion statistics on the corresponding ordered set partitions.
- **Theorem 4.10.** Let k ≤ n be positive integers. The Hilbert series Hilb(Rn,k ; q) of the graded vector space Rn,k is the generating function for coinv on OP n,k : Hilb(Rn,k ; q) = Pn,k (q) = revq ([k]!q · Stirq (n, k). In particular, we have dim(Rn,k ) = |OP n,k | = k! · Stir(n, k).
  *Proof:* Computes standard monomial bases from the lexicographic Gröbner bases, relying on the equality of dimensions between $OP_{n,k}$ and $M_{n,k}$.
- **Theorem 4.11.** Let k ≤ n be positive integers. As ungraded Sn -modules, we have Rn,k ∼=S n Q[OP n,k ]. Equivalently, we have the ungraded Frobenius character Frob(Rn,k ) = X λ`n `(λ)=k k m1 (λ), . . . , mk (λ) hλ (x),
  *Proof:* Follows directly from the established $\mathbb{S}_n$-isomorphism between the top component ideal quotient and the group algebra over ordered set partitions.
- **Theorem 4.13.** Let k ≤ n be positive integers. We have An,k = Mn,k . Moreover, the set An,k descends to a monomial basis of Rn,k .
  *Proof:* Inductively verifies that the image of the bijection $\Psi$ on $OP_{n,k}$ falls strictly within the exponent bounds defining $(n,k)$-staircases.
- **Theorem 4.14.** Let k ≤ n be positive integers and let < be the lexicographic monomial order. A Gröbner basis for In,k with respect to < is given by the variable powers xk1 , xk2 , . . . , xkn together with the reverse Demazure characters κγ(S)∗ (x∗n ) for S ⊆ [n − 1] satisfying |S| = n − k + 1. If k < n, this Gröbner basis is the reduced Gröbner basis for In,k with respect to <.
  *Proof:* Compares the number of non-divisible monomials in $\mathbb{Q}[\mathbf{x}_n]$ against the established quotient ring dimension to deduce the Gröbner basis.
- **Lemma 5.1.** We have X σ∈OP n,k q comaj(σ) = X π∈Sn q maj(π) · asc(π) n−k q .
  *Proof:* Equates the statistic by grouping ordered set partitions as ascent-starred permutations and generating the choices for sets of stars.
- **Theorem 5.3.** Let k ≤ n be positive integers. The set GS n,k of (n, k)-Garsia-Stanton monomials descends to a basis for Rn,k .
  *Proof:* Leverages Adin, Brenti, and Roichman's straightening algorithm on permutations to rewrite arbitrary monomials modulo the ideal $I_{n,k}$. Inductively reduces the coset representation into the span of the proposed Garsia-Stanton basis using the Stanley-Reisner theory of permutations.
- **Lemma 6.3.** Let s ≤ k ≤ n. We have In,k,s ⊆ Tn,k,s .
  *Proof:* Evaluates the top components of polynomials structurally vanishing on the extended point set $Y_{n,k,s}$.
- **Lemma 6.4.** Suppose S ⊆ [n] satisfies |S| = n − s + 1. The reverse Demazure character κγ(S)∗ (x∗n ) lies in In,k,s .
  *Proof:* (immediate from Lemma 3.4)
- **Lemma 6.5.** Let s ≤ k ≤ n. If xa11 · · · xann xan+1 n+1 · · · xan+k−s n+k−s ∈ Mn+k−s,k , then xa11 · · · xann ∈ Mn,k,s . On the other hand, if xa11 · · · xann ∈ Mn,k,s and 0 ≤ an+1 < an+2 < · · · < an+k−s ≤ k − 1, then xa11 · · · xann xan+1 n+1 · · · xan+k−s n+k−s ∈ Mn+k−s,k .
  *Proof:* Checks that the variable exponents consistently conform to the skip composition constraints when extending or restricting polynomial variables.
- **Lemma 6.6.** For any s ≤ k ≤ n we have |Mn,k,s | = |OP n,k,s |.
  *Proof:* Tracks the image of $OP_{n,k,s}$ under the bijection $\Psi$ via the subsets of restricted monomials.
- **Lemma 6.7.** Let s ≤ k ≤ n. A Gröbner basis for the ideal In,k,s with respect to <lex consists of the variable powers xk1 , . . . , xkn together with the reverse Demazure characters {κγ(S)∗ (x∗n ) : S ⊆ [n], |S| = n − s + 1}. If s < k, this is the reduced Gröbner basis for this term ordering. In particular, we have dim(Rn,k,s ) = |OP n,k,s |.
  *Proof:* Confirms that the dimensions of the specific point set and the bounding non-skip monomials correspond exactly to establish the Gröbner basis.
- **Lemma 6.8.** As graded Sn−j -modules we have  j Rn,k ∼= Rn−j,k,k−j ⊗ An,k,j .
  *Proof:* Constructs a multiplication map preserving the parabolic action of $\mathbb{S}_{n-j}$ to embed the module. Determines the kernel by leveraging elementary symmetric functions, and establishes full surjectivity through a precise dimension count matching the alternant basis.
- **Lemma 6.9.** Let s < k ≤ n. There is a short exact sequence 0 → Rn,k−1,s → Rn,k,s → Rn,k,s+1 → 0 of Sn -modules, where the first map is homogeneous of degree n − s and the second map is homogeneous of degree 0. Equivalently, we have grFrob(Rn,k,s ; q) = grFrob(Rn,k,s+1 ; q) + q n−s · grFrob(Rn,k−1,s ; q).
  *Proof:* Employs the canonical projection for the second map, and constructs the first homogeneous map via multiplication by an elementary symmetric function. Proves the sequence's exactness algebraically by matching the dimension counts of ordered set partitions ending in singletons.
- **Lemma 6.10.** Let 1 ≤ j ≤ n. We have grFrob(Rn−j,k,k−j ; q) = X m=max(1,k−j) min(k,n−j) q (k−m)·(n−j−m) j k−m q grFrob(Rn−j,m ; q).
  *Proof:* Re-indexes the variables to recursively express the graded Frobenius characters via the exact sequence from Lemma 6.9. Evaluates the resulting expression using the $q$-analog of Pascal's triangle recursion.
- **Theorem 6.11.** The graded Frobenius character of the module Rn,k is given by grFrob(Rn,k ; q) = Dn,k (x; q).
  *Proof:* Inducts on the evaluations of both symmetric functions under the adjoint operators $e_j(x)^\perp$ using Lemma 3.6.
- **Corollary 6.12.** The graded Frobenius character grFrob(Rn,k ) is equal to any of the following four expressions, after applying revq and ω: X |γ|=n X µ∈OP γ,k q inv(µ) xγ = X |γ|=n X µ∈OP γ,k q maj(µ) xγ = X |γ|=n X µ∈OP γ,k q dinv(µ) xγ = X |γ|=n X µ∈OP γ,k q minimaj(µ) xγ .
  *Proof:* (immediate from Theorem 6.11)
- **Corollary 6.13.** We have grFrob(Rn,k ; q) = revq   X T ∈SYT(n) q maj(T )+( n−k 2 )−(n−k)·des(T ) des(T ) n − k q s shape(T ) 0 (x)  .
  *Proof:* (no proof in this paper)
- **Theorem 6.14.** We have grFrob(Rn,k ; q) = revq    X λ`n `(λ)=k q P i (i−1)·(λi −1) k m1 (λ), . . . , mk (λ) q Q0λ (x; q)  .
  *Proof:* Links the evaluated Delta conjecture with balanced labeled Dyck paths and computes the sum over all path labellings using symmetric function expansions in dual Hall-Littlewood polynomials.
```