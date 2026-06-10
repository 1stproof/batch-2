<!-- Generated 2026-05-31T03:12:17 -->
<!-- Source PDF: chmutov__introduction_to_vassiliev_knot_invariants.pdf (6055004 bytes) -->
<!-- Citation: S. Chmutov, S. Duzhin, J. Mostovoy (2012). Introduction to Vassiliev Knot Invariants. Cambridge University Press. -->

# Introduction to Vassiliev Knot Invariants (S. Chmutov, S. Duzhin, J. Mostovoy, 2012)

## Definitions
- **1.1.1. Definition.** A parametrized knot is an embedding of the circle S 1 into the Euclidean space R3 .
- **1.2.1. Definition.** A smooth isotopy of a knot f : S 1 → R3 , is a smooth family of knots fu , with u a real parameter, such that for some value u = a we have fa = f .
- **1.2.2. Definition.** Two parametrized knots are said to be isotopic if one can be transformed into another by means of a smooth isotopy. Two oriented knots are isotopic if they represent the classes of isotopic parametrized knots; the same definition is valid for unoriented knots.
- **[Missing label] Definition.** Two parametrized knots, f and g, are ambient equivalent if there is a commutative diagram
                                                    f
                                         S 1 −−−−→ R3
                                                  
                                        ϕy
                                                  ψ
                                                   y
                                                    g
                                         S 1 −−−−→ R3
where ϕ and ψ are orientation preserving diffeomorphisms of the circle and the 3-space, respectively.
- **[Missing label] Definition.** Two parametrized knots, f and g, are ambient isotopic if there is a smooth family of diffeomorphisms of the 3-space ψt : R3 → R3 with ψ0 = id and ψ1 ◦ f = g.
- **1.2.5. Definition.** A link is a smooth embedding S 1 t · · · t S 1 → R3 , where S 1 t · · · t S 1 is the disjoint union of several circles.
- **1.4.1. Definition.** A knot is called:
      • invertible, if K ∗ = K,
      • plus-amphicheiral, if K = K,
      • minus-amphicheiral, if K = K ∗ ,
                                               ∗
      • fully symmetric, if K = K ∗ = K = K ,
                                                       ∗
      • totally asymmetric, if all knots K, K ∗ , K, K are different.
- **1.5.2. Definition.** A knot is called prime if it cannot be represented as the connected sum of two nontrivial knots.
- **1.7.1. Definition.** A (parametrized) tangle is a smooth embedding of a one-dimensional compact oriented manifold, X, possibly with boundary, into a box
        {(x, y, z) | w0 ⩽ x ⩽ w1 , −1 ⩽ y ⩽ 1 , h0 ⩽ z ⩽ h1 } ⊂ R3 ,
where w0 , w1 , h0 , h1 ∈ R, such that the boundary of X is sent into the intersection of the (open) upper and lower faces of the box with the plane y = 0. An oriented tangle is a tangle considered up to an orientation-preserving change of parametrization; an unoriented tangle is the image of a parametrized tangle.
- **[Missing label] Definition.** A string link on n strings (or strands) is an (oriented or unoriented) tangle whose skeleton consists of n intervals, the ith interval connecting pi with qi . A string link on one string is called a long knot .
- **[Missing label] Definition.** An unoriented string link on n strings whose tangent vector is never horizontal is called a pure braid on n strands.
- **[Missing label] Definition.** A braid on n strands is an (unoriented) tangle whose skeleton consists of n intervals, the ith interval connecting pi with qσ(i) , with the property that the tangent vector to it is never horizontal.
- **[Missing label] Definition.** A Gauss diagram is an oriented circle with a distinguished set of distinct points divided into ordered pairs, each pair carrying a sign ±1.
- **[Missing label] Definition.** A virtual knot is a Gauss diagram considered up to the Reidemeister moves V Ω1 , V Ω2 , V Ω3 . A long, or based virtual knot is a based Gauss diagram, considered up to Reidemeister moves that do not involve segments with the basepoint on them.
- **[Missing label] Definition.** A knot invariant with values in a set S is a map from K to S.
- **[Missing label] Definition.** The crossing number c(K) of a knot K is the minimal number of crossing points in a plane diagram of K.
- **[Missing label] Definition.** The unknotting number u(K) of a knot K is the minimal number of crossing changes in a plane diagram of K that convert it to a trivial knot, provided that any number of plane isotopies and Reidemeister moves is also allowed.
- **[Missing label] Definition.** The self-linking number of K is the linking number of K and K 0.
- **2.3.1. Definition.** The Conway polynomial C is an invariant of oriented links (and, in particular, an invariant of oriented knots) taking values in the ring Z[t] and defined by the two properties:

                                 
                    C               = 1,

                                                                
                    C               −C              = tC           .
