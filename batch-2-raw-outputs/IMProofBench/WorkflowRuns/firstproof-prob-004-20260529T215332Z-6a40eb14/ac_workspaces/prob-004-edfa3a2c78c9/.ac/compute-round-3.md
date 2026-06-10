# Compute worker reply — round 3
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c2-a28188/compute_workspace_round_3.zip

---

# Round 3 compute report: mixed rectangle estimate and the scaling test

## Verdict

**Unresolved, leaning "true but still missing a new mixed-face argument."** I did not find an exact theorem in Guth's thesis, arXiv:0710.0403, the width-volume paper, or the minimax paper that implies the desired mixed estimate
\[
R_1R_2^2\gtrsim S_1S_2S_3,\quad R_1\ll S_1,\quad R_3R_4\lesssim S_3S_4
\Longrightarrow
\operatorname{Vol}(R)\gtrsim S_1S_2^{1/2}S_3^{3/2}S_4 .
\]
The natural counterexample route
\[
(L^{-1},L^4,L^5,L^6)\to(1,L,L^5,L^6)\to(1,1,L^6,L^6)
\]
also does **not** work: the first short-side stretch is a valid Guth map, but the residual map is ruled out by Guth's boundary/rational-homotopy estimates for the boundary degree-one map.

Files produced:

- `code/round3_rectangle_checks.py`: reproducible exponent checks.
- `data/round3_rectangle_checks.txt`: output table.
- `notes/round3_source_excerpts.md`: source excerpt notes.

## Source references checked

1. Guth, *Area-contracting maps between rectangles*, MIT thesis, 2005. Local file: `papers/guth_area_contracting_thesis_2005.pdf`; MIT handle recorded in `data/guth_thesis_handle.html`.
2. Guth, *Area-expanding embeddings of rectangles*, arXiv:0710.0403. Local file: `papers/guth_area_expanding_rectangles_0710.0403.pdf`.
3. Guth, *The width-volume inequality*, arXiv:math/0609569. Local file: `papers/guth_width_volume_inequality_math0609569.pdf`.
4. Guth, *Minimax problems related to cup powers and Steenrod squares*, arXiv:math/0702066. Local file: `papers/guth_minimax_cup_powers_steenrod_squares_math0702066.pdf`.

The closest standard theorem is arXiv:0710.0403, Estimate 1, p.10:

> Suppose that \(U\) is an open set in \(R\) and that \(\Phi:(U,\partial U)\to(S,\partial S)\) is a map of pairs of degree \(D>0\). If \(0\le j<k\le l\le n\), then
> \[
> \operatorname{dil}_k(\Phi)\ge c(n)Q_1\cdots Q_j(Q_{j+1}\cdots Q_l)^{(k-j)/(l-j)}.
> \]

This is not enough for the desired mixed estimate. Guth explicitly says on the same page that Estimate 1 is more general than the embedding theorem because \(\Phi\) need not be a diffeomorphism, but it is still only the monomial quotient estimate.

The most relevant thesis lower bounds are:

- Thesis Prop. 8.1.2, pp.142-144: a relative \(2\)-cycle in \(R\) of area \(<\frac12R_1R_2\) fills with volume \(\lesssim R_1R_2^2\).
- Thesis Prop. 8.1.3, p.144: for a \(2\)-contracting diffeomorphism, \(CR_1R_2^2<S_1S_2S_3\) implies \(R_3R_4\gtrsim S_3S_4\). The current `answer.tex` adaptation to degree-one maps of pairs looks sound via slicing currents.
- Thesis pp.129-130: rational-homotopy inequalities. The relevant boundary inequality in dimension \(4,k=2\) is
  \[
  R_2R_3^2R_4\gtrsim S_2S_3^2S_4.
  \]
  Although the surrounding chapter phrases consequences for diffeomorphisms, Prop. 7.7.1 immediately before is for **any** \(k\)-contracting map between ellipsoids. A degree-one pair map \(f:(R,\partial R)\to(S,\partial S)\) induces a degree-one boundary map \(\partial R\to\partial S\), so this boundary obstruction applies up to bilipschitz constants.
- Thesis Prop. 8.1.1, pp.140-142: ellipsoid-boundary estimate. In the case \(R_2^2<S_2S_3\), it gives \(R_3R_4\gtrsim S_3S_4\); in the case \(R_2^2>S_2S_3\), it gives \(R_2R_3R_4\gtrsim S_2^{1/2}S_3^{3/2}S_4\). This is close to the missing estimate, but lacks the extra factor \(S_1\) needed after multiplying by the actual \(R_1\).

## Scaling test \(R=(L^{-1},L^4,L^5,L^6),\ S=(1,1,L^6,L^6)\)

