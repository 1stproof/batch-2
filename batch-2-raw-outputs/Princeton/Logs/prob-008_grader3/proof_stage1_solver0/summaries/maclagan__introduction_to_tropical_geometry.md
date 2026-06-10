<!-- Generated 2026-05-31T02:37:20 -->
<!-- Source PDF: maclagan__introduction_to_tropical_geometry.pdf (1113141 bytes) -->
<!-- Citation: Maclagan, D., and Sturmfels, B. (2015). Introduction to Tropical Geometry. American Mathematical Society (Graduate Studies in Mathematics, Vol. 161). -->

# Introduction to Tropical Geometry (Maclagan and Sturmfels, 2015)

## Definitions
- **Definition 2.2.1.** Let K be a field. Affine space over K of dimension n is AnK = An = {(a1 , a2 , . . . , an ) : ai ∈ K} = K n . The n-dimensional projective space over the field K is PnK = Pn = (K n+1 \ 0)/ ∼ where v ∼ λv for all λ 6= 0. The points of Pn are the equivalence classes of lines through the origin 0. We write [v0 : v1 : · · · : vn ] for the equivalence class of v = (v0 , v1 , . . . , vn ) ∈ K n+1 . The n-dimensional algebraic torus is TnK = Tn = { (a1 , a2 , . . . , an ) : ai ∈ K ∗ }.
- **Definition 2.2.2.** The coordinate ring of the affine space An is the polynomial ring K[x1 , . . . , xn ]. The homogeneous coordinate ring of the projective space Pn is K[x0 , x1 , . . . , xn ], and the coordinate ring of the algebraic torus Tn is the Laurent polynomial ring K[x±1 1 , . . . , x±1 n ].
- **Definition 2.2.5.** The degree of a polynomial f = P cu xu in K[x1 , . . . , xn ] is W = max{|u| : cu 6= 0}, where |u| = Pn i=1 ui . The homogenization f˜ of f is the homogeneous polynomial f˜ = P cu xW −|u| 0 xu ∈ K[x0 , x1 , . . . , xn ]. Given an ideal I in K[x1 , . . . , xn ], its homogenization is the ideal Iproj = h f˜ : f ∈ Ii.
- **Definition 2.3.1.** A set X ⊆ Rn is convex if for all u, v ∈ X and all 0 ≤ λ ≤ 1 we have λu + (1 − λ)v ∈ X. The convex hull conv(U ) of a set U ⊆ Rn is the smallest convex set containing U . If U = {u1 , . . . , ur } is finite then conv(U ) = { Pri=1 λi ui : 0 ≤ λj ≤ 1, Pri=1 λi = 1} is called a polytope.
- **Definition 2.3.2.** Let Γ be a subgroup of R. A Γ-rational polyhedron is P = {x ∈ Rn : Ax ≤ b}, where A is a d × n matrix with entries in Q, and b ∈ Γd . A polyhedral complex Σ is Γ-rational if every polyhedron in Σ is Γ-rational. We will be interested in the case where Γ = Γval is the value group of a field K.
- **Definition 2.3.3.** Let P ⊂ Rn be a polyhedron. The normal fan of P is the polyhedral fan NP consisting of the cones NP (F ) = cl({w ∈ Rn∨ : facew (P ) = F }) as F varies over the faces of P where cl(·) denotes the closure in the Euclidean topology on Rn . The fan NP is also called the inner normal fan of P .
- **Definition 2.3.4.** Let S = K[x±1 1 , . . . , x±1 n ] be the Laurent polynomial ring. Given f = P u∈Zn cu xu ∈ S, the Newton polytope of f is the polytope Newt(f ) = conv(u : cu 6= 0) ⊂ Rn . If Newt(f ) is 2-dimensional then we call it the Newton polygon.
- **Definition 2.3.6.** Let Σ be a polyhedral complex in Rn , and let σ be a polyhedron in Σ. The star of σ ∈ Σ is a fan in Rn , denoted starΣ (σ), whose cones are indexed by those τ ∈ Σ for which σ is a face of τ . Fix w ∈ σ. Then the cone of starΣ (σ) that is indexed by τ is the Minkowski sum τ̄ = {v ∈ Rn : ∃  > 0 with w +  v ∈ τ } + aff(σ) − w. This is independent of the choice of w.
- **Definition 2.4.12.** The Gröbner complex Σ(I) of a homogeneous ideal I in K[x0 , x1 , . . . , xn ] is the polyhedral complex constructed in Theorem 2.4.11. It consists of the polyhedra CI [w] as w ranges over (Γval )n+1 .
- **Definition 2.5.3.** Let I be an ideal in the Laurent polynomial ring K[x± ] over a field K with a valuation. A finite generating set T of I is said to be a tropical basis if, for all weight vectors w ∈ Γnval , the initial ideal inw (I) contains a unit if and only if inw (T ) = {inw (f ) : f ∈ T } contains a unit.
- **Definition 3.1.1.** The tropical hypersurface trop(V (f )) is the set {w ∈ Rn : the minimum in trop(f ) is achieved at least twice }.
- **Definition 3.2.1.** Let I be an ideal in the Laurent polynomial ring K[x± ] = K[x±1 1 , . . . , x±1 n ] and let X = V (I) be its variety in the algebraic torus Tn . The tropicalization trop(X) of the variety X is the intersection of all tropical hypersurfaces defined by Laurent polynomials in the ideal I. In symbols, trop(X) = \ f ∈I trop(V (f )) ⊆ Rn .

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 1.1.2.** The tropical polynomials in n variables x1 , . . . , xn are precisely the piecewise-linear concave functions on Rn with integer coefficients.
  *Proof:* (no proof in this paper)
