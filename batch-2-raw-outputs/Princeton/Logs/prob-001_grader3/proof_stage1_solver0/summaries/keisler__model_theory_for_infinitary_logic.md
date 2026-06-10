<!-- Generated 2026-05-31T02:09:27 -->
<!-- Source PDF: keisler__model_theory_for_infinitary_logic.pdf (328670 bytes) -->
<!-- Citation: Keisler, H. J. (1971). Model Theory for Infinitary Logic. North-Holland. -->

# Barwise: Infinitary Logic and Admissible Sets (Keisler, H. J. (1971). Model Theory for Infinitary Logic. North-Holland.)

## Definitions

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1.1 (Morley, Lopez-Escobar).** If σ is an Lω1 ω sentence true in all countable well orderings, then σ has a model with a subset of order type η—the order type of the rationals.
  *Proof:* (no proof in this paper)

- **Theorem 1.2.1 (Karp’s Theorem).** Two structures are potentially isomorphic if and only if they satisfy the same sentences of L∞ω .
  *Proof:* Structural induction on formula complexity handles the forward direction, while constructing a back-and-forth family from tuples satisfying identical formulas proves the reverse.

- **Corollary 1.2.2.** Two countable structures for a countable vocabulary L are isomorphic if and only if they satisfy the same sentences of Lω1 ω .
  *Proof:* (no proof in this paper)

- **Theorem 1.3.1 (Scott Isomorphism Theorem).** Suppose the vocabulary L is countable. Then for any countable L-structure M, there is an Lω1 ω sentence θ such that the countable models of θ are just the isomorphic copies of M.
  *Proof:* Combines the distinguishability formulas for each tuple from the Scott family into a single canonical sentence quantifying over all tuples.

- **Lemma 1.3.2 (Scott).** Let L be a countable vocabulary. Then each countable structure M has a countable Scott family of formulas in Lω1 ω .
  *Proof:* Selects formulas distinguishing each tuple in M from any other non-orbit tuple, forming a countable set that defines orbits by Karp's theorem.

- **Lemma 1.3.3.** For any structures M and N , any tuples a in M and b in N , of the same length, and any ordinal α, the following are equivalent.
   (a) (M, a) ≡α (N , b).
   (b) N |= σαM,a (b).
   (c) σαM,a (v) = σαN ,b (v).
  *Proof:* (no proof in this paper)

- **Lemma 1.3.4.** 1. For each M there is a least ordinal α, called the Scott height of M, such
       that for all partial automorphisms (a, b) of M, (M, a) ≡α (M, b) implies
       (M, a) ≡α+1 (M, b).
    2. If α is the Scott height of M and (M, a) ≡α (M, b), then (M, a) is poten-
       tially isomorphic to (M, b).
  *Proof:* (no proof in this paper)

- **Theorem 1.3.5.** N is a model of the canonical Scott sentence of M if and only if N is potentially isomorphic to M.
  *Proof:* (no proof in this paper)

- **Corollary 1.3.6.** If L is a countable vocabulary, and M is a countable L-structure, then the canonical Scott sentence of M is a Scott sentence for M in the sense of the Scott Isomorphism Theorem.
  *Proof:* (no proof in this paper)

- **Theorem 1.4.1 (ω-Completeness).** Let L be an ω-vocabulary.
    1. An L-sentence is true in all ω-models if and only if it is provable using the
       ω-rule.
    2. A set T of L-sentences has an ω-model if and only if there is no proof of a
       contradiction from T , using the ω-rule.
  *Proof:* (no proof in this paper)

