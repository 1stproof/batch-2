# Round 27 response

I read the current `answer.tex` and `research_notes.tex` first.  I saved two new scripts/logs:

- `code/round27_weighted_level_probe.py`, output `data/round27_weighted_level_probe.txt`.
- `code/round27_aux_composition_lp.py`, output `data/round27/aux_composition_lp_report.txt`.

## 1. Weighted \(f_1\)-level probe

The clean \(f_1\)-level package is valid but still does not close the hard regime.
Let \(u=f_1\), \(M_t=\langle [R,\partial R],u,t\rangle\), \(g=(f_2,f_3,f_4)|_{M_t}\), and \(w=|\nabla u|^{-1}\).  For a.e. central regular \(t\), slicing naturality gives
\[
g_\#M_t=\pm [[0,S_2]\times[0,S_3]\times[0,S_4],\partial],
\]
so \(g\) has relative degree \(1\) onto the target \(3\)-rectangle.  At smooth regular points, if \(\mu_1\ge \mu_2\ge\mu_3\) are the singular values of \(dg|_{TM_t}\), then
\[
\mu_1\le w,\qquad \mu_1\mu_2\le 1,\qquad
J_3g\le \min(w^3,1)\le w.
\]
Therefore the unconditional level bound is only
\[
\int_{M_t}w\,d\mathcal H^3\ge S_2S_3S_4.
\]

The proposed stronger level estimate is false without the hard-regime hypotheses, even for a global degree-one \(2\)-contracting map.  Take \(R=S=(1,1,L,L)\), \(f=\mathrm{id}\).  Then every central \(f_1\)-level has \(w=1\) and
\[
\int_{M_t}w=L^2,\qquad
S_2^{1/2}S_3^{3/2}S_4=L^{5/2}.
\]
The ratio is \(L^{-1/2}\to0\).  The script verifies this numerically for \(L=10,100,10^4\).

For any interval \(I\subset(0,S_1)\), coarea gives the exact identity
\[
\int_I\int_{M_t}w\,d\mathcal H^3\,dt
=\operatorname{Vol}(u^{-1}(I)).
\]
Thus an averaged hard-regime strengthening over central \(t\)'s is exactly a lower bound for the central \(f_1\)-slab volume:
\[
\operatorname{Vol}(u^{-1}I)\gtrsim |I|\,S_2^{1/2}S_3^{3/2}S_4.
\]
I found no hard-regime counterexample to this slab statement, but I also found no derivation from the level-set data alone.  Proving it would need a new ingredient preventing the \(3\)-dimensional level filling from escaping through the ambient \(x_1\)-faces; this is essentially the same missing averaged parametric tightening, repackaged.

## 2. Auxiliary-composition probe

I encoded the valid Guth Chapter 8.2 maps in exponent variables \(x_i=\log_L R_i\), with sorted side lengths after each move.  The move set in `code/round27_aux_composition_lp.py` is:

\[
\begin{array}{ll}
\text{linear:} & \text{all pair expansion sums }\le0,\\
\text{snake:} & (x_1,x_2,x_3-a,x_4+a),\quad 0\le a\le x_3-x_2,\\
\text{codim snake:} & (x_1,x_2-a,x_3+a,x_4-a),\quad a\le x_2-x_1,\ 2a\le x_4-x_3,\\
\text{short stretch:} & (x_1+a,x_2-3a,x_3+a,x_4-a),\\
& 4a\le x_2-x_1,\ 2a\le x_4-x_3,\\
\text{short technical:} & (x_1+a,x_2-3a,x_3,x_4),\quad 4a\le x_2-x_1,\\
\text{technical interpolation:} & (x_1+a,x_2-3a,a,x_3+x_4-a),\\
& 4a\le x_2-x_1,\ x_3\le a\le (x_3+x_4)/2,\\
\text{pinch:} & (a,a,a,b),\quad a\le x_1,\ 2a+b\le x_2+x_3+x_4,\ b\ge a,\\
\text{double pinch:} & (2x_1-a,a,a,b),\\
& a\ge x_1,\ 2a\le x_2+x_3,\ 3a+b\le x_1+x_2+x_3+x_4,\ b\ge a.
\end{array}
\]

Important correction: the technical interpolation is single-parameter.  I did **not** allow the older independent \(\lambda\), output-\(A\) variant; that variant recreates the previously invalid map contradicted by Guth Estimate 1.

The fixed exponent countermodel tested was the known stress family
\[
S=(0,0,1,1),\qquad
R=(-1/5,13/15,13/15,13/15).
\]
Its three theorem ratios have exponents
\[
R_1/S_1=-1/5,\qquad
R_3R_4/(S_3S_4)=-4/15,\qquad
\operatorname{Vol}(R)/(S_1S_2^{1/2}S_3^{3/2}S_4)=-1/10.
\]
For the direct map \(R\to S\), all Guth Estimate 1 exponents for \(k=2,3,4\) are \(\le0\); the maximum is exactly \(0\), saturated by \((k,j,l)=(2,1,4)\).

I then optimized, by LP, over all precomposition and postcomposition words of depth \(\le3\) in the move set above.  For each resulting composite I maximized every published Estimate 1 monomial.  Results:

\[
\begin{array}{c|c|c|c}
\text{search} & \text{depth} & \text{LP objectives} & \max\text{ Estimate 1 exponent}\\ \hline
\text{postcompose} & \le1 & 144 & 0\\
\text{precompose} & \le1 & 144 & 0\\
\text{postcompose} & \le2 & 1168 & 0\\
\text{precompose} & \le2 & 1168 & 0\\
\text{postcompose} & \le3 & 9360 & 0\\
\text{precompose} & \le3 & 9360 & 0
\end{array}
\]

The top saturated postcomposition endpoints include \(S\) itself, the snake endpoint \((0,0,0,2)\), and the pinch/double-pinch endpoint \((0,0,0,2)\); all only saturate \((2,1,4)\).  No positive monomial was found.

Conclusion: this auxiliary-composition strategy, at least at the exponent level and for all corrected Ch. 8.2 words up to depth \(3\), cannot prove the theorem.  The stress family remains an LP countermodel: even after allowed pre/post compositions, Guth's published monomial Estimate 1 never becomes contradictory.  This does not rule out a longer or genuinely new composition argument, but it rules out the obvious finite-word use of the known Chapter 8.2 maps.
