# Author round 1

Files changed: ['answer.tex', 'references.bib', 'research_notes.tex']
Ready: False
Council question: We need close the last gap in the uniqueness proof for the Dirichlet SPDE
\[
\partial_t u=\tfrac12\partial_{xx}u+\delta_0(u)+\dot W
\]
under the ABLM regularized/mild solution notion. I have proved via smooth approximations that the candidate Gibbs measure
\[
\pi(dv)\propto \exp(2\int_0^1{\bf1}_{v(x)>0}\,dx)\,\gamma(dv)
\]
is invariant, symmetrizing, and gives an \(L^2(\pi)\) spectral gap for the actual semigroup \(P_t\). The abstract uniqueness argument would be complete if
\[
R_\lambda^P(x,\cdot)\ll\pi\quad\text{for every deterministic }x\in C_0([0,1]).
\]
Bounebache--Zambotti give absolute continuity for their Dirichlet-form resolvent and transition laws outside an exceptional set, but the Critic correctly objected that this has not been transferred to the ABLM semigroup for every initial condition.

Please suggest rigorous routes to prove the pointwise resolvent/transition absolute continuity for the actual ABLM semigroup, or an alternative route to uniqueness of invariant measures avoiding this pointwise AC. In particular, assess:
1. whether ABLM approximation/stability can imply a strict all-starting-points version of the BZ process;
2. whether one can prove entrance from BZ exceptional sets using additive white noise;
3. whether uniform capacity or heat-kernel estimates for the regularized gradient SPDEs could pass to the limit;
4. whether any stationary ABLM solution must avoid all zero-capacity sets, which would suffice for uniqueness.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

I updated the canonical files and compiled `answer.tex` successfully. The revised draft now proves, directly from the smooth approximations, that the candidate Gibbs measure is invariant, that the actual ABLM semigroup is symmetric on \(L^2(\pi)\), and that it inherits a spectral gap. I also made the remaining gap precise: the only missing ingredient for full uniqueness is pointwise resolvent absolute continuity for the actual semigroup \(P_t\), not just the Dirichlet-form version.
