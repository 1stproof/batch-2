# Round 17 Literature Notes: Shifted Down-Sets

Target statement:

If `D` is a shifted down-set on `[n]`, `p 1 notin P(D)`, and
`lambda = p/(1-p) <= 1/2`, then

```tex
Z_\lambda(D) <= (1+\lambda)^{n-1}
```

equivalently `mu_p(D) <= 1-p`.

## Most relevant references found

1. P. Frankl and N. Tokushige, "Weighted multiply intersecting families",
   Studia Sci. Math. Hungar. 40 (2003), 287--291, DOI
   `10.1556/sscmath.40.2003.3.2`.
   Local copy:
   `papers/round17/frankl-tokushige-2003-weighted-multiply-intersecting.pdf`.

   Theorem: if `F` is `r`-wise intersecting and `0 < w <= (r-1)/r`, then
   `mu_w(F) <= w`, with equality for a star. This exactly explains the
   reciprocal endpoints in the complement/intersection formulation. It does
   not imply the needed non-reciprocal strip, because for `w > (r-1)/r` the
   maximum measure of arbitrary `r`-wise intersecting families tends to 1.
   Any use here must exploit the extra weighted-threshold or shifted-complex
   structure, not just `r`-wise intersection.

2. P. Frankl and A. Kupavskii, "Simple juntas for shifted families",
   Discrete Analysis 2020:14, DOI `10.19086/da.14507`, arXiv `1901.03816`.
   Local copy:
   `papers/round17/frankl-kupavskii-2020-simple-juntas-shifted.pdf`.

   This is relevant because it formalizes the philosophy that many extremal
   questions can be reduced to shifted families and then approximated by
   juntas with center `[j]`. It gives nearly-linear bounds for a multi-family
   Erdos matching problem. I did not see a direct exact weighted/nonuniform
   statement that would imply the target inequality.

3. C. J. Klivans, "Threshold graphs, shifted complexes, and graphical
   complexes", Discrete Math. 307 (2007), 2591--2597, arXiv `math/0703114`.
   Local copy:
   `papers/round17/klivans-2007-threshold-shifted-graphical.pdf`.

   Useful background: shifted complexes are order ideals in the componentwise
   partial order; threshold graphs are exactly one-dimensional shifted
   complexes. In higher dimensions shifted complexes strictly extend threshold
   behavior, so proving the original weighted-threshold conjecture would not
   automatically prove every shifted statement unless the separating threshold
   super-complex is used carefully.

4. P. H. Edelman, T. Gvozdeva, and A. Slinko, "Simplicial complexes obtained
   from qualitative probability orders", arXiv `1108.3700`; Journal of
   Discrete Mathematics 2013.
   Local copy:
   `papers/round17/edelman-gvozdeva-slinko-2011-qual-prob-complexes.pdf`.

   They place threshold complexes inside initial segment complexes and those
   inside shifted complexes, with both containments strict. This is useful
   negative guidance: shiftedness alone is much broader than thresholdness.

5. N. Alon, P. Frankl, H. Huang, V. Rodl, A. Rucinski, and B. Sudakov, "Large
   matchings in uniform hypergraphs and the conjectures of Erdos and Samuels",
   JCTA 119 (2012), 1200--1215, arXiv `1107.1219`.
   Local copy:
   `papers/round17/alon-frankl-huang-rodl-rucinski-sudakov-2011-large-matchings.pdf`.

   Relevant for the fractional matching/cover vocabulary. The results are
   uniform and asymptotic/degree-threshold in nature. I did not find an exact
   nonuniform independence-polynomial bound of the target form.

6. R. Fokkink, L. Meester, and C. Pelekis, "Optimizing stakes in simultaneous
   bets", ALEA 20 (2023), 153--165, DOI `10.30757/ALEA.v20-07`, arXiv
   `2002.06804`.
   Existing local copies are in `papers/`. This remains the closest probability
   framework: the desired complement statement is a strict near-hypotenuse
   case for convex combinations of Bernoulli variables. Their proved regions do
   not cover the full strip `q < t` with `q >= 2/3`.

## Takeaway

I did not find a published theorem that directly implies the shifted theorem.
The closest exact theorem is Frankl--Tokushige at the reciprocal endpoints
`q=(r-1)/r`; the closest probability framework is Fokkink--Meester--Pelekis.
The shifted-complex literature supports the reduction and suggests junta/stability
methods, but the target inequality is exact, nonuniform, and partition-function
weighted, which seems outside the quoted theorems.
