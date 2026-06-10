# Author round 12

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: We still need to close the small-\(p\) direction. Current strongest reductions are:

1. HUG: for \(0<p\le1/3\), \(q=1-p\), \(0\le b_i\le h\), \(B=\sum b_i\),
\[
\Pr\!\left[\sum b_i\zeta_i\ge p(B+h)\right]\ge {p\over q}
\Pr\!\left[\sum b_i\zeta_i<p(B+h)-h\right].
\]
A shifted induction proves this only in the subcritical regime \(B\le qh/p\); the original pivot normalization is supercritical unless the pivot is already at least \(p\).

2. Rational cyclic expectation form: for \(p=r/b\le1/3\), assign arbitrary weights \(w_i\) summing to \(1\) independently uniformly to cyclic bins \(\mathbb Z/b\mathbb Z\). Let \(L_j\) be the load of the length-\(r\) cyclic interval \([j,j+r)\). The rational case is equivalent to
\[
\mathbb E\,\#\{j:L_j<r/b\}\le b-r.
\]
The corresponding deterministic pointwise interval count is false.

Please focus on producing a rigorous route to prove either the supercritical HUG inequality or the cyclic expectation inequality. In particular: can the Fokkink--Meester--Pelekis endpoint injection be adapted to prove the expected cyclic inequality despite pointwise failures? Or is there a Bellman/barrier function for supercritical HUG? Please give detailed lemmas or proof skeletons, not only high-level heuristics.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files.

Summary of changes:
- Added a rigorous **subcritical shifted HUG induction** proposition to `answer.tex`.
- Added an exact **rational cyclic expectation formulation** of the remaining small-\(p\) assertion.
- Recorded new round-12 working notes in `research_notes.tex`, including:
  - the shifted HUG induction,
  - cyclic expectation formulation,
  - failure of the deterministic fixed-size coloring criterion at \(p=3/10\),
  - a size-biased identity that may support a coupling/injection proof.
- Copied `references.bib` to the canonical path.
- Ran `pdflatex` successfully on `answer.tex`; the PDF is 10 pages, within the 12-page limit.

The main theorem is still not complete, so I am not marking ready.
