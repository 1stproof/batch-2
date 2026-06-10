# Author round 4

Files changed: ['answer.tex', 'references.bib', 'research_notes.tex']
Ready: False
Council question: For the Dirichlet skew stochastic heat equation with drift \(\delta_0(u)\), can one prove all-starting fixed-time or resolvent absolute continuity \(P_t(x,\cdot)\ll\pi\) or \(R_\lambda(x,\cdot)\ll\pi\) by a “late-noise splitting” argument?

More concretely, for \(t>\varepsilon>0\),
\[
u_t=S_\varepsilon u_{t-\varepsilon}+Z_\varepsilon
+\int_{t-\varepsilon}^t S_{t-s}\delta_0(u_s)\,ds,
\]
where \(Z_\varepsilon\) has covariance equivalent to Brownian bridge measure. The drift convolution should be smoother in high modes than \(Z_\varepsilon\), but it depends on the same recent noise. A mere random Cameron–Martin shift is not enough, since dependent shifts can collapse Gaussian measure onto a null hyperplane. Is there a rigorous adaptedness/Malliavin/triangular-map argument here, or a known theorem for fixed-time absolute continuity of SPDEs with distributional drift that could apply? Please suggest a concrete proof architecture or explain the sharp obstruction.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Revised the canonical files. Main changes:

- `answer.tex`: repaired the criticized capacity section by replacing the circular finite-energy argument with a clean capacity–Krylov criterion; separated the “absolutely continuous invariant laws are unique” lemma from all-starting-point resolvent assumptions; clarified that the current result is still conditional on an all-starting upgrade.
- `research_notes.tex`: added the corrected capacity route, cautions about quasi-continuous representatives, fixed-time absolute-continuity obstacles, and stationary Fokker–Planck limitations.
- `references.bib`: added relevant regularity/ergodicity/fixed-time absolute-continuity references.
- Ran `pdflatex` twice on `answer.tex`; it compiles successfully to a 5-page PDF.
