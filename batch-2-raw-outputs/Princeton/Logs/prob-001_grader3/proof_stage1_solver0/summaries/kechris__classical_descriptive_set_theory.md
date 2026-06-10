<!-- Generated 2026-05-31T02:11:37 -->
<!-- Source PDF: kechris__classical_descriptive_set_theory.pdf (643342 bytes) -->
<!-- Citation: Kechris, A. S. (1995). Classical Descriptive Set Theory. Springer. -->

```markdown
# Classical Descriptive Set Theory, Kechris, A. S. (1995). Classical Descriptive Set Theory. Springer.

## Definitions
- **Definition 1.1.** Let X be a topological space. We say that X is metrizable if there is a metric d such that the topology is induced by the metric. We say that X is separable if there is a countable dense subset. A Polish space is a separable topological space that is metrizable by a complete metric.
- **Definition 1.7.** Baire space is the Polish space N = NN and Cantor space is the Polish space C = 2N .
- **Definition 1.15.** We say that a tree T ⊆ N<ω is pruned if for all σ ∈ T , there is i ∈ N with σbi ∈ T .
- **Definition 1.21.** Let X be a Polish space. We say that P ⊆ X is perfect if X is a closed set with no isolated points.
- **Definition 1.24.** If F ⊆ X is closed, the Cantor–Bendixson derivative is Γ(F ) = {x ∈ F : x is not an isolated point of F }. For each countable ordinal α < ω1 , we define Γα (F ) as follows: i) Γ0 (F ) = F ; ii) Γα+1 (F ) =\ Γ(Γα (F )); iii) Γα (F ) = \bigcap β<α Γβ (F ).
- **Definition 1.38.** Let X be a topological space. Let K(X) be the collection of all compact subsets of X. The Vietoris topology on K(X) is the smallest topology such that for each open U ⊆ X the sets {A ∈ K(X) : A ⊆ U } and {A ∈ K(X) : A ∩ U 6= ∅} are open.
- **Definition 1.40.** Suppose X is a metric space. We define the Hausdorff metric on K(X) by dH (A, B) = max max d(a, B), max d(b, A) .
- **Definition 2.1.** If X is any set, a σ-algebra on X is a collection of subsets of X that is closed under complement and countable union. A measure space (X, Ω) is a set X equipped with a σ-algebra Ω. If (X, ΩX ) and (Y, ΩY ) are measure spaces, we say f : X → Y is a measurable function if f −1 (A) ∈ ΩX for all A ∈ ΩY . We say that (X, ΩX ) and (Y, ΩY ) are isomorphic if and only if there is a measurable bijection with measurable inverse.
- **Definition 2.2.** If X is a topological space, the class of Borel sets B(X) is the smallest σ-algebra containing the open sets. If X and Y are topological spaces, we say that f : X → Y is Borel measurable if it is a measurable map between the measure spaces (X, B(X)) and (Y, B(Y )). We say that a measure space (X, Ω) is a standard Borel space if there is a Polish space Y such that (X, Ω) is isomorphic to (Y, B(Y )).
- **Definition 2.4.** Let X be a metrizable space. For each α < ω1 we define Σ0α (X) and Π0α (X) ⊂ P(X) as follows: Σ01 (X) is the collection of all open subsets of X; Π0α (X) is the collection of all sets X \ A where A ∈ Σ0α (X); For α > 1, Σ0α (X) is the collection of all sets X = S Ai where each Ai ∈ Π0βi (X) for some βi < α. We say that A ∈ ∆0α (X) if A ∈ Σ0α (X) and A ∈ Π0α (X). When we are working in a single space we omit the X and write Σ0α and Π0α instead of Σ0α (X) and Π0α (X).
- **Definition 2.29.** If X and Y are Polish spaces, A ∈ B(X) and B ∈ B(Y ), we say that f : X → Y is a Borel isomorphism if is a Borel measurable bijection with Borel measurable inverse.
- **Definition 2.36.** We say that U ⊂ Y × X is universal-Σ0α if U ∈ Σ0α (Y × X), and if A ∈ Σ0α (X), then A = Ua for some a ∈ A. We define Π0α universal sets similarly.
- **Definition 2.39.** Let X and Y be Polish spaces, with A ⊆ X and B ⊆ Y . We say that A is Wadge-reducible to B if there is a continuous f : X → Y such that x ∈ A if and only if f (x) ∈ B for all x ∈ A.
- **Definition 2.41.** For Γ = Σ0α or Π0α we say that A ⊆ X is Γ-complete if A ∈ Γ(X) and if B ∈ Γ(X), then B ≤w A.
- **Definition 2.46.** We say that A ⊆ X is nowhere dense set , if whenever U ⊆ X is open and nonempty, there is a nonempty open V ⊆ U such that A ∩ U = ∅. We say that B ⊆ X is meager if X is a countable union of nowhere dense sets.
- **Definition 2.53.** For A, B ⊆ X we define A =∗ B if and only if A4B is meager, where A4B = (A \ B) ∪ (B \ A).
- **Definition 2.55.** Let A ⊆ X. We say that A has the Baire property if there is an open set U such that A =∗ U .
- **Definition 3.1.** A partial function f : N → N is partial recursive if there is a computer program P such that P halts on input n if and only if n ∈ dom (f ) and if P halts on input n, then the output is f (n). We say that a set A ⊆ N is recursive if and only if its characteristic function is recursive.
- **Definition 3.3.** We say that A ⊆ N is recursively enumerable if there is a partial recursive function f : N → N such that A is the image of f .
- **Definition 3.8.** We say A is many-one reducible to B if there is a total recursive f such that n ∈ A if and only if f (n) ∈ B for all n ∈ N. We write A ≤m B if A is many-one reducible to B.
- **Definition 3.10.** We say that f : N → N is computable if there is an oracle program P such that if x ∈ N and P is run with oracle x on input n, then P halts and outputs (f (x))(n). We say that f : N → N is computable from z if there is a two oracle program P such that if x ∈ N and P is run with oracles z and x on input n, then M halts and outputs (f (x))(n).
- **Definition 3.12.** We say that A ⊆ X is Σ01 if there is a partial recursive f : N → SX such that A = S n Nf (n) .
- **Definition 3.13.** If x ∈ N we say that A ⊆ X is Σ01 (x) if there is f : N → SX partial recursive in x such that A = S n Nf (n) .
- **Definition 3.16.** Let X = Nk × N l . We say that A ⊆ X is Π0n if and only if X \ A is Σ0n . We say that A ⊆ X is Σ0n+1 if and only if there is B ⊆ N × X in Π0n such that x ∈ A if and only if ∃n (n, x) ∈ B. We say that A is ∆0n if it is both Σ0n and Π0n . We say that A ⊆ X is arithmetic if A ∈ ∆0n for some n.
- **Definition 4.1.** Let X be a Polish space. We say that A ⊆ X is analytic if there is a Polish space Y , f : Y → X continuous and B ∈ B(Y ) such that A = f (B) the image of B. We let Σ11 (X) denote the collection of all analytic subsets of X.
- **Definition 4.4.** Let X be a Polish space. We say that A ⊆ X is Π11 (X) if X \ A is Σ11 . Π11 (X)-sets are also called coanalytic. We say A ⊆ X is in ∆11 (X) if A ∈ Π11 (X) ∩ Σ11 (X).
- **Definition 4.19.** Suppose Bσ ⊆ X for all σ ∈ N<ω . We define A({Bσ }) = S f ∈N T n∈N Bσ . We call A the Souslin operation..
- **Definition 4.26.** Let C be the smallest σ-algebra containing the Borel sets and closed under the Souslin operator A.
- **Definition 4.27.** Let X be a Polish space. We say that A ⊆ X is Σ1n+1 (X) if there is B ∈ Π1n (X × X) such that A = πX (B). We say that A ⊆ X is Π1n (X) if X ⊆ A is Σ1n . We let ∆1n (X) = Σ1n (X) ∩ Π1n (X). We say that A ⊂ X is projective if it is Σ1n for some n.
- **Definition 4.37.** We say that A ⊆ X is Σ11 if there is a B ⊆ N × X such that B ∈ Π01 and A = {x : ∃y (y, x) ∈ B}. We say A ⊆ X is Π1n if X \ A is Σ1n and we say that A ⊆ X is Σ1n+1 if there is a B ⊆ N × X with B ∈ Π1n such that A = {x : ∃y (y, x) ∈ B}. We say A is ∆1n if it is both Σ1n and Π1n .
- **Definition 5.1.** We say that T ⊆ N<ω × N<ω is a tree if: i) |σ| = |τ | for all (σ, τ ) ∈ T ; ii) if (σ, τ ) ∈ T and n ≤ |σ|, then (σ|n, τ |n) ∈ T . If f, g ∈ N we say that (f, g) is a path through T if (f |n, g|n) ∈ T for all n ∈ N. We let [T ] be the set of all paths through T .
- **Definition 5.5.** If T is a tree, let T 0 = {σ ∈ T : ∃τ ∈ T σ ⊂ τ } be the subtree of nonterminal nodes of T . For α < ω1 define T α as follows: i) T 0 = T ; ii) T α+1 =(T α )0 ; iii) T α = T β<α T β for α a limit.
- **Definition 5.7.** If T ⊆ N<ω is a tree, we define a rank ρT : T → ω1 ∪ {∞}, by i) if σ ∈ T α \ T α+1 , then ρT (σ) = α. ii) if σ ∈ T α<ω1 T α , then ρT (σ) = ∞.
- **Definition 5.10.** If S and T are trees we say that f : S → T is order-preserving if f (σ) ⊂ f (τ ) for all σ, τ ∈ T with σ ⊂ τ .
- **Definition 5.17.** A norm on a set A is a function φ : A → On where On is the class of ordinals.
- **Definition 5.19.** A class of sets Γ has the reduction property if whenever A, B ∈ Γ there are A0 ⊆ A and B0 ⊆ B such that A0 , B0 ∈ Γ, A0 ∩ B0 = ∅ and A0 ∪ B0 = A ∪ B.
- **Definition 5.21.** We say that Γ has the separation property if whenever A, B ∈ Γ and A ∩ B = ∅ there is C ∈ Γ ∩ Γ̌ such that A ⊆ C and C ∩ B = ∅.
- **Definition 5.24.** Suppose A ⊆ X × Y . We say that B ⊆ A uniformizes A if and only if i) πX (A) = πX (B), and ii) for all x ∈ πX (A) there is a unique b ∈ Y such that (x, b) ∈ B.
- **Definition 5.25.** We say that Γ has the uniformization property if for all A ∈ Γ(N × N ), there is B ∈ Γ a uniformization of A.
- **Definition 5.39.** We say that an ordinal α is recursive if there is a recursive set A ⊆ N and ≺ a recursive linear order of A such that (A, ≺) ∼= (α, <).
- **Definition 5.41.** Let ω1ck be the least non-recursive ordinal. We call this ordinal the Church–Kleene ordinal.
- **Definition 5.42.** For σ, τ ∈ N<ω we say σ / τ if τ ⊂ σ or there is an n such that σ(n) 6= τ (n), but σ(m) = τ (m) for all m < n. We call / the Kleene–Brower order.
- **Definition 6.1.** A strategy for Player I is a function τ : X <N → X.
- **Definition 6.2.** We say that τ is a winning strategy for Player I if Player I wins any game played using the strategy τ , i.e., for any x0 , x1 , x2 , . . . ∈ X, the sequence τ (∅), x0 , τ (x0 ), x1 , τ (x0 , x1 ), x2 , τ (x0 , x1 , x2 ), . . . is in A.
- **Definition 6.3.** We say that the game G(A) is determined if either Player I or Player II has a winning strategy.
- **Definition 7.1.** A Borel code for a subset of X is a pair hT, li where T ⊆ N <ω is a well-founded tree and l : T → ({0} × {0, 1}) ∪ ({1} × S X ) such that: i) if l(∅) = h0, 0i, then σb0 ∈ T and σbn 6∈ T for all n ≥ 1; ii) if l(∅) = h1, ηi, then σbn 6∈ T for all n ∈ N.
- **Definition 7.2.** We define B(hT, li) inductively on the height of T . i) B(h∅, ∅i) = ∅. ii) If l(∅) = h1, ηi, then B(hT, li) = Nη . iii) If l(∅) = h0, 0i, then B(hT, li) = X \ B(hTh0i , lh0i i). iv) If l(∅) = h0, 1i, then B(hT, li) = S hni∈T B(hThni , lhni i).
- **Definition 7.13.** We say x ∈ N is hyperarithmetic if x ∈ ∆11 . We say that x is hyperarithmetic in y, and write x ≤hyp y if x ∈ ∆11 (y).
- **Definition 7.34.** We say that A is a Kσ set if it is a countable union of compact sets.
- **Definition 8.3.** The Gandy topology on N is the smallest topology in which every Σ11 -set is open.
- **Definition 9.1.** T ⊆ X is a transversal for E if |T ∩ [x]| = 1 for all x ∈ X. We say that s : X → X is a selector for E if s(x)Ex for all x ∈ X and s(x) = s(y) if xEy.
- **Definition 9.4.** Let E be an equivalence relation on X. We say that (An : n ∈ N) is a separating family for E if xEy ⇔ ∀n (x ∈ An ↔ y ∈ An ). We say that E is tame if there is a separating family (An : n ∈ N) where each An is Borel. More generally, if Ω is a σ-algebra on X containing the Borel sets, we say that E is Ω-tame if there is a separating family (An : n ∈ N) where each An ∈ Ω.
- **Definition 9.6.** Suppose E is a Borel equivalence relation on X and E ∗ is a Borel equivalence relation on Y . We say that E is Borel reducible to E ∗ if there is Borel measurable f : X → Y such that xEy ⇔ f (x)E ∗ f (y).
- **Definition 9.10.** Let E0 be the equivalence relation on C defined by xE0 y if and only if ∃n∀m ≥ n x(n) = y(n). We call E0 the Vitali equivalence relation.
- **Definition 9.11.** We say that µ is a Borel probability measure on X if there is a σ-algebra Ω on X containing the Borel sets, and a measure µ : Ω → [0, 1] with µ(X) = 1.
- **Definition 9.12.** We say that A ⊆ X is E-invariant if whenever x ∈ A and yEx, then y ∈ A. If µ is a Borel probability measure, we say that µ is E-ergodic, if µ(A) = 0 or µ(A) = 1 whenever A is µ-measurable and E-invariant.
- **Definition 9.13.** We say that A ⊆ X is E-atomic if there is x ∈ X with µ([x]) > 0.
- **Definition 10.1.** Suppose G is a group. A map α : G × X → X is an action. If α(g, α(h, x)) = α(gh, x) for all g, h ∈ G and α(e, x) = x for the identity element x. If G and X are Borel subsets of Polish spaces and the action α is Borel measurable, we say that α is a Borel action.
- **Definition 10.2.** If α : G × X → X is a Borel action, the orbit equivalence relation EG is given by xEy ⇔ ∃g ∈ G gx = y.
- **Definition 10.3.** A Borel equivalence relation E is countable if and only if every E-class is countable.
- **Definition 10.5.** We say that a countable Borel equivalence relation E is universal if E ∗ ≤B E for all countable Borel equivalence relations E.
- **Definition 11.1.** We say that a Borel equivalence relation E is finite if every equivalence class is finite. We say that E is hyperfinite if there are finite Borel equivalence relations E0 ⊆ E1 ⊆ . . . such that E = S En .
- **Definition 11.6.** If E is an equivalence relation on X we say that A ⊆ X is full for E if for all x ∈ X there is y ∈ A such that xEy.
- **Definition 11.15.** Suppose G is a finitely generated group. We say that G has polynomial growth if there is a finite X ⊆ G closed under inverse such that G = S X n and there are C, d ∈ Z such that |X n | ∈ O(nd ) for all n > 0.
- **Definition 11.17.** Let G be a countable group. We say that G has the mild growth property of order c, if there is a sequence of finite sets K0 ⊆ K1 ⊆ K2 . . . such that: i) S Ki = G; ii) 1 ∈ K0 ; iii)Ki = Ki−1 for all i; iv) Ki2 ⊆ Ki+1 for all i; v) |Ki+4 | < c|Ki | infinitely many i.
- **Definition 11.21.** Let F be a symmetric, reflexive Borel binary relation on a Borel space X. We say that F is locally finite if {y : yF x} is finite for all x. We say that Y ⊆ X is F -discrete if ¬(xF y) for all distinct x, y ∈ Y and we say that Y is maximal F -discrete if it is discrete and for all x ∈ X there is y ∈ Y with xF y.
- **Definition 11.23.** Let F0 ⊆ F1 ⊆ F2 be a sequence of locally finite, symmetric,reflexive Borel binary relations on X. We say that the sequences satisfies the Weiss condition if Fn2 ⊆ Fn+1 for all n and there is a integer c such that for all x ∈ X there are infinitely many n such that any Fn -discrete set contained in {y : yFn+2 x} has cardinality at most c.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.4.** Every Polish space is homeomorphic to a subspace of H.
  *Proof:* Constructs an embedding into the Hilbert cube using a countable dense set and a compatible metric.
- **Lemma 1.5.** Suppose X is a Polish space and X0 ⊇ X1 ⊇ X2 ⊇ . . . are closed subsets T of X such that limn→∞ diam (Xn ) = 0. Then there is x ∈ X such that Xn = {x}.
  *Proof:* Uses the completeness of the metric and the vanishing diameter to show the chosen sequence is Cauchy.
- **Lemma 1.6.** If X is a Polish space, U ⊆ X is open and ² > 0, then there are open sets U0 , U1 , U2 , . . . such that U = S Un = S U n and diam (Un ) < ² for all n.
  *Proof:* Selects small open balls around a dense subset inside the given open set.
- **Lemma 1.14.** i) U ⊆ N is open if and only if there is S ⊆ N<ω such that U = S Nσ . ii) F ⊆ N is closed if and only if there is a tree T ⊆ N <ω such that F = [T ].
  *Proof:* Translates basic clopen neighborhoods into sequences and their prefixes as trees.
- **Lemma 1.16.** i) If k > 0, then N is homeomorphic to Nd × N k . ii) N is homeomorphic to N N .
  *Proof:* Defines explicit topological interleaving bijections.
- **Theorem 1.17.** If X is a Polish space, then there is a continuous surjective φ : N → X.
  *Proof:* Builds a tree of decreasing open sets mapping Baire space sequences to unique points in the space.
- **Lemma 1.18.** Suppose X is a Polish space and Y ⊆ X is an Fσ -set and ² > 0. There are disjoint Fσ -sets Y0 , Y1 , . . . with diam (Yi ) < ², Y i ⊆ Y and S Yi = Y .
  *Proof:* Expresses the set as a disjoint union of differences of closed sets and intersects them with small open sets.
- **Theorem 1.19.** If X is Polish, there is F ⊆ N closed and a continuous bijection φ : F → X.
  *Proof:* Uses the previous lemma to build a tree of Fσ-sets with vanishing diameter and extracts a closed set of unique limits.
- **Lemma 1.22.** If P ⊆ X is a nonempty perfect set, then there is a continuous injection f : C → P . Indeed, there is a perfect F ⊆ P , homeomorphic to C. In particular |P | = 2ℵ0 .
  *Proof:* Constructs a binary tree of disjoint open subsets inside the perfect set.
- **Lemma 1.25.** Suppose X is a Polish space and F ⊆ X is closed. i) Γα (F ) is closed for all α < ω1 ; ii) |Γα+1 (F ) \ Γα (F )| ≤ ℵ0 ; iii) if Γ(F ) = F , then F is perfect, and Γα (F ) = F for all α < ω1 . iv) there is an ordinal α < ω1 such that Γα (F ) = Γα+1 (F )
  *Proof:* Uses the countable basis to injectively map isolated points to basic open sets, bounding the rank.
- **Theorem 1.27.** If X is a Polish space and F ⊆ X is closed, then F = P ∪ A where P is perfect (possibly empty), A is countable and P ∩ A = ∅.
  *Proof:* Splits the set using its Cantor-Bendixson rank into a perfect remainder and a countable union of isolated points.
- **Corollary 1.28.** If X is a Polish space. and F ⊆ X is an uncountable closed set then F contains a nonempty perfect set and |F | = 2ℵ0 . Also, if Y ⊆ X is an uncountable Fσ -set, then Y contains a perfect set. In particular every uncountable Polish space has cardinality 2 ℵ0 .
  *Proof:* (immediate from Theorem 1.27)
- **Lemma 1.30.** If X is a Polish space and U ⊆ X is open, then U (with the subspace topology) is Polish.
  *Proof:* Defines a new equivalent complete metric that blows up near the boundary of the open set.
- **Corollary 1.31.** If X is a Polish space and Y ⊆ X is Gδ , then Y is a Polish space.
  *Proof:* Constructs a complete metric on the intersection by summing the bounded complete metrics of the constituent open sets.
- **Corollary 1.32.** If X is a Polish space and Y ⊆ X is an uncountable Gδ -set, then Y contains a perfect set.
  *Proof:* (immediate from Corollary 1.31)
- **Theorem 1.33.** If X is a Polish space, then Y ⊆ X is a Polish subspace if and only if Y is a Gδ -set.
  *Proof:* Characterizes the subspace as the intersection of sets of points that admit open neighborhoods with arbitrarily small diameters.
- **Corollary 1.34.** Every Polish space is homeomorphic to a Gδ -subset of H.
  *Proof:* (immediate from Theorem 1.33)
- **Theorem 1.35.** (Mod(L), τ0 ) and (Mod(L), τ1 ) are Polish spaces.
  *Proof:* Establishes a homeomorphism between the space of models and a closed or G_delta subset of a product space.
- **Lemma 1.37.** X is Gδ -subset of 2S .
  *Proof:* Expresses the consistency and Henkin conditions as countable intersections of open and closed sets.
- **Theorem 1.42.** If d is a complete metric on X, then dH is a complete metric on K(X). In particular, if X is a Polish space, then so is K(X).
  *Proof:* (no proof in this paper)
- **Lemma 2.3.** Suppose X and Y are topological spaces and f : X → Y . i) f is Borel measurable if and only if the inverse image of every open set is Borel. ii) If Y is separable, then f is Borel measurable if and only if the inverse image of every basic open set is Borel. iii) If Y is separable and f : X → Y is Borel measurable, then the graph of f is Borel.
  *Proof:* Shows that the collection of sets with Borel preimages forms a σ-algebra and writes the graph as an intersection of Borel sets.
- **Lemma 2.5.** Suppose X is metrizable. i) Σ0α ∪ Π0α ⊆ ∆0α+1 for all α < ω1 . ii) B(X) = S α<ω1 Σ0α . iii) If X is infinite, then |B(X)| = 2ℵ0 .
  *Proof:* Proceeds by transfinite induction and bounds the cardinality of Borel sets by bounding functions on countable ordinals.
- **Lemma 2.6.** i) Σ0α is closed under countable unions and finite intersections. ii) Π0α is closed under countable intersections and finite unions. iii) ∆0α is closed under finite unions, finite intersections and complement. iv) Σ0α , Π0α and ∆0α are closed under continuous inverse images.
  *Proof:* Uses simultaneous induction on the ordinals to show closure properties.
- **Corollary 2.7.** If A ⊆ X × Y is Σ0α (respectively Π0α or ∆0α ) and a ∈ Y , then {x ∈ X : (x, a) ∈ Y } is Σ0α .
  *Proof:* (immediate from Lemma 2.6)
- **Lemma 2.22.** Suppose X and Y are disjoint Polish spaces. The disjoint union X ] Y is the space X ∪ Y where U ⊆ X ∪ Y is open if and only if U ∩ X and U ∩ Y are both open. Then X ] Y is a Polish space.
  *Proof:* Defines a complete metric combining the components' metrics, bounded away from each other.
- **Lemma 2.23.** Let X be a Polish space with topology τ . Suppose F ⊆ X is closed. There is a Polish topology τ1 on X refining τ such that F is clopen in τ1 , and τ and τ1 have the same Borel sets.
  *Proof:* Forms the Polish disjoint union of the closed set and its open complement.
- **Theorem 2.24.** Let X be a Polish space with topology τ . Suppose A ⊆ X is Borel. There is a Polish topology τ ∗ on X such that A is clopen and τ ∗ has the same Borel sets as τ .
  *Proof:* Shows that the collection of Borel sets that can be made clopen is a σ-algebra using products of topologies.
- **Theorem 2.25.** (Perfect Set Theorem for Borel Sets) If X is a Polish space and B ⊆ X is an uncountable Borel set, then B contains a perfect set.
  *Proof:* Refines the topology to make the Borel set closed, applies the Cantor-Bendixson analysis, and reverts to the original topology.
- **Theorem 2.26.** If X is a Polish space and B ⊆ X is Borel, i) there is f : N → X continuous with f (N ) = B; ii) there is a closed F ⊆ N and g : F → X continuous and one-to-one with g(F ) = B;
  *Proof:* Refines the topology so the Borel set becomes closed, then uses the previously established mappings from Baire space.
- **Theorem 2.27.** If (X, τ ) is Polish, Y is separable and f : X → Y is Borel measurable, then we can refine τ to τ ∗ with the same Borel sets such that f is continuous.
  *Proof:* Refines the topology by making the Borel preimages of a countable basis open.
- **Corollary 2.32.** If X is a Polish space, there is a Borel A ⊆ C and a Borel isomorphism f : X → A.
  *Proof:* Embeds the space in the Hilbert cube and leverages the Borel isomorphism between the unit interval and Cantor space.
- **Lemma 2.33.** Suppose X and Y are Polish spaces, f : X → Y is a Borel isomorphism between X and f (X), and g : Y → X is a Borel isomorphism between Y and g(Y ). Then there is a Borel isomorphism between X and Y .
  *Proof:* Applies the classical Schröder-Bernstein construction tracking Borel components.
- **Corollary 2.34.** i) If X is a Polish space and A ⊆ X is an uncountable Borel set, then A is Borel isomorphic to C. ii) Any two uncountable Polish spaces are Borel isomorphic. iii) Any two uncountable standard Borel spaces are isomorphic.
  *Proof:* Refines the topology to make the set clopen, embeds it in the Cantor space, and uses the Perfect Set Theorem.
- **Lemma 2.37.** If X is a separable metric space, then for all 1 < α < ω1 there is a Σ0α -universal set Uα ⊆ C × X and a Π0α -universal set Vα ⊆ C × X.
  *Proof:* Constructs the universal sets iteratively through the Borel hierarchy by coding sequences of lower-level sets into Cantor space.
- **Corollary 2.38.** i) Σ0α (C) 6= Σ0α (C) for any α < ω1 . ii) If X is an uncountable Polish space, then Σ0α (X) 6= Σ0α (X) for any α < ω1 . In particular, Σ0α (X) is a proper subset of ∆0α+1 (X).
  *Proof:* Uses a diagonalization argument on the universal sets to show the hierarchy is strict.
- **Lemma 2.42.** If A ⊆ X is Γ-complete, then A 6∈ Γ̌.
  *Proof:* Assumes otherwise and uses Wadge-reducibility to show a set not in the dual class belongs to it.
- **Lemma 2.51.** If F is closed, then F \ intr(F ) is nowhere dense, where intr(F ) is the interior of F .
  *Proof:* Observes that any open set intersecting the boundary must contain a portion outside the closed set.
- **Theorem 2.52.** (Baire Category Theorem) If X is a Polish space, then X is nonmeager.
  *Proof:* Constructs a descending sequence of shrinking open balls avoiding nowhere dense sets to find a limit point in the space.
- **Lemma 2.56.** If A has the Baire property, then X \ A has the Baire property.
  *Proof:* Shows the complement equals modulo a meager set the interior of the complement of the corresponding open set.
- **Corollary 2.57.** BP is a σ-algebra containing the Borel sets.
  *Proof:* (no proof in this paper)
- **Theorem 3.9.** (Recursion Theorem) If f : N × N → N is total recursive, there is an e such that φe (n) = φf (n) for all n.
  *Proof:* Applies the Parameterization Lemma to construct a fixed-point index for the recursive function.
- **Lemma 3.11.** f : N → N is continuous if and only if there is z ∈ N such that f is computable from z.
  *Proof:* Relates the finite amount of oracle information needed to compute prefixes to topological continuity.
- **Lemma 3.14.** Σ01 = S x∈N Σ01 (x).
  *Proof:* (no proof in this paper)
- **Lemma 3.15.** i) A ⊆ X is Σ01 if and only if there is a recursively enumerable W ⊆ SX such that A = S η∈W Nη . In particular A ⊆ N is Σ01 if and only if A is recursively enumerable. ii) A ⊆ N is Σ01 if and only if there is a recursive S ⊆ N<ω such that A = S σ∈S Nσ .
  *Proof:* Characterizes recursively enumerable images and dynamically tracks halting computations to build recursive trees.
- **Lemma 3.17.** A ⊆ N is Π01 if and only if there is a recursive tree T ⊆ N<ω such that A = [T ].
  *Proof:* Prunes forbidden prefixes from a recursive set to construct the corresponding recursive tree.
- **Lemma 3.19.** i) Σ0n is closed under finite unions, finite intersections, and computable inverse images. ii) If A ⊆ N × X ∈ Σ0n , then {x ∈ X : ∃n (n, x) ∈ A} ∈ Σ0n . iii) If f : X → N is computable and A ⊆ N × X is Σ0n then {x ∈ X : ∀m < f (x) (m, x) ∈ A} ∈ Σ0n . iv) Similarly Π0n is closed under union, intersection, computable inverse images, ∀n and ∃n < f (x). v) Σ0n ⊆ ∆0n+1 .
  *Proof:* Shows the Σ01 case by explicitly manipulating recursive enumerations and halting stages, leaving the induction as an exercise.
- **Proposition 3.21.** i) There is U ⊆ N × X a Σ0n -set that is Σ0n -universal. ii) There is V ⊆ N × X a Σ0n -set that is Σ0n -universal.
  *Proof:* Defines universal sets explicitly using recursive enumerations of programs and proceeds inductively for higher levels.
- **Corollary 3.22.** For any X there is A ⊆ X such that A is Σ0n but not ∆0n .
  *Proof:* Diagonalizes the universal sets constructed in the previous proposition.
- **Lemma 4.2.** Let X be a Polish space. The following are equivalent: i) A ∈ Σ11 ; ii) either A = ∅ or there is f : N → X continuous such that f (N ) = X; iii) there is B ⊆ N × X closed, such that A = πX (B) iv) there is a Polish space Y and B ⊆ Y × X Borel such that A = π X (B).
  *Proof:* Links continuous images of Baire space through closed graph projections mapping bounded components.
- **Lemma 4.5.** i) Σ11 and Π11 are closed under countable unions and intersections. ii) If f : X → Y is Borel measurable, and A ∈ Σ11 (X), then f (A) ∈ Σ11 (Y ). iii) Σ11 and Π11 are closed under Borel measurable inverse images.
  *Proof:* Formulates infinite intersections uniformly embedding closed conditions over sequential variables mapped by graph projections.
- **Lemma 4.11.** There is U ∈ Σ11 (C × X) that is Σ11 -universal.
  *Proof:* Projects out a coordinate from a closed universal set to capture the analytic elements.
- **Corollary 4.12.** If X is an uncountable Polish space, then there is A ∈ Σ11 (X) that is not Π11 and hence not Borel.
  *Proof:* Uses a diagonalization argument on the analytic universal set over the embedded Cantor space.
- **Theorem 4.13.** (Σ11 -Separation Theorem) Suppose X is a Polish space and A, B ⊆ X are disjoint analytic sets. There is a Borel set C ⊆ X such that A ⊆ C and B ∩ C = ∅.
  *Proof:* Assumes failure to inductively build converging sequences over trees reaching limits whose neighborhoods are successfully separated, yielding a contradiction.
- **Corollary 4.14.** If A ∈ ∆11 (X), then A is Borel. Thus B(X) = ∆11 (X).
  *Proof:* Separates the disjoint analytic complement pairs resolving exclusively into a single Borel structure.
- **Corollary 4.15.** Suppose X and Y are Polish spaces and f : X → Y . The following are equivalent: i) f is Borel measurable; ii) the graph of f is a Borel subset of X × Y ; iii) the graph of f is an analytic subset of X × Y .
  *Proof:* Rewrites the pullback logically leveraging the single-valued graph condition under analytic assumptions.
- **Lemma 4.16.** Let X be a Polish space. If A ⊆ X is uncountable, then there are disjoint open sets U0 and U1 such that Ui ∩ A is uncountable for i = 0, 1.
  *Proof:* Employs a metric cover to bound the countable points unless the uncountable subsets branch disjointly.
- **Theorem 4.17.** (Perfect Set Theorem of Σ11 -sets) If X is a Polish space and A ⊆ X is analytic and uncountable, then X contains a perfect set.
  *Proof:* Constructs a branching Cantor tree iteratively applying uncountable branching within the separated open neighborhoods.
- **Theorem 4.18.** (Mansfield, Solovay) The following are equivalent: i) every uncountable Π11 -set contains a perfect subset; ii) for all x ⊆ N, ℵL(x) 1 is countable; iii) ℵV 1 is an inaccessible cardinal in L.
  *Proof:* (no proof in this paper)
- **Lemma 4.21.** Suppose A ⊆ X. There is B ⊇ A such that B has the Baire Property and if B 0 ⊇ A has the Baire Property, then B \ B 0 is meager.
  *Proof:* Forms a Baire envelope systematically excluding components with meager intersection against basic open covers.
- **Theorem 4.22.** Suppose Aσ has the Baire Property for all σ ∈ N<ω . Then A = A({Aσ }) has the Baire Property.
  *Proof:* Takes Baire envelopes recursively bounding sequence components intersecting paths modulo meager residual unions.
- **Corollary 4.23.** If X is a Polish space, then every Σ11 -set has the Baire Property.
  *Proof:* (immediate from Theorem 4.22)
- **Theorem 4.25.** The collection of Lebesgue measurable subsets of R n is closed under the Souslin operator. In particular every Σ11 -set is Lebesgue measurable.
  *Proof:* (no proof in this paper)
- **Lemma 4.32.** If R is a well-ordering of R of order type ω1 , then R is not Lebesgue measurable.
  *Proof:* Uses Fubini's Theorem on the well-ordering subsets to force a contradiction integrating null measure fibers.
- **Corollary 4.33.** If V = L, then there is a nonmeasurable ∆12 -set.
  *Proof:* (immediate from Lemma 4.32)
- **Theorem 4.34.** (Kuratowski-Ulam Theorem) If A has the Baire property, then A is nonmeager if and only if {a ∈ X : Aa is nonmeager} is nonmeager.
  *Proof:* (no proof in this paper)
- **Theorem 4.36.** (Solovay) If ZFC + ∃κ κ inaccessible is consistent then so is ZFC + every uncountable projective set contains a perfect subset + every projective set is Lebesgue measurable and has the property of Baire.
  *Proof:* (no proof in this paper)
- **Theorem 4.38.** i) The classes Σ1n and Π1n are closed under union, intersection, ∃n ∈ N, ∀n ∈ N and computable inverse images. ii) If A ⊆ X × N is arithmetic, then {x : ∃y(x, y) ∈ A} is Σ1n . iii) There is U ⊆ N × X a Σ1n -set that is Σ1n -universal. iv) There is V ⊆ N × X a Σ1n -set that is Σ1n -universal. v) Σ1n ⊂ ∆1n+1 , but Σ1n 6= ∆1n . vi) The set WF of wellfounded trees is Π11 .
  *Proof:* (no proof in this paper)
- **Theorem 5.3.** (Normal form for Π11 ) If A ⊆ N is Π11 , then there is a tree T ⊆ N<ω × N<ω such that x ∈ A if and only if T (x) ∈ WF.
  *Proof:* Analyzes the continuous map of trees to well-founded sets and applies completeness of ill-founded trees.
- **Corollary 5.4.** If A ∈ Π11 , then there is f : N → T r continuous such that A = f −1 (WF). In otherwords, WF is Π11 -complete. In particular WF is not Σ11 .
  *Proof:* (immediate from Theorem 5.3)
- **Lemma 5.6.** For any tree T there is an α < ω1 , such that T α = T β for all β > α.
  *Proof:* Observes the strict decrease of nodes at each step to bound the stabilization step below ω1.
- **Lemma 5.8.** Let T ⊆ N<ω be a tree and let ρ be the rank of T . i) Suppose σ, τ ∈ T and σ ⊂ τ . If ρ(τ ) = ∞, then ρ(σ) = ∞. If ρ(τ ) < ∞, then ρ(σ) > ρ(τ ). ii) If σ ∈ T and ρ(τ ) < ∞ for all τ ∈ T with σ ⊂ τ , then ρ(σ) = sup{ρ(σbi) + 1 : σbi ∈ T }. iii) If ρ(σ) = ∞, then there is f ∈ [T ] ∩ Nσ ; iv) T is well-founded if and only if ρ(T ) < ∞.
  *Proof:* Checks structural properties of tree ranks under inclusion, extension, and limits to characterize well-foundedness.
- **Lemma 5.11.** i) If S, T ⊆ N<ω are trees, then ρ(S) ≤ ρ(T ) if and only if there is an order preserving f : S → T . ii) If T is a well-founded tree, then ρ(S) < ρ(T ) if and only if S = ∅ and T 6= ∅ or there is n ∈ N and f : S → Thni order preserving.
  *Proof:* Defines order-preserving maps inductively using rank boundaries and recursively matches branches.
- **Lemma 5.12.** WFα is Borel.
  *Proof:* Expresses bounded rank properties using countable intersections of Borel conditions inductively.
- **Theorem 5.13.** If A ∈ Π11 , then A is the union of ℵ1 -Borel sets.
  *Proof:* Expresses the subset using a continuous map's inverse image over all bounded well-founded tree classes.
- **Corollary 5.14.** If A ∈ Π11 and |A| > ℵ1 , then A contains a perfect set. In particular, |A| ≤ ℵ1 or |A| = 2ℵ0 .
  *Proof:* (immediate from Theorem 5.13)
- **Lemma 5.15.** i) The set {(S, T ) : ρ(S) ≤ ρ(T )} is Σ11 . ii) There is R ∈ Σ11 (N × N ) such that if T ∈ WF, then {S : (S, T ) ∈ R} = {S : ρ(S) < ρ(T )}.
  *Proof:* Projects the existence of order-preserving maps to characterize rank comparisons.
- **Corollary 5.16.** (Σ11 -Bounding) Suppose A ⊆ WF is Σ11 . Then there is α < ω1 such that A ⊆ WFα .
  *Proof:* Assumes otherwise and uses the definition of well-founded subsets to contradict the complexity class.
- **Theorem 5.20.** Π11 has the reduction property.
  *Proof:* Splits two coanalytic sets by comparing the ranks of their tree maps.
- **Lemma 5.22.** If Γ̌ has the reduction property, then Γ has the separation property.
  *Proof:* Uses the reduction property of the dual class to partition the complement space and separate the original sets.
- **Proposition 5.23.** Π11 does not have the separation property.
  *Proof:* Diagonalizes a universal set to show that a presumed Borel separator yields a contradiction.
- **Proposition 5.26.** There is a closed set C ⊆ N ×N that can not be uniformized by a Σ11 -set.
  *Proof:* Uses the failure of Borel separation to contradict the existence of an analytic uniformization.
- **Theorem 5.27.** (Kriesel’s Uniformization Theorem) Every Π11 subset of N × N can be uniformized by a Π11 -set.
  *Proof:* Selects the minimal rank mapping for elements to single out a unique branch, constructing a uniformization.
- **Corollary 5.28.** (Selection) Suppose A ⊆ X × N is Π 11 and π(A) is Borel. Then A has a Borel-uniformization.
  *Proof:* Expresses the complement of the uniformized set logically to establish Borel status.
- **Theorem 5.29.** (Kondo’s Theorem) Π11 has the uniformization property.
  *Proof:* Constructs a sequence of finer uniformizing slices by iteratively selecting lexicographically minimal nodes and minimum ranks.
- **Corollary 5.30.** Σ12 has the uniformization property.
  *Proof:* Pulls back the uniformization property from the previously established coanalytic uniformization.
- **Theorem 5.34.** i) If A ⊆ X is Π11 , there is a computable f : X → T r such that x ∈ A if and only if f (x) ∈ WF for all x ∈ X. ii) Π11 has the reduction property. iii) Any two disjoint Σ11 sets can be separated by a ∆11 -set. iv) Any Π11 -subset of N × N can be uniformized by a Π11 -set. v) If A ⊆ N × N is Π11 and π(A) = N , then A has a ∆11 -uniformization.
  *Proof:* (no proof in this paper)
- **Proposition 5.35.** O is Π11 -complete.
  *Proof:* Reduces analytic complete sets to ill-founded recursive trees via a computable mapping.
- **Lemma 5.36.** Suppose T ⊆ N<ω is a recursive tree. If [T ] 6= ∅, there is x ∈ [T ] with x ≤T O.
  *Proof:* Builds a path by iteratively selecting extensions that do not fall into the recursive tree well-order.
- **Corollary 5.37.** (Kleene Basis Theorem) If A ⊆ N is Σ11 and nonempty, there is x ∈ A with x ≤T O.
  *Proof:* Selects a base element using the computable reduction of a closed set to recursive trees.
- **Proposition 5.38.** If A ⊆ N is Π11 , there is x ∈ A such that x ∈ ∆12 .
  *Proof:* Uniformizes the singleton slice of the set and writes definitions characterizing its coordinates.
- **Lemma 5.40.** a) If α is a recursive ordinal and β < α, then β is a recursive ordinal. b) If α is a recursive ordinal, then α + 1 is a recursive ordinal. c) Suppose f : N → N, g : N → N are recursive functions such that Pf (n) is a program to compute the characteristic function of An , Pg(n) is a program that computes the characterisitic function of ≺n a well-order of An and (An , ≺n ) has order-type αn . Then sup αn is a recursive ordinal.
  *Proof:* Constructs a recursive linear sum of the well-orders to bound the recursive ordinals.
- **Theorem 5.44.** i) The set {(S, T ) : ρ(S) ≤ ρ(T )} is Σ11 . ii) There is R ∈ Σ11 (N × N ) such that if T ∈ WF, then {S : (S, T ) ∈ R} = {S : ρ(S) < ρ(T )}.
  *Proof:* (no proof in this paper)
- **Corollary 5.45.** (Effective Σ11 -Bounding) i) If A ⊆ O is Σ11 , then there is α < ω1ck such that ρ(T ) < α for all T ∈ A. ii) If A ⊆ WF and A ∈ Σ11 . Then ρ(T ) < ω1ck for all T ∈ A.
  *Proof:* Assumes otherwise and bounds the ranks to contradict the complexity class of recursive sets.
- **Theorem 6.4.** (Gale-Stewart Theorem) If A ⊆ X N is closed, then G(A) is determined.
  *Proof:* Considers games restricted to even sequences to identify a winning strategy for Player I by avoiding losing positions.
- **Theorem 6.9.** (Borel Determinacy) If A ⊆ N is Borel, then G(A) is determined.
  *Proof:* (no proof in this paper)
- **Theorem 6.11.** (Martin/Harrington) i) If there is a measurable cardinal, then Det(Σ11 ) holds. ii) Det(Σ11 ) holds if and only if x# exists for all x ∈ N .
  *Proof:* (no proof in this paper)
- **Proposition 6.12.** If Player I has a winning strategy in G∗ (A), then A contains a perfect set.
  *Proof:* Constructs a continuous one-to-one embedding mapping Cantor space directly into the winning plays.
- **Proposition 6.13.** If Player II has a winning strategy in G∗ (A), then A is countable.
  *Proof:* Identifies unique rejection positions in the game tree to bound the set's size to countable.
- **Corollary 6.14.** If A is uncountable and G∗ (A) is determined, then A contains a perfect set.
  *Proof:* (immediate from Propositions 6.12 and 6.13)
- **Corollary 6.16.** If PD holds, the any uncountable projective set contains a perfect subset.
  *Proof:* (immediate from Corollary 6.14)
- **Lemma 6.17.** If Player I has a winning strategy in G∗u (A), then A contains a perfect subset.
  *Proof:* Unfolds the game to construct a continuous one-to-one mapping into a closed uncountable set.
- **Lemma 6.18.** If Player II has a winning strategy in G∗u (A), then A is countable.
  *Proof:* Determines unique rejection positions over bounded sequences to prove the set is countable.
- **Lemma 6.19.** Player II has a winning strategy in G∗∗ (A) if and only if A is meager.
  *Proof:* Explicitly constructs responses avoiding nowhere dense sets to win, or uses rejection boundaries to cover the set with meager pieces.
- **Lemma 6.20.** If Player I has a winning strategy in G∗∗ (A), then there is η ∈ N<ω such that Nη \ A is meager.
  *Proof:* Transforms Player I's winning strategy into a counter-strategy for the complement game to establish meagerness.
- **Theorem 6.21.** Assuming Projective Determinacy all projective sets have the Baire property.
  *Proof:* Uses the existence of a winning strategy or its absence to write the set modulo meager pieces as open or meager.
- **Theorem 6.23.** (Periodicity Theorems) Assume Projective Determinacy. a) The classes with the reduction property are exactly Π 12n+1 and Σ12n+2 . b) The classes with the uniformization property are exactly Π 12n+1 and Σ12n+2 .
  *Proof:* (no proof in this paper)
- **Lemma 6.24.** a) If A and B are Borel, then Gw (A, B) is determined. b) Assuming Projective Determinacy if A and B are Projective, then Gw (A, B) is determined. c) If Player II has a winning strategy in Gw (A, B), then A ≤w B. d) If Player I has a winning strategy in Gw (A, B), then B ≤w (N \ A).
  *Proof:* Translates winning strategies directly into Wadge reductions between the sets.
- **Corollary 6.25.** If A ∈ Σ0α \ ∆0α , then A is Σ0α -complete.
  *Proof:* Applies determinacy and Wadge reductions to deduce completeness.
- **Theorem 6.27.** (Wadge, Martin) There is no infinite sequence of Borel sets A0 , A1 . . . with Ai+1 <w Ai for all i. Similarly under Projective Determinacy, there is no infinite descending Wadge-chain of projective sets.
  *Proof:* (no proof in this paper)
- **Theorem 6.29.** (Solovay) If ZF + AD then ℵ1 and ℵ2 are measurable cardinals, while ℵn is singular of cofinality ω for 3 ≤ n < ω.
  *Proof:* (no proof in this paper)
- **Lemma 7.4.** There are R ∈ Σ11 and S ∈ Π11 such that if x ∈ BC then y ∈ B(x) ⇔ (x, y) ∈ R ⇔ (x, y) ∈ S. In particular B(x) ∈ ∆11 (x).
  *Proof:* Constructs an arithmetic relation using characteristic functions verifying tree branches to validate Borel codes.
- **Corollary 7.5.** If x ∈ BC is recursive, then B(x) is ∆11 .
  *Proof:* Validates conditions over fixed recursive indices to place the result in the corresponding complexity classes.
- **Theorem 7.6.** If A ⊆ Y is a recursively coded Borel set and f : X → Y is computable, then f −1 (A) is a recursively coded Borel set.
  *Proof:* (no proof in this paper)
- **Proposition 7.7.** If α < ω1ck , then WFα is a recursively coded Borel set.
  *Proof:* (no proof in this paper)
- **Corollary 7.8.** Suppose A ⊆ X. The following are equivalent: i) A is ∆11 ; ii) A is a recursively coded Borel set.
  *Proof:* Applies bounding to the continuous mapping of trees and pulls back recursively coded classes.
- **Lemma 7.9.** There is a recursive function F : N × SY → N such that if f : X → Y is computable and e is a code for the program computing f , then Brec (F (e, i)) = f −1 (Nη ).
  *Proof:* Constructs a recursive function bounding the computable tree to map basic open sets into Borel codes.
- **Lemma 7.10.** i) There is a total recursive function Hc : N → N such that if e ∈ BC, then Brec (Hc (e)) = N \ Brec (e). ii) There is a total recursive function Hu : N → N such that if φe (n) ∈ BCrec for all n, then Brec (Hu (e)) = S n Brec (φe (n)).
  *Proof:* Uses explicit tree constructions mapping prefixes to negation and union structures for Borel codes.
- **Lemma 7.11.** If x = hT, li is a recursive Borel code, there is a recursive function G : N × T → N such that if f : N → N is a computed by program Pe , then G(e, σ) ∈ BCrec is a Borel code for f −1 (B(hTσ , lσ i) for all σ ∈ T .
  *Proof:* Uses the Recursion Theorem to construct a mapping matching branches to their recursively computed inverse images.
- **Lemma 7.12.** If T is a recursive well founded tree, then there is a recursive function G : T → BCrec , such that Brec (G(σ)) = {S ∈ T r : ρ(S) ≤ ρ(Tσ )}.
  *Proof:* Applies the Recursion Theorem across computable ranks to output Borel codes of subtrees.
- **Lemma 7.15.** i) {(x, y) : x ≤hyp y} is Π11 . In particular, {x : x ∈ ∆11 } is Π11 .
  *Proof:* Writes the explicit relation matching Borel evaluations to hyperarithmetic constraints.
- **Theorem 7.16.** Suppose A ⊆ N × N is Π11 . Then B = {x : ∃y ≤hyp x (x, y) ∈ A} is Π11 .
  *Proof:* Restricts quantification to hyperarithmetic slices by explicitly substituting recursive codes.
- **Lemma 7.17.** If ω1ck < ω1x , then O ≤hyp x.
  *Proof:* Evaluates the rank over the recursive components to establish hyperarithmetic status.
- **Theorem 7.18.** (Gandy’s Basis Theorem) If A ⊆ N is Σ11 and nonempty, there is x ∈ A such that x ≤T O, x <hyp O and ω1ck = ω1x .
  *Proof:* Uses uniformization and boundedness to identify minimal complexity bounds on elements.
- **Theorem 7.19.** (Harrison) Let A ⊆ N be Σ11 . If A is countable, then every element of A is hyperarithmetic. In particular, if A contains a nonhyperarithmetic element, then A contains a perfect set.
  *Proof:* (no proof in this paper)
- **Corollary 7.20.** Suppose A ⊆ N × N is ∆11 and {y : (x, y) ∈ A} is countable for all x ∈ N . Then i) the projection π(A) = {x : ∃y (x, y) ∈ A} is ∆11 and ii) A has a ∆11 -uniformization
  *Proof:* Uses uniformization logic over hyperarithmetic bounds to restrict and select projection witnesses.
- **Corollary 7.21.** Suppose A ⊆ N × N is a Borel set such that every section is countable. Then X the projection of X is Borel and X can be uniformized by a Borel set.
  *Proof:* (no proof in this paper)
- **Corollary 7.22.** Suppose f : N → N is continuous, A is Borel and f |A is one-to-one. Then f (A) is Borel.
  *Proof:* Projects singleton sections over Borel functions using uniformization.
- **Theorem 7.23.** If Player II has a winning strategy in G(A), then Player II has a hyperarithmetic winning strategy.
  *Proof:* Applies selection to construct a computable counter-strategy bounding winning segments over recursive trees.
- **Theorem 7.26.** Suppose A ⊆ N × N is a Borel set with countable sections. Then there are Borel measurable functions f0 , f1 , . . . with disjoint graphs such that A is the union of the graphs.
  *Proof:* Uses uniformization across hyperarithmetic mappings to systematically extract disjoint Borel graph cross-sections.
- **Lemma 7.27.** Suppose A is a ∆11 -subset of HYP. There is a hyperarithmetic x ∈ NN such that A ⊆ {x0 , x1 , . . .}.
  *Proof:* Leverages the hyperarithmetic subset constraint to selectively map finite branches to bounded indices.
- **Lemma 7.29.** Suppose A ⊆ N is ∆11 and open. Then there is a hyperarithmetic S ⊆ N<ω such that A = S σ∈S Nσ .
  *Proof:* Analyzes the well-founded bounds on prefixes to identify a hyperarithmetic restriction of paths.
- **Lemma 7.30.** If A is ∆11 and compact, then there is a finite branching hyperarithmetic tree T such that A = [T ]. More generally, if A is a compact Σ 11 -set, F is a closed ∆11 -set, and A ⊆ F , then there is a finite branching hyperarithmetic tree T such that A ⊆ [T ] ⊆ F .
  *Proof:* Trims trees sequentially to finite branching subsets avoiding empty topological intersections.
- **Corollary 7.31.** If A ⊆ N is ∆11 , compact and nonempty, then there is x ∈ A such that x ∈ HYP.
  *Proof:* Selects minimal valid paths using König's Lemma over the finite branching tree.
- **Corollary 7.32.** (Novikov) If A ⊆ N × N is ∆11 and all sections Ax = {y : (x, y) ∈ A} are compact, then π(A) is ∆11 and there is a ∆11 uniformization of X. In particular, any Borel A ⊆ N × N with compact sections has a Borel uniformization.
  *Proof:* Uniformizes the projection slice using bounds on recursive indices avoiding the invalid branches.
- **Lemma 7.35.** Suppose A is ∆11 and a Kσ -set. Then there is x ∈ A ∩ HYP.
  *Proof:* Restricts the compact projections logically to refine the branching tree and extract hyperarithmetic witnesses.
- **Corollary 7.36.** (Aresenin, Kunugui) If A ⊆ N × N is Borel and every section if Kσ , then π(A) is Borel and A has a Borel uniformization.
  *Proof:* (no proof in this paper)
- **Theorem 8.1.** (Silver’s Theorem) If X is a Polish space and E is a Π 11 -equivalence relation with uncountably many classes, then there is a nonempty perfect set P of inequivalent elements. In particular, if there are uncountably many classes, then there are 2ℵ0 classes.
  *Proof:* (no proof in this paper)
- **Proposition 8.2.** Suppose E is an equivalence relation on N and there is a nonempty open set U such that E ∩(U ×U ) is meager. Then there is a nonempty perfect set P of E-inequivalent elements.
  *Proof:* Constructs a descending array of clopen sets avoiding nowhere dense components to form a perfect set.
- **Proposition 8.4.** If U ⊆ N is nonempty ant τG -open, then U is not τG -meager.
  *Proof:* Builds a sequence of nested generic neighborhoods iteratively avoiding nowhere dense sets without reaching empty sets.
- **Lemma 8.6.** If A is τG 1,1 -nowhere dense, then A∗ is τG 2,1 -nowhere dense.
  *Proof:* Refines the product neighborhood boundaries to demonstrate density across extended components.
- **Lemma 8.7.** If x 6∈ U , then there is an E-small ∆11 -set A with x ∈ A.
  *Proof:* Applies separation bounds on small classes to construct a tight definable subset.
- **Corollary 8.8.** U is Σ11 .
  *Proof:* Translates the smallness conditions directly into logical evaluations bounding indices.
- **Lemma 8.9.** E ∩ (U × U ) is τG 1,1 -meager.
  *Proof:* Applies product category theorem metrics over Gandy subsets to identify meager boundaries.
- **Theorem 8.12.** (Burgess’ Theorem) If X is a Polish space and E is a Σ 11 -equivalence relation with at least ℵ2 equivalence classes, then there is a perfect set of inequivalent elements.
  *Proof:* (no proof in this paper)
- **Lemma 8.13.** A is a closed unbounded subset of ω1 .
  *Proof:* Analyzes equivalence components bounding tree ranks sequentially to capture limits.
- **Corollary 8.14.** If E is a Σ11 -equivalence relation, there is a sequence (Eα : α < ω1 ) of Borel equivalence relations such that: i) Eα ⊇ Eβ for α < β; ii) Eα = T β<α Eβ , for α a limit ordinal; iii) E = T α<ω1 Eα .
  *Proof:* Uses the unbounded bounds on limit mappings to align the target sequences.
- **Lemma 8.15.** Suppose A ⊆ N contains at least ℵ2 E-classes. Then there is α < ω1 and a ∈ A such that {x ∈ A : xEα a} and {x ∈ A : x 6 Eα a} each contain at least ℵ2 elements. In particular there is b ∈ A such that b 6 E a and {x ∈ A : x 6 Eα b} also contains at least ℵ2 E-classes
  *Proof:* Extracts an unbalanced component sequentially to verify that class subdivisions preserve density.
- **Corollary 8.16.** (Morley’s Theorem) If L is a countable language and T is an L-theory such that I(T, ℵ0 ) > ℵ1 , then I(T, ℵ0 ) = 2ℵ0 . Indeed if φ is an Lω1 ,ω -sentence and I(φ, ℵ0 ) > ℵ1 , then I(φ, ℵ0 ) = 2ℵ0 .
  *Proof:* (no proof in this paper)
- **Proposition 8.18.** If M a countable L-structure, there is α < ω1 such that if N is countable and M ∼α N , then M and N are isomorphic.
  *Proof:* (no proof in this paper)
- **Lemma 9.2.** Let E be a Borel equivalence relation on a Polish space X. Then E has a Borel transversal if and only if E has a Borel-measurable selector.
  *Proof:* Constructs the selector by mapping variables to intersecting transversal elements directly.
- **Proposition 9.5.** If E is a Borel equivalence relation on X, then E is tame if and only if there is a Borel measurable f : X → C such that xEy if and only if f (x) = f (y).
  *Proof:* Uses binary components mapped from separating families to extract point-separating measures.
- **Proposition 9.8.** Suppose E is a Borel equivalence relation on a Polish space X such that every E-class is Kσ . Then E is tame if and only if E has a Borel transversal. In particular this is true if every E-class is countable.
  *Proof:* Uses section uniformizations over compact elements to construct a Borel reduction transversal.
- **Proposition 9.9.** If E is a tame Borel equivalence relation on X, then E has a C-measurable transversal.
  *Proof:* Pulls back the target invariant mappings across the Souslin operator structure.
- **Lemma 9.14.** If E is a tame Borel equivalence relation, then there is no E-ergodic, nonatomic Borel probability measure on X. Indeed, if µ is an E-ergodic, nonatomic Borel probability measure on X, then E is not µ-tame.
  *Proof:* Contradicts the measure condition by separating components strictly into invariant measure bounds.
- **Lemma 9.15.** (Zero-one law for tail events) Let µ be the usual Lebesgue measure on C. If A ⊆ C is E0 -invariant, then µ(A) = 0 or µ(A) = 1.
  *Proof:* Applies independent measures across prefix matrices to force probability limits strictly.
- **Corollary 9.16.** E0 is not tame.
  *Proof:* Uses the tail events invariant distribution to deduce non-tame structure directly.
- **Theorem 9.17.** (Glimm–Effros Dichotomy) Suppose E is a Borel equivalence relation on a Polish space X. Then either i) E is tame or ii) E0 ≤B E.
  *Proof:* (no proof in this paper)
- **Corollary 9.18.** Let E be a Borel equivalence relation on a Polish space X. The following are equivalent: i) E is tame; ii) E has a C-measurable transversal; iii) There is no Borel probability measure µ that is E-ergodic and nonatomic. iv) E0 6≤B E.
  *Proof:* Restricts invariant measures across Borel reductions to map non-tame boundaries into density contradictions.
- **Theorem 10.4.** (Feldman–Moore) If E is a countable Borel equivalence relation on a Borel set X, then there is a countable group G and a Borel action of E on X such that E is the orbit equivalence relation.
  *Proof:* Builds cyclic step permutations over disjoint graph relations systematically covering the space.
- **Lemma 10.6.** Suppose G is a countable group acting on a Borel set X. Let E G be the orbit equivalence relation. Then EG ≤B E(G, C).
  *Proof:* Injects equivalence orbits systematically across the product sets to embed the relations.
- **Lemma 10.7.** Suppose G and H are countable groups and ρ : G → H is a surjective homomorphism then E(H, X) ≤B E(G, X) for any Borel X.
  *Proof:* Embeds maps injectively mapping relations via structural quotients to boundary spaces.
- **Corollary 10.8.** If E is a countable Borel equivalence relation, then E ≤ B E(Fℵ0 , C).
  *Proof:* Combines the discrete group extensions mapping into the product structures.
- **Lemma 10.9.** If G is a countable group and H ⊆ G, then E(H, X) ≤ B E(G, X) for any Borel X.
  *Proof:* Pads unmapped spaces with constants mapping into boundaries to preserve the target equivalences.
- **Lemma 10.10.** If G is a countable group, then E(G, C) ≤B E(G × Z, 2).
  *Proof:* Embeds components mapping sequentially over shifted indices validating equivalence boundaries.
- **Theorem 10.11.** If E is a countable Borel equivalence relation, then E ≤B E(F2 , 2).
  *Proof:* Chains reductions sequentially embedding the boundaries directly into the free product.
- **Theorem 11.2.** Let E be a countable Borel equivalence relation. The following are equivalent: i) E is hyperfinite; ii) E is the orbit equivalence relation for a Borel action of Z; iii) E ≤B E0 .
  *Proof:* (no proof in this paper)
- **Proposition 11.3.** If E is a finite Borel equivalence relation, then E is tame.
  *Proof:* Uses a selector over maximum components to force finite subsets directly.
- **Proposition 11.4.** If E is tame countable Borel equivalence relation, then E is hyperfinite.
  *Proof:* Builds localized mappings bounded by the selector indices to form finite equivalence relations.
- **Theorem 11.5.** Let E be a countable Borel equivalence relation, then E is hyperfinite if and only if there are tame Borel equivalence relations E 0 ⊆ E1 ⊆ E2 ⊆ . . . with E = S n En .
  *Proof:* (no proof in this paper)
- **Proposition 11.7.** i) If E ⊆ F and F is hyperfinite, then E is hyperfinite. ii) If E is hyperfinite and A ⊆ X is Borel, then E|A is hyperfinite. iii) If E is a countable Borel equivalence relation, A ⊆ X is Borel and full for E, and E|A is hyperfinite, then A is hyperfinite. iv) If E is a countable Borel equivalence relation, E ≤ B E ∗ and E ∗ is hyperfinite, then E is hyperfinite.
  *Proof:* Transfers the hyperfinite structure through bounding components directly to embedded segments.
- **Theorem 11.8.** Let E be a Borel equivalence relation on X. The following are equivalent: i) E is hyperfinite; ii) There is a Borel [x] 7→<[x] such that each infinite E-class has order type Z, ω or ω ∗ . iii) There is a Borel [x] 7→<[x] such that each infinite E-class has order type Z. iv) There is a Borel action of Z on X such that E is the orbit equivalence relation. v) There is a Borel automorphism T : X → X such that E-equivalence classes are T -orbits.
  *Proof:* Inductively links bounded cyclic components over orbits to structure discrete linear orders.
- **Corollary 11.9.** If E is a hyperfinite Borel equivalence relation, then E ≤B E(Z, C).
  *Proof:* (no proof in this paper)
- **Corollary 11.10.** If E is a hyperfinite equivalence relation on a standard Borel space X and every E class if infinite, then E is the orbit equivalence relation for a free Borel action of Z on X.
  *Proof:* (no proof in this paper)
- **Theorem 11.11.** (Doughrety-Jackson-Kechris) If E is a hyperfinite Borel equivalence relation, then E ≤B E0 .
  *Proof:* Reduces to sequences discarding tame sets, isolating occurrences via shifting markers embedded in finite matrices.
- **Corollary 11.12.** If E is a nontame hyperfinite Borel equivalence relation then E ≡ B E0 .
  *Proof:* Chains reductions via the dichotomy theorem directly embedding bounding elements.
- **Lemma 11.13.** Suppose X ⊆ C Z is tame, and f : C Z \ X → C is a Borel reduction of E|Y to E0 . Then E ≤B E0 .
  *Proof:* Extracts invariant components linking the discrete spaces directly bounding tame elements.
- **Lemma 11.14.** If X0 , X1 , . . . , ⊆ C Z are tame, then S Xn is tame.
  *Proof:* Unions the discrete parts systematically avoiding the invariant boundaries directly.
- **Theorem 11.16.** (Gromov) Suppose G is a finitely generated group. Then G is of polynomial growth if and only if G is nilpotent-by-finite.
  *Proof:* (no proof in this paper)
- **Lemma 11.18.** If G is a finitely generated group of polynomial growth O(n d ), then G has the mild growth property of order 16d + 1.
  *Proof:* Checks bounds sequentially over structural products scaling bounds uniformly over finite subsets.
- **Lemma 11.19.** Suppose G0 ⊂ G1 ⊂ G2 ⊂ S . . . are finitely generated groups with the mild growth property of order c. Then Gi has the mild growth property of order c.
  *Proof:* Rebounds nested sequences bounding limits mapping strictly inside cyclic finite boundaries.
- **Theorem 11.20.** (Jackson-Kechris-Louveau) Let G be a countable group with the mild growth property. If E is the orbit equivalence relation for a Borel action of G on a Borel space X, then E is hyperfinite.
  *Proof:* (no proof in this paper)
- **Lemma 11.22.** Let F be a locally finite, symmetric, reflexive Borel binary relation on X. Then there is a maximal F -discrete Y ⊆ X.
  *Proof:* Extracts disjoint bounds over locally bounded subcomponents capturing discrete limits.
- **Lemma 11.24.** If G is a group with the mild growth property and E is the orbit equivalence relation for a Borel action of G, then there are locally finite, symmetric, reflexive Borel binary relations F0 ⊆ F1 ⊆ . . . satisfying the Weiss condition such that E = S Fi .
  *Proof:* Validates bounds symmetrically across restricted finite components checking cyclic inverse boundaries.
- **Lemma 11.25.** Lemma 11.25 Su
  *Proof:* (no proof in this paper)
```