Bad ratios:
\[
R_1/S_1=L^{-1},\quad
R_3R_4/(S_3S_4)=L^{-1},\quad
\frac{\operatorname{Vol}(R)}{S_1S_2^{1/2}S_3^{3/2}S_4}=L^{-1}.
\]
The complementary hypothesis is satisfied strongly:
\[
\frac{R_1R_2^2}{S_1S_2S_3}=L.
\]

All Guth Estimate 1 monomials are \(O(1)\) for \(k=2,3,4\). For \(k=2\), with \(Q=S/R=(L,L^{-4},L,1)\), the exponents are
\[
-3,\ -4/3,\ -1,\ -3,\ -1/2,\ 0.
\]
Thus Estimate 1 does not rule out a bounded-\(\Dil_2\) map.

Boundary/rational-homotopy checks for the full scaling also pass:
\[
R_2R_3^2R_4/S_2S_3^2S_4=L^2,
\]
\[
R_1R_2R_3^2R_4/(S_1S_2S_3^2S_4)=L,
\]
\[
R_1R_2^2R_3^2R_4/(S_1S_2^2S_3^2S_4)=L^5.
\]
The ellipsoid-boundary B3a estimate is exactly saturated:
\[
R_2R_3R_4=S_2^{1/2}S_3^{3/2}S_4=L^{15}.
\]
So the full scaling test remains a genuine stress test for the desired theorem: it is not killed by any known monomial, boundary, or rational-homotopy inequality I found.

## Residual map after short-side stretch

The first arrow
\[
(L^{-1},L^4,L^5,L^6)\to(1,L,L^5,L^6)
\]
is Guth's short-side-stretch technical variant from thesis p.146 with \(A=L\): \(A^4=L^4<R_2/R_1=L^5\). This part is not contradicted by Estimate 1.

The residual target is
\[
R'=(1,L,L^5,L^6),\qquad S=(1,1,L^6,L^6).
\]
For \(R'\to S\), Estimate 1 still gives no obstruction: all \(k=2\) and \(k=3\) exponents are \(\le0\). The axis-linear map has \(2\)-dilation \(L\), so any construction would have to be genuinely nonlinear.

However, the boundary obstruction rules it out. For \(R'\to S\), the boundary rational-homotopy inequality gives
\[
R'_2(R'_3)^2R'_4 \gtrsim S_2S_3^2S_4.
\]
The two sides scale as
\[
L\cdot L^{10}\cdot L^6=L^{17},\qquad 1\cdot L^{12}\cdot L^6=L^{18}.
\]
Thus the inequality fails by a factor \(L\). Equivalently, the ellipsoid-boundary B3b regime applies because
\[
(R'_2)^2=L^2<S_2S_3=L^6,
\]
and B3b would require
\[
R'_3R'_4\gtrsim S_3S_4,
\]
but \(L^{11}\ll L^{12}\).

Conclusion: the decomposition through \((1,L,L^5,L^6)\) cannot yield a bounded-\(\Dil_2\) degree-one pair map. A product snake/pinching construction also fails for the same reason: crossing a 3D snake with an identity direction leaves a large mixed \(2\)-dilation, and the boundary inequality detects precisely this missing mixed control.

## Direct proof attempt and remaining gap

The clean coarea route would be:

1. Pull back a three-parameter family of \(1\)-cycles indexed by \((y_1,y_3,y_4)\).
2. Use \(\Dil_3\le1\) to get
   \[
   \operatorname{Vol}(R)\ge \int \operatorname{length}(Z_{y_1,y_3,y_4})\,dy_1dy_3dy_4.
   \]
3. Prove each relevant \(Z\) has length \(\gtrsim (S_2S_3)^{1/2}\).

The obstruction is still the same as in `answer.tex`: the obvious intervals
\[
\{y_1\}\times[0,S_2]\times\{y_3\}\times\{y_4\}
\]
fill through the \(x_1\)-faces with area \(O(S_1S_2)\), not \(\gtrsim S_2S_3\). Boundary solid-torus circles have the right filling lower bound inside \(\partial S\), but as chains in the full pair \((S,\partial S)\) they can escape through the short \(x_1\) direction. The boundary degree alone does not label which parts of \(\partial R\) map to the \(x_1\)-faces, so I do not see a valid triad-relative homology class that prevents this escape.

Therefore the remaining proof gap is precise:

- Need a chain-level tightening or mixed family of \(1\)-cycles whose fillings are forbidden to pass through the \(x_1\)-faces despite only having a map of pairs.
- Or need a new theorem strengthening Guth's boundary ellipsoid B3a by coupling it to interior degree and the short \(R_1/S_1\) direction.
- Existing Guth monomial estimates, width/packing estimates, and rational-homotopy inequalities do not supply that coupling.

## Bottom line

No counterexample construction is currently known from Guth's listed maps. The most tempting residual construction is ruled out. But the full scaling test passes every standard obstruction I checked, so a proof of the original problem still requires a genuinely new mixed interior-boundary estimate, not just a citation to Estimate 1 or to the known boundary ellipsoid inequalities.
