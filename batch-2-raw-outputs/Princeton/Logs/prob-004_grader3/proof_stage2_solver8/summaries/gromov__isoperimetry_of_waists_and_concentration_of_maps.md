<!-- Generated 2026-05-31T01:49:15 -->
<!-- Source PDF: gromov__isoperimetry_of_waists_and_concentration_of_maps.pdf (445238 bytes) -->
<!-- Citation: Mikhail Gromov (2003). Isoperimetry of waists and concentration of maps. Geometric and Functional Analysis (GAFA). -->

# Isoperimetry of waists and concentration of maps (Gromov, 2003)

## Definitions
- **(b) Deﬁnition.** Given a metric space Y and an mm space X let µX ((Y → X) + ε) stand for the supremum of the measures of the ε-neighbourhoods of the images of Y under all 1-Lipschitz maps Y → X.
- **9.1.C Iso-domination.** A measure ν on R (preferably but not necessarily iso-simple) is called an iso-dominant of X = (X, dist, µ) if for every µ-proper Lipschitz map f : X → R there exists a monotone increasing 1-Lipschitz function f : R → R such that f∗ (ν) = f∗ (µ).
- **9.3.A Normal geodesic partition.** A partition of a metric space X into topological segments S is called normal geodesic if there exists a 1-Lipschitz function d : X → R that is isometric on each segment S.

## Lemmas, Theorems, Propositions, Corollaries
- **1 Waist of the Sphere Theorem.** Let f : S n → Rk be a continuous map where S n is the unit n-sphere. Then there exists a point z ∈ Rk such that the spherical n-volumes of the ε-neighbours of the level Yz = f −1 (z) ⊂ S n , denoted Yz + ε ⊂ S n , satisfy
                            Vol(Yz + ε) ≥ Vol(S n−k + ε)                        ( )S n
for all ε > 0, where S n−k ⊂ S n denotes an equatorial (n − k)-sphere.
  *Proof:* Resolves the center map ambiguity by generic smooth map approximation and uses the weak volume concavity of spherical segments to bound the codimension measure from below.

- **3.1 Log-waist theorem (see §5.8).** Let X be a convex subset in Rn with a log-concave probability measure. Then
                                      
   wst(X → Rk , ε) ≥ wst• (Gak , ε) =
                                              gk (x)dx
                                       B(0,ε)
                    ε                     ∞                         
                                  x2                             2
                =      xk−1
                            exp − 2 dx              xk−1 exp − x2 dx . ( )log
                    0                         0
    If n ≥ k then the inequality ( )log is sharp: for example, the equality is achieved for linear maps Gan → Rk .
  *Proof:* Extends the central center-of-mass map from $k$-dimensional subsets to $n$-dimensional subsets using a partition of unity, then applies the Brunn-Minkowski theorem for intersections of log-concave measures.

- **4.4 Convex partition theorem.** Let µ be a Borel probability measure on S n and let M k denote the space of weak limits µ  of the restrictions (µ | Ui )/µ(Ui ) for all sequences of convex open Ui ’s that Hausdorﬀ converge to compact convex subsets S ⊂ S n of codimension (exactly!) k. Clearly, S ⊃ supp µ  , and, to save notation, we assume that S = supp µ  . Let ck• : M k → S n be a continuous (“center”) map, such that ck• (µ  ) ∈ S = supp µ  for all µ  (e.g. the center of mass of µ  ). The map ck• does not, in general, continuously extend to the weak closure of M k : when a sequence (Si  , µ i ) converges to (S    , µ   ) with codim S    ≥ k+1 the sequence ck• (µ i ) ∈ Si  does not have to converge. In such a case we take the limit points of all these (sub)sequences and denote by c◦ (µ   ) ⊂ S    the (compact) subset consisting of all such limits. If Π is a convex partition of S n into Sπ ’s with codim Sπ ≥ k, we denote by Cπ ⊂ Sπ the (“center”) image of the (set valued) map sending each Sπ with codimension = k to ck• (µπ ) and if codim Sπ ≥ k + 1 to c◦ (µπ ), where µπ denote the canonical system of measures associated to Π. As we know these µπ are convexly derived from µ for almost all π and thus the (“central”) subset Cπ is well deﬁned in Sπ for almost all π.
  *Proof:* (no proof in this paper)

- **4.4.A (see §6).** Let f : S n → Rk be a continuous map and ck• a center map. Then there exist a value z ∈ Rk and a convex partition Π of S n into Sπ ’s of codimension ≥ k, such that the level Yz = f −1 (z) ⊂ S n meets (the corresponding “center”) Cπ for almost all π ∈ Π.
  *Proof:* Relies on a homological intersection argument mapping the parameter space to the Grassmannian.

