<!-- Generated 2026-05-31T03:12:12 -->
<!-- Source PDF: chmutov__introduction_to_vassiliev_knot_invariants.pdf (6055004 bytes) -->
<!-- Citation: Chmutov, S., Duzhin, S. and Mostovoy, J. (2012). Introduction to Vassiliev Knot Invariants. Cambridge University Press. -->

# Introduction to Vassiliev Knot Invariants (Chmutov, Duzhin, and Mostovoy, 2012)

## Definitions
- **1.1.1. Definition.** A parametrized knot is an embedding of the circle $S^1$ into the Euclidean space $R^3$.
- **1.2.1. Definition.** A smooth isotopy of a knot $f : S^1 \to R^3$, is a smooth family of knots $f_u$, with $u$ a real parameter, such that for some value $u = a$ we have $f_a = f$.
- **1.2.2. Definition.** Two parametrized knots are said to be isotopic if one can be transformed into another by means of a smooth isotopy. Two oriented knots are isotopic if they represent the classes of isotopic parametrized knots; the same definition is valid for unoriented knots.
- **Definition.** Two parametrized knots, $f$ and $g$, are ambient equivalent if there is a commutative diagram
- **Definition.** Two parametrized knots, $f$ and $g$, are ambient isotopic if there is a smooth family of diffeomorphisms of the 3-space $\psi_t : R^3 \to R^3$ with $\psi_0 = id$ and $\psi_1 \circ f = g$.
- **1.2.5. Definition.** A link is a smooth embedding $S^1 \sqcup \cdots \sqcup S^1 \to R^3$, where $S^1 \sqcup \cdots \sqcup S^1$ is the disjoint union of several circles.
- **1.4.1. Definition.** A knot is called:
      • invertible, if $K^* = K$,
      • plus-amphicheiral, if $K = \overline{K}$,
      • minus-amphicheiral, if $K = \overline{K}^*$,
      • fully symmetric, if $K = K^* = \overline{K} = \overline{K}^*$,
      • totally asymmetric, if all knots $K, K^*, \overline{K}, \overline{K}^*$ are different.
- **1.5.2. Definition.** A knot is called prime if it cannot be represented as the connected sum of two nontrivial knots.
- **1.7.1. Definition.** A (parametrized) tangle is a smooth embedding of a one-dimensional compact oriented manifold, $X$, possibly with boundary, into a box $\{(x, y, z) \mid w_0 \leqslant x \leqslant w_1 , -1 \leqslant y \leqslant 1 , h_0 \leqslant z \leqslant h_1 \} \subset R^3$, where $w_0 , w_1 , h_0 , h_1 \in R$, such that the boundary of $X$ is sent into the intersection of the (open) upper and lower faces of the box with the plane $y = 0$. An oriented tangle is a tangle considered up to an orientation-preserving change of parametrization; an unoriented tangle is the image of a parametrized tangle.
- **Definition.** A string link on $n$ strings (or strands) is an (oriented or unoriented) tangle whose skeleton consists of $n$ intervals, the $i$th interval connecting $p_i$ with $q_i$. A string link on one string is called a long knot .
- **Definition.** An unoriented string link on $n$ strings whose tangent vector is never horizontal is called a pure braid on $n$ strands.
- **Definition.** A braid on $n$ strands is an (unoriented) tangle whose skeleton consists of $n$ intervals, the $i$th interval connecting $p_i$ with $q_{\sigma(i)}$, with the property that the tangent vector to it is never horizontal.
- **Definition.** A Gauss diagram is an oriented circle with a distinguished set of distinct points divided into ordered pairs, each pair carrying a sign $\pm 1$.
- **Definition.** A virtual knot is a Gauss diagram considered up to the Reidemeister moves $V \Omega_1, V \Omega_2, V \Omega_3$. A long, or based virtual knot is a based Gauss diagram, considered up to Reidemeister moves that do not involve segments with the basepoint on them.
- **Definition.** A knot invariant with values in a set $S$ is a map from $\mathcal{K}$ to $S$.
- **Definition.** The crossing number $c(K)$ of a knot $K$ is the minimal number of crossing points in a plane diagram of $K$.
- **Definition.** The unknotting number $u(K)$ of a knot $K$ is the minimal number of crossing changes in a plane diagram of $K$ that convert it to a trivial knot, provided that any number of plane isotopies and Reidemeister moves is also allowed.
- **Definition.** The self-linking number of $K$ is the linking number of $K$ and $K'$.
- **2.3.1. Definition.** The Conway polynomial $C$ is an invariant of oriented links (and, in particular, an invariant of oriented knots) taking values in the ring $Z[t]$ and defined by the two properties:
- **Definition.** Let $f$ be a map of a one-dimensional manifold to $R^3$. A point $p \in \operatorname{im}(f) \subset R^3$ is a double point of $f$ if $f^{-1}(p)$ consists of two points $t_1$ and $t_2$ and the two tangent vectors $f'(t_1)$ and $f'(t_2)$ are linearly independent.
- **3.1.3. Definition. (V. Vassiliev [Va1]).** A knot invariant is said to be a Vassiliev invariant (or a finite type invariant) of order (or degree) $\leqslant n$ if its extension vanishes on all singular knots with more than $n$ double points. A Vassiliev invariant is said to be of order (degree) $n$ if it is of order $\leqslant n$ but not of order $\leqslant n - 1$.
- **Definition.** Let $R$ be a commutative ring. A Vassiliev invariant of order $\leqslant n$ is a linear function $ZK \to R$ which vanishes on $K_{n+1}$.
- **Definition.** Two knots $K_1$ and $K_2$ are $n$-equivalent if they cannot be distinguished by Vassiliev invariants of degree $n$ and smaller with values in an arbitrary abelian group. A knot that is $n$-equivalent to the trivial knot is called $n$-trivial.
- **Definition.** Let $\Gamma_n \mathcal{K}$ be the set of $(n - 1)$-trivial knots. The Goussarov filtration on $\mathcal{K}$ is the descending filtration $\mathcal{K} = \Gamma_1 \mathcal{K} \supseteq \Gamma_2 \mathcal{K} \supseteq \dots \supseteq \Gamma_n \mathcal{K} \supseteq \dots$
- **Definition.** A chord diagram of order $n$ (or degree $n$) is an oriented circle with a distinguished set of $n$ disjoint pairs of distinct points, considered up to orientation preserving diffeomorphisms of the circle.
- **Definition.** The chord diagram $\sigma(K) \in A_n$ of a singular knot with $n$ double points is obtained by marking on the parametrizing circle $n$ pairs of points whose images are the $n$ double points of the knot.
- **4.1.1. Definition.** A function $f \in RA_n$ is said to satisfy the 4-term (or 4T) relations if the alternating sum of the values of $f$ is zero on the following quadruples of diagrams:
- **4.1.3. Definition.** An isolated chord is a chord that does not intersect any other chord of the diagram. A function $f \in RA_n$ is said to satisfy the 1-term relations if it vanishes on every chord diagram with an isolated chord. An unframed weight system of order $n$ is a weight system that satisfies the 1-term relations.
- **4.4.2. Definition.** The space $A^{fr}_n$ of chord diagrams of order $n$ is the vector space generated by the set $A_n$ (all diagrams of order $n$) modulo the subspace spanned by all 4-term linear combinations
- **Definition.** The product of two chord diagrams $D_1$ and $D_2$ is defined by cutting and glueing the two circles as shown:

