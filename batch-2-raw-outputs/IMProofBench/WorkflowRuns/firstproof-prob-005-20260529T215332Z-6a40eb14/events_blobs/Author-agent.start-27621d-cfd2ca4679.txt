## Referee report

### Overall verdict

`answer.tex` is **not answer-ready**. It explicitly ends by saying that it “does not yet constitute an unconditional proof or disproof of the statement.” That is correct: the document proves only conditional uniqueness, assuming extra all-starting-point absolute-continuity/Feller/equicontinuity/entrance/capacity estimates that are not part of the problem hypotheses and are not proved.

The main mathematical obstruction is real, not cosmetic: an \(L^2(\pi)\) spectral gap and reversibility with respect to \(\pi\) do **not** rule out additional invariant measures supported on \(\pi\)-null exceptional sets. The submitted proof never excludes such measures for the actual all-starting-point ABLM semigroup.

### Literature and source validation

The cited ABLM 2024 paper is correctly identified bibliographically, and its abstract confirms that it treats stochastic heat equations with distributional drift, including \(b=\delta_0\), in a regularized/mild framework. The problem’s Dirichlet-boundary extension is indeed an additional assumption beyond what is directly visible in the cited summaries. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/?utm_source=openai))

The cited 2025 Athreya–Butkovsky–Lê–Mytnik weak/mild equivalence paper exists and states equivalence results for weak and mild regularized notions; however, the visible statement says the settings are periodic, Neumann, or \(\mathbb R\), not Dirichlet. Thus any use of that paper for the present Dirichlet problem would itself require an extension or an explicit assumption. ([link.springer.com](https://link.springer.com/article/10.1007/s40072-025-00392-x))

The Bounebache–Zambotti paper is correctly cited as treating a singular local-time drift, a Gibbs invariant measure, and a Markov solution associated with a Dirichlet form. Indexed thesis material describing the same program also emphasizes that strong Feller was not proved and that absolute continuity is obtained in a Dirichlet-form sense with a semigroup/kernel representation only \(\nu\)-a.s., which is consistent with the exceptional-set concern raised in `answer.tex`. ([arxiv.org](https://arxiv.org/abs/1105.2779))

### LaTeX contract check

I compiled the supplied `answer.tex` twice with `pdflatex`. It compiled successfully and produced a 5-page PDF. The document uses exactly `\documentclass[12pt]{article}`, uses only the permitted `fullpage` layout package, and I found no forbidden margin, line-spacing, or in-document font-size changes. So the LaTeX contract is satisfied. The negative verdict is mathematical, not due to formatting.

---

## Paragraph-by-paragraph mathematical audit

### 1. “Problem statement and interpretation”

The adopted interpretation (A),
\[
P_t^n\Phi(x)\to P_t\Phi(x)
\]
for bounded continuous \(\Phi\), deterministic \(x\), and \(t>0\), is a reasonable strengthening/clarification of the problem’s “weak convergence” statement. It is good that this is recorded explicitly.

The identity
\[
\delta_0=-\frac12\frac{d}{dr}(-2H_+)
\]
has the correct sign, and the proposed Gibbs measure
\[
\pi(dv)=Z^{-1}e^{2\int_0^1{\bf 1}_{\{v(x)>0\}}\,dx}\gamma(dv)
\]
is the natural formal reversible measure for the gradient convention used here.

The Borelness and bounded-density equivalence \(\pi\sim\gamma\) are fine. The Brownian-bridge zero-occupation argument is also correct: for \(x\in(0,1)\), \(\beta(x)\) is a nondegenerate Gaussian, and the endpoints have zero Lebesgue measure.

No fatal issue in this paragraph.

### 2. “Consequences of the smooth approximations”

The convergence \(\pi_n\to\pi\) in total variation is essentially correct. Since \(0\le B_n\le1\), \(B_n(r)\to H_+(r)\) away from \(0\), and Brownian bridge paths spend zero Lebesgue time at zero, dominated convergence gives \(L^1(\gamma)\) convergence of the unnormalized densities, and hence total variation convergence after normalization.

However, the paragraph asserting that the regularized mild semigroup \(P_t^n\) is exactly the symmetric Dirichlet-form diffusion with invariant law \(\pi_n\) is an essential unproved input. For fixed \(n\), the Nemytskii map \(v\mapsto G_{1/n}(v)\) is bounded and globally Lipschitz as an \(L^2\)-valued map, so the statement is plausible and standard. But a complete proof should cite a precise theorem and verify its hypotheses: state space \(C_0([0,1])\), Dirichlet boundary condition, invariant Gaussian law, closability of the form, identification of the Dirichlet-form process with the mild SPDE, and reversibility. As written, “standard gradient-SPDE/Dirichlet-form theorem” is too vague for a rigorous standalone solution.

### 3. Proposition: invariance, symmetry, spectral gap

The passage of invariance from \(\pi_n\) to \(\pi\) is mostly correct under assumption (A) and total variation convergence. For bounded continuous \(f\),
\[
\int P_t^n f\,d\pi\to\int P_t f\,d\pi,
\]
and \(\int P_t^n f\,d\pi_n-\int P_t^n f\,d\pi\to0\) by total variation.

The same applies to symmetry for bounded continuous \(f,g\). The proof should explicitly note that equality against bounded continuous test functions implies equality of probability measures on the Polish space \(E=C_0([0,1])\), and that the Markov operator extends contractively to \(L^2(\pi)\) by Jensen plus invariance. These are standard but omitted.

The Poincaré/spectral-gap argument is basically sound. Brownian bridge measure has a Gaussian Poincaré inequality, and because \(d\pi_n/d\gamma\) is uniformly bounded above and below, the Poincaré constant transfers uniformly to \(\pi_n\). The exponential variance decay then follows for the reversible regularized semigroups.

The limit passage in the spectral-gap estimate is also plausible for bounded continuous \(f\), again using (A), uniform boundedness, and total variation convergence. Extending to all \(L^2(\pi)\) requires the previously mentioned contraction/density details.

The main caveat remains that the regularized reversibility theorem is assumed rather than proved/cited precisely.

### 4. Lemma 1: uniqueness under all-starting-point resolvent absolute continuity

This lemma is mathematically correct in substance. If
\[
R_\lambda^P(x,\cdot)\ll\pi\quad\text{for all }x,
\]
then any invariant \(\eta\) satisfies \(\eta\ll\pi\). Once \(\eta=h\pi\), symmetry and the \(L^2(\pi)\) spectral gap force \(h\equiv1\).

The proof is terse at the step extending
\[
\int P_t\varphi\,h\,d\pi=\int\varphi\,P_t h\,d\pi
\]
from bounded \(h\) to general \(h\in L^1(\pi)\). The truncation argument is standard, but in a final proof it should be written more carefully.

The truncation step \(h_a=h\wedge a\) is correct: \(P_t h=h\), Jensen/Markovianity gives \(P_t h_a\le h_a\), equality of integrals gives \(P_t h_a=h_a\), and the spectral gap implies \(h_a\) is constant. Varying \(a\) then gives \(h\equiv1\).

This lemma is conditional; its hypothesis (7) is not proved from the problem assumptions.

### 5. Strong Feller / resolvent Feller lemma

This lemma is correct. If \(\pi(A)=0\), invariance gives \(\int P_t1_A\,d\pi=0\). Strong Feller plus full support of \(\pi\) implies \(P_t1_A\equiv0\). Similarly for a Feller resolvent.

But neither strong Feller nor resolvent Feller is established. The document correctly lists this as a missing route rather than a completed proof.

### 6. Eventual equicontinuity criterion

The conditional criterion is sound. The \(L^2(\pi)\) spectral gap gives \(P_t f\to\pi(f)\) in \(L^2(\pi)\). Eventual equicontinuity and full support then upgrade this to pointwise convergence for each deterministic initial condition. Invariance of an arbitrary \(\eta\) and dominated convergence then imply \(\eta(f)=\pi(f)\) for all bounded Lipschitz \(f\), hence \(\eta=\pi\).

Again, the needed estimate (8) is not proved and is not a consequence of the stated assumptions. This is not a solution of the original problem.

### 7. “The Dirichlet-form exceptional set”

The discussion of the Bounebache–Zambotti exceptional-set issue is mathematically appropriate. Dirichlet-form constructions usually identify kernels and processes only outside properly exceptional sets, and \(L^2(\pi)\) information is insensitive to changing the process on \(\pi\)-null sets. Therefore BZ-type quasi-everywhere absolute continuity does not automatically imply all-starting-point absolute continuity for the ABLM mild semigroup.

This paragraph correctly diagnoses the central gap. It does not close it.

### 8. Entrance lemma

The entrance lemma is correct, assuming its hypotheses. The resolvent decomposition
\[
R_\lambda(x,A)=\int_0^\varepsilon e^{-\lambda t}P_t(x,A)\,dt
+e^{-\lambda\varepsilon}P_\varepsilon R_\lambda(\cdot,A)(x)
\]
gives the displayed bound, and \(P_\varepsilon(x,N)=0\) yields all-starting-point absolute continuity.

But (9), the entrance/non-hitting of the exceptional set, is not proved. This is another conditional reduction only.

### 9. Capacity/finite-energy lemma

This lemma has a serious technical problem as written.

The assumption (10) integrates quasi-continuous representatives against \(\eta\). But quasi-continuous representatives are only defined up to capacity-zero sets. If \(\eta\) may charge capacity-zero sets, then \(\int\varphi\,d\eta\) can depend on the chosen representative. Thus the assumption is not well-defined unless extra representative choices are fixed or unless one already knows \(\eta\) is smooth, which is precisely what the lemma tries to prove.

There is also a circular step in the proof. The equilibrium potential \(e_O\) satisfies \(e_O\ge1\) only quasi-everywhere on \(O\). The inequality
\[
\eta(O)\le\int e_O\,d\eta
\]
is unjustified before proving that \(\eta\) does not charge the exceptional subset of \(O\) where \(e_O<1\). This is exactly the desired conclusion, so the proof is circular unless strengthened assumptions are imposed.

Finally, after deriving \(\eta\ll\pi\), the proof says Lemma 1 gives uniqueness. Strictly speaking, Lemma 1 assumes all-starting-point resolvent absolute continuity (7), which has not been obtained in this capacity route. What is actually needed is only the second half of Lemma 1: “any invariant probability absolutely continuous with respect to \(\pi\) equals \(\pi\).” That should be stated as a separate lemma.

Thus the claim in the final paragraph that “both reductions are rigorous as stated” is too strong. The eventual-equicontinuity reduction is fine; the finite-energy/capacity reduction needs repair.

### 10. “Remaining open issues”

This section correctly admits that the proof is incomplete. It lists exactly the kind of missing ingredients needed to rule out invariant measures on \(\pi\)-null exceptional sets. Because none of these ingredients is proved from the stated assumptions, the document does not prove uniqueness.

This is fatal for answer readiness. The problem asks to prove or disprove uniqueness. The submitted document does neither: it proves uniqueness under additional hypotheses and leaves the decisive issue open.

---

## Required fixes before readiness

To become answer-ready, the solution would need one of the following:

1. A proof that the ABLM Dirichlet mild semigroup satisfies all-starting-point resolvent absolute continuity \(R_\lambda^P(x,\cdot)\ll\pi\).
2. A proof of strong Feller, resolvent Feller, asymptotic strong Feller, or the stated eventual equicontinuity estimate.
3. A rigorous proof that the process started from any deterministic \(x\) enters the BZ non-exceptional set immediately.
4. A corrected finite-energy/capacity argument proving every invariant probability is smooth for the BZ Dirichlet form, avoiding the quasi-continuous representative circularity.
5. Alternatively, a genuine counterexample producing two invariant probability measures.

Without one of these, the central exceptional-set gap remains unresolved.