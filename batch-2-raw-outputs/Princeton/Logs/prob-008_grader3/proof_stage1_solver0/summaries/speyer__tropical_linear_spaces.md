<!-- Generated 2026-05-31T02:37:25 -->
<!-- Source PDF: speyer__tropical_linear_spaces.pdf (362553 bytes) -->
<!-- Citation: Speyer, D. E. (2008). Tropical Linear Spaces. SIAM Journal on Discrete Mathematics. -->

# Tropical Linear Spaces, Speyer, D. E. (2008). SIAM Journal on Discrete Mathematics.

## Definitions

*(No named definitions found in the paper)*

## Lemmas, Theorems, Propositions, Corollaries

- **Theorem 1.2.** Every constructible space achieves the f -vector of the f -vector conjecture.
  *Proof:* Inducts on the dimension and the number of constructibility steps, reducing to transverse intersections of translated spaces via Theorem 7.4. Uses combinatorial identities over stable overlap sets to verify that the total faces sum exactly to the conjectured f-vector bounds.
- **Theorem 1.3.** Every constructible space is series-parallel.
  *Proof:* Relies on the stability of series-parallel matroids under dualization and transverse intersections via Lemma 7.1 and Proposition 7.2.
- **Proposition 2.2.** The following are equivalent: 1. pi1 ...id are tropical Plücker coordinates 2. The one skeleta of D and ∆(d, n) are the same. 3. Every face of D is matroidal.
  *Proof:* Uses geometric induction to show edges of the subdivision D cannot exceed length 1 without violating Plücker relations, appealing to a known theorem linking 1-skeleta limits to matroidality.
- **Proposition 2.3.** w ∈ L(p) if and only if Mw is loop-free.
  *Proof:* Normalizes minimal valuations to zero and bounds loop extensions dynamically during coordinate shifts across adjoining matroidal facets.
- **Proposition 2.4.** linkM ∨ (L) is homeomorphic to the chain complex of the lattice of flats of L. If N ∨ is a face of L containing v then N = ⊕ Fi+1 /Fi for some flag of flats ∅ = F0 ⊂ F1 ⊂ · · · ⊂ Fr = [n] of M.
  *Proof:* (no proof in this paper)
- **Proposition 2.5.** Let M be a matroid with M = L Mi the decomposition of M into connected parts. Then PM = Q PMi .
  *Proof:* Observes directly that the bases of a direct sum matroid are exact combinations of the bases of its constituent components.
- **Proposition 2.6.** If M ∨ is an r-dimensional face of L then the normal fan to M ∨ is a subfan of a coarsening of Br . When M ∨ is bounded, M ∨ is a Minkowski summand of the r th permutahedron.
  *Proof:* Identifies the face link in the subdivision with the normal fan of the corresponding polytope, recognizing that complete fans coarsen the braid arrangement.
- **Proposition 2.8.** Let L be a tropical linear space with tropical Plücker coordinates pI . Then L determines the pI up to addition of a common scalar.
  *Proof:* Analyzes loop-free boundary hyperplanes to deduce that uniquely formed scalar relationships strictly bind the coordinates up to a global translation.
- **Theorem 2.9.** L is a pure d-dimensional contractible polyhedral complex.
  *Proof:* Evaluates purity via the length of the matroid's graded lattice of flats and contractibility by expressing the linear space as an intersection of tropically convex hyperplanes.
- **Proposition 2.10.** The following are equivalent: 1. w lies in a bounded face of L 2. PMw is an interior face of D. 3. Mw is loop-free and co-loop-free.
  *Proof:* Checks spatial boundary criteria within the hypersimplex directly against the matroidal condition that elements cannot uniformly be loops or co-loops.
- **Proposition 2.11.** If the f -vector conjecture is true then a tropical d-plane in n-space has no more than n−i−1 d−i 2n−d−1 i−1 faces of dimension i.
  *Proof:* Sums the conjectured limit counts globally over the co-loop bounding faces structured inside the hypersimplex.