## Lemmas, Theorems, Propositions, Corollaries
- **1.3.1. Theorem (Reidemeister [Rei], proofs can be found in [PS, BZ, Mur2]).** Two unoriented knots $K_1$ and $K_2$, are equivalent if and only if a diagram of $K_1$ can be transformed into a diagram of $K_2$ by a sequence of ambient isotopies of the plane and local moves of the following three types:
  *Proof:* (no proof in this paper)
- **Theorem (Markov [Mark, Bir1]).** Two closed braids are equivalent (as links) if and only if the braids are related by a finite sequence of the following Markov moves:
  *Proof:* (no proof in this paper)
- **Theorem ([Tur3]).** Two products of simple tangles are isotopic if and only if they are related by a finite sequence of the following Turaev moves.
  *Proof:* (no proof in this paper)
- **1.8.2. Theorem (framed Reidemeister theorem).** Two knot diagrams with blackboard framing $D_1$ and $D_2$ are equivalent if and only if $D_1$ can be transformed into $D_2$ by a sequence of plane isotopies and local moves of three types $F \Omega_1, \Omega_2,$ and $\Omega_3$, where
  *Proof:* (no proof in this paper)
- **2.2.1. Proposition.**
                             X               X               1X
                lk(A, B) =          w(p) =          w(p) =      w(p)
                                                             2
                                A
                             p∈IB               B
                                             p∈IA             p∈I

where w(p) = ±1 is the local writhe of the crossing point.
  *Proof:* Resolves all inter-component crossings to untangle the links, showing each switch synchronously alters the linking number and writhe sum.
- **Theorem.** Let $A$ and $B$ be two non-intersecting curves in $R^3$, parameterized, respectively, by the smooth functions $\alpha, \beta : S^1 \to R^3$. Then $lk(A, B) = \frac{1}{4\pi} \int_{S^1 \times S^1} \frac{(\beta(v) - \alpha(u), d\alpha, d\beta)}{|\beta(v) - \alpha(u)|^3}$, where the parentheses in the numerator stand for the mixed product of 3 vectors.
  *Proof:* (no proof in this paper)
- **Proposition.** The self-linking number of a framed knot given by a diagram $D$ with blackboard framing is equal to the total writhe of the diagram $D$.
  *Proof:* Notes that a blackboard framing shift creates intersections exclusively near the knot's original crossings, preserving their local writhe.
