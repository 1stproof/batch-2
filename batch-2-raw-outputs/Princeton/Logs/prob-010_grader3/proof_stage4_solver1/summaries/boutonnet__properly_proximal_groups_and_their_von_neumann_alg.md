<!-- Generated 2026-05-31T02:30:11 -->
<!-- Source PDF: boutonnet__properly_proximal_groups_and_their_von_neumann_alg.pdf (411215 bytes) -->
<!-- Citation: R. Boutonnet, A. Ioana, J. Peterson (2021). Properly proximal groups and their von Neumann algebras. Annales Scientifiques de l'École Normale Supérieure. -->

# Properly proximal groups and their von Neumann algebras

## Definitions
- **Definition 2.2.** [OP10a] A trace preserving action σ : Γ y (Q, τ ) on a tracial von Neumann algebra (Q, τ ) is weakly compact if there exists a state ϕ on B(L2 (Q)) such that ϕ|Q = τ and ϕ ◦ Ad(u) = ϕ, for every u ∈ U (Q) ∪ σ(Γ). A regular inclusion of tracial von Neumann algebras Q ⊂ M is weakly compact if the action NM (Q) y Q is weakly compact, where NM (Q) = {u ∈ U (M ) | uQu∗ = Q} denotes the normalizer of Q in M .
- **Definition 2.3.** Consider a tracial von Neumann algebra M with two von Neumann subalgebras P, Q ⊂ M . We say that a corner of P embeds into Q inside M , and write P ≺M Q if one of the following equivalent statements holds.
  (i) There exists projections p ∈ P , q ∈ Q, a ∗-homomorphism ϕ : pP p → qQq and a non-zero element v ∈ qM p such that ϕ(x)v = vx for all x ∈ pP p;
 (ii) There exists no net of unitaries (un ) ⊂ U (P ) such that limn kEQ (xun y)k2 = 0 for all x, y ∈ M ;
- **Definition 3.1.** Given a discrete group Γ, a boundary piece is a closed subset X ⊂ ∂Γ which is invariant under the left and right Γ-actions.
- **Definition 3.4.** Fix a discrete group Γ, a closed set X ⊂ ∂Γ and a bounded net of vectors ξn ∈ ℓ2 (Γ). We say that (ξn )n has
     • positive mass on X if there exists ε > 0 such that for any neighborhood U of X inside ∆Γ, we have kPU (ξn )k > ε for all n large enough;
     • full mass on X if for any neighborhood U of X inside ∆Γ, we have
                                  lim sup kξn − PU (ξn )k = 0.
                                     n
- **Definition 3.5.** In the above setting, an operator T ∈ B(ℓ2 Γ) is said to be compact towards X if for any bounded net of vectors ξn ∈ ℓ2 Γ with full mass on X, we have limn kT ξn k = 0. We denote by K(Γ; X) the set of all operators that are compact towards X, and note that it is a hereditary C*-subalgebra of B(ℓ2 Γ).
- **Definition 3.7.** A point ω ∈ ∆Γ (i.e. an ultrafilter on Γ) is called an η-proximal element if for all h ∈ Γ, we have limg→ω ((gh) · η − g · η) = 0, in the weak-* topology. We denote by ∂η Γ ⊂ ∆Γ the set of η-proximal elements.
- **Definition 3.12.** A two-sided array of Γ into π is a map b : Γ → H such that
                         sup kb(sgt) − πs (b(g))k < ∞, for all s, t ∈ Γ.
                         g∈Γ
- **Definition 4.1.** We say that a discrete group Γ is a properly proximal group if it admits a finite family of continuous actions on compact spaces Γ y Ki , i ≥ 0, and probability measures ηi ∈ Prob(Ki ), i ≥ 0, such that:
     • For all i, there is no Γ-invariant Borel probability measure on Ki ;
     • ∪i ∂ηi Γ = ∂Γ.
