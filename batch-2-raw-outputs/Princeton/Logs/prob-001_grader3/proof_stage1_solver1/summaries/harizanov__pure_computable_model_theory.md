<!-- Generated 2026-05-31T02:08:53 -->
<!-- Source PDF: harizanov__pure_computable_model_theory.pdf (576612 bytes) -->
<!-- Citation: V. S. Harizanov (1998). Pure computable model theory. Handbook of Recursive Mathematics, Vol. 1 (Elsevier). -->

# V. S. Harizanov (1998). Pure computable model theory. Handbook of Recursive Mathematics, Vol. 1 (Elsevier).

## Definitions
- **Definition 1.** The degree spectrum of a structure A is DgSp(A) = {deg(D(B)) : B ∼= A},
- **Definition 2 ([296]).** If the degree spectrum of a structure A has a least element, then this element is called the degree of the isomorphism type of A.
- **Definition 3 ([296]).** Let A be a structure, and α a computable ordinal. We say that a Turing degree d is the α th jump degree of A if it is the least degree in {d(α) : d ∈ DgSp(A)}. The degree d is said to be proper α th jump degree of A if for every computable ordinal â < α, the structure A has no â th jump degree.
- **Definition 4 ([186]).** An automorphically nontrivial structure M is called almost computable if the measure of DgSp(M) is equal to 1 under the standard Lebesgue measure on the Cantor space.
- **Definition 5 ([237]).** A mass problem is a collection of total functions from ù to ù.
- **Definition 6 ([324]).** (i) The mass problem of a countable structure A is the set {÷D(B) : B ∼= A}. (ii) Given countable structures A and B, we say that A is Muchnik reducible to B, in symbols A ≤w B, if DgSp(A) ⊆ DgSp(B).
- **Definition 7 ([258]).** Given a language L, let {èi : i ∈ ù} be a computable enumeration of all computable infinitary Σ1 formulas in L. Given a structure A for L, let A′ be the structure obtained by adding to A infinitely many relations Pi , for i ∈ ù, where A |= Pi (x) ⇔ èi (x), and the arity of Pi is the same as the length of x in èi (x).
- **Definition 8 ([196]).** A total function F : ù → ù is limitwise monotonic if there is a computable function f: ù 2 → ù such that for all i, s ∈ ù, we have f(i, s) ≤ f(i, s + 1), the limit lim s→∞ f(i, s) exists, and F (i) = lim s→∞ f(i, s).
- **Definition 9 ([219]).** 1. A countable structure A has a d-basis if the types realized in A are all computable and the Turing degree d can list ∆00 -indices for all types realized in A. 2. A Turing degree c is 0-basis homogeneous bounding if for every automorphically nontrivial homogeneous model A with a 0-basis, there exists B such that B ∼= A and B is c-decidable.
- **Definition 10.** Let κ be a cardinal. A theory is called κ-categorical if it has exactly one model of cardinality κ, up to isomorphism.
- **Definition 11.** A theory is called Ehrenfeucht if it has finitely many but more than one countable models, up to isomorphism.
- **Definition 12 ([203]).** Let T be an uncountably categorical theory with Baldwin–Lachlan elementary chain of countable models: A0 A1 A2 · · · Aù . The spectrum of computable models of the theory T is the set: SCM(T ) = {i ≤ ù : Ai has a computable isomorphic copy}.
- **Definition 13.** (i) A complete theory T is strongly minimal if any definable subset of any model M of T is finite or co-finite. A structure M is strongly minimal if it has a strongly minimal theory. (ii) A strongly minimal model M is trivial if for all subsets A ⊆ M , acl (A) = S a∈A acl ({a}).
- **Definition 14.** A computable structure M is d-computably categorical if for every computable structure A isomorphic to M, there exists a d-computable isomorphism from M onto A.
- **Definition 15.** A computable structure M is relatively ∆0α -categorical if for every A isomorphic to M, there is an isomorphism from M to A, which is ∆0α relative to the atomic diagram of A.
- **Definition 16.** The d-computable dimension of a computable structure M is the number of computable isomorphic copies of M, up to d-computable isomorphism.
- **Definition 17 ([103]).** (i) The categoricity spectrum of A is CatSpec(A) = {x : A is x-computably categorical}. (ii) A Turing degree d is the degree of categoricity of A, if it exists, if d is the least degree in CatSpec(A). (iii) A Turing degree d is categorically definable if it is the degree of categoricity of some computable structure.
- **Definition 18.** A decidable structure A is called decidably categorical if every two decidable copies of A are computably isomorphic.
- **Definition 19.** For an infinite computable structure M (with domain ù) and a Turing degree d, we define Autd (M) to be the set of all permutations of ù, which are computable in d and induce automorphisms of M.
- **Definition 20 ([150]).** The automorphism (Turing) degree spectrum of a computable structure M, in symbols AutSp(M), is the set {deg(f) : f ∈ Aut(M) − {1M }}, where 1M is the identity automorphism of M.
- **Definition 21 ([19]).** An additional relation R on the domain of a computable structure A is called intrinsically P on A if the image of R under every isomorphism from A to a computable structure belongs to P.
- **Definition 22.** An additional relation R on the domain of a computable structure A is called relatively intrinsically P on A if the image of R under every isomorphism from A to any structure B is P relative to the atomic diagram of B.
- **Definition 23 ([151]).** The Turing degree spectrum of R on A, in symbols DgSpA (R), is the set of all Turing degrees of the images of R under all isomorphisms from A onto computable structures.
- **Definition 24 ([16]).** (i) A ≤∆0α B iff A ≤T B ⊕ ∆0α . (ii) A ≡∆0α B iff (A ≤∆0α B and B ≤∆0α A). (iii) The equivalence classes under ≡∆0α are called α-degrees.
- **Definition 25 ([70]).** Given a family of relations R on a computable structure M, define DgSp(R) = {deg(R) : R ∈ R}.
- **Definition 26.** Let A be a computable structure, and let R = (Ri )i∈I be a family of relations on A, where l (i) is the arity of Ri . Define DgSp(R; A) = deg{a ⊆ Al (i) : A |= Ri (a), i ∈ I }.
- **Definition 27.** (i) An enumeration of K c /E is a sequence (Mn )n∈ù representing all E-equivalence classes in K c . (ii) A Friedberg enumeration of K c /E is an enumeration in which every E-equivalence class is represented only once. (iii) An enumeration is ∆0α -computable if there is a ∆0α -computable sequence of computable indices for the structures.
- **Definition 28.** For equivalence relations E1 , E2 on (hyperarithmetic subsets of) ù, we say that E1 is h-reducible to E2 , in symbols E1 ≤h E2 , if there is a hyperarithmetic function f such that for all x, y, x E1 y ⇔ f(x) E2 f(y).
- **Definition 29.** Let E1 , E2 be equivalence relations on hyperarithmetic subsets X, Y ⊆ ù, respectively. The relation E1 is m-reducible to E2 , in symbols E1 ≤m E2 , iff there exists a partial computable function f with X ⊆ dom(f) and Y ⊆ f(X ) such that for all x, y ∈ X , x E1 y ⇔ f(x) E2 f(y).
- **Definition 30.** A relation E on a hyperarithmetic subset of ù is an h-complete Σ11 equivalence relation, or m-complete Σ11 equivalence relation, if E is Σ11 and every Σ11 equivalence relation E1 on a hyperarithmetic subset of ù is h-reducible to E, or m-reducible to E, respectively.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.** Let Γ be a Π11 set of computable infinitary sentences. If every ∆11 subset of Γ has a model, then Γ has a model.
  *Proof:* (no proof in this paper)
