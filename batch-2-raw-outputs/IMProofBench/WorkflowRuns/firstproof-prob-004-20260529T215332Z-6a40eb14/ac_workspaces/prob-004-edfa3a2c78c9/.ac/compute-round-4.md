# Compute worker reply — round 4
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c3-5e5a6f/compute_workspace_round_4.zip

---

# Round 4 compute report: mixed estimate / counterexample fork

## Verdict

**Still unresolved, but narrowed.** The proposed *single-slice* inequality
\[
\Fill_R(Z)\le C\,\Mass(Z)^2/S_1
\]
is false under the obvious slice-only hypotheses, even with \(R_1\ll S_1\), degree one, and \(J_2(g)\le 1\). Thus that proof route cannot work unless it uses extra data from a whole neighboring family of slices / mixed Jacobian bounds of the ambient map \(f\).

I did **not** find a valid counterexample to the original problem from Guth's maps. The tempting route through a 2-expanding embedding still reduces exactly to an uncontrolled extension problem. A shallow exponent search of Guth Chapter 8.2 maps also found no valid composition reaching the stress-test counterexample.

Files:
- `code/guth_ch8_exponent_search.py`
- `data/guth_ch8_exponent_search_round4.txt`
- `code/round4_double_pinch_counterexample.py`
- `data/round4_double_pinch_counterexample.txt`

## 1. The key slice inequality is false as stated

Fix \(S_1\le S_2\), choose \(0<r\ll S_1\), set \(B=S_1S_2/r\), and take
\[
R=[0,r]_{x_1}\times[0,B]_{x_2}\times[0,L]_{x_3}\times[0,L]_{x_4},
\qquad L\gg B.
\]
Let
\[
Z=[0,r]\times[0,B]\times\{L/2\}\times\{L/2\}.
\]
This is a relative integral \(2\)-cycle in \(R\), with boundary on the \(x_1,x_2\)-faces. Define
\[
g(x_1,x_2)=\left(S_1x_1/r,\; S_2x_2/B\right).
\]
Then \(g:Z\to[0,S_1]\times[0,S_2]\) has relative degree one and
\[
J_2 g=\frac{S_1S_2}{rB}=1,\qquad \Mass Z=rB=S_1S_2.
\]
However \(\Fill_R(Z)\gtrsim S_1S_2L\). The calibration proof is the same as in the current `answer.tex`: choose \(\psi(x_3,x_4)\) zero on the boundary of the \((x_3,x_4)\)-square, \(\psi(L/2,L/2)\gtrsim L\), \(|d\psi|\le1\), and integrate
\[
\omega=dx_1\wedge dx_2\wedge d\psi.
\]
Boundary terms on the \(x_1,x_2\)-faces vanish because \(dx_1\wedge dx_2=0\), and boundary terms on the \(x_3,x_4\)-faces vanish because \(\psi=0\). Hence every relative filling has mass \(\gtrsim S_1S_2L\).

The proposed upper bound gives only
\[
C\Mass(Z)^2/S_1=C S_1S_2^2,
\]
so it fails for \(L\gg S_2\). This example even has \(R_1=r\ll S_1\). What it lacks is precisely the ambient mixed \(2\)-dilation information: any full map extending \(g\) by target normal coordinates would have huge mixed Jacobians such as \(du\wedge dx_3\). Therefore a valid proof must use a family \(Z_y=f^{-1}(P_y)\), not just a single slice with \(J_2(g)\le1\).

## 2. Expanding-embedding route

For the stress test
\[
R^0=(L^{-1},L^4,L^5,L^6),\qquad S=(1,1,L^6,L^6),
\]
the bad ratios are
\[
R^0_1/S_1=L^{-1},\quad R^0_3R^0_4/(S_3S_4)=L^{-1},\quad
\Vol(R^0)/(S_1S_2^{1/2}S_3^{3/2}S_4)=L^{-1}.
\]
Guth arXiv:0710.0403 Theorem 2 (p.1, constructed on pp.17-18 via Lemmas 7.1 and 7.2) gives a \(2\)-expanding embedding \(S\hookrightarrow \lambda R^0\) after fixed \(L\)-independent scaling \(\lambda\), because all \((**)\) monomial conditions hold up to constants; the \(j=1,l=4,k=2\) condition is saturated before scaling.

But this gives only an inverse
\[
\Phi:U=I(S)\to S
\]
on the embedded image. Guth's Estimate 1 (arXiv:0710.0403, p.10) explicitly uses this local inverse on \(U\), and says it is enough for the embedding obstruction. It does **not** produce a map of pairs \(\lambda R^0\to S\).

