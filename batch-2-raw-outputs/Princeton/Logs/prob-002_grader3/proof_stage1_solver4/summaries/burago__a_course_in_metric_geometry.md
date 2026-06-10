<!-- Generated 2026-05-31T02:19:38 -->
<!-- Source PDF: burago__a_course_in_metric_geometry.pdf (1873888 bytes) -->
<!-- Citation: Dmitri Burago, Yuri Burago, Sergei Ivanov (2001). A Course in Metric Geometry. American Mathematical Society. -->

# A Course in Metric Geometry (Burago, Burago, Ivanov, 2001)

## Definitions
- **Definition 1.1.1.** Let X be an arbitrary set. A function d : X × X → R ∪ {∞} is a metric on X if the following conditions are satisfied for all x, y, z ∈ X.
     (1) Positiveness: d(x, y) > 0 if x 6= y, and d(x, x) = 0.
     (2) Symmetry: d(x, y) = d(y, x).
     (3) Triangle inequality: d(x, z) ≤ d(x, y) + d(y, z).
- **Definition 1.1.3.** Let X and Y be two metric spaces. A map f : X → Y is called distance-preserving if |f (x)f (y)| = |xy| for any two points x, y ∈ X. A bijective distance-preserving map is called an isometry.
- **Definition 1.1.4.** A function d : X × X → R+ ∪ {+∞} is called a semi-metric if it satisfies all properties from Definition 1.1.1 of a metric except the requirement that d(x, y) = 0 implies x = y.
- **Definition 1.2.11.** Let V be a vector space. A function | · | : V → R is a norm on V if the following conditions are satisfied for all v, w ∈ V and k ∈ R.
     (1) Positiveness: |v| > 0 if v 6= 0, and |0| = 0.
     (2) Positive homogeneity: |kv| = |k||v|.
     (3) Subadditivity (triangle inequality): |v + w| ≤ |v| + |w|.
- **Definition 1.2.17.** A scalar product is a symmetric bilinear form F whose associated quadratic form is positive definite, i.e., F (x, x) > 0 for all x 6= 0.
- **Definition 1.2.18.** Apnorm associated with a scalar product h·, ·i is defined by the formula |v| = hv, vi. A norm is called Euclidean if it is associated with some scalar product.
- **Definition 1.3.1.** Let X be a metric space, x ∈ X and r > 0. The set formed by the points at distance less than r from x is called an (open metric) ball of radius r centered at x. We denote this ball by Br (x). Similarly, a closed ball B r (x) is the set of points whose distances from x are less than or equal to r.
- **Definition 1.3.5.** A sequence {xn }∞  n=1 of points of a topological space X is said to converge to a point x ∈ X if for any neighborhood U of x there is a number n0 such that xn ∈ U for all n ≥ n0 .
- **Definition 1.4.1.** Let X and Y be metric spaces. A map f : X → Y is called Lipschitz if there exists a C ≥ 0 such that |f (x1 )f (x2 )| ≤ C|x1 x2 | for all x1 , x2 ∈ X.
- **Definition 1.4.4.** Let X and Y be metric spaces. A map f : X → Y is called locally Lipschitz if every point x ∈ X has a neighborhood U such that f |U is Lipschitz.
- **Definition 1.4.6.** Let X and Y be metric spaces. A map f : X → Y is called bi-Lipschitz if there are positive constants c and C such that
                        c|x1 x2 | ≤ |f (x1 )f (x2 )| ≤ C|x1 x2 |
for all x1 , x2 ∈ X.
- **Definition 1.4.7.** Two metrics d1 and d2 on the same set X are called Lipschitz equivalent if there are positive constants c and C such that
                       c · d1 (x, y) ≤ d2 (x, y) ≤ C · d1 (x, y)
for all x, y ∈ X.
- **Definition 1.5.1.** A sequence {xn } in a metric space is called a Cauchy sequence if |xn xm | → 0 as n, m → ∞. The precise meaning of this is the following: for any ε > 0 there exists an n0 such that |xn xm | < ε whenever n ≥ n0 and m ≥ n0 .
    A metric space is called complete if every Cauchy sequence in it has a limit.
- **Definition 1.5.11.** The space X̃ from the above theorem is called the completion of X.
- **Definition 1.5.12.** A set Y in a topological space X is nowhere dense if the closure of Y has empty interior.
- **Definition 1.6.1.** Let X be a metric space and ε > 0. A set S ⊂ X is called an ε-net if dist(x, S) ≤ ε for every x ∈ X.
    X is called totally bounded if for any ε there is a finite ε-net in X.
- **Definition 1.6.7.** A metric space is said to be boundedly compact if all closed bounded sets in it are compact.
- **Definition 1.7.1.** Let X be an arbitrary set. A set A of subsets of X is called a σ-algebra if it satisfies the following conditions:
     (1) ∅ and X are elements of A;
     (2) If A, B ∈ A, then A \ B ∈ A;
     (3) If {Ai }i∈I isSa finite or countable collection of elements of A, then
         their union i∈I Ai is also an element of A.