- **Theorem 2 ([209]).** The degree spectrum of any structure is either a singleton or is upward closed.
  *Proof:* (no proof in this paper)
- **Theorem 3 ([209, 14, 77]).** If a linear order has first jump degree, it must be 0′ . In contrast, for each computable ordinal α ≥ 2 and every Turing degree d ≥ 0(α) , there exists a linear order having proper α th jump degree d.
  *Proof:* (no proof in this paper)
- **Theorem 4 ([181]).** For n ∈ ù, if a Boolean algebra has n th jump degree, then it is 0(n) . In contrast, for each d ≥ 0(ù) , there exists a Boolean algebra with proper ù th jump degree d.
  *Proof:* (no proof in this paper)
- **Theorem 5 ([281]).** For every computable α, there is a torsion abelian group having proper α th jump degree.
  *Proof:* (no proof in this paper)
- **Theorem 6 ([39]).** There are algebraic fields and torsion-free abelian groups of any finite rank > 1, the isomorphism types of which have arbitrary Turing degrees. There are structures in each of these classes the isomorphism types of which do not have Turing degrees.
  *Proof:* (no proof in this paper)
- **Theorem 7 ([81, 238]).** For n ∈ {1, 2} and every degree d ≥ 0(n) , there is a torsion-free group having proper n th jump degree d. For every degree d > 0′′′ , there is a torsion-free group having proper n th jump degree d.
  *Proof:* (no proof in this paper)
