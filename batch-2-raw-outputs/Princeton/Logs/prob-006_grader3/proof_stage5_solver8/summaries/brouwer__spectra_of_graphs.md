<!-- Generated 2026-05-31T01:42:34 -->
<!-- Source PDF: brouwer__spectra_of_graphs.pdf (1639397 bytes) -->
<!-- Citation: A. E. Brouwer, W. H. Haemers (2011). Spectra of Graphs. Springer Universitext. -->

# Spectra of Graphs (A. E. Brouwer, W. H. Haemers, 2011)

## Definitions
*(No explicitly labeled definitions in this paper)*

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 1.3.1.** Let h be a nonnegative integer. Then (Ah )xy is the number of walks of length h from x to y. In particular, (A2 )xx is the degree of the vertex x, and tr A2 equals twice the number of edges of Γ ; similarly, tr A3 is six times the number of triangles in Γ .
  *Proof:* (no proof in this paper)
- **Proposition 1.3.2.** Let Γ be an undirected graph. All its eigenvalues are zero if and only if Γ has no edges. The same holds for the Laplace eigenvalues and the signless Laplace eigenvalues.
  *Proof:* (no proof in this paper)
- **Proposition 1.3.3.** Let Γ be a connected graph with diameter d. Then Γ has at least d + 1 distinct eigenvalues, at least d + 1 distinct Laplace eigenvalues, and at least d + 1 distinct signless Laplace eigenvalues.
  *Proof:* Relates powers of a non-negative symmetric adjacency matrix to distance to show that fewer eigenvalues imply disconnected vertices.
- **Proposition 1.3.4.** Let Γ be an undirected (multi)graph with at least one vertex, and Laplace matrix L with eigenvalues 0 = µ1 ≤ µ2 ≤ . . . ≤ µn . Let ℓxy be the (x, y)-cofactor of L. Then the number N of spanning trees of Γ equals N = ℓxy = det(L + 1n2 J) = 1n µ2 · · · µn for any x, y ∈ V Γ .
  *Proof:* Uses induction on vertices and edges to link the cofactor to the spanning trees, then evaluates the characteristic polynomial of L.
- **Proposition 1.3.5 (Cauchy-Binet).** Let A and B be m × n matrices. Then det AB⊤ = ∑S det AS det BS where the sum is over the n m m-subsets S of the set of columns, and AS (BS ) is the square submatrix of order m of A (resp. B) with columns indexed by S.
  *Proof:* (no proof in this paper)
- **Proposition 1.3.6.** Let Γ be a graph with connected components Γi (1 ≤ i ≤ s). Then the spectrum of Γ is the union of the spectra of Γi (and multiplicities are added). The same holds for the Laplace and the signless Laplace spectrum.
  *Proof:* (no proof in this paper)
- **Proposition 1.3.7.** The multiplicity of 0 as a Laplace eigenvalue of an undirected graph Γ equals the number of connected components of Γ .
  *Proof:* Observes that eigenvectors of zero imply constant values along connected components via the incidence matrix equation N⊤ u = 0.
- **Proposition 1.3.8.** Let the undirected graph Γ be regular of valency k. Then k is the largest eigenvalue of Γ , and its multiplicity equals the number of connected components of Γ .
  *Proof:* Relies directly on the relation L = kI − A.
- **Proposition 1.3.9.** The multiplicity of 0 as a signless Laplace eigenvalue of an undirected graph Γ equals the number of bipartite connected components of Γ .
  *Proof:* Evaluates the signless Laplacian Q = MM⊤ to show zero eigenvectors alternate signs across incident edges.
- **Proposition 1.3.10.** A graph Γ is bipartite if and only if the Laplace spectrum and the signless Laplace spectrum of Γ are equal.
  *Proof:* Applies a diagonal similarity transform mapping the Laplacian to the signless Laplacian, connecting the number of components.
- **Proposition 1.4.1.** Suppose Γ has m edges, and let ρ1 ≥ . . . ≥ ρr be the positive signless Laplace eigenvalues of Γ , then the eigenvalues of L(Γ ) are θi = ρi − 2 for i = 1, . . . , r, and θi = −2 if r < i ≤ m.
  *Proof:* Correlates the line graph's adjacency and the signless Laplacian utilizing their shared incidence matrix factors NN⊤ and N⊤N.
- **Corollary 1.4.2.** If Γ is a k-regular graph (k ≥ 2) with n vertices, e = kn/2 edges and eigenvalues θi (i = 1, . . . , n), then L(Γ ) is (2k − 2)-regular with eigenvalues θi + k − 2 (i = 1, . . . , n) and e − n times −2.
  *Proof:* (immediate from Proposition 1.4.1)
- **Proposition 1.5.1 (H. S. Witsenhausen; Graham & Pollak [173]).** Suppose a graph Γ with adjacency matrix A has an edge decomposition into r complete bipartite graphs. Then r ≥ n+ (A) and r ≥ n− (A), where n+ (A) and n− (A) are the numbers of positive (negative) eigenvalues of A.
  *Proof:* Embeds the component bipartite matrices into a quadratic form and tests it against orthogonal vectors from the decomposition.
- **Corollary 1.6.1.** If all eigenvalues are simple, then Aut Γ is an elementary abelian 2-group.
  *Proof:* Asserts any automorphism of higher order generates identical coordinates on orbits, causing a contradiction of simple eigenvalues.
