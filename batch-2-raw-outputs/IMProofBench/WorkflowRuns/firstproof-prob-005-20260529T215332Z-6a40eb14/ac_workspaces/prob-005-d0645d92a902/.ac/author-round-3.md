# Author round 3

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: For the SPDE with drift \(\delta_0(u)\), suppose \(\eta\) is an arbitrary invariant law of the all-starting-points ABLM Dirichlet semigroup. Is there a viable way to prove that \(\eta\) charges no Bounebache--Zambotti exceptional set, preferably via a finite-energy/capacity estimate
\[
\left|\int \varphi\,d\eta\right|\le C_\eta \mathcal E_1(\varphi,\varphi)^{1/2}
\]
or a stationary Krylov estimate? Please give a concrete proof strategy with the exact intermediate lemmas needed, and indicate whether ABLM’s local-time/regularization estimates plausibly supply those lemmas. Avoid relying on full strong Feller unless you can explain how to prove it in this singular setting.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and compiled `answer.tex` successfully with `pdflatex` twice; it produces a 5-page PDF and respects the LaTeX contract.

Main changes:
- Weakened the Nemytskii drift wording from “smooth” to the needed bounded/Lipschitz statement.
- Made the semigroup convergence interpretation explicit.
- Added a rigorous “eventual equicontinuity/e-property” criterion that would upgrade the \(L^2(\pi)\) spectral gap to pointwise convergence from every deterministic initial condition.
- Added a finite-energy/capacity criterion showing that it suffices for invariant laws to charge no Bounebache–Zambotti exceptional sets.
- Toned down the BZ–ABLM identification language.
- Expanded `research_notes.tex` with the new reduction strategies and obstacles.

I am **not** declaring readiness, since the all-starting-points upgrade is still not proved from the stated hypotheses.
