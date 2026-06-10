# Compute worker reply — round 26
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c0-8aaa80/compute_workspace_round_26.zip

---

# Round 26 literature retrieval: Guth 4D rectangle 2-dilation

## Bottom line

I refreshed the downloads and searched the accessible documents for the exact 4D rectangle result requested. I did **not** locate a public copy of Guth's unpublished/preprint item
\[
\textit{On the 2-dilation of mappings between 4-dimensional rectangles}.
\]
The only exact occurrence I found is Guth's own bibliography entry in arXiv:0802.3549, where he cites it as a preprint.

I also did **not** find, inside the thesis or arXiv:0710.0403/0802.3549, a theorem statement with the full hypotheses
\[
R,S\subset \mathbb R^4,\quad \deg f=1,\quad \operatorname{Dil}_2(f)\le 1,\quad R_1\le cS_1
\]
and the dichotomy
\[
R_3R_4\gtrsim S_3S_4
\quad\text{or}\quad
\operatorname{Vol}(R)\gtrsim S_1S_2^{1/2}S_3^{3/2}S_4 .
\]
The accessible sources justify the first alternative in a small-filling regime and the standard monomial estimates, but not the hard-regime volume alternative.

## Files saved this round

- MIT thesis PDF: `papers/round26/guth_area_contracting_thesis_mit_61207020.pdf`
- MIT item/bitstream metadata: `data/round26/mit_item_31158.json`, `data/round26/mit_bitstreams_original.json`
- Thesis text/pages/images:
  `data/round26/guth_area_contracting_thesis_pdftotext.txt`,
  `data/round26/thesis_pdfpages_139_149.txt`,
  `data/round26/page_images/thesis_p-140.png`,
  `data/round26/page_images/thesis_p143-143.png`,
  `data/round26/page_images/thesis_p144-144.png`
- arXiv:0710.0403 PDF/source/text:
  `papers/round26/arxiv_0710.0403.pdf`,
  `papers/round26/arxiv_0710.0403_e-print.tar`,
  `data/round26/arxiv_0710_0403_src/EXEMB2.TEX`,
  `data/round26/arxiv_0710.0403_pdftotext.txt`
- arXiv:0802.3549 PDF/source/text:
  `papers/round26/arxiv_0802.3549.pdf`,
  `papers/round26/arxiv_0802.3549_e-print.tar`,
  `data/round26/arxiv_0802_3549_src/LINKDIL2.TEX`,
  `data/round26/arxiv_0802.3549_pdftotext.txt`
- Missing-preprint search logs:
  `data/round26/arxiv_exact_missing.xml`,
  `data/round26/arxiv_variant_missing.xml`,
  `data/round26/crossref_exact_title.json`,
  `data/round26/openalex_exact_title.json`,
  `data/round26/datacite_exact_title.json`,
  `data/round26/semanticscholar_exact_title.json`,
  `data/round26/archive_advanced_exact_title.json`,
  `data/round26/cdx_math_mit_lguth.json`,
  `data/round26/cdx_math_stanford_lguth.json`

Download checksums are in `data/round26/download_sha256.txt`. CAS probe found Sage, GAP, Singular, and PARI/GP installed, but no CAS computation was needed.

## MIT thesis retrieval

The DSpace item is handle `1721.1/31158`, item UUID `cadf67f7-db0a-4bb0-b804-b27e1d462e55`. The original PDF bitstream is `61207020-MIT.pdf`, UUID `f3e1bda3-557c-4cc0-8244-6de14c095abd`, size `12,365,750` bytes, MD5 `788e2113627e3040d3a5a1c3cd32936b`. The thesis metadata says:

- Author: Lawrence Guth.
- Title: *Area-contracting maps between rectangles*.
- Thesis: Ph.D., MIT Department of Mathematics, 2005.
- Extent: 208 pages.

## What the thesis actually proves

The relevant part is Chapter 8, pp. 139--149, titled "Partial Results On 2-Contracting Diffeomorphisms Between 4-Dimensional Rectangles"; see `data/round26/thesis_pdfpages_139_149.txt`.

On p.139 Guth explicitly says the chapter is **partial**: he considers 2-dilation of **diffeomorphisms** between 4D rectangles and is "not able to give a complete solution." Theorem 8.1 solves only the special case in which the domain is the unit 4-cube.