- **Definition 1.7.3.** A measure on a σ-algebra A is a function µ : A → R+ ∪ {+∞} such that
     (1) µ(∅) = 0; and
     (2) if {Ai } is a finite or countable
                                        S collection
                                                P of elements of A and the
          sets Ai are disjoint, then µ( Ai ) = µ(Ai ).
- **Definition 1.7.7.** Let X be a metric space and d be a nonnegative real number.
    For a finite or countable
                     S        covering {Si }i∈I of X (that is, a collection of
sets such that X ⊂ Si ), define its d-weight wd ({Si }) by the formula
                                      X
                         wd ({Si }) =   (diam Si )d .
                                       i
If d = 0, substitute each (if any) 00 term in the formula by 1.
   For an ε > 0 define µd,ε (X) by
                           ©                                   ª
            µd,ε (X) = inf wd ({Si }) : diam(Si ) < ε for all i .
The infimum is taken over all finite or countable coverings of X by sets of diameter < ε; if no such covering exists, then the infimum is +∞.
   The d-dimensional Hausdorff measure of X is defined by the formula
                         µd (X) = C(d) · lim µd,ε (X)
                                           ε→0
where C(d) is a positive normalization constant.
- **Definition 1.7.17.** The value d0 from Theorem 1.7.16 is called the Hausdorff dimension of X and denoted by dimH (X).
- **Definition 2.1.6.** A metric that can be obtained as the distance function associated to a length structure is called an intrinsic, or length, metric. A metric space whose metric is intrinsic is called a length space.
- **Definition 2.1.10.** A length structure is said to be complete if for every two points x, y there exists an admissible path joining them whose length is equal to dL (x, y); in other words, a length structure is complete if there exists a shortest path between every two points.
- **Definition 2.3.1.** Let (X, d) be a metric space and γ be a path in X, i.e., a continuous map γ : [a, b] → X. Consider a partition Y of [a, b]), that is, a finite collection of points Y = {y0 , ..., yN } such that a = y0 ≤ y1 ≤ y2 ≤ · · · ≤ yN = b. The supremum of the sums
                                   N
                                   X
                         Σ(Y ) =         d(γ(yi−1 ), γ(yi )).
                                   i=1
over all the partitions Y is called the length of γ (with respect to the metric d) and denoted Ld (γ). A curve is said to be rectifiable if its length is finite.
- **Definition 2.4.7.** A point z ∈ X is called a midpoint between points x, y in a metric space (X, d) if d(x, z) = d(z, y) = 12 d(x, y).
- **Definition 2.5.1.** An (unparameterized) curve is an equivalence class of the minimal equivalence relation satisfying the following: paths γ1 : I1 → X and γ2 : I2 → X are equivalent whenever there exists a nondecreasing continuous map ϕ from I1 onto I2 such that γ1 = γ2 ◦ ϕ.
- **Definition 2.5.4.** A curve γ : [a, b] → X is called simple if the pre-image of every point is an interval.
- **Definition 2.5.7.** A parameterization γ : I → X is natural if L(γ, t, t0 ) = t − t0 for all t, t0 ∈ I.
- **Definition 2.5.13.** A sequence of curves uniformly converges to a curve γ if they admit parameterizations (with the same domain) that uniformly converge to a parameterization of γ.
- **Definition 2.5.15.** A curve γ : [a, b] → X is a called a shortest path if its length is minimal among the curves with the same endpoints, in other words L(γ1 ) ≥ L(γ) for any curve γ1 connecting γ(a) and γ(b).
- **Definition 2.5.21.** A topological space X is called locally compact if every point of X has a pre-compact neighborhood.
- **Definition 2.5.27.** Let X be a length space. A curve γ : I → X is called a geodesic if for every t ∈ I there exists an interval J containing a neighborhood of t in I such that γ|J is a shortest path.
- **Definition 2.7.1.** Let (X, d) be a metric space and γ : I → X a curve. The speed of γ at t ∈ I, denoted by vγ (t), is defined by
                                        d(γ(t), γ(t + ε))
                        vγ (t) := lim
                                 ε→0           |ε|
if the limit exists.
- **Definition 3.1.12.** Let (X, d) be a metric space and let R be an equivalence relation on X. The quotient semi-metric dR is defined as
                                 k
                                 X
              dR (x, y) = inf{         d(pi , qi ) : p0 = x, qk = y, k ∈ N}
                                 i=1
