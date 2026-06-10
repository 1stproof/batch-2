# Author round 1

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: We need a self-contained proof of the finite weighted Bernoulli inequality: for \(0\le p\le 1/3\), nonnegative \(w_i\) summing to \(1\), and independent \(v_i\sim\mathrm{Bernoulli}(p)\),
\[
\Pr\left[\sum_i w_i v_i\ge p\right]\ge p.
\]
Equivalently, if \(L=1/p\ge3\), \(0\le a_i\le1\), \(\sum_i a_i=L\), and \(\xi_i\sim\mathrm{Bernoulli}(1/L)\), prove
\[
\Pr\left[\sum_i a_i\xi_i\ge1\right]\ge 1/L.
\]
The reciprocal/integer \(L\) case has a coloring proof. Please suggest viable strategies for the non-integral \(L>3\) case, ideally a complete proof or a precise known theorem. Be wary of two false deterministic strengthenings: (1) rational color weights do not satisfy the desired fixed-size subset bound in general; e.g. \(a=3,b=10\), seven entries \(1/7\), three \(0\); (2) a deterministic circle-arc start-measure analogue is false.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files. I removed the unsupported Kellerer black-box claim from `answer.tex`, added a rigorous proof for the reciprocal points \(p=1/k\) (including \(p=1/3\)), retained the valid counterexamples and endpoint arguments, and isolated the remaining small-\(p\) lemma explicitly. I also expanded `research_notes.tex` with the main equivalent formulations and several failed-but-informative approaches/counterexamples to overly strong reductions.

`answer.tex` compiles successfully with `pdflatex` in 3 pages.
