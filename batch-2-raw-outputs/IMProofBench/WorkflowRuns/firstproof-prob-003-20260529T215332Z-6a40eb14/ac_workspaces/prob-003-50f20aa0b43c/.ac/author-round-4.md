# Author round 4

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: Can you focus specifically on the pivot two-tail inequality recorded in the updated answer/research notes?

For \(0<p\le 1/3\), \(\lambda=p/(1-p)\), \(0\le a\le p\), and independent Bernoulli\((p)\) variables, prove or find a counterexample to
\[
\Pr\!\left[\sum_i u_i v_i\ge p\right]
\ge
\lambda\Pr\!\left[\sum_i u_i v_i<p-a\right],
\qquad \sum_i u_i=1-a,\quad u_i\ge0.
\]
This is equivalent to the missing small-\(p\) lemma. Please suggest concrete proof strategies, especially induction invariants or threshold-family arguments that handle the same residual variable at the two thresholds \(p-a\) and \(p\). Plain adaptive Bellman bounds and pairwise merge monotonicity seem to fail.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and ran `pdflatex` successfully twice; `answer.pdf` is 5 pages.

Main mathematical updates this round:
- Added the strict complement formulation \(q\ge 2/3:\Pr[\sum w_i\eta_i>q]\le q\).
- Added an equivalent “pivot two-tail” inequality, which seems like the most promising induction target.
- Added the pivot-plus-dust construction showing the lower bound \(p\) is sharp and that stronger finite cap-vector bounds are false globally.
- Updated `research_notes.tex` with the new equivalences, failed proof routes, and computational sanity checks.
- Did **not** mark ready, since the small-\(p\) lemma remains unproved.
