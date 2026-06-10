## Referee report on the revised `answer.tex`

### Overall verdict

The revision substantially improves the previous draft: it adds a problem-interpretation section, expands the finite-boundary/GNS argument, gives more Bass–Serre reduced-word detail, and makes the graph-product expectation checks more explicit. However, I still cannot certify the proof as complete. The main remaining obstruction is the **ordinary-bidual support bookkeeping lemma**, which is essential for the boundary-intersection argument and is still not justified with the exact hypotheses and exact statements available from DKEP.

### LaTeX contract

I see no visible violation of the First Proof LaTeX contract:

- correct class: `\documentclass[12pt]{article}`;
- only `fullpage` among layout packages;
- no apparent prohibited font-size, line-spacing, or margin commands;
- source is a standalone document.

The author reports successful compilation to 7 pages. Since the mathematical proof is not answer-ready, no further LaTeX issue affects the final verdict.

---

## Literature validation

The cited literature is real and relevant.

DKEP does define the normal-bidual machinery, boundary pieces, \(K_X(M)\), \(\widetilde S_X(M)\), and the characterization of proper proximality via absence of central states on \(\widetilde S_X(M)\). In particular, DKEP Lemma 8.5 states the relevant no-central-state criterion in the normal bidual. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

DKEP Theorem 5.10 and Proposition 5.9 support the use of bounded-vector coefficient operators \(T_\xi\), the fusion identity \(T_{\xi\otimes\eta}=T_\eta T_\xi\), and the relative-compactness criterion via \(T^*T\) and \(TT^*\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) DKEP Example 5.11 identifies the coefficient boundary piece \(X_H\), and in the case \(H=L^2M\) as an \(M\)-\(B\) correspondence it recovers the subalgebra boundary from Example 3.4. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) DKEP Lemma 6.1 and Theorem 6.2 are also the right tools for the Bass–Serre/proper-proximality argument. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

