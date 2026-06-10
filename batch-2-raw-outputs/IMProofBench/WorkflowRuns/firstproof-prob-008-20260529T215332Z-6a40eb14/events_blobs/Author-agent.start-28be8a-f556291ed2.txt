## Referee report on the revised `answer.tex`

### Overall verdict

The revised draft resolves one major previous gap—the nested-to-full incidence criterion now has a plausible cocircuit-generation proof—but the proof is still **not rigorous as written**. The main new problem is that Proposition 0.2, “complete adjacent flags,” is **false as stated** and misapplies Wang’s theorem. Since Proposition 2.4 depends on it to prove that the polar of a valuated quotient is again a valuated quotient, the main construction is not established.

The document therefore is **not answer-ready**.

---

## LaTeX contract

I compiled `answer.tex` twice with `pdflatex`. It compiled successfully, produced a 5-page PDF, uses exactly `\documentclass[12pt]{article}`, uses only the permitted `fullpage` layout package, and contains no prohibited font-size or line-spacing changes. I found no LaTeX-contract violation.

---

## Literature validation

The BEZ citation is appropriate for the valuated quotient / tropical linear-space inclusion dictionary: BEZ identify valuated matroid quotients with incidence-Plücker relations and with inclusion of the corresponding projective tropical linear spaces. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S000187082100133X?utm_source=openai))

The Wang citation is real and current: arXiv lists `2412.12059` as v2, last revised March 7, 2026. ([arxiv.org](https://arxiv.org/abs/2412.12059)) Wang’s Theorem 4.3 indeed states that \(\operatorname{Dr}^1(\mu)\) is cut out by “three-term incidence relations.” ([arxiv.org](https://arxiv.org/pdf/2412.12059)) However, Wang’s terminology includes several classes of relations: degenerate hyperplane relations \(\theta(A)=\infty\), parallel hyperplane relations, and concurrent three-term minimum relations. These are explicitly listed before Theorem 4.3. ([arxiv.org](https://arxiv.org/pdf/2412.12059)) This distinction is crucial and is mishandled in `answer.tex`.

The cocircuit-generation input used in Criterion 0.1 is also a standard fact: tropical linear spaces are tropical spans of valuated cocircuits, equivalently intersections of circuit hyperplanes. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12031988/?utm_source=openai))

---

## Previous concerns: what was fixed and what remains

### 1. Nested-to-full incidence criterion

This concern is mostly addressed. The new proof of Criterion 0.1 is substantially better than the previous attempted Murota–Shioura shortcut.

The argument is:

1. Fix \(J\) and set \(c_j=q(J\setminus j)\).
2. If some \(c_j\) is finite, then \(J\) contains a \(q\)-basis, hence spans the support matroid of \(p\).
3. The nested incidence relations with upper set \(J\) say \(c\) is orthogonal to the cocircuits of \(p|J\).
4. Since the tropical hyperplane orthogonal to \(c\) is tropically convex and contains the cocircuits, it contains the tropical linear space of \(p|J\).
5. The restricted cocircuit \(C_p^*(I)|_J\) is a vector of \(p|J\) by the Plücker relations of \(p\).

This is plausible. I would still ask the author to cite the precise cocircuit-span theorem and mention closure of the tropical span if needed, but I do not see a fatal flaw in this criterion.

### 2. Complete-flag local criterion

This remains unresolved in the written proof, despite the new Wang citation. The problem is no longer an omitted reference; it is a **false proposition**.

`answer.tex` states:

> Suppose that for each \(1\le j<r\), each \(S\), and distinct \(x,y,z\), the displayed three-term minimum relation holds. Then every \(w_j\) is a valuated matroid and \(w_0\preceq\cdots\preceq w_r\).

This is not true. Wang’s theorem does not say that only the displayed concurrent minimum relations suffice in complete generality. Wang’s “three-term incidence relations” include degenerate hyperplane constraints and parallel hyperplane constraints, not just the displayed minimum over three terms.

#### Explicit counterexample to Proposition 0.2

Let
\[
E=\{\ell_1,\ell_2,\ell_3,a,b,c,d\}.
\]
Let \(w_4\) be the trivial rank-4 valuated matroid whose only finite basis is \(\{a,b,c,d\}\), so \(\ell_1,\ell_2,\ell_3\) are loops. Define:

- \(w_0(\varnothing)=0\);
- \(w_1\) finite exactly on \(\{a\},\{b\},\{c\},\{d\}\);
- \(w_2\) finite exactly on two-subsets of \(\{a,b,c,d\}\);
- \(w_3\) finite exactly on three-subsets of \(\{a,b,c,d\}\), **and also** on \(\{\ell_1,\ell_2,\ell_3\}\).

