<!-- Generated 2026-05-31T03:12:58 -->
<!-- Source PDF: diestel__graph_theory.pdf (2942933 bytes) -->
<!-- Citation: Diestel, R. (2017). Graph Theory. Springer. -->

# Graph Theory, Diestel (2017)

## Definitions

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 1.2.1.** The number of vertices of odd degree in a graph is always even.
  *Proof:* Concludes algebraically using the fact that the sum of all vertex degrees is exactly twice the number of edges.

- **Proposition 1.2.2.** Every graph G with at least one edge has a subgraph H with δ(H) > ε(H) ⩾ ε(G).
  *Proof:* Iteratively deletes vertices of degree at most the average degree, avoiding triviality. Concludes the remaining subgraph possesses a strictly greater minimum degree.

- **Proposition 1.3.1.** Every graph G contains a path of length δ(G) and a cycle of length at least δ(G) + 1 (provided that δ(G) ⩾ 2).
  *Proof:* Extracts a longest path and links its endpoint to its earliest neighbor on the path.

- **Proposition 1.3.2.** Every graph G containing a cycle satisﬁes g(G) ⩽ 2 diam(G) + 1.
  *Proof:* Uses contradiction to show that two vertices too far apart on a cycle would yield a shorter cycle via their shortest path.

- **Proposition 1.3.3.** A graph G of radius at most k and maximum degree at most d ⩾ 3 has fewer than d−2
                              d
                                 (d − 1)k vertices.
  *Proof:* Sums the maximum possible number of vertices in each distance layer from a central vertex.

- **Theorem 1.3.4. (Alon, Hoory & Linial 2002)** Let G be a graph. If d(G) ⩾ d ⩾ 2 and g(G) ⩾ g ∈ N then |G| ⩾ n0 (d, g).
  *Proof:* (no proof in this paper)

- **Corollary 1.3.5.** If δ(G) ⩾ 3 then g(G) < 2 log |G|.
  *Proof:* Computes the lower bound directly from the evaluated function provided in the previous theorem.

- **Proposition 1.4.1.** The vertices of a connected graph G can always be enumerated, say as v1 , . . . , vn , so that Gi := G[v1 , . . . , vi ] is connected for every i.
  *Proof:* Appends vertices iteratively using paths that connect unvisited vertices to the already connected component.

- **Proposition 1.4.2.** If G is non-trivial then κ(G) ⩽ λ(G) ⩽ δ(G).
  *Proof:* Analyzes a minimal edge cut and bounds the connectivity degree depending on whether all vertices are incident with the cut. Uses neighbor counts to bound the remaining component sizes.

- **Theorem 1.4.3. (Mader 1972)** Let 0  = k ∈ N. Every graph G with d(G) ⩾ 4k has a (k + 1)-connected subgraph H such that ε(H) > ε(G) − k.
  *Proof:* Selects a minimal subgraph satisfying the average degree density and confirms its minimum degree. Argues by contradiction that any small separation would violate the strict edge-density condition.

- **Theorem 1.5.1.** The following assertions are equivalent for a graph T :
               (i) T is a tree;
               (ii) Any two vertices of T are linked by a unique path in T ;
           (iii) T is minimally connected, i.e. T is connected but T − e is disconnected for every edge e ∈ T ;
           (iv) T is maximally acyclic, i.e. T contains no cycle but T + xy does, for any two non-adjacent vertices x, y ∈ T .
  *Proof:* (no proof in this paper)

- **Corollary 1.5.2.** The vertices of a tree can always be enumerated, say as v1 , . . . , vn , so that every vi with i ⩾ 2 has a unique neighbour in {v1 , . . . , vi−1 }.
  *Proof:* (immediate from Proposition 1.4.1)

- **Corollary 1.5.3.** A connected graph with n vertices is a tree if and only if it has n − 1 edges.
  *Proof:* Uses inductive accumulation along the spanning tree's vertex enumeration to pair exactly one edge per new vertex.