- **Proposition 1.2.1.** Let G be a weighted directed graph on n nodes with n × n adjacency matrix DG . Then the entry of the matrix DGn−1 in row i and column j equals the length of a shortest path from node i to node j in G.
  *Proof:* Uses the recursive formula for lengths of shortest paths and induction on the number of edges.
- **Proposition 1.2.3.** The optimal value of (1.6) is the coefficient of the monomial xb11 xb22 · · · xbdd in the mth power of the tropical polynomial (1.7).
  *Proof:* (no proof in this paper)
- **Proposition 1.2.5.** The tropical determinant solves the assignment problem.
  *Proof:* (no proof in this paper)
- **Proposition 1.3.1.** The curve V (p) is a finite graph which is embedded in the plane R2 . It has both bounded and unbounded edges, all edge slopes are rational, and this graph satisfies a zero tension condition around each node.
  *Proof:* (no proof in this paper)
- **Theorem 1.3.2 (Bézout).** Consider two tropical curves C and D of degree c and d in R2 . If the two curves intersect transversally, then the number of intersection points, counted with multiplicities as above, is equal to c · d.
  *Proof:* (no proof in this paper)
- **Theorem 1.3.3 (Stable Intersection Principle).** The limit of the point configuration C  ∩ D  is independent of the choice of perturbations. It is a well-defined multiset of c · d points contained in the intersection C ∩ D.
  *Proof:* (no proof in this paper)
- **Corollary 1.3.4.** Any two curves of degrees c and d in R2 , no matter how special they might be, intersect stably in a well-defined multiset of cd points.
  *Proof:* (immediate from Theorem 1.3.3)
- **Theorem 1.4.2.** The tropical variety of I coincides with the cone over the logarithmic limit set A∞ (I), i.e., a non-zero vector w ∈ Rn lies in trop(I) if and only if the corresponding unit vector 1/||w|| w lies in A∞ (I).
  *Proof:* (no proof in this paper)
- **Corollary 1.4.3.** The stabilizer Stab(I) ⊂ GL(n, Z) of a proper ideal I ⊂ S has a subgroup of finite index which stabilizes a nontrivial sublattice of Zn .
  *Proof:* Uses the invariance of the fan structure of the tropical variety under the stabilizer action to find a finite-index subgroup fixing a linear subspace.