Proposition 8.1.1, p.140, is a boundary/ellipsoid result. For ellipsoids with axes \(R_1\le R_2\le R_3\le R_4\) and \(S_1\le S_2\le S_3\le S_4\), a 2-contracting diffeomorphism \(E\to F\) approximately exists iff certain inequalities hold. The relevant ones are:
\[
R_2R_3\gtrsim S_2S_3,\qquad
R_2^2R_3R_4\gtrsim S_2^2S_3S_4,
\]
and
\[
R_2^2>S_2S_3\Rightarrow
R_2R_3R_4\gtrsim S_2^{1/2}S_3^{3/2}S_4,
\]
\[
R_2^2<S_2S_3\Rightarrow
R_3R_4\gtrsim S_3S_4.
\]
This is the nearest accessible source of the \(S_2^{1/2}S_3^{3/2}S_4\) exponent, but it is a boundary ellipsoid/diffeomorphism statement, not the desired interior degree-one pair-map theorem. Multiplying it by \(R_1\) would lose the needed \(S_1/R_1\) factor in the hard regime.

Proposition 8.1.2, p.143, states: if \(C\) is an oriented relative 2-cycle in a 4D rectangle \(R\) with area \(<(1/2)R_1R_2\), then \(C\) has an oriented filling with volume \(<CR_1R_2^2\). The page image `data/round26/page_images/thesis_p143-143.png` confirms the square in \(R_2^2\).

Proposition 8.1.3, p.144, states:
\[
\text{if there is a 2-contracting diffeomorphism }R\to S
\text{ and } CR_1R_2^2<S_1S_2S_3,
\]
then
\[
R_3R_4>cS_3S_4.
\]
Proof outline: take central target planes
\([0,S_1]\times[0,S_2]\times\{y_3,y_4\}\). Their relative filling volume in \(S\) is \(\gtrsim S_1S_2S_3\). Pulling back by the diffeomorphism gives relative 2-cycles in \(R\) with filling volume at least this large. Proposition 8.1.2 forces their areas to be \(\gtrsim R_1R_2\). Coarea/transverse-area over the central \((y_3,y_4)\)-rectangle gives
\(\operatorname{Vol}(R)\gtrsim R_1R_2S_3S_4\), hence \(R_3R_4\gtrsim S_3S_4\).

This is exactly the first-alternative mechanism in `answer.tex`, but Guth states it for diffeomorphisms. The adaptation to arbitrary degree-one maps of pairs requires the slicing-current/naturality argument in the draft; it is not a theorem statement I found in the thesis.

## Snake and pinching material

Section 8.2, pp.144--148, gives five nonlinear 4D maps: snake, codimension-one snake, short-side stretch, pinching, and double pinching. Guth says each map sends boundary to boundary, has degree 1, has 2-dilation \(<C\), and can be perturbed to a diffeomorphism.

The pinching idea relevant to the current draft is that the intermediate retraction may have large 2-dilation on a bad set, but a final Lipschitz pinch collapses that bad image to a lower-dimensional set, so the total composition has bounded 2-dilation. This is an upper-bound construction, not a lower-bound/tightening theorem. It supports the warning that near-optimal 4D rectangle maps are strongly nonlinear, but it does not prove the averaged estimate in `answer.tex`.

## arXiv:0710.0403

The source is `data/round26/arxiv_0710_0403_src/EXEMB2.TEX`.

Theorem 3, PDF pp.7--8 (`data/round26/arxiv_0710.0403_pages_07_08.txt`), gives the relative isoperimetric profile of a rectangle. If \(V\le c(n)R_1\cdots R_k\), write
\[
V=c(n)R_1\cdots R_j\rho^{k-j},\qquad R_j\le\rho\le R_{j+1};
\]
then
\[
I_R^k(V)\le C(n)R_1\cdots R_j\rho^{k-j+1}.
\]
In any case \(I_R^k(V)\le C(n)R_{k+1}V\). This is compatible with the small-cycle filling estimate used in the first alternative.

Estimate 1, PDF p.10 / source around `EXEMB2.TEX:656--665`, applies to maps of pairs:
\[
\Phi:(U,\partial U)\to(S,\partial S),\qquad U\subset R,
\]
of degree \(D>0\), and states
\[
\operatorname{dil}_k(\Phi)\ge
c(n)Q_1\cdots Q_j(Q_{j+1}\cdots Q_l)^{(k-j)/(l-j)}.
\]
Equivalently, for \(k\)-contracting degree-nonzero maps in the nontrivial case \(0<j<k<l\),
\[
\left({R_1\cdots R_j\over S_1\cdots S_j}\right)^{(l-k)/(k-j)}
R_1\cdots R_l\ge c(n)S_1\cdots S_l.
\]
For \(n=4,k=2,j=1,l=4\), this gives
\[
R_1^2\operatorname{Vol}(R)\gtrsim S_1^3S_2S_3S_4.
\]
This is the standard monomial obstruction in `answer.tex`; by itself it misses the desired hard-regime exponent.

