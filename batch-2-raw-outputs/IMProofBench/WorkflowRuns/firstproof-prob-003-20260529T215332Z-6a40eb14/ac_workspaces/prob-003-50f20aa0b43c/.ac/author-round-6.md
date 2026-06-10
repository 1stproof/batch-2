# Author round 6

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: We need to prove the small-p lemma:

For \(0\le p\le1/3\), all nonnegative weights \(w_i\) summing to \(1\), and iid \(v_i\sim\mathrm{Bernoulli}(p)\),
\[
\Pr\!\left[\sum_i w_i v_i\ge p\right]\ge p.
\]

Equivalent normalized form: with \(L=1/p\ge3\), \(a_i=w_i/p\), \(\sum a_i=L\), and \(\xi_i\sim\mathrm{Bernoulli}(1/L)\), prove
\[
\Pr\!\left[\sum_i a_i\xi_i\ge1\right]\ge 1/L.
\]
If any \(a_i\ge1\), this is immediate; hard case \(0\le a_i<1\). By multiplicative closure it suffices to prove \(p\in[1/6,1/3]\), i.e. \(L\in[3,6]\).

Complement form: with \(q=1-p\ge2/3\), prove
\[
\Pr\!\left[\sum_i w_i\eta_i>q\right]\le q,\qquad \eta_i\sim\mathrm{Bernoulli}(q).
\]
This is a weighted-threshold hypotenuse problem. For the bad down-set
\[
\mathcal D=\{A:\sum_{i\in A}w_i<p\},
\]
we know \(\mu_p(\mathcal D)\le1-p\) is desired; also for \(r=\lfloor1/p\rfloor\), no \(r\) members of \(\mathcal D\) cover \([m]\), so the complement threshold family is \(r\)-wise intersecting, but ordinary \(r\)-wise intersection alone is insufficient.

Please suggest a rigorous proof strategy. Especially valuable would be:
1. a self-contained proof for \(L\in[3,6]\);
2. a theorem from extremal set theory / biased measure of weighted threshold families that implies it;
3. a way to adapt Fokkink–Meester–Pelekis cyclic/injection arguments from special rational points to all \(q=t\ge2/3\);
4. or a sharp induction/pivot inequality proof:
\[
\Pr[Y\ge p]\ge \frac{p}{1-p}\Pr[Y<p-a].
\]
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and compile-checked `answer.tex` successfully with `pdflatex` twice. The draft remains intentionally **not ready** because the small-\(p\) lemma is still unproved.

Main changes:
- Fixed the Critic’s minor issues in the pair lemma, pivot-plus-dust sharpness, and convex separation argument.
- Added a weighted-threshold / \(r\)-wise-intersecting reformulation of the remaining gap.
- Recorded new research notes on the normalized \(L=1/p\) form, complement formulation, FMP hypotenuse connection, cyclic-rational representation, Pinelis left-tail attempt, and related MathOverflow bounds.
- The PDF is now 6 pages, within the contract.

I also checked the literature angle further: the complement form aligns with the “hypotenuse” weighted Bernoulli tail problem discussed by Fokkink–Meester–Pelekis; their published results cover neighboring regions and special points but do not appear to close the whole \(q=t\ge2/3\) line needed here. ([alea.impa.br](https://alea.impa.br/articles/v20/20-07.pdf))