- **Theorem 8 ([2]).** For every computable α > 3, every d > 0(α) can be realized as a proper α th jump degree of a torsion-free abelian group.
  *Proof:* (no proof in this paper)
- **Theorem 9 ([58]).** Every torsion-free abelian group of rank 1 has first jump degree.
  *Proof:* (no proof in this paper)
- **Theorem 10 ([174]).** For every automorphically nontrivial structure A, there is a symmetric irreflexive graph, a partial order, a lattice, a ring, an integral domain of arbitrary characteristic, a commutative semigroup, or a 2-step nilpotent group the degree spectrum of which coincides with DgSp(A).
  *Proof:* (no proof in this paper)
- **Theorem 11 ([109]).** Every algebraic field has first jump degree.
  *Proof:* (no proof in this paper)
- **Theorem 12 ([315, 332]).** There exists a structure the degree spectrum of which is the set of all noncomputable Turing degrees.
  *Proof:* (no proof in this paper)
- **Theorem 13 ([116]).** For each finite n, there is a structure with the degree spectrum consisting of exactly all nonlown Turing degrees.
  *Proof:* (no proof in this paper)
- **Theorem 14 ([63]).** The set of hyperimmune degrees is the degree spectrum of a structure.
  *Proof:* (no proof in this paper)
- **Theorem 15 ([144]).** If M is an almost computable structure, then there is some copy of M that is computable from Kleene’s O.
  *Proof:* (no proof in this paper)
- **Theorem 16 ([108]).** Let n ≥ 2. For every Turing degree c, there is a linear order with spectrum {d : d(n) > c}. In particular, there is a linear order the spectrum of which contains exactly the nonlown degrees.
  *Proof:* (no proof in this paper)
- **Theorem 17 ([212]).** Every low4 Boolean algebra has a computable isomorphic copy.
  *Proof:* (no proof in this paper)
- **Theorem 18 ([185]).** There exists an abelian p-group, which has a d-computable copy relative to every noncomputable ∆02 Turing degree d, but has no computable copy.
  *Proof:* (no proof in this paper)
- **Theorem 19 ([323, 258]).** For every structure A, we have DgSp(A′ ) = {d′ : d ∈ DgSp(A)}.
  *Proof:* (no proof in this paper)
- **Theorem 20 ([287, 256]).** There is a structure A such that A =w A′ .
  *Proof:* (no proof in this paper)
- **Theorem 21 ([9]).** The following sets of Turing degrees can be theory spectra: (a) the degrees of complete extensions of Peano arithmetic, (b) 1-random degrees, and (c) the union of the cones above two incomparable Turing degrees.
  *Proof:* (no proof in this paper)
- **Theorem 22 ([9]).** The collection of non-hyperarithmetic degrees is not the spectrum of a theory.
  *Proof:* (no proof in this paper)
- **Theorem 23 (ZFC + PD). ([255])** Let T be an Lù1 ù -sentence with uncountably many countable models. The following are equivalent: (i) T is a counterexample to Vaught’s conjecture; (ii) The class of models of T satisfies the property hyperarithmetic-is-computable on a cone; and (iii) There exists an oracle relative to which {DgSp(A) : A |= T } = {{X ∈ 2ù : ù1X ≥ α} : α ∈ ù1 }.
  *Proof:* (no proof in this paper)
- **Theorem 24 ([142, 157]).** For a complete decidable theory T, the following are equivalent. 1. There is a uniform procedure that maps a formula consistent with T into a computable principal type of T, which contains this formula. 2. The theory T has a decidable prime model. 3. The theory T has a prime model and the set of all principal types of T is uniformly computable.
  *Proof:* (no proof in this paper)
- **Theorem 25 ([89]).** Let T be a complete, atomic, decidable theory with a prime model A such that D c (A) has a c.e. degree c > 0. Then there is a prime model B of T such that D c (B) has a low c.e. degree a, where a < c.
  *Proof:* (no proof in this paper)
- **Theorem 26 ([171]).** There is a prime model of a complete decidable theory with Slaman–Wehner degree spectrum.
  *Proof:* (no proof in this paper)
