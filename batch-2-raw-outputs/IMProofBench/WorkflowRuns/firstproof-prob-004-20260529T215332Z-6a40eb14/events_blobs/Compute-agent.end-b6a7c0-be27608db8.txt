## literature

I searched the requested exact phrases and variants. I did **not** find the mixed estimate
\[
  \Vol(R)\gtrsim S_1S_2^{1/2}S_3^{3/2}S_4
\]
as a named/quoted Guth theorem, nor the exact phrase `S_1 S_2^{1/2} S_3^{3/2} S_4` in an indexed source. The useful sources remain:

1. Larry Guth, *Area-contracting maps between rectangles*, PhD thesis, MIT, 2005. MIT handle: `http://hdl.handle.net/1721.1/31158`. I retrieved the current DSpace page and bitstream metadata; local PDF is `papers/guth_area_contracting_thesis_2005.pdf`, text extraction is `data/pdftxt/guth_thesis_2005.txt`.
2. Larry Guth, *Area-expanding embeddings of rectangles*, arXiv:0710.0403. Local PDF/text: `papers/guth_area_expanding_rectangles_0710.0403.pdf`, `data/pdftxt/guth_area_expanding_0710.0403.txt`.
3. Larry Guth, *The width-volume inequality*, GAFA 17 (2007), 1139--1179, DOI `10.1007/s00039-007-0628-5`. This contains the classical snake-map discussion and refers back to the thesis for the harder \(2\le k<n-1\) cases.

Relevant thesis details:

- Chapter 8 is explicitly titled "Partial Results On 2-Contracting Diffeomorphisms Between 4-Dimensional Rectangles" (pp. 139--149).
- Proposition 8.1.3 proves the first-alternative style statement for diffeomorphisms: if the small relative 2-cycle filling bound applies, then \(R_3R_4\gtrsim S_3S_4\). The OCR drops a square in the displayed hypothesis; from Proposition 8.1.2 and the proof it should be the \(R_1R_2^2\) threshold.
- Section 8.2 lists five bounded-2-dilation degree-one maps, all perturbable to diffeomorphisms: snake, codimension-one snake, short-side stretch, pinching, double pinching. The exact technical remark after map 3 is narrower than the tempting overgeneralization: it gives a target \(A R_1\times A^{-3}R_2\times A\times B\) with \(A^4<R_2/R_1\), \(R_3<A<(R_3R_4)^{1/2}\), and \(R_3R_4=AB\).
- Guth’s final remarks say the thesis techniques are "not even close" to estimating the best 2-dilation for 4D rectangles. So the present mixed inequality is not something I would cite as known from Guth without an additional argument.

## algebraic reduction

The current reductions in `answer.tex` do **not** algebraically imply the desired mixed volume estimate. I wrote a reproducible LP/enumeration checker:

- code: `code/round6_trace_lp.py`
- output: `data/round6_trace_lp_output.txt`

The clean exponent countermodel is:
\[
 S=(1,1,L,L),\qquad
 R=(L^{-1/5},L^{13/15},L^{13/15},L^{13/15}).
\]
Equivalently
\[
 s=(0,0,1,1),\qquad r=(-1/5,13/15,13/15,13/15),\qquad v=\log_L\Vol(R)=12/5.
\]

It satisfies the side orderings and the two smallness assumptions:
\[
 R_1/S_1=L^{-1/5},\qquad
 {R_3R_4\over S_3S_4}=L^{-4/15}.
\]
It violates the desired conclusion by a power:
\[
 {V\over S_1S_2^{1/2}S_3^{3/2}S_4}
 =L^{12/5-5/2}=L^{-1/10}\to0.
\]
Thus for any fixed small \(\kappa\), choosing \(L\) large beats any constant \(c\kappa\).

All Guth \(n=4,k=2\) monomial estimates are satisfied. The exponent margins for left/right are:

