# Compute worker reply — round 28
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c2-438277/compute_workspace_round_28.zip

---

# Round 28 literature/proof search: 4D rectangle 2-dilation

## Bottom line

I did **not** find a public copy of Guth's cited preprint *On the 2-dilation of mappings between 4-dimensional rectangles*. The available public sources confirm that such a preprint was cited by Guth, but they do **not** contain the missing exact proof needed to close the current LE-HAF gap in `answer.tex`.

The thesis gives only **partial results** for 4D rectangles. In particular:

- It proves a useful lower bound of the form `R_3 R_4 >= c S_3 S_4` only under an extra hypothesis roughly `C R_1 R_2^2 < S_1 S_2 S_3` (OCR drops exponents in places; the proof and Proposition 8.1.2 show the `R_2^2` scale).
- It proves boundary/ellipsoid inequalities including the `S_2^{1/2} S_3^{3/2} S_4` expression, but these are for boundaries/ellipsoids/diffeomorphisms and do not give the desired rectangle pair theorem with the missing `S_1/R_1` factor.
- Guth explicitly says near the end of Chapter 8 that the thesis techniques are "not even close" to estimating the best 2-dilation of diffeomorphisms between 4D rectangles.

So my recommendation is: **do not update `answer.tex` by claiming the exact theorem follows from the thesis or from arXiv:0710.0403/0802.3549/0802.3550.** The current LE-HAF step remains the actual gap unless the unpublished preprint is obtained.

## Files downloaded / saved

Manifest with sizes and MD5s: `data/round28_lit/download_manifest.tsv`.

| item | path | bytes | md5 |
|---|---:|---:|---|
| Guth thesis PDF | `papers/guth_area_contracting_thesis_2005.pdf` | 12365750 | `788e2113627e3040d3a5a1c3cd32936b` |
| arXiv 0710.0403 PDF | `papers/arxiv_0710.0403.pdf` | 262150 | `9c42df2ea074a4d3a986abe422eddff5` |
| arXiv 0802.3549 PDF | `papers/arxiv_0802.3549.pdf` | 256530 | `0d21289029a1c674d6f7dca1bd24ae07` |
| arXiv 0802.3550 PDF | `papers/arxiv_0802.3550.pdf` | 195698 | `4d5f2861d638af612dcdbcf03ef0c43c` |
| arXiv 0710.0403 source | `papers/arxiv_0710.0403_source.tar.gz` | 39833 | `0c06f33cb41a64da74d32ca63f9bf681` |
| arXiv 0802.3549 source | `papers/arxiv_0802.3549_source.tar.gz` | 25628 | `5ee85f112af7e5b3f68223e1f56dc8c3` |
| arXiv 0802.3550 source | `papers/arxiv_0802.3550_source.tar.gz` | 23277 | `34e9b2d6530bb910b66fd7b0aad162db` |

Extracted/searchable text:

- `data/round28_lit/Guth_thesis_pdftotext_layout.txt`
- `data/round28_lit/Guth_thesis_DSpace_extracted_text.txt`
- `data/round28_lit/arxiv_0710.0403.txt`
- `data/round28_lit/arxiv_0802.3549.txt`
- `data/round28_lit/arxiv_0802.3550.txt`
- Full term hit log: `data/round28_lit/search_hits.md`
- Preprint citation grep: `data/round28_lit/preprint_citation_grep.log`
- Scalar formula grep: `data/round28_lit/scalar_formula_grep.log`
- Search script: `code/round28/search_lit.py`

MIT DSpace notes:

- The handle page and REST metadata were saved under `data/round28_lit/mit_*`.
- The thesis item UUID is `cadf67f7-db0a-4bb0-b804-b27e1d462e55`.
- The original PDF bitstream UUID is `f3e1bda3-557c-4cc0-8244-6de14c095abd`, filename `61207020-MIT.pdf`.
- Normal MIT PDF bitstream download was blocked/challenged during this round, but the local PDF already present in `papers/` matches MIT DSpace metadata by MD5 (`788e2113627e3040d3a5a1c3cd32936b`), so I treated it as the authoritative thesis PDF.

