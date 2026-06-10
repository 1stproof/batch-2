<!-- Generated 2026-05-31T02:01:47 -->
<!-- Source PDF: alon__the_probabilistic_method.pdf (216967 bytes) -->
<!-- Citation: Alon, N., Spencer, J. H. (2016). The Probabilistic Method. Wiley. -->

# Paul Erdős and the Probabilistic Method (Alon, N., Spencer, J. H., 2016)

## Definitions
*(None in this paper)*

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 2.1 ([25], [1]).** There are two absolute positive constants c1 , c2 such that c1 m2 / log m ≤ r(K3 , Km ) ≤ c2 m2 / log m for all m > 1.
  *Proof:* Analyzes the triangle-free process (adding random edges that do not create triangles) for the lower bound, and cites a random greedy algorithm for the upper bound.

- **Theorem 2.2.** For every t > 1 and s ≥ (t − 1)! + 1 there are two positive constants c1 , c2 such that for every m > 1 mt mt c1 t ≤ r(Kt,s , Kt,s , Kt,s , Km ) ≤ c2 t , log m log m where Kt,s is the complete bipartite graph with t vertices in one color class and s vertices in the other.
  *Proof:* Establishes the lower bound by constructing the first three color classes as randomly shifted copies of a Kt,s-free graph, bounding large independent sets via spectral techniques and character sum estimates.

- **Theorem 4.1.** For every fixed r ≥ 2 and s ≥ 2, there is a d = d(r, s), such that the list chromatic number of any simple r-uniform hypergraph with n vertices and at least nd edges is greater than s.
  *Proof:* Assigns randomly chosen lists of colors to the vertices and shows that with high probability no proper coloring exists.

- **Theorem 4.2 ([4]).** For any finite set X in the Euclidean plane and for any positive integer s, there is an assignment of a list of size s to every point of the plane, such that whenever we color the points of the plane from their lists, there is a monochromatic isometric copy of X.
  *Proof:* (immediate from Theorem 4.1)