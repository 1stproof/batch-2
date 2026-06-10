# Author round 1

Files changed: ['answer.tex', 'references.bib', 'research_notes.tex']
Ready: False
Council question: We need close the following precise gap. Let \(B\subset P\) be an inclusion of separable tracial von Neumann algebras with expectation, let \(A\) contain a trace-zero unitary, and set \(M=P*_B(B\bar\otimes A)\). Suppose \(P\) is properly proximal and \(P\) is not amenable relative to \(B\) inside \(P\). Is \(M\) properly proximal? 

The scalar free-product paradoxical-projection proof fails directly because the Bass--Serre half-tree projections have commutators compact only relative to \(e_B\), not in \(K_{\infty,1}(M)\). Please suggest a rigorous route: either an exact known theorem with hypotheses matching this statement, or a proof strategy using DKEP boundary pieces/normal bidual upgrading. A narrower graph-specific version is also acceptable: in the intended application \(P=M_{V_{k-1}}\), \(B=M_L\), and the graph supplies two \(B\)-orthogonal \(B\)-centered unitaries in \(P\ominus B\).
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and compile-checked `answer.tex` successfully with `pdflatex` (3 pages).

Summary of changes:
- Removed the falsely validated “DKEP permanence” theorem as a claimed standard input.
- Added a self-contained scalar free-product lemma covering the finite-dimensional base case, adapting the DKEP paradoxical-projection argument; DKEP’s published Proposition 6.7 only states the diffuse free-product case. ([arxiv.org](https://arxiv.org/pdf/2204.00517))
- Kept the graph-theoretic induction and the CDHJKN relative amenability obstruction, which matches their Theorem A criterion. ([arxiv.org](https://arxiv.org/pdf/2404.08150))
- Explicitly isolated the remaining missing ingredient as a Bass–Serre/amalgamated-free-product permanence proposition, instead of treating it as proved.
- Added detailed research notes on why the AFP step is subtle: half-tree projections are compact only relative to the amalgamating algebra, so a relative-to-full proper proximality upgrade is needed.
