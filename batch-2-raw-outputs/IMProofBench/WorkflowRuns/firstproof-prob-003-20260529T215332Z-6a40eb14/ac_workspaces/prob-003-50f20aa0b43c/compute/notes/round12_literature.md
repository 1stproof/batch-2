# Round 12 Literature Notes

Search terms used included:

- "bold play" hypotenuse Fokkink Meester Pelekis weighted Bernoulli
- "weighted Bernoulli" mean tail inequality
- Kellerer Bernoulli weighted inequality
- Kellerer "Linearkombinationen zufälliger Größen"
- cyclic interval random allocation weights loads
- biased measure weighted threshold

Closest references found:

1. R. Fokkink, L. Meester, C. Pelekis, "Optimizing stakes in simultaneous
   bets", ALEA 20 (2023), 153--165, DOI 10.30757/ALEA.v20-07.
   Local files: `papers/fokkink-meester-pelekis-2023.txt`,
   `papers/fokkink_meester_pelekis_optimizing_stakes_2023.pdf`.
   This is directly adjacent: it studies
   `pi(p,t)=sup P(sum c_i beta_i >= t)`.  The complement of the present
   problem asks for `pi(q,t+) <= q` on the strict hypotenuse with `q>=2/3`.
   Their Theorem 4.4 covers rectangles above the hypotenuse, and Proposition
   4.5 covers boundary points `(q,q)=( (k+1)/(k+2), (k+1)/(k+2) )`, but the
   near-hypotenuse strip `q<t<(k+1)/(k+2)` is not covered.

2. H. G. Kellerer, "Zur Existenz analoger Bereiche", Z. Wahrscheinlichkeitstheorie
   verw. Gebiete 1 (1963), 240--246, DOI 10.1007/BF00532495.
   Local file: `papers/kellerer-analogous-areas.txt`.
   This is an atomless analogous-region theorem.  It explains the earlier
   Kellerer lead but does not state the needed discrete Bernoulli halfspace
   inequality.

3. H. G. Kellerer, "Linearkombinationen zufälliger Größen und ihre gemeinsame
   Verteilung", Math. Z. 84 (1964), 403--414.
   Local file: `papers/kellerer-1964-linearkombinationen.html`; page images in
   `papers/kellerer_1964_pages/`.
   This is about distributions of linear combinations and joint distributions;
   I found no extractable theorem implying the rational cyclic inequality.

4. Y. Filmus, "The weighted complete intersection theorem", JCTA 151 (2017),
   84--101.  Local file: `papers/filmus_weighted_complete_intersection_2017.pdf`.
   Relevant to biased product-measure extremal problems for intersecting
   families.  It does not use the additional weighted-threshold structure of
   `{A: w(A)>1-p}` and does not imply the desired bound at bias `q>=2/3`.

5. Chaundy--Bullard / Jogdeo--Samuels binomial-tail monotonicity.  FMP quote
   Theorem 7.1: for integer `a>1`, `P(Bin(ka,1/a)>=k)` is maximal at `k=1`.
   This supports reciprocal boundary points under Csoka's conjecture/stability,
   but FMP note the corresponding generalization appears unknown.

No exact "weighted Bernoulli mean tail" or "cyclic interval random allocation"
theorem was found that closes the assertion.