- **Theorem 27 ([197]).** There is a complete theory of abelian groups with both a computable model and a prime model, but no computable prime model.
  *Proof:* (no proof in this paper)
- **Theorem 28 ([169]).** There is a complete theory of linear orders having a computable model and a prime model, but no computable prime model.
  *Proof:* (no proof in this paper)
- **Theorem 29 ([66]).** Let X ≤T ∅′ . Then X is prime bounding if and only if X is not low2 .
  *Proof:* Constructs a complete, atomic, decidable theory to diagonalize against potential prime models for the low2 case, and uses a dominating function to build a prime model for the non-low2 case.
- **Theorem 30 ([259, 245]).** Let T be a complete decidable theory. The set of all types of T is uniformly computable if and only if T has a decidable saturated model.
  *Proof:* (no proof in this paper)
- **Theorem 31 ([261]).** Every countable saturated Boolean algebra has a decidable isomorphic copy.
  *Proof:* (no proof in this paper)
- **Theorem 32 ([142, 259, 245]).** There is a complete decidable theory with all types computable, which does not have a decidable saturated model.
  *Proof:* (no proof in this paper)
- **Theorem 33 ([159]).** For every n ∈ ù, no lown c.e. degree is saturated bounding.
  *Proof:* (no proof in this paper)
- **Theorem 34 ([124, 284, 246]).** There exists a complete decidable theory T having a homogeneous model M without a decidable copy, such that the type spectrum of M consists only of computable types and is computable.
  *Proof:* (no proof in this paper)
- **Theorem 35 ([283]).** There exists a decidable model, which does not have a computable homogeneous elementary extension.
  *Proof:* (no proof in this paper)
- **Theorem 36 ([61]).** There is a complete decidable theory T such that every countable homogeneous model of T has the degree of a complete extension of Peano arithmetic.
  *Proof:* (no proof in this paper)
- **Corollary 1.** A Turing degree d is homogeneous bounding if and only d is the degree of a complete extension of Peano arithmetic.
  *Proof:* (immediate from Theorem 36)
- **Theorem 37 ([219]).** Let T be a complete decidable theory and let A be a homogeneous model of T with a 0′ -basis. Then A has an isomorphic copy decidable in a low degree.
  *Proof:* (no proof in this paper)
- **Theorem 38 ([219]).** Let T be a complete decidable theory with all types computable. Let A be a homogeneous model of T with a 0-basis. Then A has an isomorphic copy B decidable in any nonzero degree.
  *Proof:* (no proof in this paper)
- **Theorem 39 ([219, 220]).** A degree d ≤ 0′ is 0-basis homogeneous bounding if and only if d is nonlow2 .
  *Proof:* (no proof in this paper)
- **Theorem 40 (Morley).** If a theory T is κ-categorical for some uncountable cardinal κ, then T is ë-categorical for all uncountable ë.
  *Proof:* (no proof in this paper)
- **Theorem 41 ([208]).** Let T be a countably categorical theory. If T ∩ Σn+2 is Σ0n+1 uniformly in n, then T has a computable model.
  *Proof:* (no proof in this paper)
- **Theorem 42 ([95]).** There exists a countably categorical theory of arbitrary arithmetic complexity, which has a computable model.
  *Proof:* (no proof in this paper)
- **Theorem 43 ([201]).** There exists a countably categorical theory S with a computable model such that S ≡T 0(ù) .
  *Proof:* (no proof in this paper)
- **Theorem 44 ([6]).** There exist uncountably categorical theories of arbitrary arithmetic complexity, as well as of nonarithmetic complexity, which have computable models.
  *Proof:* (no proof in this paper)
- **Theorem 45 ([118]).** Let M be a computable, trivial, strongly minimal model. Then Th(M) forms a 0′′ -computable set of sentences, and thus all countable models of Th(M) are isomorphic to 0′′ -decidable ones.
  *Proof:* Shows that the elementary diagram is a model complete theory, implying ∀∃-axiomatizability and 0′′-decidability.
- **Theorem 46 ([199]).** There exists a trivial, strongly minimal (and hence uncountably categorical ) theory, which has a computable prime model and each of the other countable models computes 0′′ .
  *Proof:* (no proof in this paper)
- **Theorem 47 ([114]).** For every n ≥ 3, there exists an Ehrenfeucht theory T of arbitrary arithmetic complexity such that it has n countable models, up to isomorphism, and it has a computable model among them. There also exists such a theory, which is Turing equivalent to the true first-order arithmetic.
  *Proof:* (no proof in this paper)
