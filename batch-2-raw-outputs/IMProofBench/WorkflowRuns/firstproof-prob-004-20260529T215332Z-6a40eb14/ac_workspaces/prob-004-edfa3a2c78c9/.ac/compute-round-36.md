# Compute worker reply — round 36
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c0-d9fec4/compute_workspace_round_36.zip

---

# Round 36 literature/theorem retrieval report

Verdict: **found related but insufficient theorem**.  I located and inspected Guth's MIT thesis and the two relevant arXiv papers, but I did **not** locate a PDF/source copy of the cited unpublished preprint *On the 2-dilation of mappings between 4-dimensional rectangles*.  The thesis contains the relevant Chapter 8, but it explicitly presents only partial results for 4D rectangles, not the exact degree-one map theorem requested.

## Files saved

- `papers/round36/guth_area_contracting_thesis_mit_61207020.pdf`
  - MIT DSpace item: handle `1721.1/31158`, title *Area-contracting maps between rectangles*, Lawrence Guth, Ph.D. thesis, MIT, 2005.
  - DSpace bitstream: `61207020-MIT.pdf`, UUID `f3e1bda3-557c-4cc0-8244-6de14c095abd`, MD5 `788e2113627e3040d3a5a1c3cd32936b`, 208 pages.
  - Direct content URL from DSpace metadata: `https://dspace.mit.edu/server/api/core/bitstreams/f3e1bda3-557c-4cc0-8244-6de14c095abd/content`
- `papers/round36/guth_directional_isoperimetric_0802.3549.pdf`
  - arXiv:0802.3549, *Directional isoperimetric inequalities and rational homotopy invariants*.
- `papers/round36/guth_area_expanding_rectangles_0710.0403.pdf`
  - arXiv:0710.0403, *Area-expanding embeddings of rectangles*.
- Extracted text/images:
  - `data/round36/guth_thesis_full_layout.txt`
  - `data/round36/thesis_ch8_page-139.png` through `thesis_ch8_page-149.png`
  - `data/round36/arxiv_0802.3549_layout.txt`
  - `data/round36/arxiv_0710.0403_layout.txt`
- Search logs:
  - `data/round36/searches/`

## Thesis: exact Chapter 8 contents

Relevant source: Guth thesis, Chapter 8, "Partial Results On 2-Contracting Diffeomorphisms Between 4-Dimensional Rectangles", pp. 139-149.

The chapter is not a complete solution.  On p. 139 Guth says that for 2-dilation of diffeomorphisms between 4D rectangles, he is "not able to give a complete solution", and that Chapter 8 gives partial results.  The final remarks on p. 149 are stronger: the techniques are "not even close" to estimating the best 2-dilation in this case.

### Theorem 8.1, p. 139

Statement: for the **unit 4-cube** as domain, Guth gives a sharp-up-to-constants criterion:

`If there is a 2-contracting diffeomorphism from the unit 4-cube to S, then S_2 S_3^3 S_4^2 < C. Conversely, if S_2 S_3^3 S_4^2 < c, then there is such a diffeomorphism.`

Hypotheses: diffeomorphism, unit cube domain, side lengths ordered.  Constants `c,C` are unspecified absolute constants.  This is not the requested general rectangle theorem and not a map-of-pairs theorem.

### Proposition 8.1.1, p. 140

This is the closest-looking lower-bound statement, but it is for **ellipsoids/boundaries**, not 4D rectangles as maps of pairs.

Let `E` have axes `R_1 <= R_2 <= R_3 <= R_4` and `F` have axes `S_1 <= S_2 <= S_3 <= S_4`.  There is a 2-contracting diffeomorphism `E -> F` approximately iff:

- `B1. R_2 R_3 > S_2 S_3`.
- `B2. R_2^2 R_3 R_4 > S_2^2 S_3 S_4`.
- `B3a. If R_2^2 > S_2 S_3, then R_2 R_3 R_4 > S_2^{1/2} S_3^{3/2} S_4`.
- `B3b. If R_2^2 < S_2 S_3, then R_3 R_4 > S_3 S_4`.

This contains alternatives reminiscent of the hard case, especially `R_3 R_4 > S_3 S_4` and a `S_2^{1/2}S_3^{3/2}S_4` expression.  But the statement is for ellipsoid boundary inequalities induced by restricting a diffeomorphism to the boundary of a rectangle.  It has no `R_1`, no `S_1`, no volume alternative, and does not cover arbitrary degree-one maps of pairs.

### Proposition 8.1.3, p. 144

Statement:

`Suppose there is a 2-contracting diffeomorphism from R to S. If C R_1 R_2^2 < S_1 S_2 S_3, then R_3 R_4 > c S_3 S_4.`

Hypotheses: diffeomorphism `R -> S`; constants `c,C` absolute/unspecified.  Proof uses inverse images of coordinate 2-planes and the preceding isoperimetric estimate, Proposition 8.1.2.

This gives the first desired-looking alternative, but only under the extra hypothesis `C R_1 R_2^2 < S_1S_2S_3`.  It does not state the complementary volume alternative, and it is again for diffeomorphisms, not arbitrary degree-one maps of pairs.

