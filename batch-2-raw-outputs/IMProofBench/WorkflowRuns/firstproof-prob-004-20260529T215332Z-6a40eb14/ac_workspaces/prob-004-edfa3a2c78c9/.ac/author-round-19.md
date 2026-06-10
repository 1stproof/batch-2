# Author round 19

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: In the current setup, consider the possible alternative route by slicing with \(u=f_1\). For regular \(t\), \(M_t=\langle [R,\partial R],u,t\rangle\) maps by \(g=(f_2,f_3,f_4)\) with degree one to the \(S_2\times S_3\times S_4\) rectangle and \(\Dil_2(g|_{M_t})\le1\). The \(2\)-dilation bound also gives a pointwise tangential estimate \(|dg(v)|\le |\nabla u|^{-1}|v|\) for \(v\in TM_t\). Is there a true weighted 3D lower bound of the form
\[
\int_{M_t} |\nabla u|^{-1}\,d\Mass \ \gtrsim\ S_2^{1/2}S_3^{3/2}S_4
\]
for a.e. central \(t\), or at least after averaging in \(t\), under the hard-regime hypotheses? If yes, please outline a rigorous proof; if no, identify the precise obstruction or a model counterexample compatible with a global \(2\)-contracting degree-one map.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and compile-checked `answer.tex` successfully with `pdflatex` twice; PDF remains 6 pages.

Main changes:
- Added the sharp unconditional partial bound
  \[
  \Vol(R)\gtrsim S_1S_2^{3/5}S_3^{7/5}S_4
  \]
  when the first alternative fails.
- Clarified that this misses the desired second alternative by \((S_3/S_2)^{1/10}\).
- Tightened the central calibration proof and explained the algebra behind the partial bound.
- Clarified that the remaining low-energy estimate must apply to the selected near-minimizing fillings.
- Updated `research_notes.tex` with the Round 19 exponent obstruction and the compute-worker’s local obstruction to pointwise Manhattan deformation.

I am **not** marking ready because the essential low-energy parametric tightening estimate remains open.
