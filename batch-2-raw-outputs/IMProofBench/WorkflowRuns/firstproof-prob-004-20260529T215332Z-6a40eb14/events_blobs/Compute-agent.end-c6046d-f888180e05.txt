# Round 23 response: Guth Ch. 8 constructions do give a counterexample pattern

Bottom line: after correcting the exponent model for the technical short-side stretch variant, I found a genuine asymptotic counterexample pattern to the stated theorem.  The old searches missed it because the interpolated technical variant in `code/guth_ch8_exponent_search.py` tied together two exponents that are independent in the thesis.

Files produced:

- `code/round23_guth_ch8_search.py`
- `data/round23/guth_ch8_search_report.txt`

## Source/PDF verification

I checked the thesis text and page image.  The double pinching target on thesis p.148 is visibly
\[
R_1^2/A \times A \times A \times B,
\]
not \(R_1/A\).  The OCR ambiguity is real: `pdftotext` prints `R1/A` in one place and `R2/A` in Step 5/final, but the page image `data/round11_page_images/thesis_p148-148.png` clearly has the superscript: \(R_1^2/A\).  This also matches Step 5: the linear map from
\[
R_1\times R_1\times A^2/R_1\times AB/R_1
\]
to
\[
R_1^2/A\times A\times A\times B
\]
has exponent factors \(R_1/A,A/R_1,R_1/A,R_1/A\), so its 2-dilation exponent is \(0\).

The five encoded maps are:

1. snake:
\[
(r_1,r_2,r_3,r_4)\mapsto (r_1,r_2,r_3-a,r_4+a),\quad 0\le a\le r_3-r_2.
\]

2. codimension-one snake:
\[
(r_1,r_2,r_3,r_4)\mapsto (r_1,r_2-a,r_3+a,r_4-a),
\quad a\le r_2-r_1,\;2a\le r_4-r_3.
\]

3. short-side stretch:
\[
(r_1+a,r_2-3a,r_3+a,r_4-a),
\quad 4a\le r_2-r_1,\;2a\le r_4-r_3.
\]

4. pinching:
\[
(a,a,a,b),\quad a\le r_1,\;2a+b\le r_2+r_3+r_4.
\]

5. double pinching:
\[
(2r_1-a,a,a,b),\quad a\ge r_1,\;2a\le r_2+r_3,\;3a+b\le r_1+r_2+r_3+r_4.
\]

The technical short-side variant is the important correction.  The thesis says
\[
\lambda R_1\times \lambda^{-3}R_2\times A\times B,
\quad \lambda^4<R_2/R_1,\quad R_3<A<(R_3R_4)^{1/2},\quad R_3R_4=AB.
\]
Thus, in exponents, \(\ell=\log_L\lambda\) and \(a=\log_L A\) are independent:
\[
(r_1+\ell,\;r_2-3\ell,\;a,\;r_3+r_4-a).
\]
The older workspace code used one variable for both \(\ell\) and \(a\), which artificially excluded the hit below.

## Explicit counterexample pattern

Let
\[
S=(1,1,L,L),\qquad s=(0,0,1,1),
\]
and let
\[
R=(L^{-1/6},L^{5/6},L^{5/6},L^{5/6}),\qquad
r=(-1/6,5/6,5/6,5/6).
\]

Start with an initial diagonal linear map
\[
R\longrightarrow X_0=(1,L^{2/3},L^{2/3},L^{2/3}),
\qquad x_0=(0,2/3,2/3,2/3).
\]
The expansion exponents are
\[
x_0-r=(1/6,-1/6,-1/6,-1/6),
\]
so the largest two sum to \(0\).  Hence this initial linear map has bounded 2-dilation.

Apply Guth double pinching to \(X_0\), with \(A\) of exponent \(0\) and \(B\) of exponent \(2\).  This gives
\[
X_1=(1,1,1,L^2),\qquad x_1=(0,0,0,2).
\]
Exponent constraints:
\[
A\ge R_1:\;0\ge0,\qquad
A^2\le R_2R_3:\;0\le4/3,\qquad
A^3B\le \operatorname{Vol}(X_0):\;2\le2.
\]
The equalities are only exponent equalities; constants can be chosen to make Guth's strict inequalities true.

Now apply the corrected technical short-side interpolation to \(X_1\), with \(\lambda\) of exponent \(0\), output \(A\) of exponent \(1\), and hence output \(B\) also of exponent \(1\).  This gives
\[
X_1\longrightarrow (1,1,L,L)=S.
\]
Exponent constraints:
\[
\lambda^4\le R_2/R_1:\;0\le0,\qquad
R_3\le A\le (R_3R_4)^{1/2}:\;0\le1\le1,\qquad
AB=R_3R_4.
\]
Again, the boundary equalities are made strict by constants, without changing exponents.

## Violation of the three target conclusions

For this \(R,S\),
\[
r_1-s_1=-1/6<0,
\]
\[
r_3+r_4-s_3-s_4=5/6+5/6-1-1=-1/3<0,
\]
and
\[
\sum r_i-\left(s_1+\tfrac12s_2+\tfrac32s_3+s_4\right)
=7/3-5/2=-1/6<0.
\]
Equivalently,
\[
R_1/S_1=L^{-1/6},\quad
R_3R_4/(S_3S_4)=L^{-1/3},\quad
\operatorname{Vol}(R)/(S_1S_2^{1/2}S_3^{3/2}S_4)=L^{-1/6}.
\]

The total map has bounded 2-dilation, degree 1, and maps boundary to boundary: it is an initial linear diffeomorphism followed by Guth's degree-one Ch. 8 maps.  After multiplying all side lengths of \(R\) by a fixed constant depending only on the bounded dilation constant, the total map has \(\Dil_2\le1\).  This constant rescaling does not affect the negative powers above, so for any fixed theorem constant \(k>0\), taking \(L\) large gives
\[
R_1\le kS_1,\qquad R_3R_4\le kS_3S_4,\qquad
\operatorname{Vol}(R)\le kS_1S_2^{1/2}S_3^{3/2}S_4.
\]
So this appears to genuinely disprove the stated theorem, assuming Guth's technical short-side interpolation is allowed as stated.

## Search log

The script `code/round23_guth_ch8_search.py` ran LP searches over exponent variables with initial and terminal linear 2-contractions.  It found positive margin \(m=1/6\) already at depth \(\le3\), and randomized depth \(5\)-\(8\) searches rediscovered the same pattern with inserted zero/nonessential moves.  See `data/round23/guth_ch8_search_report.txt`.

Important diagnostic: the old "no hit" conclusion was caused by the old interpolation encoding, not by the double-pinching OCR ambiguity.  With the corrected two-parameter interpolation, both pinching and double-pinching routes can produce the intermediate exponent rectangle \((0,0,0,2)\), and the technical short-side map then sends it to \((0,0,1,1)\).