- **Theorem 48.** (i) ( follows from [44, 234]) Every computable, free, non-abelian group is ∆04 -categorical, and the result cannot be improved to ∆03 . (ii) ([80]) Every computable, free, abelian group is ∆02 -categorical, and the result cannot be improved to computable categoricity. (iii) ([80]) Every computable abelian group of the form L i∈ù Hi , where Hi ≤ (Q, +) for i ∈ ù, is ∆03 -categorical. A computable group of this form is ∆02 -categorical if and only if it is isomorphic to a free module over a localization of Z by a set of primes with a semi-low complement. (iv) ([32]) Every computable equivalence relation is ∆03 -categorical, and the result cannot be improved to ∆02 .
  *Proof:* (no proof in this paper)
- **Theorem 49 ([10, 50]).** The following are equivalent for a computable structure A. 1. The structure A is relatively ∆0α -categorical. 2. The structure A has a formally Σ0α Scott family Φ. 3. The structure A has a formally c.e. Scott family Φ.
  *Proof:* (no proof in this paper)
- **Theorem 50.** (i) ([236]) A computable linear order is relatively ∆02 -categorical if and only if it is a sum of finitely many intervals, each of type m, ù, ù ∗ , Z, or n · ç, so that each interval of type n · ç has a supremum and infimum. (ii) ([236]) A computable Boolean algebra is relatively ∆02 -categorical if and only if it can be expressed as a finite direct sum c1 ∨ · · · ∨ cn , where each ci is either atomless, an atom, or a 1-atom. (iii) ([32]) A computable equivalence structure is relatively ∆02 -categorical if and only if it either has finitely many infinite equivalence classes, or there is an upper bound on the size its finite equivalence classes. (iv) ([46]) A computable injection structure is relatively ∆02 -categorical if and only if it has finitely many orbits of type ù, or finitely many orbits of type Z. (v) ([33]) A computable abelian p-group G is relatively ∆02 -categorical iff G is reduced and ë(G) ≤ ù, or G is isomorphic to Z(p∞ ) ⊕ H , where α ≤ ù and H has finite period.
  *Proof:* (no proof in this paper)
- **Theorem 51 ([116, 51]).** For every computable ordinal α, there is a ∆0α -categorical but not relatively ∆0α -categorical structure.
  *Proof:* (no proof in this paper)
- **Theorem 52 ([168]).** There is a computably categorical algebraic field, which is not relatively computably categorical.
  *Proof:* (no proof in this paper)
- **Theorem 53 ([54]).** There is a computable structure, which is computably categorical, but ceases to be after naming any element of the structure.
  *Proof:* (no proof in this paper)
- **Theorem 54 ([83]).** Any 1-decidable computably categorical structure is relatively ∆02 -categorical.
  *Proof:* (no proof in this paper)
- **Theorem 55 ([76]).** For every computable ordinal α, there is a computably categorical structure that is not relatively ∆0α -categorical.
  *Proof:* (no proof in this paper)
- **Theorem 56 ([127, 129]).** For every finite n ≥ 2, there is a computable structure of computable dimension n.
  *Proof:* (no proof in this paper)
- **Theorem 57 ([65]).** (i) For every computable ordinal α, 0(α) is the degree of categoricity of a computable structure. (ii) For a computable successor ordinal α, every degree d that is c.e.a. in 0(α) is a degree of categoricity.
  *Proof:* (no proof in this paper)
- **Theorem 58 ([3]).** (i) There exists a Σ02 degree that is not categorically definable. (ii) Every degree of a set that is 2-generic relative to some perfect tree is not a degree of categoricity. (iii) Every noncomputable hyperimmune-free degree is not a degree of categoricity.
  *Proof:* (no proof in this paper)
- **Theorem 59 ([251]).** There exists a computable field with a splitting algorithm, which is not computably categorical, and such that its categoricity spectrum must contain degrees d0 and d1 with d0 ∧ d1 = 0.
  *Proof:* (no proof in this paper)
- **Theorem 60 ([280]).** Let A be a decidable structure. Then A is decidably categorical if and only if there is a finite tuple c of elements in A such that (A, c) is a prime model of the theory Th(A, c) and the set of complete formulas of this theory is computable.
  *Proof:* (no proof in this paper)
