## Referee report on `answer.tex`

### Overall verdict

`answer.tex` is **not** a complete solution of the stated problem. It explicitly states that it is a “partial proof/reduction,” and it leaves the “Exact-plaque energy chain-map lemma” unproved. That lemma is essential for deriving the averaged estimate that would imply the desired second alternative. Therefore, independently of any smaller issues, the submission is **not answer-ready**.

I did verify that the document compiles and appears to satisfy the stated LaTeX contract; the failure is mathematical completeness, not formatting.

---

## Literature/source validation

The cited Guth result `Area-expanding embeddings of rectangles` is real and contains the quoted framework. Guth’s Estimate 1 states a lower bound for the \(k\)-dilation of a degree-positive map of pairs \((U,\partial U)\to(S,\partial S)\), with
\[
\operatorname{dil}_k(\Phi)\ge c(n)Q_1\cdots Q_j(Q_{j+1}\cdots Q_l)^{(k-j)/(l-j)}.
\]
This supports the author’s use of the case \(n=4,k=2,j=1,l=4\): cubing the inequality with \(\Dil_2\le1\) gives
\[
R_1^2\operatorname{Vol}(R)\gtrsim S_1^3S_2S_3S_4.
\]
([arxiv.org](https://arxiv.org/pdf/0710.0403))

Guth’s Theorem 3 in the same paper gives the relative isoperimetric profile of a rectangle, including the small-volume formula used by the author. In the case of relative \(2\)-cycles with \(A\le cR_1R_2\), it indeed yields the two relevant branches \(A^{3/2}\) and \(A^2/R_1\), up to constants. ([arxiv.org](https://arxiv.org/pdf/0710.0403))

The bibliography also contains Guth’s `The width-volume inequality`, but that reference is not used in the proof. Its inclusion is harmless. The arXiv abstract confirms it concerns lower bounds for \(k\)-dilation and degree-one maps between rectangles. ([arxiv.org](https://arxiv.org/abs/math/0609569))

No cited or located source proves the new “Exact-plaque energy chain-map lemma.” In `answer.tex` itself, this lemma is explicitly identified as missing.

---

## LaTeX contract audit

I compiled the supplied `answer.tex` with `pdflatex` twice.

- Document class: exactly `\documentclass[12pt]{article}`.
- Uses `fullpage`, which is permitted.
- No forbidden packages such as `geometry`, `a4wide`, `typearea`, etc.
- No forbidden line-spacing commands.
- No forbidden in-document font-size changes such as `\small`, `\footnotesize`, `\scriptsize`, or `\fontsize`.
- Compilation succeeded with no unresolved references.
- The compiled PDF has 5 pages, within the 12-page limit.

So the LaTeX contract appears satisfied.

---

## Paragraph-by-paragraph mathematical audit

### Title and opening

The document title is “Partial proof and sharp reduction…”. This is accurate but immediately signals non-completeness. Since the task requires a full proof of the original theorem, this alone is a serious issue.

### “Problem statement and interpretation”

The interpretation of rectangles as oriented Euclidean products and degree one as relative degree on \(H_4(R,\partial R)\to H_4(S,\partial S)\) is reasonable and faithful to the problem.

The current-theoretic setup is plausible, but the approximation paragraph is not fully rigorous as written. It asserts that one may approximate a piecewise smooth map relative to the boundary strata by smooth maps with \(\Dil_2\le1+\varepsilon\). This is believable in standard PL/smooth approximation settings, but for a final proof it should be stated as a precise lemma with hypotheses ensuring preservation of the pair condition, degree, and dilation bound. This is not the main fatal gap, but it is an unproved technical point.

The third paragraph explicitly says the document proves only a first alternative and reduces the second alternative to an unproved lemma. This makes the answer non-ready by the user’s criterion.

---

## “Standard inputs”

### Dilation monotonicity

The claim that \(\Dil_2(f)\le1\) implies \(\Dil_3(f)\le1\) and \(\Dil_4(f)\le1\) is correct. If the singular values satisfy \(\sigma_1\ge\cdots\ge\sigma_4\) and \(\sigma_1\sigma_2\le1\), then \(\sigma_2\le1\), hence all later singular values are \(\le1\), and \(\sigma_1\cdots\sigma_j\le\sigma_1\sigma_2\le1\) for \(j\ge2\).

### Guth Estimate 1

The use of Guth’s Estimate 1 is valid in substance. For \(n=4,k=2,j=1,l=4\),
\[
\Dil_2(f)\ge c Q_1(Q_2Q_3Q_4)^{1/3},
\]
and with \(\Dil_2(f)\le1\), this gives
\[
R_1^2\Vol(R)\gtrsim S_1^3S_2S_3S_4.
\]
This derivation is correct.

Minor caveat: Guth’s estimate is stated for \(U\) open in \(R\) and maps of pairs; applying it directly to a closed rectangle requires the usual limiting/interior argument. This is standard but not spelled out.

### Guth isoperimetric profile

The small-volume profile
\[
\Fill_R(Z)\le C\max\{A^{3/2},A^2/R_1\},\qquad A\le cR_1R_2,
\]
is correctly derived from Guth’s Theorem 3.

The inverse estimate
\[
\Mass(Z)\ge c\min\{R_1R_2,L^{2/3},(R_1L)^{1/2}\}
\]
is also correct: if \(A>cR_1R_2\), the first term applies; otherwise invert the two branches.

The implication
\[
\Mass Z<c_*R_1R_2 \implies \Fill_R(Z)\le CR_1R_2^2
\]
is correct after decreasing \(c_*\), since \(R_2\ge R_1\).

---

## “The first alternative”

### Lemma: filling a central target plane

The calibration argument is sound. Taking
\[
\beta=\psi\,dx_1\wedge dx_2
\]
with \(\psi\) vanishing on the \((x_3,x_4)\)-boundary and \(\psi\gtrsim S_3\) on the central rectangle gives
\[
\Mass(Y)\ge \left|\int_Y d\beta\right|
= \left|\int_{P_y}\beta\right|
\gtrsim S_1S_2S_3.
\]
The boundary terms vanish for the stated reasons. This is a valid proof, assuming the standard Stokes theorem for relative currents.

Minor point: “middle half” of the \((x_3,x_4)\)-rectangle should be defined explicitly in a final proof, e.g. the concentric subrectangle with side lengths \(S_3/2,S_4/2\).

### Proposition: first alternative

The proof is mostly correct.

The argument that \(f_\#[[R]]=[[S]]\) as a relative current is acceptable: relative degree one gives equality in relative homology; in the interior, the constancy theorem identifies the current with multiplicity one; any difference supported on \(\partial S\) must vanish as a \(4\)-current because \(\partial S\) is \(3\)-rectifiable.

The slicing identity
\[
f_\#\langle [[R]],F,y\rangle
=
\langle [[S]],(x_3,x_4),y\rangle
=\pm P_y
\]
is standard but should be cited or stated with hypotheses in a final proof. It is valid for Lipschitz/piecewise smooth maps and a.e. regular \(y\).

The filling-volume lower bound for \(Z_y\) follows correctly from pushing fillings forward and using \(\Dil_3(f)\le1\).

The contradiction using the small-volume isoperimetric inequality is correct:
if \(\Mass Z_y<c_*R_1R_2\), then
\[
\Fill_R(Z_y)\le CR_1R_2^2\le Cc_2S_1S_2S_3,
\]
contradicting the target lower bound if \(c_2\) is sufficiently small.

The coarea step
\[
\Vol(R)\ge\int_Q\Mass Z_y\,dy
\]
is correct because \(J_2F\le\Dil_2(f)\le1\).

This section proves a valid partial result:
\[
R_1R_2^2\lesssim S_1S_2S_3 \implies R_3R_4\gtrsim S_3S_4.
\]

---

## “The best bound obtained from single slices”

The derivation is correct, subject to the assumption that the first alternative fails with a sufficiently small constant.

From
\[
R_1R_2^2\gtrsim S_1S_2S_3
\]
and \(R_1=\alpha S_1\), one gets
\[
R_1R_2\gtrsim \alpha^{1/2}S_1(S_2S_3)^{1/2}.
\]
The other two terms in the minimum are also at least this size, using \(S_1\le S_2\le S_3\) and \(\alpha\le1\). Thus
\[
\Vol(R)\gtrsim
\alpha^{1/2}S_1S_2^{1/2}S_3^{3/2}S_4.
\]

Combining this with Guth’s monomial estimate
\[
\Vol(R)\gtrsim
\alpha^{-2}S_1S_2S_3S_4
\]
and optimizing in \(\alpha\) gives
\[
\Vol(R)\gtrsim S_1S_2^{3/5}S_3^{7/5}S_4.
\]
The algebra is correct. This is indeed weaker than the desired
\[
S_1S_2^{1/2}S_3^{3/2}S_4
\]
by the factor \((S_2/S_3)^{1/10}\).

This section is valuable, but it explicitly demonstrates that the submitted proof does not reach the theorem.

---

## “The averaged estimate needed for the stated theorem”

The definition of \(E_y,I,A\) is reasonable.

The weighted coarea inequality
\[
I\le C\Vol(R)
\]
is correct. At a rank-two point of \(dF\), if \(K=\ker dF\), then choosing \(v\in K\) and \(n\in K^\perp\) gives
\[
|df(v)\wedge df(n)|\ge |dG(v)|\,|dF(n)|.
\]
Thus \(\Dil_2(f)\le1\) implies \(\|dG|_K\|\tau_i\le1\), and hence
\[
\|dG|_K\|_{HS}^2J_2F\le C.
\]
The rank-deficient set contributes zero to the coarea integral. This part is sound.

The lower bound
\[
A\gtrsim S_1S_2S_3|Q|\gtrsim S_1S_2S_3^2S_4
\]
is correct by the central-plane filling lemma.

The claimed sufficient estimate
\[
A\le C\left(R_1I+\frac{I^2}{S_1|Q|}\right)
+C\frac{R_3R_4}{S_3S_4}A
\]
would indeed imply the desired second alternative after absorption, provided \(R_1\le\kappa S_1\), \(R_3R_4\le\kappa S_3S_4\), and \(\kappa,\delta\) are chosen small enough. The algebra here is correct.

But this estimate is **not proved**. It is the central missing result.

---

## “A precise plaque lemma which would imply \(\eqref{sufficient}\)”

The Fubini estimate for the bad set \({\mathcal B}_z\) is plausible and essentially correct. For fixed \(x\), the set of bad \(z\)’s is contained in the union of the \(F\)-images of six coordinate \(2\)-plaques, each of area at most \(R_iR_j\le R_3R_4\), so
\[
\frac1{|Q|}\int_Q \Mass(B\llcorner{\mathcal B}_z)\,dz
\lesssim \frac{R_3R_4}{S_3S_4}\Mass B.
\]
A final proof would need to address measurability of \({\mathcal B}_z\), but for piecewise smooth \(F\) this is likely manageable.

The “Exact-plaque energy chain-map lemma” is the fatal unproved assertion. It is not a standard consequence of Federer-Fleming deformation, Guth’s profile theorem, or the cited monomial estimates. It asserts the existence of chain operators \(P_z,H_z\) with highly nontrivial mass control:
\[
\Mass H_z(Z_y)\le C\left(R_1E_y+\frac{E_y^2}{S_1}\right),
\qquad
\Mass P_z(B_y)\le C\Mass(B_y\llcorner{\mathcal B}_z).
\]
This is precisely the missing parametric tightening theorem. Without a proof or citation, the main theorem is not established.

The derivation from the lemma to a filling of \(Z_y\) is algebraically correct:
\[
C_{y,z}=P_z(B_y)-H_z(Z_y)
\]
satisfies \(\partial C_{y,z}=Z_y\), assuming the chain-homotopy identity and \(\partial B_y=Z_y\).

The measurable selection claim for \(B_y\) is too compressed. A final proof should state a precise measurable-selection theorem for near-minimizing relative integral fillings. This is probably fixable, but it is not proved here.

There is also a minor logical imprecision at the end: applying the estimate only on
\[
\Omega=\{y:E_y\le4I/|Q|\}
\]
yields a restricted version of the sufficient inequality, not literally the global displayed estimate \(\eqref{sufficient}\) for \(A\). The restricted version is still enough for the theorem because \(|\Omega|\ge3|Q|/4\) and each slice has the same filling lower bound, but the text should state this more carefully.

---

## “Remaining open issues”

This section candidly identifies the essential missing lemma. That confirms the document is not a complete solution.

The negative claim that “ordinary rectangular isoperimetric profile, all single coordinate-pair slicings, Guth’s monomial estimates, and elementary compositions” give only the weaker bound is not proved in the document. It may be true in the author’s exploratory notes, but in `answer.tex` it is unsupported. This is not needed for the partial proof, but it would not be acceptable as a theorem-level assertion without proof.

---

## Final assessment

The following pieces appear correct or essentially correct:

1. The interpretation of degree.
2. The use of Guth Estimate 1 to obtain
   \[
   R_1^2\Vol(R)\gtrsim S_1^3S_2S_3S_4.
   \]
3. The use of Guth’s small-volume relative isoperimetric profile.
4. The central-plane filling calibration.
5. The proof of the first-alternative implication.
6. The single-slice partial bound
   \[
   \Vol(R)\gtrsim S_1S_2^{3/5}S_3^{7/5}S_4.
   \]
7. The algebra showing that the averaged estimate would imply the desired theorem.

The following are fatal for answer-readiness:

1. The exact-plaque chain-map lemma is unproved.
2. The averaged estimate \(\eqref{sufficient}\) is therefore unproved.
3. The document explicitly leaves “Remaining open issues.”
4. The second alternative in the original problem is not established.

Thus `answer.tex` is a rigorous partial reduction, not a complete proof of the problem.