- **Corollary 1.5.4.** If T is a tree and G is any graph with δ(G) ⩾ |T | − 1, then T ⊆ G, i.e. G has a subgraph isomorphic to T .
  *Proof:* (immediate from Corollary 1.5.2)

- **Lemma 1.5.5.** Let T be a normal tree in G.
               (i) Any two vertices x, y ∈ T are separated in G by the set  x  ∩  y .
               (ii) If S ⊆ V (T ) = V (G) and S is down-closed, then the components of G − S are spanned by the sets  x  with x minimal in T − S.
  *Proof:* Analyzes the minimal sequence of tree-order comparable path vertices to prove intersection separation. Extends this to show that components are spanned by elements above the minimal non-spanned elements.

- **Proposition 1.5.6.** Every connected graph contains a normal spanning tree, with any speciﬁed vertex as its root.
  *Proof:* Assumes a maximal normal tree doesn't span the graph and derives a contradiction. Shows that attaching a neighboring component vertex extends the tree's normal ordering structure.

- **Proposition 1.6.1.** A graph is bipartite if and only if it contains no odd cycle.
  *Proof:* Constructs a bipartition based on the odd/even distances from a root vertex in a spanning tree. Shows that any non-tree edge forms an even cycle and preserves the alternation.

- **Proposition 1.7.1.** The minor relation   and the topological-minor relation are partial orderings on the class of ﬁnite graphs, i.e. they are reﬂexive, antisymmetric and transitive.
  *Proof:* (no proof in this paper)

- **Corollary 1.7.2.** Let X and Y be ﬁnite graphs. X is a minor of Y if and only if there are graphs G0 , . . . , Gn such that G0 = Y and Gn = X and each Gi+1 arises from Gi by deleting an edge, contracting an edge, or deleting a vertex.
  *Proof:* Follows trivially by applying induction on the order of the graph.

- **Proposition 1.7.3.**
   (i) Every T X is also an IX (Fig. 1.7.4); thus, every topological minor of a graph is also its (ordinary) minor.
  (ii) If Δ(X) ⩽ 3, then every IX contains a T X; thus, every minor with maximum degree at most 3 of a graph is also its topological minor.
  *Proof:* (no proof in this paper)

- **Theorem 1.8.1. (Euler 1736)** A connected graph is Eulerian if and only if every vertex has even degree.
  *Proof:* Extracts a maximal closed walk and applies induction to the connected components of the remaining edges. Concatenates the returning Euler tours to form a contradiction.

- **Proposition 1.9.1.** The following assertions are equivalent for edge sets D ⊆ E:
                 (i) D ∈ C(G);
                (ii) D is a (possibly empty) disjoint union of edge sets of cycles in G;
               (iii) All vertex degrees of the graph (V, D) are even.
  *Proof:* Applies induction on the number of cycles to establish even degrees and inductively decomposes the edge set into sub-cycles.

- **Proposition 1.9.2.** Together with ∅, the cuts in G form a subspace B = B(G) of E(G). This space is generated by cuts of the form E(v).
  *Proof:* Verifies that every cut can be represented as a symmetric difference of fundamental vertex cuts.

- **Lemma 1.9.3.** Every cut is a disjoint union of bonds.
  *Proof:* Applies induction on the cut's size to recursively subtract enclosed non-empty bonds until only disjoint bonds remain.

- **Theorem 1.9.4.** The cycle space C and the cut space B of any graph satisfy C = B⊥ and B = C ⊥ .
  *Proof:* Proves mutual orthogonality by noting that cycles intersect cuts in an even number of edges. Establishes completeness by contracting non-cut edges into a bipartite multigraph mapping back to the cut space.

- **Theorem 1.9.5.** Let G be a connected graph with n vertices and m edges, and let T ⊆ G a spanning tree.
                 (i) The fundamental cuts and cycles of G with respect to T form bases of B(G) and C(G), respectively.
                 (ii) Hence, dim B(G) = n − 1 and dim C(G) = m − n + 1.
  *Proof:* Demonstrates that fundamental cuts and cycles are linearly independent because each contains a unique generating edge. Sums the bases to reconstruct any general cycle or cut respectively.