- **Theorem 1.5.2.** The tropical curve V (f ) defined by the unknown polynomial coincides with the tropical curve determined by the vectors in (1.11).
  *Proof:* (no proof in this paper)
- **Corollary 1.5.3.** The polygon P + coincides with the Newton polygon Newt(f ) of the defining irreducible polynomial of the parametrized curve Image(Φ).
  *Proof:* Uses the rotation and concatenation of rays of the tropical curve to reconstruct the Newton polygon.
- **Proposition 1.6.1.** The group Gξ = hA, Xi is finitely presented if and only if either the real number ξ or its reciprocal 1/ξ is an algebraic integer over Q.
  *Proof:* (no proof in this paper)
- **Theorem 1.6.2 (Bieri-Strebel).** The Z-algebra R = S/I is finitely generated as a Z-module if and only if tropZ (I) = {0}.
  *Proof:* (no proof in this paper)
- **Theorem 1.6.5 (Bieri-Strebel).** The metabelian group GI is finitely presented if and only if the integer tropical variety tropZ (I) contains no line.
  *Proof:* (no proof in this paper)
- **Lemma 1.6.6.** The metabelian group GI is generated by the n + 1 matrices A = (1 1 \\ 0 1) and Xi = (1 0 \\ 0 xi) for i = 1, 2, . . . , n.
  *Proof:* (no proof in this paper)
- **Lemma 1.6.7.** The relations (1.17) define a presentation of the group Gh0i .
  *Proof:* (no proof in this paper)
- **Proposition 1.6.8.** For any ideal I in S, the group GI has the presentation [Xi , Xj ] = [A, Am ] = Af = 1, where m runs over monomials, f runs over I, and 1 ≤ i < j ≤ n.
  *Proof:* Transforms any word representing the polynomial generator into an alternating sum of monomials using conjugation relations.
- **Theorem 1.6.9.** Fix a tropical basis B satisfying (1.19) for the ideal I. Then the metabelian group GI is presented by the relations (1.17) where f runs over the elements in the tropical basis B and m = xu runs over the set Newton(B) ∩ Zn of lattice points u in the Newton polytope the tropical basis.
  *Proof:* (no proof in this paper)
- **Theorem 1.7.4.** The Gromov-Witten numbers Ng,d can be found tropically.
  *Proof:* (no proof in this paper)
- **Theorem 1.7.5 (Mikhalkin’s Correspondence Principle).** The number of simple tropical curves of degree d and genus g that pass through g + 3d − 1 general points in R2 , where each curve is counted with its multiplicity, is equal to the Gromov-Witten number Ng,d of the complex projective plane P2 .
  *Proof:* (no proof in this paper)
- **Lemma 2.1.1.** If val(a) 6= val(b) then val(a + b) = min(val(a), val(b)).
  *Proof:* Uses the valuation axioms and properties of neutral elements to bound the valuation from both sides.
- **Theorem 2.1.4.** The field K = k{{t}} of Puiseux series is algebraically closed when k is an algebraically closed field of characteristic zero.
  *Proof:* Constructs roots by iteratively finding zeros of the initial forms of the shifted polynomials, scaling by the Newton polygon slopes to ensure termination.
- **Theorem 2.1.8.** Fix a divisible group G and an algebraically closed residue field k. Let K be a field with a valuation val with value group G = Γval and residue field k. If val is trivial on the prime field (Fp or Q) of K, then K is isomorphic to a subfield of k((G)).
  *Proof:* (no proof in this paper)
- **Lemma 2.1.11.** Let K be algebraically closed with non-trivial valuation. Then the value group Γval is a divisible subgroup of R that is dense in R.
  *Proof:* Relies on the existence of fractional roots in algebraically closed fields.
- **Lemma 2.1.13.** If K is algebraically closed then the surjection K ∗   Γval splits: there is a group homomorphism ψ : Γval → K ∗ with val(ψ(w)) = w.
  *Proof:* Constructs homomorphisms from rational summands using the divisibility and torsion-free properties of the value group and multiplicative group.
