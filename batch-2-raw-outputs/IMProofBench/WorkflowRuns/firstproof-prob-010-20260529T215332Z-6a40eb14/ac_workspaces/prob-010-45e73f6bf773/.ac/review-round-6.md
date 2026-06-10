## Referee report on `answer.tex`

### Overall verdict

`answer.tex` **passes the formal LaTeX contract**: it uses `\documentclass[12pt]{article}`, only the permitted `fullpage` layout package, no font-size or spacing changes, compiles successfully with `pdflatex`, and the compiled PDF is 5 pages.

Mathematically, however, I **cannot certify the proof as complete**. The final graph-product application is plausible, and several cited structural results are correctly located, but the central “boundary support calculus” contains essential unproved assertions not supplied by the cited references as stated. These gaps affect the core mechanism upgrading relative proper proximality to proper proximality.

---

## Literature cross-check

The cited DKEP facts are mostly real, but some are used beyond what is explicitly stated:

- DKEP Lemma 8.5 does give a normal-bidual criterion for proper proximality relative to a boundary piece, under the stated separability/ergodicity hypotheses; for the trivial action this requires the algebra to be a factor. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- DKEP Theorem 6.2 characterizes relative proper proximality by nonexistence of central states on \(S_X(M)\) with normal restriction. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- DKEP defines boundary pieces \(X_B\) for expected subalgebras using the Jones projection and left/right translates, as used later. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- DKEP’s correspondence formalism does include the contragredient identity \(T_{\bar\xi}=T_\xi^*\) and the fusion formula \(T_{\xi\otimes\eta}=T_\eta T_\xi\), so the displayed algebraic coefficient identity (4) is believable at the generator level. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- CDHJKN Theorem 5.4 and Proposition 5.5 do provide the graph-product bimodule decomposition and fusion rules used in spirit by the proof. ([ems.press](https://ems.press/content/serial-article-files/51743))
- CDHJKN Main Theorem 0.5 gives the factoriality criterion cited in the final section. ([ems.press](https://ems.press/content/serial-article-files/51743))
- CDHJKN Main Theorem 0.1 gives the relative amenability criterion under trace-zero unitary hypotheses, and Proposition 6.3 gives a direct amenability characterization. ([ems.press](https://ems.press/content/serial-article-files/51743))

The problem is not that the cited papers are irrelevant; the problem is that several nontrivial intermediate support-calculus claims in `answer.tex` are not actually proved or explicitly supplied by those citations.

---

## Detailed audit

### 1. “Problem statement and interpretation”

This section is acceptable. The original problem’s irreducibility wording is ambiguous because it does not explicitly say the two subgraphs are nonempty, proper, or disjoint. The answer adopts the standard graph-product interpretation: \(\Gamma\) is not a nontrivial join, equivalently \(\Gamma^c\) is connected. That is a reasonable and faithful interpretation.

The statement that DKEP Lemma 8.5 applies to separable finite factors is correct, but it is important that the factor condition is only verified near the end. This is not itself an error.

---

### 2. “Boundary support calculus”

This is the main problematic part.

#### 2.1 Unsupported identification \(q_C=p e_C\)

The proof introduces \(A=B(L^2N)\), a projection \(p=p_{\rm nor}\in A^{**}\), ordinary open supports \(e_C\in A^{**}\), and asserts:

\[
e_Cp=pe_C,\qquad q_C=pe_C.
\]

This is an essential claim. The cited DKEP Proposition 2.10 does discuss normal biduals and nonunital inclusions of von Neumann algebras, but the lines in the paper do **not** state the asserted formula \(q_C=pe_C\) or the commutation \(e_Cp=pe_C\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) DKEP later says the support projection of \((K_X(M)^\sharp_J)^*\) commutes with \(M\) and \(JMJ\), but that is not the same as identifying it with the ordinary hereditary support cut down by a universal \(p\). ([arxiv.org](https://arxiv.org/pdf/2204.00517))

This is not a cosmetic issue. Lemma 1, the “cut-down support lemma,” depends entirely on the ability to compute DKEP support projections by ordinary hereditary supports in \(A^{**}\). Without a proof of \(q_C=pe_C\), the conclusion

\[
q_C(q_B\mathcal A_Nq_B)q_C\subset q_D\mathcal A_Nq_D
\]

does not follow from the ordinary \(A^{**}\)-calculation.

#### 2.2 Equation (5) is not proved

The algebraic coefficient identity (4) is plausible and follows from DKEP’s contragredient/fusion formulas. But equation (5),

\[
\K_{X_{\mathcal H}}(N)\,\K_{X_{\mathcal K}}(N)\,
\K_{X_{\mathcal H}}(N)
\subset
\K_{X_{\mathcal H\otimes_N\overline{\mathcal H}\otimes_N\mathcal K}}(N),
\]

is much stronger. DKEP defines \(K_X(M)\) via hereditary \(C^*\)-algebras associated to \(K^L_X\), not merely as the algebraic span of coefficient operators. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) The answer says the passage to closed algebras is “functorial under separately continuous multiplication,” citing DKEP Corollary 5.2, Proposition 5.9, and Theorem 5.10, but it does not state or prove the required functorial hereditary-closure result.

This is an essential missing lemma. The subsequent support inclusion (6) and the graph-product intersection lemma depend on (5).

#### 2.3 Identification \(X_{M_U}=X_{\mathcal H_U}\) is not justified

The proof defines

\[
\mathcal H_U=L^2(M)\otimes_{M_U}L^2(M)
\]

and says DKEP Example 5.11 identifies \(X_{M_U}\) with the coefficient boundary of \(\mathcal H_U\). DKEP Example 5.11 does define coefficient boundary pieces for correspondences and explicitly notes that if \(B\subset M\) and one views \(L^2M\) as an \(M\)-\(B\) correspondence, then the resulting boundary piece is \(X_B\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) But the answer uses the induced \(M\)-\(M\) correspondence \(L^2M\otimes_{M_U}L^2M\), which requires an additional verification that its coefficient boundary agrees with the Jones-projection boundary piece \(X_{M_U}\). This is probably true, but it is not proved in `answer.tex`.

#### 2.4 Direct sums and off-diagonal coefficients

The proof states that the coefficient boundary of a direct sum is supported by the join of the supports of the summands. This is nontrivial because coefficient operators for a direct sum include off-diagonal coefficients between different summands. No proof is given in `answer.tex`.

This matters directly in Lemma 2: CDHJKN decomposes the triple fusion as a direct sum, and the proof then immediately concludes that the support is dominated by \(q_{U\cap W}\). That conclusion requires the missing direct-sum support lemma.

#### 2.5 Consequence

Because of 2.1–2.4, Lemma 2, the “intersection of graph-product boundary corners,” is not rigorously established. Since Lemma 2 supplies the compact palindromic support needed for the upgrade criterion, this is a fatal gap.

---

### 3. “Finite palindromic boundary criterion”

The strategy is good, but there is one technical gap.

The proof treats \(\widetilde S(N)\) as if it were a \(C^*\)-algebra with an ordinary GNS representation. DKEP’s \(S_X(M)\) is an operator system rather than generally a \(C^*\)-algebra, and the same issue applies to the normal-bidual \(\widetilde S_X(M)\). DKEP explicitly calls \(S_X(M)\) an operator system. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

The statement

> “In the GNS representation of \(\omega\), the cyclic vector is fixed by every \(q_i\). Hence it is fixed by \(R\).”

needs justification by extending the state \(\omega\) from the operator system \(\widetilde S(N)\) to a state on a containing \(C^*\)-algebra or on \(\mathcal A_N\). This is likely fixable by a standard positive extension argument, and since \(R\in q_0\mathcal A_Nq_0\subset\widetilde S(N)\), the value \(\omega(R)\) would then be well-defined. But as written, the argument is formally incomplete.

The compression argument producing a central state on \(\widetilde S_{X_i}(N)\) is mostly correct, though it should explicitly justify normality of the compressed restriction to \(N\) by domination by a scalar multiple of \(\tau\).

The final hypertrace step is plausible. DKEP’s proof of Lemma 8.5 does construct natural u.c.p. maps from \(B(L^2M)\) into the normal-bidual compact corner. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) Still, the answer should cite the exact map more precisely.

---

### 4. “A relative Bass–Serre paradox”

This section is substantially more convincing, but still terse.

The reduced-word projection argument for \(p,q\in S_{X_B}(N)\) is plausible. The commutator formulas

\[
[p,R_x]=R_xe_B-e_BR_x,\qquad [q,R_x]=0
\]

for \(x\in P\ominus B\), and the analogous formulas for \(x\in Q\ominus B\), are believable from the amalgamated-free-product Fock decomposition. However, in a fully rigorous proof one should spell out the verification on all reduced-word sectors and explicitly invoke DKEP Lemma 6.1 with both \(x\) and \(x^*\).

The paradoxical inequalities

\[
w_1qw_1^*+w_2qw_2^*\le p,\qquad apa^*\le q
\]

are correct under the stated \(B\)-orthogonality assumptions. The \(B\)-Haar unitary argument using \(h=w_1a\) is also sound.

This proposition is probably fixable into a rigorous proof. It is not the main obstruction.

---

### 5. “Application to graph products”

This final section is mostly correct, conditional on the earlier boundary machinery.

The amalgamated free product decomposition

\[
M\cong M_{V\setminus\{v\}}*_{M_{\operatorname{Lk}(v)}}
(M_{\operatorname{Lk}(v)}\bar\otimes M_v)
\]

is standard for graph products.

The construction of \(w_1,w_2\) in the two cases for \(C(v)\) is correct. In the singleton case \(C(v)=\{r\}\), complement connectedness and \(|V|\ge3\) indeed give \(s\in\operatorname{Lk}(v)\) with \(r\not\sim s\). The conditional expectations onto \(M_{\operatorname{Lk}(v)}\) vanish for the displayed words by reduced-word considerations.

The intersection of all links is empty, and \(X_{M_\varnothing}\) is the compact boundary piece; the latter follows because the Jones projection onto \(\mathbb C\hat 1\) is rank one and its left/right translates span finite-rank operators densely.

The factoriality and nonamenability checks using CDHJKN are correct in substance. CDHJKN Main Theorem 0.5 gives the stated factoriality obstruction, and connectedness of \(\Gamma^c\) with at least three vertices excludes universal vertices and isolated exceptional complement edges. ([ems.press](https://ems.press/content/serial-article-files/51743)) For nonamenability, the answer cites Main Theorem 0.1; it should explicitly note that amenability of \(M\) is the same as amenability relative to \(M_\varnothing=\mathbb C\), or alternatively cite CDHJKN Proposition 6.3 directly. ([ems.press](https://ems.press/content/serial-article-files/51743)) This is a minor omission, not fatal.

The fatal dependence is again on Lemma 2 and the finite palindromic criterion.

---

## Final assessment

The proof has a promising architecture, but `answer.tex` does **not** yet constitute a complete rigorous solution. The main unresolved issues are:

1. The DKEP support projection calculation \(q_C=pe_C\) is asserted without proof and is not supplied by the cited proposition as stated.
2. The key product inclusion for correspondence boundary \(K\)-algebras, equation (5), is asserted but not proved.
3. The graph-product boundary intersection lemma depends on unproved identifications of \(X_{M_U}\) with an induced correspondence boundary and on an unproved direct-sum support lemma.
4. The palindromic criterion uses a GNS argument for a state on an operator system without explaining the necessary extension to a \(C^*\)-algebra.

Because these are essential to the proof, the answer is not answer-ready.