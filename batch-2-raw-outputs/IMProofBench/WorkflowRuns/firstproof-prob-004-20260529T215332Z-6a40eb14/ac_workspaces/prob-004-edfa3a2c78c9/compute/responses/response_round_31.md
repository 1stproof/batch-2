# Round 31 literature/proof retrieval: Guth 2-dilation rectangles

## Files downloaded/extracted

New round-specific downloads are in `papers/round31/`:

| file | source |
|---|---|
| `guth_area_contracting_thesis_mit_61207020.pdf` | MIT DSpace item `1721.1/31158`, bitstream `61207020-MIT.pdf` |
| `guth_area_expanding_rectangles_0710.0403.pdf`, `*_src.tar` | arXiv:0710.0403 |
| `guth_directional_isoperimetric_0802.3549.pdf`, `*_src.tar` | arXiv:0802.3549 |
| `guth_isoperimetric_rational_0802.3550.pdf`, `*_src.tar` | arXiv:0802.3550 |
| `guth_width_volume_math0609569.pdf`, `*_src.tar` | arXiv:math/0609569 |
| `guth_cv_2024_08_26.pdf` | current MIT CV, for a check of listed publications |

Extracted TeX/text is under `data/round31/src_*`, `data/round31/text/`, and selected page excerpts under `data/round31/pages/`.
Search/API logs are in `data/round31/searches/`.

## Search result for the exact preprint

I did **not** locate a PDF/TeX copy of Guth's cited preprint *On the 2-dilation of mappings between 4-dimensional rectangles*.

What I checked:

- Web search for exact and approximate titles found only adjacent Guth papers, not the preprint copy.
- arXiv API variant query `"2-dilation of mappings between 4-dimensional rectangles"` returned `totalResults=0`; the exact query timed out this round, but the previous exact arXiv API result in `data/round26/arxiv_exact_missing.xml` also has `totalResults=0`.
- Crossref, DataCite, and OpenAlex searches did not return an exact bibliographic record. DataCite returned total 0; Crossref/OpenAlex top hits were unrelated. See `data/round31/searches/{crossref_exact,datacite_exact,openalex_exact}.*`.
- Wayback CDX URL inventories for Guth's old MIT/Stanford pages did not reveal a plausibly named PDF/TeX. The old Stanford `estimate.pdf` and `finprep.pdf` files are unrelated course notes; text extracted at `data/round31/text/archive_stanford_*.txt`.
- Guth's current MIT CV lists "Area-expanding embeddings of rectangles, preprint" but not this exact 2-dilation preprint; see `data/round31/text/guth_cv_2024_08_26.txt`, around publication item 9.

The exact title is nevertheless real: arXiv:0802.3549 cites it in the references as
`[3] Guth, L., On the 2-dilation of mappings between 4-dimensional rectangles, preprint.`
This is on p.21 of the PDF (`data/round31/pages/0802_pages_20_21.txt`).

## What the accessible sources say

### 1. arXiv:0802.3549 explicitly says the missing preprint solved the degree-one map problem

On p.5 of *Directional isoperimetric inequalities and rational homotopy invariants*, Guth states:

> "The analogous problem for the 2-dilation of mappings between 4-dimensional rectangles was recently solved in [3]..."

The next sentences say the answer is complicated and, importantly, distinguish maps from diffeomorphisms:

> "the smallest 2-dilation of a degree 1 diffeomorphism may be larger than the smallest 2-dilation of a degree 1 map by an arbitrary factor."

This is strong evidence that the lost preprint treats arbitrary degree-one maps, not only embeddings/diffeomorphisms. But the cited preprint itself was not located, so I cannot quote its theorem statement or proof.

### 2. arXiv:0710.0403 has a theorem for arbitrary maps of pairs, but only monomial estimates

In *Area-expanding embeddings of rectangles*, p.10, "Estimate 1" states:

> Suppose that `U` is an open set in `R` and `Phi` is a map of pairs `(U, dU) -> (S, dS)` of degree `D > 0`. Suppose `0 <= j < k <= l <= n`. Then  
> `dil_k(Phi) >= c(n) Q_1...Q_j (Q_{j+1}...Q_l)^((k-j)/(l-j))`.

Immediately after, Guth says this is "slightly more general because `Phi` need not be a diffeomorphism." Thus this theorem does apply beyond embeddings/diffeomorphisms, to degree-positive maps of pairs. Boundary hypothesis: map of pairs to `(S, ∂S)`, with degree in relative homology. Source: `data/round31/src_0710.0403/EXEMB2.TEX`, lines 656-672; page excerpt `data/round31/pages/0710_pages_08_11.txt`.

