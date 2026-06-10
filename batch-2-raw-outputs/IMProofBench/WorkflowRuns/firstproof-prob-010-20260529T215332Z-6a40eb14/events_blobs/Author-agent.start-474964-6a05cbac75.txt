## Referee report on the revised `answer.tex`

### Verdict

The revision improves several points, especially by adding a rectangular support lemma and expanding the Bass–Serre argument. However, I still **cannot certify the proof as complete**. The main obstruction remains the graph-product boundary-support intersection lemma. It depends on several support-identification and coefficient-algebra assertions that are not proved and are not immediate from the cited papers.

### LaTeX contract

I compiled the revised `answer.tex` twice with `pdflatex`. It compiles successfully to a 5-page PDF. It uses exactly `\documentclass[12pt]{article}`, the permitted `fullpage` package, and I found no prohibited layout, line-spacing, or in-document font-size changes. So there is **no LaTeX-contract failure**.

---

## Literature validation

DKEP’s paper does contain the basic normal-bidual framework, boundary pieces, the hereditary algebra \(K_X\), the \(K_X^{\infty,1}\)-closure result, the original and normal-bidual proper proximality criteria, and the natural maps used in Lemma 8.5. In particular, DKEP Example 3.4 defines \(X_B\) using the norm-closed span of \(x_1Jy_1JTJy_2Jx_2\) with \(T\in e_BB(L^2M)e_B\), Proposition 3.6 identifies \(K_X^{\infty,1}\) with the \(\|\cdot\|_{\infty,1}\)-closure of both \(X\) and \(K_X\), and Lemma 8.5 gives the normal-bidual criterion for proper proximality under the ergodic-center hypothesis. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

However, the revised proof attributes to DKEP Proposition 2.10 a concrete support formula
\[
(B^{\sharp_J})^*=p_{\rm nor}s_BA^{**}s_Bp_{\rm nor}.
\]
The visible statement of DKEP Proposition 2.10 gives normal-bidual inclusions/intersections for \(C^*\)-algebras with faithful multiplier actions, but it does **not** explicitly state this ordinary-open-support cutdown formula. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) This is a substantive point because the later proof repeatedly identifies \(q_U\) with \(p_{\rm nor}s_U\).