- **Definition 5.1.** [AD87] A continuous action Γ y K on a compact space is said to be amenable if there exists a net of continuous maps Pn : K → Prob(Γ) such that
                      lim sup kPn (gx) − g · Pn (x)k1 = 0, for all g ∈ Γ.
                       n x∈K
- **Definition 5.2.** Given a group Γ and a boundary piece X ⊂ ∂Γ, we say that Γ is bi-exact towards X if the left Γ-action on the Gelfand spectrum of C(X)Γr is amenable.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1.** For any d ≥ 2, the von Neumann algebra of Γ := SLd (Z) does not admit a weakly compact Cartan subalgebra. Moreover, for any free ergodic p.m.p. action σ : Γ y (X, µ), the crossed product L∞ (X, µ) ⋊ Γ admits a weakly compact Cartan subalgebra A if and only if σ is weakly compact and, in this case, A is unitary conjugate with L∞ (X, µ).
  *Proof:* (no proof in this paper)
- **Corollary 1.2.** Let σ : SLd (Z) y (X, µ) and σ ′ : SLd′ (Z) y (X ′ , µ′ ) be free ergodic profinite p.m.p. actions, for some d, d′ ≥ 3. If L∞ (X) ⋊ SLd (Z) is isomorphic to L∞ (X ′ ) ⋊ SLd′ (Z), then d = d′ and the actions σ and σ ′ are virtually conjugate.
  *Proof:* (no proof in this paper)
- **Theorem 1.4.** Any properly proximal group Γ satisfies the conclusions of Theorem 1.1.
  *Proof:* (immediate from Theorem 4.16)
- **Theorem 1.5.** Let Γ be a properly proximal, weakly amenable group. Then LΓ has no Cartan subalgebra and Γ is C-rigid.
  *Proof:* (immediate from Theorem 4.17)
- **Proposition 1.6.** Groups in the following classes are properly proximal:
     • Non-amenable bi-exact groups;
     • Non-elementary convergence groups;
     • Lattices in non-compact semi-simple Lie groups of arbitrary rank;
     • Groups admitting a proper cocycle into a non-amenable representation.
Moreover, the class of properly proximal groups is stable under commensurability up to finite kernels and under direct products. In contrast, properly proximal groups are never inner amenable, and therefore no infinite direct product of non-trivial groups is properly proximal.
  *Proof:* (no proof in this paper)
- **Lemma 2.1.** A compact Hausdorff space carries a diffuse Borel probability measure if and only if it contains a perfect set.
  *Proof:* Constructs a continuous surjection to the Cantor space via a nested family of perfect subsets and pulls back a diffuse measure.
- **Lemma 2.4.** Consider a tracial von Neumann algebra M with two von Neumann subalgebras P, Q ⊂ M . Then P ≺M Q if and only if there exists a P -central state Φ : hM, eQ i → C which is normal on M and does not vanish on M eQ M .
  *Proof:* (no proof in this paper)
- **Lemma 3.6.** Any approximate unit (ei )i∈I of I0 (X) is an approximate unit for I(X). In particular,
                            I(X) = AΓ ∩ K(Γ; X).
  *Proof:* Verifies the ideal structures and checks compactness towards the boundary piece using approximate units of the ideal of vanishing functions.
- **Lemma 3.8.** The set ∂η Γ enjoys the following properties.
   (1) It is a closed subset of ∆Γ.
   (2) It is left and right Γ-invariant.
   (3) If η is Γ-invariant, then ∂η Γ = ∆Γ. Otherwise, ∂η Γ ⊂ ∂Γ.
  *Proof:* Analyzes the continuous extension of the orbit map to the Stone-Čech compactification.
- **Lemma 3.9.** Assume that the measure η is not Γ-invariant, so that X := ∂η Γ is indeed a boundary piece. Denote by λ and ρ the left and right actions of Γ on C(X), respectively. Then there exists a unital completely positive map θ : C(K) → C(X) such that for all g ∈ Γ, f ∈ C(K), we have
                           θ(g.f ) = λg (θ(f )) and ρg (θ(f )) = θ(f ).
  *Proof:* Constructs a unital completely positive map by integrating functions against translated measures and checks equivariance properties.
