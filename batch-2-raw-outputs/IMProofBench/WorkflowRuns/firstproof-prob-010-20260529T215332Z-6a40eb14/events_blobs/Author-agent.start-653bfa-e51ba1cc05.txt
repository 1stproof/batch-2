## Referee report on the revised draft

### Overall verdict

The revision addresses two previous concerns: the false non-normal meet-of-projections argument has been replaced by a palindromic-product criterion, and the compact-corner hypertrace step no longer identifies \(q_0\mathcal A_Nq_0\) with \(B(L^2N)\) directly.

However, the proof is still **not complete**. The central new “normal-bidual support-sandwich principle” is not justified and, as written, conflicts with an important warning in DKEP: the canonical embedding into the normal bidual is generally **not multiplicative**. Therefore concrete inclusions such as \(L^*BL\subset D\) cannot simply be passed to weak-* closures inside \(\mathcal A_N\) using von Neumann algebra multiplication. This invalidates the proof of the graph-product boundary-corner intersection lemma, which is essential for the final theorem.

### LaTeX contract

I recreated and compiled `answer.tex` with `pdflatex` twice. It compiles successfully to a 5-page PDF. The document uses exactly `\documentclass[12pt]{article}`, uses only the permitted `fullpage` layout package, and I found no forbidden line-spacing, margin, or font-size changes. The LaTeX contract appears satisfied.

### Literature validation

DKEP define boundary pieces as hereditary \(C^*\)-subalgebras and then define the associated \(\mathbb K_X(M)\) using the \(k\cdot k_{\infty,2}\)-closed left ideal \(\mathbb K^L_X\), not merely as the original boundary piece \(X\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) DKEP also explicitly warn that the canonical embedding \(A\to (A^\sharp)^*\) is generally only a complete order embedding, not a \(*\)-homomorphism. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) This is directly relevant to the revised proof’s support-calculus argument.

