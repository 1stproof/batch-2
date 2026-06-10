# Author round 36

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: We are stuck on the following hard-regime estimate for the 4D rectangle 2-dilation problem. Let \(F=(f_3,f_4)\), \(G=(f_1,f_2)\), central \(Q\subset[0,S_3]\times[0,S_4]\), \(Z_y=\langle [[R]],F,y\rangle\), \(E_y=\int_{Z_y}\|dG|_{TZ_y}\|_{HS}^2\,d\|Z_y\|\), \(I=\int_QE_y\,dy\), and \(q=|Q|\). Define the relaxed essential filling
\[
\EFill_f(y)=\inf\{\Mass C:\ C\in N_3(R,\partial R;\mathbb R),\ f_\#(\partial C)=\pm P_y\}.
\]
For \(z\in Q\), \({\mathcal B}_z\) is the set of points \(x\in R\) such that \(z\) lies in the \(F\)-image of at least one coordinate 2-plaque through \(x\). The reduction would be complete if one could prove, at least in the hard regime \(R_1\ll S_1\), \(R_3R_4\ll S_3S_4\),
\[
 \int_\Omega \EFill_f(y)\,dy
 \le C\left(R_1I+\frac{I^2}{S_1q}\right)
 +\frac{C}{q}\int_Q\int_\Omega
       \Mass(C_y^0\llcorner{\mathcal B}_z)\,dy\,dz,
\]
where \(\Omega=\{E_y\le 4I/q\}\) and \(C_y^0\) are near-minimizers for \(\EFill_f\).

Please suggest a portfolio of rigorous approaches to prove this estimate or replace it with an alternative hard-regime argument. In particular, address the obstruction that source-local bad-set restriction is not compatible with quotienting by \(f\)-null chains, and that ordinary cubical deformation creates seam terms or thickened bad sets whose Fubini estimate fails.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and ran `pdflatex` twice successfully. The draft remains a conditional reduction rather than a complete proof: I added a scalar stress-model note showing why the currently proved monomial/slicing estimates cannot remove the missing averaged tightening estimate. I also appended round-36 exploration notes to `research_notes.tex`.
