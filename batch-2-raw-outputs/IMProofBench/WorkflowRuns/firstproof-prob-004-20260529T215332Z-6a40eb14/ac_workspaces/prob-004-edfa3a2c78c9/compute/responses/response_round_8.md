# Round 8 response: conditional averaged filling estimate

## Main conclusion

The averaged filling estimate (AF) in the current `answer.tex` is **false as stated**.  There is a very simple diagonal degree-one, \(2\)-contracting family satisfying the slicing degree condition, the pointwise mixed bounds, and the central filling lower bounds, for which
\[
\int_Q \Fill_R(Z_y)\,dy
\gg
R_1 I+\frac{I^2}{S_1|Q|}
+\frac{R_3R_4}{S_3S_4}S_1S_2S_3|Q|.
\]
This counterexample does **not** have \(R_3R_4/S_3S_4\ll1\); it has ratio \(1\).  So it does not disprove the final theorem in the intended hard regime, but it does mean Proposition `conditional averaged filling estimate` cannot be stated for "every map as above".

## Explicit counterexample to (AF) as written

Let \(L\to\infty\), let \(M=L^a\) with \(0<a<1\), and set
\[
S=(1,1,L,L),\qquad R=(1,M,L,L).
\]
Define the linear map of pairs
\[
f(u_1,u_2,u_3,u_4)=\left(u_1,\frac{u_2}{M},u_3,u_4\right).
\]

Checks:

- \(f:(R,\partial R)\to(S,\partial S)\) has degree \(1\): its Jacobian is \(1/M\), and \((1/M)\Vol(R)=\Vol(S)\).
- The singular values are \(1,1,1,1/M\), hence \(\Dil_2(f)=1\).
- For \(F=(f_3,f_4)=(u_3,u_4)\) and central \(Q=[L/3,2L/3]^2\),
  \[
  Z_y=[0,1]\times[0,M]\times\{y_3\}\times\{y_4\}.
  \]
- \(G=(f_1,f_2)\) maps \(Z_y\) to \([0,1]^2\) with relative degree \(1\).
- On \(Z_y\), \(\lambda=\|dG|_{TZ_y}\|=1\), so
  \[
  \int_{Z_y}\lambda^2=M,\qquad I=\int_Q\int_{Z_y}\lambda^2\sim ML^2.
  \]
- The central filling is actually \(\Fill_R(Z_y)\sim ML\).  Lower bound: choose a \(1\)-Lipschitz \(\psi\) on the \((u_3,u_4)\)-rectangle, zero on its boundary and \(\psi(y)\gtrsim L\).  The calibration
  \[
  du_1\wedge du_2\wedge d\psi
  \]
  gives \(\Mass Y\gtrsim ML\) for every relative filling \(Y\) of \(Z_y\).  The matching upper bound is the slab to a normal boundary face.

Therefore
\[
\int_Q\Fill_R(Z_y)\,dy\sim ML^3.
\]
The three terms on the right side of (AF) are
\[
R_1I\sim ML^2,\qquad
\frac{I^2}{S_1|Q|}\sim M^2L^2,\qquad
\frac{R_3R_4}{S_3S_4}S_1S_2S_3|Q|\sim L^3.
\]
For \(M=L^a\), the left side has exponent \(a+3\), while the right side has exponent
\[
\max\{a+2,2a+2,3\}.
\]
For every \(0<a<1\), the gap is positive; for \(a=1/2\), (AF) fails by \(L^{1/2}\).

The pointwise weighted coarea bound is not the issue here: \(\lambda^2J_2F=1\) everywhere.  The failure is that the estimate has no term detecting a long tangential source direction that is collapsed by \(G\) but still contributes to filling distance in the normal \((u_3,u_4)\)-rectangle.

Reproducible check: `code/round8_af_model_checks.py`, output in `data/round8_af_model_checks.txt`.

## What remains open

I did **not** find a genuine counterexample in the intended hard regime
\[
R_1\ll S_1,\qquad R_3R_4/S_3S_4\ll1.
\]
The simple diagonal/permutation search found no small-\(\alpha\) linear model: for diagonal maps with \(F=(f_3,f_4)\) using the normal source coordinates, \(\Dil_2\le1\) forces \(J_2F\le1\), hence \(R_3R_4\ge S_3S_4\).  The old hard fiber model from round 7 has low energy and high filling, but it violates the mixed bound \(|df(v)\wedge df(n)|\le1\) by \(L^{1/5}\), so it is not a valid counterexample.

Recommendation: if the Author still wants to use this route, restrict the missing proposition explicitly to the reduced regime, at least including
\[
R_1\le \kappa S_1,\qquad R_3R_4\le \kappa S_3S_4,
\]
and probably also state that the estimate is only asserted after the first-alternative reduction.  The current universal formulation is untenable.

## Literature search

I searched the local Guth thesis/PDF text, arXiv sources, and recent parametric inequality literature.  I found no theorem matching (AF).

Closest Guth sources:

- Guth, *Area-expanding embeddings of rectangles*, arXiv:0710.0403.  Relevant local files: `papers/guth_area_expanding_rectangles_0710.0403.pdf`, `data/pdftxt/guth_area_expanding_0710.0403.txt`.
  - Theorem 3 / Section 1, pp. 7--9: rectangular relative isoperimetric profile.  For \(k=2,n=4\), this gives the \(A^{3/2}\) and \(A^2/R_1\) branches already used in `answer.tex`.
  - Estimate 1, pp. 10 and 12: the monomial degree/k-dilation estimate.
  - Section 6, pp. 13--16: "Tightening a complex of cycles."  This is the closest structural analogue: subdivide, replace chains skeleton-by-skeleton using isoperimetry, preserve degree by the Key Lemma, then apply the sweepout lemma.  It gives supremal chain-volume bounds, not the averaged weighted filling estimate (AF).

