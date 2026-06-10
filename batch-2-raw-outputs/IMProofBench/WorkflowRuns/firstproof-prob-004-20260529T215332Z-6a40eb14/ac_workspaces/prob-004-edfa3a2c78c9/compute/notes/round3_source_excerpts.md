# Round 3 source excerpts

Local papers:

- `papers/guth_area_contracting_thesis_2005.pdf`
- `papers/guth_area_expanding_rectangles_0710.0403.pdf`
- `papers/guth_width_volume_inequality_math0609569.pdf`
- `papers/guth_minimax_cup_powers_steenrod_squares_math0702066.pdf`

## Guth, arXiv:0710.0403, p.10

Estimate 1:

> Suppose that U is an open set in R and that Phi is a map of pairs
> (U, dU) -> (S, dS) of degree D > 0. Suppose 0 <= j < k <= l <= n.
> Then dil_k(Phi) >= c(n) Q_1 ... Q_j (Q_{j+1} ... Q_l)^((k-j)/(l-j)).

The same page says the estimate is slightly more general than the embedding
theorem because Phi need not be a diffeomorphism.

## Guth thesis, pp.140-142

Proposition 8.1.1 for 2-contracting diffeomorphisms between ellipsoid boundaries:

- B1: R_2 R_3 >= c S_2 S_3.
- B2: R_2 R_3 R_4 >= c S_2^2 S_3 S_4.
- B3a: if R_2^2 > S_2 S_3, then
  R_2 R_3 R_4 >= c S_2^{1/2} S_3^{3/2} S_4.
- B3b: if R_2^2 < S_2 S_3, then R_3 R_4 >= c S_3 S_4.

The proof uses the family of circles in a solid torus in the target ellipsoid; each
central circle has filling area at least c S_2 S_3.

## Guth thesis, pp.142-144

Proposition 8.1.2:

> Let C be an oriented relative 2-cycle in the rectangle R with area less than
> (1/2) R_1 R_2. Then C has an oriented filling with volume less than C R_1 R_2^2.

Proposition 8.1.3:

> Suppose there is a 2-contracting diffeomorphism from R to S. If
> C R_1 R_2^2 < S_1 S_2 S_3, then R_3 R_4 > c S_3 S_4.

The proof pulls back central planes
`[0,S1] x [0,S2] x {y3} x {y4}` and uses the filling estimate.

## Guth thesis, p.144

Opening of Section 8.2:

> Each map takes the boundary of the domain to the boundary of the range,
> has degree 1, and has 2-dilation less than C.

## Guth thesis, pp.145-147

Snake variants:

- Snake map:
  `R1 x R2 x R3 x R4 -> R1 x R2 x A^{-1} R3 x A R4`,
  with `1 <= A <= R3/R2`.
- Codimension-1 snake:
  `R1 x R2 x R3 x R4 -> R1 x A^{-1}R2 x A R3 x A^{-1}R4`,
  with `1 < A < (R4/R3)^{1/2}` and `A < R2/R1`.
- Short-side stretch:
  `R -> A R1 x A^{-3}R2 x A R3 x A^{-1}R4`,
  with `A >= 1`, `A < (R2/R1)^{1/4}`, and `A < (R4/R3)^{1/2}`.
- Technical variant:
  `R -> A R1 x A^{-3}R2 x R3 x R4`.
- Interpolated technical variant:
  `R -> A R1 x A^{-3}R2 x A x B`,
  where `A^4 < R2/R1`, `R3 < A < (R3 R4)^{1/2}`, and `R3 R4 = A B`.
- Pinching map:
  `R -> A x A x A x B`, provided `R1 > A` and `R2 R3 R4 > A^2 B`.