| inequality | exponent margin |
|---|---:|
| \(R_1R_2\ge cS_1S_2\) | \(2/3\) |
| \(R_1R_2R_3\ge cS_1S_2S_3\) | \(8/15\) |
| \(R_1^2R_2R_3\ge cS_1^2S_2S_3\) | \(1/3\) |
| \(V\ge cS_1S_2S_3S_4\) | \(2/5\) |
| \(R_1^3R_2R_3R_4\ge cS_1^3S_2S_3S_4\) | \(0\) |

The trace inequalities also hold. Their common right-side exponent is
\[
T=s_1+s_2+2s_3+s_4=3.
\]
For \(i=1\), the quadratic term supplies equality:
\[
r_1+v=11/5,\qquad 2v-r_1-s_3-s_4=3.
\]
For \(i=2,3,4\), the linear term supplies the inequality:
\[
r_i+v=49/15,\qquad 2v-r_i-s_3-s_4=29/15,
\]
so the slack is \(49/15-3=4/15\).

Conclusion: the four independent trace inequalities are still too weak. They allow one short side to be handled by the quadratic branch while the other three are handled separately by the linear branch.

## counterexample/proof status

I do **not** have a genuine counterexample map to the original theorem. The algebraic model above is only a counterexample to the **current reductions**.

For the specific stress test
\[
R^0=(L^{-1},L^4,L^5,L^6),\qquad S=(1,1,L^6,L^6),
\]
the desired alternatives all fail by \(L^{-1}\), and Guth’s published monomial estimates do not obstruct it. See `data/round6_scaling_known_estimates.txt`.

However, I found no reliable Guth-map construction producing a bounded-2-dilation map \(R^0\to S\). The tempting decomposition is
\[
(L^{-1},L^4,L^5,L^6)
\xrightarrow[\text{short-side stretch }A=L]{}
(1,L,L^5,L^6)
\dashrightarrow
(1,1,L^6,L^6).
\]
The first arrow is exactly Guth’s short-side stretch / technical variant. The second "middle-side snake" is not one of the safe Section 8.2 maps.

There is a concrete obstruction if one tries to realize the residual arrow by Guth’s perturbable snake/diffeomorphism constructions. For
\[
T=(1,L,L^5,L^6),\qquad S=(1,1,L^6,L^6),
\]
Guth’s boundary ellipsoid inequality B3b applies because \(T_2^2=L^2<S_2S_3=L^6\), and would force
\[
T_3T_4\gtrsim S_3S_4.
\]
But \(T_3T_4=L^{11}\) while \(S_3S_4=L^{12}\). Hence no bounded-2-dilation **diffeomorphism** of this residual type can exist. Since the Section 8.2 maps are stated as degree-one maps perturbable to diffeomorphisms, this rules out the obvious route through Guth’s listed constructions.

This does **not** rule out an arbitrary degree-one map of pairs for the residual arrow. Guth’s arXiv Estimate 1 also does not rule it out. So the status is:

- known true from literature: not found;
- known false by Guth snake maps: not established;
- likely typo/overclaim if attributed directly to Guth’s existing theorems;
- current `answer.tex` reductions: definitely insufficient.

## recommended next edit

Do not present the boxed mixed estimate as a consequence of the trace inequalities. Add the exponent model above to the "Remaining open issues" section, or replace that section by a short "Algebraic insufficiency of the trace reduction" paragraph.

If the original theorem is still the target, the next needed lemma must couple the trace inequalities simultaneously. The present inequalities allow the branches to be chosen independently in \(i\); the model \(R=(L^{-1/5},L^{13/15},L^{13/15},L^{13/15})\), \(S=(1,1,L,L)\) exploits exactly that. A successful refinement must rule out the pattern:

- \(i=1\) uses \(V^2/(R_1S_3S_4)\);
- \(i=2,3,4\) use \(R_iV\);
- no penalty is paid for making all long \(R_i\)'s equal.

Possible direction: prove an integrated/simultaneous trace estimate involving products or correlations such as \(\int A_yL_{i,y}\), or a boundary-degree estimate for the family of traces, rather than four separate Jensen bounds.
