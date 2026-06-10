# Author round 8

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: Please assess the revised support-corner lemma now used in answer.tex: for coefficient boundary supports \(q_{\mathcal H},q_{\mathcal K}\), is the inclusion
\[
q_{\mathcal H}(q_{\mathcal K}\mathcal A_Nq_{\mathcal K})q_{\mathcal H}
\subset
q_{\mathcal H\otimes_N\overline{\mathcal H}\otimes_N\mathcal K}
\mathcal A_N
q_{\mathcal H\otimes_N\overline{\mathcal H}\otimes_N\mathcal K}
\]
actually justified by DKEP Proposition 5.9 / Theorem 5.10 when interpreted in the ordinary enveloping algebra before cutting by \(p_{\rm nor}\)? If not, what exact corrected support statement is sufficient for the graph-product intersection \(q_W(q_U\mathcal A q_U)q_W\subset q_{U\cap W}\mathcal A q_{U\cap W}\)?
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Revised the canonical files. The new `answer.tex` compiles successfully with `pdflatex` twice; PDF is 4 pages. Main changes: removed the normal-bidual left-ideal multiplication argument, replaced it with an ordinary-envelope/triple-fusion support calculus, fixed the direct-sum support justification via DKEP Theorem 5.10, and made the \(\Theta(x)=q_0xq_0\) trace-extension point explicit.