- **Theorem 1.5.1 (Completeness).** For an Lω1 ω sentence ϕ, |= ϕ if and only if ` ϕ.
  *Proof:* (no proof in this paper)

- **Theorem 1.5.2 (Model Existence).** 1. Let ϕ be an Lω1 ω sentence. Then ϕ has a model if and only if there is a
       consistency property S with an element Φ containing ϕ.
    2. Let T be a countable set of Lω1 ω sentences. Then T has a model if and only
       if there is a consistency property S such that for all ϕ ∈ T and all Φ ∈ S,
       Φ ∪ {ϕ} ∈ S.
  *Proof:* (no proof in this paper)

- **Theorem 1.5.3 (Interpolation).** Let L1 and L2 be vocabularies with L = L1 ∩ L2 . Let ϕ ∈ L1ω1 ω and ψ ∈ L2ω1 ω be sentences such that |= ϕ → ψ. Then there is a sentence θ ∈ Lω1 ω such that |= ϕ → θ and |= θ → ψ.
  *Proof:* (no proof in this paper)

- **Theorem 1.5.4 (Downward Löwenheim-Skolem-Tarski Theorem).** Suppose ℵ0 ≤ µ ≤ κ. If a sentence ϕ of Lω1 ω has a model M of cardinality κ, then it has a model N of cardinality µ.
  *Proof:* (no proof in this paper)

- **Corollary 1.5.5.** (a) If two sentences of Lω1 ω have the same finite and countable models, then they are logically equivalent.
  (b) Let L be a countable vocabulary and M be a countable structure. Then any two Scott sentences of M are logically equivalent.
  *Proof:* (no proof in this paper)

- **Theorem 1.6.1 (Hanf).** For a language with a set S of sentences, there is a cardinal κ such that for all ϕ ∈ S, if ϕ has a model of cardinality ≥ κ, then it has models of arbitrarily large cardinality.
  *Proof:* Chooses the least cardinal strictly greater than the sizes of all models for sentences lacking arbitrarily large models.

- **Theorem 1.6.2 (Morley).** The Hanf number for Lω1 ω is iω1 .
  *Proof:* (no proof in this paper)

- **Theorem 1.6.3 (Morley).** The Hanf number for ω-logic is iω1CK .
  *Proof:* (no proof in this paper)

- **Proposition 2.1.1.** For every elementary first order theory T , every Σ formula is persistent with respect to T .
  *Proof:* (no proof in this paper)

- **Corollary 2.1.2.** (a) Every formula that is ∆ over a theory T is absolute with respect to T .
  (b) Every ∆0 formula is absolute with respect to every theory T .
  *Proof:* (no proof in this paper)

- **Proposition 2.2.1 (∆-separation).** If A is an admissible set, S is A-finite, and X ⊆ S is A-computable, then X is A-finite.
  *Proof:* Applies Σ-reflection and ∆0-collection to define the subset via a ∆0 formula, then invokes ∆0-separation.

- **Theorem 2.4.2 (Kleene).** For S ⊆ ω, S is Π11 if and only if there is a uniformly computable sequence of trees (Tn )n∈ω such that S = {n : Tn has no path}.
  *Proof:* (no proof in this paper)

- **Corollary 2.4.3 (Kleene).** For S ⊆ ω, S is Π11 if and only if there is a uniformly computable sequence of linear orderings (Mn )n∈ω such that
                          S = {n : Mn is a well ordering}.
  *Proof:* (no proof in this paper)

- **Theorem 2.4.4 (Harrison).** There is a computable linear ordering of type ω1CK (1 + η).
  *Proof:* (no proof in this paper)

- **Theorem 3.1.1 (Completeness I).** Let A be a countable admissible set. Any logically valid sentence in LA has a proof in A. Moreover, the set of logically valid LA sentences is A-c.e.
  *Proof:* (no proof in this paper)

- **Theorem 3.1.2 (Completeness II).** Let A be a countable admissible set. If Γ is an A-c.e. set of LA sentences, and there is no proof of a contradiction from Γ, then Γ has a model.
  *Proof:* (no proof in this paper)

- **Theorem 3.1.3 (Barwise Compactness).** Let A be a countable admissible set, and suppose Γ is an A-c.e. set of LA sentences. If every A-finite subset of Γ has a model, then Γ has a model.
  *Proof:* (immediate from Theorem 3.1.2)

- **Theorem 3.1.4 (Kreisel Compactness).** Let Γ be a Π11 set of L-sentences. If every ∆11 subset of Γ has an ω-model, then Γ set has an ω-model.
  *Proof:* (no proof in this paper)

- **Theorem 3.1.5 (Kreisel-Barwise Compactness).** Let Γ be a Π11 set of computable infinitary sentences. If every ∆11 subset of Γ has a model, then Γ has a model.
  *Proof:* (no proof in this paper)

- **Theorem 3.1.6 (Interpolation).** Let L1 and L2 be vocabularies with
L = L1 ∩ L2 . Let A be a countable admissible set. If ϕ ∈ LA 1
                                                               and ψ ∈ L2A
are sentences such that |= ϕ → ψ, then there is a sentence θ ∈ LA such that
|= ϕ → θ and |= θ → ψ.
  *Proof:* Uses ΣA-saturation to demonstrate that the negation of ψ cannot be consistent with the A-c.e. consequences of ϕ, then applies Barwise Compactness.

- **Theorem 3.2.1 (Computable Compactness).** Let A be a countable admissible set with ω ∈ A. Let Γ be an A-c.e. set of LA -sentences. If every A-finite subset of Γ has a computable model, then Γ has a computable model.
  *Proof:* Applies Barwise Compactness to Γ along with an additional sentence asserting that the models are computable and named by an infinite computable set of constants.

- **Theorem 3.2.2 (Harrison, Barwise).** 1. There is a computable linear or-
    dering of type ω1CK (1 + η).
  2. Suppose X ⊆ ω, and let α = ω1X . Then there is an X-computable linear
     ordering of type α(1 + η).
  *Proof:* Applies Barwise Compactness to sentences specifying a linear ordering with initial segments of all computable ordinal types, while preventing any hyperarithmetical descending sequences via constants.

- **Theorem 3.2.3 (Arana).** For each n ≥ 1, there exist a computable ordering
(H, <H ) of type ω1CK (1+η) (the type of the Harrison ordering) and a computable
function F from H to the set of finitary Πn sentences, in the vocabulary of
arithmetic, such that
   • for any set Γ of Σn−1 and Πn−1 sentences, if P A ∪ Γ is consistent, then so
     is P A ∪ Γ ∪ {F (a) : a ∈ H},
   • for all a ∈ H, and all sets Λ of Σn sentences, if P A ∪ Λ ∪ {F (b) : b <H a}
     is consistent, then so is P A ∪ Λ ∪ {F (b) : b <H a} ∪ {¬F (a)}.
  *Proof:* (no proof in this paper)

- **Theorem 3.3.1 (Barwise).** If A is a countable admissible set with A =
                                                                     6 HF,
the Hanf number for LA is io(A) .
  *Proof:* (no proof in this paper)

- **Theorem 3.3.2 (Barwise-Kunen).** For an admissible set A =
                                                         6 HF of arbitrary
cardinality, the Hanf number of LA is ih(A) .
  *Proof:* (no proof in this paper)

- **Theorem 3.3.3 (Expansions).** Let A be a countable admissible set. Suppose
L is an A-finite vocabulary, L0 is a finite extension of L, and M is an A-finite
L-structure. Suppose Γ is an A-c.e. set of L0A -sentences such that for each
A-finite Γ0 ⊆ Γ, M can be expanded to a model of Γ0 . Then M can be expanded
to a model of Γ.
  *Proof:* Secures the model's elements via constants and bounded quantification, then applies Barwise Compactness to Γ and the diagram of M.

- **Theorem 3.3.4 (Uniqueness).** Let A be a countable admissible set. Suppose
that L is an A-finite vocabulary, and M, N are A-finite L-structures. If M and
N satisfy the same LA sentences, then M = ∼ N.
  *Proof:* Shows that finite partial isomorphisms preserving LA satisfaction form a back-and-forth family by expanding elements using the Expansions theorem.

- **Theorem 3.3.5 (Homogeneity).** Let A be a countable admissible set, and let
L be A-finite and M be an A-finite L-structure. If a, b are tuples in M satisfying
the same LA formulas, then there is an automorphism of M taking a to b.
  *Proof:* Constructs a back-and-forth family from extensions of the partial automorphism using the Expansions theorem as in the uniqueness proof.

- **Theorem 3.3.6 (Nadel).** Let A be a countable admissible set, and let
L be A-finite and M be an A-finite L-structure. Then the Scott height of M is at
most o(A).
  *Proof:* (no proof in this paper)

- **Theorem 3.3.7 (Makkai).** There is an arithmetical structure whose Scott height
is ω1CK and is not attained.
  *Proof:* (no proof in this paper)

- **Theorem 3.3.8 (Barwise).** Any countable model of ZF has a proper end ex-
tension satisfying ZF + V = L.
  *Proof:* Applies Barwise Compactness alongside the Levy-Shoenfield Absoluteness Theorem to ensure the constructible universe properties hold.

- **Lemma 4.2.1.** For every model AM = (M, A, E, (RM )R∈L ) of KP U over M,
the class of well-founded models BM = (M, B, F, (RM )R∈L ) of KP U , over M,
such that AM is an end extension of BM , has a unique largest element with
respect to the end extension relation. This is called the well-founded part of
AM .
  *Proof:* (no proof in this paper)

- **Theorem 4.2.2 (Truncation Lemma).** If AM is a model of KP U over M,
then its well-founded part is an admissible set over M.
  *Proof:* (no proof in this paper)

- **Theorem 4.3.1 (Existence of HY PM ).** For any countable L-structure M, there
is a least admissible set above M.
  *Proof:* (no proof in this paper)

- **Theorem 4.3.2.** For a countable structure M, the Scott height is at most
o(HY PM ).
  *Proof:* (no proof in this paper)

- **Lemma 4.4.1.** Every inductive definition Γ has a unique least fixed point.
  *Proof:* Transfinitely iterates the monotone function from the empty set until reaching a closure ordinal where the fixed point stabilizes.

- **Proposition 4.4.2.** For any L-structure M, and any formula ϕ which is pos-
itive in R, the least fixed point of Γϕ is a Π11 relation on M.
  *Proof:* (no proof in this paper)

- **Theorem 4.4.3 (Moschovakis).** 1. For every admissible ordinal α there exists a structure M with closure or-
     dinal α = κM .
  2. For each structure M, the closure ordinal κM is either an admissible ordinal
     or a limit of admissible ordinals.
  *Proof:* (no proof in this paper)

- **Theorem 4.4.4 (Barwise).** If α is a limit of admissible ordinals, and α has
cofinality ω, then there exists a structure M with closure ordinal α = κM .
  *Proof:* (no proof in this paper)

- **Theorem 4.4.5 (Barwise).** Let α, β be countable admissible ordinals such that
ω ≤ α ≤ β. Then there exists a structure M, in a finite vocabulary, such that
κM = α and o(HY PM ) = β. Moreover, κM = kϕk for some formula ϕ positive
in R.
  *Proof:* (no proof in this paper)

- **Theorem 4.4.6 (Barwise).** Two structures M, N satisfy the same sentences
of Ln∞ω if and only if there is a nonempty set F of partial isomorphisms from
M to N such that
   • The empty pair (∅, ∅) belongs to F ,
   • For each (a, b) ∈ F with |a| < n and c ∈ M , there exists d ∈ N such that
     (ac, bd) ∈ F ,
   • For each (a, b) ∈ F with |a| < n and d ∈ N , there exists c ∈ M such that
     (ac, bd) ∈ F .
  *Proof:* (no proof in this paper)

- **Theorem 5.1.1 (Barwise-Schlipf).** Every computably saturated structure is
ω-homogeneous.
  *Proof:* Relies on constructing a computable set of formulas stating that appending an element to one tuple satisfies the same finitary formulas as appending to the other.

- **Theorem 5.1.2 (Barwise-Schlipf).** Let M be a countable structure. Then M
is computably saturated if and only if o(HY PM ) = ω.
  *Proof:* (no proof in this paper)

- **Corollary 5.1.3.** Every countable computably saturated structure has Scott
height ≤ ω.
  *Proof:* (no proof in this paper)

- **Theorem 5.1.4 (Barwise-Schlipf).** If M is computably saturated, then the
subsets of M which are elements of HY PM are just those definable in M by
finitary formulas with parameters in M .
  *Proof:* (no proof in this paper)

- **Theorem 5.1.5 (Resplendence).** Let M be a countable computably saturated
structure, let L0 = L ∪ {R1 , . . . , Rn } be a finite extension of L, and let Γ be
a c.e. set of finitary L0 -sentences. If Γ ∪ T h(M) is consistent, then M can be
expanded to a (computably saturated) model (M, S1 , . . . , Sn ) of Γ.
  *Proof:* (no proof in this paper)

- **Theorem 5.1.6 (Existence).** Every structure has a computably saturated ele-
mentary extension of the same cardinality.
  *Proof:* (no proof in this paper)

- **Theorem 5.1.7 (Schlipf).** An elementary first order theory T is complete if
and only if for every countable computably saturated model pair (M, N ) of models
of T , M is isomorphic to N .
  *Proof:* Completeness ensures isomorphism via the Resplendence Theorem; otherwise, the Existence Theorem yields a computably saturated extension containing non-elementarily-equivalent structures.

- **Theorem 5.1.8.** A complete elementary first order theory T admits quantifier
elimination if and only if for every countable computably saturated model M of
T , the set of partial automorphisms of M is a back-and-forth family.
  *Proof:* Forward implication follows from quantifier elimination and Resplendence ensuring automorphisms; the reverse employs Existence and Compactness to contradict any partial automorphism that fails to extend.

- **Theorem 5.1.9 (Lipschitz-Nadel).** A countable structure M = (M, +) can
be expanded to a model of P A if and only if either M =
                                                      ∼ (ω, +), or M is a
computably saturated model of Pressburger arithmetic.
  *Proof:* (no proof in this paper)

- **Theorem 5.1.10 (Schlipf).** Let M be a countable computably saturated model
of ZF . Then there is an indiscernible set I of ordinals of M such that (M, I)
is computably saturated and satisfies the replacement and separation schemes
relative to I, and for each α ∈ I, (Vα , ∈)M ≺ M and (Vα , ∈)M ∼
                                                               = M.
  *Proof:* (no proof in this paper)

- **Theorem 5.2.1.** Let A be a countable admissible set. A structure M is
ΣA -saturated if and only if A can be extended to an admissible set B above
M such that o(B) = o(A).
  *Proof:* (no proof in this paper)

- **Theorem 5.2.2 (Existence and Resplendence).** Let A be a countable admissible set.
   1. Every consistent A-c.e. set of LA -sentences has a ΣA -saturated model.
   2. Suppose M is a countable ΣA -saturated L-structure, L0 is a finite extension
      of L, and Γ is an A-c.e. set of L0A sentences. If every consequence of Γ in
      LA is true in M, then M can be expanded to a ΣA -saturated model of Γ.
  *Proof:* Constructs a consistency property containing A-c.e. sets of sentences evaluated on elements of the saturated structure.

- **Theorem 5.2.3 (Sacks [59], Friedman-Jensen [28]).** For any countable admis-
sible ordinal α > ω, there exists X ⊆ ω such that α = ω1X .
  *Proof:* Employs Existence and Resplendence to build a ΣA-saturated model encompassing a computed ordering, then utilizes saturation to prove no ordering of length α is computable.

- **Theorem 5.2.4 (Barwise).** Let A be a countable admissible set, and let σ be
a sentence in LA such that for each ordinal α in A, σ has a model of order type
α. Then σ has a model which is a linear ordering with a subset of order type η.
  *Proof:* Constructs a ΣA-saturated linear ordering with specific initial segments and inductively builds an embedding from the rationals by verifying sub-interval existence.