The extension obstruction is metric, not topological: the complement of a folded image can be collapsed only if the boundary data on nearby sheets can be interpolated without creating large mixed \(2\)-dilation. This is exactly why Guth's explicit degree-one maps in thesis §8.2 are built with special retractions and pinches onto \(1\)-dimensional or \(2\)-dimensional exceptional sets. The general Theorem 2 folding construction does not provide such controlled pair extension.

The earlier decomposition
\[
(L^{-1},L^4,L^5,L^6)\to(1,L,L^5,L^6)\to(1,1,L^6,L^6)
\]
still fails at the second arrow. The residual map
\[
R'=(1,L,L^5,L^6)\to S=(1,1,L^6,L^6)
\]
violates Guth's boundary/rational-homotopy obstruction
\[
R'_2(R'_3)^2R'_4\gtrsim S_2S_3^2S_4,
\]
since the two sides scale as \(L^{17}\) and \(L^{18}\). This is the precise obstruction for that natural extension attempt.

## 3. Source facts checked

- Guth, *Area-expanding embeddings of rectangles*, arXiv:0710.0403:
  - Theorem 1 and Theorem 2, p.1: necessary/sufficient monomial conditions for \(k\)-expanding embeddings, up to constants.
  - Estimate 1, p.10: for a degree \(D>0\) map of pairs \((U,\partial U)\to(S,\partial S)\),
    \[
    \operatorname{dil}_k\Phi\ge c(n)Q_1\cdots Q_j(Q_{j+1}\cdots Q_l)^{(k-j)/(l-j)}.
    \]
    The text immediately notes that for an embedding \(I:S\to R\), one takes \(U=I(S)\) and \(\Phi=I^{-1}\).
  - Lemmas 7.1 and 7.2, pp.17-18: Theorem 2 is built from a \(k\)-contracting linear map and a \(1\)-expanding folding embedding.

- Guth thesis, *Area-contracting maps between rectangles*:
  - p.139: Chapter 8 is explicitly “partial results” for \(2\)-contracting diffeomorphisms between \(4\)-rectangles.
  - Proposition 8.1.1, pp.140-142: boundary ellipsoid estimates B1/B2/B3a/B3b.
  - Proposition 8.1.2, pp.143-144: small relative \(2\)-cycle filling in a rectangle. OCR drops a square in places; the proof/usage gives \(\lesssim R_1R_2^2\).
  - Proposition 8.1.3, p.144: if \(CR_1R_2^2<S_1S_2S_3\), then \(R_3R_4\gtrsim S_3S_4\).
  - §8.2, pp.144-148: five explicit global degree-one maps of pairs with bounded \(2\)-dilation.
  - p.149: Guth says the known lower/upper techniques are “not even close” to estimating best \(2\)-dilation between \(4\)-rectangles.
  - p.153: a general strategy for controlled extension is stated: remove a \(1\)-dimensional polyhedron from the range, embed the complement, then extend the inverse by mapping the rest of the domain to that polyhedron. This supports the obstruction above: a controlled extension requires special low-dimensional collapse data, not just a \(2\)-expanding embedding.

## 4. Exponent-search notes

I modeled the Chapter 8.2 maps as exponent transformations. For the stress test \(R^0\to S\), a beam search with grid steps \(1\) and \(1/2\), depth \(3\), found no route ending in a final linear \(2\)-contracting map. From the residual state \((0,1,5,6)\), the best single move is the codimension-one snake to \((0,1/2,11/2,11/2)\), but the remaining final linear \(2\)-dilation exponent is still \(+1\).

Important correction from the computation: thesis p.148 OCR can make the double pinching target look like
\[
R_1/A\times A\times A\times B.
\]
That is inconsistent with Guth Estimate 1 and with the Step 3-to-Step 5 linear map. The correct target is
\[
R_1^2/A\times A\times A\times B.
\]
With the corrected exponent \(2r_1-a\) in \(\log_L\) coordinates, the apparent double-pinching counterexamples disappear; see `data/round4_double_pinch_counterexample.txt`.

## Bottom line

The single-slice inequality is definitively false. The remaining viable proof route must exploit the whole sliced family and ambient mixed \(2\)-Jacobian controls. The expanding-embedding route would give a counterexample if one could uniformly extend the inverse to a global pair map, but Guth's theorems do not supply that extension, and the most natural residual extension is blocked by the boundary inequality.
