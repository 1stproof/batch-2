### Council member: gpt-55-pro (models/openai/gpt-55-pro) ###
My take: the revised strategy is basically the right one, but I would make one repair before trusting the boundary-corner lemma.

1. **Computing \(q_{X_{M_U}}\) from the original boundary piece.**  
   This is rigorous if phrased as a *normal-support* statement, not as an equality of ordinary supports. I would write:
   \[
   q_X=\text{unit of the weak-* closure of the image of }X\text{ in }(B(L^2N)^{\sharp_J})^*.
   \]
   DKEP Prop. 3.6 plus \(\|\cdot\|_{\infty,1}\)-continuity of \(\sharp_J\)-functionals gives the same annihilator for \(X\) and \(K_X(N)\), hence the same normal-bidual support. Then DKEP Prop. 2.10 identifies this support with \(p_{\rm nor}s_X\) when \(s_X\) is the ordinary open support of the relevant hereditary boundary algebra. I would avoid saying that \(X\) and \(K_X\) have the same ordinary support in \(B(L^2N)^{**}\).

2. **Modeling \(X_{M_U}\) by \(\mathcal H_U=L^2M\otimes_{M_U}L^2M\).**  
   This is also fine, but state it as a support/coefficient identification: the cyclic vector \(1\otimes1\) has coefficient \(e_{M_U}\), and Hilbert amplifications recover the full middle corner appearing in DKEP Example 3.4. Thus the normal support of \(X_{M_U}\) is the support of the amplified coefficient algebra of \(\mathcal H_U\). This avoids needing a stronger literal equality than DKEP’s examples provide.

3. **Main remaining gap: the two-factor product formula.**  
   The line
   \[
   (T_{\xi_1}^*T_{\xi_2})(T_{\eta_1}^*T_{\eta_2})
   =T_{\xi_1\otimes\bar\xi_2\otimes\eta_1}^*T_{\eta_2}
   \]
   is the vulnerable point. Unless you set up a rectangular coefficient calculus, the two \(T\)-operators here naturally have different target correspondences. A critic can object that the expression is not literally defined in the stated framework.

   The shortest repair is to replace the double-product argument by a **triple-product support lemma**.

   Prove the elementary support lemma:

   > If \(B,C,D\subset A\) are hereditary \(C^*\)-subalgebras with supports \(b,c,d\), and
   > \[
   > BCB\subset dA^{**}d,
   > \]
   > then
   > \[
   > b(cA^{**}c)b\subset dA^{**}d.
   > \]
   > Proof: approximate elements of \(cA^{**}c\) weak-* by bounded nets from \(C\), sandwich by approximate units of \(B\), and pass to weak-* limits.

   Then prove on coefficient generators:
   \[
   (T_{\xi_1}^*T_{\xi_2})(T_{\eta_1}^*T_{\eta_2})(T_{\xi_3}^*T_{\xi_4})
   =
   T_{\xi_1\otimes\bar\xi_2\otimes\eta_1}^{\,*}
   T_{\xi_4\otimes\bar\xi_3\otimes\eta_2}.
   \]
   Now both vectors lie in an amplification of
   \[
   \mathcal H_W\otimes_M\overline{\mathcal H_W}\otimes_M\mathcal H_U
   \cong
   \mathcal H_W\otimes_M\mathcal H_W\otimes_M\mathcal H_U.
   \]
   CDHJKN fusion, applied twice, gives a direct sum of \(\mathcal H_Z\)’s with \(Z\subset U\cap W\). The direct-sum support argument then puts this triple product in \(s_{U\cap W}A^{**}s_{U\cap W}\). Hence
   \[
   s_W(s_UA^{**}s_U)s_W\subset s_{U\cap W}A^{**}s_{U\cap W},
   \]
   and cutting by \(p_{\rm nor}\) gives the desired
   \[
   q_W(q_U\mathcal A_Mq_U)q_W\subset q_{U\cap W}\mathcal A_Mq_{U\cap W}.
   \]

The direct-sum support argument itself looks acceptable; just use finite-coordinate truncation/strong-* convergence, not norm convergence.

### Council member: opus_47_max (models/anthropic/opus_47_max) ###
**Strategy assessment.** The overall route is rigorous and the three pieces you flag are defensible. Some specific notes:

**(1) $q_{X_{M_U}}$ from $X_{M_U}$ via DKEP 3.6.** Fine. The chain: DKEP 3.6 gives $\overline{X}^{\infty,1}=\overline{K_X}^{\infty,1}$; elements of $A^{\sharp_J}$ are by construction continuous for $\|\cdot\|_{\infty,1}$ (DKEP §2.3 / Lemma 2.4); so $X$ and $K_X$ have identical $\sharp_J$-annihilators and identical normal supports in $\mathcal A_N$. I'd promote your one-clause "since $\sharp_J$-functionals are continuous…" to an explicit citation — that step carries real weight.

**(2) Coefficient model.** Yes — Examples 3.4 and 5.11 together with Hilbert amplifications recover the whole $e_{M_U}$-corner. The amplification is essential: without it you only span finite-rank coefficients. Verify your $T_\xi$ convention (left vs right) is consistent throughout: $T_{\alpha\otimes\beta}=T_\beta T_\alpha$ flips with the opposite convention.

**(3) Fusion + direct-sum support.** Structure is correct, with two small tightenings.

*(a) Monotonicity $X_{M_Z}\subset X_{M_I}$ for $Z\subset I$.* Your parenthetical is right but compressed, and the whole lemma turns on it. Clean inline version: $e_{M_I}\in X_{M_I}$ (take $a=b=1$); $L^2M_Z\subset L^2M_I$ gives $e_{M_Z}\le e_{M_I}$, so $e_{M_Z}\in X_{M_I}$ by heredity; the $M$-bimodule multiplier action puts $ae_{M_Z}b\in X_{M_I}$; another heredity pass absorbs $X_{M_Z}$ into $X_{M_I}$.

*(b) CDHJKN citation.* You need the asymmetric fusion
$$\mathcal H_U\otimes_M\mathcal H_W\;\cong\;\bigoplus_Z\mathcal H_Z^{\oplus k_Z},\qquad Z\subset U\cap W,$$
applied twice (first to $\mathcal H_W\otimes\overline{\mathcal H_W}$, then to each summand $\otimes\mathcal H_U$). I'd verify that Prop 5.5 / Thm 5.4 literally delivers the $Z\subset U\cap W$ constraint in the asymmetric case, not just the symmetric $Z\subset W$ for $\mathcal H_W^{\otimes 2}$. If only the symmetric form is stated, two lines suffice: any cyclic vector in $\mathcal H_U$ is fixed by $e_{M_U}$ on the appropriate side and similarly for $\mathcal H_W$; so any surviving $\mathcal H_Z$-label satisfies $L^2M_Z\subset L^2M_U\cap L^2M_W = L^2 M_{U\cap W}$ — using $e_{M_U}e_{M_W}=e_{M_{U\cap W}}$, a standard graph-product fact — hence $Z\subset U\cap W$.

**Otherwise:** the rectangular support fact (2), the sandwich lemma (3), the strong-* coordinate-truncation argument for infinite direct sums, and the $p_{\rm nor}$-cut via Prop 2.10 are all correctly deployed. The proof is in good shape — my prediction is that any remaining critic objection lands on (3a) or (3b), and both have one-sentence repairs that easily fit your 12-page budget.

One sanity check worth doing yourself: the commutation $e_{M_U}e_{M_W}=e_{M_{U\cap W}}$ (equivalently, $E_{M_U}\circ E_{M_W}=E_{M_{U\cap W}}$ via the reduced-word structure) is a property of graph products that you implicitly rely on. A half-sentence citing this (CDHJKN §2/§3 should record it) closes it cleanly if the line-by-line critic asks.

### Council member: gemini-31-pro (models/gemini/gemini-31-pro) ###
Here is my assessment of the current strategy and how I would tighten the remaining gaps.

**1. The normal support computation**  
Your computation of $q_X = p_{\rm nor} s_U$ via $\sharp_J$-annihilators and DKEP Proposition 3.6 is elegant and rigorous. Because annihilators only depend on the $\|\cdot\|_{\infty,1}$-closure, this perfectly bridges the concrete algebraic generators of $X_{M_U}$ to the formal support projections $q_U$ in the bidual. You have cleanly avoided making unsupported claims about the multiplicativity of the normal-bidual embedding.