- **Proposition 2.2.6.** Let X = V (I) be a subvariety of the torus Tn for an ideal I ⊂ K[x±1 1 , . . . , x±1 n ]. Then i(X) = V (Iaff ), where Iaff = I ∩ K[x1 , . . . , xn ]. For an ideal I ⊂ K[x1 , . . . , xn ], the projective closure j(X) of V (I) is the subvariety of projective space Pn defined by the homogeneous ideal Iproj .
  *Proof:* Verifies mutual containment by showing polynomials in the respective ideals vanish on the corresponding closures.
- **Lemma 2.2.9.** Given any vector v ∈ Zn with the greatest common divisor of the |vi | equal to one, there is a matrix U ∈ GL(n, Z) with U v = e1 . Further, if L is a rank k subgroup of Zn with Zn /L torsion-free then there is a matrix U ∈ GL(n, Z) with U L equal to the subgroup generated by e1 , . . . , ek .
  *Proof:* Applies the Smith normal form to the basis matrix of the subgroup to find invertible transformations.
- **Lemma 2.4.2.** Let I ⊂ K[x0 , . . . , xn ] be a homogeneous ideal and w ∈ (Γval )n+1 . Then inw (I) is homogeneous, and we may choose a homogeneous Gröbner basis for I. Further, if g ∈ inw (I) then g = inw (f ) for some f ∈ I.
  *Proof:* Decomposes polynomials into homogeneous parts and reconstructs polynomials by lifting the coefficients of the initial terms.
- **Lemma 2.4.4.** Let I ⊆ K[x0 , . . . , xn ], and fix w, v ∈ Γn+1 val . Then there exists  > 0 such that the following holds for all  0 ∈ Γval with 0 <  0 <  : inv (inw (I)) = inw+ 0 v (I).
  *Proof:* Proves the claim for single polynomials using the linearity of the minimum form, then bounds the perturbation for a finite generating set.
- **Proposition 2.4.5.** Fix a homogeneous ideal I in S = K[x0 , x1 , . . . , xn ] and ν ∈ N. For each w ∈ (Γval )n+1 lying outside a finite union of hyperplanes in Rn , the monomials of degree ν outside of inw (I)ν form a K-basis for (S/I)ν . More precisely, each polynomial f ∈ Sν has a unique representation f = j +r where j ∈ I, ST(r)  w ST(f ), and r is a sum of terms not in inw (I).
  *Proof:* Uses generic weights and invertible submatrices of the coefficient matrix to identify linearly independent monomials that avoid the initial ideal.
- **Corollary 2.4.6.** For any w ∈ Γn+1 val and any homogeneous ideal I in SK , the Hilbert functions of I agrees with that of its initial ideal inw (I) ⊂ Sk , i.e. dimK (SK /I)ν = dimk (Sk / inw (I))ν for all ν ≥ 0. Thus the Krull dimensions of the residue rings SK /I and Sk / inw (I) coincide.
  *Proof:* Shows that generic combinations of basis elements preserve linear independence of monomials via a reduction to the generic weight case.
- **Lemma 2.4.8.** If I ⊂ SK is a homogeneous prime of dimension d, and w ∈ (Γval )n+1 , then every minimal associated prime of inw (I) has dimension d.
  *Proof:* Adjoins the formal variable and localizes to construct a one-dimensional Noetherian subring, then applies the Principal Ideal Theorem.
- **Theorem 2.4.11.** The polyhedra CI [w] as w varies over (Γval )n+1 form a (Γval )-rational polyhedral complex inside the n-dimensional space Rn+1/R1.
  *Proof:* Uses the Plücker embedding of the Grassmannian and bounds on monomial ideals to construct the cells of the complex.