- **Lemma 3.10.** Assume that η is not Γ invariant and write X := ∂η Γ. Denote by C(X)Γr the C*-algebra of right-Γ-invariant continuous functions on X. We have the following two facts:
     • If there is no Γ-invariant probability measure on K, then there is no left-Γ-invariant state on C(X)Γr ,
     • If the action Γ y K is topologically amenable, then the left Γ- action Γ y C(X)Γr is amenable. We refer to [BO08, Section 4.3] for the definition of amenable actions.
  *Proof:* Pushes invariant states and amenability properties from the compact space to the boundary using the ucp map from Lemma 3.9.
- **Lemma 3.11.** For every boundary piece X ⊂ ∂Γ there exists a continuous action of Γ on a compact space K, with a probability measure η ∈ Prob(K) such that X = ∂η Γ. Moreover the action Γ y K may be chosen so that:
     • If there is no left Γ-invariant state on C(X)Γr then there is no Γ-invariant probability measure on K;
     • If the action Γ y C(X)Γr is amenable then Γ y K is topologically amenable.
  *Proof:* Constructs a compact space by dualizing embeddings of C*-algebras and verifies properties using exactness and nuclearity.
- **Lemma 3.13.** If b : Γ → H is an unbounded array then X := {ω ∈ ∆Γ | limg→ω kb(g)k = +∞} is a non-empty boundary piece. Moreover there exists a unital completely positive map θ : B(H) → C(X) such that
                          θ ◦ Ad(π(g)) = λg ◦ θ and ρg ◦ θ = θ, for all g ∈ Γ.
  *Proof:* Defines an equivariant completely positive map using matrix coefficients normalized by the unbounded proper array.
- **Lemma 3.14.** Let π : Γ → U (H) be a representation. Let U be a neighborhood of X(π). Then there exists a weak operator topology neighborhood O of 0 ∈ B(H) such that π −1 (O) ⊂ U.
  *Proof:* Uses a direct compactness argument on the complement of the neighborhood in the Stone-Čech boundary.
- **Lemma 3.15.** Let π : Γ → U (H) be a representation. Let (cn ) be a uniformly bounded net in LΓ. The following conditions are equivalent:
  (i) (cn ) has full mass on X(π).
 (ii) For all other representation (ρ, K), all ξ, η ∈ H ⊗ K ⊗ ℓ2 (Γ) and all uniformly bounded net (dn ) ⊂ LΓ we have limn→∞ hcn ξdn , ηi = 0.
(iii) limn→∞ hcn (ξ ⊗ δe )c∗n , η ⊗ δe i = 0 for all ξ, η ∈ H ⊗ H.
(iv) limn→∞ hcn (ξ ⊗ δe )c∗n , η ⊗ δe i = 0 for all vectors ξ, η ∈ H ⊗ H of the form ξ = ξ0 ⊗ ξ0 , η = η0 ⊗ η0 , with ξ0 , η0 ∈ H.
  *Proof:* Derives the equivalences using basic algebraic manipulations of inner products and the Fourier expansion of the unitaries.
- **Proposition 3.16 (Weak mixing/compact dichotomy).** Let B ⊂ LΓ be a von Neumann subalgebra, and G ⊂ U (B) a group which generates B as a von Neumann algebra. The following are equivalent:
  (i) Some net of unitaries (un ) ⊂ G has full mass on X(π).
 (ii) The LΓ-bimodule H ⊗ H ⊗ ℓ2 Γ has no non-zero B-central vectors.
  *Proof:* Applies Lemma 3.15 to extract a non-zero central vector from the convex closure of conjugated unitaries.
