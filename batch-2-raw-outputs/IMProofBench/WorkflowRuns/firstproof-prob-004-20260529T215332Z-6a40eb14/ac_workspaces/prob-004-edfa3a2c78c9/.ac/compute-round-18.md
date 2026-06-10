# Compute worker reply — round 18
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c2-a313e0/compute_workspace_round_18.zip

---

# Round 18 report: estimate (13) / low-energy HAF

## Bottom line

I could not prove estimate (13).  I also did not find a hard-regime counterexample.  The most useful output from this round is a precise diagnosis of where the proposed “weighted Manhattan deformation” proof first breaks: the local coordinate-track estimate needed to pay track mass by \(R_1E_y\) plus averaged plaque-bad mass is false, even under the pointwise \(2\)-dilation constraint.  This does **not** disprove (13), but it rules out the straightforward local proof strategy.

Files produced:

- `code/round18_local_track_obstruction.py`
- `data/round18_local_track_obstruction.txt`
- `data/round18_guth_hard_scan.txt`

## Current notation checked

I read the current `answer.tex` and the relevant `research_notes.tex` entries.  The target estimate is
\[
 \int_\Omega\Fill_R(Z_y)\,dy
 \le C\int_\Omega\left(R_1E_y+\frac{E_y^2}{S_1}\right)dy
      +\frac{C}{q}\int_Q\int_\Omega
        \Mass(B_y\llcorner\mathcal B_z)\,dy\,dz . \tag{13}
\]
Here \(F=(f_3,f_4)\), \(G=(f_1,f_2)\), \(Z_y=\langle [R,\partial R],F,y\rangle\),
\[
E_y=\int_{Z_y}\lambda^2\,d\|Z_y\|,\qquad
\lambda=\|dG|_{\ker dF}\|,\qquad I=\int_QE_y\,dy,
\]
\(q=|Q|\sim S_3S_4\), \(\Omega=\{y:E_y\le 4I/q\}\), and
\[
\mathcal B_z=\{x\in R:\ z\in F(P_{ij}(x))\hbox{ for some coordinate }2\hbox{-plaque }P_{ij}(x)\}.
\]
The all-coordinate plaque Fubini estimate in `answer.tex` is correct:
\[
 {1\over q}\int_Q\int_\Omega\Mass(B_y\llcorner\mathcal B_z)\,dy\,dz
 \lesssim {R_3R_4\over S_3S_4}\int_\Omega\Fill_R(Z_y)\,dy,
\]
using the near-minimizing choice \(\Mass B_y\le2\Fill_R(Z_y)\).

## What a successful Manhattan proof would have to do

For fixed \(z\), one wants to fill each \(Z_y\) by using only coordinate-plaque tracks, discarding the part of the chosen filling \(B_y\) lying in \(\mathcal B_z\).  The formal bookkeeping would be:

1. Use coordinate-plaque tracks only.  If a track lies in a coordinate \(2\)-plaque whose \(F\)-image contains \(z\), charge it to \(B_y\llcorner\mathcal B_z\).  This is exactly why all coordinate plaques, not just vertical \(x_3x_4\)-plaques, are needed.

2. Pay the good short-direction sweep by \(R_1E_y\).  Geometrically, this is the cost of moving \(G\)-controlled surface pieces through distance \(O(R_1)\), with the \(2\)-Jacobian of the tracked surface measured by \(\lambda^2\).

3. Pay the \(G\)-grid seams by \(E_y^2/S_1\).  This is the expected one-dimensional coarea term: slicing the \(G\)-surface by \(f_1=t\), choosing levels/seams by averaging over an interval of length \(S_1\), and filling the seam family quadratically gives the scale \(E_y^2/S_1\).

4. Use the low-energy restriction only after integration:
\[
\int_\Omega E_y^2\,dy\le (4I/q)\int_\Omega E_y\,dy\le 4I^2/q.
\]
Thus (13) would imply (14), and the plaque-bad term would self-absorb in the hard regime \(R_3R_4\ll S_3S_4\).

This is internally consistent, but the local estimate required in step 2 is not true.

## First non-repairable estimate

A coordinate sweep in the \(x_1\)-direction of a surface element with tangent \(2\)-vector \(\xi\) has track density \(|e_1\wedge\xi|\).  The direct proof would need a local inequality of the schematic form
\[
 |e_1\wedge\xi|
 \lesssim \lambda^2
 +\hbox{averaged plaque-bad probability},
\]
at least after summing over the relevant coordinate tracks.  This is false.