### Section 8.2, pp. 144-148: upper constructions

Guth constructs five nonlinear degree-one maps between 4D rectangles.  The section starts by saying each map sends boundary to boundary, has degree 1, and has 2-dilation `< C`; after perturbation one can get diffeomorphisms with 2-dilation `< C`.

The two constructions most relevant to the missing preprint/the hard case:

- p. 146, "stretches the short side": degree-one map
  `R_1 x R_2 x R_3 x R_4 -> A R_1 x A^{-3}R_2 x A R_3 x A^{-1}R_4`,
  with `A >= 1`, `A < (R_2/R_1)^{1/4}`, `A < (R_4/R_3)^{1/2}`.  The technical remark also gives maps to `A R_1 x A^{-3}R_2 x A' x B` with `A^4 < R_2/R_1`, `R_3 < A' < (R_3R_4)^{1/2}`, and `R_3R_4=A'B`.
- pp. 147-148, "double pinching map": degree-one map
  `R_1 x R_2 x R_3 x R_4 -> R_1^2/A x A x A x B`,
  valid when `R_1 < A`, `A^2 < R_2R_3`, and `A^3B < R_1R_2R_3R_4`, with 2-dilation `< C`.

These are upper-bound constructions, not the requested lower-bound theorem.

## arXiv:0802.3549 clue to the missing preprint

In *Directional isoperimetric inequalities and rational homotopy invariants*, p. 5, Guth states that the analogous problem for 2-dilation of mappings between 4D rectangles "was recently solved in [3]" and says the answer is complicated: several cases, nonlinear near-optimal maps, and a gap between degree-one maps and degree-one diffeomorphisms.  The reference list identifies:

`[3] Guth, L., On the 2-dilation of mappings between 4-dimensional rectangles, preprint.`

This is the best secondary confirmation I found that the exact missing source existed and likely contained a full case analysis for **mappings**, not just diffeomorphisms.  However, arXiv:0802.3549 does not state the 4D rectangle theorem or the case alternatives.

## arXiv:0710.0403 related but insufficient

In *Area-expanding embeddings of rectangles*, Estimate 1 in Section 2 states: for `U` open in `R` and a map of pairs `(U, boundary U) -> (S, boundary S)` of degree `D>0`,

`dil_k(Phi) >= c(n) Q_1...Q_j (Q_{j+1}...Q_l)^{(k-j)/(l-j)}`

for `0 <= j < k <= l <= n`, with `Q_i=S_i/R_i`.

This is useful because it has the map-of-pairs/degree hypothesis rather than diffeomorphisms.  But specializing to `n=4,k=2` does not yield the requested dichotomy
`R_3R_4 \gtrsim S_3S_4` or
`Vol(R) \gtrsim S_1 S_2^{1/2}S_3^{3/2}S_4`
under `R_1 <= kS_1`; it gives only the broader product/quotient lower bounds.

## Search status for the unpublished preprint

I did not find a downloadable copy of *On the 2-dilation of mappings between 4-dimensional rectangles*.

Search artifacts saved in `data/round36/searches/`:

- arXiv API:
  - exact title query: `totalResults=0`.
  - `Guth 2-dilation` query: `totalResults=0`.
- Internet Archive advanced search:
  - exact title: `numFound=0`.
  - `smallest 2-dilation Guth rectangles`: `numFound=0`.
- Wayback CDX probes:
  - URL/title patterns involving `2-dilation rectangles`, `guth dilation rectangle`, and `lguth dilat`: zero rows.
- Crossref/OpenAlex/DataCite:
  - no exact-title match; broad queries returned irrelevant records.
- Semantic Scholar API:
  - rate-limited with HTTP/API 429 during this round, so no reliable new result there.
- Current MIT author/profile pages and an attempted MIT CV URL:
  - no located preprint link; the apparent CV URL returned site JavaScript/HTML rather than the old PDF.
- Bing exact-title pages:
  - no academic/preprint hit in the first result page; exact title query was swamped by irrelevant "On" results.

Older search artifacts already in the workspace (`data/round17/`, etc.) agree with this: exact-title web searches and bibliographic searches found citations to the thesis but not the unpublished 4D preprint itself.

## Bottom line for the Author

The exact problem statement does **not** follow as a stated theorem/corollary from the located MIT thesis.  The thesis provides:

- a cube-domain theorem (Theorem 8.1);
- ellipsoid/boundary inequalities with similar alternatives (Proposition 8.1.1);
- a conditional rectangle diffeomorphism lower bound giving `R_3R_4 > cS_3S_4` (Proposition 8.1.3);
- several upper constructions by degree-one boundary-to-boundary maps (Section 8.2).

The missing preprint is still the likely source for the full theorem on degree-one mappings between 4D rectangles, because arXiv:0802.3549 explicitly says that problem was solved there and distinguishes mappings from diffeomorphisms.  But I found no source copy and no secondary document that states the exact dichotomy with theorem number/constants.
