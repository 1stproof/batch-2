<!-- Generated 2026-05-31T02:08:01 -->
<!-- Source PDF: kechris__classical_descriptive_set_theory.pdf (346395 bytes) -->
<!-- Citation: A. S. Kechris (1995). Classical Descriptive Set Theory. Springer-Verlag (Graduate Texts in Mathematics, Vol. 156). -->

# Classical Descriptive Set Theory (A. S. Kechris, 1995)

## Definitions
- **Definition. (2.1)** Tree = subset T ⊆ A<N closed under initial segments. (I.e., if t ∈ T and s ⊆ t, then s ∈ T .)
- **Definition. (2.5)** Let S, T be trees (on sets A, B, resp.). A map ϕ : T → S is called monotone if s ⊆ t implies ϕ(s) ⊆ ϕ(t). For such ϕ let D(ϕ) = {x ∈ [S] : lim n length(ϕ(x|n)) = ∞}. For x ∈ D(ϕ), let [ n ϕ∗ (x) = ϕ(x|n) ∈ [T ]. We call ϕ proper if D(ϕ) = [S].
- **Definition. (3.1)** A topological space X is completely metrizable if it admits a compatible metric d such that (X, d) is complete. A separable completely metrizable space is called Polish.
- **Definition. (6.1)** A Cantor scheme on a set X is a family (As )s∈2<N such that: (i) As0 ∩ As1 = ∅ for s ∈ 2<N , (ii) Asi ⊆ As , for s ∈ 2<N , i ∈ {0, 1}.
- **Definition. (7.5)** A Lusin scheme on a set X is a family (As )s∈N<N such that: (i) Asi ∩ Asj = ∅ for s ∈ N<N , (ii) Asi ⊆ As , for s ∈ N<N , i ∈ {0, 1}.
- **Definition. (8.2)** A topological space is called a Baire space if it satisfies the equivalent conditions of 8.1.
- **Definition. (8.5)** Let X be a topological space and P ⊆ X. If P is comeager, we say that P holds generically or that the generic element of X is in P . (Sometimes the word typical is used instead of generic.)
- **Definition. (8.10)** Choquet game: Players I and II take turns in playing nonempty open subsets of X so that U0 ⊇ V0 ⊇ U1 ⊇ TV1 ⊇ . . . . T We say that II wins this run of game if n Vn (= n Un ) 6= ∅.
- **Definition. (8.12)** A nonempty topological space is a Choquet space if player II has a winning strategy in GX .
- **Definition. (8.14)** strong Choquet game
- **Definition. (8.21)** Let X be a topological space. A set A ⊆ X has the Baire property (BP) if A =∗ U for some open set U ⊆ X.
- **Definition. (8.25)** If A is comeager in U , we say that A holds generically in U or that U forces A, in symbols U |= A.
- **Definition. (8.34)** A game is determined if at least one of the two players has a winning strategy.
- **Definition. (14.1)** Let X be a Polish space. A set A ⊆ X is called analytic if there is a Polish space Y and a continuous function f : Y → X with f (Y ) = A. (The empty set is analytic, by taking Y = ∅.)
- **Definition. (24.1)** Let X, Y be metrizable spaces. A function f : X → Y is of Baire class 1 if f −1 (U ) ∈ Σ02 (X) for every open set U ⊆ Y . If Y is separable, it is clearly enough in this definition to restrict U to any countable subbasis for Y . Recursively, for 1 < ξ < ω1 we define now a function f : X → Y to be of Baire class ξ if it is the pointwise limit of a sequence of functions fn : X → Y , where fn is of Baire class ξn < ξ.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem (Urysohn metrization theorem). (1.1)** Let X be a second countable topological space. Then X is metrizable iff X is T1 and regular.
  *Proof:* (no proof in this paper)
- **Theorem (Urysohn’s Lemma). (1.2)** Let X be a metrizable space. If A, B are two disjoint subsets of X, there is a function f : X → h0, 1i such that f (x) = 0 for x ∈ A and f (x) = 1 for x ∈ B.
  *Proof:* (no proof in this paper)
- **Theorem (Tietze Extension Theorem). (1.3)** Let X be a metrizable space. If A ⊆ X is closed and f : A → R is continuous, there is fˆ: X → R which is continuous and extends f . Moreover, if f is bounded by M , i.e., |f (x)| ≤ M for x ∈ A, so is f .
  *Proof:* (no proof in this paper)
- **Proposition. (2.4)** The map T 7→ [T ] is a bijection between pruned trees on A and closed subsets of AN . Its inverse is given by F 7→ TF = {x|n : x ∈ F, n ∈ N}.
  *Proof:* (no proof in this paper)
- **Proposition. (2.6)** The set D(ϕ) is Gδ in [S] and ϕ∗ : D(ϕ) → [T ] is continuous. Conversely, if f : G → [T ] is continuous, with G ⊆ [S] a Gδ set, then there is monotone ϕ : S → T with f = ϕ∗ .
  *Proof:* (no proof in this paper)
- **Proposition. (2.8)** Let F ⊆ H be two closed nonempty subsets of AN . Then F is a retract of H.
  *Proof:* (no proof in this paper)
- **Proposition. (2.9)** Let S, T be trees on A, B respectively. If T is well-founded, then S is well-founded with %(S) < %(T ) iff there is a strictly monotone map ϕ: S → T.
  *Proof:* (no proof in this paper)
- **Proposition. (2.12)** Assume that (A, <) is a wellordered set. Then for any tree T on A, T is well-founded iff Kleene-Brouwer ordering restricted to T is a wellordered.
  *Proof:* (no proof in this paper)
- **Proposition. (3.3)** (i) The completion of a separable metric space is Polish. (ii) A closed subspace of a Polish space is Polish. (iii) The product of a sequence of completely metrizable (resp. Polish)spaces is completely metrizable (resp. Polish). The sum of a family of completely metrizable spaces is completely metrizable. The sum of a sequence of Polish spaces is Polish.
  *Proof:* (no proof in this paper)
- **Theorem (Kuratowski). (3.8)** Let X be metrizable, Y be completely metrizable, A ⊆ X, and f : A → Y be continuous. Then there is a Gδ set G with A ⊆ G ⊆ A and a continuous extension g : G → Y of f .
  *Proof:* (no proof in this paper)
- **Theorem. (3.11)** If X is metrizable and Y ⊆ X is completely metrizable, then Y is a Gδ in X. Conversely, if X is completely metrizable and Y ⊆ X is a Gδ , then Y is completely metrizable.
  *Proof:* (no proof in this paper)
- **Proposition. (4.6)** Let X be a compact topological space. Then X is metrizable iff X is Hausdorff and second countable.
  *Proof:* (no proof in this paper)
- **Theorem (Banach). (4.7)** The unit ball B1 (X ∗ ) of a separable Banach space is compact in the weak∗ -topology. A compatible metric is given by d(x∗ , y ∗ ) = ∞ X n=0 2−n−1 |hxn , x∗ i − hxn , y ∗ i| for (xn ) dense in the unit ball.
  *Proof:* (no proof in this paper)
- **Example (König’s Lemma). (4.12)** Let T be a tree on A. If T is finite splitting then [T ] 6= ∅ iff T is infinite.
  *Proof:* (no proof in this paper)
- **Theorem. (4.14)** Every separable metrizable space is homeomorphic to a subspace of the Hilbert cube I N . In particular, the Polish spaces are, up to homeomorphism, exactly the Gδ subspaces of the Hilbert cube.
  *Proof:* (no proof in this paper)
- **Theorem. (4.17)** Every Polish space is homeomorphic to to a closed subspace of RN .
  *Proof:* (no proof in this paper)
- **Theorem. (4.18)** Every non-empty compact metrizable space is a continuous image of C.
  *Proof:* (no proof in this paper)
- **Theorem. (6.2)** Let X be a nonempty perfect Polish space. Then there is an embedding of C into X.
  *Proof:* constructing a Cantor scheme of open subsets of X with decreasing diameter.
- **Corollary. (6.3)** If X is a nonempty perfect Polish space, then card X = 2ℵ0 . In particular, a nonempty perfect subset of a Polish space has the cardinality of the continuum.
  *Proof:* (immediate from Theorem. (6.2))
- **Theorem (Cantor-Bendixson). (6.4)** Let X be a Polish space. Then X can be uniquely written as X = P ∪ C, with P a perfect subset of X and C countable open.
  *Proof:* (no proof in this paper)
- **Corollary. (6.5)** Any uncountable Polish space contains a homeomorphic copy of C and in particular has cardinality 2ℵ0 .
  *Proof:* (immediate from Theorem (Cantor-Bendixson). (6.4))
- **Theorem. (7.3)** Let X be separable metrizable. Then X is zero-dimensional iff every non-empty closed subset of X is a retract of X.
  *Proof:* (no proof in this paper)
- **Theorem (Brouwer). (7.4)** The Cantor space C is unique, up to homeomorphism, perfect nonempty, compact metrizable, zero-dimensional space.
  *Proof:* (no proof in this paper)
- **Proposition. (8.1)** Let X be a topological space. The following statements are equivalent: (i) Every nonempty open set in X is non-meager. (ii) Every comeager set in X is dense. (iii) The intersection of countably many dense open sets in X is dense.
  *Proof:* (no proof in this paper)
- **Proposition. (8.3)** If X is a Baire space and U ⊆ X is open, U is a Baire space.
  *Proof:* (no proof in this paper)
- **Theorem (The Baire Category theorem). (8.4)** Every completely metrizable space is Baire. Every locally compact Hausdorff space is Baire.
  *Proof:* (no proof in this paper)
- **Theorem (Oxtoby). (8.11)** A nonempty topological space X is a Baire space iff player I has no winning strategy in the Choquet game GX .
  *Proof:* (no proof in this paper)
- **Theorem. (8.17)** Let X be a nonempty separable metrizable space and X̂ a Polish space in which X is dense. Then i) (Oxtoby) X is Choquet ⇔ X is comeager in X̂; ii) (Choquet) X is strong Choquet ⇔ X is Gδ in X̂ ⇔ X is Polish
  *Proof:* (no proof in this paper)