- **Proposition 2.12.** The bounded part of L⊥ is negative that of L. If L is a tropical linear space of dimension d in n space then the bounded part of L is at most min(d, n − d)-dimensional.
  *Proof:* Reverses self-dual loops and co-loops to uniformly bound the interior dimensionality against the bounds of the ambient spaces.
- **Proposition 3.1.** p(L ∩ L′ ) is a tropical Plücker vector. stable
  *Proof:* Embeds both subdivisions into a higher-dimensional Minkowski sum and projects the lowest bounding faces back down to form a valid regular subdivision.
- **Corollary 3.2.** Every face of Dp(L ∩ L′ ) is of the form PM ∧M ′ for PM and PM ′ faces of Dp(L) and Dp(L′ ) . stable
  *Proof:* (immediate from Proposition 3.1)
- **Lemma 3.3.** Suppose that M and M ′ are transverse and let Γ = Γ(M, M ′ ). Then M ∧ M ′ is a loop-free matroid whose connected components are in bijection with the components of Γ. M ∧ M ′ is the matroid formed by repeatedly taking parallel connections along the edges of Γ. M ∧ M ′ has rank d + d′ − n.
  *Proof:* Validates that bases extracted through iteratively contracting tree components perfectly match the generating limits of transverse matroid intersections.
- **Proposition 3.4.** Let 0 ≤ d, d′ ≤ n with d + d′ ≥ n. Suppose that L and L′ are tropical linear spaces in n-space of dimension d and d′ . Then L ∩ L′ ⊆ L ∩ L′ . If L and L′ meet stable transversely then L ∩ L′ = L ∩ L′ . stable
  *Proof:* Matches loop presence in the intersected matroidal facets against component loops, reserving strict equivalence for spaces with fully spanned ambient degrees.
- **Lemma 3.5.** M and M ′ are transverse, i.e., Γ(M, M ′ ) is a forest and has no multiple edges.
  *Proof:* Relies on dimension counting across linearly mapped independent intersections to force the bipartite graph representations to drop multiple paths.
- **Theorem 3.6.** Let L and L′ be tropical linear spaces. Then, for a generic v ∈ Rn , L and L′ + v meet transversely. L ∩ L′ = limv→0 (L ∩ (L′ + v)). stable
  *Proof:* Generically separates lower-dimensional overlap subspaces to ensure full transverse intersection, relying on limits evaluated via Plücker vector continuity.
- **Theorem 4.1.** Trop I is the set of w for which Inw I contains no monomial.
  *Proof:* (no proof in this paper)
- **Proposition 4.2.** Trop L = L(p).
  *Proof:* Cross-checks generalized vanishing Plücker combinations dynamically against ideals forming isolated loop-free basis expansions.
- **Proposition 4.3.** Let L and L′ ⊂ K n be two linear spaces. Then there exists a linear space L̃′ ⊂ K n with Trop L̃′ = Trop L′ and Trop L ∩ Trop L′ = Trop L ∩ Trop L̃′ = Trop(L∩ L̃′ ). stable stable If Trop L and Trop L′ meet transversely, then we already have Trop L ∩ Trop L′ = Trop(L∩ L′ ) without having to choose an L̃′ . stable
  *Proof:* Introduces randomized term scalings to stop classical intersection cancellations, applying a cochain zero-sum rule to the intersection acyclic components mapping single minimal overlaps.
- **Proposition 4.4.** If M is a rank d matroid on n elements, the function −ρ(·) on [n] d obeys the tropical Plücker relations, where ρ(S) is the rank of the flat spanned by S for any S ⊂ [n]. M is a face of the corresponding subdivision.
  *Proof:* Checks minimal combinations strictly over 4-element flats mapping 2-rank permutations inside generic subdivided matroids.
- **Proposition 5.1.** Π(T ) = Pµ(T ) for a series-parallel matroidal µ(T ). Every series-parallel matroid can be written as µ(T ) for some bi-colored trivalent tree T .
  *Proof:* Systematically shrinks edge subtrees via graphical leaf deletion, linking series branches directly to mapped black and white constraint extensions.