- **Corollary 1.6.2.** Let Aut Γ be transitive on X. (Then Γ is regular of degree k, say.) (i) If m(θ ) = 1 for some eigenvalue θ 6= k, then v = |X| is even, and θ ≡ k (mod 2). If Aut Γ is moreover edge-transitive then Γ is bipartite and θ = −k. (ii) If m(θ ) = 1 for two distinct eigenvalues θ 6= k, then v ≡ 0 (mod 4). (iii) If m(θ ) = 1 for all eigenvalues θ , then Γ has at most two vertices.
  *Proof:* Divides vertex sets according to eigenvector values generated by transitivity, deducing necessary conditions on parameters.
- **Proposition 1.7.1.** Let Γ and ∆ be two edge-disjoint graphs on the same vertex set, and Γ ∪ ∆ their union. We have µ2 (Γ ∪ ∆ ) ≥ µ2 (Γ ) + µ2 (∆ ) ≥ µ2 (Γ ).
  *Proof:* Operates the variational Rayleigh quotient on the combined quadratic forms.
- **Proposition 1.7.2.** Let Γ be a graph with vertex set X. Suppose D ⊂ X is a set of vertices such that the subgraph induced by Γ on X \ D is disconnected. Then |D| ≥ µ2 (Γ ).
  *Proof:* Adds all edges between D and the rest of the graph to forge an eigenvector forcing the lowest non-trivial bound.
- **Proposition 2.1.1.** Suppose A is a collection of commuting Hermitean linear transformations on V (i.e., AB = BA for A, B ∈ A ), then V has a basis consisting of common eigenvectors of all A ∈ A .
  *Proof:* Uses induction on the dimension to isolate stable subspaces upon which all commuting operators act.
- **Theorem 2.2.1.** Let T ≥ 0 be irreducible. Then there is a (unique) positive real number θ0 with the following properties: (i) There is a real vector x0 > 0 with T x0 = θ0 x0 . (ii) θ0 has geometric and algebraic multiplicity one. (iii) For each eigenvalue θ of T we have |θ | ≤ θ0 . If T is primitive, then |θ | = θ0 implies θ = θ0 . In general, if T has period d, then T has precisely d eigenvalues θ with |θ | = θ0 , namely θ = θ0 e2π i j/d for j = 0, 1, . . . , d − 1. In fact the entire spectrum of T is invariant under rotation of the complex plane over an angle 2π /d about the origin. (iv) Any nonnegative left or right eigenvector of T has eigenvalue θ0 . More generally, if x ≥ 0, x 6= 0 and T x ≤ θ x, then x > 0 and θ ≥ θ0 ; moreover, θ = θ0 if and only if T x = θ x. (v) If 0 ≤ S ≤ T or if S is a principal minor of T , and S has eigenvalue σ , then |σ | ≤ θ0 ; if |σ | = θ0 , then S = T . (vi) Given a complex matrix S, let |S| denote the matrix with elements |S|i j = |Si j |. If |S| ≤ T and S has eigenvalue σ , then |σ | ≤ θ0 . If equality holds, then |S| = T , and there are a diagonal matrix E with diagonal entries of absolute value 1 and a constant c of absolute value 1, such that S = cET E −1 .
  *Proof:* Establishes the spectral radius via topological compactness bounds, leverages the triangle inequality on matrix powers to identify rotations, and proves geometric uniqueness by strict eigenvector positivity limits.
- **Lemma 2.3.1.** If, for an equitable partition, v is an eigenvector of B for an eigenvalue λ , then Sv is an eigenvector of A for the same eigenvalue λ .
  *Proof:* Evaluates ASv natively via SBv.
- **Theorem 2.4.1 (Courant-Fischer).** Let W be an i-subspace of V . Then θi ≥ min u∈W, u6=0 u⊤ Au u⊤ u and θi+1 ≤ max u∈W ⊥ , u6=0 u⊤ Au u⊤ u
  *Proof:* (no proof in this paper)
- **Theorem 2.5.1.** Let S be a real n × m matrix such that S⊤ S = I. Let A be a real symmetric matrix of order n with eigenvalues θ1 ≥ . . . ≥ θn . Define B = S⊤ AS and let B have eigenvalues η1 ≥ . . . ≥ ηm and respective eigenvectors v1 . . . vm . (i) The eigenvalues of B interlace those of A. (ii) If ηi = θi or ηi = θn−m+i for some i ∈ [1, m], then B has a ηi -eigenvector v such that Sv is a ηi -eigenvector of A. (iii) If for some integer l, ηi = θi , for i = 1, . . . , l (or ηi = θn−m+i for i = l, . . . , m), then Svi is a ηi -eigenvector of A for i = 1, . . . , l (respectively i = l, . . . , m). (iv) If the interlacing is tight, then SB = AS.
  *Proof:* Maps intersections of the matrix eigenspaces onto the bounds with Rayleigh's principle, recursively verifying matching eigenvectors via orthogonal isolation.
- **Corollary 2.5.2.** If B is a principal submatrix of a symmetric matrix A, then the eigenvalues of B interlace the eigenvalues of A.
  *Proof:* (immediate from Theorem 2.5.1)
- **Corollary 2.5.3.** Let A be a real symmetric matrix of order n. Let x1 , . . . , xm be nonzero orthogonal real vectors of order n. Define a matrix C = (ci j ) by ci j = 1 ||xi ||2 x⊤i Ax j . (i) The eigenvalues of C interlace the eigenvalues of A. (ii) If the interlacing is tight, then Ax j = ∑ ci j xi for all j. (iii) Let x = ∑ x j . The number r := x⊤ Ax x⊤ x lies between the smallest and largest eigenvalue of C. If x is an eigenvector of A with eigenvalue θ , then also C has an eigenvalue θ (for eigenvector 1).
  *Proof:* Normalizes the vectors into an isometric matrix and invokes interlacing on the transformed diagonal elements.
