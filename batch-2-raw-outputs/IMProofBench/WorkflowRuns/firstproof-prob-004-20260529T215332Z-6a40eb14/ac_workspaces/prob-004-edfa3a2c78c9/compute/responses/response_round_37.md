# Round 37 response: QEAT finite models, dual diagnostics, and literature pass

Verdict: **partial diagnostics only**.  I did **not** find a counterexample to
the quotient `(QEAT)` statement, but I also did **not** close the missing
kernel/homotopy estimate.  The finite LP models support the current quotient
formulation and identify a sharp dual certificate pattern: the residual term
must be a target/quotient cochain whose pullback is bounded by the exact bad
mask on every source representative of the same `f_#` target chain.

Files created:

- `code/round37/qeat_lp_models.py`
- `data/round37/qeat_lp_models.md`
- `code/round37/pl_chart_exact_bad.py`
- `data/round37/pl_chart_exact_bad.md`
- `notes/round37/qeat_dual_derivation.md`
- `code/round37/lit_search_unusual.py`
- `data/round37/lit_search/summary.json`
- `papers/round37/ems_magazine_2024_solved_unsolved_47217.pdf`
- `data/round37/ems_magazine_2024_solved_unsolved_47217.txt`

## 1. Finite quotient LP model

I modeled finite cellular chains with source 3-cells, a cellular push-forward
`F_3`, a pushed boundary map `F_2 d`, exact-plaque bad masks `w_i(z)`, and the
quotient seminorm

```text
beta_z(t) = min sum_i w_i(z) |D_i|  subject to F_3 D = t.
```

The LP dual is

```text
beta_z(t) = max <lambda,t>
            subject to |<F_3^* lambda, sigma_i>| <= w_i(z)
            for every source 3-cell sigma_i.
```

This is the most useful output of the computation.  It says that a residual
cochain can be nonzero on a target 3-cell only if every source representative
of that target 3-cell is bad enough.  This is exactly the quotient-compatible
replacement for source-local bad restriction.

Smallest two-sheet model:

```text
C_3^src = span(A,A'),     C_3^tar = span(T),
F_3(A)=F_3(A')=T,
F_2 dA=F_2 dA'=P.
```

The LP output was:

| bad mask on `(A,A')` | raw bad mass of chosen `A` | `beta_z([A])` | beta minimizer | beta dual |
|---|---:|---:|---|---|
| A bad only `(1,0)` | 1 | 0 | `(0,1)` | `0` |
| A' bad only `(0,1)` | 0 | 0 | `(1,0)` | `0` |
| both bad `(1,1)` | 1 | 1 | `(1,0)` | `1` |
| none bad `(0,0)` | 0 | 0 | `(1,0)` | `0` |

So the old unsaturated bad-set problem disappears in the **statement** of
QEAT: if one `f_#`-equivalent representative is nonbad, then the beta residual
vanishes.  This does not prove QEAT, but it confirms that the residual term has
the correct quotient behavior.

A second 3-target-cell model with redundant representatives gave the same
pattern.  For `t=T0+T1+T2`, beta was `0,0,1,2` for four masks; the dual target
cochains were respectively `(0,0,0)`, `(0,0,0)`, `(0,0,1)`, `(0,1,1)`.  See
`data/round37/qeat_lp_models.md`.

## 2. Explicit PL exact-plaque realization

I also wrote down a genuine affine PL chart realizing the unsaturated exact
plaque phenomenon for **3-cells**, not just the old 2-cell toy model.  Two
disjoint cubical charts have coordinates `(u,v,s,t)`:

```text
A:  f(u,v,s,t) = (u,v,s,t)
A': f(u,v,s,t) = (u,v,s,eps*t)
```

On the central relative 3-cells `{t=0}`, the maps agree:

```text
f_# A = f_# A' = [0,1]^3 x {0}.
```

But the full coordinate `(s,t)` plaque through a point of `A` has `F`-image
`[0,1] x [-1,1]`, while the corresponding plaque through `A'` has image
`[0,1] x [-eps,eps]`.  For `z=(1/2,0.4)`, the output was:

| eps | Dil_2 on A | Dil_2 on A' | A bad? | A' bad? |
|---:|---:|---:|---|---|
| 0.5 | 1 | 1 | yes | yes |
| 0.25 | 1 | 1 | yes | no |
| 0.1 | 1 | 1 | yes | no |
| 0.01 | 1 | 1 | yes | no |