**2. The gap in the fusion intersection lemma**  
There is a serious syntactic gap in Equation (7). In DKEP (Definition 5.1 and Example 5.11), the coefficient boundary $X_{\mathcal H}$ is generated by $L_\xi^* R_\eta$, where $L_\xi(x) = x\xi$ and $R_\eta(x) = \xi x$. These operators map $L^2 M \to \mathcal H \to L^2 M$. The notation $T_\xi^* T_\eta$ in your draft conflates left and right modular actions. More importantly, you cannot naively concatenate $(L_{\alpha}^* R_{\beta})(L_{\gamma}^* R_{\delta})$ into a single $L^* R$ of a Connes fusion tensor product using the identity $T_{\alpha\otimes\beta} = T_\beta T_\alpha$; the domains, codomains, and inner products do not match algebraically. 

**3. The shortest rigorous repair**  
You can bypass abstract correspondence calculus entirely by evaluating the concrete generators of $X_{M_U}$. By DKEP Example 3.4/5.11, $X_{M_U}$ is the norm closure of $\text{span}\{x e_U y : x,y \in M\}$. Therefore, the product $X_{M_W} X_{M_U} X_{M_W}$ is topologically spanned by operators of the form 
\[
    S = x_1 e_W a e_U b e_W x_2.
\]
Here is the golden insight: the core operator $e_W a e_U b e_W$ evaluates on $x \in L^2 M$ as $E_W(a E_U(b E_W(x)))$. This action is **exactly** a coefficient of the 4-fold Connes fusion correspondence $\mathcal H = \mathcal H_W \otimes_M \mathcal H_U \otimes_M \mathcal H_W \otimes_M \mathcal H_W$. 

To prove this in your draft, define the vectors:
\[
    \zeta_1 = \hat 1_W \otimes a^* \hat 1_U \otimes \hat 1_W \otimes \hat 1_W, \qquad \zeta_2 = \hat 1_W \otimes \hat 1_U \otimes b \hat 1_W \otimes \hat 1_W.
\]
Evaluate $L_{\zeta_1}^* R_{\zeta_2}(x)$ by testing against $w \in L^2M$. Computing the inner product $\langle w\zeta_1, \zeta_2 x \rangle_{\mathcal H}$ iteratively right-to-left gives:
1. $\langle w\hat 1_W, \hat 1_W \rangle_M = E_W(w^*)$
2. $\langle a^*\hat 1_U, E_W(w^*)\hat 1_U \rangle_M = E_U(a E_W(w^*))$
3. $\langle \hat 1_W, E_U(a E_W(w^*)) b \hat 1_W \rangle_M = E_W(E_U(a E_W(w^*)) b)$
4. Applying the final $\tau$ against $\hat 1_W x$ yields:
\[
 \tau\big( E_W(E_U(a E_W(w^*)) b) E_W(x) \big) = \tau\big( w^* E_W(a E_U(b E_W(x))) \big).
\]
Hence, $L_{\zeta_1}^* R_{\zeta_2} = e_W a e_U b e_W$. Consequently, $S = L_{\zeta_1 x_1^*}^* R_{\zeta_2 x_2} \in X_{\mathcal H}$. 

Now apply your fusion tools: by CDHJKN Proposition 5.5, $\mathcal H_W \otimes_M \mathcal H_W \cong \bigoplus_{Y \subset W} \mathcal H_Y$. Applying this to the 4-fold correspondence, $\mathcal H$ decomposes into a direct sum of correspondences $\mathcal H_Z$ for $Z \subset W \cap U \cap W \cap W = U \cap W$. 

By your existing direct-sum support argument (which correctly uses finite coordinate truncations), the coefficient algebra $X_{\mathcal H}$ is supported by $\bigvee s_Z \le s_{U \cap W}$. This immediately establishes the inclusion $X_{M_W} X_{M_U} X_{M_W} \subset s_{U\cap W} A^{**} s_{U\cap W}$. 

Sandwiching by approximate units for $X_{M_W}$ gives $s_W s_U s_W \subset s_{U \cap W} A^{**} s_{U \cap W}$. Finally, cut by $p_{\rm nor}$ to obtain $q_W q_U q_W \subset q_{U \cap W} \mathcal A_M q_{U \cap W}$, yielding your palindromic containment.

This fix requires replacing roughly 15 lines of the `Lemma 1` proof, perfectly respects your 12-page limit, and relies only on rock-solid concrete inner product evaluations.