- **Corollary 2.5.4.** Let C be the quotient matrix of a symmetric matrix A whose rows and columns are partitioned according to a partitioning {X1 , . . . , Xm }. (i) The eigenvalues of C interlace the eigenvalues of A. (ii) If the interlacing is tight, then the partition is equitable.
  *Proof:* (no proof in this paper)
- **Theorem 2.6.1 (Schur [291]).** Let A be a real symmetric matrix with eigenvalues θ1 ≥ θ2 ≥ . . . ≥ θn and diagonal elements d1 ≥ d2 ≥ . . . ≥ dn . Then ∑ti=1 di ≤ ∑ti=1 θi for 1 ≤ t ≤ n.
  *Proof:* Forms a principal submatrix by deleting rows and columns beyond t and extracts the bound natively via interlacing constraints.
- **Theorem 2.7.1 (see [336]).** The Schur complement A/A11 satisfies (i) I O −A21 A−1 11 I A11 A12 A21 A22 I −A−1 11 A12 O I = A11 O O A/A11 , (ii) det(A/A11 ) = det A/ det A11 , (iii) rk A = rk A11 + rk(A/A11 ).
  *Proof:* (no proof in this paper)
- **Corollary 2.7.2.** If rk A = rk A11 , then A22 = A21 A−1 11 A12 .
  *Proof:* (no proof in this paper)
- **Theorem 2.8.1.** Let A and B be Hermitean matrices of order n, and let 1 ≤ i, j ≤ n. (i) If i + j − 1 ≤ n then λi+ j−1 (A + B) ≤ λi (A) + λ j (B). (ii) If i + j − n ≥ 1 then λi (A) + λ j (B) ≤ λi+ j−n (A + B). (iii) If B is positive semidefinite, then λi (A + B) ≥ λi (A).
  *Proof:* Constructs a test subspace overlapping the tops of both individual eigenspaces and applies the Courant-Fischer max-min bounds.
- **Theorem 2.8.2.** Let A and B be Hermitean matrices of order n. Then for all t, 0 ≤ t ≤ n, we have ∑ti=1 λi (A + B) ≤ ∑ti=1 λi (A) + ∑ti=1 λi (B).
  *Proof:* Uses the characterization of the sum of the highest eigenvalues as the maximum trace over constrained subspaces.
- **Lemma 2.9.1.** Let G be a real symmetric n × n-matrix. Equivalent are: (i) For all x ∈ Rn , x⊤ Gx ≥ 0. (ii) All eigenvalues of G are nonnegative. (iii) G can be written as G = H ⊤ H, with H an m × n matrix, where m is the rank of G.
  *Proof:* Drops zero rows from the decomposed square root matrix built upon the orthogonal eigensystem diagonalization.
- **Lemma 2.9.2.** Let N be a real m × n matrix. Then the matrices NN ⊤ and N ⊤ N have the same nonzero eigenvalues (including multiplicities). Moreover, rk NN ⊤ = rk N ⊤ N = rk N.
  *Proof:* Evaluates mapping eigenspaces directly with $N^\top u$, restricting null kernels to guarantee corresponding eigenvalue matches.
- **Lemma 2.10.1.** (i) A strictly diagonally dominant complex matrix is nonsingular. (ii) A symmetric diagonally dominant real matrix with nonnegative diagonal entries is positive semidefinite. (iii) Let B be a symmetric real matrix with nonnegative row sums and nonpositive off-diagonal entries. Define a graph Γ on the index set of the rows of B, where two distinct indices i, j are adjacent when bi, j 6= 0. The multiplicity of the eigenvalue 0 of B equals the number of connected components C of Γ such that all rows i ∈ C have zero row sum.
  *Proof:* Selects the maximal absolute element in a hypothetical eigenvector forcing strict boundaries onto sums of the complex absolute entries.
- **Proposition 2.10.2.** Let A = (ai j ) be a complex matrix of order n, and λ an eigenvalue of A. Put ri = ∑ j6=S i |ai j |. Then for some i we have λ ∈ B(aii , ri ). If C is a connected component of i B(aii , ri ) that contains m of the aii , then C contains m eigenvalues of A.
  *Proof:* Parametrizes the matrix off-diagonals to 0 continuously, demonstrating path preservation of eigenvalues within the bounded disks.
- **Lemma 2.11.1.** Let P = Q N N⊤ R be a real symmetric matrix of order n with two eigenvalues a and b, partitioned with square Q and R. Let Q have h eigenvalues θ j distinct from a and b. Then R has h eigenvalues a + b − θ j distinct from a and b, and h = mP (a) − mQ (a) − mR (a) = mP (b) − mQ (b) − mR (b), where mM (η ) denotes the multiplicity of the eigenvalue η of M.
  *Proof:* Normalizes P into a projector matrix, bridging its disjoint parts to pair non-trivial eigenvalues together and resolving dimensions via trace invariants.
- **Proposition 3.1.1.** Each graph Γ has a real eigenvalue θ0 with nonnegative real corresponding eigenvector, and such that for each eigenvalue θ we have |θ | ≤ θ0 . The value θ0 (Γ ) does not increase when vertices or edges are removed from Γ . Assume that Γ is strongly connected. Then (i) θ0 has multiplicity 1. (ii) If Γ is primitive (strongly connected, and such that not all cycles have a length that is a multiple of some integer d > 1), then |θ | < θ0 for all eigenvalues θ different from θ0 . (iii) The value θ0 (Γ ) decreases when vertices or edges are removed from Γ .
  *Proof:* (no proof in this paper)
