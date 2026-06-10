# Author round 5

Files changed: ['answer.tex', 'references.bib', 'research_notes.tex']
Ready: False
Council question: (none)
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files.

Summary of changes:
- Reworked `answer.tex` into a cleaner partial solution:
  - Added a general rational coloring criterion.
  - Reorganized the \(p=1/k\) and \(p=2/b\) proofs under that criterion.
  - Made the pair-counting arithmetic explicit.
  - Added finite sharpness examples and retained pivot-plus-dust sharpness.
  - Filled in the coordinatewise down-closed proof in the convex-hull formulation.
  - Kept an explicit “Remaining open issues” section because the small-\(p\) lemma is still not proved.
- Updated `research_notes.tex` with the new coloring/MMS-style criterion, cyclic counter-observation, four-tail pivot invariant, buffered invariant notes, and complement/intersection viewpoint.
- Added relevant bibliography entries to `references.bib`.
- Ran `pdflatex` on `answer.tex` twice successfully; compiled PDF is 5 pages and has no warnings/errors.

I also added a literature pointer to Fokkink–Meester–Pelekis, whose paper frames the related convex-combination Bernoulli tail optimization problem and proves it only in certain parameter regions, not the full strict hypotenuse case needed here. ([arxiv.org](https://arxiv.org/abs/2002.06804))

I am **not** marking ready, because the essential sufficiency proof for all \(0\le p\le 1/3\) remains open in the draft.