- **[Missing label] Definition.** Let f be a map of a one-dimensional manifold to R3 . A point p ∈ im(f ) ⊂ R3 is a double point of f if f −1 (p) consists of two points t1 and t2 and the two tangent vectors f 0 (t1 ) and f 0 (t2 ) are linearly independent.
- **3.1.3. Definition. (V. Vassiliev [Va1]).** A knot invariant is said to be a Vassiliev invariant (or a finite type invariant) of order (or degree) ⩽ n if its extension vanishes on all singular knots with more than n double points. A Vassiliev invariant is said to be of order (degree) n if it is of order ⩽ n but not of order ⩽ n − 1.
- **[Missing label] Definition.** Let R be a commutative ring. A Vassiliev invariant of order ⩽ n is a linear function ZK → R which vanishes on Kn+1 .
- **[Missing label] Definition.** Two knots K1 and K2 are n-equivalent if they cannot be distinguished by Vassiliev invariants of degree n and smaller with values in an arbitrary abelian group. A knot that is n-equivalent to the trivial knot is called n-trivial.
- **[Missing label] Definition.** Let Γn K be the set of (n − 1)-trivial knots. The Goussarov filtration on K is the descending filtration
                     K = Γ1 K ⊇ Γ2 K ⊇ . . . ⊇ Γn K ⊇ . . .
- **[Missing label] Definition.** A chord diagram of order n (or degree n) is an oriented circle with a distinguished set of n disjoint pairs of distinct points, considered up to orientation preserving diffeomorphisms of the circle. The set of all chord diagrams of order n will be denoted by An .
- **[Missing label] Definition.** The chord diagram σ(K) ∈ An of a singular knot with n double points is obtained by marking on the parametrizing circle n pairs of points whose images are the n double points of the knot.
- **4.1.1. Definition.** A function f ∈ RAn is said to satisfy the 4-term (or 4T) relations if the alternating sum of the values of f is zero on the following quadruples of diagrams:

(4.1.1)        f(      ) − f(     ) + f(      ) − f(      ) = 0.
In this case f is also called a (framed) weight system of order n.
- **4.1.3. Definition.** An isolated chord is a chord that does not intersect any other chord of the diagram. A function f ∈ RAn is said to satisfy the 1-term relations if it vanishes on every chord diagram with an isolated chord. An unframed weight system of order n is a weight system that satisfies the 1-term relations.
- **4.4.2. Definition.** The space Afnr of chord diagrams of order n is the vector space generated by the set An (all diagrams of order n) modulo the subspace spanned by all 4-term linear combinations

                          −          +         −          .

The space An of unframed chord diagrams of order n is the quotient of Afnr by the subspace spanned by all diagrams with an isolated chord.
- **[Missing label] Definition.** The product of two chord diagrams D1 and D2 is defined by cutting and glueing the two circles as shown:
                               ·          =                    =

