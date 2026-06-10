<!-- Generated 2026-05-31T01:41:40 -->
<!-- Source PDF: cassels__rational_quadratic_forms.pdf (346818 bytes) -->
<!-- Citation: J.W.S. Cassels (1978). Rational Quadratic Forms. London Mathematical Society Monographs (Academic Press). -->

# Heights and quadratic forms: Cassels’ theorem and its generalizations (J.W.S. Cassels (1978). Rational Quadratic Forms. London Mathematical Society Monographs (Academic Press).)

## Definitions
*(No explicitly labeled definitions in this paper)*

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1 (Cassels’ Theorem).** Let F (X) = \sum_{i=1}^N \sum_{j=1}^N f_{ij} X_i X_j \in \mathbb{Z}[X] be an isotropic integral quadratic form in N ≥ 2 variables, then there exists x ∈ \mathbb{Z}^N \setminus \{0\} such that F (x) = 0 and \max_{1≤i≤N} |x_i| ≤ (3 \sum_{i=1}^N \sum_{j=1}^N |f_{ij}|)^{\frac{N−1}{2}}.
  *Proof:* Applies Minkowski's Linear Forms Theorem to find an anisotropic point, then uses its orthogonal reflection to contradict minimality.

- **Theorem 3.1.** Let K be a number field or a function field, and let F (X) be an isotropic quadratic form in N variables over K. Then there exists x ∈ K^N such that F (x) = 0 and h(x) \ll_{K,N} H(F )^{(N−1)/2}.
  *Proof:* Deduced as a direct implication of standard height inequalities applied to previous results over rational and algebraic function fields.

- **Theorem 4.1.** Let K be a number field, a function field of finite type, or Q, and let F be a nonzero quadratic form in N ≥ 2 variables over K. Let V ⊆ K^N be an M -dimensional vector space, 1 ≤ M ≤ N . Let L ≥ 1 be the dimension of a maximal totally isotropic subspace of the quadratic space (V, F ), and assume that L is greater than λ, the dimension of the radical of (V, F ). Then there exists a maximal totally isotropic subspace U ⊆ V such that H(U) \ll_{K,M,L,\lambda} H(F)^{(M-L)/2} H(V) \text{ if } K \neq \mathbb{Q}, \text{ and } H(F)^{(L-\lambda)(L-\lambda+1)/4(L-\lambda)} H(V)^{3+2} \text{ if } K = \mathbb{Q}.
  *Proof:* Uses Northcott's finiteness property to choose a subspace of minimal height over global fields, and arithmetic Bezout's theorem over $\mathbb{Q}$.

- **Theorem 5.1.** Let K be a number field, a function field of finite type, or Q, and let F be a nonzero quadratic form in N ≥ 2 variables over K. Let V ⊆ K^N be an M -dimensional vector space, 1 ≤ M ≤ N , so that the Witt index of the quadratic space (V, F ) is ω ≥ 1. Let λ = dim_K (V^⊥ ) and r = M − λ, the rank of F on V . There exists an orthogonal decomposition of the quadratic space (V, F ) of the form (7) with all components of bounded height.
  *Proof:* Derived as an application of the height bounds for totally isotropic subspaces from Theorem 4.1.

- **Theorem 5.2.** Let K be a number field, a function field over a perfect constant field of characteristic 6= 2, or Q. Let (V, F ) be a regular quadratic space over K with V ⊆ K^N of dimension M , 1 ≤ M ≤ N , N ≥ 2. Let σ be an element of the isometry group O(V, F ). Then either σ is the identity, or there exist an integer 1 ≤ l ≤ 2M − 1 and reflections τ_1 , ..., τ_l ∈ O(V, F ) such that (18) σ = τ_1 ◦ · · · ◦ τ_l , and for each 1 ≤ i ≤ l, (19) H(τ_i ) \ll_{K,M} H(F )^{M/3} H(V )^{M/2} H(σ)^{5M−1}.
  *Proof:* (no proof in this paper)

- **Conjecture 5.3.** Suppose that two nonsingular integral quadratic forms F and G in N ≥ 3 variables are integrally equivalent, i.e., F (AX) = G(X) for some matrix A ∈ GL_N (\mathbb{Z}). Then there exists such an integral equivalence A with |A| \ll_N (|F | + |G|)^{p(N )} , for some function p(N ), independent of F and G, where |A| is the sup-norm of A viewed as a vector in \mathbb{Z}^N.
  *Proof:* (no proof in this paper)

- **Theorem 6.1.** Consider a quadratic polynomial in N ≥ 2 variables with integer coefficients Q(X) = F (X) + L(X) + A, where F is a nonsingular integral quadratic form, L is a linear form, and A is an integer. Assume that Q has an integral zero x. Then there exists such a zero satisfying ...
  *Proof:* Uses geometry of numbers for $N=3,4$, the circle method for $N \ge 5$, and elementary methods for $N=2$.

- **Theorem 6.2.** Let K be a number field, F a quadratic form in N ≥ 2 variables over K, and V_1 , . . . , V_M ⊂ K^N proper subspaces of K^N , M ≥ 1. Suppose that there exists a point x ∈ K^N \setminus \cup_{i=1}^M V_i such that F (x) = 0. Then there exists such a point with H(x) \ll_{K,N,M} H(F )^{(N +1)/2}.
  *Proof:* Combines homogenization of the quadratic polynomial with Cassels'-type search bounds.

- **Theorem 6.3.** Let V ⊆ K^N be an L-dimensional vector space, 1 ≤ L ≤ N . Let F be a quadratic form in N variables defined over K. Let ω be the Witt index of the quadratic space (V, F ), λ the dimension of its radical V^⊥ , r = L − λ the rank of F on V , and let m = ω + λ be the dimension of a maximal totally isotropic subspace of (V, F ). Let Z(V, F ) = \{z ∈ V \setminus \{0\} : F (z) = 0\}. Let Z_K and M = M (Z_K ) be as in (21), (22) above. Suppose that Z(V, F ) \not\subseteq Z_K . Then there exist m linearly independent vectors x_1 , . . . , x_m in V over K such that x_1 , . . . , x_m ∈ Z(V, F ) \setminus Z_K , (23) h(x_1 ) ≤ h(x_2 ) ≤ · · · ≤ h(x_m ), and for each 1 ≤ n ≤ m, (24) ...
  *Proof:* First establishes the result for forms with a specific monomial, then extends to generic forms by splitting off a hyperbolic plane. Uses previous height bounds and Siegel's lemma to carefully control heights throughout.