where the infimum is taken over all choices of {pi } and {qi } such that qi is R-equivalent to pi+1 for all i = 1, . . . , k − 1.
- **Definition 3.1.15.** Let (Xα , dα ) be a collection of length spaces. Consider the disjoint union ∪α Xα . We introduce a length metric d on this disjoint union defining d(x, y) by the following rule:
    If x, y ∈ Xα for some α, then d(x, y) = dα (x, y);
   Otherwise, d(x, y) = ∞. The metric d will be referred to as the length metric of disjoint union.
- **Definition 3.2.4.** Let a topological space (P, d) be covered by a collection of length spaces (Pα , dα ), each isometric to a simplex (or a convex polyhedron). Assume that for any two simplexes Pα and Pβ their intersection Pα ∩ Pβ is a face in both of them, and that the restrictions of the metrics of Pα and Pβ to Pα ∩ Pβ coincide. Consider the maximal metric d majorized by all metrics dα . The length space (P, d) is called a polyhedral space, or, more precisely, a Euclidean polyhedral space.
- **Definition 3.2.9.** A (metrized) graph is the result of gluing of a disjoint collection of metric segments {Ei } and points {vj } (regarded with the length metric of disjoint union) along an equivalence relation R defined on the union of the set {vj } and the set of the endpoints of the segments.
- **Definition 3.2.20.** The restriction to G of the intrinsic distance associated with the length structure of a Cayley graph is called the word metric on G (with respect to a given set of generators).
- **Definition 3.3.1.** Let X and Y be two metric spaces. A map f : X → Y is called an isometry onto its image if it preserves distance. The latter means that |f (x)f (y)| = |xy| for any two points x, y ∈ X (and thus it is automatically injective).
    A map that is surjective and preserves distance is called an isometry. Two spaces are said to be isometric if there exists an isometry from one to the other.
- **Definition 3.3.2.** A length space X is said to be homogeneous if for every x, y ∈ X there exists an isometry I : X → X such that I(x) = y.
- **Definition 3.3.4.** A metric spaces X is said to be locally isometric to a homogeneous space Y if each point in X possesses a neighborhood isometric to an open set in Y . Spaces locally isometric to a Euclidean space are said to be flat.
- **Definition 3.3.5.** One says that a group G acts on a set X if there is a map ϕ : G × X → X, which we abbreviate as ϕ(g, x) = g(x), such that
    (i) gh(x) = g(h(x)) and
    (ii) e(x) = x
    for every g, h ∈ G, x ∈ X. Here e is the unit of G.
- **Definition 3.4.1.** A map f : X → Y is called a local isometry at x ∈ X if x has a neighborhood Ux such that (the restriction of) f maps Ux isometrically onto an open set Uy in Y . A map which is a local isometry at every point is called a local isometry.
- **Definition 3.4.13.** Let a group G act on a set X. This action is said to be free if gx 6= x for all x ∈ X, g ∈ G \ {e}.
- **Definition 3.4.14.** Let a group G act on a topological space X. This action is said to be totally discontinuous if every point x has a neighborhood U such that gU ∩ U = ∅ for all g ∈ G such that gx 6= x.
- **Definition 3.5.1.** A map f between two length spaces is called an arcwise isometry if L(γ) = L(f (γ)) for every path γ.
- **Definition 3.6.5.** A subset A in a metric space (X, d) is said to be convex if the restriction of d to A is strictly intrinsic and finite.
- **Definition 3.6.6.** Suppose that the metric of X is strictly intrinsic. A set A in X is said to be locally convex if every point x ∈ A has a neighborhood U in A such that for every two points y, z ∈ U , there is a shortest path between y and z contained in A.
- **Definition 3.6.12.** Let X be a metric space with diam(X) ≤ π. The cone metric dc on Con(X) is given by the formula
                            p
(3.1)            dc (p, q) = t2 + s2 − 2ts cos(d(x, y)),
where p, q ∈ Con(X), p = (x, t), q = (y, s).

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 1.1.5.** Let d be a semi-metric on X. Introduce an equivalence relation Rd on X: set xRd y iff d(x, y) = 0. Since d(x, y) = d(x1 , y1 ) whenever xRd x1 and yRd y1 , the projection dˆ of d onto the quotient space X̂ = X/Rd is well-defined. Then (X̂, dˆ) is a metric space.
  *Proof:* (no proof in this paper)
- **Proposition 1.2.22.** Every n-dimensional Euclidean space is isomorphic to Rn . This means that there is a linear isomorphism f : Rn → V such that hf (x), f (y)i = hx, yi for all x, y ∈ Rn . In particular, these spaces are isometric.
  *Proof:* Expresses the vectors via an orthonormal basis and maps linearly to components in $\mathbb{R}^n$.
- **Proposition 1.3.6.** Let X and Y be metric spaces. Then
     (1) A sequence in X cannot have more than one limit.
     (2) A point x ∈ X is an accumulation point of a set S ⊂ X (i.e., belongs to the closure of S) if and only if there exists a sequence {xn }∞n=1 such that xn ∈ S for all n and xn → x. In particular, S is closed if and only if it contains all limits of sequences contained within S.
     (3) A map f : X → Y is continuous at a point x ∈ X if and only if f (xn ) → f (x) for any sequence {xn } converging to x.
  *Proof:* (no proof in this paper)
