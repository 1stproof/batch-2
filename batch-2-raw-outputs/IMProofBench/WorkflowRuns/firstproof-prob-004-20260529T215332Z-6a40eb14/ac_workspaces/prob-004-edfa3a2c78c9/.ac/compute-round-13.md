# Compute worker reply — round 13
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c2-2aa4fc/compute_workspace_round_13.zip

---

# Round 13 compute report

## 1. Search for Guth's 4D 2-dilation preprint

I did **not** find a downloadable copy of

> Larry Guth, *On the 2-dilation of mappings between 4-dimensional rectangles*, preprint.

What I checked:

- Exact web searches for the full title and variants requested in the prompt.
- arXiv search/listing for Larry Guth.  The relevant 2007--2008 arXiv items present are:
  - `0710.0403`, *Area-expanding embeddings of rectangles*.
  - `0802.3549`, *Directional isoperimetric inequalities and rational homotopy invariants*.
  - `0802.3550`, *Isoperimetric inequalities and rational homotopy invariants*.
  No arXiv item with the 4D 2-dilation title appears in Guth's author listing.
- Current MIT page `https://math.mit.edu/~lguth/` and likely subdirectories (`Papers/`, `papers/`, `Preprints/`, etc.); no hit.
- Internet Archive CDX for old Stanford/MIT/NYU pages:
  - `data/round13/cdx_math_stanford_lguth.json`
  - `data/round13/cdx_www_math_stanford_lguth.json`
  - `data/round13/cdx_math_mit_lguth.json`
  - `data/round13/cdx_cims_nyu_guth.json`
  - `data/round13/cdx_math_nyu_guth.json`
  - targeted wildcard searches for `*dilat*`, `*rect*`, `*rectangle*`, `*mapping*`, etc.
  The only old Stanford PDF with an "estimate" type name was a 2006 teaching handout on estimating integrals, saved as `papers/round13/archive_stanford_estimate_20060718.pdf`; it is unrelated.
- Citation/metadata APIs:
  - Semantic Scholar exact title: 0 results.
  - OpenAlex searches: no plausible result.
  - Crossref title search: no plausible result.
  - DataCite exact title: 0 results.
  - Internet Archive advanced search exact/keyword: 0 results.

I downloaded the arXiv source for `0802.3549` to `papers/round13/guth_directional_0802.3549_src.tar.gz` and extracted it to `data/round13/directional_src/`.  The source file `LINKDIL2.TEX` contains the exact reference:

```tex
\bibitem{G4} Guth, L., On the 2-dilation of mappings between 4-dimensional rectangles, preprint.
```

The same source says the problem was "recently solved" and that the answer is complicated: near-optimal maps are far from linear, cases split by rectangle dimensions, and the optimal 2-dilation among degree-one diffeomorphisms can be arbitrarily larger than among degree-one maps.  Since no copy surfaced, I cannot quote its theorem statements.  Based on the available evidence, it was not simply `0710.0403`; that paper is the area-expanding embedding paper and cites the thesis/width-volume material, but not this 4D 2-dilation preprint.

## 2. Directional inequalities for all target coordinate pairs

Let target pairs be \(A=(a,b)\), \(a<b\), and let \(F_A=(f_a,f_b)\).  Let \(Q_A\) be the central rectangle in the \((y_a,y_b)\)-coordinates.  For a.e. \(y\in Q_A\), the slice
\[
Z^A_y=\langle [R,\partial R],F_A,y\rangle
\]
maps to the complementary target 2-rectangle \(P^A_y\).  If \(A^c=(c,d)\), the target calibration gives
\[
\Fill_S(P^A_y)\gtrsim S_cS_d\min(S_a,S_b).
\]

For source pairs \(ij\in\{12,13,14,23,24,34\}\), define
\[
M^{ab}_{ij}:=\int_{F_A^{-1}(Q_A)}
\left|\frac{\partial(f_a,f_b)}{\partial(x_i,x_j)}\right|\,dx .
\]
Important bookkeeping: \(M^{ab}_{ij}\) is the integral of a **source minor of the slicing map**; it equals the integrated directional volume of the slices in the complementary source projection.  With this convention, the relative directional filling estimate gives, for every target pair \(ab\),
\[
S_a\,S_1S_2S_3S_4
\lesssim
R_1(M^{ab}_{12}+M^{ab}_{13}+M^{ab}_{14})
 +R_2(M^{ab}_{23}+M^{ab}_{24})
 +R_3M^{ab}_{34}. \tag{DI}_{ab}
\]
Thus the six left sides are:

| target pair \(ab\) | left side of \((DI)_{ab}\) |
|---|---:|
| \(12\) | \(S_1^2S_2S_3S_4\) |
| \(13\) | \(S_1^2S_2S_3S_4\) |
| \(14\) | \(S_1^2S_2S_3S_4\) |
| \(23\) | \(S_1S_2^2S_3S_4\) |
| \(24\) | \(S_1S_2^2S_3S_4\) |
| \(34\) | \(S_1S_2S_3^2S_4\) |

The current `answer.tex` inequality (14) is the \(ab=34\) case.

## 3. Pointwise \(\Dil_2\le 1\) model

Let \(A=df=(a_{\alpha i})\), target index \(\alpha\), source index \(i\).  In lexicographic pair order
\[
12,13,14,23,24,34,
\]
the \(6\times 6\) compound matrix \(B=\Lambda^2 A\) has entries
\[
B_{\alpha\beta,ij}
=a_{\alpha i}a_{\beta j}-a_{\alpha j}a_{\beta i}
=\frac{\partial(f_\alpha,f_\beta)}{\partial(x_i,x_j)}.
\]
The pointwise 2-dilation condition is
\[
\|B\|_{\ell^2(\Lambda^2)\to\ell^2(\Lambda^2)}\le 1.
\]
In particular each row and each column has \(\ell^2\)-norm at most 1, and every entry has absolute value at most 1.

The compound-matrix/Plucker constraint can be written compactly using the wedge-pairing matrix \(J\) for
\[
p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}.
\]
For an actual \(B=\Lambda^2 A\),
\[
B^TJB=(\det A)J
\]
and equivalently \(B\) sends decomposable 2-vectors to decomposable 2-vectors.  These are much stronger than arbitrary \(6\times 6\) contraction constraints, but after passing to absolute-value integrals \(M^{ab}_{ij}\), much of the sign-sensitive content is lost.

## 4. Algebraic/scaling obstruction to closing the proof from these inequalities alone

I built a reproducible exponent check:

- script: `code/round13_directional_model.py`
- output: `data/round13/directional_model_output.txt`

Use the stress family already in the notes:
\[
S=(1,1,L^6,L^6),\qquad R=(L^{-1},L^4,L^5,L^6).
\]
Then \(R_1/S_1=L^{-1}\), \(R_3R_4/S_3S_4=L^{-1}\), and
\[
\Vol(R)=L^{14}\quad\text{while}\quad
S_1S_2^{1/2}S_3^{3/2}S_4=L^{15}.
\]
So this scaling violates the desired second alternative by \(L^{-1}\).

Now impose a formal pointwise differential model
\[
df\sim \operatorname{diag}(1,L^{-1},L^{-1},1)
\]
on a set of volume \(L^{14}\).  This is **not** asserted to be an actual rectangle map; it is a test of the algebraic information retained by the integrated directional inequalities plus the exact compound/Plucker constraints.

For this model:

- \(\|\Lambda^2df\|=1\), so \(\Dil_2\le1\).
- \(\det df=L^{-2}\), hence \(\int\det df=L^{14}L^{-2}=L^{12}=\Vol(S)\), matching the degree volume identity.
- The diagonal entries of \(\Lambda^2df\) have exponents
  \[
  (12,13,14,23,24,34)=(-1,-1,0,-2,-1,-1).
  \]
- The Plucker/conformal relation holds: \(B_{12}B_{34}\), \(-B_{13}B_{24}\), and \(B_{14}B_{23}\) all have exponent \(-2=\det df\).

The script verifies the six directional inequalities at the exponent level:

| target pair | LHS exponent | available RHS exponent | slack |
|---|---:|---:|---:|
| \(12\) | 12 | 12 | 0 |
| \(13\) | 12 | 12 | 0 |
| \(14\) | 12 | 13 | 1 |
| \(23\) | 12 | 16 | 4 |
| \(24\) | 12 | 17 | 5 |
| \(34\) | 18 | 18 | 0 |

Conclusion: the six integrated directional inequalities, even supplemented by pointwise \(\Dil_2\le1\), degree-volume, and exact decomposable/Plucker compound-matrix structure, do **not** algebraically imply the desired lower bound.  They admit the same hard-regime stress scaling with \(\Vol(R)=L^{14}\) instead of the desired \(L^{15}\).

This does not disprove the theorem, because the diagonal model ignores boundary/side-spanning constraints of an actual map of pairs.  It does show that the remaining proof cannot close by manipulating only the absolute-value minor budgets \(M^{ab}_{ij}\) from these directional slice inequalities.  A successful route needs an additional input that sees one-dimensional spanning/boundary data, global family topology of the fibers, or a sharper signed/parametric relation not destroyed by taking absolute values.
