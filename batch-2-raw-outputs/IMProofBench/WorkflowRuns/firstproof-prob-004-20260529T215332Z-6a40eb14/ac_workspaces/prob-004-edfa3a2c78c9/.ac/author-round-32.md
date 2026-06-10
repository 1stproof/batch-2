# Author round 32

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: The previous exact-plaque pointwise chain-map lemma appears too strong because low-\(G\)-energy null sheets can force any physical homotopy of all of \(Z_y\) to pay ordinary mass. The current sharp missing input is the averaged estimate
\[
 A_\Omega:=\int_\Omega\Fill_R(Z_y)\,dy
 \le C\left(R_1I+\frac{I^2}{S_1|Q|}\right)
 +\frac{C}{|Q|}\int_Q\int_\Omega
   \Mass(B_y\llcorner{\mathcal B}_z)\,dy\,dz.
\]
Here \(Z_y=\langle [R],(f_3,f_4),y\rangle\), \(E_y=\int_{Z_y}\|d(f_1,f_2)\|^2\), \(I=\int_QE_y\,dy\), \(\Omega=\{E_y\le4I/|Q|\}\), and \({\mathcal B}_z\) is the exact coordinate-plaque bad set.

Please focus on one of the following: either (1) give a rigorous proof strategy for this averaged estimate avoiding the false pointwise sweep, preferably via dual cochains/cellular acyclic carriers/essential filling; or (2) identify a genuine counterexample to this averaged estimate, especially in the hard regime \(R_1\ll S_1\), \(R_3R_4\ll S_3S_4\). I need actionable lemmas with enough detail to convert into a proof, not just high-level intuition.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and compiled `answer.tex` successfully with `pdflatex` twice. The PDF is 5 pages and the LaTeX contract remains satisfied.

Main changes:
- Demoted the unproved “Exact-plaque energy chain-map lemma”; it is no longer presented as an ordinary lemma.
- Recast the remaining gap as the averaged tightening estimate `(AT)`, which is exactly the restricted estimate needed to finish the theorem.
- Added a note explaining why the literal pointwise chain-map version is too strong: low-energy null sheets/flaps cannot be physically swept at cost depending only on \(E_y\).
- Updated `research_notes.tex` with the exact obstruction and several alternative formulations: dual cochain tightening, essential filling norm, and a weighted \(f_1\)-level-set route.
- Copied `references.bib` to the canonical path unchanged.
