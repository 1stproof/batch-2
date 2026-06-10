<!-- Generated 2026-05-31T02:20:47 -->
<!-- Source PDF: gruber__convex_and_discrete_geometry.pdf (3434633 bytes) -->
<!-- Citation: P. M. Gruber (2007). Convex and Discrete Geometry. Springer. -->

# Convex and Discrete Geometry (Gruber, 2007)

## Definitions
None in this paper.

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 1.1.** Let C ⊆ Ed and f : C → R. Then the following statements are equivalent:
(i) f is a convex function.
(ii) epi f is a convex set in Ed × R = Ed+1.
  *Proof:* (no proof in this paper)
- **Lemma 1.1.** Let f : I → R be convex. Then
f (y) − f (x) f (z) − f (x) f (z) − f (y)
≤ ≤ for x, y, z ∈ I, x < y < z.
y−x z−x z−y
  *Proof:* Uses a convex combination to interpolate the intermediate point and applies the convexity definition to bound the slopes.
- **Theorem 1.1.** Let f : I → R be convex. Then f is Lipschitz on each compact interval in int I . Thus, in particular, f is absolutely continuous on each compact interval in int I and continuous on int I .
  *Proof:* Bounds the variation on any compact interval using the three-point difference quotient inequalities.
- **Theorem 1.2.** Let f : I → R be convex and x ∈ int I . Then f has affine support at x.
  *Proof:* Finds a separating constant between the supremum of left-hand difference quotients and the infimum of right-hand difference quotients.
- **Theorem 1.3.** Let I be open and f : I → R. Then the following statements are equivalent:
(i) f is convex.
(ii) f has affine support at each x ∈ I .
  *Proof:* Shows that the pointwise supremum of a family of affine and thus convex functions is convex.
- **Theorem 1.4.** Let I be open and f : I → R convex. Then f − and f + exist, are non-decreasing (not necessarily strictly), and f − ≤ f + on I . f is differentiable precisely at those points x ∈ I where f − is continuous. Hence f (x) exists for all x ∈ I with a set of exceptions which is at most countable and f is non-decreasing on its domain of definition.
  *Proof:* Uses the monotonicity of difference quotients to establish the existence, monotonicity, and limit properties of one-sided derivatives.
- **Theorem 1.5.** Let I be open and f : I → R convex. If f is differentiable on I , then f is continuous, i.e. f is of class C 1 .
  *Proof:* (no proof in this paper)
- **Proposition 1.2.** Let f : I → R be convex and x ∈ int I . Then an affine function a : R → R of the form a(y) = f (x) + u(y − x) for y ∈ R is an affine support of f at x if and only if
f − (x) ≤ u ≤ f + (x).
  *Proof:* Characterizes affine supports by bounding their slopes between the left and right derivatives.
- **Theorem 1.6.** Let f : I → R be convex and x ∈ int I . Then the following statements are equivalent:
(i) f is differentiable at x.
(ii) f has unique affine support at x, say a : R → R, where a(y) = f (x) + u(y − x) for y ∈ R and u = f (x).
  *Proof:* (immediate from Proposition 1.2)
- **Theorem 1.7.** Let I be open and f : I → R convex. Then f is twice differentiable almost everywhere on I . Moreover, for almost every x ∈ I ,
1
f (y) = f (x) + f (x)(y − x) + f (x)(y − x)2 + o(|y − x|2 ) as y → x, y ∈ I.
2
  *Proof:* Extends Lebesgue's differentiability theorem to the non-decreasing derivative, then recovers the Taylor expansion via absolute continuity.
- **Theorem 1.8.** Let I be open and f : I → R differentiable. Then the following statements are equivalent:
(i) f is convex.
(ii) f is non-decreasing.
  *Proof:* Applies the first mean value theorem to construct local affine supports based on the non-decreasing derivative.
- **Corollary 1.1.** Let I be open and f : I → R twice differentiable. Then the follow-ing are equivalent:
(i) f is convex.
(ii) f ≥ 0.
  *Proof:* (no proof in this paper)
