# Author round 18

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: The remaining core problem is the complement form: for \(q\ge 2/3\), nonnegative weights \(\sum_i w_i=1\), and iid \(\eta_i\sim\mathrm{Bernoulli}(q)\), prove
\[
\Pr\!\left[\sum_i w_i\eta_i>q\right]\le q.
\]
Equivalently, for \(p=1-q\le1/3\), prove the original lower bound.

I tried:
1. The \(q=2/3\) 3-wise-intersecting coupling, which works at exactly \(2/3\).
2. For \(q>2/3\), a three-set coupling with common-intersection parameter \(\alpha=3q-2\), giving only
\[
3\Phi_q(w)-2\le \Pr_\alpha\{w(A)>\alpha\},
\]
which does not close near \(q=2/3\).
3. A moment/polynomial majorant in centered form \(X=\sum_i w_i(\eta_i-q)\in[-q,p]\), using
\[
P(X)=X(X-p)(X+q),\qquad \mathbb E P(X)=pq(q-p)\sum_i(w_i^2-w_i^3)\ge0,
\]
but continuity near \(0^+\) obstructs a fixed polynomial majorant of \(1_{\{X>0\}}\).
4. Largest-weight induction, which reduces to the pivot/two-tail inequality already recorded.

Please suggest a rigorous route to prove the complement inequality. I am especially interested in whether one can make a threshold-flow/derivative argument from the \(q=2/3\) case, a largest-weight induction with a sharp residual lower-tail lemma, or a finite-dimensional moment/transport argument work.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and ran `pdflatex` twice successfully. The compiled `answer.pdf` remains **12 pages**, within the contract. I polished the shifted-compression reduction per the Critic’s minor rigor suggestions and added new research-note material on the complement mean-tail formulation, the \(q=2/3\) coupling obstruction, polynomial-majorant attempts, and the transport-dual slice target.

I am **not** declaring readiness, because the main small-\(p\) assertion is still not proved in `answer.tex`.