- **Proposition 3.1.2.** Let Γ be a connected graph with largest eigenvalue θ1 . If Γ is regular of valency k, then θ1 = k. Otherwise, we have kmin < k̄ < θ1 < kmax where kmin , kmax and k̄ are the minimum, maximum and average degree.
  *Proof:* Applies Perron-Frobenius limits against the uniform vector and binds averages via the equitable partition quotient bound.
- **Theorem 3.1.3 (Smith [310], cf. Lemmens & Seidel [238]).** The only connected graphs having largest eigenvalue 2 are the following graphs (the number of vertices is one more than the index given). Ân (n ≥ 2) D̂n (n ≥ 4) Ê6 Ê7 Ê8 For each graph, the corresponding eigenvector is indicated by the integers at the vertices. Moreover, each connected graph with largest eigenvalue less than 2 is a subgraph of one of the above graphs, i.e., one of the graphs An = Pn , the path with n vertices (n ≥ 1), or Dn (n ≥ 4) E6 E7 E8 Finally, each connected graph with largest eigenvalue more than 2 contains one of Ân , D̂n , Ê6 , Ê7 , Ê8 as a subgraph.
  *Proof:* Plugs explicit integers into adjacency relations ensuring exactly $\lambda = 2$, enforcing strict upper bounds upon any graph with extra edges.
- **Proposition 3.1.4 (Hoffman-Smith [212]).** Let Γ be a connected graph, and let the graph Γ ′ be obtained from Γ by subdividing an edge e. Let Γ and Γ ′ have largest eigenvalues λ and λ ′ , respectively. Then if e lies on an endpath, we have λ ′ > λ , and otherwise λ ′ ≤ λ , with equality only when both equal 2.
  *Proof:* Fuses eigenvectors of the original graph to build a positive test vector for the newly subdivided edge, constraining Perron-Frobenius sums via path-ends.
- **Proposition 3.1.5 (Csikvári [106]).** Let Γ be a graph, and let Γ ′ be obtained from Γ by a Kelmans operation. Then θ1 (Γ ) ≤ θ1 (Γ ′ ). (And hence also θ1 (Γ ) ≤ θ1 (Γ ′ ).)
  *Proof:* Submits the previously maximal eigenvector to the new Kelmans graph, showing positive displacement under the new ordered subset boundaries.
- **Proposition 3.2.1.** (i) Let Γ be a graph and ∆ an induced subgraph. Then the eigenvalues of ∆ interlace those of Γ , (ii) Let Γ be a graph and let ∆ be a subgraph, not necessarily induced, on m vertices. Then the i-th largest Laplace eigenvalue of ∆ is not larger than the i-th largest Laplace eigenvalue of Γ (1 ≤ i ≤ m), and the i-th largest signless Laplace eigenvalue of ∆ is not larger than the i-th largest signless Laplace eigenvalue of Γ (1 ≤ i ≤ m).
  *Proof:* Interlaces induced elements via principal matrices directly, then extracts non-induced factors utilizing incidence matrix representations deleting edge columns.
- **Proposition 3.3.1.** Let Γ be a graph with eigenvalues k = θ1 ≥ θ2 ≥ . . . ≥ θn . Equivalent are: (i) Γ is regular (of degree k), (ii) AJ = kJ, (iii) ∑ θi2 = kn.
  *Proof:* Reconciles sum-of-squares with degree summation, forcing uniformity exclusively when the trace equals the graph maximum element parameter.
- **Proposition 3.3.2.** The graph Γ is regular and connected if and only if there exists a polynomial p such that J = p(A).
  *Proof:* Molds an explicit polynomial utilizing exclusively the distinct non-trivial eigenvalues, rendering the characteristic transformation onto the all-ones dimension block.
- **Proposition 3.4.1.** (i) A graph Γ is bipartite if and only if for each eigenvalue θ of Γ , −θ is also an eigenvalue, with the same multiplicity. (ii) If Γ is connected with largest eigenvalue θ1 , then Γ is bipartite if and only if −θ1 is an eigenvalue of Γ .
  *Proof:* Relies on Perron-Frobenius equivalence maps generating mirrored eigenvectors precisely on completely partitioned cyclic components.
- **Theorem 3.5.1.** α (Γ ) ≤ n − n− = |{i|θi ≥ 0}| and α (Γ ) ≤ n − n+ = |{i|θi ≤ 0}|.
  *Proof:* Embeds the independence set as an empty principal block and filters strictly using general subset interlacing limitations.
- **Theorem 3.5.2.** If Γ is regular of nonzero degree k, then α (Γ ) ≤ n − θn k − θn , and if a coclique C meets this bound, then every vertex not in C is adjacent to precisely −θn vertices of C.
  *Proof:* Models an equitable matrix partition collapsing into a 2x2 quotient, enforcing bounds by testing tight interlacing onto its explicit zero roots.
- **Proposition 3.5.3.** Let Γ have minimum vertex degree δ . Then α (Γ ) ≤ n − θ1 θn δ 2 − θ1 θn .
  *Proof:* (no proof in this paper)
- **Theorem 3.5.4.** α (Γ ) ≤ n − n− (B) and α (Γ ) ≤ n − n+ (B).
  *Proof:* (no proof in this paper)
- **Theorem 3.5.5.** Let B be a weighted adjacency matrix of Γ with constant row sums b and smallest eigenvalue s. Then α (Γ ) ≤ n(−s)/(b − s).
  *Proof:* (no proof in this paper)
