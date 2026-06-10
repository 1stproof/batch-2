## Referee report

### LaTeX / First Proof contract

I reconstructed `answer.tex` and ran `pdflatex` twice. It compiles successfully to a 5-page PDF. The document class is exactly `\documentclass[12pt]{article}`, the only layout package used is `fullpage`, and I saw no prohibited line-spacing, font-size, or margin changes. Thus I do **not** reject on LaTeX-contract grounds.

### Literature cross-check

The cited DKEP paper does contain the normal-bidual framework, Lemma 8.5, Theorem 5.6, Theorem 5.10, Proposition 5.9, Example 5.11, and Theorem 6.2 in forms relevant to the proof. In particular, Lemma 8.5 requires an ergodicity condition on the center, which for the trivial action means the algebra must be a factor. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) Theorem 5.6 is an annihilator/mixing/relative-compactness equivalence, but its exact hypotheses and conclusion are more delicate than the proof records. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) Example 5.11 identifies coefficient boundary pieces for correspondences and the subalgebra example. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

The CDHJKN paper does contain the graph-product fusion rules used in spirit by the answer: their Theorem D / Proposition 5.5 gives decompositions indexed by subsets of intersections. ([arxiv.org](https://arxiv.org/pdf/2404.08150)) It also contains the factoriality/fullness/diffuseness theorem and the amenability criterion used at the end, although the answer’s citation “Main Theorem 0.5” does not match the numbering in the checked source, where this appears as Theorem E / Theorem 2.4 and Proposition 6.3. ([arxiv.org](https://arxiv.org/pdf/2404.08150))

## Main verdict

The proof is **not answer-ready**. The overall strategy is plausible, but several essential technical steps are either unsupported, misstated, or rely on nontrivial support-calculus facts that are not proved and are not immediate from the cited references. The most serious unresolved points are:

1. The identification of normal-bidual support projections \(q_X\) with \(p_N\bar q_X\) and the assertion that \(X\) and \(K_X(N)\) have the same normal-bidual support are not adequately justified.
2. The direct-sum and finite-fusion coefficient lemmas are not proved rigorously enough for the later support-intersection argument.
3. The boundary support intersection lemma is the central new ingredient, but its passage from concrete coefficient products to a normal-bidual projection inequality has major gaps.
4. The finite-boundary criterion uses a formal expression \(\Theta(T)=q_0Tq_0\) despite earlier acknowledging that the canonical map into the normal bidual is not multiplicative.
5. The Bass–Serre proposition is plausible but compressed; several reduced-word and operator-system membership claims need proof.

Below is the detailed audit.

---

## Section: Problem statement and interpretation

The interpretation of irreducibility as “not a nontrivial join” / connected complement is reasonable and explicitly recorded. This satisfies the ambiguity requirement.

The use of DKEP Lemma 8.5 for the trivial action is acceptable **only after** \(M\) has been shown to be a factor, since Lemma 8.5 assumes the action on the center is ergodic. The answer later attempts to prove factoriality before applying the finite-boundary criterion, so this is structurally okay. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

However, the notation
\[
\mathcal A_N=(A_N^{\sharp_J})^*
\]
and the support projection \(q_X\) are introduced in a compressed way. That is not fatal by itself, but the later proof depends on very precise properties of these objects.

---

## Section: Normal supports and coefficient boundary pieces

This section contains a **major unresolved support-calculus gap**.

The answer states that if \(\bar q_X\in A_N^{**}\) is the ordinary open support of the hereditary algebra \(X\), then DKEP Proposition 2.10 gives
\[
p_N\bar q_X=\bar q_Xp_N,\qquad q_X=p_N\bar q_X,
\]
and that the weak-* closure of \(X\) in \(\mathcal A_N\) has unit \(q_X\). But the checked statement of DKEP Proposition 2.10 gives inclusions/intersections of normal-bimodule biduals and nonunital inclusions of von Neumann algebras; it does not, as quoted, explicitly prove this formula with the ordinary open support in \(A^{**}\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) This formula is central to Lemma 3 and cannot be used without proof.

Similarly, the claim that DKEP Theorem 5.6 implies \(X\) and \(K_X(N)\) have the same \(A_N^{\sharp_J}\)-annihilator is plausible but not proved carefully. Theorem 5.6 gives equivalences involving \(K^{\infty,1}_{X,Y}\) and functionals vanishing on \(XB(L^2N,L^2M)Y\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) To derive the answer’s annihilator equality, one must explicitly use heredity of \(X\), verify the multiplier hypotheses, and show the conclusion for all relevant \(A_N^{\sharp_J}\)-functionals. The answer merely asserts this.

This is not a cosmetic issue: the support-intersection proof later depends exactly on this annihilator/support identification.

---

## Lemma `induced subalgebra boundary`

This lemma is mostly plausible, but the proof is too compressed.

The use of DKEP Example 5.11 to identify the coefficient boundary of \({}_N L^2N_B\) with the subalgebra boundary \(X_B\) is consistent with the cited source. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) The formulas for \(T_{\widehat 1}\) as \(E_B\) and as the inclusion are also plausible.

However, the sentence “DKEP Theorem 5.10 and the fusion identity give that \(H\otimes_BK\) is mixing relative to \(X_B\times Y_K\)” hides a nontrivial stability-under-fusion argument. Theorem 5.10 gives equivalent characterizations of mixing for one correspondence; it does not by itself state the required fusion stability in the form used here. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) The proof should explicitly verify the bounded-vector condition for elementary tensors and then pass to a cyclic dense set.

