## Referee report

**Verdict:** `answer.tex` is **not answer-ready**. The LaTeX contract appears satisfied, but the mathematical proof has several essential gaps. The most serious gaps are in the normal-bidual support bookkeeping, the identification of subalgebra boundary pieces with coefficient boundaries, the direct-sum/finite-fusion support lemma, and the boundary-support intersection lemma. These are not cosmetic: they are the central technical bridge from relative proper proximality for link subalgebras to ordinary proper proximality.

## Source and compile checks

- I checked the cited DKEP paper. DKEP Lemma 8.5 indeed gives a normal-bidual criterion for relative proper proximality in terms of absence of central states on \(\widetilde S_X(M)\). ([arxiv.org](https://arxiv.org/pdf/2204.00517))  
- DKEP Proposition 2.10, however, is much weaker than the concrete open-support formula asserted in `answer.tex`; it states an intersection/inclusion result for simultaneous normal biduals, not the full \(pA^{**}p\), \(pr_Y\)-corner calculus claimed. ([arxiv.org](https://arxiv.org/pdf/2204.00517))  
- DKEP Example 3.4 defines the subalgebra boundary \(X_B\), and Example 5.11 identifies \(X_{L^2M_B}\) with that boundary; this does not automatically prove the stronger fused-correspondence identification used in the answer. ([arxiv.org](https://arxiv.org/pdf/2204.00517))  
- CDHJKN Proposition 5.5 does support the stated graph-product fusion rule, and CDHJKN Theorem 2.4 supports the final factoriality/fullness claim under the state-zero-unitary hypothesis. ([ems.press](https://ems.press/content/serial-article-files/51743))  
- I compiled `answer.tex` with `pdflatex` twice. It compiled successfully to 6 pages. The document class is exactly `\documentclass[12pt]{article}`, the `fullpage` package is the only layout package, and I did not find prohibited font-size or spacing changes. Thus the LaTeX contract itself is not the reason for rejection.

## Detailed audit

### 1. Problem interpretation

The interpretation of irreducibility as “not a non-trivial join”, equivalently connected complement graph, is reasonable and is explicitly recorded. This satisfies the ambiguity requirement in the prompt.

The use of DKEP Lemma 8.5 is acceptable only after one knows that the final graph product \(M\) is a separable finite factor. The final section attempts to establish this using CDHJKN Theorem 2.4, which is a valid source for the full factor conclusion under the relevant assumptions. ([ems.press](https://ems.press/content/serial-article-files/51743))

### 2. Normal support bookkeeping lemma

This is the first major problem. The lemma asserts:

\[
(Y^{\sharp_J})^*=(pr_Y)\,\mathcal A_N\,(pr_Y),
\qquad r_Yp=pr_Y,
\]

where \(r_Y\) is the ordinary open support of \(Y\subset B(L^2N)\) and \(p\) is a simultaneous normal support projection. The proof says this is “precisely” DKEP Proposition 2.10. It is not. Proposition 2.10 gives an inclusion/intersection statement for simultaneous normal biduals; it does not state the ordinary open-support compression formula, nor the commutation \(r_Yp=pr_Y\), nor weak-* density of \(pYp\) in the asserted corner. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

This is not a minor citation issue. The later proof of the boundary-support intersection lemma depends critically on being able to compute \(q_U\) as \(pr_U\) and multiply support projections inside the ordinary bidual. Without a proved support-calculus lemma, the central inequality

\[
q_Wq_Uq_W\le q_{U\cap W}
\]

is not established.

The second half of the lemma also asserts that \(X\) and \(K_X(N)\) have the same normal-bidual support. The proof invokes DKEP Proposition 3.6, Corollary 3.2, and Proposition 2.4, but does not check the exact hypotheses needed to pass from vanishing on \(X\) to vanishing on \(K_X^{\infty,1}(N)\). DKEP Theorem 5.6 gives annihilator criteria for \(K_{X,Y}^{\infty,1}\), but with specific boundary-piece and multiplier assumptions. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) The answer states the conclusion for “any boundary piece” without proving the needed hypotheses.

**Status:** essential unproved lemma; proof not valid as written.

### 3. Subalgebra coefficient lemma

The answer claims that the coefficient boundary of

\[
\mathcal H_B={}_N L^2N_B\otimes_B {}_B L^2N_N
\]

is exactly the subalgebra boundary \(X_B\). This is plausible, but the proof given is incomplete.

DKEP Example 5.11 says that if \(B\subset M\) and one considers \(L^2M\) as an \(M\)-\(B\) correspondence, the corresponding boundary piece is the subalgebra boundary from Example 3.4. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) It does **not** directly say that the fused \(N\)-\(N\) correspondence \(L^2N\otimes_B L^2N\) has the same coefficient boundary.

The formula

\[
T_{\xi\otimes\bar\alpha}^{*}T_{\eta\otimes\bar\beta}
 =
T_\xi^{*}\theta_{\alpha,\beta}T_\eta
\]

is asserted without a careful convention check for left/right bounded vectors. More seriously, the proof says that \(\theta_{\alpha,\beta}\) are rank-one coefficients and that these recover the full \(e_BB(L^2N)e_B\cong B(L^2B)\) part in DKEP Example 3.4. But rank-one Hilbert-space operators generate \(\mathbb K(L^2B)\), not automatically all of \(B(L^2B)\). If “rank-one” means a Hilbert-module rank-one operator, this must be explained; if it means Hilbert-space rank-one, the argument is insufficient. DKEP Example 3.4 explicitly uses arbitrary \(T\in e_BB(L^2M)e_B\), not only rank-one \(T\). ([arxiv.org](https://arxiv.org/pdf/2204.00517))

**Status:** important identification underproved. Since later \(X_{M_U}\) is treated as the coefficient boundary of \(L^2M\otimes_{M_U}L^2M\), this gap propagates.

### 4. Direct sums and finite fusions lemma

This lemma has multiple issues.

First, it applies DKEP Theorem 5.10 to an arbitrary boundary piece \(X\), but Theorem 5.10 assumes \(M,JMJ\subset M(X)\) and \(N,JNJ\subset M(Y)\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) The lemma as stated omits this assumption.

Second, the infinite direct-sum argument is too terse. The proof says \(P_F\xi\to\xi\) and \(T_{P_F\xi}\to T_\xi\) in “the strong module topology” and that mixing operators are strongly closed in Theorem 5.10. The theorem’s proof contains a delicate closure argument for bounded vectors; the answer does not verify the required uniform boundedness and closure hypotheses. This is not automatic for arbitrary infinite direct sums.

Third, the finite-fusion coefficient algebra \(\mathcal C_U\) is asserted to be a \(*\)-algebra by “standard coefficient calculus”. The exact product formula depends on bounded-vector conventions and on inserting conjugate correspondences in the correct order. This can likely be proved, but it is an essential lemma and is not actually proved in the text.

Fourth, the construction of a contractive approximate unit for \(X_{M_U}\) rests on the previous coefficient-boundary identification. Since that identification is not established, this approximate-unit statement is not established either.

**Status:** essential lemma underproved.

### 5. Boundary-support intersection lemma

The CDHJKN fusion rule quoted here is supported by the literature: for graph-product bimodules \(H_U(V_1,V_2)\), fusing over the middle algebra decomposes as a direct sum over \(W\subset U_1\cap U_2\). ([ems.press](https://ems.press/content/serial-article-files/51743))

However, the proof’s operator-algebraic support step depends on the earlier unproved support calculus. In particular, the proof uses:

\[
q_U=pr_U,\qquad q_Wq_Uq_W=p(r_Wr_Ur_W)p,
\]

and the equality \(pr_{K_I}p=q_I\). These are precisely the unsupported claims from Lemma 1.

The passage

\[
h_\alpha k_\beta h_\alpha\in K_{X_{M_I}}(M)
\quad\Longrightarrow\quad
r_Wr_Ur_W\in r_{K_I}A^{**}r_{K_I}
\]

also needs more detail. It requires a controlled choice of approximate units, norm approximation by finite-fusion coefficients, strong-* convergence in the ordinary bidual, and strong-* closedness of the hereditary corner. The answer sketches this but does not rigorously justify all limiting steps.

**Status:** central lemma not rigorously proved.

### 6. Finite-boundary-to-compact-boundary lemma

This lemma is one of the more convincing parts, but it still depends on previous support facts.

The compression argument using \(q_i^\perp\) is plausible: DKEP states that the support projection of \((K_X(M)^{\sharp_J})^*\) commutes with both \(M\) and \(JMJ\), which is what is needed for the calculation. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

However, the final hypertrace construction invokes a “canonical” u.c.p. map

\[
\Theta_0:B(L^2N)\to q_0\mathcal A_Nq_0
\]

with \(\Theta_0(x)=xq_0\). DKEP Lemma 8.5 does mention natural u.c.p. maps from \(B(L^2M)\) into the normal-bidual compact corner, but the answer does not quote or prove the specific formula used here. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) This is probably fixable, but it is still a missing detail in the current proof.

**Status:** mostly plausible, but not fully rigorous as written.

### 7. Relative Bass–Serre proposition

This section is plausible but contains handwaving.

The commutator formula

\[
[p,JxJ]=(1-e_B)JxJe_B-e_BJxJ(1-e_B),\qquad [q,JxJ]=0
\]

for \(x\in P\ominus B\) is stated with only a brief reduced-word explanation. A strict proof should check the AFP normal form on all possible word types, including one-letter words and the \(B\)-vacuum component.

The use of DKEP Lemma 6.1 is appropriate in principle: DKEP Lemma 6.1 says that it suffices to verify the commutator condition on an ultraweakly dense generating subalgebra. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) But the answer should explicitly check the condition for adjoints as well, and should explain why the centered \(P\), centered \(Q\), and \(B\) pieces generate \(N\) in the required sense.

The paradoxical inequalities

\[
w_1qw_1^*+w_2qw_2^*\le p,\qquad apa^*\le q
\]

are reasonable, but again only sketched. The proof of \(q\,w_1^*w_2\,q=0\) from \(E_B(w_1^*w_2)=0\) needs an explicit AFP reduced-word argument.

**Status:** likely repairable, but not complete at strict-referee level.

### 8. Graph-product application

The graph combinatorics are correct. I also exhaustively checked the two local combinatorial claims for graphs up to six vertices by code: connected complement implies \(C(v)\neq\varnothing\), and if \(C(v)=\{r\}\), then there is \(s\in\operatorname{Lk}(v)\) with \(s\not\sim r\). This code check is only a sanity check, but no issue was found.

The standard graph-product AFP decomposition

\[
M\cong M_{V\setminus\{v\}}*_{M_{\operatorname{Lk}(v)}}(M_{\operatorname{Lk}(v)}\bar\otimes M_v)
\]

is used without citation or proof. This is standard, but a complete proof should cite a graph-product reference or include a short verification.

The final appeal to CDHJKN Theorem 2.4 is valid for factoriality/fullness under the state-zero-unitary hypothesis. ([ems.press](https://ems.press/content/serial-article-files/51743)) The conclusion “diffuse full factor, hence non-amenable” is standard, but should be cited or replaced with a direct use of CDHJKN’s amenability criterion. CDHJKN Proposition 6.3 gives an amenability characterization that could be used directly. ([ems.press](https://ems.press/content/serial-article-files/51743))

**Status:** final application is structurally plausible, but it depends on the unproved technical lemmas above.

## Overall conclusion

The answer has a coherent high-level strategy, and several cited ingredients are real. However, the current `answer.tex` does **not** constitute a complete rigorous solution. The proof’s main technical engine—the support calculus for DKEP normal biduals and its interaction with graph-product fusion coefficients—is asserted rather than proved, and at several points the cited DKEP results do not state the stronger claims used in the argument. These are essential gaps, not merely missing exposition.