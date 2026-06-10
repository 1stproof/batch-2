# Referee report

## Verdict

`answer.tex` is **not answer-ready**. The decisive reason is that the manuscript explicitly presents itself as a **partial proof**, introduces an essential unproved Lemma `random-puncture`, states “I do not have a rigorous proof of this deformation lemma,” and ends with “Remaining open issues.” Therefore it does **not** fully solve the stated problem.

## LaTeX contract check

I compiled `answer.tex` with `pdflatex` twice. It compiles successfully to a 6-page PDF. It uses exactly `\documentclass[12pt]{article}`, uses the permitted `fullpage` package, and I found no forbidden margin packages, line-spacing changes, or explicit in-document font-size commands. Thus the LaTeX contract appears satisfied. The rejection is mathematical, not LaTeX-related.

## Literature check

The cited Guth paper exists as arXiv:0710.0403, *Area-expanding embeddings of rectangles*, by Larry Guth. The arXiv page describes it as estimating when there is a \(k\)-expanding embedding between rectangles, sharp up to dimensional constants. ([arxiv.org](https://arxiv.org/abs/0710.0403))

The use of Guth’s rectangular isoperimetric profile is broadly consistent with Theorem 3 in the paper: Guth states an isoperimetric profile theorem for relative integral cycles in a rectangle, with a small-volume estimate and a general estimate \(I_R^k(V)\le C(n)R_{k+1}V\). ([arxiv.org](https://arxiv.org/pdf/0710.0403)) The use of Guth’s Estimate 1 is also consistent with the cited formula: for a degree-\(D>0\) map of pairs, Guth gives a lower bound for \(k\)-dilation involving \(Q_i=S_i/R_i\). ([arxiv.org](https://arxiv.org/pdf/0710.0403))

## Section-by-section mathematical audit

### 1. “Problem statement and interpretation”

The interpretation of degree one via relative homology is reasonable and faithful to the problem. Renaming the small theorem constant from \(k\) to \(\kappa\) is also sensible.

However, the section immediately declares the proof incomplete: it says the argument only reduces the remaining case to Lemma `random-puncture`, and explicitly says that this lemma is not proved. This alone prevents acceptance.

### 2. “Standard tools”

The current-theoretic framework is plausible but somewhat compressed. The assertion that \(f_\#[R,\partial R]-[S,\partial S]\) is zero modulo boundary currents follows morally from degree one and the constancy theorem for top-dimensional currents, but a complete proof should spell out the passage from a piecewise smooth map of pairs to integral currents and the use of relative currents.

The slicing naturality statement is standard, but again the manuscript gives no details about the regularity/measurability hypotheses needed for piecewise smooth maps. This is probably fixable, but in a complete proof it should be written more carefully.

The singular-value argument proving \(\Dil_2(f)\le1\Rightarrow \Dil_j(f)\le1\) for \(j=3,4\) is correct.

The stated Guth isoperimetric estimate (1) follows from the \(k=2,n=4\) small-volume part of Theorem 3. The monomial estimate (2) also follows from Estimate 1 with \(j=1,k=2,l=4\), after cubing the dilation inequality. These uses appear mathematically consistent.

### 3. Lemma “central target filling”

The calibration argument is essentially correct. Because \(y_3,y_4\) lie in the central third of the \((x_3,x_4)\)-rectangle and \(S_3\le S_4\), one can choose a \(1\)-Lipschitz function \(\psi\) vanishing on the boundary and satisfying \(\psi(y)\gtrsim S_3\). The form
\[
dx_1\wedge dx_2\wedge d\psi
\]
has controlled comass, and the boundary term on \(\partial S\) vanishes for the stated reasons. This proves the claimed lower bound up to dimensional constants.

Minor issue: for full rigor, the proof should specify approximation of the distance function by smooth functions and justify Stokes for integral currents, but this is standard and likely repairable.

### 4. Proposition “first alternative”

The logic is sound modulo standard current-theoretic details. For a.e. central \(y\), the slice \(Z_y\) maps to the target plane \(P_y\). Any filling of \(Z_y\) in \(R\) pushes forward to a filling of \(P_y\) in \(S\), and \(\Dil_3(f)\le1\) prevents mass increase. Thus \(\Fill_R(Z_y)\gtrsim S_1S_2S_3\).

Then Guth’s small-cycle filling estimate forces \(\Mass Z_y\gtrsim R_1R_2\) under the stated hypothesis \(C_1R_1R_2^2\le S_1S_2S_3\). Coarea for \(F=(x_3,x_4)\circ f\) and \(J_2F\le1\) gives
\[
R_1R_2R_3R_4\gtrsim R_1R_2S_3S_4,
\]
hence \(R_3R_4\gtrsim S_3S_4\). This part is a credible partial result.

### 5. “Consequences of the same slicing”

The derivation of (4) from (1) and (3) is correct: either the slice mass is already \(\gtrsim R_1R_2\), or one of the two Guth filling branches forces
\[
\Mass Z_y\gtrsim (S_1S_2S_3)^{2/3}
\quad\text{or}\quad
\Mass Z_y\gtrsim (R_1S_1S_2S_3)^{1/2}.
\]

The integration giving (5) is also correct.

The derivation of (6) from Guth’s monomial estimate and \(R_1\le\kappa S_1\) is correct:
\[
R_1^2\Vol(R)\gtrsim S_1^3S_2S_3S_4
\]
implies
\[
\Vol(R)\gtrsim \kappa^{-2}S_1S_2S_3S_4.
\]

The algebra leading to (8), (9), and (10) is also correct. In particular, if both desired alternatives fail, then the remaining regime is indeed extremely anisotropic:
\[
\alpha=R_1/S_1\lesssim \kappa^2,
\qquad
S_3/S_2\gtrsim \alpha^{-4}\kappa^{-2}.
\]

This section is useful but only gives a reduction, not the theorem.

### 6. “Weighted coarea”

The pointwise inequality
\[
\lambda^2J_2F\le1
\]
is correct. If \(T=\ker dF\), \(N=T^\perp\), and \(v\in T\) realizes \(\lambda=\|dG|_T\|\), then
\[
df(v)=(dG(v),0),\qquad df(n)=(dG(n),dF(n)),
\]
so the two-vector \(df(v)\wedge df(n)\) has norm at least \(\lambda |dF(n)|\). Since \(\Dil_2(f)\le1\), this bounds \(\|dF|_N\|\), hence \(J_2F\le\lambda^{-2}\) when \(\lambda>0\).

The coarea conclusion
\[
I=\int_Q\int_{Z_y}\lambda^2\,d\|Z_y\|\,dy\le \Vol(R)
\]
is therefore sound.

The lower bound \(E_y\ge S_1S_2\) is also correct in principle: \(G_\#Z_y\) is the fundamental relative current of the \(S_1\times S_2\) rectangle, and the area formula gives its mass bounded by \(\int_{Z_y}J_2(G|_{Z_y})\le E_y\).

Again, some regularity/current details are compressed but likely fixable.

### 7. “Projection and the random-puncture reduction”

The Fubini estimate (13) is plausible but not fully rigorous as written.

Issues:

1. **Measurable selection of fillings.** The manuscript chooses measurable almost-minimizing fillings \(B_y\) without proof. A complete proof needs a measurable selection argument or an approximation by countably many fillings.

2. **Measurability of \(\mathcal B_z\).** The set
   \[
   \mathcal B_z=\{x:z\in F(V_{\pi_{12}x})\}
   \]
   should be Borel or at least measurable to restrict currents and apply Fubini. This is probably true because the relevant incidence set is a projection of a compact/closed set, but it is not proved.

3. **Constant mismatch in (13).** Since
   \[
   q=|Q|=\frac{S_3S_4}{9},
   \]
   the last inequality should have a dimensional constant:
   \[
   \lesssim \frac{R_3R_4}{S_3S_4}A,
   \]
   not literally \(2(R_3R_4/S_3S_4)A\). This is not fatal, but the displayed constant is inaccurate.

4. **The area estimate itself is otherwise correct.** For fixed \(u\), the area of \(F(V_u)\cap Q\) is at most the parametrized area of \(F|_{V_u}\), which is at most \(R_3R_4\) because \(J_2(F|_{V_u})\le1\).

Thus (13) is a credible estimate up to standard measurability and constant issues.

### 8. Lemma “random-puncture deformation”

This is the fatal gap. Lemma `random-puncture` is stated without proof and is essential. The author explicitly writes:

> “I do not have a rigorous proof of this deformation lemma.”

Therefore the theorem is not proved.

There is also a possible formulation issue in the heuristic following the lemma. The text says that on \(R\setminus\mathcal B_z\), every vertical rectangle \(V_u\) has
\[
F(V_u)\subset Q\setminus\{z\}.
\]
The definition only implies \(z\notin F(V_u)\); it does **not** imply \(F(V_u)\subset Q\), since \(F(V_u)\) may leave \(Q\). This may or may not be fixable, but as written the heuristic statement is false.

### 9. Conditional proposition

The proposition “If Lemma `random-puncture` holds, then the theorem follows” is mostly correct.

Averaging (14), using (13), and absorbing the bad term under \(R_3R_4\le\kappa S_3S_4\) gives the claimed inequality
\[
F_0q\lesssim R_1I+\frac{I^2}{S_1q}.
\]
The subsequent contradiction argument with
\[
I\le \eta qS_1(S_2S_3)^{1/2}
\]
is algebraically correct. Finally \(I\le\Vol(R)\) gives the desired second alternative after choosing \(\kappa\) sufficiently small.

But this remains only a conditional proof because Lemma `random-puncture` is unproved.

### 10. “The false non-absorbing estimate”

The counterexample is correctly analyzed. For
\[
S=(1,1,L,L),\qquad R=(1,M,L,L),
\]
and
\[
f(u_1,u_2,u_3,u_4)=(u_1,u_2/M,u_3,u_4),
\]
the derivative has singular values \(1,1,1,1/M\), so \(\Dil_2(f)=1\). The weighted energy satisfies \(I\sim ML^2\), while the calibrated filling lower bound gives \(A\gtrsim ML^3\). Taking \(M=L^{1/2}\), the proposed non-absorbing right-hand side has largest order \(L^3\), whereas \(A\sim L^{7/2}\). This section is correct and usefully identifies why a stronger estimate would be false.

### 11. “Remaining open issues”

This section explicitly confirms that the proof is incomplete. It identifies the unproved deformation lemma as the central missing point. Since the problem asks for a complete proof, the existence of this section alone makes the submission not answer-ready.

## Summary of defects affecting validity

Fatal defects:

1. The proof explicitly depends on an unproved Lemma `random-puncture`.
2. The manuscript explicitly admits incompleteness.
3. The final theorem is only proved conditionally on the missing lemma.

Nonfatal but relevant technical gaps:

1. Current/slicing formalism is compressed and would need full justification in a final proof.
2. The measurable choice of fillings \(B_y\) is not justified.
3. The measurability of \(\mathcal B_z\) is not proved.
4. Equation (13) suppresses a dimensional constant while displaying an explicit constant.
5. The heuristic after Lemma `random-puncture` incorrectly states \(F(V_u)\subset Q\setminus\{z\}\); the definition only gives \(z\notin F(V_u)\).

The partial results up to the first alternative, weighted coarea estimate, and conditional absorption argument are largely sound, but they do not constitute a complete solution.