Local affine model: take the fiber tangent plane \(T=\operatorname{span}(e_3,e_4)\), \(\xi=e_3\wedge e_4\), and a linear differential
\[
dF(e_1)=L,\qquad dF(e_2)=L^{-1},\qquad
dG(e_3)=L^{-1},\qquad dG(e_4)=L^{-1},
\]
with all other displayed components zero.  The singular values are
\[
L,\ L^{-1},\ L^{-1},\ L^{-1},
\]
so \(\Dil_2=1\).  On \(T\),
\[
\lambda^2=L^{-2}.
\]
But sweeping the \(e_3e_4\)-sheet in the \(x_1\)-direction has density
\[
|e_1\wedge e_3\wedge e_4|=1.
\]

If the parameter square has area \(q=L^2\), the only \(2\)-dimensional plaque image here is \(F(P_{12})\), with area \(1\), so the averaged bad-puncture probability is \(1/q=L^{-2}\).  Therefore the desired local payment fails by
\[
{1\over L^{-2}+L^{-2}}={L^2\over2}.
\]

The numerical table saved in `data/round18_local_track_obstruction.txt` is:

| \(L\) | \(\Dil_2\) | \(\lambda^2\) | bad probability | track density | ratio |
|---:|---:|---:|---:|---:|---:|
| 10 | 1 | \(10^{-2}\) | \(10^{-2}\) | 1 | 50 |
| 30 | 1 | \(1.11\cdot10^{-3}\) | \(1.11\cdot10^{-3}\) | 1 | 450 |
| 100 | 1 | \(10^{-4}\) | \(10^{-4}\) | 1 | 5000 |
| 300 | 1 | \(1.11\cdot10^{-5}\) | \(1.11\cdot10^{-5}\) | 1 | 45000 |
| 1000 | 1 | \(10^{-6}\) | \(10^{-6}\) | 1 | 500000 |

This is not a global counterexample to (13).  The obstruction is local: it says that a proof cannot simply deform surface elements along coordinate tracks and pay pointwise by \(\lambda^2\) plus the averaged all-plaque bad probability.  Any proof of (13) must use a genuinely global family mechanism: degree, cancellation, or compatibility of the \(Q\)-family must prevent the above local pattern from carrying the filling volume.

## Counterexample search status

I found no new counterexample satisfying the hard-regime assumptions.  Existing checks already showed no positive-margin diagonal/permutation affine counterexample (`data/round9_hard_regime_search.txt`).  I reran a small randomized scan of the corrected Guth Chapter 8 exponent-move model:

`data/round18_guth_hard_scan.txt`:

```
# depth 4
seeds 201,202,203: No all-three violating composition found in 1000 random trials each.

# depth 5
seeds 201,202,203: No all-three violating composition found in 1000 random trials each.
```

This scan is only heuristic.  It does not rule out a composition of Guth snake/pinching maps, but it gives no evidence for one.  The previous corrected model remains relevant: the tempting stress family
\[
S=(1,1,L^6,L^6),\qquad R=(L^{-1},L^4,L^5,L^6)
\]
passes the known monomial obstructions but has not been realized by the verified Chapter 8 constructions.

## Literature fallback

No external theorem equivalent to (13) was located this round.  The useful source locations remain:

- `data/round17/arxiv_0802_3549_src/LINKDIL2.TEX`, lines 392--400: Guth states that the analogous problem for \(2\)-dilation of mappings between \(4\)-dimensional rectangles was recently solved in `[G4]`, that the answer is complicated, and that near-optimal maps are far from linear.
- Same file, lines 1588--1590: bibliography entry `[G4] Guth, L., On the 2-dilation of mappings between 4-dimensional rectangles, preprint.`
- `data/round17/arxiv_0710_0403_src/EXEMB2.TEX`, lines 656--663: Guth Estimate 1, the standard monomial lower bound for degree-one maps of pairs.
- `data/round17/arxiv_0802_3549_src/LINKDIL2.TEX`, lines 878--892: the relative directional isoperimetric proposition.  Its specialization is the valid estimate (15) in `answer.tex`, but it does not close the hard-regime exponent gap.

Targeted web search for the exact `[G4]` title and close variants again gave no usable PDF/TeX/theorem statement beyond the already-saved evidence in `data/round17/`.

## Recommendation

Do not paste a proof of (13) into `answer.tex` yet.  The current draft should continue to label (13) as the sole gap.  A future proof needs a nonlocal parametric tightening theorem that bypasses the false local track-density estimate above.  In particular, it must exploit compatibility of the family \(\{Z_y\}_{y\in Q}\), not merely pointwise coordinate-plaque deformation plus averaged bad mass.
