<!-- Generated 2026-05-31T01:40:46 -->
<!-- Source PDF: boyd__convex_optimization.pdf (2594443 bytes) -->
<!-- Citation: S. Boyd, L. Vandenberghe (2004). Convex Optimization. Cambridge University Press. -->

# Convex Optimization (S. Boyd, L. Vandenberghe, 2004)

## Definitions
- **Definition.** f : Rn → R is convex if dom f is a convex set and for all x, y ∈ dom f , 0 ≤ 𝜃 ≤ 1,

                                  f (𝜃x + (1 − 𝜃)y) ≤ 𝜃f (x) + (1 − 𝜃)f (y)
- **definition.** convex f : R → R is self-concordant if |f 000 (x)| ≤ 2f 00 (x) 3/2 for all x ∈ dom f

## Lemmas, Theorems, Propositions, Corollaries
- **Separating hyperplane theorem.** if C and D are nonempty disjoint (i.e., C ∩ D = ∅) convex sets, there exist a ≠ 0, b s.t.

                                aT x ≤ b for x ∈ C,         aT x ≥ b for x ∈ D
  *Proof:* (no proof in this paper)

- **supporting hyperplane theorem.** if C is convex, then there exists a supporting hyperplane at every boundary point of C
  *Proof:* (no proof in this paper)

- **Farkas’ lemma.** Ax   0,   cT x < 0    and AT y + c = 0,      y 0
       are strong alternatives
  *Proof:* Applies strong duality to a feasible linear programming problem.

- **arbitrage theorem.** there is no arbitrage ⇔ there exists a risk-neutral probability distribution under which each asset price is its expected payoff
  *Proof:* Employs Farkas' lemma on the investment payoff matrix to establish a risk-neutral probability distribution.