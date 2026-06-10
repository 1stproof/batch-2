# Author round 8

Files changed: ['answer.tex', 'research_notes.tex']
Ready: False
Council question: We need prove or refute the remaining small-p lemma:

For \(0\le p\le 1/3\), \(w_i\ge0\), \(\sum_iw_i=1\), and iid \(v_i\sim\mathrm{Bernoulli}(p)\), prove
\[
\Pr\left[\sum_i w_i v_i\ge p\right]\ge p.
\]

Equivalently, for \(q=1-p\ge2/3\), prove
\[
\Pr\left[\sum_i w_i\eta_i>q\right]\le q,\qquad \eta_i\sim\mathrm{Bernoulli}(q).
\]

A promising reduction added this round: define
\[
\Phi_q(w)=\Pr_q\left[\sum_i w_i\eta_i>q\right].
\]
If two weights \(x\le y\) are coalesced to \(x+y\), and \(Z\) is the contribution of the other weights, then
\[
\Phi_q(\ldots,x+y,\ldots)-\Phi_q(\ldots,x,y,\ldots)
=pq\left(\Pr[q-x-y<Z\le q-y]-\Pr[q-x<Z\le q]\right),
\]
up to endpoint conventions. If for every non-unit vector and every \(q\ge2/3\) some pair can be coalesced without decreasing \(\Phi_q\), repeated coalescence proves the lemma because the one-weight vector has \(\Phi_q=q\). Random searches support existence of such a pair, though arbitrary prescribed pairs can fail.

Please suggest a rigorous proof strategy for either the small-\(p\) lemma directly or this coalescence assertion. I am especially interested in: (1) an induction or averaging proof that some pair has nonnegative coalescence gain; (2) a known theorem about biased product measures of halfspaces through their mean; (3) a combinatorial injection/shadow argument for the strict complement inequality; or (4) a Bellman/dynamic-programming invariant stronger than the failed scalar minorant.
Council to: (default models)
Parse warnings: (none)

## Thinking summary

Updated the canonical files and compile-checked `answer.tex` successfully with `pdflatex`; the PDF is 8 pages and within the contract. I fixed the noted \(p=0\) edge-case wording and the residual-weight notation in the unit-gap converse. Since I still do not have a proof of the small-\(p\) lemma, I did not mark the solution ready.

Main mathematical addition this round: I added a coalescence reduction in the complement formulation. It derives the exact change in the bad upper-tail probability when two weights \(x\le y\) are merged:
\[
\Delta=pq\big(\Pr[q-x-y<Z\le q-y]-\Pr[q-x<Z\le q]\big),
\]
and records that the desired lemma would follow from proving that some pair can always be coalesced without decreasing the complement tail. This is not a proof yet, but it gives a concrete finite extremal target.