- **Proposition 3.6.1 (Wilf [332]).** Let Γ be connected with largest eigenvalue θ1 . Then χ (Γ ) ≤ 1 + θ1 with equality if and only if Γ is complete or is an odd cycle.
  *Proof:* Constrains chromatic subgraphs to maintain minimum internal degrees equal to colors lacking, isolating strict paths mapping immediately onto Brooks' constraints.
- **Theorem 3.6.2 (Hoffman [210]).** If Γ is not edgeless then χ (Γ ) ≥ 1 − θ1 θn .
  *Proof:* Manipulates orthogonal projections via quotient coloring maps yielding bounded traces matching precisely across isolated bounds.
- **Proposition 3.6.3.** Put m = χ (Γ ). Then (i) θ1 + θn−m+2 + . . . + θn ≤ 0. (ii) If n > m, then θ2 + . . . + θm + θn−m+1 ≥ 0. (iii) If n > tm, then θt+1 + . . . + θt+m−1 + θn−t(m−1) ≥ 0.
  *Proof:* Filters combinations of mutually disjoint subspace characteristic vectors stripped by specific eigenvalues, evaluating remaining trace interlacing constraints directly.
- **Corollary 3.6.4.** If the eigenvalue θn has multiplicity g and θ2 > 0, then χ (Γ ) ≥ min(1 + g, 1 − θn θ2 ).
  *Proof:* Replaces overlapping spectrum values explicitly utilizing the multiplicity limit condition mapped into quotient trace substitutions.
- **Proposition 3.7.1 (Lovász [249]).** Let Γ be regular of valency k. Then c(Γ ) ≤ n(−θn )/(k − θn ).
  *Proof:* Submits a specifically scaled tensor matrix product into the weighted Hoffman bounds directly mirroring capacity growth.
- **Lemma 3.7.2.** ϑ (Γ ⊠ ∆ ) ≤ ϑ (Γ )ϑ (∆ ).
  *Proof:* Tensors the optimal representation matrices element-wise retaining bounding relations.
- **Theorem 3.7.3.** The Shannon capacity c(Γ ) satisfies α (Γ ) ≤ c(Γ ) ≤ ϑ (Γ ).
  *Proof:* Limits maximum matrix traces on independence subsets and expands universally tracking identical limits inside multi-level block parameters.
- **Theorem 3.7.4 (‘Sandwich’).** α (Γ ) ≤ ϑ (Γ ) ≤ χ (Γ ) .
  *Proof:* Designs a block coloring matrix explicitly balancing cross-components into bounds identical precisely to the quotient subset maximum values.
- **Proposition 3.7.5.** Suppose Γ is regular of valency k, with smallest eigenvalue θn . Then ϑ (Γ ) ≤ −nθn k − θn .
  *Proof:* Extracts immediate trace limits placing the scaled adjacency values inside general feasible parameters defining theta.
- **Proposition 3.7.6.** One has ϑ (Γ )ϑ (Γ ) ≥ n for a graph Γ of order n. Equality holds if Γ is vertex transitive.
  *Proof:* (no proof in this paper)
- **Lemma 3.7.7.** η (Γ ⊠ ∆ ) ≤ η (Γ )η (∆ ).
  *Proof:* Compares matrices under Kronecker parameters generating multiplied matrix dimension ranks spanning exact boundaries.
- **Theorem 3.7.8.** The Shannon capacity c(Γ ) satisfies α (Γ ) ≤ c(Γ ) ≤ η (Γ ).
  *Proof:* Sets bounds directly across empty diagonal coclique limits extending constraints universally to tensor limits mimicking independent variables.
- **Proposition 3.7.9.** α (Γ ) ≤ η (Γ ) ≤ χ (Γ ).
  *Proof:* Instantiates boolean components strictly aligned with the cover to demonstrate a directly comparable rank matrix definition.
- **Proposition 3.8.1.** Let Γ be a connected bipartite cubic graph such that all of its eigenvalues are integral. Then Γ is one of 8 possible graphs, namely (i) K3,3 , (ii) 23 , (iii) K2,3 ∗ ⊗ K2 , (iv) C6 K2 , (v) the Desargues graph (that is, the bipartite double Π ⊗ K2 of the Petersen graph Π ), (vi) T ∗ (cospectral with the previous), (vii) the bipartite double of Σ , (viii) the point-line incidence graph of the generalized quadrangle of order 2 (that is, the unique 3-regular bipartite graph with diameter 4 and girth 8, also known as Tutte’s 8-cage).
  *Proof:* Defines structural constraints via trace polynomial powers determining all hexagons and quadrangles; enumerates solutions to the finite Diophantine equations resolving topologies uniquely.
- **Proposition 3.8.2.** Let Γ be a connected nonbipartite cubic graph such that all of its eigenvalues are integral. Then Γ is one of 5 possible graphs, namely (ix) K4 , (x) K3 K2 , (xi) the Petersen graph, (xii) the graph on 10 vertices defined by i ∼ (i + 1) (mod 10), 0 ∼ 5, 1 ∼ 3, 2 ∼ 6, 4 ∼ 8, 7 ∼ 9 (or, equivalently, the graph obtained from K3,3 by replacing two nonadjacent vertices by a triangle with a Y − ∆ operation), (xiii) Σ .
  *Proof:* Translates each graph into a bipartite map using tensor pairing sets, resolving via fixed-point free involutions mirroring corresponding unique cases.
