<!-- Generated 2026-05-31T01:44:37 -->
<!-- Source PDF: bapat__graphs_and_matrices.pdf (3742017 bytes) -->
<!-- Citation: R. B. Bapat (2010). Graphs and Matrices. Springer Universitext. -->

```markdown
# Graphs and Matrices (R. B. Bapat, 2010)

## Definitions

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 2.2.** If G is a connected graph on n vertices, then rank Q(G) = n − 1.
  *Proof:* Argues the left null space of the incidence matrix is one-dimensional since all components of a null vector must be equal.
- **Theorem 2.3.** If G is a graph on n vertices and has k connected components then rank Q(G) = n − k.
  *Proof:* Sums the ranks of the disjoint block incidence matrices corresponding to the connected components.
- **Lemma 2.4.** Let G be a connected graph on n vertices. Then the column space of Q(G) consists of all vectors x ∈ IRn such that i xi = 0.
  *Proof:* Shows the column space is a subspace of the zero-sum vectors and matches its dimension.
- **Lemma 2.5.** Let G be a graph on n vertices. Columns j1 , . . . , jk of Q(G) are linearly independent if and only if the corresponding edges of G induce an acyclic graph.
  *Proof:* Relates linear dependence to singular cycle submatrices and independence to the rank of acyclic forests.
- **Lemma 2.6.** Let G be a graph with incidence matrix Q(G). Then Q(G) is totally unimodular.
  *Proof:* Inductively expands the determinant along a column with at most one non-zero entry.
- **Lemma 2.7.** Let G be a tree on n vertices. Then any submatrix of Q(G) of order n − 1 is nonsingular.
  *Proof:* Demonstrates that all such submatrices have determinants of equal magnitude and the overall matrix rank is n-1.
- **Lemma 2.8.** Let A be an n × n matrix and suppose A has a zero submatrix of order p × q where p + q ≥ n + 1. Then det A = 0.
  *Proof:* Evaluates the determinant via Laplace expansion along the zero block.
- **Theorem 2.10.** Let G be a tree with the vertex set {1, 2, . . . , n}. Let Q be the incidence matrix of G and let Q n be the reduced incidence matrix obtained by deleting row n of Q. Then Q −1 n = Pn .
  *Proof:* Directly multiplies the path matrix and incidence matrix elements to verify they yield the identity.
- **Lemma 2.11.** Let A be an n × n integer matrix. Then A is nonsingular and admits an integer inverse if and only if A is unimodular.
  *Proof:* Uses the adjoint matrix representation of the inverse to show the determinant must be ±1.
- **Theorem 2.12.** Let A be an m × n integer matrix. Then there exist unimodular matrices S and T of order m × m and n × n, respectively, such that diag(z 1 , . . . , zr ) 0 S AT = , 0 0 where z 1 , . . . , zr are positive integers (called the invariant factors of A) such that z i divides z i+1 , i = 1, 2, . . . , r − 1. Furthermore, z 1 . . . z i = di , where di is the greatest common divisor of all i × i minors of A, i = 1, . . . , min{m, n}.
  *Proof:* (no proof in this paper)
- **Theorem 2.13.** Let G be a graph with vertex set V (G) = {1, 2, . . . , n} and edge set {e1 , . . . , em }. Suppose the edges e1 , . . . , en−1 form a spanning tree of G. Let Q 1 be the submatrix of Q formed by the rows 1, . . . , n − 1 and the columns e1 , . . . , en−1 . Let q = m − n + 1. Partition Q as follows: Q1 Q1 N Q= . −1 Q 1 −1 Q 1 N Set Q −1 1 0 , B= 0 0 Q −1 1 0 , T = In−1 −N , S= 1 1 0 Iq Q1 F= , H = In−1 N . −1 Q 1 Then the following assertions hold: (i) B is an integer reflexive g-inverse of Q. (ii) S and T are unimodular matrices. In−1 0 (iii) S QT = is the Smith normal form of Q. 0 0 (iv) Q = F H is an integer rank factorization of Q.
  *Proof:* (no proof in this paper)
- **Lemma 2.14.** If A is an m × n matrix, then for an n × 1 vector x, Ax = 0 if and only if x A+ = 0.
  *Proof:* Uses properties of symmetric matrix products and the definition of the Moore-Penrose pseudo-inverse.
- **Lemma 2.15.** If G is connected, then I − Q Q + = n1 J.
  *Proof:* Identifies the rows of the idempotent matrix I - QQ+ as spanning the one-dimensional left null space of Q.
- **Lemma 2.16.** Let Cn be the cycle on the vertices {1, . . . , n}, n ≥ 3, and let M be its incidence matrix. Then det M equals 0 if n is even and 2 if n is odd.
  *Proof:* (no proof in this paper)
- **Lemma 2.17.** Let G be a connected graph with n vertices and let M be the incidence matrix of G. Then the rank of M is n − 1 if G is bipartite and n otherwise.
  *Proof:* Analyzes the left null space of M, showing a non-zero vector exists if and only if the graph lacks odd cycles.
- **Lemma 2.18.** Let G be a graph and let R be a substructure of G with an equal number of vertices and edges. Let N be the incidence matrix of R. Then N is nonsingular if and only if R is a vertex-disjoint union of rootless trees and unicyclic graphs with the cycle being odd.
  *Proof:* (no proof in this paper)
- **Lemma 2.19.** Let G be a bipartite graph. Then the 0–1 incidence matrix M of G is totally unimodular.
  *Proof:* Proceeds by induction on submatrix size, matching column sums for bipartite partitions to identify singular cases.
- **Lemma 2.20.** Let G be a bipartite graph with incidence matrix M. Then there exists a 0–1 vector z which is a solution of (2.1).
  *Proof:* Deduces the existence of an integral basic feasible solution due to the total unimodularity of M.
- **Lemma 2.21.** Let G be a bipartite graph with the incidence matrix M. Then there exists a 0–1 vector z which is a solution of (2.2).
  *Proof:* (no proof in this paper)
- **Theorem 2.22.** If G is a bipartite graph then ν(G) = τ (G).
  *Proof:* Applies the linear programming duality theorem to the matching and vertex cover incidence matrices.
- **Lemma 3.2.** Let G be a connected graph with vertices {1, . . . , n} and let A be the adjacency matrix of G. If i, j are vertices of G with d(i, j) = m, then the matrices I, A, . . . , Am are linearly independent.
  *Proof:* Examines the first non-zero entry at position (i,j) which corresponds to the length of the shortest path.
- **Corollary 3.3.** Let G be a connected graph with k distinct eigenvalues and let d be the diameter of G. Then k > d.
  *Proof:* Compares the linear independence of matrix powers against the degree of the minimal polynomial.
- **Theorem 3.4.** (i) For any positive integer n, the eigenvalues of K n are n − 1 with multiplicity 1 and −1 with multiplicity n − 1. (ii) For any positive integers p, q, the √ √ eigenvalues of K p,q are pq, − pq and 0 with multiplicity p + q − 2.
  *Proof:* Solves for the spectrum by recognizing complete graphs as permutations of the all-ones matrix J and block forms.
- **Lemma 3.5.** For n ≥ 2, the eigenvalues of Q n are 1, ω, ω2 , . . . , ωn−1 , where 2πi ω = e n , is the primitive nth root of unity.
  *Proof:* Extracts the complex roots from the factored characteristic polynomial of the permutation matrix.
- **Theorem 3.6.** For n ≥ 2, the eigenvalues of Cn are 2 cos 2πn k , k = 1, . . . , n.
  *Proof:* Expresses the adjacency matrix of a cycle as a sum of permutation matrices and evaluates at their roots.
- **Theorem 3.7.** For n ≥ 1, the eigenvalues of Pn are 2 cos πk n+1 , k = 1, . . . , n.
  *Proof:* Embeds the path graph eigenvectors symmetrically into extended cycle graph eigenvectors to derive the spectrum.
- **Theorem 3.8.** Let G be a graph with V (G) = {1, . . . , n} and let A be the adjacency matrix of G. Then det A = (−1)n−c1 (H )−c(H ) 2c(H ) , where the summation is over all spanning elementary subgraphs H of G.
  *Proof:* Expands the determinant using permutation signatures, recognizing cycle decompositions correspond to elementary subgraphs.
- **Theorem 3.10.** Let G be a graph with vertices {1, . . . , n} and let A be the adjacency matrix of G. Let φλ (A) = det(λI − A) = λn + c1 λn−1 + · · · + cn be the characteristic polynomial of A. Then ck = (−1)c1 (H )+c(H ) 2c(H ) , where the summation is over all the elementary subgraphs H of G with k vertices, k = 1, . . . , n.
  *Proof:* Equates characteristic polynomial coefficients to principal minors evaluated via spanning elementary subgraphs.
- **Corollary 3.11.** Let G be a graph with vertices {1, . . . , n} and let A be the adjacency matrix of G. Let φλ (A) = det(λI − A) = λn + c1 λn−1 + · · · + cn be the characteristic polynomial of A. Suppose c3 = c5 = · · · = c2k−1 = 0. Then G has no odd cycle of length i, 3 ≤ i ≤ 2k − 1. Furthermore, the number of (2k + 1)-cycles in G is − 21 c2k+1 .
  *Proof:* Inductively eliminates smaller elementary subgraphs to isolate the count of minimum odd cycles.
- **Corollary 3.12.** Using the notation of Corollary 3.11, if c2k+1 = 0, k = 0, 1, . . . , then G is bipartite.
  *Proof:* (immediate from Corollary 3.11)
- **Lemma 3.13.** Let G be a bipartite graph with adjacency matrix A. If λ is an eigenvalue of A with multiplicity k, then −λ is also an eigenvalue of A with multiplicity k.
  *Proof:* Negates specific block components of the eigenvectors due to the bipartite adjacency structure.
- **Theorem 3.14.** Let G be a graph with vertices {1, . . . , n} and let A be the adjacency matrix of G. Then the following conditions are equivalent. (i) G is bipartite; (ii) if φλ (A) = λn + c1 λn−1 + · · · + cn is the characteristic polynomial of A, then c2k+1 = 0, k = 0, 1, . . .; (iii) the eigenvalues of A are symmetric with respect to the origin, i.e., if λ is an eigenvalue of A with multiplicity k, then −λ is also an eigenvalue of A with multiplicity k.
  *Proof:* Combines eigenvalue symmetry, characteristic polynomial constraints on odd cycles, and bipartite graph properties.
- **Theorem 3.15.** Let G be a graph with n vertices, m edges and let λ1 ≥ · · · ≥ λn be 1 the eigenvalues of G. Then λ1 ≤ ( 2m(n−1) n )2 .
  *Proof:* Applies the Cauchy-Schwarz inequality against the sum of squared eigenvalues which equals 2m.
- **Lemma 3.16.** Let G be a graph with n vertices and let H be an induced subgraph of G with p vertices. Then λ1 (G) ≥ λ1 (H ) and λn (G) ≤ λ p (H ).
  *Proof:* Applies Cauchy's interlacing inequalities relating the eigenvalues of symmetric matrices and principal submatrices.
- **Lemma 3.17.** For a graph G, δ(G) ≤ λ1 (G) ≤ Δ(G).
  *Proof:* Uses the maximal coordinate of the eigenvector to bound the degree from above and the Rayleigh quotient for the lower bound.
- **Theorem 3.18.** For any graph G, χ (G) ≤ 1 + λ1 (G).
  *Proof:* Examines a vertex-minimal induced subgraph requiring the full chromatic number and bounds its minimum degree.
- **Lemma 3.19.** If B and C are symmetric n × n matrices, then λ1 (B + C) ≤ λ1 (B) + λ1 (C).
  *Proof:* Uses the extremal representation of eigenvalues to bound the maximum of the sum's Rayleigh quotient.
- **Lemma 3.20.** Let B be an n × n positive semidefinite matrix and suppose B is partitioned as B11 B12 B= , B21 B22 where B11 is p × p. Then λ1 (B) ≤ λ1 (B11 ) + λ1 (B22 ).
  *Proof:* Expresses the partitioned positive semidefinite matrix as a product and applies the spectral radius sum bound.
- **Lemma 3.21.** Let B be an n × n symmetric matrix and suppose B is partitioned as B11 B12 B= , B21 B22 where B11 is p × p. Then λ1 (B) + λn (B) ≤ λ1 (B11 ) + λ1 (B22 ).
  *Proof:* Applies positive semidefinite spectral bounds to the block-partitioned shifted matrix B minus its minimal eigenvalue.
- **Lemma 3.22.** Let B be a symmetric matrix partitioned as ⎡ ⎤ 0 B12 · · · B1k ⎢ B21 0 · · · B2k ⎥ ⎢ ⎥ B=⎢ . .. . . . ⎥ . ⎣ .. . . .. ⎦ Bk1 Bk2 · · · 0 Then λ1 (B) + (k − 1)λn (B) ≤ 0.
  *Proof:* Proceeds by induction on the block count, continually applying block separation and tracking minimum eigenvalues.
- **Theorem 3.23.** Let G be a graph with n vertices and with at least one edge. Then λ1 (G) χ (G) ≥ 1 − . λn (G)
  *Proof:* Partitions the adjacency matrix according to proper color classes and invokes the zero-diagonal block eigenvalue bound.
- **Lemma 3.24.** Let A and B be symmetric matrices of order m × m and n × n, respectively. If λ1 , . . . , λm and μ1 , . . . , μn are the eigenvalues of A and B, respectively, then the eigenvalues of A⊗ In + Im ⊗ B are given by λi +μ j ; i = 1, . . . , m; j = 1, . . . , n.
  *Proof:* Diagonalizes A and B simultaneously with orthogonal matrices to map the Kronecker sum spectrum.
- **Lemma 3.25.** Let A and B be symmetric matrices of order m × m and n × n, respectively. If λ1 , . . . , λm and μ1 , . . . , μn are the eigenvalues of A and B, respectively, then the eigenvalues of A⊗ B are given by λi μ j ; i = 1, . . . , m; j = 1, . . . , n.
  *Proof:* (no proof in this paper)
- **Lemma 3.26.** Let G and H be graphs with m and n vertices, respectively. If λ1 , . . . , λm and μ1 , . . . , μn are the eigenvalues of G and H, respectively, then the eigenvalues of G × H are given by λi + μ j , i = 1, . . . , m; j = 1, . . . , n.
  *Proof:* (immediate from Lemma 3.24)
- **Theorem 3.27.** Let G be a graph with n vertices. If the energy ε(G) of G is a rational number then it must be an even integer.
  *Proof:* Concludes the sum of positive eigenvalues must be a rational integer root of the Kronecker characteristic polynomial.
- **Lemma 3.28.** Let B be a 0 − 1 n × n matrix such that bi j = 1 if i ≥ j. Then det B equals 1 if b12 = b23 = · · · = bn−1n = 0; otherwise det B = 0.
  *Proof:* Evaluates the upper triangular determinant inductively by subtracting adjacent columns.
- **Corollary 3.29.** Let G be a directed, acyclic graph with V (G) = {1, . . . , n}. Let B be the antiadjacency matrix of G. Then det B = 1 if G has a Hamiltonian path, and det B = 0, otherwise.
  *Proof:* Translates the directed acyclic topology into upper triangular matrix zero-conditions evaluated by Lemma 3.28.
- **Theorem 3.30.** Let G be a directed, acyclic graph with V (G) = {1, . . . , n}. Let B be the antiadjacency matrix of G, and let n det(x B + I ) = ci x i . i=0 Then c0 = 1 and ci equals the number of directed paths of i vertices in G, i = 1, . . . , n.
  *Proof:* Sums non-singular principal minors which indicate the existence of Hamiltonian paths in vertex subsets.
- **Lemma 3.32.** Let T be a tree with V (T ) = {1, . . . , n}, and let A be the adjacency matrix of T. Then A is nonsingular if and only if T has a perfect matching.
  *Proof:* Checks non-zero permutation determinant terms which exclusively require the existence of a unique perfect matching.
- **Theorem 3.33.** Let T be a nonsingular tree with V (T ) = {1, . . . , n} and let A be the adjacency matrix of T. Let M be the perfect matching in T. Let B = [bi j ] be the n × n matrix defined as follows: bi j = 0 if i = j or if P(i, j) is not alternating. If P(i, j) is alternating, then set d(i, j)−1 bi j = (−1) 2 . Then B = A−1 .
  *Proof:* Confirms the inverse by computing the matrix product through alternating path parity and distance cancellations.
- **Theorem 3.34.** Let T be a nonsingular tree with V (T ) = {1, . . . , n} and let A be the adjacency matrix of T. Then there exists a signature matrix F such that F A−1 F is the adjacency matrix of a graph.
  *Proof:* Employs a diagonal matrix tracking alternating path parity to map all non-zero inverse elements to positive ones.
- **Lemma 3.36.** Let T be a nonsingular tree with V (T ) = {1, . . . , n}. Then T −1 is a connected graph.
  *Proof:* Deduces structural connectedness from the fact that a disconnected inverse would imply a disconnected tree.
- **Corollary 3.37.** Let T be a nonsingular tree with V (T ) = {1, . . . , n}. Then the number of alternating paths in T, which equals the number of edges in T −1 , is at least n − 1.
  *Proof:* (immediate from Lemma 3.36)
- **Theorem 3.38.** Let T be a nonsingular tree with V (T ) = {1, . . . , 2n}. Then the following conditions are equivalent: (i) the number of alternating paths in T has the minimum possible value 2n − 1; (ii) T −1 is a tree; (iii) T is a corona tree; (iv) T −1 is isomorphic to T.
  *Proof:* Cyclically proves equivalences using edge counts, constraints on perfect matching endpoints, and block matrix inverses.
- **Lemma 4.2.** Let X be an n × n matrix with zero row and column sums. Then the cofactors of any two elements of X are equal.
  *Proof:* Normalizes columns and applies zero-sum symmetries to equate off-diagonal and principal minors.
- **Lemma 4.3.** Let G be a graph with V (G) = {1, . . . , n} and E(G) = {e1 , . . . , em }. Then the following assertions hold. (i) L(G) is a symmetric, positive semidefinite matrix. (ii) The rank of L(G) equals n − k, where k is the number of connected components of G. (iii) For any vector x, x L(G)x = i∼j (xi − xj )2 . (iv) The row and the column sums of L(G) are zero. (v) The cofactors of any two elements of L(G) are equal.
  *Proof:* Derives algebraic structure, quadratic forms, and cofactors directly from the Laplacian factorization into incidence matrices.
- **Lemma 4.4.** The eigenvalues of the n × n matrix aI + bJ are a with multiplicity n − 1, and a + nb with multiplicity 1.
  *Proof:* Shifts the known single-rank spectrum of the all-ones matrix by scalar multiplication and identity addition.
- **Lemma 4.5.** Let G be a graph with V (G) = {1, 2, . . . , n}. Let the eigenvalues of L(G) be λ1 ≥ · · · ≥ λn−1 ≥ λn = 0. Then the eigenvalues of L + aJ are λ1 ≥ · · · ≥ λn−1 and na.
  *Proof:* Decomposes the spectrum via an orthogonal matrix that isolates the all-ones eigenvector of the graph Laplacian.
- **Lemma 4.6.** Let G be the graph obtained by removing p disjoint edges from Kn , n ≥ 2p. Then the eigenvalues of L(G) are n − 2 with multiplicity p, n with multiplicity n − p − 1, and 0 with multiplicity 1.
  *Proof:* Evaluates the block diagonal modifications introduced to the complete graph Laplacian and shifts via Lemma 4.5.
- **Theorem 4.7.** Let G be a graph with V (G) = {1, 2, . . . , n}. Let W be a nonempty proper subset of V (G). Then the determinant of L(W |W ) equals the number of spanning forests of G with |W | components in which each component contains one vertex of W .
  *Proof:* Utilizes the Cauchy-Binet expansion of incidence matrices to enumerate non-singular rootless forest submatrices.
- **Theorem 4.8.** Let G be a graph with V (G) = {1, 2, . . . , n}. Then the cofactor of any element of L(G) equals the number of spanning trees of G.
  *Proof:* Applies the forest determinant counting specifically to a single omitted vertex to enumerate connected spanning trees.
- **Lemma 4.9.** The eigenvalues of L(Cn ) are 2 − 2 cos 2πn j , j = 1, . . . , n.
  *Proof:* (immediate from Theorem 3.6)
- **Corollary 4.10.** Let G be a tree with V (G) = {1, 2, . . . , n}. Let i, j be distinct vertices of G and suppose that the unique path between i and j has length . Then det L(i, j|i, j) = .
  *Proof:* (immediate from Theorem 4.7)
- **Theorem 4.11.** Let G be a graph with V (G) = {1, 2, . . . , n}. Let the eigenvalues of L(G) be λ1 ≥ · · · ≥ λn−1 ≥ λn = 0. Then the number of spanning trees of G equals λ1 · · · λn−1 /n.
  *Proof:* Evaluates the sum of principal minors representing spanning trees against the elementary symmetric polynomials of eigenvalues.
- **Theorem 4.12.** Let G be a graph with V (G) = {1, 2, . . . , n} and with at least one edge. Let the eigenvalues of L(G) be λ1 ≥ · · · ≥ λn−1 ≥ λn = 0. Then λ1 ≥ Δ + 1.
  *Proof:* Maximizes the largest eigenvalue of the triangular Cholesky factor bounded below by the maximum degree node.
- **Theorem 4.13.** Let G be a graph with vertex set V = {1, . . . , n}. Let L be the Laplacian of G with the maximum eigenvalue λ1 . Then λ1 ≤ max{di + dj − c(i, j) : 1 ≤ i < j ≤ n, i ∼ j}, where c(i, j) is the number of vertices that are adjacent to both i and j.
  *Proof:* Binds the Laplacian spectral radius by manipulating eigenvector component equations across adjacent vertices.
- **Corollary 4.14.** Let G be a graph with the vertex set V = {1, . . . , n}. Let L be the Laplacian of G with maximum eigenvalue λ1 . Then λ1 ≤ max{di + dj : 1 ≤ i < j ≤ n, i ∼ j}.
  *Proof:* (immediate from Theorem 4.13)
- **Lemma 4.15.** Let H be the (n − 1) × n matrix defined as follows. The rows and the columns of H are indexed by the edges and the vertices of T , respectively. Set hij = 1 if edge ei is directed away from vertex j, and hij = 0 otherwise. Then HQ = In−1 .
  *Proof:* Verifies the identity directly by observing index cancellation between outgoing edge heads and tails.
- **Theorem 4.16.** The rows and the columns of Q+ are indexed by the edges and the vertices of T , respectively. The (i, j)-element of Q+ is − tni if j is in the head component of ei , and it equals 1 − tni if j is in the tail component of ei .
  *Proof:* Uses the generalized inverse property HQ=I and the null-space condition Q+1=0 to explicitly construct the pseudo-inverse.
- **Theorem 4.18.** For i, j = 1, . . . , n, the (i, j)-element of L + is given by 1 n−1 α(i, j, ek )f (ek , i)f (ek , j). n2 k=1
  *Proof:* (no proof in this paper)
- **Theorem 4.19.** For i, j = 1, . . . , n − 1, the (i, j)-element of K −1 is given by 1 n ± (n − f (ei , ej ))(n − f (ej , ei )), where the sign is positive or negative according as ei and ej are similarly oriented or oppositely oriented, respectively.
  *Proof:* (no proof in this paper)
- **Theorem 5.1.** Let G be a connected graph with n vertices, m edges, and let T be a spanning tree of G. For each ei ∈ E(T c ), let x i be the incidence vector of the fundamental cycle Ci . Then {x i : ei ∈ E(T c )} forms a basis for the cycle subspace of G.
  *Proof:* Proves basis linear independence since each fundamental cycle contains a strictly unique edge outside the tree.
- **Theorem 5.2.** Let G be a connected graph with n vertices, m edges, and let T be a spanning tree of G. For each ei ∈ E(T ), let y i be the incidence vector of the fundamental cut Ki . Then {y i : ei ∈ E(T )} forms a basis for the cut subspace of G.
  *Proof:* Shows cut subspace independence because every fundamental cut splits the tree on one uniquely defined edge.
- **Lemma 5.4.** B f = −C f .
  *Proof:* Exploits orthogonality between the cycle and cut subspaces, leading to the zero product of their fundamental matrices.
- **Theorem 5.6.** Let Q 1 be the reduced incidence matrix obtained by deleting the last row of Q and suppose Q 1 is partitioned as Q 1 = [Q 11 , Q 12 ], where Q 11 is of order (n − 1) × (n − 1). Then B f = Q −1 11 Q 12 and C f = −Q 12 (Q 11 ) .
  *Proof:* Extracts fundamental structures algebraically by factoring the cut matrix into the reduced incidence matrix columns.
- **Theorem 5.7.** Let G be a connected graph with n vertices, m edges, and let B be the fundamental cut matrix of G with respect to the spanning tree T. Then the following assertions hold: (i) a set of columns of B is a linearly independent set if and only if the corresponding edges of G induce an acyclic graph; (ii) a set of n − 1 columns of B is a linearly independent set if and only if the corresponding edges form a spanning tree of G; (iii) if X is a submatrix of B of order (n − 1) × (n − 1), then det X is either 0 or ±1; (iv) det B B equals the number of spanning trees of G.
  *Proof:* Links independence in B to tree topologies by taking determinants of the totally unimodular reduced incidence matrices.
- **Lemma 5.8.** Columns j1 , . . . , jk of C are linearly dependent if the subgraph of G induced by the corresponding edges contains a cut.
  *Proof:* Confirms dependence by placing the incidence vector of any existing cut into the null space of the cycle matrix.
- **Lemma 5.9.** Let X be a submatrix of C of order (m − n + 1) × (m − n + 1). Then X is nonsingular if and only if the edges corresponding to the column indices of X form a cotree of G.
  *Proof:* Correlates a non-singular span with the absence of cuts which forces the unselected edges to form a connected spanning tree.
- **Lemma 5.10.** Let F ⊂ E(G) and suppose the columns of C indexed by F are linearly dependent. Then the subgraph of G induced by F contains a cut.
  *Proof:* Proves the contrapositive by noting that uncut edges uniquely extend into full cotrees representing non-singular blocks.
- **Lemma 5.11.** Let G be a connected graph with n vertices, m edges, and let B be the fundamental cut matrix of G with respect to the spanning tree T. Then B is totally unimodular.
  *Proof:* Reduces arbitrary minors by augmenting them with spanning tree columns, concluding they evaluate to unimodular roots.
- **Lemma 5.12.** Let G be a connected graph with n vertices, m edges, and let C be the fundamental cycle matrix of G with respect to the spanning tree T. Then C is totally unimodular.
  *Proof:* Relates arbitrary cycle minors directly to the fundamentally symmetric cut submatrices, invoking prior total unimodularity.
- **Theorem 5.13.** Let G be a connected graph with n vertices, m edges, and let B be the fundamental cut matrix of G with respect to the spanning tree T. Let E ⊂ E(T ) and let B B [E|E] be the submatrix of B B with rows and columns indexed by E. Then det B B [E|E] equals the number of ways of extending E c to a spanning tree of G.
  *Proof:* Evaluates submatrix sums via Cauchy-Binet, where non-zero blocks directly map to acyclic edge combinations bridging trees.
- **Corollary 5.14.** Let G be a connected graph with n vertices, m edges, and let B be the fundamental cut matrix of G with respect to the spanning tree T. Let ei ∈ E(T ) and let B B (ei |ei ) be the submatrix of B B with row and column indexed by ei deleted. Then det B B (ei |ei ) equals the number of spanning forests of G with two components, such that the endpoints of ei are in different components.
  *Proof:* (immediate from Theorem 5.13)
- **Lemma 6.1.** Let G be a connected graph with n vertices, and let A be the adjacency matrix of G. Then (I + A)n−1 > 0.
  *Proof:* Employs the interpretation of matrix powers tracking existence of paths of maximum necessary lengths between nodes.
- **Lemma 6.2.** Let G be a connected graph with n vertices, and let A be the adjacency matrix of G. If x ≥ 0 is an eigenvector of A, then x > 0.
  *Proof:* Multiplying by the strictly positive graph connection matrix guarantees all resulting eigenvector components are strictly positive.
- **Theorem 6.3.** Let G be a connected graph with n ≥ 2 vertices, and let A be the adjacency matrix of G. Then the following assertions hold: (i) A has an eigenvalue λ > 0 and an associated eigenvector x > 0. (ii) for any eigenvalue μ = λ of A, −λ ≤ μ < λ. Furthermore, −λ is an eigenvalue of A if and only if G is bipartite. (iii) if u is an eigenvector of A for the eigenvalue λ, then u = αx for some α.
  *Proof:* Guarantees the Perron vector via Brouwer's fixed point theorem and uniquely bounds other modes via triangle inequalities.
- **Theorem 6.4.** Let G be a graph with n vertices, and let A be the adjacency matrix of G. Then ρ(G) is an eigenvalue of G and there is an associated nonnegative eigenvector.
  *Proof:* Pads the known positive eigenvector from the maximal connected component with zeros for the remaining disjoint subgraphs.
- **Lemma 6.5.** Let G be a connected graph with n vertices, and let H = G be a spanning, connected subgraph of G. Then ρ(G) > ρ(H).
  *Proof:* Yields a strict bound on spectral radii by applying the element-wise strictly positive Perron vector of the supergraph.
- **Lemma 6.6.** Let G be a connected graph and let A be the adjacency matrix of G. Let μ > 0, x ≥ 0 be such that Ax ≥ μx, Ax = μx. Then μ < ρ(G).
  *Proof:* Projects the inequality against the positive Perron eigenvector, enforcing strict bound containment on the Rayleigh quotient.
- **Lemma 6.7.** Let G be a connected graph with n vertices and let H = G be a vertex-induced subgraph of G. Then ρ(G) > ρ(H).
  *Proof:* Pads the subgraph's eigenvector with zeros to form a strict test vector against the full graph adjacency matrix.
- **Theorem 6.8.** Let G be a connected graph and let H = G be a subgraph of G. Then ρ(G) > ρ(H).
  *Proof:* Transitive composition of the strict inequality bounds governing spanning and induced subgraph spectral radii.
- **Theorem 6.9.** Let G be a connected graph with n vertices. Then ρ(G) is an eigenvalue of G with algebraic multiplicity 1.
  *Proof:* (immediate from Theorem 6.3)
- **Theorem 6.10.** Let G be a k-regular graph. Then ρ(G) equals k, and it is an eigenvalue of G. It has algebraic multiplicity 1 if G is connected.
  *Proof:* Observes the all-ones vector natively eigenvectors to the maximal node degree under regular connectivity.
- **Theorem 6.11.** Let G be a connected graph with n vertices, and let A be the adjacency matrix of G. Then for any y, z ∈ IRn , y = 0, z > 0, y Ay yy ≤ ρ(G) ≤ maxi (Az)i zi .
  *Proof:* Sandwiches the maximal eigenvalue via the optimal Rayleigh quotient and contradictory bounds on the left Perron eigenvector.
- **Corollary 6.12.** Let G be a connected graph with n vertices and m edges. Let d1 ≥ · · · ≥ dn be the vertex degrees. Then the following assertions hold: (i) 2m n ≤ ρ(G) ≤ d1 ; (ii) 1 2m n i=1 di dj ≤ ρ(G) ≤ maxi 1 d1i j∼i di dj . Furthermore, equality holds in any of the above inequalities if and only if G is regular.
  *Proof:* Evaluates test inequalities explicitly parameterized by the constant unit vector and degree-scaled variables.
- **Theorem 6.13.** Let G be a graph with n vertices, m edges, and no triangles. Then m ≤ n4 .
  *Proof:* Proves Turan's bound dynamically tracking adjacency matrix traces lacking odd cycle traces against maximal node bounds.
- **Theorem 6.14.** Let G be a graph with n vertices. Then G is a connected, regular graph if and only if J is in the adjacency algebra of G.
  *Proof:* Constrains the commutative operations forcing polynomials on the adjacency matrix to match the flat structure of J.
- **Theorem 6.15.** Let G be a k-regular graph with n vertices. Let A and A be the adjacency matrices of G and Gc , respectively. If k = λ1 , λ2 , . . . , λn are the eigenvalues of A, then n − 1 − λ1 , −1 − λ2 , . . . , −1 − λn are the eigenvalues of A.
  *Proof:* Maps the complementary matrix representation entirely through the graph's pre-diagonalized orthogonal basis.
- **Corollary 6.16.** Let G be a k-regular graph with n vertices. Then φ(Gc , λ) = (−1)n λ+k+1−n λ+k+1 φ(G, −λ − 1).
  *Proof:* Maps characteristic polynomial roots symmetrically inverted via the complementing transformations.
- **Theorem 6.17.** Let G be a k-regular graph with n vertices. Then the number of spanning trees of G is given by n1 φ (G, λ)|λ=k .
  *Proof:* Evaluates spanning trees functionally leveraging the determinant derivative matching remaining polynomial eigen-roots.
- **Lemma 6.18.** Let G be a graph with n vertices. Let A and B be the adjacency matrices of G and of G , respectively. If M is the incidence matrix of G, then M M = B + 2I. Furthermore, if G is k-regular then MM = A + kI.
  *Proof:* Formulates line graph and Laplacian components by distributing incident entries across node-edge cross products.
- **Corollary 6.19.** Let G be a graph. If μ is an eigenvalue of G then μ ≥ −2.
  *Proof:* (immediate from Lemma 6.18)
- **Theorem 6.20.** Let G be a k-regular graph with n vertices. Then φ(G , λ) = (λ + 2) 2 (k−2) φ(G, λ + 2 − k).
  *Proof:* Adjusts the characteristic polynomials tracking roots through the dimensional disparity between incidence pseudo-inverses.
- **Lemma 6.21.** Let G be a strongly regular graph with parameters (n, k, a, c) and let A be the adjacency matrix of G. Then A2 = kI + aA + c(J − I − A).
  *Proof:* Enumerates walk trajectories isolating lengths natively prescribed by strongly regular adjacent node constraints.
- **Lemma 6.22.** Let G be a graph which is neither complete nor empty, and let A be the adjacency matrix of G. Then G is strongly regular if A2 is a linear combination of A, I and J.
  *Proof:* (no proof in this paper)
- **Theorem 6.23.** Let G be a strongly regular graph with parameters (n, k, a, c) and let A be the adjacency matrix of G. Let Δ = (a − c)2 + 4(k − c). Then any eigenvalue of A is either k or 21 (a − c ± Δ).
  *Proof:* Extracts non-trivial eigenvectors directly resolving the roots of the explicitly formed quadratic matrix equality.
- **Theorem 6.24.** Let G be a connected, strongly regular graph with parameters (n, k, a, c). Let Δ = (a − c)2 + 4(k − c). Then the numbers m1 = 21 n − 1 + (n − 1)(c − a) − 2k √ Δ and m2 = 21 n − 1 − (n − 1)(c − a) − 2k √ Δ are nonnegative integers.
  *Proof:* Solves for algebraic multiplicities applying the zero-sum trace to constraints of the derived irrational eigenvalue pairing.
- **Theorem 6.25.** Let G be a connected regular graph with exactly three distinct eigenvalues. Then G is strongly regular.
  *Proof:* Concludes strong regularity because the third-degree minimal polynomial enforces a quadratic relation among components.
- **Theorem 6.26.** Let G be a graph in which any two distinct vertices have exactly one common neighbour. Then G has a vertex that is adjacent to every other vertex, and, more precisely, G consists of a number of triangles with a common vertex.
  *Proof:* Refutes arbitrary regularity relying on integer division constraints applied to strongly regular graph parameters.
- **Theorem 6.27.** Let G be a graph with n vertices, m edges, and suppose 2m ≥ n. Then ε(G) ≤ 2mn + (n − 1) 2m − (2mn)2 .
  *Proof:* Uses Cauchy-Schwarz against the graph's energy summation and trace to upper bound absolute value divergence.
- **Theorem 6.28.** Let G be a graph with n vertices, m edges, and suppose 2m ≤ n. Then ε(G) ≤ 2m.
  *Proof:* Iteratively subtracts null vertices applying the general bound inequality to isolate active dense components.
- **Theorem 6.29.** Let G be a graph with n vertices. Then ε(G) ≤ n2 (1 + n).
  *Proof:* Derives the peak theoretical capacity analytically locating function critical points scaling graph dimension limits.
- **Lemma 7.1.** Let G be a block graph with n vertices. Let B1 , . . . , Bk be the blocks of G where Bi is the complete graph with bi vertices, i = 1, . . . , k. Let (α1 , . . . , αk ) be a k-tuple of nonnegative integers satisfying the following conditions: (i) k i=1 αi = n (ii) for any nonempty S ⊂ {1, . . . , k}, i∈S αi ≤ |V (G S )|. If Bi is a pendant block, then αi equals either bi or bi − 1.
  *Proof:* Eliminates invalid tuple values isolating targeted combinatorial subsets mapping node constraints linearly.
- **Theorem 7.2.** Let G be a block graph with n vertices. Let B1 , . . . , Bk be the blocks of G. Let A be the adjacency matrix of G. Then det A = (−1)n−k (α1 − 1) · · · (αk − 1) where the summation is over all k-tuples (α1 , . . . , αk ) of nonnegative integers satisfying the following conditions: (i) k i=1 αi = n (ii) for any nonempty S ⊂ {1, . . . , k}, i∈S αi ≤ |V (G S )|.
  *Proof:* Recursively partitions pendant block segments simplifying determinant derivations functionally through Schur complements.
- **Corollary 7.3.** Let T be a tree with n vertices and let A be the adjacency matrix of T. Then A is nonsingular over reals if and only if T has a perfect matching.
  *Proof:* Constrains the block determinant sum verifying only single matching edges provide valid non-zero variable assignments.
- **Lemma 7.5.** Let G be a connected graph with n vertices and let K be the signless Laplacian of G. If G is bipartite, then K is singular with rank n − 1. If G is non-bipartite, the
  *Proof:* (no proof in this paper)
```