- **Proposition 1.9.6.**
   (i) The kernel of B is C(G).
  (ii) The image of B t is B(G).
  *Proof:* (no proof in this paper)

- **Proposition 1.9.7.** BB t = A + D.
  *Proof:* (no proof in this paper)

- **Theorem 2.1.1. (König 1931)** The maximum cardinality of a matching in G is equal to the minimum cardinality of a vertex cover of its edges.
  *Proof:* Assigns a vertex cover by selecting endpoints of a maximum matching based on their reachability via alternating paths. Verifies the cover includes exactly the matching size and covers all edges without augmenting paths.

- **Theorem 2.1.2. (Hall 1935)** G contains a matching of A if and only if |N (S)| ⩾ |S| for all S ⊆ A.
  *Proof:* Provides three independent proofs based on extending alternating paths, inducting on the bipartite sets, and reducing to an edge-minimal subgraph satisfying the condition.

- **Corollary 2.1.3.** Every k-regular (k ⩾ 1) bipartite graph has a 1-factor.
  *Proof:* Directly verifies that the marriage condition holds because subsets project at least an equal number of edges onto their neighborhood.

- **Theorem 2.1.4. (Gale & Shapley 1962)** For every set of preferences, G has a stable matching.
  *Proof:* Iteratively improves matchings to strictly increase happiness based on vertex preferences. Concludes with a stable matching when no unmatched vertex is acceptable to its neighbors.

- **Corollary 2.1.5. (Petersen 1891)** Every regular graph of positive even degree has a 2-factor.
  *Proof:* Splits vertices along an Euler tour to construct a regular bipartite graph, then applies the 1-factor theorem.

- **Theorem 2.2.1. (Tutte 1947)** A graph G has a 1-factor if and only if q(G − S) ⩽ |S| for all S ⊆ V (G).
  *Proof:* Assumes the graph is edge-maximal without a 1-factor and analyzes alternating paths between maximum disconnected subsets. Identifies a specific configuration violating Tutte's condition.

- **Corollary 2.2.2. (Petersen 1891)** Every bridgeless cubic graph has a 1-factor.
  *Proof:* Demonstrates that the sum of odd degrees in any odd component forces enough crossing edges to automatically satisfy Tutte's condition.

- **Theorem 2.2.3.** Every graph G = (V, E) contains a vertex set S with the following two properties:
   (i) S is matchable to CG−S ;
  (ii) Every component of G − S is factor-critical.
Given any such set S, the graph G contains a 1-factor if and only if |S| = |CG−S |.
  *Proof:* Applies induction on the graph's size and selects a maximally violating subset for Tutte's condition. Argues that components outside this set are factor-critical and that the set matches into them perfectly.

- **Lemma 2.3.1.** Let k ∈ N, and let H be a cubic multigraph. If |H| ⩾ sk , then H contains k disjoint cycles.
  *Proof:* Inducts on the number of cycles by removing the shortest cycle and suppressing degree-2 vertices. Uses bounds on the remaining multigraph's size to recursively guarantee the required disjoint cycles.

- **Theorem 2.3.2. (Erdős & Pósa 1965)** There is a function f : N → N such that, given any k ∈ N, every graph contains either k disjoint cycles or a set of at most f (k) vertices meeting all its cycles.
  *Proof:* Extracts a maximal subgraph with bounded degrees and bounds the number of disjoint cycles inside it. Augments intersecting elements into a minimal covering set for all cycles.

- **Theorem 2.4.1. (Nash-Williams 1961; Tutte 1961)** A multigraph contains k edge-disjoint spanning trees if and only if for every partition P of its vertex set it has at least k (|P | − 1) cross-edges.
  *Proof:* Derives the tree packing by combining the components' internal edge-disjoint trees with those covering the quotient partition.

