<!-- Generated 2026-05-31T01:16:08 -->
<!-- Source PDF: ma__introduction_to_the_theory_of_non_symmetric_dirich.pdf (1783943 bytes) -->
<!-- Citation: Ma, Z.-M., Röckner, M. (1992). Introduction to the Theory of (Non-Symmetric) Dirichlet Forms. Springer. -->

# Strong Uniqueness for Certain Infinite Dimensional Dirichlet Operators and Applications to Stochastic Quantization (Liskevich & Röckner, Annali della Scuola Normale Superiore di Pisa 1998)

## Definitions
- **DEFINITION 1.** A linear set D c D(A) is called a domain of strong uniqueness of A if there exists only one selfadjoint extension of A ~D in L2.
- **DEFINITION 2.** A linear set D C D(A) is called a domain of Markov uniqueness of A if there exists only one extension of A ~D which is a Markov generator in L 2 .
- **DEFINITION 3.** Let p > 1. A linear set D C D(Ap) is called a domain of Lp-strong uniqueness of A if all extensions B of A ~D in LP such that -B is a generator of a Co-semigroup in LP coincide with Ap.

## Lemmas, Theorems, Propositions, Corollaries
- **PROPOSITION 1.** Let A be a Markov generator. Let D C D(A) n V(A1). Then if is a domain of L 1-strong uniqueness for A, it is also a domain of Markov uniqueness.
  *Proof:* Applies the definition of the $L^1$-generator and evaluates the limit as $t \downarrow 0$ to show the extensions coincide.
- **THEOREM 1.** Suppose that there exist, I such that where for all Then i is essentially self-adjoint in
  *Proof:* Constructs a sequence of finite-dimensional approximating semigroups with smooth coefficients and uses Duhamel's formula. Relies on established gradient bounds to pass to the limit and prove the resulting extension is unique in $L^2$.
- **THEOREM 2.** . Suppose that there exists a sequence of mappings such that Then the operator i has a unique extension which generates
  *Proof:* Adapts the finite-dimensional approximation strategy of Theorem 1, employing $L^1$ gradient estimates via Duhamel's formula.
- **COROLLARY 1.** Let the conditions of Theorem 2 be satisfied. Then is a domain of Markov uniqueness for the operator A.
  *Proof:* (immediate from Theorem 2)
- **PROPOSITION 2.** Let u be the solution to (2) with .f’ E Suppose that b is as above satisfying, in addition, that there exists c+ e such that Then
  *Proof:* Differentiates the parabolic equation, multiplies by the gradient components, and integrates to bound the norm using dissipativity.
- **PROPOSITION 3.** Let f3 = a -f- 8, b =a1+ 811 with a, 8, aI, 81 : Suppose that E L2(JRd, v), ~131- E v) and that the condition of Proposition 2 is satisfied. Let u be the solution of (2). Then
  *Proof:* Multiplies the Cauchy problem by the solution, integrates by parts with respect to the measure, and bounds the result using Proposition 2.
- **PROPOSITION 4.** Let u be the solution to (2). In addition to the conditions of Proposition 3 assume that lalo E L4(JRd, v), 181- E v), 8 E C1(JRd, Rd), and that there exist Eo E (0, 1 ), c (eo) E R+ such that for all Then there exists C(so) E R+ (depending only on 80) such that
  *Proof:* Assembles derivative bounds from Lemmas 1, 2, and 3 into a single inequality. Integrates over time and applies Propositions 2 and 3 while tuning constants to absorb the remaining gradient terms.
- **LEMMA 1.** Let w := i7u. Then
  *Proof:* Leverages the evolution equation for $u$ and isolates the desired term using integration by parts.
- **LEMMA 2.** Let u be the solution to (2), w = Vu. Then
  *Proof:* Differentiates the equation along spatial directions, takes the scalar product with the gradient, and sums the results.
- **LEMMA 3.** Let u be the solution to (2), w := Vu. Then
  *Proof:* Multiplies the main equation by the weighted gradient and integrates by parts while invoking Lemma 1.
- **THEOREM 3.** Let fl E a + 8, E L~, ~!- E L 2. Suppose that there exists a sequence of mappings (8m)mEN, Sm : ~-l- H H-, such that all conditions of Theorem 1 hold. Then (0 +_ (~8, ~~)+ ~ has a unique extension which generates a Co-semigroup on L p for all p E ( 1 ~ 1 + 1 £o , 1 + l-:aeo).
  *Proof:* (no proof in this paper)
- **THEOREM 4.** Let 1 p 2, p a + 3, = L2-p, 181- E L 2. Suppose that there exists a sequence of mappings (8m)mEN, Sm : ’H- ~--+ H-, such that Then the operator (A -f-_ V.)+ has a unique extension which generates a Co-semigroup on LP.
  *Proof:* Modifies the approximation argument of Theorem 2 to handle the $L^p$ setting directly.