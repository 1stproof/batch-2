<!-- Generated 2026-05-31T02:36:21 -->
<!-- Source PDF: ardila__the_bergman_complex_of_a_matroid_and_phylogenetic.pdf (191247 bytes) -->
<!-- Citation: Ardila, F., and Klivans, C. J. (2006). The Bergman complex of a matroid and phylogenetic trees. Journal of Combinatorial Theory, Series B. -->

# The Bergman complex of a matroid and phylogenetic trees (Ardila and Klivans, 2006)

## Definitions
- **Definition.** Given ! ∈ Rn , let F(!) denote the unique flag of subsets

      ∅ =: F0 ⊂ F1 ⊂ · · · ⊂ Fk ⊂ Fk+1 := [n]

  for which ! is constant on each set Fi − Fi−1 and has !|Fi −Fi−1 < !|Fi+1 −Fi . The weight class of a flag F is the set of vectors ! such that F(!) = F.
- **Definition.** The Bergman fan of a matroid M with ground set [n] is the set
      !
      B(M) := {! ∈ Rn : M! has no loops}.
  The Bergman complex of M is
      B(M) := {! ∈ S n−2 : M! has no loops},
  where S n−2 is the sphere { ! ∈ Rn : !1 + · · · + !n = 0 , !21 + · · · + !2n = 1}.
- **Definition.** The weight class of a flag F is valid for M if MF has no loops.
- **Definition.** The fine subdivision of B(M) is the subdivision of B(M) into valid weight classes: two vectors u and v of B(M) are in the same class if and only if F(u) = F(v).
   The coarse subdivision of B(M) is the subdivision of B(M) into M! -equivalence classes: two vectors u and v of B(M) are in the same class if and only if Mu = Mv .
- **Definition.** A dissimilarity map on [n] is a map # : [n] × [n] → R such that #(i, i) = 0 for all i ∈ [n], and #(i, j ) = #(j, i) for all i, j ∈ [n].
- **Definition.** A dissimilarity map is an ultrametric if, for all i, j, k ∈ [n], two of the values #(i, j ), #(j, k) and #(i, k) are equal and not less than the third.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem ([6, Theorem 1.11.1]).** Let S be a collection of r-subsets of [n]. Let PS be the polytope in Rn with vertex set {eb1 + · · · + ebr | {b1 , . . . , br } ∈ S}, where ei is the ith unit vector. Then S is the collection of bases of a matroid if and only if every edge of PS is a translate of the vector ei − ej for some i, j ∈ [n].
  *Proof:* (no proof in this paper)

- **Proposition 1.** If ! is in the weight class of F = {∅ =: F0 ⊂ · · · ⊂ Fk+1 := [n]}, then the !-minimum bases of M are exactly those containing r(Fi ) − r(Fi−1 ) elements of Fi − Fi−1 , for each i. Consequently, M! depends only on F, and we call it MF .
  *Proof:* Simulates the greedy algorithm to show that bases are constructed by sequentially choosing elements from successive subsets in the flag.

- **Proposition 2.** If F = {∅ =: F0 ⊂ · · · ⊂ Fk+1 := [n]}, then
              k+1
              "                                          k+1
                                                         #
      MF =           (M|Fi )/Fi−1       and    LMF !            [Fi−1 , Fi ].
               i=1                                        i=1
  *Proof:* Analyzes the greedy algorithm's choices on the flag's subsets to identify the resulting minimum bases as the direct sum of minors.

- **Theorem 1.** The weight class of a flag F is valid for M if and only if F is a flag of flats of M. Therefore, the fine subdivision of the Bergman complex B(M) is a geometric realization of "(LM − { 0̂ , 1̂ }), the order complex of the proper part of the lattice of flats of M.
  *Proof:* Evaluates loop formation in the matroid, proving a loop exists if and only if a subset in the flag contains a dependent element outside its closure.

- **Corollary.** The Bergman complex B(M) is homotopy equivalent to a wedge of $             "(LM ) (r−2)-dimensional spheres. Its subdivision into weight classes is a pure, shellable simplicial complex.
  *Proof:* (immediate from Theorem 1)

- **Theorem 2.** Suppose that the weight classes of two maximal flags F are F ' are adjacent. Say F and F ' only differ in rank i; that is, F − Fi = F ' − Fi' . Then the following conditions are equivalent:
  (i) MF = MF ' ,
 (ii) MF = MF −Fi ,
(iii) Fi ∪ Fi' = Fi+1 ,
(iv) The interval [Fi−1 , Fi+1 ] of LM is a diamond poset.
  *Proof:* Computes the lattice of flats for the differing sub-matroids, confirming they match if and only if the bounding interval is a diamond poset.

- **Theorem ([12, Theorem 7.2.5]).** A map # : [n] × [n] → R is an ultrametric if and only if it is the distance function of an equidistant n-tree.
  *Proof:* (no proof in this paper)

- **Theorem 3.** A dissimilarity map # : [n] × [n] → R is an ultrametric if and only if the corresponding weight vector on the edges of Kn is in the Bergman fan B(K      ! n ).
  *Proof:* Establishes cyclic equivalences between ultrametric conditions and spanning tree minimality by analyzing maximum edge weights in triangles and cycles.

- **Proposition 3.** The map f : Tn × R → B(K    ! n ) is a piecewise linear homeomorphism. It identifies the decomposition of the space of trees Tn into combinatorial tree types with the coarse decomposition of the Bergman fan B(K! n ).
  *Proof:* Constructs a piecewise linear mapping from tree parameters to leaf distances, matching tree combinatorial types to matroid equivalence classes using a cycle-breaking algorithm.

- **Corollary.** The order complex of the proper part of the partition lattice !n is a subdivision of the complex Tn .
  *Proof:* (immediate from Theorem 1)