- **Theorem 4.3.** Consider a discrete countable group Γ, and let X ⊂ ∂Γ be a boundary piece. The following facts are equivalent.
  (i) There are continuous actions Γ y Ki , i = 1, . . . , k on compact spaces Ki with probability measures ηi ∈ Prob(Ki ) such that there is no Γ-invariant probability measure on any Ki and such that X ⊂ ∪ki=1 ∂ηi Γ.
 (ii) There is a single continuous action Γ y K on a compact space K with a probability measure η ∈ Prob(K) such that there is no Γ-invariant probability measure on K and X = ∂η Γ.
(iii) There is no left-Γ-invariant state on C(X)Γr ;
(iv) There is no left-Γ-invariant state on (C(X)∗∗ )Γr .
  *Proof:* Establishes equivalences through Hahn-Banach separation, Goldstine's theorem, and careful construction of right-invariant functions in the quotient C*-algebra. Key steps involve lifting elements to bounded functions and using quasi-central approximate units.
- **Lemma 4.4.** If X is a Banach space and (xi ) is a net of elements in X which converges *-weakly to an element x ∈ X ∗∗ , then we have inf{kyk | y ∈ conv({xi })} ≤ kxk.
  *Proof:* Proceeds by contradiction using the Hahn-Banach separation theorem and Goldstine's theorem.
- **Lemma 4.5.** Let A be a unital C ∗ -algebra with a closed ideal I ⊂ A. Suppose Γ is a countable group which acts on A by ∗-automorphisms which preserve I. If I0 ⊂ I is a countable set, then there exists an increasing sequence αn ∈ I, with 0 ≤ αn ≤ 1, such that k(1 − αn )ak → 0 for all a ∈ I0 , and such that kαn − g · αn k → 0 for all g ∈ Γ.
  *Proof:* Extracts a quasi-central sequence using an approximate unit for the ideal crossed product.
- **Proposition 4.7.** If Γ admits a proper two-sided array into a non-amenable representation then it is properly proximal.
  *Proof:* Uses Lemma 3.13 to produce an equivariant ucp map and shows amenability fails, establishing proper proximality.
- **Proposition 4.10.** We have the following stability properties.
     (1) A direct product of finitely many properly proximal groups is again properly proximal;
     (2) A co-amenable subgroup (e.g. a finite index subgroup) of a properly proximal group is properly proximal.
     (3) The class of properly proximal groups is stable under commensurability up to finite kernels.
  *Proof:* Verifies stability by tracking boundaries of product groups, restricting invariant states for co-amenable subgroups, and averaging over finite quotients.
- **Proposition 4.11.** Properly proximal groups are not inner amenable.
  *Proof:* Observes that an inner amenable group yields a left-invariant state on the boundary, contradicting proper proximality.
- **Lemma 4.12.** Take a subgroup Γ < G and denote by π : ∆Γ → ∆G the continuous map extending the embedding. Assume that G acts continuously on a compact space K and consider also the restricted Γ action on K. Then for any η ∈ Prob(K), we have ∂η Γ ⊃ π −1 (∂η G). In the case where Γ is discrete inside G, then π is an embedding and the formula can be read as ∂η Γ ⊃ ∂η G ∩ ∆Γ.
  *Proof:* Explicitly constructs a continuous function lifting the bounded continuous functions on the larger group to the discrete subgroup.
- **Lemma 4.13.** Consider an almost k-simple, connected, simply connected algebraic group G over a local field k. Then there are finitely many proper parabolic k-subgroups Pi < G and measures ηi ∈ Prob(G(k)/Pi (k)) such that ∂G = ∪i ∂ηi G.
  *Proof:* Uses the Cartan decomposition of simple groups over local fields to analyze the action of the split torus. Proves three claims about the convergence of translates of unipotent radicals to deduce proximality in the boundary.
- **Proposition 4.14.** Consider finitely many local fields ki , and semi-simple connected ki -groups Gi . Set Gi := Gi (ki ) for each i and take a discrete subgroup Γ in G := Πi Gi whose projection on each Gi is Zariski dense. Then Γ is properly proximal. In particular, lattices in semi-simple algebraic groups over local fields are properly proximal.
  *Proof:* Reduces the problem to simply connected, almost simple groups with non-compact closure, then applies Furstenberg's Lemma and Lemma 4.13.