This gap is probably repairable, but as written it is not a complete proof.

The self-conjugacy assertion
\[
\overline{\xi\otimes\eta}\mapsto J\eta\otimes J\xi
\]
is also stated without checking module actions. In the tracial case it is likely correct, but it should be verified because the later finite-fusion algebra uses conjugate correspondences.

---

## Lemma `direct sums and finite coefficient algebras`

This lemma is essential and is not proved rigorously enough.

### Direct-sum part

The answer claims that if each summand \(\mathcal K_j\) has coefficient boundary contained in \(X\), then every coefficient of \(\bigoplus_j\mathcal K_j\) belongs to \(K_X(N)\). This is a strong conclusion.

The proof sketches a closure argument using Hilbert-norm convergence of bounded vectors and projections \(p_k\uparrow 1\). But several points are missing:

- It is not shown that finite-coordinate truncations of a bounded vector remain bounded with the required uniform control.
- It is not shown carefully that the class of \(X\)-mixing operators is closed under the convergence used.
- The passage from mixing of all bounded vectors to membership \(T_\xi^*T_\xi\in K_X(N)\), rather than only in \(K_X^{\infty,1}(N)\) or the normal-bidual support corner, needs exact use of DKEP Proposition 5.9 and Theorem 5.10. Proposition 5.9 distinguishes \(K_{X,Y}\) from \(K^{\infty,1}_{X,Y}\), and the proof does not track this distinction carefully. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

This is a serious gap because Lemma `intersection` later relies on coefficients of direct sums being controlled by \(K_{X_{M_I}}\).

### Finite coefficient algebra part

The algebraic formula for products of coefficients is plausible. But the proof that \(X_{M_U}\) has a contractive approximate unit in the norm closure of \((\mathcal C_U)_+\) is underdeveloped.

The answer asserts that the “usual net”
\[
f_\varepsilon\Big(\sum_{j=1}^nT_{\xi_j}^*T_{\xi_j}\Big)
\]
is a contractive approximate unit. To make this rigorous, one must specify the directed set of finite positive coefficient sums and prove that these generate the hereditary algebra \(X_{M_U}\). This is plausible from DKEP Example 5.11, but the answer does not spell out the hereditary-generation argument.

The conclusion that each such functional-calculus term is a norm limit of positive finite-fusion coefficients also needs a careful polynomial-approximation argument inside the nonclosed algebra \(\mathcal C_U\). The proof gestures at this but does not give the details.

---

## Lemma `boundary support intersection`

This is the central technical lemma of the solution, and it has the most serious gaps.

The algebraic identity
\[
hkh
=
T_{\xi\otimes\bar\xi\otimes\eta}^{*}
T_{\xi\otimes\bar\xi\otimes\eta}
\]
is correct for coefficient operators.