- **Elementary Lemma.** Let ϕ0 (t), t ∈ [0, t0 ≤ ∞) be a smooth positive monotone decreasing function where, (log ϕ0 )   ≤ 0, and, moreover, (log ϕ0 )   is monotone decreasing. Let λ(τ ), τ ≤ τ0 < t0 be a positive function and define, for t ∈ [0, t0 − τ0 ], ψ(t) = inf 0≤τ ≤τ0 λ(τ )ϕ0 (t + τ ). Then
          ε           t0 −τ0            ε             t0
                ψ(t)dt           ψ(t)dt ≥     ϕ0 (t)dt       ϕ0 (t)dt .
            0            0                0             0
  *Proof:* Stated as a straightforward calculation.

- **5.1 Non-vanishing Lemma.** For each m ≤ n, the top Stiefel–Whitney class of the m-th Whitney’s power Lm i does not vanish
                          i )  = 0 , for N = Nm = m(2 − 1) .
                     wN (Lm                          i
  *Proof:* Computes Stiefel-Whitney classes recursively over the nested Cartesian fibrations of projective spaces.

- **5.2 Vanishing Corollary.** Every continuous section Qi → Lm i , m ≤ n, vanishes at some point q ∈ Qi . Moreover, the zero set of a section supports a non-zero homology class in H Nm (Qi ; Z2 ).
  *Proof:* (immediate from 5.1 Non-vanishing Lemma)

- **5.3 c• -corollary.** Denote by S the space of all n-dimensional geodesically convex subsets S ⊂ S n , each contained in a hemisphere, with the Hausdorﬀ topology and let S  → c• = c• (S) ∈ S n be a continuous map S → S n . Then for each continuous map f : S n → Rk , k = 1, 2, . . . , n − 1, there exists a partition Π ∈ Pi of S n , for each i = 1, 2, . . . , such that
  (i) All convex subsets Sπ making Π have equal n-dimensional volumes = Voln (S n )/2i ;
 (ii)
                            f (c• (Sπ )) = f (c• (Sπ  ))         (+)•
        for all π, π   in all Π.
  *Proof:* Constructs a continuous map from the sequence of hyperplanes in the partition space to Euclidean vectors, subsequently applying the Vanishing Corollary to find a root.

- **5.6 Generalization of the Vanishing Lemmas.** Suppose, in the context of §7 we are given equatorial spheres H1m ⊂H n , H2m ⊂H n , . . . , Him ⊂H n . If m ≥ k + 1, then there exists a partition π ∈ Pi satisfying (i) and (ii) of §5.3 where, moreover, all hyperplanes h ∈ H n of level j are contained in Hjm for all j = 1, . . . , i.
  *Proof:* Replicates the arguments of §5.1 replacing $S^n$ with $S^m$.

- **5.7 c• -corollary.** There exists a convex partition Π of S n into Sπ with dim Sπ ≤ k for all π, such that
                            f (c• (Sπ )) = f (c• (Sπ  ))                   (+)∞
                                                                              •
for all pairs π, π   ∈ Π, where c• (Sπ ) for dim Sπ < n refers to some limit point of c• (Sπi ) for Sπ = ∩∞ i=1 Sπi , where πi ∈ Pi are finite partitions converging to Sπ .
  *Proof:* Iteratively intersects sets using a dense sequence of orthogonal $m$-spheres to drive their dimensional width to zero and considers the resulting limit partitions.

- **5.8.A Concavity property.** Let µ be a 1-log-concave measure on a convex subset in Rn and let U1 and U2 be two convex domains. Consider the translates U1 + x1 of U1 for all x1 ∈ Rn and the intersections Ux1 = (U1 + x1 ) ∩ U2 ⊂ Rn . Then the function µ(Ux1 ) is 1-log-concave x1 ∈ Rn in-so-far as it is > 0.
  *Proof:* Employs the Brunn-Minkowski theorem specifically applied to log-concave subsets.

- **6.2 UB-partition Theorem.** If ck• and Cπ are as in §4.4 and k < n then the conclusion of 4.4.A holds true for every UB-family: there exists a convex partition Π of S n into (at most) k-dimensional subsets Sπ such that some Yz , z ∈ Z meets Cπ ⊂ Sπ for almost all π ∈ Π.
  *Proof:* Constructs a relative $(2n-k)$-cycle from the pull-back of the diagonal and verifies its $\mathbb{Z}_2$-intersection with the diagonal in the quotient parameter space is non-zero.

- **6.3.B Corollary.** The volumes of the ε-neighbourhoods of Y0 = p0 (Y = S k ) in the standard round sphere S n are bounded from below by those of the equatorial S n−k ⊂ S n , provided n is odd and k = 2m − 1.
  *Proof:* (no proof in this paper)

- **7.1 Parametric BU-partition Theorem.** The map β   is Z2 -onto.
  *Proof:* Automatically ensured by functoriality and homological continuity in the fiber bundles across $B$.

- **Parametric BU-theorem.** If k < n (or k = n and the fibers Zb are contractible) then the (tautological) projection BU → B is Z2 -onto. Consequently, the f  × f -image f  × f (BU) ⊂ Z projects Z2 -onto Z.
  *Proof:* Stated as obvious.

- **Corollary.** Let fb : S n → Z, b ∈ B, be a continuous family of maps. Then the assignment to each b ∈ B of (the subset of) those z ∈ Z for which ∃ s ∈ S, where fb (s) = fb (−s) = z, is a Z2 -morphism.
  *Proof:* (immediate from Parametric BU-theorem)

- **Subdivision Lemma.** Let µ be a measure on S n with positive continuous density and H denote the space of oriented hyperplanes (equators) h dividing S n into halves of equal µ-measure, say Xh+ and Xh− . The totalities of these make fibrations X + and X − over H with half-sphere fibers. Then the Z2 -waist of (S n , µ) is bounded from below by the sum of the Z2 -waists of X + and X − : if Z2 - wst(X ± −→ Z, ε) ≤ w± (h, ε), then
                     n                                        
          Z2 - wst (S , µ) → Z, ε ≥ inf w+ (h, ε) + w− (h, ε) .
                                        h∈H
  *Proof:* Immediate corollary of applying the Borsuk-Ulam theorem sequentially to sphere bundles.

- **9.1.A Lemma (Isoperimetric inequality in R).** Let ν be given by a strictly positive continuous density function, ν = ϕ(t)dt on some open, finite or infinite, segment in R. Then ν is iso-simple in the following two cases.
   1. ϕ(t) is strictly monotone increasing.
   2. µ(X) < ∞, the function ϕ is even (ϕ(t) = ϕ(−t)), strictly monotone increasing for t < 0 and the corresponding function sν (v) is sublinear for v ≤ 12 µ(X),
                 sν (v1 + v2 ) ≤ sν (v1 ) + sν (v2 ) ,   v1 + v2 ≤ 12 µ(X) .
  *Proof:* Stated as straightforward.

- **9.1.B Domination Corollary.** Let ν satisfy 1 or 2 and let f : R → R be a 1-Lipschitz map that is assumed µ-proper in the case 1. Then there exists a monotone increasing 1-Lipschitz function f : R → R, unique on the segment where ϕ > 0, such that f∗ (ν) = f∗ (ν).
  *Proof:* (immediate from 9.1.A Lemma)

- **9.2.B Corollary (Euclid?). Spherical isoperimetric inequality.** The distance function to a point s0 ∈ S, that is f (s) = dist(s, s0 ) is iso-extremal for the standard geometry on S n . Furthermore, this remains valid for every convex sector, i.e. a subset X ⊂ S n containing s0 and −s0 .
  *Proof:* Convex-derived measures on geodesic segments are $\sin^{n-1}$-concave, allowing iso-domination by the normalized simple measure.

- **9.2.C Euclidean Subcorollary.** Let X ⊂ Rn be a convex cone. Then the distance to the origin, f (x) = x , is iso-extremal on X.
  *Proof:* Taking the scaling limit from spherical sectors to Euclidean space.

- **9.2.D Borel’s Gaussian isoperimetric inequality.** Normal projections of Gan = (Rn , e− x2 dx) to lines in Rn are iso-extremal.
  *Proof:* Convex-derived Gaussian measures are 2-log-concave, ensuring iso-domination by a one-dimensional simple measure.

- **Levy domination inequality.** Let X = (X, dist, µ) be a compact smooth Riemannian pm space, where X may have non-empty convex boundary and where smoothness of µ means that µ = ϕ(x) dx for ϕ(x) > 0 and C 2 -smooth. If X is smoothly sinα -concave for some α > 0 then it is iso-dominated by the normalized measure sinα t dt on [0, π].
  *Proof:* (no proof in this paper)

- **9.4.B Schwarz Symmetrization Lemma.** Granted the assumptions above, the space X → B is iso-restricted by X   = B × R, provided the function ϕ(θ, v) is convex in θ.
  *Proof:* Directly applies Jensen-style geometric averaging inequalities using the convexity of the boundary slope operators.

- **9.4.C Schwarz’ Product Theorem.** Let Xi = (Xi , disti , µi ), i = 1, . . . , r, be Riemannian manifolds with smooth measures µi iso-dominated by measures νi on R. Then the isoperimetric profile (vX , sX ) of X = X1 × · · · × Xr is restricted by that of X   = (R, ν1 ) × · · · × (R, νr ),
                       vX (s) ≤ vX   (s) , sX (v) ≥ sX   (v) .
  *Proof:* Applying the Schwarz Symmetrization Lemma repeatedly using the convex bounding function $\sqrt{1 + \delta^2}$.

- **Schwarz Fibration Theorem.** If X is iso-dominated by ν1 and all fibers Xx by ν2 , then the isoperimetric profile of X is restricted by that of X   = (R, ν1 ) × (R, ν2 ).
  *Proof:* (no proof in this paper)