- **Corollary 4.15.** A finitely generated subgroup Γ < GLd (Q) with trivial solvable radical is properly proximal.
  *Proof:* Takes the Zariski closure and diagonal embedding into products of local fields, then applies Proposition 4.14.
- **Theorem 4.16.** Assume that Γ is a properly proximal group. Consider a trace preserving action σ : Γ y (Q, τ ) on a tracial von Neumann algebra. Denote M := Q ⋊ Γ Then any weakly compact von Neumann subalgebra P ⊂ M such that NM (P )′′ contains LΓ admits a corner that embeds into Q inside M .
  *Proof:* Assumes no corner embeds and uses the weakly compact state to build a central functional which induces a left-invariant state on the boundary, contradicting proper proximality.
- **Theorem 4.17.** Assume that Γ is properly proximal and weakly amenable. Consider a trace preserving action Γ y (Q, τ ) on a tracial von Neumann algebra. Denote M := Q ⋊ Γ. Then for any amenable von Neumann subalgebra P ⊂ M such that NM (P )′′ contains LΓ we have that P ≺M Q. In particular, Γ is Cartan-rigid.
  *Proof:* Applies Popa's intertwining-by-bimodules and Proposition 4.18 to the dual co-action.
- **Proposition 4.18.** Consider a group Γ which is both properly proximal and weakly amenable. Consider also any tracial von Neumann algebra B and set M := B ⊗ LΓ. Let A ⊂ M be an amenable von Neumann subalgebra and assume that for any g ∈ Γ, there exists a unitary wg ∈ U (B) such that wg ⊗ ug belongs to NM (A)′′ . Then A ≺M B.
  *Proof:* Uses Popa and Vaes' structure theorem to construct states witnessing amenability, extracting a left-invariant boundary state to contradict proper proximality if intertwining fails.
- **Theorem 5.4.** Take a countable group Γ with a non-empty boundary piece X ⊂ ∂Γ. The following assertions are equivalent.
  (i) Γ is bi-exact towards X;
 (ii) There exists an amenable action Γ y K and η ∈ Prob(K) such that X ⊂ ∂η Γ;
(iii) Γ is exact and there exists a map µ : Γ → Prob(Γ) such that
                    lim kµ(sgt) − s · µ(g)k1 = 0, for all s, t ∈ Γ, ω ∈ X.
                    g→ω
  *Proof:* Constructs locally approximately invariant probability measures from an amenable action on a compact space and uses exactness.
- **Lemma 5.5.** Consider an exact group Γ and a boundary piece X ⊂ ∂Γ. Then Γ is bi-exact towards X if and only if there exists a u.c.p. map
                                     θ : Cλ∗ (Γ) ⊗min Cρ∗ (Γ) → B(ℓ2 Γ)
such that θ(x ⊗ y) − xy ∈ K(Γ; X) (see Definition 3.5) for all x ∈ Cλ∗ (Γ), y ∈ Cρ∗ (Γ).
  *Proof:* (no proof in this paper)
- **Theorem 5.6.** Consider a group Γ with a boundary piece X ⊂ ∂Γ. Assume that Γ is bi-exact towards X. For any net of unitaries (un ) ⊂ U (LΓ) with positive mass on X (viewed as a net in ℓ2 Γ), the relative commutant (un )′ ∩ LΓ has an amenable direct summand.
  *Proof:* Extends a state on the relative commutant to the minimal tensor product using bi-exactness, approximating it by vector states to yield an amenable direct summand.
- **Proposition 5.7.** Consider a discrete group Γ and a boundary piece X ⊂ ∂Γ. The following are equivalent.
  (i) There exists a map µ : Γ → Prob(Γ) as in Theorem 5.4.(iii) ;
 (ii) There exists a two-sided array into the regular representation b : Γ → ℓ2 (Γ) which is proper towards X, meaning that the corresponding boundary piece introduced in Lemma 3.13 contains X;