## Search result summary by source

### Guth thesis, `papers/guth_area_contracting_thesis_2005.pdf`

Relevant chapter: Chapter 8, "Partial Results On 2-Contracting Diffeomorphisms Between 4-Dimensional Rectangles" (PDF text page 139 in `data/round28_lit/search_hits.md`).

Important hits:

- PDF pp. 140-142: Proposition 8.1.1 gives boundary/ellipsoid inequalities. The key ones are:
  - `B3a`: in the OCR, "If R > S_2 S_3, then R_2 R_3 R_4 > S_2^{1/2} S_3^{3/2} S_4" (the missing exponent is on `R_2`; context is the case `R_2^2 > S_2 S_3`).
  - `B3b`: if `R_2^2 < S_2 S_3`, then `R_3 R_4 > c S_3 S_4`.
- PDF pp. 143-144: Proposition 8.1.2 is the small-area relative 2-cycle filling estimate in a rectangle. It is the local isoperimetric input.
- PDF p. 144: Proposition 8.1.3 proves that if there is a 2-contracting diffeomorphism `R -> S` and the extra filling-scale hypothesis holds, then `R_3 R_4 > c S_3 S_4`.
- PDF pp. 144-148: five upper-bound constructions: snake map, codimension-one snake, short-side stretch, pinching, double pinching. These are useful for understanding the case structure but are not a lower-bound proof of the desired theorem.
- PDF p. 149 / extracted text line 4863: Guth says the thesis techniques are "not even close" to estimating the best 2-dilation between 4D rectangles.

Assessment: Chapter 8 is useful background and proves the first alternative in a restricted case, but it is not the missing theorem. The boundary/ellipsoid `S_2^{1/2} S_3^{3/2} S_4` inequality cannot be transplanted directly to the desired rectangle degree-one map statement because it lacks the `S_1` dependence and is proved for boundary ellipsoids/diffeomorphisms.

### arXiv:0710.0403, `papers/arxiv_0710.0403.pdf`

Source file: `papers/arxiv_0710.0403_source_dir/EXEMB2.TEX`.

Important hit:

- `EXEMB2.TEX` lines 867-875: Estimate 1, for a `k`-contracting map from `U subset R` to `S` of nonzero degree, gives
  ```
  [(R_1 ... R_j)/(S_1 ... S_j)]^((l-k)/(k-j)) R_1 ... R_l
    >= c(n) S_1 ... S_l
  ```
  for `0 < j < k < l`.

Assessment: This is exactly the monomial estimate already known in the notes. It supports the weaker monomial route but does not prove the exact 4D rectangle alternative or LE-HAF.

### arXiv:0802.3549, `papers/arxiv_0802.3549.pdf`

Source file: `papers/arxiv_0802.3549_source_dir/LINKDIL2.TEX`.

This is the strongest evidence that the missing preprint exists:

- `LINKDIL2.TEX` lines 392-399 says the analogous problem for "the 2-dilation of mappings between 4-dimensional rectangles" was recently solved in citation `[G4]`, that the answer is complicated, and that degree-one diffeomorphisms may require arbitrarily larger 2-dilation than degree-one maps.
- `LINKDIL2.TEX` line 1590 cites:
  ```
  Guth, L., On the 2-dilation of mappings between 4-dimensional rectangles, preprint.
  ```
- The same appears in the extracted PDF text at page 21; see `data/round28_lit/preprint_citation_grep.log`.

Assessment: This paper confirms the cited result but does not reproduce the theorem/proof. It is not enough to fill the proof gap.

### arXiv:0802.3550, `papers/arxiv_0802.3550.pdf`

I found no exact 4D rectangle theorem or citation to the missing preprint in the searched text/source. It is mainly relevant for rational homotopy/isoperimetry background, not the present theorem.

## Missing preprint search

I tried these routes and saved logs where possible:

- MIT DSpace handle/API and bitstream metadata for `1721.1/31158`.
- `hdl.handle.net` / MIT mirror-style paths.
- Internet Archive metadata/advanced search for the thesis/preprint title.
- arXiv API exact title search for the preprint.
- OpenAlex exact title search.
- Larry Guth MIT homepage mirror/index checks.
- Broad web searches for the exact title and variants.

I found only the citation in arXiv:0802.3549, not the preprint PDF/source.

Saved API/log files include:

- `data/round28_lit/arxiv_api_2dilation_rectangles.xml` (`totalResults=0`)
- `data/round28_lit/openalex_2dilation_rectangles_exact.json` (`count=0`)
- `data/round28_lit/internet_archive_search_*.json`
- `data/round28_lit/semanticscholar_2dilation_rectangles.json` (rate-limited/429)
- `data/round28_lit/lguth_home.html`

## LE-HAF / no-flap probe

I wrote a separate note: `data/round28_lit/le_haf_no_flap_probe.md`.

The useful point is that the no-flap case has a clean chain-algebra formulation. Let `Z=Z_y`, and let `B=B_y` be a near-minimizing relative 3-filling of `Z`. Choose a cubulation `K_theta`. If, for a puncture `z`, we can construct a relative chain map
```
P_z : C_*(K_theta) -> C_*(partial R) + C_*(bad cells for z)
```
and a chain homotopy `H_z` from the identity to `P_z`,
```
partial H_z + H_z partial = P_z - Id,
```
then, since `Z=partial B`,
```
partial{P_z(B)-H_z(Z)} = -Z
```
in relative chains. Hence
```
C_{y,z} = H_z(Z) - P_z(B)
```
fills `Z`. If `P_z` sends all good 3-cells into `partial R`, only bad cells of `B` survive in `P_z(B)`, so
```
Mass C_{y,z} <= Mass H_z(Z_y)
                + Mass(B_y restricted to bad cells).
```

Thus in the no-flap case, where `B_y` avoids bad cells, the desired filling is simply `C=H_z(Z_y)`. This avoids the uncontrolled seam term from the earlier sharp-cut argument.

What is still missing:

1. A construction of `P_z,H_z` with
   ```
   Mass H_z(Z_y) <= C (R_1 E_y + E_y^2/S_1).
   ```
   A pointwise push of all of `Z_y` cannot work, because low-`G`-energy flaps can have large ordinary mass. The homotopy must ignore null-homologous flaps or charge only the degree-carrying part of `G_# Z_y`.

2. An averaged bad-cell bound
   ```
   E_{z,theta} Mass(B_y restricted to bad cells)
     <= C (R_3 R_4)/(S_3 S_4) Mass B_y.
   ```
   This is plausible for exact coordinate 2-plaque tracks because each coordinate plaque has `F`-image area at most `R_i R_j <= R_3 R_4`. It is not automatically stable under thickened/near-miss cells: rank-one oscillation can make a small-area image have a large neighborhood in `Q`.

So the no-flap chain algebra is sound, but the geometric construction of a cellular punctured Manhattan projection with exact-plaque badness and the required energy homotopy bound remains the unresolved LE-HAF step.

## Suggested update to `answer.tex`

I would update next round as follows:

1. Add a literature remark: public sources found in this round do not contain the exact 4D rectangle theorem. arXiv:0802.3549 cites the missing preprint, but the proof itself was not located.
2. Keep the thesis-derived restricted alternative as background only: Guth thesis Chapter 8, Proposition 8.1.3 proves `R_3 R_4 >= c S_3 S_4` under an additional filling-scale hypothesis, not in full generality.
3. Do not assert that the boundary ellipsoid Proposition 8.1.1 proves the volume alternative for degree-one rectangle maps.
4. Move the LE-HAF no-flap chain-map formulation into `research_notes.tex` as the best current proof skeleton. It is cleaner than the sharp-cut chain comparison, but should be labelled as a gap until `P_z,H_z` and the averaged bad-cell estimate are actually constructed.