- **Theorem 1.9.** Let f : I → R be convex, x1 , . . . , xn ∈ I , and λ1 , . . . , λn ≥ 0 such that λ1 + · · · + λn = 1. Then λ1 x1 + · · · + λn xn ∈ I and
f (λ1 x1 + · · · + λn xn ) ≤ λ1 f (x1 ) + · · · + λn f (xn ).
  *Proof:* First proof proceeds by induction on the number of points; the second uses the affine support at the center of mass.
- **Corollary 1.2.** Let x1 , . . . , xn ≥ 0 and λ1 , . . . , λn ≥ 0 be such that λ1 + · · · + λn = 1. Then
x1λ1 · · · xnλn ≤ λ1 x1 + · · · + λn xn .
In particular,
1 x1 + · · · + xn
(x1 · · · xn ) n ≤ .
n
  *Proof:* (immediate from Theorem 1.9)
- **Corollary 1.3.** Let x, y ≥ 0 and p, q > 1 such that 1p + q1 = 1. Then
xp yq
xy ≤ + .
p q
  *Proof:* (immediate from Corollary 1.2)
- **Corollary 1.4.** Let x1 , y1 , . . . , xn , yn ≥ 0 and p, q > 1 such that 1p + q1 = 1. Then
p p 1 q q 1
x1 y1 + · · · + xn yn ≤ x1 + · · · + xn p y1 + · · · + yn q .
  *Proof:* Applies Young's inequality pointwise to normalized terms and sums them.
- **Corollary 1.5.** Let f, g : I → R be non-negative, integrable, with non-vanishing integrals and let p, q > 1 such that 1p + q1 = 1. Then
1 1
p q
f g dx ≤ f p dx gq d x .
I I I
  *Proof:* Applies Young's inequality pointwise to normalized functions and integrates.
- **Corollary 1.6.** Let x1 , y1 , . . . , xn , yn ≥ 0 and p ≥ 1. Then
1 p p 1 p p 1
(x1 + y1 ) p + · · · + (xn + yn ) p p ≤ x1 + · · · + xn p + y1 + · · · + yn p .
  *Proof:* Factors the sum and applies Hölder's inequality to each part.
- **Corollary 1.7.** Let f, g : I → R be non-negative and integrable and let p ≥ 1. Then
1 1 1
p p p
( f + g) p d x ≤ f pd x + g pd x .
I I I
  *Proof:* (no proof in this paper)
- **Theorem 1.10.**   has the following properties:
(i)  (1) = 1.
(ii)  (x + 1) = x (x) for x > 0, i.e.   satisfies Euler’s functional equation.
(iii)  is logarithmic convex, i.e. log   is convex for x > 0.
  *Proof:* Direct limit evaluations verify the function values, and Hölder's inequality for integrals proves logarithmic convexity.
- **Theorem 1.11.** Let g : R+ → R+ be a function having the Properties (i)–(iii) of Theorem 1.10. Then g =   on R+ .
  *Proof:* Bounds the function by shifting its argument and combines its log-convexity with the functional equation to establish Gauss's limit formula.
- **Theorem 2.1.** Let f : C → R be convex, x1 , . . . , xn ∈ C, and λ1 , . . . , λn ≥ 0 such that λ1 + · · · + λn = 1. Then λ1 x1 + · · · + λn xn ∈ C and
f (λ1 x1 + · · · + λn xn ) ≤ λ1 f (x1 ) + · · · + λn f (xn ).
  *Proof:* (no proof in this paper)
- **Theorem 2.2.** Let f : C → R be convex. Then f is Lipschitz on each compact subset of int C. Thus, in particular, f is continuous on int C.
  *Proof:* Localizes an upper bound using an interior simplex, then bounds variations using the one-dimensional difference quotient inequalities.
- **Theorem 2.3.** Let f : C → R be convex and P an affine subspace in Ed through a point x ∈ int C. Suppose that the restriction f |P has an affine support a P at x. Then f has an affine support a at x which extends a P , i.e. a|P = a P .
  *Proof:* Extends the affine support one dimension at a time by finding a separating slope that satisfies the convexity bounds.
- **Theorem 2.4.** Let C be open and f : C → R. Then the following are equivalent:
(i) f is convex.
(ii) f has affine support at each x ∈ C.
  *Proof:* (no proof in this paper)
