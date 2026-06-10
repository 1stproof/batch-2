<!-- Generated 2026-05-31T02:36:47 -->
<!-- Source PDF: herrmann__how_to_draw_tropical_planes.pdf (332586 bytes) -->
<!-- Citation: Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. (2012). How to draw tropical planes. Electronic Journal of Combinatorics. -->

# How to draw tropical planes (Herrmann, Jensen, Joswig, Sturmfels, 2012)

## Definitions
(None)

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 2.1.** Fix any field K of characteristic different from 2. The tropical Grassmannian Gr(3, 7), with its induced Gröbner fan structure, is a simplicial fan with f -vector (721, 16800, 124180, 386155, 522585, 252000) . The homology of the underlying five-dimensional simplicial complex is free Abelian, and it is concentrated in top dimension: H∗ Gr(3, 7); Z = H5 Gr(3, 7); Z = Z7470 .
  *Proof:* The ideal over the rationals is processed with Gfan by exploiting codimension-one connectivity to traverse the maximal Gröbner cones up to symmetry; Macaulay2 is then used to verify characteristic-free Gröbner bases for prime characteristics, evaluating homological cancellation exclusively at the Fano cone.

- **Theorem 2.2.** The Dressian Dr(3, 7), with its Plücker fan structure, is a non-simplicial fan. The underlying polyhedral complex is six-dimensional and has the f -vector (616, 13860, 101185, 315070, 431025, 211365, 30) . Its 5-skeleton is triangulated by the Grassmannian Gr(3, 7), and the homology is H∗ Dr(3, 7); Z = H5 Dr(3, 7); Z = Z7440 .
  *Proof:* Recursively enumerates configurations via abstract tree arrangements to efficiently parse the Plücker relations, computing the integral homology via the crosscut complex.

- **Corollary 2.3.** The number of combinatorial types of generic planes in TP6 is 94. The numbers of types of generic planes in TP3 , TP4 , and TP5 are 1, 1, and 7, respectively.
  *Proof:* Extracts the 94 specific generic facets of TP6 from the Dressian complex generated in Theorem 2.2, contrasting them against the generic variants in lower dimensions.

- **Proposition 3.1.** (Speyer [27, Proposition 2.2]) A weight vector λ ∈ R          d    lies in the Dressian Dr(d, n), seen as a fan, if and only if it induces a matroid subdivision of the hypersimplex ∆(d, n).
  *Proof:* (no proof in this paper)

- **Corollary 3.2.** Let M be a connected matroid of rank d on [n] and let λM ∈ {0, 1}          d be the vector which satisfies λM (X) = 0 if X is a basis of M and λM (X) = 1 if X is not a basis of M. Then λM lies in the Dressian Dr(d, n), and the corresponding matroid decomposition of ∆(d, n) has the matroid polytope PM as a maximal cell.
  *Proof:* Translates the basis exchange axiom into combinatorial quadratic Plücker relations and applies Proposition 3.1.

- **Proposition 3.3.** (Kapranov [20, Corollary 1.4.14]). Each regular subdivision of the product of simplices ∆d−1 × ∆n−d−1 is induced by a regular matroid subdivision of ∆(d, n).
  *Proof:* (no proof in this paper)

- **Proposition 3.4.** The split complex of ∆(d, n) is a simplicial subcomplex of the Dressian Dr(d, n), with its secondary complex structure. They are equal if d = 2 or d = n − 2.
  *Proof:* (no proof in this paper)

- **Corollary 3.5.** The simplicial complex of stable sets of the edge graph of the hypersimplex ∆(d, n) is a subcomplex of Dr(d, n). Hence, the dimension of the Dressian Dr(d, n), seen as a polytopal complex, is bounded below by one less than the maximal size of a stable set of this edge graph.
  *Proof:* (no proof in this paper)

- **Theorem 3.6.** The dimension of the Dressian Dr(3, n) is of order Θ(n2 ).
  *Proof:* Derives a quadratic upper bound on spread from Speyer's theorem, then constructs a matching quadratic lower bound via non-basis stable sets of the generalized Fano matroid.

- **Proposition 3.7.** As n increases, the spread of the rays of Dr(3, n) is not bounded by a constant.
  *Proof:* Relates rays of Dr(3, n) to mixed subdivisions of dilated triangles using the Cayley trick to demonstrate unbounded polygon growth.

- **Proposition 4.1.** Each metric tree arrangement gives rise to an abstract tree arrangement by ignoring the edge lengths. The converse is not true: for n ≥ 9, there exist abstract arrangements of n trees that do not support any metric tree arrangement.
  *Proof:* Applies the Four Point Condition to strip metric data and constructs an explicit 9-tree non-regular counterexample configuration to reject the converse.

- **Lemma 4.2.** Each matroid subdivision Σ of ∆(3, n) defines an abstract arrangement T (Σ) of n trees. Moreover, if Σ is regular then T (Σ) supports a metric tree arrangement.
  *Proof:* Maps regular subdivision boundaries to dual trees and assigns metric edge lengths by applying the Split Decomposition Theorem to compatible splits on contraction facets.

- **Proposition 4.3.** Let Σ and Σ̄ be two matroid subdivisions of ∆(3, n) such that Σ refines Σ̄. If Σ and Σ̄ induce the same subdivision on the boundary of ∆(3, n) then Σ and Σ̄ coincide.
  *Proof:* Assumes strict refinement to locate a split hyperplane defined by a codimension-1 cell, extracting Euclidean point subconfigurations to derive a contradiction via an isolated boundary-defined square cell.

- **Theorem 4.4.** The equivalence classes of arrangements of n metric trees are in bijection with the regular matroid subdivisions of the hypersimplex ∆(3, n). Moreover, the secondary fan structure on Dr(3, n) coincides with the Plücker fan structure.
  *Proof:* Proceeds by induction to propagate finite Plücker minimums from overlapping deletion facets, applying Proposition 4.3 to establish equivalent fan structures.

- **Proposition 4.5.** Each polytopal subdivision Σ of ∆2 × ∆n−4 , or each mixed subdivision M(Σ) of the triangle (n − 3)∆2 , determines an abstract arrangement T (Σ) of n trees.
  *Proof:* Constructs abstract trees by tracing parallel edge classes rooted at upward triangles within lozenge tilings.

- **Proposition 5.1.** Let L be a tropical plane in TPn−1 with f0 (L) vertices, f1b (L) bounded edges, f1u (L) unbounded edges, f2b (L) bounded 2-cells and f2u (L) unbounded 2-cells. Then f0 (L) ≤ (n − 2)(n − 3)/2, f1b (L) ≤ (n − 4)(n − 3), f1u (L) ≤ n(n − 3), f2b (L) ≤ (n − 4)(n − 5)/2, f2u (L) ≤ 3n(n − 1)/2 . These five inequalities are equalities if and only if L is a series-parallel plane.
  *Proof:* (no proof in this paper)

- **Proposition 6.1.** The Grassmannian Gr(M) of the Pappus matroid M is a graph with 19 nodes and 30 edges. One of the nodes gets replaced by a triangle in the Dressian Dr(M). The Dressian Dr(M) is a simplicial complex with 18 vertices, 30 edges and one triangle.
  *Proof:* Exhaustively graphs the split nodes, Graves triads, and connector nodes of the Grassmannian; localizes the trinomials of the Pappus ideal to demonstrate that the core triangle of the Dressian isolates the Hessian configuration.