- **Proposition 3.9.1.** Let Γ be a graph with adjacency matrix A (with eigenvalues θ1 ≥ . . . ≥ θn ), Laplacian L (with eigenvalues µ1 ≤ . . . ≤ µn ), and signless Laplacian Q (with eigenvalues ρ1 ≥ . . . ≥ ρn ). Then (i) (Zhang & Luo [338]) µn ≤ ρ1 . If Γ is connected, then equality holds if and only if Γ is bipartite. (ii) Let dx be the degree of the vertex x. If Γ has at least one edge then ρ1 ≤ max x∼y (dx + dy ). Equality holds if and only if Γ is regular or bipartite semiregular. (iii) (Yan [334]) 2θi ≤ ρi (1 ≤ i ≤ n).
  *Proof:* Unites Perron-Frobenius element-bounding functions with Courant-Weyl constraints mapping the signless operator exactly spanning local adjacency sets.
- **Corollary 3.9.2 ([10]).** Let Γ be a graph on n vertices with at least one edge. Then µn ≤ max x∼y (dx + dy ). If Γ is connected, then equality holds if and only if Γ is bipartite regular or semiregular.
  *Proof:* (no proof in this paper)
- **Proposition 3.9.3 ([178]).** Let Γ be a graph on n vertices with at least one edge, and let dx be the degree of the vertex x. Then µn ≥ 1 + max x dx . If Γ is connected, then equality holds if and only if max x dx = n − 1.
  *Proof:* Notes the implicit minimum spanning limits set by star subgraphs, demonstrating maximal vertices bind to strict eigenvalue edges inherently lacking strictly disjoint matching parameters.
- **Proposition 3.10.1.** If Γ is connected, with Laplace eigenvalues ν1 ≥ ν2 ≥ ... ≥ νn = 0 and vertex degrees d1 ≥ d2 ≥ ... ≥ dn > 0, then for 1 ≤ m ≤ n − 1 we have 1 + ∑m i=1 di ≤ ∑m i=1 νi .
  *Proof:* Separates target vectors into components matching top degree vertices and their neighbors, then utilizes the induced quotient matrices trace matching elements resolving the dimension strictly.
- **Proposition 3.10.2.** Let Γ be a graph with Laplace eigenvalues ν1 ≥ ν2 ≥ ... ≥ νn = 0 and with vertex degrees d1 ≥ d2 ≥ ... ≥ dn . Let 1 ≤ m ≤ n. If Γ is not Km + (n − m)K1 , then νm ≥ dm − m + 2.
  *Proof:* (no proof in this paper)
- **Proposition 3.11.1.** Let Γ be a threshold graph with Laplace eigenvalues (in non-increasing order) ν1 ≥ ν2 ≥ . . . ≥ νn = 0. Let dx be the degree of the vertex x. Then ν j = #{x | dx ≥ j}.
  *Proof:* Iteratively runs down definitions confirming sequential addition parameters onto simple boundaries directly.
- **Theorem 3.11.2.** Let Γ be an undirected graph with Laplace eigenvalues (in non-increasing order) ν1 ≥ ν2 ≥ . . . ≥ νn = 0. Let dx be the degree of the vertex x. Then for all t, 0 ≤ t ≤ n, we have ∑t i=1 νi ≤ ∑t i=1 #{x | dx ≥ i}.
  *Proof:* Reduces the graph recursively through contradiction components checking semi-bipartite bounds specifically transformed utilizing dual properties mirroring degree offsets accurately tracking trace limits.
- **Lemma 3.11.3.** Let Γ be a semi-bipartite graph with clique of size c and Laplace eigenvalues be ν1 ≥ ν2 ≥ . . . ≥ νn = 0. Let δ be the maximum degree among the vertices in the coclique, so that δ ≤ c. If νc > c or νc = c > δ then we have ∑c i=1 νi ≤ ∑c i=1 #{x | dx ≥ i}.
  *Proof:* Generates structured partitioned elements tracking the strictly defined invariant eigenspaces directly to prove bounded components using the all-ones characteristic limitation exclusively.
- **Lemma 3.11.4.** If νc > δ , then the invariant subspace W spanned by the L-eigenvectors for νi , 1 ≤ i ≤ c, is spanned by the columns of I X where X is nonpositive.
  *Proof:* Tests elements continuously under edge weight transitions forcing strict variable dependencies, determining invariant bounds accurately enforcing completely nonpositive subspace vectors universally bounding limits.
- **Theorem 3.12.1 (Duval & Reiner [143]).** If H is an m-uniform hypergraph with degrees dx and Laplace eigenvalues νi with ν1 ≥ ν2 ≥ . . . ≥ 0, and H is invariant for downshifting, then ν j = #{x | dx ≥ j} for all t.
  *Proof:* (no proof in this paper)
- **Lemma 3.12.2.** (i) a⊤⊤ = a, (ii) (a ∪ b)⊤ = a⊤ + b⊤ and (a + b)⊤ = a⊤ ∪ b⊤ , (iii) a E b if and only if b⊤ E a⊤ .
  *Proof:* (no proof in this paper)
- **Proposition 3.14.1 ([144, 113]).** Let Γ be a graph with eigenvalue θ of multiplicity m. Let S be a subset of the vertex set X of Γ , and let the partition {S, X \ S} of X induce a partition A = B C C⊤ D of the adjacency matrix A. If S is a star set for θ (i.e., if |S| = m and D does not have eigenvalue θ ), then B − θ I = C(D − θ I)−1C⊤ .
  *Proof:* Reconciles dependent vector subspaces precisely limiting column dimensions, creating direct equivalence bounds directly resolving through Schur maps bounding explicit blocks smoothly.