- **Proposition 1.4.3.** (1) All Lipschitz maps are continuous.
     (2) If f : X → Y and g : Y → Z are Lipschitz maps, then g ◦ f is Lipschitz and dil(g ◦ f ) ≤ dil f · dil g.
     (3) The set of real-valued Lipschitz functions on a metric space (and, more generally, the set of Lipschitz functions from a metric space to a normed space) is a vector space. One has dil(f +g) ≤ dil f +dil g, dil(λf ) = |λ| dil f for any Lipschitz functions f and g and λ ∈ R.
  *Proof:* (no proof in this paper)
- **Theorem 1.4.11.** 1. Two norms on a vector space determine the same topology if and only if they are Lipschitz equivalent;
    2. All norms on a finite-dimensional vector space are Lipschitz equivalent.
  *Proof:* (no proof in this paper)
- **Proposition 1.5.5.** Let X be a metric space and Y ⊂ X. Then
     (1) If Y is complete, then Y is closed in X.
     (2) If X is complete and Y is closed in X, then Y is complete.
  *Proof:* (no proof in this paper)
- **Proposition 1.5.9.** Let X be a metric space and X 0 a dense subset of X. Let Y be a complete space and f : X 0 → Y a Lipschitz map. Then there exists a unique continuous map f˜ : X → Y such that f˜|X 0 = f . Moreover f˜ is Lipschitz and dil f˜ = dil f .
  *Proof:* Defines the extension point-wise as the limit of Cauchy sequences in the complete space $Y$, preserving the Lipschitz bound.
- **Theorem 1.5.10.** Let X be a metric space. Then there exists a complete metric space X̃ such that X is a dense subspace of X̃. It is essentially unique in the following sense: if X̃ 0 is another space with these properties, then there exists a unique isometry f : X̃ → X̃ 0 such that f |X = id.
  *Proof:* Equips the set of Cauchy sequences with a semi-metric using limits of distances, projects to equivalence classes, and uses Proposition 1.5.9 for unique extension.
- **Theorem 1.5.13 (Baire’s theorem).** A complete metric space cannot be covered by countably many nowhere dense subsets. Moreover, a union of countably many nowhere dense subsets has a dense complement.
  *Proof:* Constructs a nested sequence of closed balls avoiding each nowhere dense set, producing a Cauchy sequence whose limit evades the union.
- **Theorem 1.6.5.** Let X be a metric space. Then the following statements are equivalent:
      (1) X is compact.
      (2) Any sequence in X has a converging subsequence.
      (3) Any infinite subset of X has an accumulation point.
      (4) X is complete and totally bounded.
  *Proof:* (no proof in this paper)
- **Proposition 1.6.6.** Let X and Y be Hausdorff topological spaces. Then
      (1) If S ⊂ X is a compact set, then S is closed in X.
      (2) If X is compact and S ⊂ X is closed in X, then S is compact.
      (3) If {Xn }∞n=1 is aTsequence of compact sets such that Xn+1 ⊂ Xn for
          all n, then the ∞  n=1 Xn 6= ∅.
      (4) A subset of Rn is compact if and only if it is closed and bounded.
      (5) If X is compact and f : X → Y is a continuous map, then f (X) is a compact set.
      (6) If X is compact and f : X → Y is bijective continuous map, then f is a homeomorphism.
      (7) If X is compact and f : X → R is a continuous function, then f attains its maximum and minimum.
  *Proof:* (no proof in this paper)
- **Theorem 1.6.11 (Lebesgue’s Lemma).** Let X be a compact metric space, and let {Uα }α∈A be an open covering of X. Then there exists a ρ > 0 such that any ball of radius ρ in X is contained in one of the sets Uα .
  *Proof:* Defines a nonexpanding, strictly positive radius function for subsets and leverages compactness to extract its minimum.
- **Theorem 1.6.12.** Let X and Y be metric spaces and let X be compact. Then every continuous map f : X → Y is uniformly continuous, i.e., for every ε > 0 there is a δ > 0 such that for all x1 , x2 ∈ X such that |x1 x2 | < δ one has |f (x1 )f (x2 )| < ε.
  *Proof:* Applies Lebesgue's lemma to the open covering formed by pre-images of small balls.
- **Theorem 1.6.14.** A compact metric space cannot be isometric to a proper subset of itself. In other words, if X is a compact space and f : X → X is a distance-preserving map, then f (X) = X.
  *Proof:* Assumes an uncovered point exists and derives a contradiction by adding it to the image of a maximal $\varepsilon$-separated set.
