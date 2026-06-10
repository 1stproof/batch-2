# Round 9 report: self-absorbing averaged filling estimate

## Bottom line

I do **not** think the desired estimate
\[
A:=\int_Q \operatorname{Fill}_R(Z_y)\,dy
\le C\left(R_1I+\frac{I^2}{S_1q}\right)
+C\frac{R_3R_4}{S_3S_4}A
\tag{SAF}
\]
is a specialization, or a modest anisotropic variant, of Guth's proof of Estimate 1 in arXiv:0710.0403.  The proof in 0710.0403 is structurally close enough to explain why one might hope for (SAF), but the actual chain complex, dimensions, and estimates do not contain the averaged weighted filling information needed here.

I also did **not** find a hard-regime counterexample with
\[
R_1\le \kappa S_1,\qquad R_3R_4\le \kappa S_3S_4,\qquad \operatorname{Dil}_2(f)\le 1
\]
and failure of the desired volume lower bound.  Diagonal/permutation affine maps are rigorously ruled out in this regime, and a limited exponent search through Guth Chapter 8.2 snake/pinch/double-pinch moves found no hit.

Main reproducible files:

- `data/round9/source_excerpts.md`: line-numbered source excerpts from Guth 0710.0403 and thesis Chapter 8.
- `code/round9_hard_regime_search.py`: diagonal LP and Guth-move exponent scan.
- `data/round9_hard_regime_search.txt`: output of the scan.
- Existing local sources used: `data/arxiv_0710_0403_src/EXEMB2.TEX`, `papers/guth_area_expanding_rectangles_0710.0403.pdf`, `papers/guth_area_contracting_thesis_2005.pdf`.

## What Guth 0710.0403 actually gives

In Section 6 of arXiv:0710.0403, Guth fixes \(0<j<k<l\), defines
\[
R_1\cdots R_j L^{k-j}=\delta(n) S_1\cdots S_j S_j^{k-j},
\]
cuts \(R\) into blocks
\[
R_1\times\cdots\times R_j\times L\times\cdots\times L,
\]
and builds a chain map
\[
C_0:B\to I_{\rm rel}(S),\qquad C_0(F)=\Phi(F\cap U),
\]
where a \(p\)-face of the domain decomposition maps to a relative \(p\)-chain in \(S\).  The tightened complex \(C_1\) agrees with \(C_0\) on the \(k\)-skeleton.  For \(p\ge k+1\), \(C_1(F^{p})\) is filled inductively using the rectangular isoperimetric profile, with bounds of the form
\[
|C_1(F^p)|\lesssim \delta\,S_1\cdots S_j\,S_j^{p-j}.
\]
Then Guth glues to a coarser decomposition with blocks
\[
R_1\times\cdots\times R_l\times L\times\cdots\times L
\]
and obtains the volume bound
\[
|C_1^+(F^p)|
\lesssim
\left(\frac{R_1\cdots R_j}{S_1\cdots S_j}\right)^{(l-k)/(k-j)}
R_1\cdots R_l\,S_j^{p-l}.
\]
The Key Lemma says \(C_1\) has the same degree as \(C_0\); its proof uses gradual refinements \(\Gamma_s\) and a homotopy lemma requiring small mass on all relevant faces.  Finally, the sweepout lemma forces some glued \(p\)-face to have volume \(\gtrsim S_1\cdots S_p\), yielding Estimate 1.

For the current problem, the relevant published index choice \(j=1,k=2,l=4,n=4\) gives only
\[
\left(\frac{R_1}{S_1}\right)^2 R_1R_2R_3R_4
\gtrsim S_1S_2S_3S_4,
\]
i.e.
\[
R_1^3R_2R_3R_4\gtrsim S_1^3S_2S_3S_4.
\]
This is exactly the monomial estimate already in `answer.tex`.

## Why this does not prove (SAF)

The natural complex for the central fibers is dimension-shifted:

- vertices \(v\subset Q\): \(Z_v=\langle [R,\partial R],F,v\rangle\), a relative \(2\)-cycle in \(R\);
- edges \(e\subset Q\): \(W_e=\langle [R,\partial R],F,e\rangle\), a relative \(3\)-chain in \(R\) with \(\partial W_e=Z_{v_+}-Z_{v_-}\) mod \(\partial R\);
- squares \(\tau\subset Q\): \(X_\tau=\langle [R,\partial R],F,\tau\rangle\), a relative \(4\)-chain in \(R\).

If one chooses fillings \(Y_v\) of the vertex cycles, then for an edge
\[
Y_{v_+}-Y_{v_-}-W_e
\]
is a relative \(3\)-cycle, and compatibility over \(2\)-cells is a top-dimensional obstruction.  This is the right chain picture for a possible parametric proof of (SAF), but it is not Guth's same-dimension chain map \(p\)-face \(\mapsto p\)-chain, and Guth's Key Lemma does not directly apply to these vertex fillings.

The two finite terms in (SAF) also do not appear in Guth's proof:

- \(R_1I\) would have to come from a new deformation of the fiber cycles using the weighted tangential energy
  \[
  I=\int_Q\int_{Z_y}\lambda^2,
  \qquad \lambda=\|d(f_1,f_2)|_{\ker dF}\|.
  \]
  Guth's proof uses uniform \(k\)-volume bounds on every \(k\)-face from \(\operatorname{Dil}_k\), not an averaged weighted energy on vertex cycles.
- \(I^2/(S_1q)\) would have to come from a strip/coarea optimization in the \((f_1,f_2)\)-rectangle, roughly choosing strip width \(h\sim S_1q/I\).  Again, there is no such averaged strip selection in Estimate 1.
- The absorbing term \((R_3R_4/S_3S_4)A\) would have to enter at the \(2\)-cell stage of the \(Q\)-complex, where incompatible vertex fillings are charged back to the original average filling.  One would need to prove that the uncontrolled \(2\)-cells occupy only a fraction \(\sim R_3R_4/S_3S_4\) of the target parameter area.  This is exactly the missing parametric/coarea input.

The product-domain generalization at the end of 0710.0403 also does not close this.  It gives
\[
|X|^{(l-j)/(k-j)}|Y|
\gtrsim (S_1\cdots S_j)^{(l-j)/(k-j)}S_{j+1}\cdots S_l
\]
for \(X^j\times Y^{l-j}\times Z^{n-l}\) with \(Y\) rectangular.  This is still a monomial degree estimate.  To turn it into (SAF), one would need an auxiliary projection/fiber-volume bound for the actual \(F=(f_3,f_4)\) family; that bound is essentially the desired parametric estimate, not a consequence of the proposition.

## Chapter 8 thesis check

Chapter 8.1 gives exactly the first-alternative estimate now in the draft:

- Proposition 8.1.2: a relative \(2\)-cycle in \(R\) of area \(<\frac12R_1R_2\) fills with volume \(\lesssim R_1R_2^2\).
- Proposition 8.1.3: if \(CR_1R_2^2<S_1S_2S_3\), then \(R_3R_4\gtrsim S_3S_4\), by pulling back central \([0,S_1]\times[0,S_2]\) planes.

Chapter 8.2 lists five bounded-\(2\)-dilation degree-one maps: snake, codimension-one snake, short-side stretch, pinching, and double pinching.  These are useful for counterexample searches, but I found no valid composition producing the hard-regime failure.  The older scaling-test target
\[
R=(L^{-1},L^4,L^5,L^6),\qquad S=(1,1,L^6,L^6)
\]
is still blocked by the residual middle-side snake problem noted in prior rounds.

## Counterexample search

### Diagonal/permutation maps

These are impossible in the hard regime for a simple reason.  For an affine diagonal/permutation map, let the scaling factors be \(a_i=S_i/R_{\pi(i)}\).  If \(\operatorname{Dil}_2\le1\), then \(a_i a_j\le1\) for every pair.  In particular, the two target sides \(S_3,S_4\) are assigned to some source sides \(R_{\pi(3)},R_{\pi(4)}\), so
\[
S_3S_4\le R_{\pi(3)}R_{\pi(4)}\le R_3R_4.
\]
Thus \(R_3R_4\le\kappa S_3S_4\) is impossible for \(\kappa<1\).

The LP in `code/round9_hard_regime_search.py` confirms this: the best common exponent margin for simultaneous failure of
\[
R_1/S_1,\quad R_3R_4/(S_3S_4),\quad
\operatorname{Vol}(R)/(S_1S_2^{1/2}S_3^{3/2}S_4)
\]
is \(0\), not positive.

### Guth Chapter 8.2 exponent scan

Using the exact exponent move model from the thesis maps, the scan in `data/round9_hard_regime_search.txt` found no all-three-failing composition in 3 seeds, 1000 random trials each, depth 4.  This is only evidence, not a proof.  The earlier baseline route search also found no depth-3 route from the scaling-test \(R\) to \(S\); see `data/round9_guth_ch8_search_baseline.txt`.

## Strongest partial lemma I can justify

Here is the clean rigorous partial lemma to add to the notes if useful.

**Lemma.** No degree-one affine diagonal/permutation map \(f:R\to S\) with \(\operatorname{Dil}_2(f)\le1\) can lie in the hard regime \(R_3R_4< S_3S_4\).  Hence any counterexample in the hard regime must use genuinely nonlinear mixing of the coordinates.

The proof is the pair-product argument above.  It is weak relative to the theorem, but it rules out the most obvious explicit constructions and explains why a counterexample, if it exists, has to exploit the nonlinear snake/pinch mechanisms rather than ordinary anisotropic scaling.

## Recommendation

Do not present (SAF) as a consequence of Guth's Estimate 1.  It should be stated as a new missing parametric filling lemma.  The closest modern literature, Guth--Liokumovich on parametric inequalities and Staffa on parametric coarea for \(1\)-cycles, supports the point that this is a genuinely parametric problem; those papers do not provide the needed \(2\)-cycle, \(4\)-dimensional, weighted, anisotropic version.
