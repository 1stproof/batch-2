<!-- Generated 2026-05-31T02:38:29 -->
<!-- Source PDF: herrmann__how_to_draw_tropical_planes.pdf (332586 bytes) -->
<!-- Citation: Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. (2009). How to draw tropical planes. Electronic Journal of Combinatorics. -->

```markdown
# How to draw tropical planes, Herrmann, Jensen, Joswig, Sturmfels (2009)

## Definitions
*(None)*

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 2.1.** Fix any field K of characteristic different from 2. The tropical Grassmannian Gr(3, 7), with its induced Gröbner fan structure, is a simplicial fan with f -vector (721, 16800, 124180, 386155, 522585, 252000) . The homology of the underlying five-dimensional simplicial complex is free Abelian, and it is concentrated in top dimension: H∗ Gr(3, 7); Z = H5 Gr(3, 7); Z = Z7470 .
  *Proof:* Traverses the maximal Gröbner cones up to symmetry using Gfan, checking polyhedral continuations, and utilizes Macaulay2 over Z to establish characteristic-freeness outside the Fano cone.

- **Theorem 2.2.** The Dressian Dr(3, 7), with its Plücker fan structure, is a non-simplicial fan. The underlying polyhedral complex is six-dimensional and has the f -vector (616, 13860, 101185, 315070, 431025, 211365, 30) . Its 5-skeleton is triangulated by the Grassmannian Gr(3, 7), and the homology is H∗ Dr(3, 7); Z = H5 Dr(3, 7); Z = Z7440 .
  *Proof:* Recursively exhaustively enumerates abstract tree arrangements using polymake, validating via linear programming, and computes homology via the crosscut complex.

- **Corollary 2.3.** The number of combinatorial types of generic planes in TP6 is 94. The numbers of types of generic planes in TP3 , TP4 , and TP5 are 1, 1, and 7, respectively.
  *Proof:* Analyzes low-dimensional spaces directly utilizing known graphs and dual trees, extracting n=7 directly from Theorem 2.2.

- **Proposition 3.1.** (Speyer [27, Proposition 2.2]) A weight vector λ ∈ R [n] d lies in the Dressian Dr(d, n), seen as a fan, if and only if it induces a matroid subdivision of the hypersimplex ∆(d, n).
  *Proof:* (no proof in this paper)

- **Corollary 3.2.** Let M be a connected matroid of rank d on [n] and let λM ∈ {0, 1} [n] d be the vector which satisfies λM (X) = 0 if X is a basis of M and λM (X) = 1 if X is not a basis of M. Then λM lies in the Dressian Dr(d, n), and the corresponding matroid decomposition of ∆(d, n) has the matroid polytope PM as a maximal cell.
  *Proof:* Maps the basis exchange axiom to combinatorial quadratic Plücker relations to establish λM in Dr(d,n) and applies Proposition 3.1.

- **Proposition 3.3.** (Kapranov [20, Corollary 1.4.14]). Each regular subdivision of the product of simplices ∆d−1 × ∆n−d−1 is induced by a regular matroid subdivision of ∆(d, n).
  *Proof:* (no proof in this paper)

- **Proposition 3.4.** The split complex of ∆(d, n) is a simplicial subcomplex of the Dressian Dr(d, n), with its secondary complex structure. They are equal if d = 2 or d = n − 2.
  *Proof:* (no proof in this paper)

- **Corollary 3.5.** The simplicial complex of stable sets of the edge graph of the hypersimplex ∆(d, n) is a subcomplex of Dr(d, n). Hence, the dimension of the Dressian Dr(d, n), seen as a polytopal complex, is bounded below by one less than the maximal size of a stable set of this edge graph.
  *Proof:* (no proof in this paper)

- **Theorem 3.6.** The dimension of the Dressian Dr(3, n) is of order Θ(n2 ).
  *Proof:* Bounds the dimension above via the maximal number of facets of a matroid subdivision, and bounds it below by leveraging the generalized Fano matroid to find a quadratic-sized stable set in the edge graph.

- **Proposition 3.7.** As n increases, the spread of the rays of Dr(3, n) is not bounded by a constant.
  *Proof:* Employs the Cayley trick to relate coarsest mixed subdivisions of dilated triangles with arbitrarily many polygons to rays of the Dressian via regular matroid subdivisions.

- **Proposition 4.1.** Each metric tree arrangement gives rise to an abstract tree arrangement by ignoring the edge lengths. The converse is not true: for n ≥ 9, there exist abstract arrangements of n trees that do not support any metric tree arrangement.
  *Proof:* Deduces the first assertion from the Four Point Condition, and proves the converse using a specific nine-caterpillar tree counterexample.

- **Lemma 4.2.** Each matroid subdivision Σ of ∆(3, n) defines an abstract arrangement T (Σ) of n trees. Moreover, if Σ is regular then T (Σ) supports a metric tree arrangement.
  *Proof:* Derives the abstract arrangement from matroid subdivisions on the contraction facets and uses the Split Decomposition Theorem to assign lengths.

- **Proposition 4.3.** Let Σ and Σ̄ be two matroid subdivisions of ∆(3, n) such that Σ refines Σ̄. If Σ and Σ̄ induce the same subdivision on the boundary of ∆(3, n) then Σ and Σ̄ coincide.
  *Proof:* Assumes a strict refinement yielding an interior face, isolates rank-3 affine point subconfigurations, and reaches a contradiction via the boundary intersections.

- **Theorem 4.4.** The equivalence classes of arrangements of n metric trees are in bijection with the regular matroid subdivisions of the hypersimplex ∆(3, n). Moreover, the secondary fan structure on Dr(3, n) coincides with the Plücker fan structure.
  *Proof:* Constructs a valid tropical Plücker vector from tree metrics by induction on n, and employs Proposition 4.3 to establish equality of the secondary and Plücker structures.

- **Proposition 4.5.** Each polytopal subdivision Σ of ∆2 × ∆n−4 , or each mixed subdivision M(Σ) of the triangle (n − 3)∆2 , determines an abstract arrangement T (Σ) of n trees.
  *Proof:* Associates tree branches with upward triangles and parallel edges in lozenge tilings, contracting edges to accommodate non-triangulations.

- **Proposition 5.1.** Let L be a tropical plane in TPn−1 with f0 (L) vertices, f1b (L) bounded edges, f1u (L) unbounded edges, f2b (L) bounded 2-cells and f2u (L) unbounded 2-cells. Then f0 (L) ≤ (n − 2)(n − 3)/2, f1b (L) ≤ (n − 4)(n − 3), f1u (L) ≤ n(n − 3), f2b (L) ≤ (n − 4)(n − 5)/2, f2u (L) ≤ 3n(n − 1)/2 . These five inequalities are equalities if and only if L is a series-parallel plane.
  *Proof:* (no proof in this paper)

- **Proposition 6.1.** The Grassmannian Gr(M) of the Pappus matroid M is a graph with 19 nodes and 30 edges. One of the nodes gets replaced by a triangle in the Dressian Dr(M). The Dressian Dr(M) is a simplicial complex with 18 vertices, 30 edges and one triangle.
  *Proof:* Explicitly maps the 19 nodes of Gr(M) as split nodes, Graves triads, and connector nodes, then constructs the core triangle of Dr(M) algebraically from a specific trinomial in the Pappus ideal.
```