- **Corollary 2.4.14.** Every homogeneous ideal I ⊂ K[x0 , . . . , xn ] has finite universal Gröbner basis.
  *Proof:* Takes the union of Gröbner bases computed for representative vectors over the finitely many cells of the Gröbner complex.
- **Corollary 2.4.15.** Let I be a homogeneous ideal with constant coefficients. Then the negated Gröbner complex −Σ(I) is equal to the Gröbner fan of I.
  *Proof:* (no proof in this paper)
- **Proposition 2.5.1.** Let I be an ideal in K[x± ], and fix w ∈ (Γval )n . Then inw (I) equals the image of in(0,w) (Iproj ) in k[x± ] obtained by setting x0 = 1.
  *Proof:* Relates the initial forms of polynomials to their homogenizations, then extends to ideals by taking a homogeneous Gröbner basis.
- **Lemma 2.5.2.** Let I be an ideal in K[x±1 1 , . . . , x±1 n ], and fix w ∈ (Γval )n . 1. If inw (I) = h1i, then there is f ∈ I with inw (f ) = 1. 2. If inv (inw (I)) = inw (I) for v ∈ Zn , then inw (I) is homogeneous with respect to the grading given by deg(xi ) = vi . 3. If g ∈ inw (I), then g = inw (h) for some h ∈ I. 4. If f, g ∈ K[x±1 1 , . . . , x±1 n ], then inw (f g) = inw (f ) inw (g).
  *Proof:* Utilizes the homogenized ideal, evaluates degree minimums, and directly applies the definitions of initial forms and Gröbner bases.
- **Theorem 2.5.4.** Every ideal I in K[x± ] has a finite tropical basis.
  *Proof:* Chooses a representative vector for each cell of the Gröbner complex and adds to the generating set the polynomials that yield unit initial forms.
- **Lemma 2.5.7.** Let φ∗ : K[x±1 1 , . . . , x±1 m ] → K[x±1 1 , . . . , x±1 n ] be a monomial map. Let I ⊆ K[x±1 1 , . . . , x±1 m ] be an ideal, and let I 0 = φ∗ −1 (I). Then φ∗ (inφ(w) (I 0 )) ⊆ inw (I) for all w ∈ (Γval )n . Thus, in particular, if inw (I) 6= h1i then we also have inφ(w) (I 0 ) 6= h1i.
  *Proof:* Applies the monomial transformation to initial forms and tracks the effect on minimum weights.
- **Corollary 2.5.8.** Let φ∗ : K[x±1 1 , . . . , x±1 n ] → K[x±1 1 , . . . , x±1 n ] be a monomial automorphism, let I ∈ K[x±1 1 , . . . , x±1 n ] and let I 0 = φ∗ −1 (I). Then inw (I) = h1i if and only if inφ(w) (I 0 ) = h1i.
  *Proof:* (immediate from Lemma 2.5.7)
- **Theorem 3.1.3 (Kapranov’s Theorem).** Fix a Laurent polynomial f = P u∈Zn cu xu in K[x± ] = K[x±1 1 , . . . , x±1 n ]. The following three sets coincide: 1. the tropical hypersurface trop(V (f )) in Rn ; 2. the closure in Rn of the set {w ∈ (Γval )n : inw (f ) is not a monomial }; 3. the closure of the set { (val(v1 ), . . . , val(vn )) : v ∈ V (f ) }. In addition, if w = val(v) for v ∈ (K ∗ )n with f (v) = 0 and n > 1 then Uw = {v0 ∈ V (f ) : val(v0 ) = w} is an infinite subset of the hypersurface V (f ).
  *Proof:* Shows mutual equivalence of the definitions by using properties of minimum valuations, and relies on Proposition 3.1.5 for the existence of infinite roots.
- **Proposition 3.1.5.** Let f = P u∈Zn cu xu ∈ K[x±1 1 , . . . , x±1 n ], and let w ∈ Γnval . If inw (f ) is not a monomial, let α ∈ (k∗ )n satisfy inw (f )(α) = 0. Then there exists y ∈ (K ∗ )n with f (y) = 0, val(y) = w, and t−w y = α. If n > 1 then there are infinitely many such y.
  *Proof:* Proceeds by induction on the number of variables, handling cases where the initial form vanishes or doesn't vanish on hyperplanes by lifting roots.