(iii) There exists a unitary representation ρ : Γ → U (K), weakly contained in the regular representation of Γ, and an array q : Γ → K which is proper towards X.
  *Proof:* (no proof in this paper)
- **Proposition 5.8.** Consider a discrete group Γ and finitely many boundary pieces Xi ⊂ ∂Γ, i = 1, . . . , n. Assume that for each i, Γ is bi-exact towards Xi . Then Γ is bi-exact towards ∪i Xi .
  *Proof:* Takes the direct sum of the proper arrays associated to each individual boundary piece.
- **Corollary 5.9 (Ozawa).** The group Γ := Z2 ⋊ SL2 (Z) is bi-exact.
  *Proof:* Decomposes the boundary into two pieces using natural actions on the projective line and flag variety, applying Proposition 5.8.
- **Lemma 6.1.** Fix a tuple k̄ = (k1 , . . . , kl ). Then for any neighborhood U ⊂ ∆Γ of Xk̄ , there exists C > 0 such that
                                       skj (g)
                         {g ∈ Γ |                ≥ C for all j} ⊂ U.
                                     skj+1 (g)
  *Proof:* Proceeds by contradiction by extracting convergent subsequences of the Cartan components and evaluating the pushforward measure on flag varieties.
- **Corollary 6.2.** For all ω ∈ ∂Γ and 1 ≤ i ≤ n, if limg→ω si (g)/si+1 (g) = +∞, then ω ∈ Xi . So the sets Xi cover the Stone-Cěch boundary: ∂Γ = ∪d−1 i=1 Xi .
  *Proof:* Follows from Lemma 6.1 and the fact that ratios of singular values of determinant-1 matrices must diverge.
- **Proposition 6.3.** SL3 (Z) is bi-exact towards X0 .
  *Proof:* Observes that the parabolic subgroup is amenable, making the boundary action amenable, and applies Theorem 5.4.
- **Corollary 6.4.** Denote by Λ either the top-left copy of SL2 (Z) or the copy of Z2 inside Γ := SL3 (Z):
                                                           
                     ∗ ∗ 0                            1 0 ∗
               Λ = ∗ ∗ 0 ≃ SL2 (Z) or Λ = 0 1 ∗ ≃ Z2 .
                     0 0 1                            0 0 1
Then for any diffuse subalgebra A of LΛ the relative commutant A′ ∩ LΓ is amenable.
  *Proof:* Applies Theorem 5.6 by checking that sequences going to infinity in the subgroup diverge in both singular value ratios.
- **Proposition 6.6.** For all d ≥ 3, consider inside Γd := PSLd (Z) the following subgroup Λd isomorphic to Zd−1 :
                                                        
                                  I      u
                      Λd := ± d−1            , u ∈ Zd−1 ≃ Zd−1
                                    0    1
Then L(Λd ) is a maximal abelian subalgebra inside L(Γd ) and the inclusion L(Λ3 ) ⊂ L(Γ3 ) is not isomorphic with the inclusion L(Λd ) ⊂ L(Γd ) for any d ≥ 4.
  *Proof:* Uses the relative ICC condition from Lemma 6.7 and observes that the centralizer structure differs for d >= 4.
- **Lemma 6.7.** Fix d ≥ 3 and denote by Γ := GLd (Z) and by Λ ≃ Zd−1 the subgroup
                                                   
                             Id−1 u           d−1
                      Λ=                ,u∈Z        ≃ Zd−1 .
                               0    1
Then for all g ∈ Γ such that {sgs−1 , s ∈ Λ} is finite we have either g ∈ Λ, or −g ∈ Λ.
  *Proof:* Explicitly computes conjugates of group elements to show that non-diagonal entries are unbounded unless the matrix is in the subgroup.