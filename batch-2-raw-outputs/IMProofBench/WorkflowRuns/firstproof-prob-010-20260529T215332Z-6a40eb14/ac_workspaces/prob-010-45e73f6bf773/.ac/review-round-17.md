## Referee report on the revised draft

### Verdict

The revised `answer.tex` **now appears mathematically complete and answer-ready**. The author has addressed the two prior fatal issues:

1. the invalid strong-operator-to-universal-bidual weak-* passage; and  
2. the invalid multiplication of concrete \(B(L^2M)\)-operators inside the nonmultiplicative DKEP normal bidual.

The new proof of the boundary support intersection works in the ordinary enveloping bidual \(A^{**}\), uses concrete coefficient products only there, and passes to the normal bidual only after applying the DKEP support projection. This is the correct strategy in view of DKEP Remark 2.8, which explicitly notes that the canonical map \(A\to(A^\sharp)^*\) is generally not multiplicative. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

---

## LaTeX contract check

I compiled the supplied `answer.tex` twice with `pdflatex`.

- Document class is exactly `\documentclass[12pt]{article}`.
- The `fullpage` package is used; no forbidden layout package or manual margin change is present.
- No forbidden line-spacing or in-document font-size changes are present.
- Compilation succeeds.
- The PDF is 5 pages, within the 12-page limit.

So there is **no LaTeX-contract violation**.

---

## Literature validation

The revised proof’s main cited inputs are supported by the literature:

- DKEP’s normal-bidual framework, including Proposition 2.10 and the warning that the canonical embedding into the normal bidual is not generally multiplicative, matches the revised proof’s caution and ordinary-bidual strategy. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- DKEP Theorem 5.6 supports the annihilator criterion used to pass from \(K_X^{\infty,1}\)-membership to vanishing against \(\sharp_J\)-normal functionals that vanish on \(X\). ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- DKEP Theorem 5.10, Proposition 5.9, and Example 5.11 support the direct-sum/mixing argument and the coefficient-boundary formalism. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- DKEP Lemma 8.5 supports the final normal-bidual characterization of proper proximality relative to a boundary piece. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- CDHJKN Theorem 0.4 / Theorem 5.4 and Proposition 5.5 support the graph-product correspondence decomposition and fusion rules used in the boundary-intersection lemma. ([ems.press](https://ems.press/content/serial-article-files/51743?nt=1))
- CDHJKN Main Theorem 0.5 and Proposition 6.3 support the final factoriality and nonamenability conclusions. ([ems.press](https://ems.press/content/serial-article-files/51743?nt=1))

---

## Review of previous concerns

### 1. Nonmultiplicativity of the normal bidual — addressed

The previous draft incorrectly multiplied concrete coefficient operators after embedding them into \(\mathcal A_M=(B(L^2M)^{\sharp_J})^*\). The revised proof explicitly avoids this. In the new boundary-support intersection lemma, all coefficient products \(hkh\) are computed concretely in \(B(L^2M)\), then limits are taken in the ordinary bidual \(A_M^{**}\), and only afterward is the result compressed by the DKEP projection \(p_M\).

This resolves the earlier fatal objection.

### 2. Strong-operator convergence versus weak-* convergence in \(A^{**}\) — addressed

The old proof used strong convergence of finite-coordinate cutdowns to infer weak-* convergence in the universal bidual, which was invalid. The revised direct-sum lemma instead uses the DKEP mixing-closure argument from the proof of Theorem 5.10. This is the right mechanism and avoids the earlier topology error.

### 3. Induced subalgebra boundary conventions — addressed

The revised proof of \(X_{\mathcal H_B}=X_B\) fixes the earlier directional confusion for the coefficient maps \(T_{\widehat 1}\). It now correctly identifies \(T_{\widehat1}:L^2N\to L^2B\) for \({}_NL^2N_B\) and the inclusion \(T_{\widehat1}:L^2B\to L^2N\) for \({}_BL^2N_N\). This section is now acceptable.

### 4. Hypertrace step in the finite-boundary criterion — addressed

The finite-boundary criterion now treats \(\Theta(T)=q_0Tq_0\) as DKEP’s u.c.p. compression into the normal compact corner, not as a multiplicative embedding. The construction of the resulting Connes hypertrace is sufficiently clear.

---

## Paragraph-by-paragraph mathematical audit

### Problem interpretation

The interpretation of irreducibility as nontrivial join-irreducibility, equivalently connectedness of \(\Gamma^c\), is explicitly stated. This resolves the ambiguity in the original problem statement.

### Normal supports and coefficient boundary pieces

The normal-support paragraph is now correctly framed around the ordinary bidual \(A^{**}\) and the support projection \(p_N\). The proof should be read for the boundary pieces actually used later, namely \(X_{M_U}\), \(X_B\), and \(\mathbb K(L^2M)\), for which the necessary multiplier hypotheses hold; DKEP Example 3.4 explicitly gives \(M\) and \(JMJ\) in the multiplier algebra for subalgebra boundary pieces. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

### Lemma `\ref{lem:coeff}`

The proof of \(X_{\mathcal H_B}=X_B\) is now coherent. The fusion argument gives \(X_{\mathcal H_B}\subset X_B\), while the vectors \(\xi\otimes\widehat1\) show that every generator of \(X_B\) appears as a coefficient for \(\mathcal H_B\). The self-conjugacy map in the tracial case is standard.

### Lemma `\ref{lem:dsupport}`

The direct-sum support argument now uses DKEP’s strong-module closure machinery rather than invalid universal-bidual weak-* convergence. The conclusion that coefficients of the direct sum lie in \(K_X(N)\) follows from mixing relative to \(X\times B(L^2N)\), Theorem 5.10, and Proposition 5.9.

The construction of \(\mathcal C_U\) and the approximate units is also valid: coefficient products are computed concretely using \(T_{\xi\otimes\eta}=T_\eta T_\xi\), and functional calculus with functions vanishing at zero gives contractive approximate units inside the required norm closure.

### Lemma `\ref{lem:intersection}`

This is the critical repair, and it now works.

For positive finite-fusion coefficients \(h=T_\xi^*T_\xi\) and \(k=T_\eta^*T_\eta\), the identity

\[
hkh=T_{\xi\otimes\bar\xi\otimes\eta}^*
T_{\xi\otimes\bar\xi\otimes\eta}
\]

is used only in the concrete algebra \(B(L^2M)\). CDHJKN’s fusion rule then decomposes the correspondence containing \(\xi\otimes\bar\xi\otimes\eta\) over subsets of \(U\cap W\). The direct-sum lemma places this coefficient in \(K_{X_{M_{U\cap W}}}^{\infty,1}(M)\). Passing to approximate-unit limits in \(A^{**}\), then using annihilators in \(A^{\sharp_J}\), proves

\[
0\le q_Wq_Uq_W\le q_{U\cap W}.
\]

The induction producing the palindromic support inclusion is also correct.

### Finite boundary criterion

The compression by \(q_i^\perp\) is valid because the DKEP support projections commute with both \(N\) and \(JNJ\). The GNS argument with the positive palindromic product is correct. The construction of the hypertrace from \(\omega(q_0)=1\) is now adequately justified.

### Relative Bass–Serre paradox

The reduced-word arguments are concise but mathematically standard. The projections \(p,q,e_B\) lie in \(S_{X_B}(N)\), the inequalities

\[
w_1qw_1^*+w_2qw_2^*\le p,\qquad apa^*\le q
\]

follow from the AFP reduced-word decomposition, and the \(B\)-Haar unitary \(h=w_1a\) gives pairwise orthogonal translates of \(e_B\). This proves relative proper proximality via DKEP Theorem 6.2.

### Application to graph products

The graph-product AFP splitting is standard. The construction of \(w_1,w_2\) from the complement graph is correct in both cases \(|C(v)|\ge2\) and \(|C(v)|=1\). The intersection of all links is empty because no vertex lies in its own link. The boundary-intersection lemma then places the palindromic product in the compact corner.

The final use of CDHJKN to obtain factoriality and nonamenability is valid: connectedness of \(\Gamma^c\) with at least three vertices rules out universal vertices and isolated exceptional complement edges, and Proposition 6.3 rules out amenability under the same condition.

---

## Final assessment

The revised proof now resolves the earlier fatal defects. I do not find a remaining mathematical gap that affects the stated theorem. The document compiles, satisfies the LaTeX contract, records the problem interpretation, and gives a complete proof under that interpretation.