All finite values are \(0\), all other values are \(\infty\).

A direct finite check shows that all displayed adjacent three-term minimum relations in Proposition 0.2 hold. The nonloop part is just the ordinary uniform flag, and any term involving the extra finite coordinate \(w_3(\ell_1\ell_2\ell_3)\) is paired with an \(\infty\)-term from \(w_2\) or \(w_4\), so it never creates a unique finite minimum.

But \(w_3\) is not a valuated matroid: its finite support is not the set of bases of a matroid. Basis exchange fails between
\[
\{\ell_1,\ell_2,\ell_3\}
\quad\text{and}\quad
\{a,b,c\}.
\]
For example, removing \(\ell_1\) from the first basis and adding any of \(a,b,c\) does not produce a finite \(w_3\)-basis.

Thus Proposition 0.2 is false as stated.

This is a fatal issue because Proposition 2.4 invokes Proposition 0.2 to conclude that the reversed polar sequence is a complete valuated flag.

A repair may be possible: the author could restate the flag criterion with the full Wang relations, including degenerate and parallel relations, or add precise ordinary-support hypotheses and prove that the polar sequence satisfies all Wang relations. But this is not done in the current `answer.tex`.

---

## Section-by-section audit

### Section 0: Conventions and two local facts

The conventions are now clearer and the BEZ quotient/inclusion dictionary is appropriately cited.

Criterion 0.1 is a serious improvement over the previous version. I would accept it after minor polishing and exact theorem citation.

Proposition 0.2 is the main problem. As explained above, it is false as stated. The proof says Wang’s theorem “says exactly” that the displayed three-term relations cut out rank-\(j\) elementary quotients. This is not accurate: Wang’s theorem uses a broader package of three-term incidence relations, including degenerate and parallel hyperplane relations. The displayed relation in `answer.tex` is only the concurrent-minimum relation.

The Higgs completion formula is still cited rather tersely, but this is probably acceptable if the cited Murota/Dress–Terhalle results really have the stated form. The endpoint check for \(h_r\simeq\mu_M\) is reasonable.

### Section 1: Flat-lattice duality and flat constancy

Lemma 1.1 is correct: a rank-reversing anti-automorphism of a semimodular flat lattice forces modularity.

Lemma 1.2 is also sound. The common-complement argument and incidence relation with \(\mu_M\) correctly prove flat constancy of \(\nu\).

### Section 2: The polar transform

The definition of \(\nu^{\perp_M}\) is well-defined using flat constancy.

Lemma 2.1 is improved and essentially plausible. One minor detail remains compressed: extending submodularity from flats to all subsets via \(M\)-closure should be spelled out, since
\[
\operatorname{cl}(A\cap B)\subseteq \operatorname{cl}(A)\cap\operatorname{cl}(B)
\]
is used together with monotonicity. This is fixable and not the main gap.

Lemma 2.2, the elementary opposition lemma, is plausible. The case analysis is terse but mostly convincing.

Proposition 2.4 is not proved because it depends on the false Proposition 0.2. Even if the actual polar sequence has the right support properties, the proof must explicitly invoke a correct version of Wang’s theorem and verify all its hypotheses.

### Section 3: Order reversal

The equal-rank, \(a=0\), and \(b=r\) edge cases have been restored and are mostly satisfactory.

The nested-incidence duality argument is strong and appears essentially correct. The Boolean-frame case and the nullity-one circuit case are plausible.

However, Theorem 3.1 depends on Proposition 2.4 to know that the polar objects are valuated matroids, so the theorem is not rigorously established until the Proposition 0.2 issue is fixed.

### Section 4: Agreement with flats

This section is essentially correct. The modularity argument
\[
Y^\perp\vee F=\hat1
\iff
Y^\perp\wedge F=\hat0
\iff
Y\vee F^\perp=\hat1
\]
is valid, and it identifies the image of the embedded flat \(F\) with \(F^\perp\). This part is conditional only on the polar transform being well-defined on all of \(\Dr(M)\).

---

## Summary of remaining required fixes

To make the proof answer-ready, the author must repair Proposition 0.2. Acceptable routes include:

1. State Wang’s theorem accurately, including degenerate and parallel hyperplane relations, and prove that the polar sequence in Proposition 2.4 satisfies all of those relations; or

2. Add sufficient support hypotheses to Proposition 0.2 and prove that, under those hypotheses, the displayed relations plus support conditions imply the full Wang conditions; or

3. Bypass Proposition 0.2 entirely by directly proving that each \(\nu^{\perp_M}\) satisfies the Plücker relations and is a quotient of \(\mu_M\).

Until this is done, the construction of \(\Phi\) is not rigorously established.