- **Theorem 1.6.15.** Let X be a compact metric space. Then
      (1) Any nonexpanding surjective map f : X → X is an isometry.
      (2) If a map f : X → X is such that |f (x)f (y)| ≥ |xy| for all x, y ∈ X, then f is an isometry.
  *Proof:* (1) Minimizes the total pairwise distance over finite $\varepsilon$-nets to show nonexpanding surjections must strictly preserve all inter-point distances. (2) Applies the first part to the inverse map acting on a dense image.
- **Theorem 1.7.5 (Lebesgue).** There exists a unique Borel measure mn over Rn which is invariant under parallel translations and such that mn ([0, 1]n ) = 1.
  *Proof:* (no proof in this paper)
- **Proposition 1.7.8.** Let X and Y be metric spaces, and let A and B be subsets of X. Then
     (1) If A ⊂ B, then µd (A) ≤ µd (B).
             S       P
     (2) µd ( Ai ) ≤   µd (Ai ) for any finite or countable collection of sets Ai ⊂ X.
     (3) If dist(A, B) > 0, then µd (A ∪ B) = µd (A) + µd (B).
     (4) If f : X → Y is a Lipschitz map with a Lipschitz constant C, then µd (f (X)) ≤ C d · µd (X).
     (5) If f : X → Y is a C-homothety, i.e., |f (x1 )f (x2 )| = C|c1 x2 | for all x1 , x2 ∈ X, then µd (f (X)) = C d · µd (X).
  *Proof:* (no proof in this paper)
- **Theorem 1.7.9.** For any metric space X and any d ≥ 0, µd is a measure on the Borel σ-algebra of X.
  *Proof:* (no proof in this paper)
- **Theorem 1.7.12.** 0 < µn (I n ) < ∞.
  *Proof:* (no proof in this paper)
- **Theorem 1.7.14 (Vitali’s Covering Theorem).** Let X be a bounded set in Rn and let B be a collection of closed balls in Rn such that for every x ∈ X and ε > 0 there is a ball B ∈ B such that x ∈ B and diam(B) < ε. Then B contains a finite or countable subcollection {Bi } of disjoint balls which covers X upSto a set of zero measure, i.e., such that Bi ∩ Bj = ∅ if i 6= j and µn (X \ i Bi ) = 0.
  *Proof:* Constructs a sequence of disjoint balls greedily to maintain diameter ratios, then bounds the remainder by proving unselected balls belong to bounded expansions.
- **Corollary 1.7.15.** The normalization constant for the n-dimensional Hausdorff measure equals the volume of the Euclidean n-ball of diameter 1.
  *Proof:* Employs Vitali's covering theorem and Bieberbach's inequality to bound the measure of the unit cube directly from above and below.
- **Theorem 1.7.16.** For a metric space X there exists a d0 ∈ [0, +∞] such that µd (X) = 0 for all d > d0 and µd (X) = ∞ for all d < d0 .
  *Proof:* Uses finite covers to show the sum ratio forces the limit to zero or infinity depending on the scaling exponent $d$.
- **Proposition 1.7.19.** Let X be a metric space. Then
     (1) If Y ⊂ X, then dimH (Y ) ≤ dimH (X).
     (2) If X is covered by a finite or countable collection {Xi } of its subsets, then dimH (X) = supi dimH (Xi ).
     (3) If f : X → Y is a Lipschitz map, then dimH (f (X)) ≤ dimH (X). In particular, bi-Lipschitz equivalent metric spaces have equal Hausdorff dimensions.
     (4) dimH (Rn ) = dimH (I n ) = n.
  *Proof:* (no proof in this paper)
- **Proposition 2.3.4.** The length structure L = Ld induced by a metric d possesses the following properties:
    (i) Generalized triangle inequality: L(γ) ≥ d(γ(a), γ(b)).
    (ii) Additivity: if a < c < b, then L(γ, a, c) + L(γ, c, b) = L(γ). In particularly, L(γ, a, c) is a nondecreasing function of c.
    (iii) If γ is rectifiable, the function L(γ|[c,d] ) = L(γ, c, d) is continuous in c and d.
    (iv) L is a lower semi-continuous functional on the space of continuous maps of [a, b] in X with respect to point-wise convergence, and hence with respect to the uniform (i.e., C 0 -) topology. This means that if a sequence of rectifiable paths γi (with the same domain) is such that γi (t) converges to γ(t) (as i → ∞, for every t in the domain), then lim inf L(γi ) ≥ L(γ).
  *Proof:* Verifies the properties from the sequential sum definitions, using the triangle inequality to pass supremum limits and bound errors.
- **Proposition 2.3.12.** Let (X, d) be a metric space and db be the intrinsic metric induced by d.
     (1) If γ is a rectifiable curve in (X, d), then Ldb(γ) = Ld (γ).
     (2) The intrinsic metric induced by db coincides with d.b In other words, inducing a length metric is an idempotent operation.
  *Proof:* Combines bounds obtained from point-wise partitions and limits to assert equal induced lengths and metrics.