- **Corollary 2.4.2.** Every 2k-edge-connected multigraph G has k edge-disjoint spanning trees.
  *Proof:* Bounds the minimum number of cross-edges using the edge-connectivity and strictly applies the tree packing theorem.

- **Theorem 2.4.3. (Nash-Williams 1964)** The edges of a multigraph G = (V, E) can be covered by at most k trees if and only if G[U ] ⩽ k (|U | − 1) for every non-empty set U ⊆ V .
  *Proof:* Derives the tree covering by merging the components' internal tree covers with the quotient's spanning trees.

- **Theorem 2.4.4. (Bowler & Carmesin 2015)** For every connected multigraph G = (V, E) and every k ∈ N there is a partition P of V such that every G[U ] with U ∈ P has k edge-disjoint spanning trees and the edges of G/P can be covered by k spanning trees.
  *Proof:* Uses edges of a maximal exchange chain forest to group components into a minimal spanning partition. Proves the internal subsets strictly preserve connectivity and spanning paths without overlaps.

- **Lemma 2.4.5.** If e0 starts an exchange chain for T and lies in two of its trees, then there is a family T   of k spanning trees of G such that E(T )   E(T   ).
  *Proof:* Identifies a minimal length exchange chain to modify a sequence of spanning trees. Proves that substituting the chain's edges maintains all fundamental cycles and strictly increases the total tree edges.

- **Theorem 2.5.1. (Gallai & Milgram 1960)** Every directed graph G has a path cover P and an independent set { vP | P ∈ P } of vertices such that vP ∈ P for every P ∈ P.
  *Proof:* Applies induction on the graph's size and modifies the paths terminating at a minimal set of endpoints. Substitutes path tails to maintain a valid disjoint cover while avoiding cycle contradictions.

- **Corollary 2.5.2. (Dilworth 1950)** In every ﬁnite partially ordered set (P, ⩽), the minimum number of chains with union P is equal to the maximum cardinality of an antichain in P .
  *Proof:* Translates the order relation into a directed graph and directly extracts the equivalence via the path cover theorem.

- **Proposition 3.1.1.** A graph is 2-connected if and only if it can be constructed from a cycle by successively adding H-paths to graphs H already constructed (Fig. 3.1.1).
  *Proof:* Constructs the graph inductively by appending paths and proving any maximal such subgraph must encompass the entire graph.

- **Lemma 3.1.2.** Let G be any graph.
           (i) The cycles of G are precisely the cycles of its blocks.
          (ii) The bonds of G are precisely the minimal cuts of its blocks.
  *Proof:* Shows that paths connecting vertices of any cycle must remain inside their maximal block. Applies this boundary property equivalently to minimal edge cuts.

- **Lemma 3.1.3.** The following statements are equivalent for distinct edges e, f of a graph G:
    (i) The edges e, f belong to a common block of G.
   (ii) The edges e, f belong to a common cycle in G.
  (iii) The edges e, f belong to a common bond of G.
  *Proof:* Uses inductive disjoint path constructions to link blocks to cycles, and cycles to edge cuts. Ties the minimal cuts directly back to block definitions.

- **Lemma 3.1.4.** The block graph of a connected graph is a tree.
  *Proof:* (no proof in this paper)

- **Lemma 3.2.1.** Let e be an edge in a graph G. If G −    . e is 3-connected, then so is G.
  *Proof:* Verifies that any resulting separator of the suppressed graph would directly correspond to a valid separator in the original graph.

- **Lemma 3.2.2.** Every 3-connected graph G  = K 4 has an edge e such that G −       . e is another 3-connected graph.
  *Proof:* Chooses a maximal topological minor and identifies a path outside its structure that avoids specific parallel edges. Proves that suppressing this path yields another valid 3-connected graph.

- **Theorem 3.2.3. (Tutte 1966)** A graph G is 3-connected if and only if there exists a sequence G0 , . . . , Gn of graphs such that
   (i) G0 = K 4 and Gn = G;
  (ii) Gi+1 has an edge e such that Gi = Gi+1 − . e, for every i < n.
