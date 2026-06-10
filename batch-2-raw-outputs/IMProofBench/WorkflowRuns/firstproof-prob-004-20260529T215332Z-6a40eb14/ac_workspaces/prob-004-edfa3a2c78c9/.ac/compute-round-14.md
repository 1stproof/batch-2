# Compute worker reply — round 14
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c3-89f310/compute_workspace_round_14.zip

---

# Round 14 compute report: HAF status

## 1. Targeted search for Guth's 4D preprint

I did **not** locate a copy of Larry Guth, *On the 2-dilation of mappings between 4-dimensional rectangles*, preprint.

Refreshed checks this round:

- Exact web searches for the title and variants.
- arXiv exact-title API: `data/round14/arxiv_exact_title.xml`, with `opensearch:totalResults=0`.
- Crossref/OpenAlex/DataCite/Internet Archive metadata:
  `data/round14/crossref_title.json`,
  `data/round14/openalex_title.json`,
  `data/round14/datacite_title.json`,
  `data/round14/archive_exact_title.json`.
  None gives a plausible match; Crossref/OpenAlex only return unrelated noisy results.
- Internet Archive CDX for old Stanford/MIT/NYU Guth pages:
  `data/round14/cdx_math_stanford_lguth.json`,
  `data/round14/cdx_www_math_stanford_lguth.json`,
  `data/round14/cdx_math_mit_lguth.json`,
  `data/round14/cdx_math_nyu_lguth.json`.
  The only old Stanford PDFs found were course notes/handouts:
  `papers/round14/archive_stanford_finprep_20060718.pdf` and
  `papers/round14/archive_stanford_estimate_20060718.pdf`; they are unrelated.
- Current MIT page `data/round14/current_mit_lguth.html` says Guth's papers are on arXiv; no current page hit for the missing preprint.

The exact citation still only appears in Guth's arXiv source for *Directional isoperimetric inequalities and rational homotopy invariants*, `data/round13/directional_src/LINKDIL2.TEX`:

```tex
\bibitem{G4} Guth, L., On the 2-dilation of mappings between 4-dimensional rectangles, preprint.
```

The same paper states that the analogous problem for 2-dilation between 4D rectangles was recently solved in that preprint, that the answer is complicated, that near-optimal maps are far from linear, and that the minimum among degree-one diffeomorphisms can be larger than among degree-one maps. See `data/pdftxt/guth_directional_isoperimetric_0802.3549.txt`, lines 232--237.

Verdict on the source question: the original theorem may well be a corollary of the unavailable preprint, but I found no extractable theorem/proof and no evidence that HAF itself appears in any available Guth source. Do not cite HAF as Guth without obtaining the preprint.

## 2. Exponent and construction checks

New reproducible script: `code/round14_haf_checks.py`.
Output: `data/round14/haf_checks.txt`.

### Prompt hard model

\[
S=(1,1,L,L),\qquad
R=(L^{-1/5},L^{13/15},L^{13/15},L^{13/15}).
\]

Scaling checks:

| quantity | exponent |
|---|---:|
| \(R_1/S_1\) | \(-1/5\) |
| \(R_3R_4/(S_3S_4)\) | \(-4/15\) |
| \(\Vol(R)\) | \(12/5\) |
| \(T=S_1S_2^{1/2}S_3^{3/2}S_4\) | \(5/2\) |
| \(\Vol(R)/T\) | \(-1/10\) |
| first-alternative margin \(R_1R_2^2/(S_1S_2S_3)\) | \(8/15\) |
| best affine/permuted linear \(2\)-dilation exponent \(R\to S\) | \(1/3\) |

Thus this model saturates the current lower bound
\[
\Vol(R)\gtrsim \alpha^{1/2}T,\qquad \alpha=R_1/S_1,
\]
because \(\alpha^{1/2}T\) has exponent \(12/5\). It also saturates Guth's
\(j=1,k=2,l=4\) monomial estimate:
\[
R_1^3R_2R_3R_4 \gtrsim S_1^3S_2S_3S_4
\]
with exponent margin \(0\). But it is **not** an affine counterexample: any coordinate-permuted affine map has \(\Dil_2\sim L^{1/3}\).

Bounded Guth Chapter 8.2 route search on this model, using the corrected snake / codimension-one snake / short-side stretch / pinching / double-pinching exponent rules:

```text
step=1/5 depth=2 beam=1000: not found
searched 2517 states
```

This is not a proof of nonexistence, but it found no actual map of pairs behind the exponent model.

### Older stress model

\[
S=(1,1,L^6,L^6),\qquad R=(L^{-1},L^4,L^5,L^6).
\]

Scaling checks:

| quantity | exponent |
|---|---:|
| \(R_1/S_1\) | \(-1\) |
| \(R_3R_4/(S_3S_4)\) | \(-1\) |
| \(\Vol(R)\) | \(14\) |
| \(T=S_1S_2^{1/2}S_3^{3/2}S_4\) | \(15\) |
| \(\Vol(R)/T\) | \(-1\) |
| first-alternative margin \(R_1R_2^2/(S_1S_2S_3)\) | \(1\) |
| best affine/permuted linear \(2\)-dilation exponent \(R\to S\) | \(2\) |

Guth monomial estimates are all satisfied; again \(j=1,k=2,l=4\) is exactly saturated. A fresh coarse search found no short route:

```text
step=1 depth=3 beam=1000: not found
searched 3224 states
```