Section 6, PDF pp.15--16 (`data/round26/arxiv_0710.0403_pages_15_18.txt`), is Guth's tightening construction for complexes of cycles. It gradually tightens chains in a cell complex, using rectangular isoperimetry and a homotopy lemma to preserve degree. This is important background, but it proves the monomial estimates above. I found no two-parameter averaged tightening statement there with a self-absorbing \((R_3R_4/S_3S_4)A\) error term.

## arXiv:0802.3549 and the missing preprint

The source is `data/round26/arxiv_0802_3549_src/LINKDIL2.TEX`.

On PDF p.5 / source around `LINKDIL2.TEX:384--400`, Guth discusses the 4D case \(n=4,k=k_1=k_2=k_3=2\). He then says that the analogous problem for the 2-dilation of mappings between 4-dimensional rectangles was solved in the preprint, that the answer is complicated, that near-optimal mappings are far from linear, and that the smallest 2-dilation of a degree-one diffeomorphism may be arbitrarily larger than that of a degree-one map.

The bibliography entry on PDF p.21 / source `LINKDIL2.TEX:1588--1590` is:

`Guth, L., On the 2-dilation of mappings between 4-dimensional rectangles, preprint.`

This is strong evidence that the missing item concerned **degree-one maps**, not only embeddings/diffeomorphisms. However, since I could not recover the preprint, I cannot certify the exact theorem statement, constants, side-length hypotheses, or whether its maps are stated as smooth, PL, piecewise smooth, or in some other category.

Theorem 3 of arXiv:0802.3549, PDF p.21, is for ellipses, not rectangles:
\[
\operatorname{Dil}_k(\Phi)>c(n)\left(|D|Q_{n-k_1+1}Q_{k_3}Q_1\cdots Q_n\right)^{k/(n+2)}.
\]
In the 4D \(k=2\) specialization this gives
\[
\operatorname{Dil}_2(\Phi)\gtrsim
|D|^{1/3}Q_1^{1/3}Q_2^{2/3}Q_3^{2/3}Q_4^{1/3}.
\]
It is not the desired rectangle dichotomy.

## Search status for the preprint

Fresh round-26 exact-title searches:

- arXiv exact and variant API queries: `totalResults=0`.
- DataCite exact title: zero data entries.
- Semantic Scholar: rate-limited (`429`) in this round; prior round searches also did not locate a copy.
- Crossref and OpenAlex: only unrelated/noisy titles, no Guth/2-dilation/4D rectangle candidate.
- Internet Archive advanced search: two false positives from an unrelated satellite-imagery repository.
- Wayback CDX for MIT and Stanford Guth pages: no recovered preprint URL.

So the preprint remains confirmed only bibliographically, not retrieved.

## Practical implication for `answer.tex`

What can be cited safely:

1. Guth thesis Proposition 8.1.3 for the first alternative, with the caveat that Guth states it for diffeomorphisms; the draft's extension to degree-one pair maps is a separate slicing-current argument.
2. arXiv:0710.0403 Estimate 1 for arbitrary degree-nonzero maps of pairs and the monomial lower bounds.
3. arXiv:0710.0403 Theorem 3 / thesis Proposition 8.1.2 for rectangular filling estimates.
4. arXiv:0802.3549 for the existence/citation of the missing preprint and for directional/rational-homotopy methods, not for the requested rectangle theorem.

What cannot be cited from the accessible documents:

- A complete theorem proving the hard-regime lower bound
\(\operatorname{Vol}(R)\gtrsim S_1S_2^{1/2}S_3^{3/2}S_4\) under \(R_1\ll S_1\) and \(R_3R_4\ll S_3S_4\).
- The proposed averaged estimate in `answer.tex`.
- A precise black-box statement for arbitrary piecewise smooth degree-one maps of pairs matching the problem.

My conclusion is that the desired theorem is very likely in Guth's missing preprint, and likely for degree-one maps rather than only diffeomorphisms, but the accessible literature does not provide a recoverable theorem statement or proof to quote.