- **Theorem 2.5.** Let f : C → R be convex and x ∈ int C. Then the following statements are equivalent:
(i) f is differentiable at x.
(ii) The partial derivatives f xi (x), i = 1, . . . , d, exist.
  *Proof:* Bounds the directional limits between linear approximations along the basis vectors using Jensen's inequality and convexity.
- **Theorem 2.6.** Let C be open and f : C → R convex. Then f is differentiable almost everywhere on C.
  *Proof:* Demonstrates that one-sided partial derivatives are measurable limits of continuous functions, then invokes Fubini's theorem.
- **Theorem 2.7.** Let f : C → R be convex and x ∈ int C. Then the following are equivalent:
(i) f is differentiable at x.
(ii) f has unique affine support at x, say a : Ed → R, where a(y) = f (x)+u·(y−x) for y ∈ Ed and u = grad f (x) = f x1 (x), . . . , f xd (x) .
  *Proof:* Projects the function onto coordinate axes and equates the unique gradient components to the one-dimensional derivatives.
- **Theorem 2.8.** Let C be open and f : C → R convex and differentiable on C. Then all partial derivatives of f are continuous, i.e. f is of class C 1 .
  *Proof:* Establishes a uniform Lipschitz bound on gradients and shows that any convergent subsequence of gradients limits to the true gradient.
- **Theorem 2.9.** Let C be open and f : C → R convex. Then f is twice differentiable almost everywhere on C.
  *Proof:* Proves the subgradient's inverse mapping is differentiable almost everywhere via Rademacher's theorem, then recovers the second-order expansion by integrating directional derivatives.
- **Theorem 2.10.** Let C be open and f : C → R of class C 2 . Then the following statements are equivalent:
(i) f is convex.
(ii) For any x ∈ C the Hessian form H (x) of f at x is positive semi-definite.
  *Proof:* Evaluates the chain rule on line segments to apply the one-dimensional second-derivative criterion for convexity.
- **Theorem 2.11.** Let C be compact and convex. Then the set D of all differences of continuous convex functions on C is dense in the space of all real continuous functions on C, endowed with the maximum norm.
  *Proof:* First proof constructs convex differences from polynomials via a quadratic shift; the second invokes Stone's approximation theorem.
- **Theorem 2.12.** Let f : [a, b]×E2 → R be of class C 2 and assume that for each fixed x ∈ [a, b] the function (y, z) → f (x, y, z) for (y, z) ∈ E2 is convex, respectively, strictly convex. Let α, β ∈ R and assume that y : [a, b] → R is a function of class C 1 such that y(a) = α, y(b) = β. Then the following statements are equivalent:
(i) y is a minimizer, respectively, unique minimizer of the integral
b
I (w) = f x, w(x), w (x) d x
a
among all functions w : [a, b] → R of class C 1 with w(a) = α, w(b) = β.
(ii) y satisfies the Euler–Lagrange equation
d
f y (x, y, y ) − f y (x, y, y ) = 0.
dx
  *Proof:* Expands the varied integral using the local convexity inequality and shows it exceeds the minimum due to the Euler-Lagrange condition.
- **Lemma 3.1.** Let A ⊆ Ed . Then conv A is the set of all convex combinations of points of A.
  *Proof:* Proceeds by induction on the number of points, iteratively factoring combinations into sub-combinations.
- **Theorem 3.1.** Let A ⊆ Ed . Then conv A is the set of all convex combinations of affinely independent points of A, i.e. the union of all simplices with vertices in A.
  *Proof:* Eliminates affine dependencies by shifting weights toward zero along a null vector without changing the convex combination.
- **Corollary 3.1.** Let A ⊆ Ed be compact. Then conv A is compact.
  *Proof:* Expresses the convex hull as the continuous image of a compact simplex parameter space via Carathéodory's theorem.
- **Proposition 3.1.** Let C ⊆ Ed be convex. Then the following statements hold:
(i) cl C is convex.
(ii) relint C is convex.
(iii) C ⊆ cl relint C.
  *Proof:* Exploits sequence limits for closure properties and shrinking balls to prove interior point properties.
- **Proposition 3.2.** Let A ⊆ Ed be bounded. Then cl conv A = conv cl A.
  *Proof:* Demonstrates mutual inclusion by leveraging the compactness of the convex hull of the closed set.