- **Proposition 2.4.1.** Let (X, d) be a length space and db be the intrinsic metric induced by d. Then db = d.
  *Proof:* Exploits bounds to show induced distances can be bounded from both above and below by the intrinsic distances.
- **Theorem 2.4.3.** If L is a lower semi-continuous length structure, then L coincides with the length structure induced by its intrinsic metric d = dL on all curves admissible for L: L(γ) = Ld (γ). As usual, the semi-continuity means that if a sequence of paths γi (t) pointwise converges to γ(t), then lim inf L(γi ) ≥ L(γ).
  *Proof:* Discretizes the curve to find short connecting curves approximating the metric, passing to a point-wise limit to apply the semi-continuity assumption.
- **Lemma 2.4.8.** If d is a strictly intrinsic metric, then for every two points x, y there exists a midpoint z.
  *Proof:* Applies the continuous length parameterization of a shortest path to directly identify a halfway point.
- **Lemma 2.4.10.** If d is an intrinsic metric, then, given a positive ε, for every two points x, y ∈ X there exists an ε-midpoint z, that is, a point z such that |2d(x, z) − d(x, y)| ≤ ε and |2d(y, z) − d(x, y)| ≤ ε. In other words, if 2r > d(x, y), then the balls Br (x) and Br (y) have a nonempty intersection.
  *Proof:* Examines a nearly shortest path realizing the distance and uses its length continuity to isolate the approximated midpoint.
- **Corollary 2.4.12.** Given a positive ε and two points x, y ∈ X in a space with a strictly intrinsic metric d, there exists a finite sequence of points x1 = x, x2 , . . . , xk = y such that every two neighboring points in this sequence are ε-close (that is, d(xi , xi+1 ) ≤ ε for all I = 1, . . . , k − 1) and Pk−1 i=1 d(xi , xi+1 ) = d(x, y).
  *Proof:* (no proof in this paper)
- **Theorem 2.4.16.** Let (X, d) be a complete metric space.
    1. If for every x, y ∈ X there exists a midpoint, then d is strictly intrinsic.
    2. If for every x, y ∈ X and every positive ε there exists an ε-midpoint, then d is intrinsic.
  *Proof:* Iteratively constructs a dense set of dyadic midpoint approximations, then uses uniform Lipschitz extensions via completeness to produce continuous interpolating paths.
- **Corollary 2.4.17.** A complete metric space (X, d) is a length space iff, given a positive ε and two points x, y ∈ X, there exists a finite sequence of points x1 = x1 , x2 , . . . , xk = y such that every two neighboring points in this sequence are ε-close (i.e., d(xi , xi+1 ) ≤ ε for all i = 1, . . . , k − 1) and Pk−1 i=1 d(xi , xi+1 ) < d(x, y) + ε.
  *Proof:* (no proof in this paper)
- **Proposition 2.5.9.** Every rectifiable curve γ : [a, b] → X can be represented in the form γ = γ̄ ◦ ϕ where γ̄ : [0, L(γ)] → X is a natural parameterization and ϕ is a nondecreasing continuous map from [a, b] onto [0, L(γ)].
  *Proof:* Constructs a continuous, non-decreasing length function as the new parameter to inherently unit-speed map the curve image.
- **Theorem 2.5.14 (Arzela–Ascoli Theorem).** In a compact metric space, any sequence of curves with uniformly bounded lengths contains a uniformly converging subsequence.
  *Proof:* Unit-speed reparameterizes the curves to bound their uniform Lipschitz constants, then extracts limits across a dense subset using a diagonal process.
- **Proposition 2.5.17.** If shortest paths γi in a length space (X, d) converge to a path γ as i → ∞, then γ is also a shortest path.
  *Proof:* Uses the lower semi-continuity of length to prove the limit preserves distance equality.
- **Proposition 2.5.19.** Let (X, d) be a compact metric space and let x, y ∈ X be points that can be connected by at least one rectifiable curve. Then there exists a shortest path between x and y.
  *Proof:* Extracts a convergent subsequence of paths nearing the infimum length using Arzela-Ascoli, evaluating the limit's length via semi-continuity.
- **Corollary 2.5.20.** Let (X, d) be a boundedly compact metric space. Then for every two points x, y ∈ X connected by a rectifiable curve there exists a shortest path between x and y.
  *Proof:* Localizes the search into a single compact closed ball and delegates to the preceding proposition.
- **Proposition 2.5.22.** If (X, d) is a complete locally compact length space, then every closed ball in X is compact (and hence X is boundedly compact).
  *Proof:* Investigates the supremum of radii of compact balls, refuting finite values by packing finite $\varepsilon$-nets.