CDHJKN does provide the graph-product bimodule decomposition and fusion rules in the needed general direction, and its Main Theorem 0.5 and Proposition 6.3 support the final factoriality and nonamenability checks. ([ems.press](https://ems.press/content/serial-article-files/51743)) But the use of the fusion rules inside the boundary-support calculation still requires additional operator-norm and bounded-vector arguments not supplied in `answer.tex`.

---

## Detailed audit

### 1. Problem statement and interpretation

This part is acceptable. The author explicitly interprets irreducibility as join-irreducibility, equivalently connected complement graph. This is the standard graph-product interpretation and resolves the ambiguity in the problem statement.

### 2. DKEP normal-bidual setup

The general definitions are broadly consistent with DKEP. The use of Lemma 8.5 for a separable finite factor with trivial action is acceptable, since the center is trivial and hence the ergodic-center hypothesis is automatic. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

But the support notation is still too compressed. The proof needs a precise justification of the passage from ordinary open support projections in \(B(L^2N)^{**}\) to the support projections \(q_X\) in DKEP’s normal bidual. This is not merely notational; it is used crucially in Lemma \(\ref{lem:intersection}\).

### 3. Boundary support calculus

The new support lemma (2) is mathematically reasonable: if \(BC\subset eA^{**}s\) and \(CB\subset sA^{**}e\), the approximate-unit argument does give
\[
r(sA^{**}s)r\subset eA^{**}e.
\]
The added rectangular lemma is also basically correct: if \(T^*T\in D\), then \(T=Td\) for the support \(d\) of \(D\).

However, the first support assertion remains problematic. The paper states:

\[
(B^{\sharp_J})^*=p_{\rm nor}s_BA_N^{**}s_Bp_{\rm nor}.
\tag{1}
\]

This is not proved in `answer.tex`, and the cited DKEP Proposition 2.10 does not visibly state this formula. It may be derivable with extra work, but that derivation is essential and absent. Without it, the equality
\[
q_U=p_{\rm nor}s_U
\]
is not justified.

### 4. The definition and identification of \(\mathcal B_U\)

This is still a major gap. The proof claims:

\[
\mathcal B_U=K_{X_{M_U}}(M).
\]

This is an essential lemma, but it is not proved. The argument says it follows from the definitions, the \(T\)-operator identities, and CDHJKN fusion. That is not enough.

Specific problems:

- DKEP Example 3.4 defines \(X_{M_U}\) using all operators in the corner \(e_{M_U}B(L^2M)e_{M_U}\), not only rank-one-type coefficient operators. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) One must prove that the finite-fusion coefficient algebra described by the author really recovers the DKEP hereditary algebra \(K_{X_{M_U}}(M)\).
- DKEP Example 5.11 gives a coefficient-boundary construction for a correspondence, but it does not automatically identify \(K_X\) for \(X=X_{M_U}\) with the norm-closed algebra generated by all finite Connes fusions of \(\mathcal H_U\) and \(\overline{\mathcal H_U}\). ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- The proof does not handle off-diagonal coefficients arising from direct-sum decompositions carefully.
- The proof does not justify that coefficients of arbitrary bounded vectors in possibly infinite direct sums are norm limits of coefficients of finite-support vectors.

The last point is particularly serious. The sentence

> “Finite-support vectors in these direct sums are dense, and the coefficient maps are norm continuous”

is not valid in the form needed. Finite-support vectors are dense in Hilbert norm, but \(T_\xi\) is controlled by the bounded-vector/right-bounded norm, not merely by Hilbert norm. In infinite direct sums, truncations of a bounded vector need not converge in the operator norm of the associated \(T_\xi\). Thus the passage from finite-support vectors to arbitrary bounded vectors is not justified.

### 5. Intersection lemma

The revision addresses part of my previous objection by adding the rectangular support lemma. That helps with the formal step
\[
T_\alpha^*T_{\eta_2}\in s_IA^{**}s_U
\]
provided one already knows
\[
T_\alpha^*T_\alpha\in\mathcal B_I,\qquad T_{\eta_2}^*T_{\eta_2}\in\mathcal B_U.
\]

But the proof of \(T_\alpha^*T_\alpha\in\mathcal B_I\) still depends on the unresolved direct-sum/bounded-vector issue above. CDHJKN gives decomposition and fusion rules at the bimodule level, but the proof must still show that the corresponding coefficient supports behave correctly under arbitrary bounded vectors and infinite multiplicity direct sums. The current draft does not.

Therefore Lemma \(\ref{lem:intersection}\), the central boundary-corner inclusion
\[
q_W(q_U\mathcal A_Mq_U)q_W\subset q_{U\cap W}\mathcal A_Mq_{U\cap W},
\]
remains unproved.

### 6. Finite palindromic criterion

This part is substantially improved and is likely correct modulo standard DKEP facts.

The compression argument using \(q_i^\perp\) is plausible. The GNS argument with the palindromic product is also sound. The final hypertrace step is supported by DKEP’s Lemma 8.5 proof, where a natural map from \(B(L^2M)\) into the normal-bidual \(K_X\)-corner is used. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

Still, the proof should explicitly justify normality of the compressed restriction to \(N\), for example by domination by a scalar multiple of \(\tau\). This is fixable and not the main obstruction.

### 7. Relative Bass–Serre proposition

The revised argument is much clearer than before. The reduced-word commutator formulas, the inequalities
\[
w_1qw_1^*+w_2qw_2^*\le p,\qquad apa^*\le q,
\]
and the \(B\)-Haar argument for \(h=w_1a\) are now plausible.

However, the proof is still somewhat compressed. In particular, the claim that DKEP Lemma 6.1 directly gives \(p,q\in S_{X_B}(N)\) requires a precise identification of the relevant \(X_B\)-mixing space with the commutator target. DKEP Lemma 6.1 is stated for dual normal \(M\)-bimodules and \(X\)-mixing/proximal points, not directly as the simple criterion used here. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) This is probably repairable, but as written it is still a black-box application.

That said, the Bass–Serre proposition is less problematic than the boundary-corner intersection lemma.

### 8. Application to graph products

The graph-theoretic part is sound. The construction of \(w_1,w_2\) from complement-connectedness is correct. The AFP splitting over the link is standard.

The final factor and nonamenability checks are also essentially correct. CDHJKN Main Theorem 0.5 gives the relevant factoriality obstruction, and Proposition 6.3 gives the amenability characterization; connectedness of \(\Gamma^c\) with at least three vertices rules out the exceptional isolated complement vertex/edge cases. ([ems.press](https://ems.press/content/serial-article-files/51743))

But because the preceding relative-proximality and boundary-intersection machinery is not rigorously established, the final conclusion does not yet follow.

---

## Which previous concerns were addressed?

Addressed or partially addressed:

- The author added a rectangular support lemma, which directly targets the previous rectangular-support objection.
- The finite palindromic criterion now treats the operator-system extension issue more explicitly.
- The Bass–Serre paradox proof now includes more reduced-word and orthogonality detail.
- The graph-combinatorial and CDHJKN factor/nonamenability steps are clearer.

Still unresolved:

- The concrete identification \(q_X=p_{\rm nor}s_X\) remains insufficiently proved.
- The equality \(\mathcal B_U=K_{X_{M_U}}(M)\) remains an essential unproved lemma.
- The use of CDHJKN fusion rules for arbitrary bounded vectors in possibly infinite direct sums remains unjustified.
- The proof of Lemma \(\ref{lem:intersection}\) still depends on those unresolved support/coefficient issues.

New issue introduced:

- The revised draft now explicitly attributes formula (1) to DKEP Proposition 2.10, but the cited proposition does not visibly state that formula. This is a new citation-accuracy problem.

---

## Final assessment

The revised draft is stronger than the prior version, but it still does **not** constitute a complete rigorous proof. The central boundary-support intersection lemma is not established with sufficient precision, and several essential identifications are asserted rather than proved.