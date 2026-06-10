# Compute worker reply — round 29
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c3-7db360/compute_workspace_round_29.zip

---

# Round 29 response: LE-HAF reduced to one exact-plaque chain-map lemma

## Bottom line

I did not prove LE-HAF, and I did not find a rigorous hard-regime counterexample to it.  The useful output is a sharper diagnosis: the first lemma whose truth/falsity decides the current averaged tightening step is an **exact-plaque energy chain-map lemma**.  It is stronger than a standard cubical deformation theorem in exactly the two places where the previous proof attempts broke:

1. it must use exact coordinate plaque badness, not thickened bad cells or near-miss neighborhoods;
2. its homotopy mass bound cannot be a literal pointwise source sweep of all of \(Z_y\), because low-\(G\)-energy flaps and dead sheets defeat that.

Files produced:

- `data/round29/decisive_lemma.tex`: insertable TeX statement of the decisive lemma and the no-seam implication.
- `code/round29_plaque_obstructions.py`: small reproducible checks for the two obstructions below.
- `data/round29/plaque_obstructions.txt`: numerical/log output.

## The decisive lemma

Let \(F=(f_3,f_4)\), \(G=(f_1,f_2)\), and
\[
{\mathcal B}_z=\{x\in R:\ z\in F(P_{ij}(x))\hbox{ for at least one coordinate \(2\)-plaque }P_{ij}(x)\}.
\]
For a.e. regular \(y\in Q\), set \(Z_y=\langle [[R]],F,y\rangle\) and
\[
E_y=\int \|dG|_{TZ_y}\|_{HS}^2\,d\|Z_y\|.
\]

The needed statement is:

**Exact-plaque energy chain-map lemma.**  There is a universal \(C\) such that, for every relative integral \(3\)-chain \(B_y\) with \(\partial B_y=Z_y\), and for a.e. \(z\in Q\), there are relative chain operators \(P_z,H_z\), defined at least on \(B_y\) and \(Z_y\), satisfying
\[
\partial H_z(T)+H_z(\partial T)=P_z(T)-T,\qquad
\partial P_z(T)=P_z(\partial T),
\]
and
\[
\Mass H_z(Z_y)\le C\left(R_1E_y+\frac{E_y^2}{S_1}\right),
\qquad
\Mass P_z(B_y)\le C\,\Mass(B_y\llcorner{\mathcal B}_z).
\]

The second estimate is meant literally with the exact \({\mathcal B}_z\), not with a cell-star, \(\delta\)-neighborhood, or other enlargement.

If this lemma holds, then LE-HAF follows immediately and without any seam term.  Indeed,
\[
C_{y,z}=P_z(B_y)-H_z(Z_y)
\]
is a relative \(3\)-chain with
\[
\partial C_{y,z}=P_zZ_y-(P_zZ_y-Z_y)=Z_y.
\]
Hence
\[
\Fill_R(Z_y)\le
C\left(R_1E_y+\frac{E_y^2}{S_1}\right)
+C\,\Mass(B_y\llcorner{\mathcal B}_z).
\]
Averaging in \(z\in Q\) and then \(y\in\Omega\) gives exactly
\[
\int_\Omega\Fill_R(Z_y)\,dy
\le C\int_\Omega\left(R_1E_y+\frac{E_y^2}{S_1}\right)dy
 +\frac{C}{q}\int_Q\int_\Omega
       \Mass(B_y\llcorner{\mathcal B}_z)\,dy\,dz .
\]

This also explains the no-seam identity precisely: we never cut \(B_y\).  The chain map \(P_z\) is applied to the whole \(B_y\), and its good part is killed relatively; only the mass estimate for \(P_z(B_y)\) is charged to \({\mathcal B}_z\).

An averaged-over-shifts version with \(P_{z,\theta},H_{z,\theta}\) would be equally sufficient if the two displayed mass estimates hold after averaging in \(\theta\).

## Exact plaques vs thickened cells

Exact coordinate plaques do give the desired Fubini estimate:
\[
\frac1q\int_Q\Mass(B\llcorner{\mathcal B}_z)\,dz
=\int_R \frac{|\{z:x\in{\mathcal B}_z\}|}{q}\,d\|B\|(x)
\le C\frac{R_3R_4}{S_3S_4}\Mass B,
\]
because for fixed \(x\), each coordinate \(2\)-plaque through \(x\) has \(F\)-image area at most its source area, hence at most \(R_3R_4\).

But this is not stable under thickening.  A rank-one comb plaque already breaks it.  Let \(Q=[0,1]^2\), and let \(F(u,v)=\gamma_N(u)\), where \(\gamma_N\) runs along \(N\) vertical line segments spaced \(1/N\) apart.  Then \(J_2(F|_{\hbox{plaque}})=0\), so the exact image has area zero.  However the \(\delta=c/N\) neighborhood of the image contains at least a \(\min(1,2c)\) fraction of \(Q\).  The script output includes:

| \(N\) | \(\delta\) | exact area | thickened lower bound |
|---:|---:|---:|---:|
| 100 | \(1/(3N)\) | 0 | 0.666667 |
| 1000 | \(1/(3N)\) | 0 | 0.666667 |

So a standard cubical bad-cell enlargement can mark a fixed fraction of \(Q\) while the area-controlled exact bad set has measure zero.  This is why the decisive lemma has to be exact-plaque and essentially pointwise/current-theoretic, not an ordinary cell-star deformation.

## Why a literal pointwise sweep is false

The homotopy bound in the decisive lemma also cannot come from physically sweeping every surface element of \(Z_y\) through a short source direction.  The local affine model is:
\[
T=\operatorname{span}(e_3,e_4),\qquad
dF(e_1)=L,\quad dF(e_2)=L^{-1},\quad
dG(e_3)=dG(e_4)=L^{-1}.
\]
The singular values are \(L,L^{-1},L^{-1},L^{-1}\), so \(\Dil_2=1\).  On \(T\),
\[
\lambda^2=\|dG|_T\|^2\sim L^{-2}.
\]
If \(q=L^2\), the averaged exact-plaque bad probability is also \(\sim L^{-2}\).  But sweeping the \(e_3e_4\)-sheet in the \(e_1\)-direction has track density \(1\).  The ratio is therefore \(\sim L^2\):

| \(L\) | \(\lambda^2\) | bad probability | track density | ratio |
|---:|---:|---:|---:|---:|
| 100 | \(10^{-4}\) | \(10^{-4}\) | 1 | 5000 |
| 1000 | \(10^{-6}\) | \(10^{-6}\) | 1 | 500000 |

Thus low-\(G\)-energy flaps cannot be moved pointwise at the claimed cost.  In a multi-sheet fiber where only one sheet carries the \(G\)-degree, the dead sheets must be killed algebraically through \(P_z(B_y)\), or ignored after cancellation, not swept by \(H_z\) as ordinary mass.  This is exactly the unresolved content of the decisive lemma.

## Recommendation for `answer.tex`

I would not state LE-HAF as proved.  The clean replacement is to insert the exact-plaque energy chain-map lemma above as the named missing lemma.  Then say:

- the no-seam implication from that lemma to LE-HAF is rigorous;
- exact plaques are sufficient for the Fubini bad-mass estimate;
- thickened bad cells and literal source sweeps are rigorously insufficient;
- the remaining issue is precisely whether such an exact-plaque, energy-sensitive chain map exists for the two-parameter family of degree-one \(2\)-contracting slices.

That is the sharpest form I can isolate: proving this lemma closes the current gap, while falsifying it by a genuine degree-one hard-regime map would falsify the current LE-HAF route.