The use of CDHJKN fusion rules is plausible in spirit: Proposition 5.5 gives that fusing \(H_{U_1}\) and \(H_{U_2}\) decomposes over subsets of \(U_1\cap U_2\). ([arxiv.org](https://arxiv.org/pdf/2404.08150)) But the answer applies this to arbitrary finite fusions and direct sums from \(\mathcal F_W\) and \(\mathcal F_U\). That requires an induction over the number of fusion factors and careful tracking of labels. The answer only states this in one sentence.

More seriously, the passage from concrete products \(h_\alpha^Wh_\beta^Uh_\alpha^W\) to the projection inequality
\[
q_Wq_Uq_W\le q_I
\]
is not rigorous as written.

Specific problems:

1. The proof uses ordinary open supports \(\bar q_U\in A_M^{**}\) and then compresses to \(\mathcal A_M=p_MA_M^{**}p_M\). But, as noted above, the formula \(q_U=p_M\bar q_U\) and commutation of \(p_M\) with \(\bar q_U\) have not been proved.

2. The assertion that approximate units converge “strongly, hence weak-*” to their open supports in \(A_M^{**}\) is not enough unless one specifies the representation/topology and shows that the functionals in \(A_M^{\sharp_J}\) extend normally to that setting.

3. The conclusion that vanishing of all \(\phi\in A_M^{\sharp_J}\) on \(X_{M_I}\) implies membership in \(q_I\mathcal A_Mq_I\) depends on the earlier unproved annihilator equality between \(X_{M_I}\) and \(K_{X_{M_I}}(M)\).

4. The proof only shows vanishing on products involving special approximate-unit elements. It does not fully justify that the limiting element in the normal bidual is exactly \(q_Wq_Uq_W\), especially given the earlier warning that the canonical map \(A_M\to\mathcal A_M\) is not multiplicative.

Because this lemma is essential for placing the final palindromic product in the compact corner, these are fatal gaps.

---

## Lemma `finite boundary criterion`

The first half of the proof is mostly sound: compressing a nonproper-proximal central state by \(q_i^\perp\) is a standard argument, provided \(q_i\in\widetilde S(N)\) and commutes with \(N\) and \(JNJ\). DKEP Lemma 8.5 supports the central-state characterization for finite factors. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

However, the final hypertrace step is not rigorous.

The answer defines
\[
\Theta(T)=q_0Tq_0
\]
and calls it “DKEP’s \(N\)- and \(JNJ\)-bimodular u.c.p. compression.” But earlier the answer correctly warned that the canonical map \(B(L^2N)\to\mathcal A_N\) is not multiplicative. Thus the expression \(q_0Tq_0\) is not automatically meaningful as a u.c.p. map from the concrete algebra \(B(L^2N)\) into \(\mathcal A_N\).

DKEP Lemma 8.5’s proof does mention natural \(M\)-bimodular u.c.p. maps from \(B(L^2M)\) into the normal compact corner, but the answer must state the exact map and verify its properties. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) As written, the proof uses a formal compression notation that is not justified in the nonmultiplicative normal-bidual setting.

This is another essential gap: without a rigorously defined \(\Theta\), the construction of the Connes hypertrace is incomplete.

---

## Proposition `relative Bass--Serre paradox`

This proposition is plausible, but the proof is too compressed for a complete rigorous solution.

The reduced-word commutator formulas for \(p,q\) should be proved, not merely asserted. They are believable, but they are the mechanism that places \(p,q\) in \(S_{X_B}(N)\). DKEP Lemma 6.1 says one can check a dense generating set, but the answer does not explicitly verify the hypotheses, including the adjoint conditions. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

The inequalities
\[
w_1qw_1^*+w_2qw_2^*\le p,\qquad apa^*\le q
\]
also need more detail. In particular, the proof should justify carefully that \(q w_1^*w_2 q=0\) follows from \(E_B(w_1^*w_2)=0\) by the AFP reduced-word decomposition.

The \(B\)-Haar argument for \(h=w_1a\) is correct in spirit, but the proof should explicitly handle negative powers and derive pairwise orthogonality via
\[
e_B h^k e_B=E_B(h^k)e_B=0.
\]

These are likely repairable gaps, but the proposition is not presently a fully rigorous proof.

---

## Section: Application to graph products

The graph-product AFP decomposition over \(M_{\mathrm{Lk}(v)}\) is standard and plausible, but no reference or proof is given. Since it is a structural step, it should be cited or proved.

The graph-combinatorial construction of \(w_1,w_2\) is essentially correct:

- If \(C(v)\) has two vertices, choosing \(u_r,u_t\) works.
- If \(C(v)=\{r\}\), connectedness of \(\Gamma^c\) and \(|V|\ge 3\) indeed gives \(s\in\mathrm{Lk}(v)\) with \(s\not\sim r\).

The expectation computations are plausible but should be written in terms of graph-product reduced words.

The final factoriality and nonamenability conclusions are correct in spirit, but the citation is inaccurate/unclear. The checked CDHJKN source states factoriality as Theorem E / Theorem 2.4, not “Main Theorem 0.5.” The theorem says that obstructions to factoriality come from universal vertices or isolated exceptional nonedge pairs, and a connected complement with at least three vertices excludes these. ([arxiv.org](https://arxiv.org/pdf/2404.08150)) The amenability criterion is Proposition 6.3 and says amenability requires every nonedge to be an isolated exceptional pair; connectedness of \(\Gamma^c\) with at least three vertices excludes this. ([arxiv.org](https://arxiv.org/pdf/2404.08150))

The answer also should explicitly note that a trace-zero unitary forces \(\dim M_v\ge 2\), which is a hypothesis in the CDHJKN amenability criterion.

---

## Conclusion

The proof has a plausible high-level strategy, and many of the intended ingredients exist in the literature. But `answer.tex` does not presently give a complete rigorous solution. The normal-bidual support calculus, the direct-sum coefficient lemma, the support-intersection lemma, and the hypertrace compression step are essential and remain insufficiently proved. Therefore the answer is not ready.