- **Theorem 61 ([132]).** Every c.e. degree d is the degree of decidable categoricity of some decidable almost prime model.
  *Proof:* (no proof in this paper)
- **Theorem 62 ([131]).** There exists a decidable Ehrenfeucht theory T such that T has a decidable prime model that is decidably categorical, and T has a decidable almost prime model that is not decidably categorical.
  *Proof:* (no proof in this paper)
- **Theorem 63 ([264]).** For every Turing degree d, the degree of the isomorphism type of the group Autd (ù) is d′′ .
  *Proof:* (no proof in this paper)
- **Theorem 64 ([268]).** For every pair c, d of Turing degrees, we have (Autd (ù) ≦ Autc (ù)) ⇔ (d ≤ c), where ≦ stands for the usual group-theoretic embedding.
  *Proof:* (no proof in this paper)
- **Theorem 65 ([192]).** For every Turing degree d, the unique normal series for Autd (ù) has the form {1} ✁ E ✁ F ✁ Autd (ù), where F is the subgroup of permutations that change only finitely many numbers, E is the subgroup of even permutations of F , and 1 is the identity permutation.
  *Proof:* (no proof in this paper)
- **Theorem 66 ([270]).** There exists a 2-generated Π01 group G such that G   Autc (ù).
  *Proof:* (no proof in this paper)
- **Theorem 67 ([265]).** There exists a first-order sentence in the language of groups such that for every G ≦ Autc (ù), (G |= φ) ⇔ (G ∼= Autc (ù)).
  *Proof:* (no proof in this paper)
- **Theorem 68 ([88, 231]).** There exists a computable structure M such that Aut(M) has 2ù elements, while Autc (M) has only one element.
  *Proof:* (no proof in this paper)
- **Theorem 69 ([263]).** For a computable structure M, the group Autc (M) is isomorphic to a computable one if and only if there exists a finite tuple p such that Aut(M, p) = {1}, and the set {(m, n) : m ∼=c n} is c.e., where m ∼=c n ⇔ (∃f ∈ Autc (M))[f: m → n].
  *Proof:* (no proof in this paper)
- **Corollary 2 ([263]).** A finitely generated group G is isomorphic to Autc (M) for some computable structure M if and only if G has a decidable word problem.
  *Proof:* (immediate from Theorem 69)
- **Theorem 70 ([260]).** For every Turing degree d ≤ 0′′ , there exists a computable structure M such that deg (D(Autc (M))) = d.
  *Proof:* (no proof in this paper)
- **Theorem 71 ([150]).** 1. Let d0 and d1 be incomparable Turing degrees. Then no computable structure M has AutSp(M) = {d0 , d1 } or AutSp(M) = {0, d0 , d1 }. 2. There exist pairwise incomparable ∆02 Turing degrees d0 , d1 , d2 , and computable structures A and B such that AutSp(A) = {d0 , d1 , d2 } and AutSp(B) = {0, d0 , d1 , d2 }.
  *Proof:* (no proof in this paper)
- **Theorem 72 ([262]).** Let A be an atomic decidable Boolean algebra. For every computable Boolean algebra B, we have (Autc (B) ∼= Autc (A)) ⇒ (B ∼=c A).
  *Proof:* (no proof in this paper)
- **Theorem 73 ([302]).** A computable linear order A contains a dense interval if and only if card(Autc (L)) > 1 for every computable L such that L ∼= A.
  *Proof:* (no proof in this paper)
- **Theorem 74 ([273]).** For Turing ideals I and J we have: (AutI (Q) ≦ AutJ (Q)) ⇔ (I ⊆ J ), and (AutI (Q) ∼= AutJ (Q)) ⇔ (I = J ).
  *Proof:* (no proof in this paper)
- **Theorem 75 ([274]).** There is a first-order sentence ô such that, up to isomorphism, the group Autc (Q) is the only model of ô among all subgroups of Autc (ù).
  *Proof:* (no proof in this paper)
- **Theorem 76 ([224]).** The following three properties, known to be true for Aut(Q), fail for Autc (Q): (a) the group is divisible; (b) every element is a commutator of itself with some other element; and (c) two elements are conjugate if and only if they have isomorphic orbital structures.
  *Proof:* (no proof in this paper)
- **Theorem 77 ([266]).** For every computable division ring R, there exists a computable copy of the module M = L i∈ù R such that Autc (M) contains only multiplications by scalars from R.
  *Proof:* (no proof in this paper)
