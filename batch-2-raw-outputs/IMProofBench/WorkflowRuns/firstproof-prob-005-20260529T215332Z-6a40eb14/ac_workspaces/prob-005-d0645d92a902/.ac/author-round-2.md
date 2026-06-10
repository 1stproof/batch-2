# Author round 2

Files changed: ['answer.tex', 'references.bib', 'research_notes.tex']
Ready: False
Council question: Can one prove uniqueness of invariant measures for this Dirichlet skew stochastic heat equation without proving pointwise transition/resolvent absolute continuity? In particular, is there a rigorous route showing that any invariant law η of the actual all-starting-points ABLM semigroup must be absolutely continuous with respect to the Gibbs/Brownian-bridge measure π, perhaps via a stationary Fokker--Planck argument, finite-dimensional projections with uniform entropy/Fisher estimates, Markov uniqueness, asymptotic coupling, or Feller plus L^2 spectral gap plus irreducibility? Please focus on a route that could close the exceptional-set gap and state the specific lemmas/estimates needed.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and compile-checked `answer.tex` successfully with `pdflatex` twice; it now produces a 5-page PDF.

Main changes:
- Made the regularized reversibility argument more rigorous via the closed gradient Dirichlet form.
- Corrected the resolvent absolute-continuity notation.
- Added a precise strong-Feller/resolvent-Feller lemma showing how to upgrade invariance + full support to pointwise AC.
- Added an entrance lemma showing exactly how to remove the Bounebache–Zambotti exceptional-set obstruction.
- Updated `research_notes.tex` with the strong-Feller, entrance, OU-comparison, uniform-density, Girsanov-obstruction, and Dirichlet-form-comparison strategies.
- Updated `references.bib` with standard Dirichlet-form/ergodicity/strong-Feller references.

I have **not** marked the solution ready: the all-starting-points pointwise AC/entrance theorem remains the essential missing input.
