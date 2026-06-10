# Round 11 literature/computation report

## Retrieved sources

I downloaded and converted to text:

- Guth thesis: `papers/guth-thesis-area-contracting.pdf`, MIT DSpace handle `https://dspace.mit.edu/handle/1721.1/31158`, bitstream name `61207020-MIT.pdf`.  DSpace metadata says 208 pages, thesis (MIT Mathematics, 2005), title *Area-contracting maps between rectangles*.
- Guth, *The width-volume inequality*: `papers/width-volume-arxiv.pdf`, `https://arxiv.org/abs/math/0609569`.
- Guth, *Area-expanding embeddings of rectangles*: `papers/area-expanding-arxiv.pdf`, `https://arxiv.org/abs/0710.0403`.
- Guth, *Minimax problems related to cup powers and Steenrod squares*: `papers/minimax-arxiv.pdf`, `https://arxiv.org/abs/math/0702066`.

Auxiliary files:

- `data/search_summary_requested_terms.md`: page-hit summary for the requested terms.
- `data/round11_key_excerpts.md`: extracted page excerpts.
- `data/round11_guth_ch8_stress_search.txt` and `data/round11_guth_ch8_stress_search_deeper.txt`: exponent searches for the stress family using Guth Chapter 8.2 moves.
- `data/round11_page_images/thesis_p130-130.png` and `data/round11_page_images/thesis_p148-148.png`: page images resolving OCR ambiguities.

## Main conclusion

I did **not** find the theorem in the prompt as a proved black box in Guth's thesis or the three papers.  In fact the thesis explicitly says the relevant problem is not solved: thesis p. 22 says the 2-dilation problem for diffeomorphisms between 4D rectangles is "far from solving Problem 1" and "I do not even have a guess"; thesis p. 139 introduces Chapter 8 as "Partial Results On 2-Contracting Diffeomorphisms Between 4-Dimensional Rectangles" and again says "I am not able to give a complete solution."

Recommendation: **do not cite a complete Guth theorem for the prompt theorem.**  Use Guth as black boxes only for:

1. the degree-one monomial inequalities from *Area-expanding embeddings*, Estimate 1;
2. the rectangular relative isoperimetric profile, *Area-expanding embeddings*, Theorem 3;
3. the Chapter 8.1 first-alternative argument, especially thesis Propositions 8.1.2 and 8.1.3, adapted to degree-one maps of pairs.

The remaining second-alternative step still needs a genuinely family-level/parametric filling estimate for the central slices.  I did not find it in the retrieved sources.

## Exact relevant statements found

### 1. Area-expanding / monomial estimate

In *Area-expanding embeddings*, Theorem 1, p. 1, Guth proves the necessary inequalities for a \(k\)-expanding embedding \(S\hookrightarrow R\):
\[
(R_1\cdots R_j)^{(l-j)/(k-j)}R_{j+1}\cdots R_l
\ge c(n)(S_1\cdots S_j)^{(l-j)/(k-j)}S_{j+1}\cdots S_l .
\]

More useful for us is Estimate 1, p. 10: if \(U\subset R\) and \(\Phi:(U,\partial U)\to(S,\partial S)\) has degree \(D>0\), then
\[
\operatorname{dil}_k(\Phi)\ge c(n)Q_1\cdots Q_j(Q_{j+1}\cdots Q_l)^{(k-j)/(l-j)}.
\]
For \(n=4,k=2,j=1,l=4,\Dil_2\le1\), this gives only
\[
R_1^3R_2R_3R_4\gtrsim S_1^3S_2S_3S_4.
\]
With \(R_1=\alpha S_1\), this is
\[
\operatorname{Vol}(R)\gtrsim \alpha^{-2}S_1S_2S_3S_4.
\]
This is already in the draft.  It helps when \(S_3/S_2\) is not too large, but it does not imply
\(\operatorname{Vol}(R)\gtrsim S_1S_2^{1/2}S_3^{3/2}S_4\) in the hard high-aspect regime.

The proof uses complexes of cycles and a tightening construction.  The key pieces are:

- Theorem 3, pp. 7-9: rectangular relative isoperimetric profile.
- Lemma 4.1, pp. 11-12: small complexes of cycles are null-homotopic.
- Key Lemma, pp. 14-16: the tightened complex \(C_1\) has the same degree as the original map.