- Guth, *Area-contracting maps between rectangles*, PhD thesis, MIT, 2005.  Local files: `papers/guth_area_contracting_thesis_2005.pdf`, `data/pdftxt/guth_thesis_2005.txt`.
  - Chapter 8, Proposition 8.1.2, thesis p. 143: a relative \(2\)-cycle in a \(4\)-rectangle with area \(<\frac12R_1R_2\) fills with volume \(\lesssim R_1R_2^2\) (OCR sometimes drops the square).
  - Proposition 8.1.3, thesis p. 144: if \(CR_1R_2^2<S_1S_2S_3\), then \(R_3R_4\gtrsim S_3S_4\).  This is exactly the first-alternative argument now in the draft.
  - Boundary inequality B3a/B3b, thesis pp. 140--142: the inverse-image-of-circles argument gives \(R_2R_3R_4\gtrsim S_2^{1/2}S_3^{3/2}S_4\) in one case and \(R_3R_4\gtrsim S_3S_4\) in the other.  This has the desired \(S_2^{1/2}S_3^{3/2}\) pattern, but it is a boundary ellipsoid/diffeomorphism argument, not a parametric filling theorem for the interior slices \(Z_y\).

- Guth, *Directional isoperimetric inequalities and rational homotopy invariants*, arXiv:0802.3549.  Downloaded as `papers/guth_directional_isoperimetric_0802.3549.pdf`.
  - Proposition 2.2 gives directional filling estimates for relative cycles in rectangles.
  - Proposition 2.3 gives the corresponding ellipsoid estimate.
  These are non-parametric; they may be useful if one can bound source-directional volumes of \(Z_y\) by the weighted energy, but I do not see that bound from the present hypotheses.

Recent related parametric sources:

- Guth--Liokumovich, *Parametric inequalities and Weyl law for the volume spectrum*, arXiv:2202.11805 / Geometry & Topology 29 (2025), 863--902.  Downloaded as `papers/guth_liokumovich_parametric_inequalities_2202.11805.pdf`.
  - Conjecture 1.3: parametric isoperimetric inequality for localized contractible families.
  - Conjecture 1.6: parametric coarea inequality.
  - Theorem 4.1: parametric coarea for \(1\)-cycles in \(3\)-domains.
  - Theorem 5.1/5.4: parametric isoperimetry for \(0\)-cycles in \(2\)-domains.
  This is conceptually close but not a ready-made estimate for integral \(2\)-cycles in a \(4\)-rectangle, and it uses \(\mathbb Z_2\), flat families, localization, and \(p\)-sweepout scale bounds rather than the weighted fiber energy \(I\).

- Staffa, *Parametric Coarea Inequality for 1-cycles*, arXiv:2410.23195v2, 15 Nov 2025.  Downloaded as `papers/staffa_parametric_coarea_1cycles_2410.23195.pdf`.
  - Theorem 1.2 proves the Guth--Liokumovich parametric coarea conjecture for \(1\)-cycles in arbitrary dimension.
  - It does not supply the needed \(2\)-cycle parametric filling estimate.

Phrase-hit log and extracted source snippets are saved in:

- `data/round8/literature_phrase_hits.txt`
- `data/round8/key_source_excerpts.txt`

## Possible restricted-regime proof skeleton

For the small-\(\alpha\), small-\(R_1\) regime, I would not try to prove (AF) fiberwise.  The counterexample above shows that even harmless collapsed tangential directions destroy a universal fiberwise averaged estimate.  A viable restricted lemma would need to use the whole two-parameter family as a complex of cycles, in Guth's sense.

Precise skeleton to try:

1. Work only after the reductions \(R_1\le\kappa S_1\), \(R_3R_4\le\kappa S_3S_4\), and \(R_1R_2^2\gtrsim S_1S_2S_3\).  State these in the lemma.
2. Discretize \(Q\) into squares of side \(\rho\), and discretize the target \((f_1,f_2)\)-rectangle into vertical strips of width
   \[
   h\sim \frac{S_1|Q|}{I}.
   \]
   The intended balance is that strip-boundary costs summed over \(Q\) produce \(I^2/(S_1|Q|)\).
3. Replace the slice family \(y\mapsto Z_y\) by a cubical complex of cycles: vertices are regular fibers, edges are the sliced \(3\)-chains over parameter edges, and \(2\)-cells are the sliced \(4\)-chains over parameter squares.
4. On each vertex fiber, use \(G=(f_1,f_2)\) and \(\lambda^2\) to choose good strip cuts.  The deformation of the parts to a controlled skeleton should cost \(R_1\int_{Z_y}\lambda^2\), giving \(R_1I\) after averaging.
5. Glue the vertex-level choices across parameter edges using a Guth-style tightening of the complex, not independent fillings.  The obstruction to continuity is exactly where Guth's Key Lemma is needed: tightening must preserve the family degree.
6. The defect term should enter only from parameter \(2\)-cells whose fillings use the actual source \((x_3,x_4)\)-area rather than the target \(Q\)-area.  The total available source normal area is \(R_3R_4\), while the target parameter area is \(\sim S_3S_4\), so the uncontrolled part should be bounded by
   \[
   \frac{R_3R_4}{S_3S_4}F_0|Q|.
   \]

The missing technical lemma is a localized integral-current analogue of Guth--Liokumovich parametric filling, but for the family of \(2\)-cycles \(Z_y\) with a weighted \(G\)-energy budget.  I did not find this lemma in the literature.

