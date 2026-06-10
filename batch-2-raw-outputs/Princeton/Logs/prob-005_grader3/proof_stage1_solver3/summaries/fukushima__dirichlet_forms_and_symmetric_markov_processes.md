<!-- Generated 2026-05-31T01:14:51 -->
<!-- Source PDF: fukushima__dirichlet_forms_and_symmetric_markov_processes.pdf (111161 bytes) -->
<!-- Citation: Fukushima, M., Oshima, Y., Takeda, M. (1994). Dirichlet Forms and Symmetric Markov Processes. de Gruyter. -->

# Fukushima, M., Oshima, Y., Takeda, M. (1994). Dirichlet Forms and Symmetric Markov Processes. de Gruyter.

## Definitions
*(No labeled definitions found in the text)*

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 2.1 (A.Beurling and J.Deny[BD59], cf. [FTake08]. [CF12]).** Let (E, F) be a closed symmetric form on L2 (S; m) and {Tt , t > 0} be the
associated L2 semigroup.
   Then {Tt , t > 0} is Markovian if and only if
   (*) every normal contraction operates on (E, F)
in the sense that, for any normal contraction φ and for any u ∈ F ,
v = φ(u) ∈ F and E(v, v) ≤ E(u, u).
  *Proof:* (no proof in this paper)

- **Theorem 3.1.** Let (S, m, E, F) be a regular Dirichlet form.
(i) There exists an m-symmetric Hunt process X on S properly associated
with it in the following sense:

  Pt f is a quasi continuous version of Tt f for any f ∈ B(S) ∩ L2 (S; m),

(ii) Uniqueness: If X1 , X2 , are properly associated, then there exists a
properly excepional set N for both processes and X1 S\N ∼ X2 S\N
  *Proof:* Proved by passing to a strongly regular representation via quasi-homeomorphism, and constructing the transition function using the Markov property and potential theory directly.

- **Theorem 4.1 ([CF12]).** (i) X̌ is µ-symmetric Hunt process on S.
  (ii) Let (Ě, F̌) be the Dirichlet form on L2 (S; µ) of X̌.
     Then (Ě, F̌) is regular.
  (iii) Let (F̌e , Ě) be the extended Dirichlet space of (Ě, F̌).
     Then (F̌e , Ě) = (Fe , E).
  *Proof:* (no proof in this paper)

- **Theorem 4.2 ([FTake08], [FOT11], [CF12]).** (I) E on Fe admits a unique
expression: for u, v ∈ Fe ,

        E(u, v) = E (c) (u, v)
          ∫                                               ∫
        1
      +           u(x) − u
                 (e         e(y))(e
                                  u(x) − ve(y))J(dx, dy) + u e(x)e
                                                                 v (x)κ(dx),
        2 S×S\d                                            S

where E (c) is a strongly local symmetric form, J is a symmetric Radon
measure on S × S \ d and κ is a Radon measure on S.
(II) J(dx, dy) = N (x, dy)µH (dx), κ(dx) = N (x, {∂})µH (dx)
where (N (x, dy), H) is the Lévy system of the Hunt process X introduced
by S.Watanabe[W64] and µH is the Revuz measure of the PCAF H.
(III) E is strongly local if and only if X is a diﬀusion with no killing inside
S, namely, its path is continuous on [0, ∞) a.s.
  *Proof:* Derived by making an orthogonal decomposition of the finite-energy martingale additive functional into continuous, jump, and killing parts and evaluating the energy of each term.

- **Theorem 5.1 (Albeverio-Ma[AM91], Fitzsimmons[Fi01]).** Let S be
a Lusin space, m be a σ-ﬁnite measure on it with full support and X be an
m-symmetric right process on S.
   Then the Dirichlet form of X on L2 (S; m) is quasi regular and
   X is properly associated with it.
  *Proof:* (no proof in this paper)

- **Theorem 5.2 (Chen-Ma-Roeckner[CMR94]).** If (S, m, E, F) is quasi
regular Dirichlet form, then there exist
                              b m,
   a regular Dirichlet form (S,    b F)
                                b E,  b and
   a quasi homeomorphism j from S to Sb such that
   mb = m ◦ j −1 and (E, b F)
                           b on L2 (S;b m)
                                         b is the image Dirichlet form of
(E, F) on L2 (S; m) by j.
  *Proof:* (no proof in this paper)

- **Theorem 5.3.** For any quasi regular Dirichlet form (S, m, E, F), there are
an E-polar Borel set N ⊂ S and an m-symmetric special Borel standard
process X on S \ N that is properly associated with (E, F).
  *Proof:* Proved by using the transfer method (Theorem 5.2) to apply the known result for regular Dirichlet forms (Theorem 3.1) to quasi-regular ones.