I see no weighted or averaged filling estimate for a two-parameter family of central slices in this proof.

### 2. Thesis Chapter 8: the actual 4D 2-dilation material

Thesis p. 140 lists the embedding inequalities for a 2-contracting diffeomorphism \(R\to S\):
\[
R_1R_2\gtrsim S_1S_2,\quad
R_1R_2R_3\gtrsim S_1S_2S_3,\quad
R_2^2R_3\gtrsim S_2^2S_3,
\]
\[
\operatorname{Vol}(R)\gtrsim\operatorname{Vol}(S),\quad
R_1^3R_2R_3R_4\gtrsim S_1^3S_2S_3S_4.
\]

Proposition 8.1.1, pp. 140-142, solves the boundary ellipsoid problem up to constants.  The important part is:
\[
\text{if }R_2^2>S_2S_3,\quad R_2R_3R_4\gtrsim S_2^{1/2}S_3^{3/2}S_4,
\]
and if \(R_2^2<S_2S_3\), then \(R_3R_4\gtrsim S_3S_4\).  This is close to the desired mixed expression, but it is a **boundary 3-volume** estimate, not the desired 4-volume estimate with an \(S_1\) factor.  Multiplying by \(R_1\) would give \(R_1S_2^{1/2}S_3^{3/2}S_4\), which is too weak when \(R_1\ll S_1\).

Proposition 8.1.2, pp. 143-144: if \(C\) is an oriented relative 2-cycle in \(R\) with area \(<\frac12R_1R_2\), then it fills with volume \(\lesssim R_1R_2^2\).

Proposition 8.1.3, p. 144: if there is a 2-contracting diffeomorphism \(R\to S\) and
\[
CR_1R_2^2<S_1S_2S_3,
\]
then
\[
R_3R_4\gtrsim S_3S_4.
\]
This is exactly the first-alternative mechanism in the current draft.  Although Guth states it for diffeomorphisms, the proof only uses degree/slicing, \(\Dil_3\le1\), and the relative isoperimetric estimate; it should adapt to degree-one maps of pairs.

### 3. Rational homotopy inequalities

Thesis Section 7.7, p. 130, records the \(n=4,k=2\) rational-homotopy inequalities.  The page image confirms:
\[
R_2R_3^2R_4\gtrsim S_2S_3^2S_4,
\]
and, from the double,
\[
R_1R_2R_3^2R_4\gtrsim S_1S_2S_3^2S_4,
\qquad
R_1R_2^2R_3^2R_4\gtrsim S_1S_2^2S_3^2S_4.
\]
Thesis p. 143 notes that \(R_1R_2R_3^2R_4\gtrsim S_1S_2S_3^2S_4\) is not implied by the earlier embedding/boundary inequalities.  These are useful checks, but they still do not imply the prompt's \(S_1S_2^{1/2}S_3^{3/2}S_4\) volume lower bound.

### 4. Minimax paper

The minimax paper gives a general mechanism for degree-one maps:
Proposition 9.1, p. 53, and Proposition 9.2, p. 54, say that for natural mod-2 operations \(O\),
\[
\Lambda V_{(M,g)}(Oa(k,M))\ge V_{(N,h)}(Oa(k,N)).
\]
On p. 54 Guth states that estimating rectangle minimax volumes would reprove the known monomial inequalities, and ends with a conjectural rectangle formula.  I found no proved rectangle minimax formula that gives the missing mixed central-slice estimate.

## Reconstruction of the proved partial argument

