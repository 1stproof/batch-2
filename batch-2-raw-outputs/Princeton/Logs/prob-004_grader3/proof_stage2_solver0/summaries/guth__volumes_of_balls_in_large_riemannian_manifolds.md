<!-- Generated 2026-05-31T01:51:30 -->
<!-- Source PDF: guth__volumes_of_balls_in_large_riemannian_manifolds.pdf (416761 bytes) -->
<!-- Citation: Guth, L. (2011). Volumes of balls in large Riemannian manifolds. Annals of Mathematics. -->

# Volumes of balls in large Riemannian manifolds (Guth, 2011)

## Definitions
(none)

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.** For each dimension n, there is a number δ(n) > 0 so that the following estimate holds. If (M n , g) is a complete Riemannian n-manifold with filling radius at least R, then V (R) ≥ δ(n)Rn .
  *Proof:* Constructs a mapping from the manifold to a rectangular nerve of a good cover, bounds the multiplicity of the cover and the volume of the image, and uses homological properties to show the fundamental class vanishes if the volume bound is violated.

- **Theorem 2.** For each dimension n, there is a number δ(n) > 0 so that the following estimate holds. Suppose that (M n , hyp) is a closed hyperbolic n-manifold and that g is another metric on M , and suppose that Vol(M, g) < δ(n)Vol(M, hyp). Let (M f, g̃) denote the universal cover of M with the metric induced from g. Then there is a point p ∈ M f so that the unit ball around p in (M f, g̃) has a larger volume than the unit ball in hyperbolic n-space. In other words, the following inequality holds: V(M ‹,g̃) (1) > VHn (1).
  *Proof:* Uses Lemma 9 to bound the simplicial norm of the fundamental class in the rectangular nerve, pulls it back to the manifold, and applies Thurston's lower bound on the simplicial volume of hyperbolic manifolds.

- **Corollary 1.** Let (M n , g) be a closed Riemannian manifold. Suppose that there is a degree 1 map from (M n , g) to the unit n-sphere with Lipschitz constant 1. Then V (R) ≥ δ(n)Rn for all R ≤ 1.
  *Proof:* Applies Theorem 1 using Gromov's result that the filling radius is at least that of the unit n-sphere.

- **Corollary 2 (systolic inequality).** Let (M n , g) be a closed aspherical Riemannian manifold. Suppose that the shortest noncontractible curve in (M n , g) has length at least S. Then V (S) ≥ δ(n)S n .
  *Proof:* Applies Theorem 1 using Gromov's lower bound for the filling radius in terms of the systole.

- **Corollary 3.** Let (M n , g) be a closed aspherical Riemannian manifold, and let V (R) measure the volumes of balls in the universal cover (M f, g̃). Then V (R) ≥ δ(n)Rn for all R.
  *Proof:* Applies Theorem 1 using Gromov's result that the universal cover has infinite filling radius.

- **Lemma 1.** Let (M n , g) be a complete Riemannian n-manifold, and let p be any point in M . Then there is a radius R so that B(p, R) is a good ball.
  *Proof:* Iteratively examines balls of exponentially decreasing radii, showing that failure of the reasonable growth condition would violate the unit density of Riemannian manifolds.

- **Lemma 2.** If (M n , g) is a closed Riemannian manifold, then it has a good cover.
  *Proof:* Applies the Vitali covering lemma to the set of scaled good balls covering the manifold.

- **Lemma 3.** If s < 1, and we look at any ball B(s) of radius s, not necessarily in our cover, then the number of balls Bi from our cover, with radius in the range (1/2)s ≤ ri ≤ 2s, intersecting B(s), is bounded by a dimensional constant C(n).
  *Proof:* Bounds the number of intersecting cover balls by comparing the volume of their disjoint scaled cores to the bounded volume of their union.

- **Lemma 4.** There are constants α(n), γ(n), depending only on n, that make the following estimate hold. For any open set U ⊂ M , any λ ≥ 0, and any w < (1/100), |MU (γ log(1/w) + λ)| ≤ e−αλ |Nw (U )|. Taking U = M , it follows that |M (λ)| < Ce−αλ |M |. If B is a good ball in our cover with radius r, then we have the following estimate : |MB (γ log(1/r) + λ)| ≤ e−αλ |B|.
  *Proof:* Partitions the cover into layers of disjoint balls and defines a core subset for each layer that intersects a bounded number of lower-layer balls. Uses the core's volume properties to establish exponential decay for the average volume of high-multiplicity intersections.

- **Lemma 5.** There are constants C(n) and β(n) > 0, depending only on n, so that the volume of φ(M ) ∩ Star(F ) obeys the following inequality : |φ(M ) ∩ Star(F )| < CV (1)r1 (F )n+1 e−βd(F ) . Also, |φ(M )| < C|M |.
  *Proof:* Combines the high-multiplicity volume bounds with the reasonable growth estimates of good balls to bound the image volume in the rectangular nerve.

- **Lemma 6.** If φ∗ ([M ]) = 0 in N , then the filling radius of (M n , g) is at most 1.
  *Proof:* Constructs a filling in L∞(M) using a fine triangulation of the nerve's filling chain and homotopes the Kuratowski embedding to it within a 1-neighborhood.

- **Lemma 7.** If (M, g) is a closed aspherical manifold with systole at least 1, then there is a map ψ : N → M so that the composition ψ ◦ φ : M → M is homotopic to the identity.
  *Proof:* Maps the nerve's 1-skeleton to M using the centers of covering balls, extends to higher simplices via the systole bound and asphericity, and explicitly constructs the homotopy.

- **Lemma 8.** For any β > 0 and any integer n > 0, there is a small positive ε(β, n) that makes the following statement true. Let z be an n-cycle in the rectangular complex N . Suppose that for every face F in N , |z ∩ Star(F )| < εr1 (F )n e−βd(F ) . Then [z] = 0 in N .
  *Proof:* Constructs a sequence of homologous cycles pushed into successively lower-dimensional skeletons of the rectangular nerve. Uses a pulling map near face boundaries to control the volume increase, ultimately pushing the cycle into the (n-1)-skeleton where it vanishes.

- **Theorem 1 (closed case).** For each dimension n, there is a number δ(n) > 0 so that the following estimate holds. If (M n , g) is a closed Riemannian n-manifold with filling radius greater than R, then V (R) ≥ δ(n)Rn .
  *Proof:* Combines the volume bounds on the rectangular nerve faces with Lemma 8 to show the fundamental cycle vanishes if V(1) is small, which by Lemma 6 forces the filling radius to be at most 1.

- **Lemma 9.** For each number V0 > 0 and each dimension n, there is a constant C(V0 , n) so that the following estimate holds. If (M, g) has V (1) < V0 , then the simplicial norm kφ∗ ([M ])k ≤ C(V0 , n)Vol(M, g).
  *Proof:* Modifies the sequence of homological surgeries from Lemma 8, distinguishing between thick and thin faces to handle the lack of an absolute volume bound. Applies the Federer-Fleming deformation theorem on thick faces to uniformly bound the volume stretch.

- **Theorem 1 (general case).** For each dimension n, there is a number δ(n) > 0 so that the following estimate holds : If (M n , g) is a complete Riemannian n-manifold with filling radius at least R, then V (R) ≥ δ(n)Rn .
  *Proof:* Extends the closed-manifold proof to complete manifolds by replacing the finite sequence of homological mappings in the nerve with an infinite sequence of cycles on locally finite chains.