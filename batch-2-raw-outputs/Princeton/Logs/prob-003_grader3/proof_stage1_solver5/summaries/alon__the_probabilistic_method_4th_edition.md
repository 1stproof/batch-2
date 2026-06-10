<!-- Generated 2026-05-31T02:03:57 -->
<!-- Source PDF: alon__the_probabilistic_method_4th_edition.pdf (322250 bytes) -->
<!-- Citation: Alon, Spencer (2016). The Probabilistic Method (4th Edition). Wiley. -->

# Large cliques and independent sets all over the place (Alon, Spencer (2016). The Probabilistic Method (4th Edition). Wiley.)

## Definitions
(None)

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.** There exists an n-vertex graph G for which mG (log n) ≤ 22(log log n)1/2+o(1) .
  *Proof:* (immediate from Theorem 2)

- **Theorem 2.** For any n ≥ 4 and k ≥ log n there exists an n-vertex graph G with p log log mG (k) ≤ 6 log log n log log k.
  *Proof:* Applies Theorem 8 with parameters $r = (\log N)^t$ or $r = k$, optimizing the choice of the parameter $t$.

- **Proposition 3.** Provided n is sufficiently large compared to r ≥ 2 we have mn (r) = Θ(r log n).
  *Proof:* (no proof in this paper)

- **Proposition 4.** For any n there exists an n-vertex graph which is 2r+8 log n, r -locally Ramsey for all r.
  *Proof:* Bounds the probability of missing cliques or independent sets in the random graph $G(n, 1/2)$ using Janson's inequality and a union bound.

- **Lemma 5.** For any integer N ≥ 4 there exists an N -vertex (m, r)-locally Ramsey graph for any m, r which satisfy log r ≤ (log m)2 29 log N .
  *Proof:* Applies Lemma 6 by taking lexicographic products of the random graph from Proposition 4 and optimizing the choice of parameters.

- **Lemma 6.** Let G be an n-vertex graph. Suppose that for some 2 ≤ r2 < . . . < rk we know that mG (rt ) ≤ mt , for 2 ≤ t ≤ k. Then log βG (m, `) ≥ log m − ` log(2m2 ) max log(mt+1 /m2 )+t 2≤t≤k log rt , (1) for any choice of mk+1 ≥ min(n, m) + 1.
  *Proof:* Proceeds by induction on the number of lexicographic powers, using the local properties of subsets and pigeonholing vertices by their first coordinate.

- **Lemma 7.** If there exists an n-vertex (m, r)-locally Ramsey graph then there exists a graph which is both m, 17 log r n -locally Ramsey and (r/2, 2)-locally Ramsey, provided r ≥ 16 log n.
  *Proof:* Takes a p-scramble of the graph and uses Chernoff bounds and Turán's theorem to show small cliques and independent sets are destroyed while preserving large ones.

- **Theorem 8.** For any t ≥ 2 there exists a (m, r)-locally Ramsey graph on N ≥ 4 vertices, provided log m ≥ t2t (log r)t (log N )1/t and log r ≥ t log log N .
  *Proof:* Uses induction on $t$, iteratively applying the scrambling lemma (Lemma 7) and taking lexicographic powers (Lemma 6).

- **Proposition 9.** Provided n ≥ 4r log n and r ≥ 2 we have mn (r) ≥ (0.5 + o(1))r log n.
  *Proof:* Iteratively removes the largest guaranteed cliques or independent sets given by standard Ramsey bounds.

- **Proposition 10.** Provided n is sufficiently large compared to r we have for G ∼ G(n, 1/2) that w.h.p. mG (r) = Θ(r log n).
  *Proof:* Uses the fact that almost all $K_r$-free graphs are $r-1$ colorable to bound the probability of missing cliques or independent sets.