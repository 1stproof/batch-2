<!-- Generated 2026-05-31T02:37:33 -->
<!-- Source PDF: dress__valuated_matroids.pdf (115341 bytes) -->
<!-- Citation: Dress, A. W. M., Wenzel, W. (1992). Valuated Matroids. Advances in Mathematics. -->

# Valuated Matroids – A new Look at the Greedy Algorithm (Dress & Wenzel, 1992)

## Definitions
- **Definition 1.** A valuated matroid of rank m with values in R,  is a pair (E, v), consisting of a finite set E with #E ≥ m together with a map v : m E → R ∪ {−∞} satisfying (V1) and (V0) there exists some B ∈ m E with v(B) 6= −∞.
- **Definition 2.** Assume v : m E → R ∪ {−∞} is some map with v(B) 6= −∞ for at least one B ∈ m E . The greedy algorithm runs as follows: Step 0 : Choose some e1 , . . . , em ∈ E with v({e1 , . . . , em }) 6= −∞. Step k(1 ≤ k ≤ m) : Assume that x1 , . . . , xk−1 ∈ E are already determined and choose some xk ∈ E such that v({x1 , . . . , xk , ek+1 , . . . , em }) ≥ v({x1 , . . . , xk−1 , x, ek+1 , . . . , em }) for all x ∈ E.
- **Definition 3.** Two maps v, w : m E → R ∪ {−∞} are called projectively equivalent, if there exists some α ∈ R and some map ϕ : E → R such that w(e − 1, . . . , em ) = α + X ϕ(ei ) + v(e1 , . . . , em ) for all e1 , . . . , em ∈ E.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem (missing label in source).** Assume E is a finite set with #E ≥ m and v : m E → R ∪ {−∞} is some map satisfying (V0). Then (E, v) is a valuated matroid, if and only if the greedy algorithm works for vϕ for all α ∈ R and all maps ϕ : E → R.
  *Proof:* Proves necessity by using the valuation exchange property (V1) to induct on the symmetric difference between an arbitrary basis and the greedy basis, establishing global optimality. Proves sufficiency by contradiction; if (V1) fails, a specific weight function ϕ is constructed that forces the greedy algorithm to terminate at a sub-optimal basis.