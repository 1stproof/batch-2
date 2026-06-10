## Referee report

### Overall verdict

`answer.tex` **does not yet constitute a complete rigorous solution**. It compiles and satisfies the formal LaTeX contract, and the high-level strategy is plausible. However, the proof has several essential gaps in the operator-algebraic support calculus underlying Lemma 1, especially the identification of the DKEP normal support \(q_X\) with the ordinary support of the original boundary piece \(X\), and the use of DKEP Proposition 2.6 / Proposition 3.6 for an annihilator statement they do not state. Since Lemma 1 is central to the finite-boundary reduction, these are not cosmetic issues.

---

## 1. LaTeX contract audit

I reconstructed `answer.tex` and ran `pdflatex` twice. The document compiled successfully to a **5-page PDF**, with no unresolved references after the second run.

Contract checks:

- Uses exactly `\documentclass[12pt]{article}`.
- Uses `fullpage`, which is permitted.
- No `geometry`, `a4wide`, `typearea`, manual margin changes, line-spacing changes, or in-document font-size changes.
- PDF is at most 12 pages.

So there is **no LaTeX-contract failure**.

---

## 2. Literature validation

The two cited papers exist and are relevant.

- DKEP’s paper *Properly Proximal von Neumann Algebras* is the intended source for the normal-bidual formulation, boundary pieces, \(S_X(M)\), and Lemma 8.5. DKEP Lemma 8.5 states, under separability and ergodicity of the action on the center, that proper proximality relative to \(X\) is equivalent to absence of an \(M\)-central invariant state on the normal-bidual operator system \(\widetilde S_X(M)\). For the trivial action on a factor, the author’s specialized use is broadly consistent. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- CDHJKN’s graph-product paper is correctly identified as containing the relevant graph-product structure results. It states the fusion decomposition for the bimodules \(H_U(V_1,V_2)\) and gives the fusion rule over \(W\subset U_1\cap U_2\). ([content.ems.press](https://content.ems.press/assets/public/full-texts/serials/prims/61/4/14299216/online/10.4171-prims-61-4-3.pdf)) It also states the factoriality criterion in Main Theorem 0.5 and the amenability criterion in Proposition 6.3. ([content.ems.press](https://content.ems.press/assets/public/full-texts/serials/prims/61/4/14299216/online/10.4171-prims-61-4-3.pdf))

However, several **specific uses** of DKEP in `answer.tex` are not justified by the cited results as written.

---

## 3. Paragraph-by-paragraph mathematical audit

### Problem statement and interpretation

The author explicitly adopts the standard interpretation of irreducibility as “not a nontrivial join,” equivalently \(\Gamma^c\) connected. This is reasonable and necessary because the original problem statement is imprecise about nonempty/proper subgraphs. This part is acceptable.

The assumption that traces are faithful normal traces is also standard for graph products of tracial von Neumann algebras.

### DKEP normal-bidual setup

The statement of DKEP Lemma 8.5 is broadly acceptable after specializing to the trivial group action and a factor. DKEP’s actual Lemma 8.5 includes a group action and assumes ergodicity on the center; for a finite factor and the trivial action this condition is satisfied. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

No fatal issue here, though the paper should explicitly say “we apply Lemma 8.5 to the trivial group action; ergodicity on \(Z(N)\) follows because \(N\) is a factor.”

---

## 4. Major issue: the support-calculus paragraph is not rigorous

This is the most serious problem.

### 4.1 Incorrect statement that \(p_{\rm nor}\) is central

`answer.tex` says:

> Let \(p_{\rm nor}\in A_N^{**}\) be the central projection implementing the simultaneous \(N\)- and \(JNJ\)-normal representation...

This is not correct as stated. DKEP define \(p_{\rm nor}\) as the projection associated to states whose restriction to \(M\) is normal, and they identify \((A^\sharp)^*\) with \(p_{\rm nor}A^{**}p_{\rm nor}\). But DKEP explicitly warn that the canonical embedding \(A\to (A^\sharp)^*\) is not generally a \(*\)-homomorphism because \(p_{\rm nor}\) need not be central. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

This matters because the proof repeatedly cuts ordinary \(A^{**}\)-support inclusions by \(p_{\rm nor}\). Such cutdowns can be valid if one proves the needed commutation with the particular support projections, but the text’s blanket “central projection” statement is false and cannot be used as a shortcut.

### 4.2 The formula \(q(B)=p_{\rm nor}s_B\) in the simultaneous \(N,JNJ\)-normal setting is not proved

The author claims that DKEP’s paragraph before Remark 2.8 plus Proposition 2.10 give

\[
(B^{\sharp_J})^*=q(B)\mathcal A_Nq(B),\qquad q(B)=p_{\rm nor}s_B.
\]

DKEP’s one-normal discussion does say that for an \(M\)-\(C^*\)-subalgebra \(B\), the support \(q_B\) commutes with \(p_{\rm nor}\) and yields a corner inside \(p_{\rm nor}A^{**}p_{\rm nor}\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) But DKEP Proposition 2.10, in the simultaneous category, is stated as an inclusion/intersection result for the two normal structures; it does not, by itself, explicitly give the full support formula claimed in `answer.tex`. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

This may be derivable, but `answer.tex` does not give the derivation. Since the later proof depends on cutting ordinary support inclusions by \(p_{\rm nor}\), this is an essential missing lemma.

### 4.3 Misuse of DKEP Proposition 2.6 and Proposition 3.6

The text says:

> Proposition 3.6 and the strong-bimodule annihilator criterion of Proposition 2.6 imply that every \(\sharp_J\)-functional vanishing on \(X\) vanishes on \(K_X^{\infty,1}(N)\), hence on \(K_X(N)\).

This is not supported by the cited statements.

- DKEP Proposition 2.6 is Magajna’s bidual identification \(X^{\natural\natural}\cong (X^\sharp)^*\). It is not stated as a “strong-bimodule annihilator criterion.” ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- DKEP Proposition 3.6 says \(K_X^{\infty,1}\) is the \(\|\cdot\|_{\infty,1}\)-closure of \(K_X\) and is a closed strong bimodule. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) It does not by itself say that every \(\sharp_J\)-functional vanishing on \(X\) vanishes on \(K_X\).

The conclusion that \(X\) and \(K_X(N)\) have the same annihilator in \(A_N^{\sharp_J}\) is essential because DKEP’s support \(q_X\) is the support of \((K_X(N)^{\sharp_J})^*\), whereas the proof later computes supports using the original coefficient boundary piece \(X_{M_U}\). This identification is not proved.

A valid proof would need a precise statement such as:

\[
\operatorname{Ann}_{A^{\sharp_J}}(X)=\operatorname{Ann}_{A^{\sharp_J}}(K_X(N)),
\]

with a proof using the exact topology defining \(A^{\sharp_J}\) and DKEP’s relative compactness results. The current citations do not provide that.

This is a **fatal gap** for the present solution.

---

## 5. Coefficient boundary \(X_{M_U}=X_{\mathcal H_U}\)

The identification of \(X_{M_U}\) with the DKEP coefficient boundary of

\[
\mathcal H_U=L^2M\otimes_{M_U}L^2M
\]

is plausible. DKEP Example 3.4 defines the boundary piece associated to a subalgebra \(B\subset M\) using the Jones projection \(e_B\), and Example 5.11 defines the coefficient boundary \(X_H\) of a correspondence. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

However, the proof in `answer.tex` is compressed. In particular, the identity \(T_{\Omega_U}=e_{M_U}\) is nontrivial and should be computed explicitly from DKEP’s definition of \(T_\xi\). This is probably repairable, but as written it is more of a sketch than a rigorous proof.

---

## 6. Special approximate units and finite-fusion coefficients

The claim that \(X_{M_U}\) has a contractive approximate unit whose elements are norm limits of finite sums of coefficients of finite fusions of \(\mathcal H_U\) and \(\overline{\mathcal H_U}\) is plausible but insufficiently justified.

The argument requires several nontrivial facts:

1. \(X_{M_U}\) is hereditarily generated by positive coefficient generators.
2. Functional calculus of finite positive sums can be approximated by polynomials without constant term.
3. Products of coefficient operators are again coefficient operators of finite Connes fusions, using \(T_{\bar \xi}=T_\xi^*\) and \(T_{\xi\otimes\eta}=T_\eta T_\xi\).
4. CDHJKN’s fusion rules apply exactly to all such finite fusions in the form needed.

DKEP does give the formula \(T_{\xi\otimes\eta}=T_\eta T_\xi\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) CDHJKN gives the needed type of fusion rule. ([content.ems.press](https://content.ems.press/assets/public/full-texts/serials/prims/61/4/14299216/online/10.4171-prims-61-4-3.pdf)) But the passage from arbitrary approximate units in the hereditary algebra to the specific finite-fusion coefficient form is not written with enough detail for a strict proof.

This issue is not necessarily fatal by itself, but it compounds the support-identification gap above.

---

## 7. Lemma “boundary-corner intersection”

The intended statement

\[
q_W(q_U\mathcal A_M q_U)q_W\subset q_{U\cap W}\mathcal A_Mq_{U\cap W}
\]

is the core technical engine of the proof. The high-level strategy is sensible: multiply finite-fusion coefficients, use the coefficient calculus, apply CDHJKN fusion, and pass to supports.

But the proof depends on the unproved support equality

\[
q_{X_{M_U}}=p_{\rm nor}s_U
\]

where \(s_U\) is the ordinary support of the original boundary piece \(X_{M_U}\). As explained above, this is not established.

There is also an additional technical issue: the proof says that the vector

\[
\xi_1\otimes\overline{\xi_2}\otimes\eta_1
\]

decomposes into summands \(\mathcal H_Z\) with \(Z\subset U\cap W\). This is plausible by repeated use of CDHJKN Proposition 5.5, but the proof does not spell out the induction or the exact specialization of CDHJKN’s \(H_U(V_1,V_2)\) notation to the full \(M\)-\(M\) correspondences being used. CDHJKN’s fusion rule does indeed decompose over \(W\subset U_1\cap U_2\), but the author needs to explicitly identify their \(\mathcal H_U\) with the \(H_U(V,V)\) of CDHJKN. ([content.ems.press](https://content.ems.press/assets/public/full-texts/serials/prims/61/4/14299216/online/10.4171-prims-61-4-3.pdf))

Because Lemma 1 is used to force the palindromic product into the compact corner, this gap is fatal unless repaired.

---

## 8. Finite boundary criterion

This lemma is mostly sound conditional on the DKEP normal-bidual framework.

The compression argument using \(q_i^\perp\) is plausible because DKEP states that the support projection of \((K_X(M)^{\sharp_J})^*\) commutes with both \(M\) and \(JMJ\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) The GNS argument using the palindromic positive contraction is also a good way to avoid non-normal meet problems.

One point should be expanded: the final hypertrace construction invokes “the u.c.p. map from \(\mathbb B(L^2N)\) to \(q_0\mathcal A_Nq_0\) used in DKEP’s proof of Lemma 8.5.” This is probably correct, but a standalone proof should state the map and its properties, rather than relying on an implicit object inside another proof.

This is a minor-to-moderate exposition gap, not the main fatal issue.

---

## 9. Relative Bass–Serre paradox

The AFP argument is plausible. The projections \(p,q\) onto reduced words with first \(P\)- or \(Q\)-letter are standard, and the commutator formulas with right multiplication are credible. DKEP Lemma 6.1 is indeed the type of result allowing one to verify \(p,q\in S_{X_B}(N)\) from commutator conditions on an ultraweakly dense \(*\)-subalgebra. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

However, this proposition is written as a compressed proof. A strict proof should include:

- A precise AFP Fock-space decomposition.
- Verification of the commutator formulas on each reduced-word sector.
- A proof that \(q w_1^*w_2 q=0\) follows from \(E_B(w_1^*w_2)=0\).
- A proof that \(h=w_1a\) is \(B\)-Haar for all positive and negative powers.

These details are likely repairable. I would not reject the proof solely for this section, but it is not fully detailed.

The final invocation of DKEP Theorem 6.2 is acceptable in spirit: DKEP Theorem 6.2 gives equivalent formulations involving \(B\)-central states on \(S_X(M)\). ([arxiv.org](https://arxiv.org/pdf/2204.00517))

---

## 10. Application to graph products

The graph-product application is mostly correct, assuming the earlier lemmas.

The AFP splitting

\[
M\cong M_{V\setminus\{v\}}*_{M_{L_v}}(M_{L_v}\bar\otimes M_v)
\]

is standard for graph products. The construction of \(w_1,w_2\) from complement-neighbors of \(v\) is combinatorially correct.

The argument that \(\bigcap_v L_v=\emptyset\) is correct because no vertex lies in its own link.

The identification \(X_{M_\emptyset}=\mathbb K(L^2M)\) is correct in spirit: \(M_\emptyset=\mathbb C\), so the Jones projection is rank one and its \(M,JMJ\)-translates generate the compact operators.

The factoriality and nonamenability arguments are supported by CDHJKN:

- Main Theorem 0.5 says factoriality can fail only through universal vertices whose vertex algebra is not a factor, or through exceptional two-dimensional non-edge pairs adjacent to all other vertices. ([content.ems.press](https://content.ems.press/assets/public/full-texts/serials/prims/61/4/14299216/online/10.4171-prims-61-4-3.pdf))
- Proposition 6.3 characterizes amenability by vertex amenability plus the condition that every non-edge pair is an isolated two-dimensional exceptional pair. ([content.ems.press](https://content.ems.press/assets/public/full-texts/serials/prims/61/4/14299216/online/10.4171-prims-61-4-3.pdf))

Since \(\Gamma^c\) is connected with at least three vertices, an isolated complement vertex or isolated complement edge is impossible. This part is sound.

---

## 11. Summary of essential gaps

The answer is not ready because the following essential points remain unproved or incorrectly cited:

1. **False statement:** \(p_{\rm nor}\) is called central, but DKEP explicitly warn that \(p_{\rm nor}\) need not be central. ([arxiv.org](https://arxiv.org/pdf/2204.00517))  
2. **Unproved support cutdown formula:** The claimed simultaneous formula
   \[
   (B^{\sharp_J})^*=p_{\rm nor}s_B\,\mathcal A\,p_{\rm nor}s_B
   \]
   is not directly stated by DKEP Proposition 2.10 and is not proved.
3. **Mis-cited annihilator equality:** DKEP Proposition 2.6 and Proposition 3.6 do not establish that \(X\) and \(K_X(N)\) have the same annihilator in \(A^{\sharp_J}\). This is essential for computing \(q_X\) from the original boundary piece.
4. **Core Lemma 1 depends on that unsupported support identification.** Therefore the palindromic compact-corner inclusion is not rigorously established.
5. Several technically nontrivial coefficient/fusion and approximate-unit assertions are sketched but not fully proved.

Because these gaps affect the central mechanism of the proof, `answer.tex` is not a complete rigorous solution.