Prior deeper searches are stronger: `data/round11_guth_ch8_stress_search_deeper.txt` searched the same stress family with corrected Chapter 8.2 moves:

```text
step=1 depth=5 beam=2000: not_found, searched 16939 states
step=1/2 depth=5 beam=2500: not_found, searched 39483 states
step=1/4 depth=4 beam=2500: not_found, searched 89136 states
```

### Affine/permutation maps

The LP in `code/round14_haf_checks.py` maximizes a common positive exponent margin by which all three desired alternatives fail, over coordinate-permuted diagonal affine maps satisfying \(\Dil_2\le1\). Result:

```text
best common failure margin = 0
Conclusion: no positive-margin hard-regime affine/permutation counterexample.
```

So affine maps do not threaten the theorem/HAF.

### Formal laminate/minor models

The formal diagonal compound-matrix model from round 13 remains a warning:
`code/round13_directional_model.py`, output `data/round13/directional_model_output.txt`.
It satisfies degree-volume, \(\|\Lambda^2df\|\le1\), Plucker/conformal relations, and all six integrated directional inequalities at the exponent level while still sitting at the bad volume scale. But it ignores boundary/side-spanning constraints and is not an actual map of pairs. It shows only that directional absolute-minor bookkeeping cannot prove HAF.

## 3. HAF in simplified settings

The hard-regime averaged filling estimate in the draft is
\[
A\le C\left(R_1I+\frac{I^2}{S_1|Q|}\right)
  +C\frac{R_3R_4}{S_3S_4}A. \tag{HAF}
\]

I found no counterexample to HAF under both hard hypotheses
\[
R_1\ll S_1,\qquad R_3R_4\ll S_3S_4.
\]
However, HAF is not a consequence of any currently validated estimate in `answer.tex`.

What is rigorously available:

- PL transversality/cubical slicing gives the cycle complex \(y\mapsto Z_y\) and weighted coarea
  \[
  I=\int_Q\int_{Z_y}\lambda^2\le \Vol(R).
  \]
- The target calibration gives
  \[
  A=\int_Q\Fill_R(Z_y)\,dy \gtrsim S_1S_2S_3|Q|.
  \]
- For almost-minimizing fillings \(B_y\), the random-puncture bad-mass average is valid:
  \[
  {1\over |Q|}\int_Q\int_Q \Mass(B_y\cap\mathcal B_z)\,dy\,dz
  \lesssim {R_3R_4\over S_3S_4}A.
  \]
  This is the source of the self-absorbing term.

Where the other two terms should come from in any proof:

- \(R_1I\): good pieces of the fillings should be pushed or coned in the short \(x_1\)-direction, with cost \(R_1\) times the weighted \(G=(f_1,f_2)\)-energy on the degree-carrying slice complex.
- \(I^2/(S_1|Q|)\): after slicing in the \(f_1\)-direction, seams/caps should be controlled by a coarea/Jensen optimization over an \(S_1\)-long parameter, producing a quadratic cost in the total energy \(I\).
- \((R_3R_4/S_3S_4)A\): filling mass lying over vertical source rectangles whose \(F=(f_3,f_4)\)-image hits a chosen puncture cannot be tightened cheaply; averaged over punctures, this mass is at most the displayed fraction of \(A\).

The unproved step is a genuine lifting/deformation lemma: on the good set, one must turn punctured-parameter triviality into a controlled source filling. The previous random-puncture lemma failed precisely because puncturing \(Q\) does not by itself kill large vertical relative sheets in the source. Known counterexamples to the naive lemma either have \(R_3R_4\gtrsim S_3S_4\) or \(R_1\sim S_1\), so they do not disprove hard-regime HAF, but they rule out any universal black-box version.

For maps where \(F\) has extra controlled vertical-image lift data, HAF looks provable by the above skeleton. Mere small area or point-avoidance of \(F(V_u)\) is not enough; the lift/control hypothesis must explicitly prevent the round-12 vertical-sheet counterexample. For central fibers close to the \(A^2/R_1\) branch of the rectangular profile, a single-fiber proof cannot work: such fibers can have large filling and low \(G\)-energy. The family-level compatibility over \(Q\), plus \(R_3R_4\ll S_3S_4\), is exactly the missing ingredient.

## 4. Verdict and recommendation

My verdict:

- **Not found / not safely citeable as Guth:** the unavailable preprint is cited and likely contains a full complicated 4D answer, but no source statement was recovered. HAF is not present in the available thesis/arXiv materials.
- **Not false by any actual construction found:** affine maps, coordinate permutations, and corrected Chapter 8.2 exponent compositions produced no hard-regime counterexample map. The bad examples are formal exponent/laminate models or counterexamples to overbroad lemmas outside the hard regime.
- **Not currently provable from the draft reductions:** directional isoperimetry, Plucker identities, and monomial estimates all allow the stress scalings. HAF requires a new parametric/topological deformation theorem.

Recommended next author move: do **not** present HAF as established. Either (a) attempt one final precise proof of a **weakened hard-regime HAF** with explicit PL/cubical hypotheses and a lifting lemma for the good set, or (b) abandon this route and state the current result as a sharp reduction plus conjectural missing estimate. If the proof is attempted, the key lemma must directly produce the \(R_1I\), \(I^2/(S_1|Q|)\), and self-absorbing bad-mass terms; manipulating the existing absolute-minor inequalities will not close the exponent gap.