- **Theorem 2.5.23.** Let (X, d) be a complete locally compact length space. Then this space is strictly intrinsic: for every x, y ∈ X such that d(x, y) < ∞ there exists a shortest path γ connecting x and y, i.e., a curve γ : [a, b] → X such that γ(a) = x, γ(b) = y and L(γ) = d(x, y).
  *Proof:* (no proof in this paper)
- **Theorem 2.5.28 (Hopf–Rinow–Cohn-Vossen Theorem).** For a locally compact length space X, the following four assertions are equivalent:
      (i) X is complete.
     (ii) X is boundedly compact, i.e., every closed metric ball in X is compact.
     (iii) Every geodesic γ : [0, a) → X can be extended to a continuous path γ : [0, a] → X.
     (iv) There is a point p ∈ X such that every shortest path γ : [0, a) → X with γ(0) = p can be extended to a continuous path γ : [0, a] → X.
  *Proof:* Assumes non-compact bounding to sequence paths approaching critical bounds, extracting a generalized extension point limit to derive a contradiction.
- **Lemma 2.6.1.** If X is a connected metric space, then µ1 (X) ≥ diam X.
  *Proof:* Reduces the cover to generic open chains, forming points to link endpoints via triangle inequalities bounding the combined sums.
- **Theorem 2.6.2.** Let X be a metric space, γ : [a, b] → X a simple curve. Then L(γ) = µ1 (γ([a, b])).
  *Proof:* Frames upper bounds via equal-length arc partitions, and pairs with lower bounds derived directly from applying Lemma 2.6.1 to subset segments.
- **Theorem 2.7.4.** Let (X, d) be a metric space, γ : [a, b] → X a rectifiable curve. Then for almost all t ∈ [a, b] (i.e., for all t except a set of zero measure) the following holds: either
                                    L(γ|[t−ε,t+ε0 ] )
                            lim inf                   = 0,
                              0
                            ε,ε →0+    ε + ε0
or
                                d(γ(t − ε), γ(t + ε0 ))
                          lim                           = 1.
                           0
                        ε,ε →0+    L(γ|[t−ε,t+ε0 ] )
  *Proof:* Sets a positive measure assumption over failing points to build a contradictory cover bound mapped by Vitali's covering theorem.
- **Corollary 2.7.5.** If γ is as in Theorem 2.7.4, then for almost all t ∈ [a, b] either
                                  L(γ|[t,t+ε] )
                          lim inf               = 0,
                            ε→0        |ε|
or
                              d(γ(t), γ(t + ε))
                         lim                     =1
                        ε→0      L(γ|[t,t+ε] )
(if ε < 0, the interval [t, t + ε] in the denominator of the last formula should be interpreted as [t + ε, t]).
  *Proof:* (immediate from Theorem 2.7.4)
- **Theorem 2.7.6.** Let X be a metric space; γ : [a, b] → X is a Lipschitz curve. Then the speed vγ (t) exists for almost all t ∈ [a, b] and L(γ) = Rb a vγ (t) dt where R is the Lebesgue integral.
  *Proof:* Interprets fractional limits linking length arc functions over intervals to substitute continuous derivatives using Lipschitz integration.
- **Lemma 3.1.1.** Let a topological space X be covered by a collection (not necessarily finite or countable) of open sets {Xα }. Assume that each Xα is equipped with a length structure Lα and that these structures agree. The latter assumption means that, if a curve γ belongs to the intersection of Xα and Xβ , then Lα (γ) = Lβ (γ).
    Then there exists a unique length structure L on X whose restriction to every Xα is Lα . Moreover, if X is connected and all intrinsic metrics induced by Lα on Xα are finite, then so is L.
  *Proof:* Assembles length sequentially over localized sub-path spans to compile uniquely preserved length maps globally.
- **Corollary 3.1.2.** Consider two intrinsic metrics d1 and d2 defined on the same set X and inducing the same topology. Assume that every point x ∈ X has a neighborhood Ux such that the restrictions of the metrics to this neighborhood coincide: for every p, q ∈ Ux , d1 (p, q) = d2 (p, q). Then d1 = d2 .
  *Proof:* (no proof in this paper)
- **Proposition 3.1.5.** If a complete metric d on a set X is not intrinsic, then there exists another metric d1 on X such that d 6= d1 but every point has a neighborhood where d and d1 coincide.
  *Proof:* Generates an alternative local metric bounded by chained epsilon-steps, mapping identical bounds to non-intrinsic divergence zones.
- **Lemma 3.1.23.** Let b : X × X → R+ ∪ {+∞} be an arbitrary function. Consider the class D of all semi-metrics d on X such that d ≤ b, i.e., d(x, y) ≤ b(x, y) for all x, y ∈ X. Then D contains a unique maximal semi-metric dm such that dm ≥ d for all d ∈ D.
  *Proof:* Fixes the maximal distance function trivially via the supremum point-wise operation confirming the overarching triangle inequality directly.