- **Theorem 78 ([10, 50]).** Let A be a computable structure. A relation R on A is relatively intrinsically Σ0α iff R is definable by a computable Σα formula with finitely many parameters.
  *Proof:* (no proof in this paper)
- **Theorem 79 ([116, 51]).** For every computable ordinal α, there is a computable structure A with an intrinsically Σ0α relation R such that R is not definable by a computable Σα formula with finitely many parameters.
  *Proof:* (no proof in this paper)
- **Theorem 80 ([152]).** Let A be a computable structure, and let R be a relation that is intrinsically c.e. on A, while ¬R is not. Then, under a certain extra decidability condition, for any c.e. degree d, we have d ∈ DgSpA (R).
  *Proof:* (no proof in this paper)
- **Theorem 81 ([16]).** Let A be a computable structure, and let R be a relation that is not intrinsically ∆0α on A. Then, under certain extra effectiveness conditions, for any Σ0α set C , there is an isomorphism f from A onto a computable copy with f(R) ≡∆0α C .
  *Proof:* (no proof in this paper)
- **Theorem 82 ([205]).** Let (P,  ) be a computable partially ordered set. There are a computable structure A and a computable unary relation R on its domain such that (DgSpA (R), ≤) ∼= (P,  ) and every degree in DgSpA (R) is realized via a c.e. set.
  *Proof:* (no proof in this paper)
- **Theorem 83 ([82]).** A computable relation on a computable Boolean algebra is either intrinsically computable or has infinite Turing degree spectrum.
  *Proof:* (no proof in this paper)
- **Theorem 84 ([78]).** If a computable linear order has infinitely many successor pairs, then the degree spectrum of the successor relation is closed upward in the c.e. Turing degrees.
  *Proof:* (no proof in this paper)
- **Theorem 85 ([320]).** For a computable structure A, and a relation R on A, the following are equivalent: (i) R is intrinsically ∆11 on A; (ii) R is relatively intrinsically ∆11 on A; and (iii) R is definable in A by a computable infinitary formula with finitely many parameters.
  *Proof:* (no proof in this paper)
- **Theorem 86 ([321, 137]).** For a computable structure A and relation R on A, the following are equivalent: (i) R is intrinsically Π11 on A; (ii) R is relatively intrinsically Π11 on A; and (iii) R is definable in A by a Π11 disjunction of computable infinitary formulas with finitely many parameters.
  *Proof:* (no proof in this paper)
- **Theorem 87 ([137]).** The following sets are equal: 1. the set of Turing degrees of Π11 paths through O; 2. the set of Turing degrees of left-most paths of computable trees T ⊆ ù <ù such that T has a path, but no hyperarithmetic path; 3. the set of Turing degrees of maximal well-ordered initial segments of Harrison orders; 4. the set of Turing degrees of superatomic parts of Harrison Boolean algebras; and 5. the set of Turing degrees of divisible parts of Harrison groups.
  *Proof:* (no proof in this paper)
- **Theorem 88 (folklore; see [229, 239]).** Every computable vector space over a computable field has a 0′ -computable basis, and this bound is sharp.
  *Proof:* (no proof in this paper)
- **Theorem 89 (folklore; see [107, 240, 288]).** The algebraic closure of Q(xi : i ∈ ù) has a 0′ -maximal algebraically independent set, and this bound is sharp.
  *Proof:* (no proof in this paper)
- **Theorem 90 ([80]).** Let S ⊆ ù be a c.e. set of primes. (i) Every computable free module F (S) over the localization of Z by S has a Σ03 (actually, Π02 in S) set of generators. (ii) Every computable copy of F (S) has a Σ02 set of generators if and only if the complement of S is semi-low.
  *Proof:* (no proof in this paper)
- **Theorem 91 ([44, 234]).** Every computable copy of F∞ has a Π02 basis, and the result cannot be improved to Σ02 .
  *Proof:* (no proof in this paper)
- **Theorem 92 ([319]).** 1. A computable, torsion-free, abelian group of finite rank greater than 1 has an order in every Turing degree. 2. A computable, torsion-free, abelian group of infinite rank has an order in every Turing degree d ≥ 0′ . 3. Let n > 1. A computable, torsion-free, properly n-step nilpotent group has an order in every Turing degree d ≥ 0(n) .
  *Proof:* (no proof in this paper)
- **Theorem 93 ([240]).** For every nonempty Π01 class P, there is a computable orderable field F and a Turing degree preserving bijection f: P → C(F ).
  *Proof:* Relies on representing Boolean topological spaces as spaces of orderings of formally real fields.