- **Proposition 3.3.** Let C be a closed convex cone in Ed with apex o and lineality space L. Then
C = (C ∩ L ⊥ ) ⊕ L ,
where C ∩ L ⊥ is a pointed closed convex cone with apex o.
  *Proof:* Decomposes vectors into orthogonal components and verifies that the complementary projection forms a pointed cone.
- **Theorem 3.2.** The following statements hold:
(i) Radon’s Theorem. Let A  = ∅ be a set of at least d + 2 points in Ed . Then there are subsets B, C of A such that
B ∩ C = ∅, conv B ∩ conv C  = ∅.
(ii) Carathéodory’s Theorem. Let A  = ∅ be a set in Ed . Then conv A is the set of all convex combinations of affinely independent points in A.
(iii) Helly’s Theorem. Let F be a family of convex bodies in Ed . If any d + 1 convex bodies in F have non-empty intersection, then the intersection of all convex bodies in F is non-empty.
  *Proof:* Connects linear dependence to Radon partitions, leverages them to eliminate points for Carathéodory, and uses distance-minimizing points for Helly.
- **Theorem 3.3.** Let A ⊆ Ed be bounded. Then A is contained in a (solid Euclidean) ball of radius
1
d 2
= diam A.
2d + 2
  *Proof:* Bounds the circumradius of any sub-simplex of at most d+1 points using distances, then applies Helly's theorem.
- **Theorem 3.4.** Each finite set in Ed has a centrepoint.
  *Proof:* Expresses the centrepoint condition via open halfspaces and uses Helly's theorem to prove their intersection is non-empty.
- **Theorem 3.5.** Let G be an open connected set in Cd . Then the following statements are equivalent:
(i) G is the domain of convergence of a power series in d complex variables of the form (1).
(ii) G is a complete, logarithmically convex Reinhardt domain.
  *Proof:* Interpolates interior points using Abel's lemma and Hölder-like bounds on the power series coefficients.
- **Lemma 4.1.** Let C ⊆ Ed be a closed convex set. Then the metric projection pC : Ed → C is non-expansive, i.e.
pC (x) − pC (y) ≤ x − y for x, y ∈ Ed .
  *Proof:* Proves that the projection strictly separates points via the boundary hyperplanes of an orthogonal slab.
- **Theorem 4.1.** Let C ⊆ Ed be a closed convex set. For each x ∈ bd C, there is a support hyperplane HC (x) of C at x, not necessarily unique. If C is compact, then for each vector u ∈ Ed \ {o}, there is a unique support hyperplane HC (u) of C with exterior normal vector u.
  *Proof:* Projects exterior points to construct converging normal vectors, then uses a compactness argument to isolate the boundary supports.
- **Theorem 4.2.** Let C ⊆ Ed be closed and let int C  = ∅. Then the following are equivalent:
(i) C is convex.
(ii) C has a support hyperplane HC (x) at each point x ∈ bd C.
  *Proof:* Derives a contradiction by selecting a point on a segment bridging an unseparated exterior point and the interior.
- **Corollary 4.1.** Let C ⊆ Ed be closed and convex. Then
C= HC− (x).
x∈bd C
  *Proof:* (no proof in this paper)
- **Theorem 4.3.** Let h : Ed → R. Then the following statements are equivalent:
(i) h is the support function of a (unique) convex body C, i.e. h = h C .
(ii) h has the following properties:
h(λu) = λh(u) for u ∈ Ed , λ ≥ 0
h(u + v) ≤ h(u) + h(v) for u, v ∈ Ed
  *Proof:* Demonstrates that supremum operators preserve subadditivity and uses the supporting hyperplanes of the epigraph cone to construct the body.
- **Proposition 4.1.** Let C, D be convex sets in Ed . Then the following statements are equivalent:
(i) C and D are separated, respectively, strongly separated.
(ii) The convex set C − D = {x − y : x ∈ C, y ∈ D} and {o} are separated, respectively, strongly separated.
  *Proof:* Translates separation conditions to the origin and the Minkowski difference, relying on the convexity of the difference set.
- **Theorem 4.4.** Let C, D ⊆ Ed be convex. Then the following hold:
(i) Let C be compact, D closed and C ∩ D = ∅. Then C and D are strongly separated.
(ii) Let relint C ∩ relint D = ∅. Then C and D are separated.
  *Proof:* Separates compact sets using the shortest distance segment, and extends separation to relative interiors by arguing their difference omits the origin.
