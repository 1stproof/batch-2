# Author round 22

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: The remaining gap is the atomic penalized comparison `(13')` in `answer.tex`: for a low-energy central slice \(Z_y=\langle R,(f_3,f_4),y\rangle\), a penalized near-minimizing filling \(B_y\), and a puncture \(z\in Q\), construct a relative filling \(C_{y,z}\) of \(Z_y\) with
\[
\Mass C_{y,z}\le C\left(R_1E_y+\frac{E_y^2}{S_1}\right)
      +C\,\Mass(B_y\llcorner\mathcal B_z).
\]
Please focus on whether there is a rigorous chain-level construction of \(C_{y,z}\). In particular: can one implement a coordinate-plaque/Manhattan deformation without assuming a false pointwise track estimate, perhaps using the penalized minimality of \(B_y\)? Or is there a concrete obstruction showing that `(13')` must be modified? I need a proof skeleton detailed enough to turn into LaTeX, or a precise reason the statement is false.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and ran `pdflatex` twice successfully. The PDF remains 7 pages and within the LaTeX contract.

This round I sharpened the remaining gap: the draft now reformulates the missing averaged estimate as an atomic penalized fixed-puncture comparison `(13')`, and records why penalized near-minimizing fillings are compatible with the self-absorption step. I also updated `research_notes.tex` with the failed level-slice shortcut and the next rational-homotopy/directional-invariant probe.

The proof is still **not ready**: the atomic comparison `(13')` remains unproved, so I am not declaring readiness.