DKEP Example 5.11 does define coefficient boundary pieces, and DKEP record the Connes-fusion coefficient formula \(T_{\xi\otimes\eta}=T_\eta T_\xi\). ([arxiv.org](https://arxiv.org/pdf/2204.00517)) CDHJKN provide the graph-product bimodule/fusion formulas cited by the author. ([ems.press](https://ems.press/content/serial-article-files/51743)) CDHJKN also give the factoriality criterion and the relative amenability criterion used in the last section. ([ems.press](https://ems.press/content/serial-article-files/51743))

### Detailed audit

#### 1. Problem statement and interpretation

This part is acceptable. The author explicitly adopts the standard graph-product interpretation of irreducibility as nontrivial join-irreducibility, equivalently connectedness of \(\Gamma^c\). This is necessary because the original problem statement’s wording is slightly ambiguous.

#### 2. Normal-bidual setup

The definitions of \(\mathcal A_N\), \(q_X\), and \(\widetilde S_X(N)\) are broadly consistent with DKEP Lemma 8.5. For a separable finite factor with the trivial group action, the center-ergodicity hypothesis in DKEP Lemma 8.5 is automatic. DKEP Lemma 8.5 gives the normal-bidual no-central-state criterion used later. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

This setup is fine, but the subsequent “support calculus” is not.

#### 3. Boundary support calculus: fatal gap

The claimed support-sandwich principle says that for hereditary \(C^*\)-subalgebras \(B,D\subset B(L^2N)\) and a left ideal \(L\),
\[
L^*BL\subset D
\quad\Longrightarrow\quad
r(p_B\mathcal A_Np_B)r\subset p_D\mathcal A_Np_D.
\tag{1}
\]
The proof treats the normal bidual as though it were an ordinary weak-* closure of \(B(L^2N)\) with multiplication extending concrete multiplication. This is not justified.

DKEP’s normal bidual is not the usual enveloping von Neumann algebra. DKEP explicitly state that the canonical embedding \(A\to(A^\sharp)^*\) need not be a \(*\)-homomorphism. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) Therefore the line

> “separate weak-* continuity of multiplication sends the inclusion \(L^*BL\subset D\) to …”

is not valid as written. The inclusion \(L^*BL\subset D\) is an inclusion for concrete products inside \(B(L^2N)\), but the products in \(\mathcal A_N\) are products in the normal-bidual von Neumann algebra. Without a theorem proving compatibility of these products for the relevant supports and ideals, the argument does not go through.

This is not a cosmetic issue. It is the main engine behind the graph-product boundary intersection lemma.

#### 4. Correspondence support inclusion

The claimed inclusion
\[
q_{\mathcal H}(q_{\mathcal K}\mathcal A_Nq_{\mathcal K})q_{\mathcal H}
\subset
q_{\mathcal H\otimes_N\mathcal K}\mathcal A_Nq_{\mathcal H\otimes_N\mathcal K}
\tag{2}
\]
still lacks a rigorous proof. The coefficient identity
\[
T_\xi^*(T_\eta^*T_{\eta'})T_{\xi'}
=
T_{\xi\otimes\eta}^*T_{\xi'\otimes\eta'}
\]
is correct at the level of coefficient generators, using DKEP’s fusion formula. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) But the proof then jumps from generator-level containment to support-corner containment in the DKEP normal bidual.

There are two unresolved problems:

1. \(q_{\mathcal H}\) is the support of \(\mathbb K_{X_{\mathcal H}}(N)\) in the DKEP normal bidual, not merely the ordinary support of the hereditary algebra generated by \(T_\xi^*T_\eta\). DKEP’s \(\mathbb K_X(M)\) is built through the \(k\cdot k_{\infty,2}\)-closed left ideal and is not simply the original coefficient boundary piece. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

2. The proof of (2) depends on the invalid support-sandwich principle above.

Thus the correspondence support inclusion remains an essential unproved lemma.

#### 5. Graph-product boundary-corner intersection lemma

The lemma
\[
q_W(q_U\mathcal A_Mq_U)q_W
\subset q_{U\cap W}\mathcal A_Mq_{U\cap W}
\tag{3}
\]
depends entirely on the preceding support calculus. Since that support calculus is not established, this lemma is not proved.

There are also minor internal issues:

- In the proof, the sentence “Applying (1) to \(\mathcal H_W\) and \(\mathcal H_U\)” appears to mean applying equation (2), not equation (1).
- The sentence “proving (2)” near the end should say “proving (3).”

These numbering slips are minor, but the unproved support-corner inclusion is fatal.

The CDHJKN fusion rule itself is relevant and correctly points in the intended direction: their Main Theorem 0.4 / Theorem 5.4 / Proposition 5.5 provide the bimodule decomposition and fusion rules. ([ems.press](https://ems.press/content/serial-article-files/51743)) But CDHJKN do not prove the DKEP normal-bidual support statement needed here.

#### 6. Finite palindromic boundary criterion

This section is substantially improved. The previous false argument involving lattice meets of noncommuting projections has been replaced by the palindromic product
\[
R=q_mq_{m-1}\cdots q_1q_2\cdots q_m,
\]
which is a positive contraction. If a state takes value \(1\) on each \(q_i\), then after extending the state to the generated \(C^*\)-algebra, the GNS vector is fixed by each \(q_i\), hence by \(R\). This avoids the earlier non-normal-meet problem.

The compact-corner issue is also improved. DKEP’s proof of Lemma 8.5 does provide natural u.c.p. maps from \(B(L^2M)\) into the normal-bidual compact corner. ([arxiv.org](https://arxiv.org/pdf/2204.00517)) The author should cite this more precisely and specify the bimodularity needed, but this part is plausibly repairable.

The finite criterion would be acceptable if hypothesis (5) were actually established. In the application, however, (5) depends on the unproved graph-product boundary intersection lemma.

#### 7. Relative Bass–Serre paradox

This section is improved. The reduced-word commutator formulas
\[
[p,R_x]=R_xe_B-e_BR_x,\qquad [q,R_x]=0
\]
for \(x\in P\ominus B\), and the analogous formulas for \(x\in Q\ominus B\), are plausible. DKEP Lemma 6.1 is indeed the correct tool for reducing the \(S_X(M)\)-membership check to an ultraweakly dense generating algebra. ([arxiv.org](https://arxiv.org/pdf/2204.00517))

The proof is still terse, but this part is likely repairable by writing out the reduced-word calculation in full. I do not regard this as the main obstruction.

#### 8. Application to graph products

The graph-product decomposition over \(M_{\operatorname{Lk}(v)}\) is standard. The construction of the unitaries \(w_1,w_2\) in the two complement-neighbor cases appears correct.

The factoriality argument is consistent with CDHJKN Main Theorem 0.5: connectedness of \(\Gamma^c\) with at least three vertices rules out universal vertices and isolated exceptional complement edges. ([ems.press](https://ems.press/content/serial-article-files/51743))

The nonamenability argument is also consistent with CDHJKN Main Theorem 0.1: applying the relative amenability criterion with \(V_1=V\), \(V_2=\varnothing\) would force every nonedge to be an exceptional isolated complement edge, impossible in a connected complement graph with at least three vertices. ([ems.press](https://ems.press/content/serial-article-files/51743))

But the final passage from relative proper proximality for the link boundary pieces to ordinary proper proximality depends on the unproved palindromic compact-corner inclusion, which in turn depends on the invalid support-sandwich argument.

### Previous concerns: status

- **False meet-of-projections argument:** addressed.
- **Compact-corner identification \(q_0\mathcal A q_0\cong B(L^2N)\):** addressed in spirit by using a DKEP u.c.p. map, though the exact cited properties should be stated more carefully.
- **Bass–Serre \(p,q\in S_{X_B}\):** partially addressed; now plausible but still abbreviated.
- **Unsupported DKEP support/fusion calculus:** not resolved. It has been replaced by a new support-sandwich principle, but that principle is not proved and is incompatible with the nonmultiplicativity warning in DKEP.
- **New issue:** the proof conflates the coefficient boundary \(X_{\mathcal H}\) with the associated DKEP \(\mathbb K_{X_{\mathcal H}}\)-corner; this is nontrivial and not justified.

### Final assessment

The revised proof is closer in structure, but it still contains a fatal gap in the normal-bidual support calculus. The theorem is not rigorously proved by the submitted `answer.tex`.