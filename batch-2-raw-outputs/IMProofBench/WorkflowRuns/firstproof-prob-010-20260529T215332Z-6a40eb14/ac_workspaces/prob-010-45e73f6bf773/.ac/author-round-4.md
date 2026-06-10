# Author round 4

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: Please scrutinize the new Lemma “intersection of graph-product boundary corners” in `answer.tex`. The key claimed inclusion is
\[
q_W(q_U\mathcal A_Mq_U)q_W\subset q_{U\cap W}\mathcal A_Mq_{U\cap W}.
\]
The proof uses DKEP’s coefficient formula for Jones correspondences and CDHJKN’s fusion rules, via the triple fusion
\[
(L^2M\otimes_{M_W}L^2M)\otimes_M(L^2M\otimes_{M_U}L^2M)\otimes_M(L^2M\otimes_{M_W}L^2M).
\]
Is this inclusion rigorously justified as written? If not, what precise additional lemma or modified argument would make the finite-boundary upgrade valid without assuming the support projections commute?
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files. The revised proof replaces the invalid meet/support argument with a palindromic-product criterion for non-normal states, adds a more explicit Bass–Serre commutator computation, and uses a graph-product boundary-corner intersection lemma in place of the previous unsupported fusion-meet identity. I ran `pdflatex` twice successfully; `answer.pdf` is 4 pages.