- **Theorem (Choquet). (8.18)** A nonempty, second countable topological space is Polish iff it is T1 , regular and strong Choquet.
  *Proof:* (no proof in this paper)
- **Theorem (Sierpiński). (8.19)** Let X be Polish and Y separable metrizable. If there is a continuous open surjection of X onto Y , then Y is Polish.
  *Proof:* (no proof in this paper)
- **Proposition. (8.22)** Let X be a topological space. The class of sets having the BP is a σ-algebra on X. It is the smallest σ-algebra containing all open sets and all meager sets.
  *Proof:* (no proof in this paper)
- **Proposition. (8.23)** Let X be a topological space and A ⊆ X. Then the following statements are equivalent: i) A has the BP; ii) A = G ∪ M , where G is Gδ nad M is meager; iii) A = F \ M where F is Fσ and M is meager.
  *Proof:* (no proof in this paper)
- **Proposition. (8.26)** Let X be a topological space and suppose that A ⊆ X has the BP. Then either A is meager or there is a nonempty open set U ⊆ X on which A is comeager (i.e., X |= (X \ A) or there is nonempty open U ⊆ X, with U |= A). If X is a Baire space, exactly one of these alternatives holds.
  *Proof:* (no proof in this paper)
- **Proposition. (8.27)** Let X be a topological space. (i) If An ⊆ X, then for any open U ⊆ X, U |= \ n An ⇔ ∀n(U |= An ) (ii) If X is a Baire space, A has BP in X and U varies below over nonempty open sets in X, and V over a weak basis, then U |=∼ A ⇔ ∀V ⊆ U (V 6|= A).
  *Proof:* (no proof in this paper)
