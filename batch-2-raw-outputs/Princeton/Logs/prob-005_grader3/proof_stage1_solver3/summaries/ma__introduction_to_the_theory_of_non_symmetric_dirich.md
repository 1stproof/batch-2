<!-- Generated 2026-05-31T01:14:52 -->
<!-- Source PDF: ma__introduction_to_the_theory_of_non_symmetric_dirich.pdf (265897 bytes) -->
<!-- Citation: Ma, Z., Röckner, M. (1992). Introduction to the Theory of (Non-Symmetric) Dirichlet Forms. Springer. -->

# Energy Measure Closability for Dirichlet Forms (Ma, Z., Röckner, M. (1992). Introduction to the Theory of (Non-Symmetric) Dirichlet Forms. Springer.)

## Definitions
*(None explicitly labeled in this paper)*

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 1.1.** Let X be a locally compact Hausdorff space, µ a Radon measure on X with full support and (E, F ) a regular symmetric Dirichlet form on L2 (X, µ). Then there exists a minimal energy dominant measure m for (E, F ). It is unique up to mutual equivalence of energy dominant measures. We may choose m to be finite.
  *Proof:* Constructs the measure via a weighted sum of energy measures for a dense sequence of functions.

- **Theorem 1.1.** Let X be a locally compact Hausdorff space, µ a Radon measure on X with full support and (E, F ) a regular symmetric Dirichlet form on L2 (X, µ) with core C. If m is a finite energy dominant measure for (E, F ) then (E, C) is closable in L2 (X, m) and its closure (E, F (m) ) is a regular symmetric Dirichlet form on L2 (X, m). If X is second countable then the result is true also for infinite m.
  *Proof:* Constructs a decreasing sequence of truncations converging to zero in uniform norm and bounds their energy components. Utilizes uniform m-integrability of energy densities, tightness of the jump measure, and Urysohn's lemma.

- **Corollary 1.1.** Let the hypotheses of Theorem 1.1 be in force. Then dom H (m),1 ∩ L∞ (X, m) is an algebra, and for all f ∈ dom H (m) we have f 2 ∈ dom H (m),1 .
  *Proof:* (immediate from Theorem 1.1)

- **Lemma 2.1.** There is a constant c > 0 such that for any f ∈ C and any α > 0 we have E(f − Tα (f )) ≤ c Γ(f )({|f | ≥ α}). For the local part Ec we observe the stronger result Ec (f − Tα (f )) = Γc (f )({|f | ≥ α}).
  *Proof:* Bounds the energy using relatively compact open neighborhoods, the locality of the strongly local part, and contraction properties.

- **Lemma 2.2.** Let (un )n ⊂ F be an E-Cauchy sequence. Then the sequence (Γ(un ))n is convergent in L1 (X, m) and in particular, uniformly m-integrable, i.e. for any ε > 0 we can find some δ > 0 such that for any Borel set A ⊂ X, m(A) < δ implies supn Γ(un )(A) < ε.
  *Proof:* Uses a point-wise absolute difference inequality for the square roots of energy densities to show the sequence is Cauchy in L1.

- **Corollary 2.1.** Assume that m is finite or that X is second countable. Let (wn )n ⊂ F be an E-Cauchy sequence and let ε > 0. Then there exists a compact set K ⊂ X such that supn \int_X \int_{X\K} (wn (x) − wn (y))^2 J(dxdy) < ε.
  *Proof:* Applies the uniform integrability from Lemma 2.2 for finite measures and Prohorov's theorem for the second countable case.

- **Proposition 2.1.** Let (un )n ⊂ C be a sequence that is E-Cauchy and converges to zero in L2 (X, m). Then there are a sequence (kj )j ⊂ N with limj kj = ∞ and a subsequence (vj )j of (un )n such that limj E(vj − T_{1/kj} (vj )) = 0.
  *Proof:* Combines the uniform m-integrability of the energy measures with the L2 convergence of the sequence.

- **Theorem 3.1.** Let (X, X , µ) be a σ-finite measure space and (E, F ) a symmetric Dirichlet form on L2 (X, µ) satisfying Assumptions 3.1 and 3.2. Let m be a finite energy dominant measure for (E, F ). Then (E, B) is closable in L2 (X, m) and its closure (E, F (m) ) is a symmetric Dirichlet form.
  *Proof:* Modifies the proof of Theorem 1.1 by passing to subsequences and leveraging cutoff functions built from the nowhere-vanishing function χ.

- **Theorem 4.1.** Let m be a minimal energy dominant measure for (E, F ). Then m charges no set of zero capacity.
  *Proof:* (no proof in this paper)

- **Theorem 4.2.** Let m be an energy dominant measure for (E, F ) and m0 its absolutely continuous part with respect to Cap as in (26). Then also m0 is energy dominant.
  *Proof:* Evaluates the measure on a set of zero capacity to verify absolute continuity is preserved.

- **Theorem 4.3.** Assume (E, F ) is irreducible or transient. Let m be an energy dominant measure for (E, F ) that does not charge sets of zero capacity. Then m has full quasi-support.
  *Proof:* Verifies the full quasi-support condition by using the weak capacitary inequality to show zero m-measure implies zero capacity.

- **Corollary 4.1.** Assume (E, F ) is irreducible or transient. If m is an energy dominant measure for (E, F ), then m0 has full quasi-support.
  *Proof:* (immediate from Theorem 4.2)

- **Theorem 4.4.** Let (E, F ) be a regular Dirichlet form on L2 (X, µ) with core C. Assume (E, F ) is irreducible or transient and let m be an energy dominant measure for (E, F ). Then (E, C) is closable in L2 (X, m).
  *Proof:* (no proof in this paper)

- **Lemma 4.1.** Let u ∈ F be such that ue = 0 Γ(u)-a.e. Then also Γ(u)({ue = 0}) = 0.
  *Proof:* Approximates the indicator function with compactly supported continuously differentiable functions and applies dominated convergence.

- **Theorem 5.1.** Let (X, X , µ) be a measure space and (E, F ) a Dirichlet form on L2 (X, µ). Assume that B vanishes nowhere on X. Then the following hold: (i) There exists a minimal energy dominant measure m for the transferred Dirichlet form (Ê, F̂) on the locally compact Hausdorff space ∆. (ii) The form (E, ˆ B̂c ) is closable in L2 (∆, m), and its closure (E, ˆ F̂ (m) ) is a regular symmetric Dirichlet form. (iii) The Dirichlet form (E, ˆ F̂ (m) ) admits a carré du champ.
  *Proof:* (no proof in this paper)