## Referee report on revised `answer.tex`

### Overall verdict

The revision improves the exposition and fixes one of the previously identified circular arguments, but it is **still not answer-ready**. The document explicitly concludes that it “does not yet prove or disprove the original all-starting-points statement,” and the stated problem asks for a proof or disproof of uniqueness of invariant measures. Conditional criteria are not enough.

The main unresolved gap remains exactly the decisive one: the proof does not show that an arbitrary invariant probability measure is absolutely continuous with respect to the Gibbs measure \(\pi\), nor does it rule out invariant measures supported on a \(\pi\)-null exceptional set.

---

## LaTeX contract check

I compiled the revised `answer.tex` twice with `pdflatex`. It compiled successfully and produced a 5-page PDF. It uses exactly

```latex
\documentclass[12pt]{article}
```

and only the permitted `fullpage` layout package. I found no forbidden line-spacing, font-size, or margin/layout changes. Thus the LaTeX contract is satisfied. The failure is mathematical, not formatting-related.

---

## Literature validation

The ABLM 2024 citation is bibliographically correct: the paper appears in *Communications on Pure and Applied Mathematics* 77(5), pages 2708–2777, and concerns stochastic heat equations with distributional drift, including measure-valued drifts such as \(\delta_0\). ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/))

The 2025 Athreya–Butkovsky–Lê–Mytnik weak/mild equivalence paper exists, but its stated bounded-domain settings are periodic and Neumann, not Dirichlet. Thus it cannot by itself justify a Dirichlet ABLM–BZ identification unless an additional Dirichlet extension is proved or assumed. ([link.springer.com](https://link.springer.com/article/10.1007/s40072-025-00392-x))

The Bounebache–Zambotti paper indeed constructs a Gibbs-type invariant measure and associated Dirichlet form for a skew stochastic heat equation with local-time drift. Its Proposition 2.5 gives a resolvent-kernel absolute-continuity statement, but the proof proceeds through a capacity-zero exceptional set and represents the \(L^2\)-resolvent only almost everywhere before extending the kernel on the exceptional set. This supports the author’s diagnosis that quasi-everywhere absolute continuity is not automatically an all-starting-points statement. ([arxiv.org](https://arxiv.org/pdf/1105.2779))

---

## Status of previous concerns

### Addressed or improved

1. **The circular finite-energy/capacity argument was removed.**  
   The previous draft used quasi-continuous representatives before proving that invariant measures do not charge exceptional sets. The revised draft replaces this with a capacity–Krylov criterion. That new criterion is non-circular as a conditional lemma.

2. **The “absolutely continuous invariant laws are unique” step is now separated.**  
   Lemma `\ref{lem:ac}` correctly isolates the spectral-gap argument showing that if \(\eta\ll\pi\), then \(\eta=\pi\). This resolves the previous logical dependency issue where Lemma 1 was being reused with stronger hypotheses than needed.

3. **The \(L^2(\pi)\)-extension details are somewhat clearer.**  
   The revised proof now explicitly mentions Jensen contraction, density of \(C_b(E)\), and extension to a symmetric Markov contraction.

### Still unresolved

1. **No all-starting-points absolute continuity is proved.**  
   The proof still does not establish
   \[
   R_\lambda^P(x,\cdot)\ll\pi\qquad\text{for all }x\in E.
   \]

2. **No strong Feller, resolvent Feller, eventual equicontinuity, entrance, or capacity–Krylov estimate is proved.**  
   These are only listed as sufficient criteria.

3. **The BZ exceptional set is still not excluded for arbitrary invariant measures.**  
   The document proves uniqueness only among invariant laws already known to be absolutely continuous with respect to \(\pi\), or under additional estimates.

4. **The regularized Dirichlet-form identification is still cited vaguely.**  
   The phrase “usual Galerkin/Dirichlet-form identification” is plausible for fixed smooth \(n\), but a fully rigorous proof should cite a precise theorem and verify its assumptions.

---

## Detailed mathematical audit

### 1. Problem statement and interpretation

The adopted interpretation (A),
\[
P_t^n\Phi(x)\to P_t\Phi(x)
\]
for bounded continuous \(\Phi\), deterministic \(x\), and \(t>0\), is clearly stated. This is good and addresses possible ambiguity in the problem’s phrase “weakly.”

The formal gradient identity
\[
\delta_0=-\frac12\frac{d}{dr}(-2H_+)
\]
has the correct sign. The proposed Gibbs measure
\[
\pi(dv)=Z^{-1}e^{2\int_0^1{\bf1}_{\{v(x)>0\}}\,dx}\gamma(dv)
\]
is the natural reversible candidate.

The argument that \(\pi\sim\gamma\), and that Brownian bridge paths spend zero Lebesgue time at zero, is correct.

No serious issue here.

---

### 2. Total variation convergence of \(\pi_n\)

The proof of
\[
\|\pi_n-\pi\|_{\mathrm{TV}}\to0
\]
is correct in substance. Since \(0\le B_n\le1\), \(B_n(r)\to H_+(r)\) away from zero, and Brownian bridge paths have zero occupation time at zero, dominated convergence gives convergence of the Gibbs densities in \(L^1(\gamma)\).

This part is sound.

---

### 3. Regularized reversible semigroups

The statement that, for fixed \(n\), the regularized SPDE has invariant reversible law
\[
\pi_n(dv)\propto \exp\left(2\int_0^1B_n(v(x))\,dx\right)\gamma(dv)
\]
is formally correct.

However, the proof still relies on an unstated “usual Galerkin/Dirichlet-form identification.” For a complete proof, one should verify or cite a theorem covering:

- the Dirichlet boundary setting;
- the state space \(E=C_0([0,1])\), not merely \(L^2(0,1)\);
- the closure of the cylinder form;
- identification of the Dirichlet-form process with the mild SPDE;
- invariance and reversibility of \(\pi_n\).

For fixed \(n\), this is standard and likely repairable, but it is still a gap in a standalone proof.

---

### 4. Proposition `\ref{prop:limit}`

The passage of invariance and symmetry from \((P_t^n,\pi_n)\) to \((P_t,\pi)\) is mostly correct under assumption (A) and total variation convergence.

The spectral-gap argument is also essentially correct:

- Brownian bridge measure satisfies a Gaussian Poincaré inequality.
- Uniform upper/lower bounds on \(d\pi_n/d\gamma\) transfer the Poincaré inequality uniformly to \(\pi_n\).
- Reversibility gives exponential \(L^2\)-variance decay.
- Assumption (A) and total variation convergence allow passage to the limit for bounded continuous \(f\).
- Density of \(C_b(E)\) in \(L^2(\pi)\) extends the result.

This proposition is acceptable modulo the earlier unproved regularized Dirichlet-form identification.

---

### 5. Lemma `\ref{lem:ac}`

This lemma is correct: if \(\eta=h\pi\) is invariant, symmetry gives \(P_t h=h\) in \(L^1(\pi)\). Then the truncations \(h_a=h\wedge a\) satisfy \(P_t h_a=h_a\), and the spectral gap forces each \(h_a\) to be constant. Letting \(a\to\infty\) gives \(h\equiv1\).

This successfully addresses one previous concern.

---

### 6. Resolvent and Feller criteria

Lemma `\ref{lem:resolvent}` is correct: if every resolvent kernel is absolutely continuous with respect to \(\pi\), then every invariant \(\eta\) is absolutely continuous with respect to \(\pi\), and Lemma `\ref{lem:ac}` applies.

Lemma `\ref{lem:sf}` is also correct: strong Feller or resolvent Feller plus full support of \(\pi\) upgrades \(\pi\)-a.e. null-set avoidance to all starting points.

But neither hypothesis is proved. These are conditional criteria only.

---

### 7. Eventual equicontinuity criterion

The eventual equicontinuity criterion is mathematically sound. The \(L^2(\pi)\) spectral gap plus full support of \(\pi\) does upgrade to pointwise convergence if the uniform-in-large-time local equicontinuity estimate (8) holds.

However, estimate (8) is not proved and is not a stated assumption of the problem.

---

### 8. Bounebache–Zambotti exceptional set

The discussion is accurate in spirit. BZ-type Dirichlet-form constructions yield quasi-everywhere statements, and changing a Markov process on a \(\pi\)-null exceptional set is invisible to \(L^2(\pi)\) arguments.

A technical issue remains: BZ work naturally on \(H=L^2(0,1)\), while the problem’s Markov semigroup lives on \(E=C_0([0,1])\). Since the Gibbs measure is supported on continuous paths, this can likely be reconciled, but the draft does not spell out how the exceptional set and capacity are transferred to \(E\).

This is not the central fatal issue, but it would matter in a complete proof.

---

### 9. Entrance lemma

Lemma `\ref{lem:entrance}` is correct. If the process enters \(N^c\) immediately from every deterministic point, then quasi-everywhere resolvent absolute continuity becomes all-starting-points resolvent absolute continuity.

But condition (9),
\[
P_s(x,N)=0\qquad x\in E,\ s>0,
\]
is not proved.

---

### 10. Capacity–Krylov lemma

The new Lemma `\ref{lem:krylov}` is a genuine improvement over the previous finite-energy/capacity argument. The proof is no longer circular: it uses a Krylov-type estimate on open neighborhoods of capacity-zero sets and tightness of an arbitrary invariant measure to conclude that invariant measures do not charge exceptional sets.

The argument is valid as a conditional lemma, subject to clarifying that \(\capacity\) means the BZ capacity associated with the limiting Dirichlet form.

But the estimate
\[
 \sup_{x\in K}\mathbb E_x\int_\varepsilon^T{\bf1}_O(u_s)\,ds
      \le C\,\operatorname{Cap}(O)^\alpha
\]
is a major additional assumption. It is not proved and does not follow from the hypotheses of the problem.

Thus this section supplies another possible route to uniqueness, not a proof of uniqueness.

---

## Fatal issue

The revised `answer.tex` ends with a “Remaining open issues” section that explicitly says the proof does not prove or disprove the original all-starting-points statement. Under the grading instructions, that alone forces

\[
\texttt{<answer\_ready>false</answer\_ready>}.
\]

Mathematically, the fatal missing step is still:

\[
\text{Every invariant probability measure } \eta \text{ must satisfy } \eta\ll\pi.
\]

The draft proves this only under additional assumptions such as resolvent absolute continuity, strong Feller regularity, eventual equicontinuity, entrance into the non-exceptional set, or a capacity–Krylov estimate. None of these is established from the stated problem hypotheses.

---

## Required work for readiness

To become answer-ready, the author must either:

1. prove one of the all-starting-points upgrades (7), (8), (9), or (10);
2. prove directly that every invariant law is absolutely continuous with respect to \(\pi\);
3. prove a different uniqueness theorem that avoids exceptional-set issues; or
4. construct a genuine counterexample/disproof.

As written, the revised document is a useful conditional analysis, but not a solution to the problem.