- **Theorem. (8.29)** Let X be a topological space and A ⊆ X. Put U (A) = [ {U open ; U |= A}. Then U (A) \ A is meager, and if A has the BP, A \ U (A), and thus A∆U (A) is meager, so A =∗ U (A).
  *Proof:* (no proof in this paper)
- **Theorem (Banach-Mazur, Oxtoby). (8.33)** Let X be a nonempty topological space. Then i) A is comeager ⇔ II has a winning strategy in G∗∗ (A). ii) If X is Choquet and there is a metric d on X whose open balls are open in X, then A is meager in a nonempty open set ⇔ I has winning strategy in G∗∗ (A).
  *Proof:* (no proof in this paper)
- **Theorem (Uspenskiı̆). (9.18)** Every Polish group is isomorphic to a (necessarily closed) subgroup of H(IN ).
  *Proof:* (no proof in this paper)
- **Theorem (Keller’s Theorem). (9.19)** If X is a separable infinite-dimensional Banach space, B1 (X ∗ ) with the weak∗ -topology is homeomorphic to the Hilbert cube IN .
  *Proof:* (no proof in this paper)
- **Proposition. (11.5)** Every Borel set has the Baire property, and every Borel function is Baire measurable.
  *Proof:* (no proof in this paper)
- **Theorem (Lebesgue, Hausdorff). (11.6)** Let X be a metrizable space. The class of Borel functions f : X → R is the smallest class of functions from X into R which contains all the continuous functions and is closed under taking pointwise limits of sequences of functions.
  *Proof:* (no proof in this paper)
- **Theorem (Lusin). (17.12)** Let X be a metrizable space and µ a finite Borel measure on X. Let Y be a second countable topological space and f : X → Y a µ-measurable function. For every ε > 0, there is a closed set F ⊆ X with µ(X \ F ) < ε such that f |F is continuous. Moreover, if X is Polish, we can take F to be compact. In particular, if Y = R, there is a continuous g : X → R with µ({x; f (x) 6= g(x)}) < ε.
  *Proof:* (no proof in this paper)
- **Theorem (Lebesgue, Hausdorff, Banach). (24.3)** Let X, Y be metrizable spaces, with Y separable. Then for 1 < ξ < ωi , f : X → Y is in Bξ iff f is Σ0ξ+1 -measurable. In particular, S ξ Bξ is the class of Borel functions.
  *Proof:* (no proof in this paper)