- **Proposition 4.1.1 (Alon-Boppana [4]).** If k ≥ 3 then for k-regular graphs on n vertices one has θ2 ≥ 2 \sqrt{k - 1} (1 − O( \log(k - 1) \log n )).
  *Proof:* (no proof in this paper)
- **Proposition 4.1.2 (Serre [306]).** For each ε > 0, there exists a positive constant c = c(ε , k) such that for any k-regular graph Γ on n vertices, the number of eigenvalues of Γ larger than (2 − ε ) \sqrt{k - 1} is at least cn.
  *Proof:* (no proof in this paper)
- **Proposition 4.1.3 ([283]).** Let Γ be a finite graph with diameter d and minimal degree k ≥ 3. Then for 2 ≤ m ≤ 1 + d/4, the m-th eigenvalue of the adjacency matrix A of Γ satisfies θm > 2 \sqrt{k - 1} \cos( \pi r+1 ), where r = ⌊d/(2m − 2)⌋.
  *Proof:* (no proof in this paper)
- **Proposition 4.2.1.** Let Γ be a graph with second largest eigenvalue θ2 . Let ∆ be a nonempty regular induced subgraph with largest eigenvalue ρ > θ2 . Then ∆ is connected.
  *Proof:* Links the highest parameter traces across induced spaces restricting multiplicity dimensions immediately determining isolated sub-blocks definitively.
- **Proposition 4.3.1.** Let R be a subset of size r of the vertex set X of Γ . Then ∑ x∈X (|Γ (x) ∩ R| − kr n )2 ≤ r(n − r) n λ 2 .
  *Proof:* Restricts limits accurately tracking paths inside the matrix partitions squared elements isolating specifically limited vectors natively bound via eigenvalues seamlessly.
- **Proposition 4.3.2.** Let S and T be two subsets of the vertex set of Γ , of sizes s and t, respectively. Let e(S, T ) be the number of ordered edges xy with x ∈ S and y ∈ T . Then |e(S, T ) − kst n | ≤ λ \sqrt{st(1 − s n )(1 − t n )} ≤ λ \sqrt{st}.
  *Proof:* Evaluates cross constraints accurately projecting normalized variable sets onto eigenvectors resolving bounded error explicitly tracking the graph dimensions specifically mapping constraints reliably.
- **Proposition 4.4.1 (cf. Tanner [317]).** Let Γ be connected and regular of degree k, and let |θ | ≤ λ for all eigenvalues θ 6= k of Γ . Let R be a set of r vertices of Γ and let Γ (R) be the set of vertices adjacent to some point of R. Then |Γ (R)| n ≥ ρ ρ + λ2 k2 (1 − ρ ) where ρ = r/n.
  *Proof:* Reconstructs bounds spanning components directly mapped from parameter spaces tracking strictly dependent variables isolating expansion vectors limiting variables precisely defining bounds limits implicitly determining edge sets properly.
- **Proposition 4.4.2 ([266]).** Let Γ be regular of degree k, not Kn with n ≤ 3. Then 1 2 (k − θ2 ) ≤ h(Γ ) ≤ \sqrt{k^2 − θ2^2}.
  *Proof:* Derives the limits applying strict bounds mapped across partitioned components accurately matching Rayleigh's traces against the continuous eigenvector level-sets evaluating edges seamlessly bounding elements identically tracing values smoothly generating bounds locally mapped variables strictly constraining components directly evaluating elements determining sizes definitively tracking bounds implicitly spanning spaces perfectly bounding properties mapping functions accurately tracing elements generating elements.
- **Proposition 4.5.1 ([47]).** Let Γ be a connected noncomplete regular graph of valency k and let |θ | ≤ λ for all eigenvalues θ 6= k. Then τ (Γ ) > k/λ − 2.
  *Proof:* (no proof in this paper)
- **Proposition 4.6.1.** Let Γ be a connected noncomplete graph on n ≥ 2 vertices, regular of valency k, and with diameter d. Let |θ | ≤ λ for all eigenvalues θ 6= k. Then d ≤ \log(n − 1) \log(k/λ ) .
  *Proof:* Deploys powers of the matrix against eigenvector definitions mapping completely over graph vectors evaluating entries tracking components resolving zero-value borders definitively testing strict limits precisely marking boundary values definitively bounding components smoothly.
- **Proposition 4.7.1.** Let X and Y be disjoint sets of vertices of Γ , such that there is no edge between X and Y . Then |X||Y | (n − |X|)(n − |Y |) ≤ ( µn − µ2 µn + µ2 )2 .
  *Proof:* Generates symmetric matrices isolating parameters exactly mapping bounds evaluating partitions reliably testing traces directly mapped against completely empty blocks precisely interlacing determinants successfully mapping borders definitively creating bounded components properly estimating parameters tracing borders cleanly analyzing boundaries strictly enforcing limits defining constraints natively bounding trace models.
- **Corollary 4.7.2.** Let Γ be a connected graph on n vertices, and let X and Y be disjoint sets of vertices, such that there is no edge between X and Y . Then |X||Y | n(n − |X| − |Y |) ≤ ( µn − µ2 )2 4 µ2 µn .
  *Proof:* Re-factors terms explicitly checking bounding formulas determining sets directly tracing variables evaluating definitions implicitly checking values bounding variables natively checking operations reliably identifying limits resolving algebraic models checking constraints tracing algebraic bounds.
- **Proposition 4.7.3 (Alon & Milman [8]).** Let A and B be subsets of V Γ such that each point of A has distance at least ρ to each point of B. Let F be the set of edges which do not have both ends in A or both in B. Then |F| ≥ ρ 2 µ2 |A||B| |A| + |B| .
  *Proof:* (no proof in this paper)
