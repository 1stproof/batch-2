# Author round 9

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: The remaining core problem is the unit-gap/two-tail inequality equivalent to the small-\(p\) lemma: for \(0<p\le 1/3\), \(q=1-p\), \(0\le b_i\le1\), \(B=\sum b_i\), and \(\zeta_i\sim\mathrm{Bernoulli}(p)\), prove
\[
\Pr\!\left[\sum_i b_i(\zeta_i-p)\ge p\right]
\ge {p\over q}\Pr\!\left[\sum_i b_i(\zeta_i-p)<-q\right].
\]
This resembles a martingale/ballot inequality for jumps \(+qb_i\) with probability \(p\) and \(-pb_i\) with probability \(q\), with all jump ranges at most \(1\). A naive shifted induction
\[
\Pr[S\ge x+p]\ge(p/q)\Pr[S<x-q]
\]
closes under conditioning but its base case fails for shifts \(x>q\); a restricted domain closes only when the remaining total \(B\le q/p\), not in the hard dust regime. Can you suggest a rigorous proof route for this two-tail inequality, or a precise known theorem (Kellerer/Kanter/Pinelis/ballot/size-bias/etc.) that implies it? If you think the inequality is false, give a concrete counterexample; otherwise prioritize proof strategies that could fit in a short LaTeX solution.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files. Main changes:

- Removed the false pairwise coalescence assertion as a proposed route.
- Added the explicit \(p=0.3,\ w_i=1/4\) counterexample and the infinite equal-weight family showing all pair coalescences can decrease \(\Phi_q\).
- Tightened the “Remaining open issues” section to reflect that the small-\(p\) lemma is still the essential unresolved gap.
- Added persistent research notes on the failed pair-coalescence route, the FMP hypotenuse formulation, the Bellman/unit-gap induction obstruction, and the influence-flow diagnostic.
- Copied `references.bib` to the canonical path.
- Ran `pdflatex` twice successfully; `answer.pdf` is 8 pages, with no LaTeX warnings.