## Lemmas, Theorems, Propositions, Corollaries
- **1.3.1. Theorem (Reidemeister [Rei], proofs can be found in [PS, BZ, Mur2]).** Two unoriented knots K1 and K2 , are equivalent if and only if a diagram of K1 can be transformed into a diagram of K2 by a sequence of ambient isotopies of the plane and local moves of the following three types:
  *Proof:* (no proof in this paper)
- **[Missing label] Theorem (Markov [Mark, Bir1]).** Two closed braids are equivalent (as links) if and only if the braids are related by a finite sequence of the following Markov moves:
   (M1) b ←→ aba−1 for any a, b ∈ Bn ;
   (M2) Bn 3          b        ←→        b               ∈ Bn+1 ,         b        ←→        b        .
                     ...                ...                              ...                ...
  *Proof:* (no proof in this paper)
- **[Missing label] Theorem ([Tur3]).** Two products of simple tangles are isotopic if and only if they are related by a finite sequence of the following Turaev moves.
  *Proof:* (no proof in this paper)
- **1.8.2. Theorem (framed Reidemeister theorem).** Two knot diagrams with blackboard framing D1 and D2 are equivalent if and only if D1 can be transformed into D2 by a sequence of plane isotopies and local moves of three types F Ω1 , Ω2 , and Ω3 , where
                     F Ω1 :
while Ω2 and Ω3 are usual Reidemeister moves defined in 1.3.1.
  *Proof:* (no proof in this paper)
- **2.2.1. Proposition.**
                             X               X               1X
                lk(A, B) =          w(p) =          w(p) =      w(p)
                                                             2
                                A
                             p∈IB               B
                                             p∈IA             p∈I

where w(p) = ±1 is the local writhe of the crossing point.
  *Proof:* Relies on the fact that crossing switches make the two components unlinked, and each switch algebraically shifts the linking number by the negative of its local writhe.
- **[Missing label] Theorem.** Let A and B be two non-intersecting curves in R3 , parameterized, respectively, by the smooth functions α, β : S 1 → R3 . Then
                                         (β(v) − α(u), du, dv)
                                Z
                              1
                 lk(A, B) =                                    ,
                             4π S 1 ×S 1    |β(v) − α(u)|3
where the parentheses in the numerator stand for the mixed product of 3 vectors.
  *Proof:* (no proof in this paper)
- **[Missing label] Proposition.** The self-linking number of a framed knot given by a diagram D with blackboard framing is equal to the total writhe of the diagram D.
  *Proof:* Notes that for the blackboard framing, all crossings with the shifted knot occur exactly near the self-crossings with matching writhes, so the result follows from the linking number formula.
- **[Missing label] Theorem.** The product of two Vassiliev invariants of degrees ⩽ p and ⩽ q is a Vassiliev invariant of degree ⩽ p + q.
  *Proof:* Evaluates the complete resolution of a singular knot with $p+q+1$ double points as an alternating sum over an $n$-dimensional binary cube, then applies a lemma about alternating sums of functions on cubes.
- **[Missing label] Lemma.** Let f, g be functions on Qn , where n = p+q +1. If the alternating sums of f over any (p + 1)-face, and of g over any (q + 1)-face of Qn are zero, so is the alternating sum of the product f g over the entire cube Qn .
  *Proof:* Applies induction on $n$ utilizing a difference operator $\delta$ that projects to $(n-1)$-dimensional faces and satisfies a Leibniz rule.
- **3.3.1. Proposition.** V0 = {const}, dim V0 = 1.
  *Proof:* Any invariant of degree 0 has a jump of 0 across any crossing change, meaning its value on any knot must equal its value on the unknot.
- **3.3.2. Proposition.** V1 = V0 .
  *Proof:* Pulls the single double point into a "figure infinity" configuration where the singular knot vanishes.
- **3.3.3. Proposition.** dim V2 = 2.
  *Proof:* Shows any knot with two double points reduces to one of two cyclic orderings (1122 or 1212); deduces the kernel is $V_1$ and the quotient image is bounded by 1, with the Conway $c_2$ coefficient providing the non-constant invariant.