- **Theorem 94 ([70]).** Every computable copy of Fn , where n > 1, has an order in every Turing degree.
  *Proof:* (no proof in this paper)
- **Theorem 95 ([182]).** Let H be a computable and effectively completely decomposable group. Then there is a computable copy G of H such that DgSp(BiO(G)) contains 0, but is not upward closed.
  *Proof:* (no proof in this paper)
- **Proposition 1.** (i) The class of linear orders can be characterized by a single first-order sentence. (ii) The class of abelian p-groups is characterized by a single computable Π2 sentence. (iii) The classes of well orders and reduced abelian p-groups cannot be characterized by single computable infinitary sentences.
  *Proof:* (no proof in this paper)
- **Proposition 2 ([140]).** (i) For the following classes K, the index set I (K) is Π02 : (a) linear orders, (b) Boolean algebras, (c) abelian p-groups, and (d) vector spaces over Q. (ii) (Kleene, Spector.) For the following classes K, the index set I (K) is not hyperarithmetic: (a) well-orders, (b) superatomic Boolean algebras, and (c) reduced abelian p-groups.
  *Proof:* (no proof in this paper)
- **Theorem 96.** (i) ([333, 282]) The index set of computable prime models is an m-complete Π0ù+2 set. (ii) ([333]) The index set of computable homogeneous models is an m-complete Π0ù+2 set. (iii) ([282]) The index set of structures with uncountably categorical theories is a ∆0ù -hard Σ0ù+1 set. (iv) ([282]) The index set of structures with countably categorical theories is a ∆0ù -hard Π0ù+2 set. (v) ([99]) The index set of structures with decidable countably categorical theories is an m-complete Σ03 − Σ03 set. (vi) ([35]) (a) The index set of computable structures with noncomputable Scott ranks is m-complete Σ11 . (b) The index set of structures with the Scott rank ù1CK is m-complete Π02 relative to Kleene’s O. (c) The index set of structures with the Scott rank ù1CK+1 is m-complete Σ02 relative to Kleene’s O.
  *Proof:* (no proof in this paper)
- **Theorem 97.** (i) ([100]) The index set of decidable structures is Σ03 -complete. (ii) ([333]) The index set of hyperarithmetically categorical structures is Π11 -complete. (iii) ([83]) The index set of relatively computably categorical structures is Σ03 -complete.
  *Proof:* (no proof in this paper)
- **Theorem 98 ([76]).** The index set of computably categorical structures is Π11 -complete.
  *Proof:* (no proof in this paper)
- **Proposition 3 ([140]).** Consider the class K consisting of copies of the Harrison order and of the linear orders of rank at most ù. Then K c / ∼ = has a hyperarithmetic Friedberg enumeration, but the index set I (K) is not hyperarithmetic.
  *Proof:* (no proof in this paper)
- **Theorem 99.** (i) ([30]) The isomorphism problem for computable vector spaces over Q is m-complete among Π03 sets. (ii) ([30]) The isomorphism problem for torsion-free abelian groups of finite characteristic is m-complete among Σ03 sets. (iii) ([140]) (a) The isomorphism problem for abelian p-groups is m-complete among Σ11 sets. (b) The isomorphism problem for trees is m-complete among Σ11 sets.
  *Proof:* (no proof in this paper)
- **Proposition 4 ([101]).** There is a class K of structures with hyperarithmetic index set such that the bi-embeddability relation on K c is complete among Σ11 equivalence relations.
  *Proof:* (no proof in this paper)
- **Theorem 100 ([96]).** The isomorphism of computable graphs is complete with respect to the chosen effective reducibility in the context of all Σ11 equivalence relations on ù.
  *Proof:* (no proof in this paper)
- **Theorem 101 ([97]).** The computable isomorphism relation on computable structures from classes including predecessor trees, Boolean algebras, and metric spaces is a complete Σ03 equivalence relation under the computable reducibility.
  *Proof:* Reduces the Σ03 -complete one-one equivalence relation of c.e. sets to the computable isomorphism on predecessor trees.
- **Theorem 102 ([106]).** For every Σ11 equivalence relation E on ù, there exists a hyperarithmetic class K of structures, which is closed under isomorphism, and such that E is h-equivalent to the bi-embeddability relation on computable structures from K.
  *Proof:* (no proof in this paper)