For \(F=(f_3,f_4)\) and central \(y\in [S_3/3,2S_3/3]\times[S_4/3,2S_4/3]\), let
\[
Z_y=\langle [R,\partial R],F,y\rangle .
\]
By slicing naturality, \(f_\#Z_y\) is the central relative \(S_1\times S_2\) plane \(P_y\) in \(S\).

A calibration with \(\omega=dx_1\wedge dx_2\wedge d\psi(x_3,x_4)\), where \(\psi=0\) on the \((x_3,x_4)\)-boundary and \(\psi(y)\gtrsim S_3\), gives
\[
\Fill_S(P_y)\gtrsim S_1S_2S_3.
\]
Since \(\Dil_2(f)\le1\Rightarrow \Dil_3(f)\le1\), every filling of \(Z_y\) pushes forward to a no-larger filling of \(P_y\), so
\[
\Fill_R(Z_y)\gtrsim S_1S_2S_3.
\]
If \(CR_1R_2^2<S_1S_2S_3\), Guth's isoperimetric profile forces \(\Mass Z_y\gtrsim R_1R_2\).  Coarea over a central \(Q\) of area \(\sim S_3S_4\) gives
\[
\Vol(R)\ge \int_Q\Mass Z_y\,dy\gtrsim R_1R_2S_3S_4,
\]
hence \(R_3R_4\gtrsim S_3S_4\).

This is solid, but it stops exactly when \(R_1R_2^2\gtrsim S_1S_2S_3\).  In that remaining case, the single-fiber isoperimetric profile yields only the known weaker averaged lower bound, losing a factor \((R_1/S_1)^{1/2}\).  I found no parametric repair in Guth's sources.

## Stress family and Guth constructions

For
\[
S=(1,1,L^6,L^6),\qquad R=(L^{-1},L^4,L^5,L^6),
\]
the three desired conclusions all fail at exponent \(-1\):
\[
R_1/S_1=L^{-1},\quad R_3R_4/(S_3S_4)=L^{-1},\quad
\Vol(R)/(S_1S_2^{1/2}S_3^{3/2}S_4)=L^{-1}.
\]

However the known Guth lower bounds do **not** rule it out:

- Estimate 1 has \(Q=(L,L^{-4},L,1)\); the strongest \(j=1,l=4\) monomial is exactly \(L^0\), so it is sharp but not contradictory.
- Proposition 8.1.3 is not triggered, since \(R_1R_2^2=L^7>S_1S_2S_3=L^6\).
- Boundary Proposition 8.1.1 is also sharp but not contradictory: \(R_2^2=L^8>S_2S_3=L^6\) and \(R_2R_3R_4=L^{15}=S_2^{1/2}S_3^{3/2}S_4\).
- The rational-homotopy inequalities on thesis p. 130 are all satisfied with positive margin.

I then checked whether Guth's Chapter 8.2 constructions directly produce this map.  They do not, as far as the exponent model sees.

- Snake map fixes \(R_1,R_2\), so cannot fix the \(L^{-1},L^4\to1,1\) issue.
- Codimension-one snake has parameter \(a\le (R_4/R_3)^{1/2}=L^{1/2}\), far too small to reduce \(R_2=L^4\) to \(1\).
- Short-side stretch can make \(R_1\) into \(1\) only in the technical variant, leaving residual exponents \((0,1,5,6)\); the final linear 2-dilation exponent to the target is still \(1\).
- Pinching requires \(A<R_1=L^{-1}\), so its first three output sides are too small for the stress target.
- Double pinching (thesis p. 148) outputs \(R_1^2/A\times A\times A\times B\), with \(R_1<A\), \(A^2<R_2R_3\), \(A^3B<\Vol(R)\).  It creates at most one very long side unless \(A\) is already large, and then the two \(A\)-sides do not match the target's two \(L^6\)-directions.

The reproducible beam search in `data/round11_guth_ch8_stress_search_deeper.txt` found no route ending in a linear 2-contracting map:

- step \(1\), depth \(5\), beam \(2000\): searched 16939 states, not found;
- step \(1/2\), depth \(5\), beam \(2500\): searched 39483 states, not found;
- step \(1/4\), depth \(4\), beam \(2500\): searched 89136 states, not found.

This is not a proof that no counterexample exists.  It only says the published/thesis snake/pinch templates do not obviously realize the stress family.

## Final recommendation

The state after this search is: **still unresolved**.  The exact obstacle is the missing family-level filling estimate for the two-parameter family \(Z_y\) of central slices.  Guth's thesis gives the correct first-alternative lemma and several sharp nearby obstructions, but explicitly labels the 4D 2-dilation rectangle problem as incomplete.  The minimax paper suggests a possible high-level route through parametric cycle-space lower bounds, but supplies no rectangle estimate strong enough for the desired \(S_1S_2^{1/2}S_3^{3/2}S_4\) term.