- **3.4.2. Proposition. (V. Vassiliev [Va1]).** The value of a Vassiliev invariant v of order ⩽ n on a knot K with n double points depends only on the chord diagram of K:
                       σ(K1 ) = σ(K2 ) ⇒ v(K1 ) = v(K2 ).
  *Proof:* Aligns the two singular knots at their double points and deforms them into each other, noting that all newly created double points yield zero since the invariant vanishes beyond degree $n$.
- **3.4.3. Corollary.** The module of R-valued Vassiliev invariants of degree at most n is finitely generated over R.
  *Proof:* (immediate from 3.4.2. Proposition)
- **[Missing label] Theorem ([G1, BL, BN1]).** The coefficient jn (K) is a Vassiliev invariant of order ⩽ n.
  *Proof:* Expands the Jones skein relation with $t=e^h$ to show the difference across a resolved crossing is divisible by $h$, making any knot with $k$ double points $O(h^k)$.
- **[Missing label] Theorem ([BL, BN1]).** The coefficient θn (K) is a Vassiliev invariant of order ⩽ n.
  *Proof:* Mirroring the Jones polynomial proof, this utilizes the fact that an R-matrix $R$ and its inverse $R^{-1}$ are congruent modulo $h$.
- **[Missing label] Theorem.** The Casson invariant coincides with the second coefficient of the Conway polynomial c2 .
  *Proof:* Verifies the Gauss diagram formula is independent of basepoint and invariant under Reidemeister moves, checks that it evaluates to 0 on the unknot and 1 on the trefoil, and proves it has degree 2.
- **[Missing label] Lemma.** The linking number of two components of a tangle is a Vassiliev invariant of order 1.
  *Proof:* Resolves a double point via the Vassiliev skein relation to show it evaluates to 0 on self-intersections and 1 on cross-component intersections, forcing any two-component link with two double points to evaluate to zero.
- **4.2.1. Theorem (Vassiliev–Kontsevich).** For R = C the map αn identifies Vn /Vn−1 with the subspace of unframed weight systems Wn ⊂ RAn . In other words, the space of unframed weight systems is isomorphic to the graded space associated with the filtered space of Vassiliev invariants,
                              ∞           ∞
                                      ∼
                             M           M
                      W=         Wn =        Vn /Vn+1 .
                             n=0           n=0
  *Proof:* (no proof in this paper)
- **[Missing label] Lemma (4-term relation for knots).** Any Vassiliev invariant satisfies
                                                                          
           f            −f                 +f                −f              = 0,
  *Proof:* Applies the Vassiliev skein relation to explicitly expand each of the four terms into differences of pairs, demonstrating that the full alternating sum algebraically cancels to zero.
- **4.3.2. Theorem.** The bialgebra of knots FK considered with the singular knot filtration is a bialgebra with a decreasing filtration (see Section A.2.3).
  *Proof:* Confirms the multiplication respects the filtration $K_m K_n \subseteq K_{m+n}$ and uses commutator relations between the coproduct $\delta$ and the crossing-flip operators to show $\delta(K_n) \subseteq \sum K_p \otimes K_q$.
- **4.3.3. Lemma.**
                        δ ◦ σi = (σi ⊗ id + si ⊗ σi ) ◦ δ,

where both the left-hand side and the right-hand side are understood as linear operators from XK into XK ⊗ XK .
  *Proof:* Verified directly by evaluating both operator expressions on an arbitrary element of the expanded knot basis.
- **4.3.6. Proposition.** The algebra of F-valued Vassiliev knot invariants V F is a bialgebra with an increasing filtration (page 475).
  *Proof:* (immediate from 4.3.2. Theorem)
- **[Missing label] Lemma.** The product is well-defined modulo 4T relations.
  *Proof:* Proves that rotating one diagram inside the other by one "click" corresponds to moving a chord endpoint around the fixed diagram, which algebraically expands precisely into a sum of $n$ four-term relations.