- **Proposition 3.1.6.** Let f ∈ K[x± ] be a Laurent polynomial. The tropical hypersurface trop(V (f )) is the support of a pure polyhedral complex of dimension n − 1.
  *Proof:* (no proof in this paper)
- **Proposition 3.1.7.** Suppose that all coefficients of the Laurent polynomial f have zero valuation. Then trop(V (f )) is the support of (n−1)-dimensional polyhedral fan. This fan is the (n − 1)-dimensional skeleta of the normal fan to the Newton polyhedron of f .
  *Proof:* (no proof in this paper)
- **Corollary 3.2.3.** Every tropical variety is a finite intersection of tropical hypersurfaces. More precisely, if T is a tropical basis of the ideal I then trop(X) = \ f ∈T trop(V (f )).
  *Proof:* Directly applies the definition of a tropical basis to show that non-membership in the variety implies non-membership in one of the basis hypersurfaces.
- **Theorem 3.2.4 (Fundamental Theorem of Tropical Algebraic Geometry).** Let I be an ideal in K[x± ] and X = V (I) its variety in the algebraic torus Tn ∼= (K ∗ )n . Then the following three subsets of Rn coincide: 1. The tropical variety trop(X) as defined in equation (3.1); 2. the closure in Rn of the set of all vectors w ∈ (Γval )n with inw (I) 6= h1i; 3. the closure in Rn of the set of coordinatewise valuations of points in X: val(X) = {(val(u1 ), . . . , val(un )) : (u1 , . . . , un ) ∈ X}.
  *Proof:* Evaluates non-unit initial ideals to equate the first two definitions, then utilizes Kapranov's theorem and reduces to irreducible components to prove equivalence with the third.
- **Lemma 3.2.5.** Let X ⊂ Tn be an irreducible variety of dimension d, with prime ideal I ⊂ K[x± ], and w ∈ trop(X) ∩ Γnval . Then all minimal associated primes of the initial ideal inw (I) in k[x± ] have the same dimension d.
  *Proof:* Homogenizes the ideal and applies the Principal Ideal Theorem to preserve dimensions through minimal primes.
- **Proposition 3.2.6.** Let X be a subvariety of Tn . Then there exists a projection φ : Tn → Tm for which the image φ(X) ⊂ Tm is closed in the Zariski topology. This projection can be chosen so that the kernel of the associated map φ : Rn → Rm does not nontrivially intersect a finite number of subspaces of Rn .
  *Proof:* (no proof in this paper)
- **Proposition 3.2.7.** Let I be an ideal in K[x±1 ]. The set {w ∈ Rn : inw (I) 6= h1i} is the support of an (Γval )-rational polyhedral complex.
  *Proof:* Uses the homogenized Gröbner complex to express the locus as a union of cells that do not contain monomials.
- **Lemma 3.2.8.** Let X ⊂ Tn have dimension d, with ideal I ⊆ K[x±1 1 , . . . , x±1 n ]. Then every polyhedron in the polyhedral complex Σ whose support is the set {w ∈ (Γval )n : inw (I) 6= h1i} has dimension at most d.
  *Proof:* Rotates the affine span to standard coordinates and counts variables avoided by the initial ideal to bound the dimension.
- **Proposition 3.2.9.** Let X be an irreducible d-dimensional subvariety of Tn , with ideal I = IX ⊆ K[x±1 ]. Fix w ∈ Γnval with inw (I) 6= h1i, and α ∈ (k∗ )n ∈ V (inw (I)). Then there is y ∈ X with val(y) = w and t−w y = α. If dim(X) > 0 then there are infinitely many such y.
  *Proof:* Projects onto a lower-dimensional torus to apply the inductive hypothesis, then lifts the roots using the properties of the initial ideal.