- **Proposition 5.2.** The facets of Π(T ) are given by (1) the equations i∈Ae xe ≥ ae when e is an edge connecting two vertices of the opposite color and Ae is the set of leaves on the same side of e as the black endpoint, (2) the equations xi ≥ 0 when i is joined to a white vertex and (3) the equations xi ≤ 1 P when i is joined to a black vertex. (All of these are subject to already having the equality xi = d.)
  *Proof:* Prunes bounding redundancies iteratively and subjects isolated strict facets to boundary perturbations across contracted leaf nodes.
- **Proposition 5.3.** Let e be an internal edge of T joining two vertices of opposite colors. Then the corresponding facet of Π(T ) is Π(T1 ) × Π(T2 ) where T \\e = T1 ⊔ T2 . If e joins a leaf i to a vertex v then the corresponding facet of Π(T ) is Π(T \\e) × P{i} where {i} is given the structure of a rank 1 matroid if v is black and a rank 0 matroid if v is white. The faces of Π(T ) are in bijection with the possible colored forests that can result from repeated splittings of T along edges connecting vertices of opposite color or connecting leaves to the rest of T . The faces of Π(T ) that correspond to loop and co-loop-free matroids are in bijection with the possible colored forests that can arise by repeated splittings along internal edges between vertices of opposite color.
  *Proof:* Iterates defining boundary checks mapping independent bi-colored sub-blocks into distinct direct coordinate products.
- **Theorem 6.1.** Let L be a d-dimensional tropical linear space in n space. Then L has at most n−2 d−1 vertices, with equality iff L is series parallel.
  *Proof:* Implements Euler topological sums checking beta invariants, bounding the polytope overlaps explicitly against series-parallel vertex structures.
- **Theorem 6.2.** Let L be a d-dimensional tropical linear space in n space with n = 2d or n = 2d + 1. Then L has at most 1 bounded facet if n = 2d and at most d if n = 2d + 1.
  *Proof:* Analyzes isolated facet constraints by mapping interior sub-cycles against the isolated single perfect matching criteria. Leverages length limits on non-crossing connected components mapped across internal bases bounds.
- **Proposition 6.3.** Let M be a matroid on at least 2 elements. Then β(M) = 0 if and only if M is disconnected and β(M) = 1 if and only if M is series-parallel.
  *Proof:* (no proof in this paper)
- **Lemma 6.4.** Let M be a matroid and let D be a matroidal subdivision of PM . Let D̊ denote the set of internal faces of D. Then tM (z, w) = X Pγ ∈D̊ (−1)dim(PM )−dim(Pγ ) tγ (z, w).
  *Proof:* Converts subset rankings across bounded facets mapping linearly shifted subsets over a bounded half-space Euler characteristic identity.
- **Lemma 6.5.** P Let Pdim(P be any bounded polytope and Γ the internal faces of a decomposition of P . Then γ∈Γ (−1) )−dim(γ) = 1.
  *Proof:* Applies the standard alternating sum Euler characteristic to contractible inner polytopes against their bounding spherical shells.
- **Lemma 6.6.** Let Γ = Γ(M, M ′ ). Γ may have multiple edges, let Γ be the simple graph obtained by replacing each multiple edge of Γ by a single edge. Then PM ∩ PM ′ is empty if and only if Γ has no perfect matchings. PM ∩ PM ′ is matroidal if and only if Γ has precisely one perfect matching.
  *Proof:* Establishes bijectivity between perfect graph matchings and bounded independent coordinate limits, forcing single overlap chains for full matroidality limits.
- **Lemma 7.1.** Let M̃ be aLseries-parallel matroid and let PM be a face of PM̃ , assume that M is loop-free. Let M = Mi be the decomposition of M into connected components. Then each of the Mi are series-parallel.
  *Proof:* Matches loop-free subdivisions dynamically using recursive bi-colored boundary maps splitting isolated components.
- **Proposition 7.2.** Let M = L Mi and M ′ = L Mi′ be transverse matroids on [n] with all of the Mi and Mi′ series-parallel. Then M ∧ M ′ is a direct sum of series-parallel matroids, and is series parallel if it is connected.
  *Proof:* Relies on the fact that iterative parallel component connections naturally enforce combined series-parallel behavior.