- **Theorem.** The product of two Vassiliev invariants of degrees $\leqslant p$ and $\leqslant q$ is a Vassiliev invariant of degree $\leqslant p + q$.
  *Proof:* Applies the Vassiliev skein relation on a knot with $p+q+1$ double points to formulate the product as an alternating sum over a binary cube.
- **Lemma.** Let $f, g$ be functions on $Q_n$, where $n = p+q+1$. If the alternating sums of $f$ over any $(p + 1)$-face, and of $g$ over any $(q + 1)$-face of $Q_n$ are zero, so is the alternating sum of the product $fg$ over the entire cube $Q_n$.
  *Proof:* Uses induction on $n$ with a discrete boundary operator that operates on cube faces and satisfies a Leibniz rule.
- **3.3.1. Proposition.** $V_0 = \{const\}, \dim V_0 = 1$.
  *Proof:* Transforming any knot into the unknot via crossing changes accumulates zero jump for a degree 0 invariant, rendering it constant.
- **3.3.2. Proposition.** $V_1 = V_0$.
  *Proof:* Smoothing a knot's single double point yields two independent closed curves, evaluating to zero for order 1 invariants.
- **3.3.3. Proposition.** $\dim V_2 = 2$.
  *Proof:* Identifies two basic singular knots with two double points (cyclic orders 1122 and 1212) that any knot reduces to. Evaluates the Casson invariant to show the second dimension is strictly realized.
- **3.4.2. Proposition. (V. Vassiliev [Va1]).** The value of a Vassiliev invariant $v$ of order $\leqslant n$ on a knot $K$ with $n$ double points depends only on the chord diagram of $K$: $\sigma(K_1) = \sigma(K_2) \implies v(K_1) = v(K_2)$.
  *Proof:* Deforms one knot into the other while fixing double point neighborhoods; any new crossings introduced appear at different parameter values and vanish under the degree bound.
- **3.4.3. Corollary.** The module of $R$-valued Vassiliev invariants of degree at most $n$ is finitely generated over $R$.
  *Proof:* (immediate from 3.4.2. Proposition.)
- **Theorem ([G1, BL, BN1]).** The coefficient $j_n(K)$ is a Vassiliev invariant of order $\leqslant n$.
  *Proof:* Substitutes $t = e^h$ into the Jones polynomial skein relation to show crossing changes differ by $O(h)$, hence $k$ double points yield $O(h^k)$.
- **Theorem ([BL, BN1]).** The coefficient $\theta_n(K)$ is a Vassiliev invariant of order $\leqslant n$.
  *Proof:* Uses the fact that an R-matrix and its inverse are congruent modulo $h$, mirroring the approach for the Jones polynomial.
- **Theorem.** The Casson invariant coincides with the second coefficient of the Conway polynomial $c_2$.
  *Proof:* Verifies the Gauss diagram formula is invariant under basepoint relocation and Reidemeister moves. Tests it on the trefoil to confirm it spans the dimension of $V_2$.
- **Lemma.** The linking number of two components of a tangle is a Vassiliev invariant of order 1.
  *Proof:* Applies the skein relation to show single-component double points vanish and inter-component ones yield 1, so two double points guarantee evaluation to zero.
- **4.2.1. Theorem (Vassiliev–Kontsevich).** For $R = C$ the map $\alpha_n$ identifies $V_n / V_{n-1}$ with the subspace of unframed weight systems $W_n \subset RA_n$. In other words, the space of unframed weight systems is isomorphic to the graded space associated with the filtered space of Vassiliev invariants,
  *Proof:* Proves the forward direction showing the symbol of every Vassiliev invariant is an unframed weight system satisfying 1T and 4T relations; defers the converse to Section 8.8.1.
- **Lemma (4-term relation for knots).** Any Vassiliev invariant satisfies
  *Proof:* Resolves the four singular knots via the skein relation and observes the resulting eight configurations cancel out exactly.
- **4.3.2. Theorem.** The bialgebra of knots $FK$ considered with the singular knot filtration is a bialgebra with a decreasing filtration (see Section A.2.3).
  *Proof:* Proves the multiplicative condition using prior results and the comultiplicative property by calculating commutators of the coproduct and crossing change operators.
- **4.3.3. Lemma.** $\delta \circ \sigma_i = (\sigma_i \otimes id + s_i \otimes \sigma_i ) \circ \delta$, where both the left-hand side and the right-hand side are understood as linear operators from $XK$ into $XK \otimes XK$.
  *Proof:* Directly verifies the operator equality on an arbitrary element of the set of knots differing by crossing changes.
- **4.3.6. Proposition.** The algebra of $F$-valued Vassiliev knot invariants $V F$ is a bialgebra with an increasing filtration (page 475).
  *Proof:* Follows directly by duality from the filtered bialgebra structure established on the algebra of knots.
- **Lemma.** The product is well-defined modulo 4T relations.
  *Proof:* Demonstrates that rotating the attachment point of the second diagram around the first diagram by one chord translates into a combination of 4T relations, yielding equivalence upon a full revolution.