However, this is not the desired mixed estimate. It gives only the known monomial lower bounds. I found no occurrence of a term equivalent to
`S_1 S_2^{1/2} S_3^{3/2} S_4`
or the mixed three-term estimate in 0710.0403, 0802.3549, 0802.3550, or the thesis text.

The references of 0710.0403 do not cite the exact missing preprint; they cite the thesis, width-volume, minimax/cup-powers, etc. See `data/round31/src_0710.0403/EXEMB2.TEX`, lines 1537-1546.

### 3. Guth thesis Chapter 8 is about diffeomorphisms, not arbitrary maps

The thesis Chapter 8 title is "Partial Results On 2-Contracting Diffeomorphisms Between 4-Dimensional Rectangles" (p.139). It explicitly says Guth is not giving a complete solution there.

Useful lower bounds:

- Proposition 8.1.1, pp.140-142, is for a `2-contracting diffeomorphism` between ellipsoid boundaries. It includes:
  - `B3a`: if the appropriate short-scale condition holds, then roughly  
    `R_2 R_3 R_4 > c S_2^{1/2} S_3^{3/2} S_4`;
  - `B3b`: otherwise `R_3 R_4 > c S_3 S_4`.
- Proposition 8.1.3, p.144, states: if there is a `2-contracting diffeomorphism` from `R` to `S` and `C R_1 R_2^2 < S_1 S_2 S_3`, then `R_3 R_4 > c S_3 S_4`.

These arguments use inverse images under diffeomorphisms, boundary diffeomorphism information, transverse area increase, and filling-volume preservation. I do not see a statement in the thesis extending them to arbitrary degree-one maps of pairs.

Useful upper constructions:

- Section 8.2, p.144, says its five non-linear maps between 4-rectangles "take the boundary of the domain to the boundary of the range, have degree 1, and have 2-dilation less than C"; it then says they can be slightly perturbed to diffeomorphisms.
- The short-side stretch map and technical remark are on p.146.
- The pinching map is on p.147, with conditions `R_1 > A` and `R_2 R_3 R_4 > A^2 B`; the mechanism collapses the large-2-dilation region to a line.

These are constructions, not the missing lower-bound theorem.

### 4. Directional/rational-homotopy papers do not replace the missing plaque lemma

arXiv:0802.3549 contains a genuine directional isoperimetric estimate.

- p.10 states a "Directional Isoperimetric Inequality in an Ellipse" bounding directional volumes of a filling.
- Proposition 2.2, p.12, is the rectangle relative-cycle version: for a relative integral cycle `z` in a rectangle, there is `y` with `∂y = z + B`, `B ⊂ ∂R`, and directional estimates for `y` and some directional volumes of `B`.
- But Guth explicitly notes the limitation: if the index tuple `J` includes `1`, he proves no upper bound on `Vol_J(B)`.

The same paper's Theorem 3 gives a degree-`D` lower bound for maps between ellipses. In dimension `n=4`, `k=k_1=k_2=k_3=2`, p.5 gives
`Dil_2(Phi) >= c |D|^{1/3} Q_1^{1/3} Q_2^{2/3} Q_3^{2/3} Q_4^{1/3}`.
This is useful but still a monomial/rational-homotopy estimate for ellipses, not the mixed rectangle estimate.

arXiv:0802.3550 gives the earlier first-order rational-homotopy/ellipse estimate. Proposition 7.1 on p.14 is again an ellipsoid-to-ellipsoid degree-`D` lower bound, not a 4-rectangle mixed plaque theorem.

Conclusion: these directional estimates are adjacent technology and may inform a proof, but I did not find a ready substitute for the missing exact-plaque lemma or the mixed estimate.

## Bottom line for the user's theorem

I cannot give a source-backed corollary proof of the user's theorem from the located documents. The only source that appears to contain the needed complete 4-dimensional degree-one map result is the missing Guth preprint cited in arXiv:0802.3549, and I could not locate its text.

What can be cited safely:

1. arXiv:0710.0403, Estimate 1, p.10: applies to arbitrary degree-positive maps of pairs, not just diffeomorphisms, but gives only monomial bounds.
2. Guth thesis, Chapter 8, pp.139-149: gives partial 4D diffeomorphism lower bounds and degree-one snake/pinching constructions, but not a complete arbitrary-map theorem.
3. arXiv:0802.3549, p.5 and p.21: confirms the exact missing preprint existed and apparently solved the degree-one map problem, while distinguishing degree-one maps from degree-one diffeomorphisms.
4. arXiv:0802.3549/0802.3550 directional/rational-homotopy estimates: no direct replacement for the mixed rectangle estimate.

So the proof should not currently cite the mixed estimate as an established theorem unless the missing preprint is obtained from Guth or another archive.
