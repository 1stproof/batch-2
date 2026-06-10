<!-- Generated 2026-05-31T02:38:32 -->
<!-- Source PDF: oxley__matroid_theory_2nd_edition.pdf (5128962 bytes) -->
<!-- Citation: Oxley, J. (2011). Matroid Theory (2nd Edition). Oxford University Press. -->

```markdown
# Matroid Theory (2nd Edition) (Oxley, 2011)

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 1.1.1.** Let E be the set of column labels of an m × n matrix A over a field F, and let I be the set of subsets X of E for which the multiset of columns labelled by X is a set and is linearly independent in the vector space V (m, F). Then (E, I) is a matroid.
  *Proof:* Proves the independence augmentation property by comparing dimensions of vector subspaces.
- **Lemma 1.1.3.** The set C of circuits of a matroid has the following property:
(C3) If C1 and C2 are distinct members of C and e ∈ C1 ∩ C2 , then there is a member C3 of C such that C3 ⊆ (C1 ∪ C2 ) − e.
  *Proof:* Proceeds by contradiction, applying the independence augmentation property to maximal independent sets.
- **Theorem 1.1.4.** Let E be a set and C be a collection of subsets of E satisfying (C1)–(C3). Let I be the collection of subsets of E that contain no member of C. Then (E, I) is a matroid having C as its collection of circuits.
  *Proof:* Shows that the independent sets defined by avoiding circuits satisfy the matroid axioms by contradiction.
- **Corollary 1.1.5.** Let C be a set of subsets of a set E. Then C is the collection of circuits of a matroid on E if and only if C has the following properties:
(C1) ∅ ∈/ C.
(C2) If C1 and C2 are members of C and C1 ⊆ C2 , then C1 = C2 .
(C3) If C1 and C2 are distinct members of C and e ∈ C1 ∩ C2 , then there is a member C3 of C such that C3 ⊆ (C1 ∪ C2 ) − e.
  *Proof:* (immediate from Theorem 1.1.4)
- **Proposition 1.1.6.** Suppose that I is an independent set in a matroid M and e is an element of M such that I ∪ e is dependent. Then M has a unique circuit contained in I ∪ e, and this circuit contains e.
  *Proof:* Assumes two distinct circuits exist and uses the circuit elimination axiom to find a contradiction.
- **Proposition 1.1.7.** Let E be the set of edges of a graph G and C be the set of edge sets of cycles of G. Then C is the set of circuits of a matroid on E.
  *Proof:* Verifies the circuit elimination axiom by explicitly constructing a new cycle from parts of two intersecting cycles.
- **Lemma 1.2.1.** If B1 and B2 are bases of a matroid M , then |B1 | = |B2 |.
  *Proof:* Applies the independence augmentation property to derive a contradiction from unequal sizes.
- **Lemma 1.2.2.** The set B of bases of a matroid has the following property:
(B2) If B1 and B2 are members of B and x ∈ B1 − B2 , then there is an element y of B2 − B1 such that (B1 − x) ∪ y ∈ B.
  *Proof:* Uses independence augmentation to find y and verifies that the resulting set has maximal size.
- **Theorem 1.2.3.** Let E be a set and B be a collection of subsets of E satisfying (B1) and (B2). Let I be the collection of subsets of E that are contained in some member of B. Then (E, I) is a matroid having B as its collection of bases.
  *Proof:* Assumes the independence augmentation property fails and iteratively uses the basis exchange property to reach a contradiction regarding basis cardinalities.
- **Lemma 1.2.4.** All the members of B have the same cardinality.
  *Proof:* Argues by contradiction using the basis exchange property to strictly decrease the difference between two bases of unequal size.
- **Corollary 1.2.5.** Let B be a set of subsets of a set E. Then B is the collection of bases of a matroid on E if and only if it has the following properties:
(B1) B is non-empty.
(B2) If B1 and B2 are in B and x ∈ B1 − B2 , then there is an element y of B2 − B1 such that (B1 − x) ∪ y ∈ B.
  *Proof:* (immediate from Theorem 1.2.3)
- **Corollary 1.2.6.** Let B be a basis of a matroid M . If e ∈ E(M ) − B, then B ∪ e contains a unique circuit, C(e, B). Moreover, e ∈ C(e, B).
  *Proof:* (immediate from Proposition 1.1.6)
- **Proposition 1.2.9.** Let M be a graphic matroid. Then M ∼ = M (G) for some connected graph G.
  *Proof:* Identifies the components of a disconnected graph into a single vertex without creating new cycles.
- **Lemma 1.3.1.** The rank function r of a matroid M on a set E has the following property:
(R3) If X and Y are subsets of E, then
                     r(X ∪ Y ) + r(X ∩ Y ) ≤ r(X) + r(Y ).
  *Proof:* Extends a basis of X ∩ Y to a basis of X ∪ Y and bounds the sum of ranks using sub-bases for X and Y.
- **Theorem 1.3.2.** Let E be a set and r be a function that maps 2E into the set of non-negative integers and satisfies (R1)–(R3). Let I be the collection of subsets X of E for which r(X) = |X|. Then (E, I) is a matroid having rank function r.
  *Proof:* Verifies the matroid axioms for I by algebraic manipulation of the rank conditions and proves r coincides with the induced rank.
- **Lemma 1.3.3.** Let E be a set and r be a function on 2E satisfying (R2) and (R3). If X and Y are subsets of E such that r(X ∪ y) = r(X) for all y in Y − X, then r(X ∪ Y ) = r(X).
  *Proof:* Proceeds by induction on the size of Y - X using the submodular inequality.
- **Corollary 1.3.4.** Let E be a set. A function r : 2E → Z+ ∪ {0} is the rank function of a matroid on E if and only if r has the following properties:
(R1) If X ⊆ E, then 0 ≤ r(X) ≤ |X|.
(R2) If X ⊆ Y ⊆ E, then r(X) ≤ r(Y ).
(R3) If X and Y are subsets of E, then
                     r(X ∪ Y ) + r(X ∩ Y ) ≤ r(X) + r(Y ).
  *Proof:* (immediate from Theorem 1.3.2)
- **Proposition 1.3.5.** Let M be a matroid with rank function r and suppose that X ⊆ E(M ). Then
(i) X is independent if and only if |X| = r(X);
(ii) X is a basis if and only if |X| = r(X) = r(M ); and
(iii) X is a circuit if and only if X is non-empty and, for all x in X,
      r(X − x) = |X| − 1 = r(X).
  *Proof:* (no proof in this paper)
- **Proposition 1.3.10.** Let D be a collection of non-empty subsets of a set E. Then D is the set of circuits of a paving matroid on E if and only if there are a positive integer k with k ≤ |E| and a subset D  of D such that
(i)  every member of D  has k elements, and if two distinct members D1 and D2 of D  have k − 1 common elements, then every k-element subset of D1 ∪ D2 is in D  ; and
(ii) D − D  consists of all of the (k + 1)-element subsets of E that contain no member of D  .
  *Proof:* (no proof in this paper)
- **Lemma 1.4.2.** For every subset X of the ground set of a matroid M ,
                                r(X) = r(cl(X)).
  *Proof:* Shows that a basis for X is also a basis for cl(X) because adding any element from the closure creates a dependent set.
- **Lemma 1.4.3.** The closure operator of a matroid on a set E has the following properties:
(CL1) If X ⊆ E, then X ⊆ cl(X).
(CL2) If X ⊆ Y ⊆ E, then cl(X) ⊆ cl(Y ).
(CL3) If X ⊆ E, then cl(cl(X)) = cl(X).
(CL4) If X ⊆ E and x ∈ E, and y ∈ cl(X ∪ x) − cl(X), then x ∈ cl(X ∪ y).
  *Proof:* Verifies the conditions algebraically using the properties of the rank function and basis extensions.
- **Lemma 1.4.4.** For a matroid M on a set E, if X ⊆ E and x ∈ E, then
                         r(X) ≤ r(X ∪ x) ≤ r(X) + 1.
  *Proof:* Follows directly from the increasing property and submodularity of the rank function.
- **Theorem 1.4.5.** Let E be a set and cl be a function from 2E into 2E satisfying (CL1)–(CL4). Let

                   I = {X ⊆ E : x ∈
                                  / cl(X − x) for all x in X}.

Then (E, I) is a matroid having closure operator cl.
  *Proof:* Proves the independent sets I satisfy the matroid axioms using Mac Lane–Steinitz exchange and verifies the closure operators match.
- **Lemma 1.4.6.** Suppose X ⊆ E and x ∈ E. If X is in I, but X ∪ x is not, then x ∈ cl(X).
  *Proof:* Uses the Mac Lane–Steinitz exchange property on elements removed from X U x.
- **Corollary 1.4.7.** Let E be a set. A function cl : 2E → 2E is the closure operator of a matroid on E if and only if it satisfies the following conditions:
(CL1) If X ⊆ E, then X ⊆ cl(X).
(CL2) If X ⊆ Y ⊆ E, then cl(X) ⊆ cl(Y ).
(CL3) If X ⊆ E, then cl(cl(X)) = cl(X).
(CL4) If X ⊆ E and x ∈ E, and y ∈ cl(X ∪ x) − cl(X), then x ∈ cl(X ∪ y).
  *Proof:* (immediate from Theorem 1.4.5)
- **Lemma 1.4.9.** Suppose that M is a matroid and X ⊆ E(M ). If x ∈ cl(X), then cl(X ∪ x) = cl(X).
  *Proof:* (no proof in this paper)
- **Proposition 1.4.10.** Let M be a matroid and X be a subset of E(M ). Then
(i) X is a spanning set if and only if r(X) = r(M );
(ii) X is a basis if and only if it is both spanning and independent;
(iii) X is a basis if and only if it is a minimal spanning set; and
(iv) X is a hyperplane if and only if it is a maximal non-spanning set.
  *Proof:* Connects spanning definitions directly to rank properties and closure logic.
- **Proposition 1.4.11.** Let M be a matroid and X be a subset of E(M ). Then
(i)  X is a circuit if and only if X is a minimal non-empty set such that x ∈ cl(X − x) for all x in X.
(ii) cl(X) = X ∪ {x : M has a circuit C such that x ∈ C ⊆ X ∪ x}.
  *Proof:* Applies the fundamental circuit property to a basis of X to establish closure membership.
- **Proposition 1.4.12.** The set C of circuits of a matroid satisfies the following:
(C3)  If C1 and C2 are members of C with e ∈ C1 ∩ C2 and f ∈ C1 − C2 , then there is a member C3 of C such that f ∈ C3 ⊆ (C1 ∪ C2 ) − e.
  *Proof:* Uses closure properties and Proposition 1.4.11(ii) to guarantee a circuit containing f while avoiding e.
- **Corollary 1.4.13.** Let C be a collection of subsets of a set E. Then C is the set of circuits of a matroid on E if and only if C satisfies (C1), (C2), and (C3)  .
  *Proof:* (immediate from Proposition 1.4.12)
- **Proposition 1.4.14.** Let M be a rank-r matroid having C   as its set of non-spanning circuits. Then
  C(M ) = C   ∪ {X ⊆ E(M ) : |X| = r + 1 and X contains no member of C   }.
  *Proof:* Relies on the fact that any dependent set of size r+1 is a circuit if and only if it contains no smaller circuit.
- **Proposition 1.4.15.** Let G be a graph. Then H is a hyperplane in M (G) if and only if E(G) − H is a minimal set of edges whose removal from G increases the number of connected components.
  *Proof:* Translates the maximal non-spanning set property to graph topology regarding connected components.
- **Theorem 1.4.16.** Let E be a set. A function r from 2E into the set of non-negative integers is the rank function of a matroid on E if and only if it has the following properties:
(R1)  r(∅) = 0.
(R2)  If X ⊆ E and x ∈ E, then r(X) ≤ r(X ∪ x) ≤ r(X) + 1.
(R3)  If X ⊆ E and x and y are elements of E such that r(X∪x) = r(X ∪ y) = r(X), then r(X ∪ x ∪ y) = r(X).
  *Proof:* (no proof in this paper)
- **Proposition 1.5.1.** Suppose that E is a set that labels a multiset of elements from V (m, F). Let I be the collection of subsets X of E such that X labels an affinely independent subset of V (m, F). Then (E, I) is a matroid.
  *Proof:* Converts affine independence to linear independence in one higher dimension.
- **Proposition 1.5.6.** Let E be a set and Λ be a collection of subsets of E each having at least three elements such that every two distinct members of Λ meet in at most one element. Let I be the set of subsets X of E having at most three elements such that no member of Λ contains three elements of X. Then (E, I) is a simple matroid of rank at most three whose rank-one flats are the one-element subsets of E and whose rank-two flats are the members of Λ together with all two-element subsets Y of E for which no member of Λ contains Y . Moreover, every simple matroid of rank at most three arises in this way.
  *Proof:* (no proof in this paper)
- **Proposition 1.5.14.** Let M be a matroid having a subset X that is both a circuit and a hyperplane. Let B   = B(M ) ∪ {X}. Then B   is the set of bases of a matroid M   on E(M ). Moreover,

              C(M   ) = (C(M ) − {X}) ∪ {X ∪ e : e ∈ E(M ) − X}.
  *Proof:* (no proof in this paper)
- **Proposition 1.5.17.** There is a rank-r matroid M on E whose collection C of circuits is C1 ∪ C2 ∪ C3 ∪ C4 .
  *Proof:* Explicitly checks the circuit elimination axiom against all combinations of the defined circuit collections.
- **Proposition 1.5.18.** Let r be an integer exceeding two. A matroid M is a rank-r spike with tip t if and only if M has the following properties:
(i)   E(M ) is the union of r lines L1 , L2 , . . . , Lr each of which is a 3-element circuit containing the point t;
(ii) for all k in {1, 2, . . . , r − 1}, the union of any k of L1 , L2 , . . . , Lr has rank k + 1; and
(iii) r(L1 ∪ L2 ∪ . . . ∪ Lr ) = r.
  *Proof:* (no proof in this paper)
- **Theorem 1.6.2.** Let A be a family (A1 , A2 , . . . , Am ) of subsets of a set S. Let I be the set of partial transversals of A. Then I is the collection of independent sets of a matroid on S.
  *Proof:* Proves independence augmentation using bipartite matchings and recoloring paths in the symmetric difference.
- **Lemma 1.7.3.** For all matroids M , the poset L(M ) is a lattice and, for all flats X and Y of M ,

                    X ∧ Y = X ∩ Y and X ∨ Y = cl(X ∪ Y ).
  *Proof:* Shows closure properties guarantee that the intersection is closed and the closure of the union forms the join.
- **Theorem 1.7.5.** A lattice L is geometric if and only if it is the lattice of flats of a matroid.
  *Proof:* Verifies that flats of a matroid form a semimodular lattice satisfying the Jordan-Dedekind chain condition, then constructs a valid rank function from the height of atoms to prove the converse.
- **Lemma 1.7.6.** If X and Y are flats of a matroid M and X ⊆ Y , then every maximal chain of flats from X to Y has length r(Y ) − r(X).
  *Proof:* Follows directly from the fact that covering in the lattice of flats corresponds exactly to a rank increment of one.
- **Proposition 1.7.8.** Let X be a flat in a matroid M and suppose that r(X) = r(M ) − k where k ≥ 1. Then M has a set {H1 , H2 , . . . , Hk } of hyperplanes such that X = ∩ki=1 Hi .
  *Proof:* Proceeds by induction on the corank, repeatedly intersecting flats with a chosen hyperplane.
- **Lemma 1.8.3.** If (E, I) is a matroid M , then BG is a solution to the optimization problem 1.8.2.
  *Proof:* Deduced immediately from comparing element weights against any other basis.
- **Lemma 1.8.4.** If 1 ≤ j ≤ r, then w(ej ) ≥ w(fj ).
  *Proof:* Derives a contradiction by showing the greedy choice would have picked a heavier available element otherwise.
- **Theorem 1.8.5.** Let I be a collection of subsets of a set E. Then (E, I) is a matroid if and only if I has the following properties:
(I1) ∅ ∈ I.
(I2) If I ∈ I and I   ⊆ I, then I   ∈ I.
(G) For all weight functions w : E → R, the greedy algorithm produces a maximal member of I of maximum weight.
  *Proof:* Constructs a specific weight function that forces the greedy algorithm to fail if the independence augmentation property does not hold.
- **Theorem 2.1.1.** Let M be a matroid and B ∗ (M ) be {E(M ) − B : B ∈ B(M )}. Then B ∗ (M ) is the set of bases of a matroid on E(M ).
  *Proof:* Proves the complementary sets satisfy the basis exchange axioms by mapping the dual condition.
- **Lemma 2.1.2.** The set B of bases of a matroid M has the following property:
(B2)∗ If B1 and B2 are in B and x ∈ B2 − B1 , then there is an element y of B1 − B2 such that (B1 − y) ∪ x ∈ B.
  *Proof:* Uses the fundamental circuit of x with respect to B1 to find an element y whose removal restores independence.
- **Corollary 2.1.5.** Let B be a set of subsets of a set E. Then B is the collection of bases of a matroid on E if and only if B satisfies (B1) and (B2)∗ .
  *Proof:* Demonstrates equivalence by passing to the complementary clutter and applying Theorem 1.2.3.
- **Proposition 2.1.6.** Let M be a matroid on a set E and suppose X ⊆ E. Then
(i) X is independent if and only if E − X is cospanning;
(ii) X is spanning if and only if E − X is coindependent;
(iii) X is a hyperplane if and only if E − X is a cocircuit; and
(iv) X is a circuit if and only if E − X is a cohyperplane.
  *Proof:* Converts maximal/minimal characterizations of the sets between the primal and dual matroids.
- **Proposition 2.1.7.** If M   is obtained from M by relaxing a circuit–hyperplane X of M , then (M   )∗ can be obtained from M ∗ by relaxing the circuit–hyperplane E(M ) − X of M ∗ .
  *Proof:* Matches the augmented basis set directly to its complement.
- **Proposition 2.1.9.** For all subsets X of the ground set E of a matroid M ,

                        r∗ (X) = r(E − X) + |X| − r(M ).
  *Proof:* Employs an augmentation lemma to disjointly extend bases of X in the dual and E-X in the primal to full bases.
- **Lemma 2.1.10.** Let I and I ∗ be disjoint subsets of E(M ) such that I is independent and I ∗ is coindependent. Then M has a basis B and a cobasis B ∗ such that B and B ∗ are disjoint, I ⊆ B, and I ∗ ⊆ B ∗ .
  *Proof:* Extends I to a full basis within the restriction E - I*, leveraging cospanning properties.
- **Proposition 2.1.11.** In a matroid M , let C be a circuit and C ∗ be a cocircuit. Then |C ∩ C ∗ |  = 1.
  *Proof:* Proves by contradiction using the closure of the hyperplane complement of C*.
- **Proposition 2.1.12.** Let (X, Y, {z}) be a partition of the ground set E of a matroid M where X or Y may be empty. Then z ∈ cl(X) if and only if z  ∈ cl∗ (Y ).
  *Proof:* Evaluates the rank equations for closure in the primal and corank formulations in the dual.
- **Proposition 2.1.15.** Let A be a clutter. Then b(b(A)) = A.
  *Proof:* (no proof in this paper)
- **Proposition 2.1.19.** C ∗ (M ) = b(B(M )) and b(C ∗ (M )) = B(M ).
  *Proof:* Establishes equivalence between cocircuits and minimal blocking sets of bases.
- **Corollary 2.1.20.** C(M ) = b(B ∗ (M )) and b(C(M )) = B ∗ (M ).
  *Proof:* (immediate from Proposition 2.1.19)
- **Proposition 2.1.21.** Let H be a set of subsets of a set E. Then H is the collection of hyperplanes of a matroid on E if and only if H has the following properties:
(H1) E ∈/ H.
(H2) H is a clutter.
(H3) If H1 and H2 are distinct members of H and e ∈ E − (H1 ∪ H2 ), then there is a member H3 of H such that H3 ⊇ (H1 ∩ H2 ) ∪ e.
  *Proof:* (no proof in this paper)
- **Lemma 2.1.22.** Let X and Y be collections of subsets of a finite set E such that every member of X contains a member of Y, and every member of Y contains a member of X . Then the minimal members of X are precisely the minimal members of Y.
  *Proof:* (no proof in this paper)
- **Proposition 2.1.23.** Let M be a matroid having ground set E. Then D is a circuit of M if and only if D is a minimal non-empty subset of E such that |D ∩ C ∗ |  = 1 for every cocircuit C ∗ of M .
  *Proof:* Utilizes orthogonality and minimal intersection properties to characterize circuits via clutters.
- **Proposition 2.1.24.** If T is an m-partition {T1 , T2 , . . . , Tk } of a set E, then T is the set of hyperplanes of a paving matroid of rank m + 1 on E. Moreover, for r ≥ 2, the set of hyperplanes of every rank-r paving matroid on E is an (r − 1)-partition of E.
  *Proof:* (no proof in this paper)
- **Lemma 2.1.26.** The set of hyperplanes of an r-spike M consists of
(i) the members of C3 ;
(ii) all sets of the form E − {xi , yi , xj , yj } with 1 ≤ i < j ≤ r; and
(iii) all (r − 1)-element subsets of E − t that contain at most one element of each {xi , yi } and are not contained in any member of C3 .
  *Proof:* Deduced by tracking which subsets of legs allow the closure to span the entire spike.
- **Proposition 2.1.27.** Let e be an element of a spike M that has tip t. Then M \e is self-dual. Moreover, if M is a free spike, then M \t is identically self-dual.
  *Proof:* Maps circuits and cocircuits to each other under a specific permutation of elements.
- **Proposition 2.1.28.** For r ≥ 3, a rank-r matroid M on a 2r-element set E is a tipless spike if and only if there is a partition of E into r pairs of elements such that the union of every two such pairs is both a circuit and a cocircuit of M .
  *Proof:* Concludes from the structure of non-spanning circuits and explicit construction in subsequent proofs.
- **Proposition 2.1.29.** For some r ≥ 3, let E = {x1 , y1 , x2 , y2 , . . . , xr , yr } and let M be a rank-r matroid on E. Suppose that {xi , yi , xj , yj } is both a circuit and a cocircuit of M for all i and j with 1 ≤ i < j ≤ r. Then there is a unique rank-r spike N with tip t and legs {t, x1 , y1 }, {t, x2 , y2 }, . . . , {t, xr , yr } such that N \t = M . Hence M is a tipless spike.
  *Proof:* Extends the ground set by a tip and validates the spiked circuit conditions via orthogonality.
- **Theorem 2.2.8.** Let M be the vector matroid of the matrix [Ir |D] where the columns of this matrix are labelled, in order, e1 , e2 , . . . , en and 1 ≤ r < n. Then M ∗ is the vector matroid of [−DT |In−r ] where its columns are also labelled e1 , e2 , . . . , en in that order.
  *Proof:* Computes matrix rank under block partitions to verify bases map directly to their complements.
- **Corollary 2.2.9.** If a matroid M is representable over a field F, then M ∗ is also representable over F.
  *Proof:* (immediate from Theorem 2.2.8)
- **Lemma 2.2.20.** Let X be a totally unimodular matrix. If Y is obtained from X by pivoting on the non-zero entry xst of the latter, then Y is totally unimodular.
  *Proof:* Confirms determinant invariance on all square submatrices via cofactor expansion.
- **Lemma 2.2.21.** Let {e1 , e2 , . . . , er } be a basis of a matroid M of non-zero rank. Then M is regular if and only there is a totally unimodular matrix [Ir |D] representing M over R whose first r columns are labelled, in order, e1 , e2 , . . . , er .
  *Proof:* Relies on row reduction operations preserving total unimodularity via pivoting.
- **Proposition 2.2.22.** The dual of a regular matroid is regular.
  *Proof:* Observes that the dual representative matrix construction preserves total unimodularity.
- **Proposition 2.2.23.** Let [Ir |D] be an r × n matrix over a field F where r is in {1, 2 . . . , n − 1}. Then the orthogonal subspace of R[Ir |D] is R[−DT |In−r ].
  *Proof:* Verifies the dot product of any two rows from the respective matrices is zero.
- **Corollary 2.2.24.** Let W be an r-dimensional subspace of V (n, F). Then W ⊥ has dimension n − r. Moreover, (W ⊥ )⊥ = W .
  *Proof:* (no proof in this paper)
- **Proposition 2.2.26.** The Vámos matroid V8 is not representable.
  *Proof:* Computes intersection dimensions of vector subspaces to force an unintended linear dependence.
```