- **Lemma 7.3.** Let M be a series-parallel matroid. Call a flat Q of M “good” if M|Q and M/Q are connected and not loops. Let f and g ∈ M. Then the collection of all good flats Q such that f ∈ Q, g 6∈ Q forms a chain Q1 ⊂ · · · ⊂ Qd . Moreover, the length d of this chain is preserved when the roles of f and g are switched.
  *Proof:* Constructs ordered chains crossing bipartite components spanning leaf-to-leaf paths to count symmetric connected flats.
- **Theorem 7.4.** Let L and L′ be two series-parallel tropical linear spaces in n-space, of dimensions d and d′ . Let a and b ∈ Rn be such that L meets L′ + a and L′ + b transversely. Then L ∩ (L′ + a) and L ∩ (L′ + b) have the same bounded f -vector.
  *Proof:* Formulates generic path translations maintaining affine spacing configurations mapping uniform overlap distributions via limiting face subdivisions encoded inside Lemma 7.5.
- **Lemma 7.5.** There exist decompositions E+ and E− of PN such that, if ± 2r P i i=1 (−1) wei > 0 then N is subdivided according to E± in Eǫw for ǫ a sufficiently small positive number. D Moreover, there is an integer D such that E+ and E− each have c+1 interior faces of codimension c.
  *Proof:* Decomposes structural hyperplanes via crossing paths overlapping good flats, checking bounding face counts crossing strict independent subsets. Compares positive and negative overlapping cycle splits against uniformly bounded permutations.
- **Lemma 7.6.** If L is a constructible d-plane in n-space and S and T are disjoint subsets of [n] then L \ S/T is also constructible.
  *Proof:* Inducts backwards through operations governing space derivation via overlapping bounds directly intersecting classical hyperplane dualizations.
- **Lemma 7.7.** For w1 ≪ w2 ≪ · · · ≪ wn , we have M ∨ ∩ (M ′ )∨ 6= ∅ if and only if (T, T ′ ) is nice. If (T, T ′ ) is nice then M ∨ ∩ (M ′ )∨ is bounded if and only if T ∩ T ′ = ∅.
  *Proof:* Analyzes bounding vectors separated over generic limit points checking bounding gaps directly against strict coordinate overlap restrictions.
- **Theorem 8.1.** Let L be a tropical 2-plane in n-space. Then there exists a tree T as above such that pij = −(1/2)d(i, j). Moreover, L/(1, . . . , 1) is an embedding of T \ {leaves of T } in Rn /(1, . . . , 1), where the bounded part of L/(1, . . . , 1) is the image of the internal edges of T . For every such T , set pij = (−1/2)d(i, j), pij obeys the tropical Plücker relations. p is generic if and only if the corresponding L is series-parallel if and only if the tree T is trivalent ( i.e. every non-leaf has degree 3.) Every 2-dimensional tropical linear space is realizable.
  *Proof:* (no proof in this paper)
- **Proposition 8.2.** τ d (p) obeys the tropical Plücker relations.
  *Proof:* Verifies maximal matrix minors evaluated against symmetric series coefficients matching classical Plücker combinations.
- **Theorem 8.4.** The vertices of τ d (L) are of the form µ(T, c)∨ where c ranges over the n−2 d−1 ways to color the internal vertices of T black and white with d − 1 colored black and n − d − 1 colored white. The bounded i-dimensional faces of τ d (T ) are in bijection with the ordered pairs (F, c), where F is a forest with i trees that can be obtained by splitting T along internal edges and c is a black and white coloring of the internal vertices of F using d−i black vertices and n−d−i white vertices. (F, c) is contained in (F ′ , c′ ) if and only if (F ′ , c′ ) can be obtained from (F, c) by repeated splitting along edges connecting vertices of opposite colors.
  *Proof:* Expresses coordinate parameters recursively into convex internal bounding limits mapping specific interior facet domains. Distributes matching constraints exactly across tree elements maintaining cyclic block properties accurately matching vertex dimension assignments.
- **Corollary 8.5.** τ d (L) has fi,d,n = n−2i d−i n−i−1 i−1 bounded faces of dimension i.
  *Proof:* Implements counting rules directly distributing bounded trivalent component subsets mapping recursive component separations.