Moreover, the graphs in any such sequence are all 3-connected.
  *Proof:* Recursively applies the previous edge-suppressing lemma to iteratively shrink the graph down to a complete graph on four vertices.

- **Lemma 3.2.4.** Every 3-connected graph G  = K 4 has an edge e such that G/e is again 3-connected.
  *Proof:* Assumes no edge contraction maintains 3-connectedness and derives a contradiction by analyzing the minimal components of the resulting separators. Asserts that the vertices would separate smaller subgraphs.

- **Theorem 3.2.5. (Tutte 1961)** A graph G is 3-connected if and only if there exists a sequence G0 , . . . , Gn of graphs with the following two properties:
               (i) G0 = K 4 and Gn = G;
               (ii) Gi+1 has an edge xy such that d(x), d(y) ⩾ 3 and Gi = Gi+1 /xy, for every i < n.
Moreover, the graphs in any such sequence are all 3-connected.
  *Proof:* Iteratively applies the previous contraction lemma to build sequences down to K4. Checks that the minimal degree limits strictly prevent separators from shrinking component connectivity.

- **Theorem 3.2.6. (Tutte 1963)** The cycle space of a 3-connected graph is generated by its non-separating induced cycles.
  *Proof:* Proceeds by induction on the size of the largest component isolated outside the cycle. Recursively decomposes any spanning or separating cycle into overlapping smaller non-separating cycles.

- **Theorem 3.3.1. (Menger 1927)** Let G = (V, E) be a graph and A, B ⊆ V . Then the minimum number of vertices separating A from B in G is equal to the maximum number of disjoint A–B paths in G.
  *Proof:* Presents three separate proofs using induction on graph size, induction on the path system limits, and alternating walks. Establishes the equivalence between minimal vertex separators and maximal disjoint paths.

- **Lemma 3.3.2.** If an alternating walk W as above ends in B   V [P], then G contains a set of disjoint A–B paths exceeding P.
  *Proof:* Examines the symmetric difference of the current path system and an alternating walk. Constructs a strictly larger disjoint path system by flipping the matched path segments.

- **Lemma 3.3.3.** If no alternating walk W as above ends in B   V [P], then G contains an A–B separator on P.
  *Proof:* Constructs a strict separator by selecting the furthest vertices reachable by alternating walks. Proves that any alternative connecting path must cross this exact vertex boundary.

- **Corollary 3.3.4.** For B ⊆ V and a ∈ V   B, the minimum number of vertices separating a from B in G is equal to the maximum number of paths forming an a–B fan in G.
  *Proof:* (immediate from Theorem 3.3.1)

- **Corollary 3.3.5.** Let a and b be two distinct vertices of G.
   (i) If ab ∈/ E, then the minimum number of vertices separating a from b in G is equal to the maximum number of independent a–b paths in G.
  (ii) The minimum number of edges separating a from b in G is equal to the maximum number of edge-disjoint a–b paths in G.
  *Proof:* (immediate from Theorem 3.3.1)

- **Theorem 3.3.6. (Global Version of Menger’s Theorem)**
            (i) A graph is k-connected if and only if it contains k independent paths between any two vertices.
               (ii) A graph is k-edge-connected if and only if it contains k edge-disjoint paths between any two vertices.
  *Proof:* Evaluates the local minimum separators across every pair of vertices. Ties the independent and edge-disjoint path bounds globally to the formal vertex/edge-connectivity limits.

- **Theorem 3.4.1. (Mader 1978)** Given a graph G with an induced subgraph H, there are always MH (G) independent H-paths in G.
  *Proof:* (no proof in this paper)

- **Corollary 3.4.2.** Given a graph G with an induced subgraph H, there are at least 12 κH (G) independent H-paths and at least 12 λH (G) edge-disjoint H-paths in G.
  *Proof:* Re-indexes Mader's vertex and edge separator definitions. Explicitly assigns fractional boundary sizes to prove the worst-case bound guarantees at least half the optimal number of disjoint paths.