<!-- Generated 2026-05-31T02:36:26 -->
<!-- Source PDF: dress__valuated_matroids.pdf (115341 bytes) -->
<!-- Citation: Dress, A. W. M., and Wenzel, W. (1992). Valuated Matroids. Advances in Mathematics. -->

# Valuated Matroids – A new Look at the Greedy Algorithm (Dress and Wenzel, 1992)

## Definitions
- **Definition 1.** A valuated matroid of rank m with values in R, is a pair (E, v), consisting of a finite set E with #E ≥ m together with a map v : m → R ∪ {−∞} satisfying (V1) and (V0) there exists some B ∈ m with v(B) 6= −∞.
- **Definition 2.** Assume v : m → R ∪ {−∞} is some map with v(B) 6= −∞ for at least one B ∈ m . The greedy algorithm runs as follows: Step 0 : Choose some e1 , . . . , em ∈ E with v({e1 , . . . , em }) 6= −∞. Step k(1 ≤ k ≤ m) : Assume that x1 , . . . , xk−1 ∈ E are already determined and choose some xk ∈ E such that v({x1 , . . . , xk , ek+1 , . . . , em }) ≥ v({x1 , . . . , xk−1 , x, ek+1 , . . . , em }) for all x ∈ E. We say that the greedy algorithm works for v if for all starting sequences e1 , . . . , em ∈ E with v({e1 , . . . , em }) 6= −∞ and all permitted choices of the x1 , . . . , xm one has v({x1 , . . . , xm }) ≥ v(B) for all B ∈ m in which case v is called admissible.
- **Definition 3.** Two maps v, w : m → R ∪ {−∞} are called projectively equivalent, if there exists some α ∈ R and some map ϕ : E → R such that m X w(e − 1, . . . , em ) = α + ϕ(ei ) + v(e1 , . . . , em ) for all e1 , . . . , em ∈ E.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem.** Assume E is a finite set with #E ≥ m and v : m → R ∪ {−∞} is some map satisfying (V0). Then (E, v) is a valuated matroid, if and only if the greedy algorithm works for vϕ for all α ∈ R and all maps ϕ : E → R.
  *Proof:* Necessity is proved by showing the valuation is admissible via induction on the symmetric difference size between the chosen basis and an arbitrary basis, utilizing a matroid contraction argument. Sufficiency is established by contradiction: if the exchange property fails, a specific projective weight function is constructed to penalize elements, causing the greedy algorithm to fail and contradicting the assumption.