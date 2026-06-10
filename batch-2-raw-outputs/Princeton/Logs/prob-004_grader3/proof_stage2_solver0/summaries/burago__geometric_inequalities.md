<!-- Generated 2026-05-31T01:51:29 -->
<!-- Source PDF: burago__geometric_inequalities.pdf (235295 bytes) -->
<!-- Citation: Burago, Yu. D., & Zalgaller, V. A. (1988). Geometric Inequalities. Springer. -->

# SHEPHARD’S INEQUALITIES, HODGE-RIEMANN RELATIONS, AND A CONJECTURE OF FEDOTOV (Burago, Yu. D., & Zalgaller, V. A. (1988). Geometric Inequalities. Springer.)

## Definitions

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1 (Alexandrov-Fenchel).** For convex bodies K, L, C1 , . . . , Cn´2 in Rn
               VpK, L, C1 , . . . , Cn´2 q2 ě VpK, K, C1 , . . . , Cn´2 q VpL, L, C1 , . . . , Cn´2 q.
  *Proof:* (no proof in this paper)

- **Theorem 1.2 (Shephard).** Given convex bodies K1 , . . . , Km , C1 , . . . , Cn´2 in Rn ,
define the m ˆ m symmetric matrix M by setting
                               Mij :“ VpKi , Kj , C1 , . . . , Cn´2 q.
Then
                                        p´1qm det M ď 0.
  *Proof:* Deduced from the Alexandrov-Fenchel inequality and the spectral characterization of positive matrices in Lemma 2.1.

- **Conjecture 1.3 (Fedotov).** Let k ď n{2, and let K1 , . . . , Km , C1 , . . . , Cn´2k be
convex bodies in Rn . Define the m ˆ m symmetric matrix M by setting
                               Mij :“ VpKi rks, Kj rks, C1 , . . . , Cn´2k q.
Then
                                             p´1qm det M ď 0.
  *Proof:* (no proof in this paper)

- **Lemma 1.4.** Conjecture 1.3 is valid in the following two cases:
a. When k “ 1 and m is arbitrary.
b. When m “ 2 and k is arbitrary.
  *Proof:* Deduces the first case directly from Theorem 1.2 and the second by iterating the Alexandrov-Fenchel inequality.

- **Theorem 1.5.** For every k ą 1, Conjecture 1.3 is false for some m ą 2.
  *Proof:* Applies the polarization formula and Hodge-Riemann relations to construct counterexamples that fail the hyperbolicity criterion of Lemma 2.3.

- **Lemma 2.1.** Let M be a symmetric positive matrix. The following are equivalent:
1. The positive eigenspace of M is one-dimensional.
2. xx, Myy2 ě xx, Mxy xy, Myy for all x ě 0 and y ě 0.
3. xx, Myy “ 0 implies xx, Mxy ď 0 for all x and y ě 0, y ‰ 0.
  *Proof:* Uses the Perron-Frobenius theorem to isolate the positive eigenspace and evaluates the quadratic form on its orthogonal complement.

- **Proposition 2.2.** In the setting and notations of Theorem 1.2, we have det   řM “ 0
if andřonly if there are linearly independent vectors x, y ą 0 such that K “ i xi Ki ,
L “ i yi Ki yield equality in the Alexandrov-Fenchel inequality of Theorem 1.1.
  *Proof:* Characterizes the vanishing determinant by analyzing the roots and gradient of an associated quadratic form near the origin.

- **Lemma 2.3.** For a symmetric positive m ˆ m matrix, the following are equivalent:
1. The positive eigenspace of M is one-dimensional.
2. p´1q|I| det MI ď 0 for all I Ď rms.
  *Proof:* Uses induction on the matrix dimension along with the Perron-Frobenius theorem to bound the dimension of the positive eigenspace.

- **Theorem 3.1 (McMullen-Timorin).** Fix n ě 2 and a simple polytope Λ P Rn , and
let m ě 1, k ď n{2, K1 , . . . , Km , L, C1 , . . . , Cn´2k P PpΛq, and x P Rm . If
                  ÿ
                    xi VpKi rks, M rk ´ 1s, L, C1 , . . . , Cn´2k q “ 0             (3.1)
                    i
holds for every M P PpΛq, then
                      ÿ
                p´1qk   xi xj VpKi rks, Kj rks, C1 , . . . , Cn´2k q ě 0.         (3.2)
                         i,j
Moreover, the statement is nontrivial in the sense that for any n ě 2 and k ď n{2,
there is a simple polytope Λ “ L “ C1 “ ¨ ¨ ¨ “ Cn´2k in Rn , m ě 1, K1 , . . . , Km P
PpΛq, and x P Rm so that (3.1) holds and the inequality in (3.2) is strict.
  *Proof:* (no proof in this paper)

- **Theorem 3.2.** Let k ď n{2, L, C1 , . . . , Cn´2k P PpΛq, and let α “ |I|“k αI DI be
                                                                    ř
a homogeneous differential operator of order k with constant coefficients. If
                                αDhL DhC1 ¨ ¨ ¨ DhCn´2k V “ 0,                    (3.3)
then
                               p´1qk α2 DhC1 ¨ ¨ ¨ DhCn´2k V ě 0.                 (3.4)
Moreover, equality is attained if and only if αV “ 0.
  *Proof:* (no proof in this paper)

- **Lemma 3.3.** For any homogeneous differential operator α “ |I|“k αI DI , there
                                                                ř

exist m ě 1, K1 , . . . , Km P PpΛq, and x P Rm so that α “ i xi pDhKi qk .
                                                       ř
  *Proof:* Applies the polarization formula to expand the differential operator into directional derivatives of strongly isomorphic polytopes.

- **Lemma 5.2.** For every k ě 2 and n ě 2k, Conjecture 1.3 fails for m “ 3.
  *Proof:* Constructs an explicit counterexample using parallelepipeds and evaluates their mixed volumes using the permanent formula.