This is **not** a counterexample to QEAT: in the unit chart the slice
`G=(u,v)` has energy `2` and the filling mass is `1`.  Its role is to show
that exact plaque badness is genuinely not saturated under `f_#` equivalence,
so a source-local projection cannot be the proof mechanism.

## 3. Diagonal PL sanity check

For diagonal maps `R -> S=(1,1,L,L)`, the script verified the expected
behavior: if the chart is 2-contracting, then the full coordinate `(x3,x4)`
plaque is already large whenever the map carries the target `Q` in the
obvious way.  For example:

| L | R | Dil_2 | R3R4/S3S4 | status |
|---:|---|---:|---:|---|
| 16 | `(1,1,16,16)` | 1 | 1 | 2-contracting |
| 16 | `(1,1,16,1)` | 16 | 1/16 | not 2-contracting |
| 32 | `(1,1,32,32)` | 1 | 1 | 2-contracting |
| 32 | `(1,1,32,1)` | 32 | 1/32 | not 2-contracting |

This did not find a diagonal counterexample.  Any real counterexample would
have to use nonlinear degree-carrying structure, not a single diagonal chart.

## 4. Dual proof route attempted

The finite dual calculation suggests the following exact target-pullback form
of QEAT.  For each admissible dual `psi` with `||F_3^* delta psi||_* <= 1`,
one wants, for a.e. `y,z`, a decomposition

```text
<psi, P_y> = <delta psi, T^reg_{y,z}> + <lambda_{y,z}, F_3 C_y^0>,
```

with

```text
Mass_src(T^reg_{y,z}) <= C (R_1 E_y + E_y^2/S_1),
|<F_3^* lambda_{y,z}, sigma>| <= 1_{sigma in B_z} Mass(sigma).
```

The second line makes the residual bounded by `beta_z([C_y^0])` by the beta
dual LP above.

The only proof route I see that preserves the quotient is target-side.  Choose
a singular Green kernel/one-form `eta_z` on the parameter square `Q` with

```text
d eta_z = delta_z - q^{-1} dy_3 dy_4,
```

then pull it back by `F=(f_3,f_4)`.  Because the construction is through target
coordinates, it respects `ker f_#`.  The singular term is supported exactly
where a full coordinate plaque sees `z`, i.e. the exact `B_z`, not a thickened
cell star.

The unresolved analytic step is the regular kernel bound

```text
int_Omega int_Q |regular sweep made by F^* eta_z on Z_y| dz dy
    <= C (R_1 I + I^2/(S_1 q)).
```

A direct absolute-value estimate on the Green kernel either loses a logarithm
or charges a thickened bad set.  I did not find the needed principal-value or
Stokes cancellation.

## 5. Literature search

I ran one more targeted pass over unusual sources:

- arXiv API, Crossref, OpenAlex, DataCite, Internet Archive, OpenLibrary;
- MIT DSpace, Stanford SearchWorks, HathiTrust, WorldCat pages where reachable;
- Wayback CDX inventories for old MIT, Stanford, NYU/CIMS, and Toronto Guth
  personal-page patterns;
- local extracted thesis/arXiv text and prior round responses.

Search log: `data/round37/lit_search/summary.json`.

Result: **no downloadable copy** of Guth's unpublished preprint
`On the 2-dilation of mappings between 4-dimensional rectangles`, and no
secondary theorem explicitly implying

```text
R3R4/(S3S4)
+ R1 sqrt(R3R4)/(S1 sqrt(S3S4))
+ Vol(R)/(S1 S2^(1/2) S3^(3/2) S4) >= c.
```

The exact/near hits in the search log are query echoes or the already-known
citation in Guth's `Directional isoperimetric inequalities...`.  Crossref and
OpenAlex returned irrelevant titles; DataCite/OpenLibrary/Internet Archive
returned no exact record; Semantic Scholar was rate-limited; the Wayback CDX
inventories did not reveal a suggestive preprint/PDF URL.

One new adjacent source was saved: the 2024 EMS Magazine "Solved and unsolved
problems" note, `papers/round37/ems_magazine_2024_solved_unsolved_47217.pdf`.
It discusses a relative-degree rectangle problem and cites Guth's
`The width-volume inequality`, Theorem 2, as a complex/surprising source for a
simple lower bound.  It does **not** state the missing 4D mixed estimate.

## Bottom line

- **Proof route:** target-pullback Green/cochain homotopy plus the beta-dual
  residual is the cleanest route I found.
- **Counterexample:** none found for quotient QEAT.  The explicit PL model is
  only an obstruction to source-local proof strategies.
- **Remaining gap:** prove the regular Green-kernel estimate with exact
  plaque singular residual and no thickening/log loss.
