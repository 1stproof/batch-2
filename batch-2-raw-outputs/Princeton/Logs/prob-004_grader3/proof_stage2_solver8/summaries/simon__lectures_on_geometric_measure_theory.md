<!-- Generated 2026-05-31T01:49:32 -->
<!-- Source PDF: simon__lectures_on_geometric_measure_theory.pdf (1234390 bytes) -->
<!-- Citation: Leon Simon (1983). Lectures on Geometric Measure Theory. Centre for Mathematical Analysis (ANU). -->

# Lectures on Geometric Measure Theory (Leon Simon, 1983)

## Definitions
- **1.2 Definition:** A subset A   X is said to be  -measurable if  (S ) D  (S n A) C  (S \ A) for each subset S   X.
- **1.4 Definition:** A collection S of subsets of X is a  -algebra if (1) ∅; X 2 S (2) A 2 S ) X n A 2 S (3) A1 ; A2 ; : : : 2 S ) [j1D1 Aj 2 S.
- **1.6 Definition:** If X is a topological space then we define the Borel subsets of X to be the smallest  -algebra of subsets of X which contains all the open sets
- **1.21 Definition:** We say a Borel regular measure   on a topological space X is “open  -finite” if X D [j Vj where Vj is open in X and  (Vj ) < 1 for each j D 1; 2; : : :.
- **3.6 Definition:** a subset A   X is covered finely by a collection B of balls, meaning that inf{diam B W x 2 B 2 B } D 0 8x 2 A:
- **4.3 Definition (Symmetric Vitali Property):** An outer measure  0 on a metric space X is said to have the Symmetric Vitali Property if given any A   X with  0 (A) < 1 and any collection B of closed balls with centers in A which cover A finely (i.e. inf{  W B  (x ) 2 B } D 0 for each x 2 A), 9 a countable pairwise disjoint collection B 0 D {B j (xj ) W j D 1; 2; : : :}   B with  0 (A n ([j1D1 B j (xj ))) D 0.
- **5.6 Definition:** Given a Hausdorff space X, a “Radon measure” on X is an outer measure on X having the 3 properties: (R1) is Borel regular and  (K ) < 1 8 compact K   X (R2) (A) D inf U open; U  A (U ) for each subset A   X (R3) (U ) D sup K compact; K U (K ) for each open U   X:
- **1.12 Definition:** A bounded open set     Rn is said to be a Lipschitz domain if there are constants 0 <       such that 8 y 2 @  there is a v 2 S n 1 and a Lipschitz function u W B  (0) \ v ? ! (  ;   ) such that Uy \   D {y C x C t v W x 2 BM   (0) \ v ? ; t < u(x )} Uy \ @  D {y C x C t v W x 2 BM   (0) \ v ? ; t D u(x )};

## Lemmas, Theorems, Propositions, Corollaries
- **1.7 Lemma.** The collection M of all  -measurable subsets is a  -algebra which includes all subsets of X of  -measure zero.
  *Proof:* Checks properties of a sigma-algebra directly using Caratheodory's criterion.
- **1.12 Corollary (Egoroff’s Theorem.)** If A   X is  -measurable with finite measure, if fk W A ! [ 1; 1] are  -measurable for each k D 1; 2; : : :, and if lim fk (x ) D 0 for each x 2 A, then for each " > 0 there is a  -measurable subset B   A with fk ! 0 uniformly on B and  (A n B ) < ".
  *Proof:* Defines nested measurable sets where the sequence is bounded and uses continuity of measure to bound the complement's measure.
- **1.15 Theorem (Caratheodory’s Criterion.)** If X is a metric space with metric d and if is an outer measure on X with the property (A [ B ) D  (A) C  (B ) for all sets A; B   X with dist(A; B ) > 0; then all Borel sets are  -measurable.
  *Proof:* Shows closed sets are measurable by constructing a sequence of expanding annular regions and bounding their measure via subadditivity.
- **1.20 Corollary.** Suppose   W Rn ! Rn is linear and A   Rn . Then Ln (  (A)) D j det  jLn (A); A   Rn :
  *Proof:* Decomposes the linear map via the spectral theorem into orthogonal and diagonal transformations, applying Lebesgue measure's translation invariance.
- **1.22 Theorem.** Suppose X is a topological space with the property that every closed subset of X is the countable intersection of open sets (this trivially holds e.g. if X is a metric space), and suppose   is an open  -finite (as in 1.21 above) Borel-regular measure on X. Then (1) (A) D inf U open; U  A (U ) for each subset A   X, and (2) (A) D sup C closed; C  A (C ) for each  -measurable subset A   X .
  *Proof:* Constructs a sigma-algebra of sets satisfying the approximation property, shows it contains closed sets, and handles the infinite measure case via open sigma-finiteness.
- **1.24 Theorem (Lusin’s Theorem.)** Let   be a Borel regular outer measure on a topological space X having the property that every closed subset can be expressed as the countable intersection of open sets (e.g. X is a metric space), let A be any  -measurable subset of X with  (A) < 1, and let f W A ! R be  -measurable. Then for each " > 0 there is a closed set C   X with C   A,  (A n C ) < ", and f jC continuous.
  *Proof:* Partitions the range into intervals, applies Theorem 1.22 to approximate preimages with closed sets, and bounds the residual measure.
- **2.6 Theorem.** Ln (A) D Hn (A) D Hnı (A) for every A   Rn and every ı > 0:
  *Proof:* Proves H <= L by covering intervals with balls of same measure, and L <= H via the isodiametric inequality on covering collections.
- **2.7 Theorem (Isodiametric Inequality.)** Ln (A)   !n diam A 2 n for every set A   Rn :
  *Proof:* Applies Steiner symmetrization successively along coordinate planes to construct a highly symmetric set of the same measure without increasing diameter.
- **3.3 Theorem.** Let   be any outer measure on the metric space X such that all Borel sets are measurable (e.g.   is Borel regular), t   0, and A1   A2   X. Then ‚ n ( ; A2 ; x )   t 8 x 2 A1 ) t Hn (A1 )    (A2 );
  *Proof:* Constructs a fine cover of balls satisfying the density bound and extracts a disjoint subcover using the 5-times covering lemma to bound the measure.
- **3.4 Lemma (5-times Covering Lemma).** If B is any family of closed balls in X with R   sup diam B W B 2 B < 1, then there is a pairwise disjoint subcollection B 0   B such that [B2B B   [B2B 0 Bb
  *Proof:* Greedily selects maximal disjoint subcollections in decaying radius buckets to ensure every discarded ball intersects a selected ball of at least half its radius.
- **3.7 Corollary.** A   X is covered finely (as in Definition 3.6) by a collection B of closed balls, then there is a pairwise disjoint subcollection B 0   B such that A n [jND1 Bj   [ B2B 0n B1 ;:::;BN Bb for each finite subcollection {B1 ; : : : ; BN }   B 0.
  *Proof:* Applies the 5-times covering lemma and shows that points outside any finite union of the chosen balls are covered by the 5-times expansion of the remaining chosen balls.
- **3.8 Theorem (Upper Density Theorem.)** If   is an outer measure on X such that all Borel sets are measurable (e.g.   is Borel regular) and if A is a  -measurable subset of X with  (A) < 1, then ‚ n ( ; A; x ) D 0 for Hn -a.e. x 2 X n A:
  *Proof:* Applies Theorem 3.3 to the complement of a closed subset of A and uses inner regularity to shrink the residual measure to zero.
- **3.10 Corollary.** If A   Rn is Ln -measurable then the density ‚n (Ln ; A; x ) exists Ln -a.e. x 2 Rn , and ‚n (Ln ; A; x ) D 0 Ln -a.e. x 2 Rn n A and D 1 Ln -a.e. x 2 A.
  *Proof:* (immediate from 3.8)
- **3.11 Theorem.** For any Hn -measurable subset of A of a metric space X: (1) If Hn (A) < 1, then ‚ n (Hn ; A; x )   1 for Hn -a.e. x 2 A. (2) If Hnı (A) < 1 for each ı > 0 (note this is automatic if A is a totally bounded subset of X ), then ‚ n (Hn1 ; A; x )   2 n for Hn -a.e. x 2 A.
  *Proof:* Uses inner regularity and Theorem 3.3 for the upper bound, and constructs a covering violating the density assumption for the lower bound.
- **4.5 Lemma (Besicovitch Covering Lemma.)** Suppose B is a collection of closed balls in Rn , let A be the set of centers, and suppose the set of all radii of balls in B is a bounded set. Then there are sub-collections B1 ; : : : ; BN   B (N D N (n) ) such that each Bj is a pairwise disjoint (or empty) collection, and [jND1 Bj still covers A—i.e. A   [jND1 ([B2Bj B ).
  *Proof:* (no proof in this paper)
- **4.6 Theorem.** Suppose  ;  0 are open  -finite (as in 1.21) Borel regular measures on a metric space X,  0 has the Symmetric Vitali Property, and A   X, t   0. Then ‚  0 ( ; x )   t for all x 2 A )  (A)   t 0 (A):
  *Proof:* Imitates Theorem 3.3, but invokes the Symmetric Vitali Property on the finely covering collection of balls instead of the 5-times covering lemma.
- **4.7 Corollary.** If  ;  0 are as in Theorem 4.6 above then ‚   0 ( ; x ) < 1 for  0 -a.e. x 2 X.
  *Proof:* Applies Theorem 4.6 on level sets of the density and uses finiteness of measure to bound the level sets' measure to zero as the density bound goes to infinity.
- **4.8 Theorem (General Upper Density Th.)** If  ;  0 are Borel regular measures on a metric space X, if  0 open  -finite (as in 1.21) and has the Symmetric Vitali Property, and if A is a  -measurable subset of X with  (A) < 1, then ‚  0 (      A; x ) D 0 for  0 -a.e. x 2 X n A:
  *Proof:* Identical logic to Theorem 3.8 but substituting the general comparison theorem 4.6 in place of 3.3.
- **4.9 Theorem.** If   is open   -finite (as in 1.21) Borel regular measure on a metric space X, if has the Symmetric Vitali Property, and if A is a  -measurable subset of X, then lim #0 (A \ B  (x )) (B  (x )) D 1  - a.e. x 2 A 0  - a.e. x 2 X n A:
  *Proof:* Decomposes the density of the ball into pieces intersecting A and its complement, applying Theorem 4.8 to drive the off-set portion to zero.
- **4.10 Corollary.** If X;   are as in Theorem 4.9 and if f W X ! R is locally  -integrable on X (i.e. f is  -measurable and x 2 X ) B  (x ) jf j d  < 1 for some   > 0), then lim #0 ( (B  (x ))) 1 B  (x ) f d  D f (x ) for  - a.e. x 2 X
  *Proof:* Reduces to non-negative functions, uses Lusin's theorem to approximate by continuous functions, and applies Theorem 4.9 to the residual.
- **4.12 Lemma.** If  ;  0 is any pair of Borel regular measures on a metric space X with -finite, then there is a Borel set B   X with  0 (B ) D 0 and   (X n B ) absolutely continuous with respect to  0 (i.e.  0 (S ) D 0 )  (S n B ) D 0).
  *Proof:* In the finite measure case, takes the supremum of µ over µ₀-null sets to find a maximal null set B, then extends to the σ-finite case via union.
- **4.14 Theorem.** Suppose  ;  0 are open   -finite (as in 1.21) Borel regular measures on the metric space X, t > 0, and A   X with ‚  0 ( ; x )   t for all x 2 A. (i) If   has the Symmetric Vitali Property then  (A)   t 0 (A). (ii) If  0 has the Symmetric Vitali Property then  (A n B )   t 0 (A), where B (with 0 (B ) D 0) is as in 4.12.
  *Proof:* Uses inner regularity to approximate µ₀ and constructs a fine cover, bounding measures via the Vitali property of µ or its absolutely continuous part.
- **4.16 Theorem (Differentiation Theorem.)** Suppose  ;  0 are open  -finite (as in 1.21) Borel regular measures on the metric space X. (i) If   has the Symmetric Vitali Property, then there is a Borel set S of  -measure zero such that ‚  0 ( ; x ) (as in 4.15) exists for all x 2 X n S . (ii) If  0 has the Symmetric Vitali Property, then there is a Borel set S of  0 -measure zero such that ‚  0 ( ; x ) exists and is finite for all x 2 X n S . In either case ‚  0 ( ; x ) is a Borel measurable function of x 2 X n S .
  *Proof:* Bounds the measure of sets where upper and lower densities diverge using the comparison theorems, proving they are equal almost everywhere. Establishes measurability via semi-continuity quotients.
- **4.18 Theorem (Radon-Nikodym.)** Suppose  ;  0 are open  -finite (as in 1.21) Borel regular measures on X, and  0 has the Symmetric Vitali Property. (i) If   is absolutely continuous with respect to  0 (i.e. E   X with  0 (E ) D 0 ) (E ) D 0 and hence   also has the Symmetric Vitali Property), then ( ) (A) D A ‚  0 ( ; x ) d 0 (x ) for every Borel set A   X . (ii) If we drop the condition that   is absolutely continuous with respect to  0 , then in place of ( ) we can still conclude that there is a Borel set Z with  0 (Z ) D 0 and ( ) (A) D A ‚  0 ( ; x ) d 0 (x ) C ( Z )(A) for each Borel set A   X. (iii) Finally, if   also has the Symmetric Vitali Property, then we get ( ) with Z D {x 2 X W ‚  0 ( ; x ) D 1}
  *Proof:* Defines an absolutely continuous measure from the density, uses comparison theorems to show it matches the original measure, and handles singular parts via Lemma 4.12.
- **5.1 Lemma.** Let X be a Hausdorff space and K1 ; : : : ; KN be pairwise disjoint compact subsets of X. Then there are pairwise disjoint open subsets U1 ; : : : ; UN with Kj   Uj for each j D 1; : : : ; N .
  *Proof:* (no proof in this paper)
- **5.2 Corollary.** A compact Hausdorff space is normal: i.e. given closed disjoint subsets K1 ; K2 of a compact Hausdorff space, we can find disjoint open U1 ; U2 with Kj   Uj for j D 1; 2.
  *Proof:* (immediate from 5.1)
- **5.3 Lemma.** If X is a locally compact Hausdorff space and V is a neighborhood of a point x, then there is a neighborhood Ux of x such that U x is a compact subset of V .
  *Proof:* Intersects a compact neighborhood with V, applies normality of compact Hausdorff spaces to strictly separate x from the boundary.
- **5.4 Lemma.** Let X be a locally compact Hausdorff space, K   X compact, and K   V , V open. Then there is an open U   K with U   V , U compact, and an f W X ! [0; 1] with f   1 in a neighborhood of K and f   0 on X n U .
  *Proof:* Covers K with finitely many neighborhoods having compact closure, applies Urysohn's lemma to the union, and scales the function.
- **5.5 Corollary (Partition of Unity.)** If X is a locally compact Hausdorff space, K   X is compact, and if U1 ; : : : ; UN is any open cover for K, then there exist continuous 'j W X ! [0; 1] such that support 'j is a compact subset of Uj for each j , and jND1 'j   1 in a neighborhood of K.
  *Proof:* Constructs refined compact covers and applies Lemma 5.4 to build bump functions, normalizing their sum to form the partition.
- **5.7 Lemma.** Let X be a Hausdorff space and   a Radon measure on X. Then   automatically has the property (A) D sup K A; K compact (K ) for every  -measurable set A   X with  (A) < 1.
  *Proof:* Uses outer regularity to trap A between open and compact sets with an arbitrarily small measure gap.
- **5.8 Lemma.** Let X be a Hausdorff space and assume that   is an outer measure on X satisfying the properties (R2), (R3) above, and in addition assume that (K1 [ K2 ) D  (K1 ) C  (K2 ) < 1 whenever K1 ; K2 are compact and disjoint. Then (R1) holds and hence   is a Radon measure.
  *Proof:* Proves all open sets are measurable by approximating an arbitrary set and the open set simultaneously with compact and open covers to check Caratheodory's criterion.
- **5.9 Lemma.** Let X be a locally compact Hausdorff space and suppose that each open set is the countable union of compact subsets. Then any Borel regular outer measure on X which is finite on each compact set is automatically a Radon measure.
  *Proof:* Appeals to Theorem 1.22 since the space is sigma-compact, satisfying inner and outer regularity conditions.
- **5.10 Theorem.** Let X be a locally compact Hausdorff space,   a Radon measure on X and 1   p < 1. Then Cc (X ) is dense in Lp ( ); that is, for each " > 0 and each f 2 Lp there is a g 2 Cc (X ) such that kg f kp < ".
  *Proof:* Approximates by simple functions, uses inner regularity to shrink them to disjoint compact supports, and applies Urysohn's lemma.
- **5.11 Corollary.** If X is a locally compact Hausdorff space such that every open set in X is the countable union of compact sets, and if   is any Borel regular outer measure on X which is finite on each compact set, then the space Cc (X ) is dense in L1 ( ).
  *Proof:* (immediate from 5.10)
- **5.12 Theorem (Riesz for non-negative functionals.)** Suppose X is a locally compact Hausdorff space,   W KC ! [0; 1) with  (cf ) D c (f ),  (f C g ) D  (f ) C  (g ) whenever c   0 and f; g 2 KC , where KC is the set of all non-negative continuous functions f on X with compact support. Then there is a Radon measure   on X such that  (f ) D X f d  for all f 2 KC .
  *Proof:* Defines the measure variationally on open sets and extends to all sets. Proves it satisfies Radon conditions using Urysohn functions, and confirms integration matches the functional.
- **5.14 Theorem (Riesz Representation Theorem.)** Suppose X is a locally compact Hausdorff space, and L W Cc (X; H ) ! R is linear with sup f 2Cc (X;H );jf j 1; support f  K L(f ) < 1 whenever K   X is compact. Then there is a Radon measure   on X and Borel measurable   W X ! H with j j D 1 -a.e. on X, and L(f ) D X f;   d  for any f 2 Cc (X; H ).
  *Proof:* Defines a supremum-based total variation functional, applies Theorem 5.12 to get a Radon measure, uses classical Riesz representation for L1, and normalizes the vector field.
- **5.15 Theorem (Compactness Theorem for Radon Measures.)** Suppose { k } is a sequence of Radon measures on the locally compact,   -compact Hausdorff space X with the property supk  k (K ) < 1 for each compact K   X. Then there is a subsequence  k 0 which converges to a Radon measure   on X in the sense that lim  k 0 (f ) D  (f ) for each f 2 K(X );
  *Proof:* Uses Banach-Alaoglu to extract a weakly convergent subsequence of functionals and applies Theorem 5.12 to map the limit to a Radon measure.
- **1.2 Theorem.** If A is a non-empty subset of X and f W A ! R is Lipschitz, then 9 f W X ! R with Lip f D Lip f , and f D f jA. Also, f can be chosen so that supX jf j D supA jf j.
  *Proof:* Constructs the extension explicitly as the infimum of Lipschitz cones and caps it to preserve the uniform bound.
- **1.4 Theorem (Rademacher’s theorem.)** If f is Lipschitz on Rn , then f is differentiable Ln -almost everywhere; that is, the gradient rf (x ) D (D1 f (x ); : : : ; Dn f (x )) exists and ( ) lim y!x f (y ) f (x ) rf (x ) (y x) jy xj D 0 for Ln -a.e. x 2 Rn .
  *Proof:* Evaluates directional derivatives, proves they exist almost everywhere via absolute continuity on lines, and shows full differentiability using a countable dense set of directions.
- **1.5 Theorem. (C 1 Approximation Theorem.)** Suppose f W Rn ! R is Lipschitz. Then for each " > 0 there is a C 1 (Rn ) function g with Ln ( x W f (x ) ¤ g (x ) [ x W rf (x ) ¤ rg (x ) ) < ":
  *Proof:* Applies Rademacher's theorem, Egoroff's theorem, and Lusin's theorem to find a set of near-full measure where the gradient is continuous, then uses Whitney's extension.
- **1.6 Theorem (Whitney Extension Theorem.)** If C   Rn is closed and if h W C ! R and   W C ! Rn are continuous, and if for each compact K   C ( ) lim y!x; y2K R (x; y ) D 0 uniformly for x 2 K; where R (x; y ) D h(y ) h(x ) (x ) (y x) jx yj ; then there is a C 1 function g W Rn ! R such that g D h and rg D   on C .
  *Proof:* (no proof in this paper)
- **1.9 Theorem.** Suppose X; Y are metric spaces, X is  -compact, A   X is Hm-measurable, Hm (A) < 1 and f W A ! Y is Lipschitz, and let N (f; y ) D H0 (f 1 y ) (i.e. N (f; y ) is the multiplicity function, counting the number of points, possibly 1, in the preimage f 1 y). Then (i) f (A) is Hm -measurable. (ii) N (f; y ) is an Hm -measurable function of y 2 Y with Y N (f; y )d Hm   (Lip f )m Hm (A):
  *Proof:* Partitions the domain into tiny sets to approximate the multiplicity function, bounding the measure sum via the Lipschitz property.
- **1.10 Theorem.** Suppose X is a   -compact metric space, m 2 {1; 2; : : :}; k > 0 (k need not be an integer), A   X is HmCk -measurable and HmCk (A) < 1, and f W A ! Rm is Lipschitz. Then Hk (f 1 y ) is an Lm -measurable function of y 2 Rm and Rm Hk (f 1 y ) d Lm ( y ) !m !k !mCk (Lip f )m HmCk (A):
  *Proof:* Extends f to a global Lipschitz map, bounds the sum of preimage diameters using the isodiametric inequality, and integrates over range.
- **1.13 Lemma.** Suppose that     Rn is an open, bounded and convex. Then   is Lipschitz.
  *Proof:* Expresses the boundary near each point as a graph over a tangent plane and bounds the Lipschitz constant geometrically via convexity.
- **2.5 Lemma.** If u 2 BVloc (U ), then u(  ) ! u in L1loc (U ) and ˇDu(  ) ˇ ! jDuj in the sense of Radon measures in U (see 5.15 of Ch. 1) as   # 0.
  *Proof:* Exploits the dual characterization of the total variation via smooth test vector fields and leverages the uniform convergence of mollified test functions.
- **2.6 Theorem (Compactness Theorem for BV Functions.)** If uk is a sequence of BVloc (U ) functions satisfying sup k 1 (kuk kL1 (W ) C W ˇDuk ˇ) < 1 for each W    U , then there is a subsequence uk 0   uk and a BVloc (U ) function u such that uk 0 ! u in L1loc (U ) and W jDuj   lim inf W ˇDuk 0 ˇ 8W    U:
  *Proof:* Uses mollification and Arzela-Ascoli to prove precompactness in L1, then relies on lower semi-continuity of total variation.
- **2.7 Lemma.** Suppose U is bounded, open and convex, let ı 2 (0; 1) be such that there is R > 0 and   2 U with BıR (  )   U   BR (  ), and let u 2 BV (U ). Then for any 2 (0; 1) and any ˇ 2 R with ( ) min Ln x 2 U W u(x )   ˇ ; Ln x 2 U W u(x )   ˇ Ln (U ): we have U ju ˇj d Ln   CR U jDuj;
  *Proof:* Smooths u via mollifiers, applies the classical Poincaré inequality for smooth functions, and passes to the limit.
- **2.8 Lemma.** Suppose U; ı;  ; R are as in 2.7, u 2 BV (Rn ) with spt u   U . Then Rn jDuj   C U jDuj C R 1 U juj d Ln ;
  *Proof:* Scales the distance function to boundary, constructs a smooth cutoff function, and applies the product rule bound for BV variation.
- **3.3 Theorem (Area Formula.)** Suppose U is open in Rn and f W U ! Rm is locally Lipschitz, with n   m, and Jf is as in 3.2. Then A Jf d Ln D Rm H0 (A \ f 1 y ) d Hn (y ) for each Lebesgue measurable A   U .
  *Proof:* Decomposes the domain into measurable subsets where the derivative bounds the geometry, applying scaling estimates. (Proof truncated in this text).