- **Corollary 3.1.24.** Let a set X be covered by a collection of subsets {Xα } each carrying a semi-metric dα . Consider the class D of all semi-metrics d (possibly taking infinite values) such that d(x, y) ≤ dα (x, y) whenever x, y ∈ Xα . Then D contains a unique maximal semi-metric dm such that dm (x, y) ≥ d(x, y) for all d ∈ D and x, y ∈ X. If all dα are intrinsic (semi-) metrics, then so is dm .
  *Proof:* (immediate from Lemma 3.1.23)
- **Theorem 3.1.27.** Let (X, d) be a metric space and R an equivalence relation on X. Consider the function bR on X × X defined by
                         (
                           0       if x is R-equivalent to y,
             bR (x, y) =
                           d(x, y) otherwise.
Then the maximal semi-metric among those not exceeding bR coincides with the semi-metric dR obtained by gluing (X, d) along R as in Definition 3.1.12.
  *Proof:* Demonstrates overlapping chained sums matching both bounded distance inequalities precisely to confirm mutual identities.
- **Lemma 3.3.6.** d coincides with the quotient metric dRG .
  *Proof:* Translates disjoint distance sequences using sequential group mappings linking representative points structurally inside unbroken paths.
- **Theorem 3.4.11.** If a topological space Y is a connected, locally arcwise connected and locally simply connected in the large, then there exists a universal covering f : X → Y . A universal covering is unique up to an equivalence.
  *Proof:* (no proof in this paper)
- **Proposition 3.4.15.** Let a group G act on a topological space X freely and totally discontinuously. Then the projection X → X/G is a covering map. Moreover this is a regular covering and the group of its deck transformations coincides with G.
  *Proof:* Maps the group shifts evenly onto open subsets preserving disjoint neighborhood structures over locally bijective covers.
- **Proposition 3.4.16.** Let f : X → Y be a regular covering and G its group of deck transformations. Then the length metrics on Y are in 1- 1 correspondence with the G-invariant length metrics on X so that for corresponding metrics dX on X and dY on Y f is a local isometry from (X, dX ) to (Y, dY ).
  *Proof:* (no proof in this paper)
- **Lemma 3.4.17.** Let f : X → Y be a local isometry of a complete length space X. Given a geodesic (shortest path) γ : [0, a] → Y and a point x0 such that f (x0 ) = γ(0), there exists a unique geodesic (resp. shortest path) γ̃ : [0, a] → X such that γ̃(0) = x0 and f (γ̃(t)) = γ(t).
  *Proof:* Extends continuous path mappings step-wise along lifting open segments terminating Cauchy sequences iteratively to maximal bounds.
- **Theorem 3.4.18.** Let f : X → Y be a surjective local isometry of a complete locally compact length space X. Assume that each point in Y has a neighborhood such that every geodesic segment contained in our neighborhood is a unique shortest path between its end-points. Then f is a covering map.
  *Proof:* Identifies uniform balls over local neighborhoods isolating non-overlapping lifts iteratively back-tracing geodesics uniquely without intersection.
- **Proposition 3.5.5.** Every (locally-)finite 2-dimensional polyhedral space admits an arcwise isometry onto a planar polygon. In other words, every 2-dimensional polyhedral metric can be induced by a map to R2 .
  *Proof:* Tessellates the face geometry uniquely via Dirichlet-Voronoi regions bending cut structures onto flat target planes matching original metrics identically.
- **Proposition 3.6.1.** The direct product of strictly intrinsic metrics is a strictly intrinsic metric. The direct metric product of two length spaces is a length space.
  *Proof:* Calculates pairwise points establishing precisely equidistant midpoints natively from the derived Pythagorean definitions.
- **Lemma 3.6.4.** A constant-speed path in Z is a shortest path (a geodesic) if and only if it is the product of two shortest paths (geodesics) in X and Y with constant-speed parameterizations.
  *Proof:* (no proof in this paper)
- **Lemma 3.6.9.** If X is a space with strictly intrinsic finite metric and F : X → Y is a distance-preserving map, then the image Im(F ) := F (X) is convex in Y .
  *Proof:* (no proof in this paper)
- **Proposition 3.6.11.** Let X and Y be length spaces, and α : [a, b] → X, β : [c, d] → Y shortest paths. Then the product of their images R = Im(α) × Im(β) is convex in X × Y and isometric to a Euclidean rectangle.
  *Proof:* Parameterizes natural arc length distances simultaneously over combined axes tracking Pythagorean relations linking directly inside rectangular spans.
- **Proposition 3.6.13.** If X is a metric space with diam(X) ≤ π, then dc is a metric.
  *Proof:* Binds spherical inequalities evaluating respective plane cases validating triangle constraints via bounding planar angles.