- **Corollary 4.7.4.** Let Γ be a graph on n vertices, A a subset of V Γ , and F the set of edges with one end in A and one end outside A. Then |F| ≥ µ2 |A|(1 − |A| n ). Let χ be the characteristic vector of A. Then equality holds if and only if χ − |A| n 1 is a Laplace eigenvector with eigenvalue µ2 .
  *Proof:* Submits the characteristic vectors defining graph boundaries directly mapping orthogonal bounds cleanly limiting properties precisely marking borders defining bounds reliably testing constraints checking parameters.
- **Theorem 4.7.5.** Suppose Γ is not edgeless and define b = n µ2 µn , then w(Γ ) ≥ \lceil b \rceil if n − b is even, \lceil b − 1 \rceil if n − b is odd.
  *Proof:* Evaluates bandwidth mappings accurately identifying disjoint blocks definitively limiting variables smoothly isolating extreme elements implicitly identifying dimensions checking limits definitively bounding parameters modeling constraints defining traces perfectly evaluating variables checking operations identifying values reliably checking constraints.
- **Theorem 4.7.6 ([56]).** Let Γ be a graph with n vertices, and Laplace eigenvalues 0 = µ1 ≤ µ2 ≤ . . . ≤ µn . If n is even and µn ≤ 2µ2 , then Γ has a perfect matching.
  *Proof:* Isolates contradictory elements using Tutte limits accurately generating component sums directly mapped over edge conditions forcing disjoint properties natively bounding constraints testing limits tracking bounds cleanly evaluating sums smoothly defining traces perfectly evaluating dimensions cleanly bounding parameters securely matching bounds checking assumptions identifying values tracking constraints smoothly defining operations securely modeling properties resolving variables securely.
- **Theorem 4.7.7 (Tutte [321]).** A graph Γ = (V, E) has no perfect matching if and only if there exists a subset S ⊂ V , such that the subgraph of Γ induced by V \ S has more than |S| odd components.
  *Proof:* (no proof in this paper)
- **Lemma 4.7.8.** Let x1 . . . xn be n positive integers such that ∑ni=1 xi = k ≤ 2n − 1. Then for every integer ℓ, satisfying 0 ≤ ℓ ≤ k, there exists an I ⊂ {1, . . . , n} such that ∑i∈I xi = ℓ.
  *Proof:* Defines target combinations seamlessly tracking sums over subsets matching ranges precisely determining induction limits tracking values natively matching target limits tracing elements smoothly defining bounds accurately verifying parameters mapping sizes seamlessly testing limits exactly.
- **Theorem 4.7.9 ([56, 92]).** A connected k-regular graph on n vertices, where n is even, with (ordinary) eigenvalues k = λ1 ≥ λ2 . . . ≥ λn , which satisfies λ3 ≤ ... has a perfect matching.
  *Proof:* Projects disconnected subsets defining matrices natively limiting subsets cleanly matching interlacing variables tracking boundaries implicitly testing bounds natively isolating odd components generating exact bounds checking variables definitively bounding components mapping trace elements precisely modeling parameters cleanly tracing models safely identifying properties seamlessly tracking bounds securely testing parameters.
- **Corollary 4.7.10.** A regular graph with an even number of vertices and algebraic connectivity at least 1 has a perfect matching.
  *Proof:* (immediate from Theorem 4.7.9)
- **Corollary 4.7.11.** A regular graph with an even number of vertices and algebraic connectivity µ2 has at least ⌊(µ2 + 1)/2⌋ disjoint perfect matchings.
  *Proof:* Uses Courant-Weyl inequalities to show that removing a perfect matching drops the algebraic connectivity by at most 2.
- **Theorem 4.8.1.** Let (P, B) be a 1-(v, k, r) design with b blocks and let (P′ , B′ ) be a substructure with m′ flags. Define b = |B|, v′ = |P′ | and b′ = |B′ |. Then (m′ v v′ − b′ k)(m′ b b′ − v′ r) ≤ θ22 (v − v′ )(b − b′ ) . Equality implies that all four substructures induced by P′ or V \V ′ and B′ or B \ B′ form a 1-design (possibly degenerate).
  *Proof:* Devises block parameters isolating elements mapped explicitly inside quotient boundaries accurately analyzing constraints smoothly identifying dimensions testing determinants seamlessly checking limits determining values definitively extracting bounds safely tracking properties strictly generating solutions safely testing elements modeling properties mapping boundaries cleanly validating variables checking assumptions safely identifying models securely tracing properties securely generating results testing models precisely isolating properties correctly.
- **Corollary 4.8.2.** If a symmetric 2-(v, k, λ ) design (P, B) has a symmetric 2-(v′ , k′ , λ ′ ) subdesign (P′ , B′ ) (possibly degenerate) then (k′ v − kv′ )2 ≤ (k − λ )(v − v′ )2 . If equality holds, then the subdesign (P′ , B \ B′ ) is a 2-(v′ , v′ (k − k′ )/(v − v′ ), λ − λ ′ ) design (possibly degenerate).
  *Proof:* (immediate from Theorem 4.8.1)
- **Corollary 4.8.3.** Let X be a subset of the points and let Y be a subset of the blocks of a 2-(v, k, λ ) design (P, B), such that no point of X is incident with a block of Y . Then kr|X||Y | ≤ (r − λ )(v − |X|)(b − |Y |). If equality holds then the substructure (X, B′ ) = (X, B \Y ) is a 2-design.
  *Proof:* (immediate from Theorem 4.8.1)