- **Theorem 4.5.** Let µ1 , . . . , µd be d finite, signed, non-atomic measures on  M, M . Then the range of the (finite, signed, non-atomic) vector-valued measure µ = (µ1 , . . . , µd ) on  M, M , that is the set
R(M) = µ(B) = µ1 (B), . . . , µd (B) : B ∈ M ⊆ Ed ,
is compact and convex.
  *Proof:* Applies Zorn's lemma to find a minimal measurable set spanning the hull, then iteratively drops dimensions to locate the range.
- **Theorem 4.6.** Assume that there is a control for (1) which transfers a to b. Then the following propositions hold:
(i) There is a time optimal control which transfers a to b.
(ii) Let u be a time optimal control which transfers a to b in minimum time T , say. Then there is a point w ∈ Ed such that for the solution of the initial value problem
(2) ẏ = −A T y, y(T ) = w,
the following statement holds, where w(t) = B T y(t):
u(t) ∈ C ∩ HC w(t) for almost every t ∈ [0, T ].
  *Proof:* Defines the reachable set as a compact convex continuous image, then translates supporting hyperplanes at the optimal boundary back to the control condition.
- **Theorem 5.1.** Let C ∈ C p . Then the set of singular points of bd C has σ -finite (d − 2)-dimensional Hausdorff measure.
  *Proof:* Proves singular points correspond to multidimensional normal cones, bounding their measure by projecting rational simplices.
- **Corollary 5.1.** Let C ∈ C p . Then the set of singular points of bd C has Hausdorff dimension at most d − 2.
  *Proof:* (immediate from Theorem 5.1)
- **Theorem 5.2.** Let C ∈ C p . Then the set of singular points of bd C is meagre in bd C.
  *Proof:* Defines closed singular point sets bounded by angle, proving they contain no interior to show they are nowhere dense.
- **Lemma 5.1.** Let D ⊆ Ed be open and convex and f : D → R convex. Then, given x ∈ D, the following are equivalent:
(i) f is differentiable at x.
(ii) x, f (x) is a smooth boundary point of epi f .
  *Proof:* (no proof in this paper)
- **Theorem 5.3.** Let D ⊆ Ed be open and convex and f : D → R convex. Then f is differentiable at each point of D with a set of exceptions which is of σ -finite (d − 1)-dimensional Hausdorff measure and meagre in D.
  *Proof:* Maps the boundary differentiability and Baire category properties of the epigraph directly onto the function domain.
- **Lemma 5.2.** Let D ⊆ Ed be open and convex and f : D → R convex. Then, given x ∈ D, the following statements are equivalent:
(i) f is twice differentiable at x in the sense of Theorem 2.9,
(ii) epi f is twice differentiable at x, f (x) .
  *Proof:* Translates the second-order Taylor expansion quadratic forms between the function domain and the tangent hyperplane of the epigraph.
- **Theorem 5.4.** Let C ∈ C p . Then bd C is almost everywhere twice differentiable.
  *Proof:* (immediate from Theorem 2.9)
- **Theorem 5.5.** Let C ∈ C. Then ext C is the smallest subset of C (with respect to inclusion) with convex hull C.
  *Proof:* Recursively slices the convex body with supporting hyperplanes, applying induction on the dimension.
- **Theorem 5.6.** Let C ∈ C and let f : C → R be a continuous convex function. Then f attains its maximum m at an extreme point of C.
  *Proof:* Applies Jensen's inequality to the extreme point representation, forcing equality at the maximum values.
- **Theorem 5.7.** The set Ωd of all doubly stochastic d × d matrices is the convex hull of the d × d permutation matrices and each permutation matrix is an extreme point of Ωd .
  *Proof:* Uses induction on the number of positive entries, subtracting a scaled permutation matrix identified via zero-free diagonals.
- **Lemma 5.3.** Let M be a real d × d matrix. Then the following are equivalent:
(i) Each diagonal of M contains 0.
(ii) M has a p × q zero submatrix with p + q = d + 1.
  *Proof:* Employs induction on dimension, decomposing the matrix into submatrices to trace the dependencies of non-zero diagonals.