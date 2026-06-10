<!-- Generated 2026-05-31T02:38:01 -->
<!-- Source PDF: speyer__tropical_linear_spaces.pdf (362553 bytes) -->
<!-- Citation: Speyer, D. E. (2008). Tropical Linear Spaces. Mathematische Zeitschrift / Selecta Mathematica. -->

```markdown
# Tropical Linear Spaces (Speyer, D. E. 2008)

## Definitions

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.2.** Every constructible space achieves the f -vector of the f -vector conjecture.
  *Proof:* Inducts simultaneously on the target space dimension and the number of sequence construction steps. Perturbs the intersection generically to evaluate nice pairs of subsets and resolves the counts via combinatorial summation identities.
- **Theorem 1.3.** Every constructible space is series-parallel.
  *Proof:* Shows that if two series-parallel tropical linear spaces meet transversely, their intersection decomposes into connected components of transverse matroids which remain series-parallel.
- **Proposition 2.2.** The following are equivalent: 1. pi1 ...id are tropical Plücker coordinates 2. The one skeleta of D and ∆(d, n) are the same. 3. Every face of D is matroidal.
  *Proof:* Uses induction to show edge lengths are 1 ruling out larger steps, leverages the Gelfand-Goresky-MacPherson-Serganova theorem for matroidal verification, and identities Plücker relations locally.
- **Proposition 2.3.** w ∈ L(p) if and only if Mw is loop-free.
  *Proof:* Shifts coordinates to assume zero minimal weight, tracking when elements act as loops in deformed matroids. Employs direct sum decompositions and parallel connections across limits to ensure structural consistency.
- **Proposition 2.4.** linkM ∨ (L) is homeomorphic to the chain complex of the lattice of flats of L. If N ∨ is a face of L containing v then N = L Fi+1 /Fi for some flag of flats ∅ = F0 ⊂ F1 ⊂ · · · ⊂ Fr = [n] of M.
  *Proof:* (no proof in this paper)
- **Proposition 2.5.** Let M be a matroid with M = L Mi the decomposition of M into connected parts. Then PM = Q PMi .
  *Proof:* Follows directly from the standard definition of direct sums where combined bases distribute across connected components.
- **Proposition 2.6.** If M ∨ is an r-dimensional face of L then the normal fan to M ∨ is a subfan of a coarsening of Br . When M ∨ is bounded, M ∨ is a Minkowski summand of the r th permutahedron.
  *Proof:* Identifies the local cone of the normal fan with the dual Bergman complex which refines the braid arrangement into a permutahedron.
- **Proposition 2.8.** Let L be a tropical linear space with tropical Plücker coordinates pI . Then L determines the pI up to addition of a common scalar.
  *Proof:* Analyzes the normal fan of a codimension 1 face corresponding to a loop-free matroid to fix coordinates up to global translation.
- **Theorem 2.9.** L is a pure d-dimensional contractible polyhedral complex.
  *Proof:* Proves pure dimensionality via the order complex of graded flats and topological contractibility by bounding tropically convex hyperplanes.
- **Proposition 2.10.** The following are equivalent: 1. w lies in a bounded face of L 2. PMw is an interior face of D. 3. Mw is loop-free and co-loop-free.
  *Proof:* Equates interior faces with those lacking coloop or loop elements by verifying they avoid the coordinate facets.
- **Proposition 2.11.** If the f -vector conjecture is true then a tropical d-plane in n-space has no more than n−i−1 d−i 2n−d−1 i−1 faces of dimension i.
  *Proof:* Computes the explicit combinatorial bound directly by summing the configurations over all possible loop-free interior faces.
- **Proposition 2.12.** The bounded part of L⊥ is negative that of L. If L is a tropical linear space of dimension d in n space then the bounded part of L is at most min(d, n − d)-dimensional.
  *Proof:* Exploits the self-dual symmetry of the loop/coloop-free conditions to restrict the bounded dimensionality of the dual space.
- **Proposition 3.1.** p(L ∩ L′ ) is a tropical Plücker vector.
  *Proof:* Expresses the stable intersection geometrically as a regular subdivision derived from projecting the lower faces of lifted Minkowski sums.
- **Corollary 3.2.** Every face of Dp(L ∩ L′ ) is of the form PM ∧M ′ for PM and PM ′ faces of Dp(L) and Dp(L′ ) .
  *Proof:* (immediate from Proposition 3.1)
- **Lemma 3.3.** Suppose that M and M ′ are transverse and let Γ = Γ(M, M ′ ). Then M ∧ M ′ is a loop-free matroid whose connected components are in bijection with the components of Γ. M ∧ M ′ is the matroid formed by repeatedly taking parallel connections along the edges of Γ. M ∧ M ′ has rank d + d′ − n.
  *Proof:* Formalizes iterative parallel connections on the bipartite graph to verify bases remain as component intersections without introducing loops.
- **Proposition 3.4.** Let 0 ≤ d, d′ ≤ n with d + d′ ≥ n. Suppose that L and L′ are tropical linear spaces in n-space of dimension d and d′ . Then L ∩ L′ ⊆ L ∩ L′ . If L and L′ meet transversely then L ∩ L′ = L ∩ L′ .
  *Proof:* Employs the dual subdivisions to verify that any existing loop element in the component matroids translates into a loop in the intersection.
- **Lemma 3.5.** M and M ′ are transverse, i.e., Γ(M, M ′ ) is a forest and has no multiple edges.
  *Proof:* Uses an edge and connected component counting argument on the intersection of the spanning affine spaces to conclude the graph is a forest.
- **Theorem 3.6.** Let L and L′ be tropical linear spaces. Then, for a generic v ∈ Rn , L and L′ + v meet transversely. L ∩ L′ = limv→0 (L ∩ (L′ + v)).
  *Proof:* Relies on the continuous variation of Plücker coordinates to show translated affine linear spaces have non-overlapping degenerate boundaries.
- **Theorem 4.1.** Trop I is the set of w for which Inw I contains no monomial.
  *Proof:* (no proof in this paper)
- **Proposition 4.2.** Trop L = L(p).
  *Proof:* Matches local valuations of exact Plücker relations over the power series field ensuring coordinate ideals avoid standalone monomials.
- **Proposition 4.3.** Let L and L′ ⊂ K n be two linear spaces. Then there exists a linear space L̃′ ⊂ K n with Trop L̃′ = Trop L′ and Trop L ∩ Trop L′ = Trop L ∩ Trop L̃′ = Trop(L∩ L̃′ ). If Trop L and Trop L′ meet transversely, then we already have Trop L ∩ Trop L′ = Trop(L∩ L′ ) without having to choose an L̃′ .
  *Proof:* Rescales the linear space dynamically with generic weights to avoid leading-term cancellation in the Plücker intersection sum. Establishes that the stable tropical intersection coincides algebraically with the generic coordinate limit.
- **Proposition 4.4.** If M is a rank d matroid on n elements, the function −ρ(·) on [n] d obeys the tropical Plücker relations, where ρ(S) is the rank of the flat spanned by S for any S ⊂ [n]. M is a face of the corresponding subdivision.
  *Proof:* Directly validates the tropical Plücker relation bounds iteratively, utilizing the minimal rank properties over matroid vertex definitions.
- **Proposition 5.1.** Π(T ) = Pµ(T ) for a series-parallel matroidal µ(T ). Every series-parallel matroid can be written as µ(T ) for some bi-colored trivalent tree T .
  *Proof:* Inducts recursively by mapping target tree node deletions directly to series and parallel extensions of the associated graphical matroid.
- **Proposition 5.2.** The facets of Π(T ) are given by (1) the equations P i∈Ae xe ≥ ae when e is an edge connecting two vertices of the opposite color and Ae is the set of leaves on the same side of e as the black endpoint, (2) the equations xi ≥ 0 when i is joined to a white vertex and (3) the equations xi ≤ 1 P when i is joined to a black vertex. (All of these are subject to already having the equality P xi = d.)
  *Proof:* Cancels redundant boundary inequalities and identifies each functional limit as a distinct facet via inductive structural tree restrictions.
- **Proposition 5.3.** Let e be an internal edge of T joining two vertices of opposite colors. Then the corresponding facet of Π(T ) is Π(T1 ) × Π(T2 ) where T \\e = T1 ⊔ T2 . If e joins a leaf i to a vertex v then the corresponding facet of Π(T ) is Π(T \\e) × P{i} where {i} is given the structure of a rank 1 matroid if v is black and a rank 0 matroid if v is white. The faces of Π(T ) are in bijection with the possible colored forests that can result from repeated splittings of T along edges connecting vertices of opposite color or connecting leaves to the rest of T . The faces of Π(T ) that correspond to loop and co-loop-free matroids are in bijection with the possible colored forests that can arise by repeated splittings along internal edges between vertices of opposite color.
  *Proof:* Iteratively splits opposite-colored vertices to show graph operations directly equate to the recursive facet decompositions mapping.
- **Theorem 6.1.** Let L be a d-dimensional tropical linear space in n space. Then L has at most n−2 d−1 vertices, with equality iff L is series parallel.
  *Proof:* Compares Tutte beta invariants with internal face subdivisions to deduce the bound relies directly on the series-parallel exactness limit.
- **Theorem 6.2.** Let L be a d-dimensional tropical linear space in n space with n = 2d or n = 2d + 1. Then L has at most 1 bounded facet if n = 2d and at most d if n = 2d + 1.
  *Proof:* Formulates bounded facets as perfect matchings of bipartite cyclic graphs. Constrains the maximum matchings by bounding possible connected component pairings using strict edge-counting and cycle limits in the distinct cases.
- **Proposition 6.3.** Let M be a matroid on at least 2 elements. Then β(M) = 0 if and only if M is disconnected and β(M) = 1 if and only if M is series-parallel.
  *Proof:* (no proof in this paper)
- **Lemma 6.4.** Let M be a matroid and let D be a matroidal subdivision of PM . Let D̊ denote the set of internal faces of D. Then tM (z, w) = P Pγ ∈D̊ (−1)dim(PM )−dim(Pγ ) tγ (z, w).
  *Proof:* Recalculates the rank generating function via inclusion-exclusion bounds integrated over the Euler characteristics of local contractible sub-polytopes.
- **Lemma 6.5.** Let P be any bounded polytope and Γ the internal faces of a decomposition of P . Then P γ∈Γ (−1)dim(P )−dim(γ) = 1.
  *Proof:* Applies the direct Euler characteristic topological equality over contractible bounded geometries mapping back to the spherical boundary.
- **Lemma 6.6.** Let Γ = Γ(M, M ′ ). Γ may have multiple edges, let Γ be the simple graph obtained by replacing each multiple edge of Γ by a single edge. Then PM ∩ PM ′ is empty if and only if Γ has no perfect matchings. PM ∩ PM ′ is matroidal if and only if Γ has precisely one perfect matching.
  *Proof:* Maps geometric polytope vertices directly to graph perfect matchings where a single matching structurally defines a valid matroidal product.
- **Lemma 7.1.** Let M̃ be a series-parallel matroid and let PM be a face of PM̃ , assume that M is loop-free. Let M = L Mi be the decomposition of M into connected components. Then each of the Mi are series-parallel.
  *Proof:* Derives the resulting inheritance strictly from the explicit colored tree forest decomposition properties characterizing the series-parallel matroids.
- **Proposition 7.2.** Let M = L Mi and M ′ = L Mi′ be transverse matroids on [n] with all of the Mi and Mi′ series-parallel. Then M ∧ M ′ is a direct sum of series-parallel matroids, and is series parallel if it is connected.
  *Proof:* Notes directly that the underlying parallel connection construction fundamentally preserves the topological series-parallel structural property.
- **Lemma 7.3.** Let M be a series-parallel matroid. Call a flat Q of M “good” if M|Q and M/Q are connected and not loops. Let f and g ∈ M. Then the collection of all good flats Q such that f ∈ Q, g 6∈ Q forms a chain Q1 ⊂ · · · ⊂ Qd . Moreover, the length d of this chain is preserved when the roles of f and g are switched.
  *Proof:* Associates good flat sequences with alternating block color transitions across tree paths directly establishing strict nested topological chains.
- **Theorem 7.4.** Let L and L′ be two series-parallel tropical linear spaces in n-space, of dimensions d and d′ . Let a and b ∈ Rn be such that L meets L′ + a and L′ + b transversely. Then L ∩ (L′ + a) and L ∩ (L′ + b) have the same bounded f -vector.
  *Proof:* Generically perturbs the intersection space to show the continuous f-vector counts remain topologically invariant. Explicitly counts codimension faces by resolving path decompositions along unique cycles in the associated transverse intersection graph.
- **Lemma 7.5.** There exist decompositions E+ and E− of PN such that, if ± P2r i=1 (−1)i wei > 0 then N is subdivided according to E± in Eǫw for ǫ a sufficiently small positive number. Moreover, there is an integer D such that E+ and E− each have D c+1 interior faces of codimension c.
  *Proof:* Analyzes the relative positional shifts along crossing hyperplanes induced by generic coordinate perturbations. Proves the intersection subdivision branches uniquely into identifiable nested flat configurations enumerated by alternating sum lengths.
- **Lemma 7.6.** If L is a constructible d-plane in n-space and S and T are disjoint subsets of [n] then L \ S/T is also constructible.
  *Proof:* Inducts recursively using the dualization and stable intersection constraints verifying the bounded subset correctly preserves valid constructibility.
- **Lemma 7.7.** For w1 ≪ w2 ≪ · · · ≪ wn , we have M ∨ ∩ (M ′ )∨ 6= ∅ if and only if (T, T ′ ) is nice. If (T, T ′ ) is nice then M ∨ ∩ (M ′ )∨ is bounded if and only if T ∩ T ′ = ∅.
  *Proof:* Identifies paired sub-component properties mathematically resolving the limits by applying strict functional bounds and verifying continuous path distances.
- **Theorem 8.1.** Let L be a tropical 2-plane in n-space. Then there exists a tree T as above such that pij = −(1/2)d(i, j). Moreover, L/(1, . . . , 1) is an embedding of T \ {leaves of T } in Rn /(1, . . . , 1), where the bounded part of L/(1, . . . , 1) is the image of the internal edges of T . For every such T , set pij = (−1/2)d(i, j), pij obeys the tropical Plücker relations. p is generic if and only if the corresponding L is series-parallel if and only if the tree T is trivalent ( i.e. every non-leaf has degree 3.) Every 2-dimensional tropical linear space is realizable.
  *Proof:* (no proof in this paper)
- **Proposition 8.2.** τ d (p) obeys the tropical Plücker relations.
  *Proof:* Realizes the metric tree lengths purely by evaluating maximal minors directly over generically assigned power series Vandermonde determinants.
- **Theorem 8.4.** The vertices of τ d (L) are of the form µ(T, c)∨ where c ranges over the n−2 d−1 ways to color the internal vertices of T black and white with d − 1 colored black and n − d − 1 colored white. The bounded i-dimensional faces of τ d (T ) are in bijection with the ordered pairs (F, c), where F is a forest with i trees that can be obtained by splitting T along internal edges and c is a black and white coloring of the internal vertices of F using d−i black vertices and n−d−i white vertices. (F, c) is contained in (F ′ , c′ ) if and only if (F ′ , c′ ) can be obtained from (F, c) by repeated splitting along edges connecting vertices of opposite colors.
  *Proof:* Expresses the tree space subdivision generically via combined convex functional projections matching colored tree combinations. Verifies facets strictly map to interior integer inequalities corresponding directly to the vertex degree counts.
- **Corollary 8.5.** τ d (L) has fi,d,n = n−i−1 d−i n−2i i−1 bounded faces of dimension i.
  *Proof:* Uses an explicit edge splitting and subset combinatorial argument iteratively evaluating tree separations verifying exact tree forest counts.
```