CDHJKN contains the graph-product bimodule decomposition and fusion rules used in the intersection lemma. Their fusion formula has the form
\[
H_{U_1}(V_1,V_2)\otimes_{M_{V_2}}H_{U_2}(V_2,V_3)
 \cong \bigoplus_{W\subset U_1\cap U_2}H_W(V_1,V_3)^{\oplus k},
\]
which is exactly the kind of input the proof needs. ([arxiv.org](https://arxiv.org/pdf/2404.08150)) CDHJKN Theorem 2.4 also supports the final claim that a join-irreducible graph product with at least three vertices and state-zero vertex unitaries is a diffuse full factor. ([arxiv.org](https://arxiv.org/pdf/2404.08150)) Caspers–Fima support the star/link amalgamated-free-product decomposition used in equation (8). ([ems.press](https://ems.press/content/serial-article-files/30688))

---

## Previously raised concerns and their status

### 1. Problem interpretation

**Addressed.** The revised draft explicitly records that “irreducible” means join-irreducible, equivalently connected complement graph. This is a faithful and standard interpretation of the stated condition.

### 2. Normality of central states in the factor case

**Addressed.** The revised draft now correctly says that for a finite factor, ruling out central states whose restriction is normal is equivalent to ruling out central states restricting to the trace, after normalization.

### 3. Direct sums and DKEP Theorem 5.10

**Mostly addressed.** The revised text now argues using the cyclic-vector criterion from DKEP Theorem 5.10 rather than informal finite-support approximation. This is much better. The direct-sum argument is still concise, but it is now plausibly valid: the union of cyclic sets in the summands is cyclic for the Hilbert direct sum, and Theorem 5.10 then controls arbitrary bounded vectors.

### 4. Finite-boundary-to-compact-boundary lemma

**Substantially addressed.** The revised proof now explicitly handles the operator-system issue by extending the state only as a GNS device and noting that the relevant projections and palindromic product lie in \(\widetilde S(N)\). The compression argument and the use of the canonical u.c.p. map into the compact normal corner are now much clearer and align with DKEP Lemma 8.5.

### 5. Bass–Serre paradox

**Improved, probably acceptable modulo minor expansion.** The reduced-word explanation is now more detailed. The proof still compresses some AFP normal-form checks, but the argument is now recognizable and plausible: the first-letter projections, commutator computations, paradoxical inequalities, and \(B\)-Haar unitary argument all match the DKEP free-product strategy.

### 6. Graph-product application

**Mostly addressed.** The revised expectation computations for \(w_1,w_2\) are explicit enough, and the final use of CDHJKN Theorem 2.4 is supported by the literature.

---

## Remaining serious issue: support bookkeeping lemma

The main unresolved problem is Lemma `ordinary support bookkeeping`.

The proof asserts that if \(p_\ell,p_r\) are the one-normal support projections for the \(N\)- and \(JNJ\)-module structures, then DKEP Proposition 2.10 “realizes”
\[
(A_N^{\sharp_J})^* = p_\ell p_r A_N^{**}p_\ell p_r,
\]
and “in particular” \(p_\ell,p_r\) commute. This is not stated in DKEP Proposition 2.10 in the form quoted. Proposition 2.10 states that the simultaneous normal bidual is the intersection of the two one-normal biduals inside \(M(A)^{**}\), and it gives a nonunital inclusion for invariant subalgebras; it does not explicitly identify the unit as \(p_\ell p_r\) or prove the commutation of \(p_\ell\) and \(p_r\). ([arxiv.org](https://arxiv.org/pdf/2204.00517))

This may be derivable, especially because the one-normal support projections lie in biduals of commuting multiplier algebras, but the derivation is not written. Since the later proof uses
\[
q_Wq_Uq_W=(pr_Wp)(pr_Up)(pr_Wp)=p\,r_Wr_Ur_W\,p,
\]
the exact support projection \(p\), its commutation with ordinary supports, and the legitimacy of multiplying these projections inside \(A^{**}\) are essential. The proof cannot simply cite Proposition 2.10 for a stronger product formula than the source visibly states.

There is also a missing hypothesis: DKEP’s one-normal support discussion for a subalgebra \(B\subset A\) assumes that the multiplier representation of \(M\) on \(B\) is faithful. The original draft included this faithfulness assumption; the revised lemma removed it. DKEP’s support statement explicitly includes a faithfulness condition for the subalgebra multiplier action. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) Boundary pieces used later probably satisfy faithfulness, but the lemma as stated is broader than the available theorem and should be corrected.

Finally, the equality
\[
q_X=p_Nr_X=p_N\rho_X
\]
is still underjustified. The proof says DKEP Proposition 2.4 “identifies \(A_N^{\sharp_J}\) with the functionals continuous for this topology.” That is not the exact statement of Proposition 2.4. Proposition 2.4 is an annihilator characterization of simultaneous strong bimodule closure, not a direct identification with all \(\|\cdot\|_{\infty,1}\)-continuous functionals. The intended conclusion may be true using Proposition 3.6 plus the strong-bimodule annihilator formulation, but the current proof does not spell it out accurately enough.

Because Lemma `ordinary support bookkeeping` is used directly in the proof of the boundary-support intersection lemma, this is not a cosmetic issue. It is an essential technical bridge.

---

## Boundary-intersection lemma after revision

The revised monomial tracking is much improved. The argument that products of the form
\[
T_{\alpha_1}^*T_{\alpha_2}T_{\beta_1}^*T_{\beta_2}
T_{\alpha_3}^*T_{\alpha_4}
\]
can be rewritten, using conjugates and the identity \(T_{\xi\otimes\eta}=T_\eta T_\xi\), as a coefficient operator of a finite fusion whose labels include both \(W\) and \(U\), is now much clearer. The CDHJKN fusion rule then gives labels contained in \(W\cap U\), as required. ([arxiv.org](https://arxiv.org/pdf/2404.08150))

However, the conclusion
\[
0\le q_Wq_Uq_W\le q_{U\cap W}
\]
still depends on the ordinary-bidual support lemma. Since that lemma remains inadequately justified, the intersection lemma remains unproved at referee standard.

---

## Minor issues and possible fixes

1. **Restore faithfulness hypotheses** in Lemma `ordinary support bookkeeping`, or restrict it explicitly to the boundary pieces actually used.

2. **Replace \(p_\ell p_r\) by the meet/support projection** of the simultaneous normal bidual unless the commutation of \(p_\ell,p_r\) is proved. If the author wants to use \(p_\ell p_r\), they must prove that the one-normal supports commute in \(A_N^{**}\).

3. **Rewrite the proof of \(q_X=p_Nr_X=p_N\rho_X\)** using the exact DKEP statements: Proposition 3.6 gives equality of \(\|\cdot\|_{\infty,1}\)-closures, while Proposition 2.4 gives the simultaneous strong-bimodule annihilator characterization. The current wording is too imprecise.

4. In the Bass–Serre proposition, the reduced-word verification is probably correct, but a fully formal proof should explicitly handle the length-one cancellation cases in the AFP normal form.

---

## Final assessment

The revised proof is significantly stronger than the previous version and most earlier objections have been addressed. Nevertheless, the proof still relies on an essential support-calculus lemma that is not stated with correct hypotheses and is not fully derived from the cited DKEP results. Since this lemma is indispensable for converting relative boundary supports into the compact boundary, the proof is not yet a complete rigorous solution.