# Round 3 compute report

## Bottom line

I did **not** find a counterexample. More importantly, I found a recent partial-flag completion result that covers the requested computational gap `rank(p)=1`, `rank(q)=3`: Jidong Wang, *Lorentzian polynomials and the incidence geometry of tropical linear spaces*, arXiv:2412.12059v2 (2026), Proposition `complete-towards-point` and Theorem F. It says that if a valuated quotient ends in a rank-1 valuated matroid, then the partial flag can be completed by elementary quotients, with the underlying matroids forming the Higgs factorization. Thus any `p <= q <= mu_M` with `rank p = 1` admits an elementary refinement `p <= h <= q`, and the elementary-opposition lemma in `answer.tex` already proves order reversal for this case.

I also think there is now a clean proof route for the general full-incidence duality. The missing degenerate case `delta=b-a+1` should follow from applying the already-proved **single-quotient opposition** theorem to a localized minor of `q` on the modular interval `[W^\perp,U^\perp]`. I spell this out below as a proposed lemma.

Files created:

- `code/pg32_flat_opposition_z3.py`: exact Z3 encoding for `PG(3,2)`, ranks `1,3`.
- `data/pg32_rank1_rank3_K1_finite.json`: finite `{0,1}` search, `UNSAT`.
- `data/pg32_rank1_rank3_K2_finite.json`: finite `{0,1,2}` search, timeout/unknown.
- `data/pg32_rank1_rank3_K3_finite.json`: finite `{0,1,2,3}` search, timeout/unknown.
- `data/pg32_rank1_rank3_K1_with_inf.json`: `{0,1,∞}` search, timeout/unknown.
- `code/audit_one_point_completion.py` and `data/one_point_completion_audit_round3.json`: finite audit of formula (3).
- `papers/wang_2412.12059_src.tar`, `papers/wang_2412.12059_src/arXiv2026.tex`: Wang source.

## Literature findings

### Quotients / flag Dressians

Brandt--Eur--Zhang:

- Definition 4.2.2: valuated quotient `mu <= nu` by the exchange/incidence inequality.
- Proposition 4.2.3: tropical incidence-Plucker relations are equivalent to a pair being a valuated matroid quotient; points of `FlDr(r_1,...,r_k;n)` are valuated flag matroids.
- Theorem 4.3.1: `mu <= nu` iff `trop(mu) subset trop(nu)`.
- Corollary 4.3.2: quotients compose; minors preserve quotients; underlying ordinary matroids form a quotient.
- Theorem 5.1.2: every elementary valuated quotient arises from deleting/contracting one new element of a valuated matroid. This is only rank-difference one; it does **not** itself prove arbitrary-rank factorization.

Jarra--Lorscheid:

- Theorem 2.17: for a tract `F`, if covector sets form a chain then the sequence is a flag `F`-matroid; a flag implies consecutive quotients; if `F` is perfect, consecutive quotients imply the covector-chain condition. Since the tropical hyperfield is perfect, this recovers composability/flag behavior for valuated matroids.
- Proposition 2.21: BEZ valuated flag matroids are exactly flag matroids over the tropical hyperfield.
- Remark 2.22 explicitly says this recovers BEZ Theorem 4.3.1 and Proposition 4.2.3.

Joswig--Loho--Luber--Olarte:

- Lemma 8: for a finite valuated matroid `mu` on the uniform ground set, its truncation and elongation form quotients with `mu`.
- Proposition 9: iterating gives a piecewise-linear embedding of the Dressian into the flag Dressian.
- Theorem 10: for adjacent ranks, tropical incidence relations alone imply both functions are valuated matroids.

Murota:

- Theorem 2.1 in *Matroid valuation on independent sets*: with max/`-∞` convention, truncation and elongation of a valuated matroid are valuated matroids. This is the source for the two min-formulas in `answer.tex` after sign reversal.
- Theorem 4.1: relative truncation/elongation with respect to a spanning set / independent set also yields valuated matroids.
- Theorem 3.2 gives the independent-set extension satisfying exchange, submodularity, and augmentation properties.

### Partial flag completion

Wang, arXiv:2412.12059v2:

- The paper explicitly formulates the partial-flag completion question: given `mu_0 -> mu_k`, can one insert elementary quotients?
- Proposition `extension-implies-higgs`: if a valuated matroid on `[n] sqcup I` deletes/contracts to the endpoints, then an elementary Higgs-factorization completion exists.
- Proposition `complete-towards-point`: if `mu_0 -> mu_{d-1}` has rank-1 lower endpoint, then there are valuated matroids completing it by elementary quotients, and the underlying flag is the Higgs factorization. It also constructs a multi-element extension.
- Theorem F: for any point `[w] in Trop(mu)`, the partial flag `{[w]} subset Trop(mu)` can be completed.

This covers the requested `rank 1` versus `rank 3` search, but not arbitrary intermediate ranks. Wang also notes that no counterexample to general tropical partial-flag completion is known, while prescribed underlying-matroid completions can fail.

### Modular lattices, q-matroids, Coxeter/building directions

Hirai, *Uniform semimodular lattices and valuated matroids*:

- Theorem 4.30: integer points of a tropical linear space of an integer valuated matroid form a uniform semimodular lattice; the paper relates this to Euclidean buildings of type A.
- This is useful background for coordinate-free valuated matroids/buildings, but I did not find an arbitrary-rank quotient-duality theorem of the kind needed here.

q-matroids:

- Jurrius--Pellikaan, *Defining the q-analogue of a matroid*, Theorem 42: the dual rank function defined using orthogonal complements is a q-matroid; Theorem 45: bases of the dual are orthogonal complements of bases.
- Byrne--Ceria--Jurrius, *Constructions of new q-cryptomorphisms*, develops cryptomorphisms and duality via orthogonal complements.
- These are unvaluated q-matroid results. I did not find a valuated q-matroid quotient/flag theorem that covers this problem.

Coxeter/other types:

- Recent “minuscule Coxeter Dressian” work studies valuated Coxeter matroids and subdivisions in minuscule types. It is not a type-A arbitrary-rank quotient-opposition theorem.
- Type D valuated delta-matroid / isotropical linear space results are adjacent in spirit, but do not cover this modular-matroid relative Dressian question.

## Audit of one-point completion formula

The formula in `answer.tex`

```tex
h_j(B)=min{nu(C): B subset C, |C|=k}       (j <= k)
h_j(B)=min{nu(C): C subset B, |C|=k}       (j >= k)
```

is valid with these hypotheses/clarifications:

1. `nu` must be a nonzero valuated matroid quotient `nu <= mu_M`; the all-`∞` function must be excluded.
2. For `j >= k`, dependent `j`-subsets of `M` must be assigned `∞`.
3. Murota Theorem 2.1 proves the layers are valuated matroids, but it does not by itself prove the **relative endpoint** `h_r = mu_M`. That endpoint uses the extra hypothesis `nu <= mu_M`.

A short proof of the endpoint: for an `M`-basis `B`, set
`m(B)=min{nu(C): C subset B, |C|=k}`. If `B' = B-e+f` is an adjacent `M`-basis and `C subset B` minimizes `m(B)`, then if `e notin C` we have `C subset B'`. If `e in C`, apply the incidence relation for `nu <= mu_M` with `S=C-e` and `T=B union {f}`. The term indexed by `e` has value `nu(C)`; incidence gives another finite term `i != e` with value `<= nu(C)`, and `S union {i} subset B'`. Hence `m(B') <= m(B)`, and symmetry gives equality on the basis graph. Thus `h_r` is projectively trivial.

Computational audit: `code/audit_one_point_completion.py` exhaustively checked nonempty small cases over `{0,1,2,∞}` where flat enumeration was feasible:

| matroid | checks | failures | ranks checked |
|---|---:|---:|---|
| `Boolean_U_4,4` | 550 | 0 | 1,2,3 |
| `U_2,4` | 13 | 0 | 1 |
| `Fano_PG_2_2` | 212 | 0 | 1,2 |
| `U_2,3_plus_U_2,3` | 400 | 0 | 1,3 |

## PG(3,2) Z3 search

Encoding details in `code/pg32_flat_opposition_z3.py`:

- `PG(3,2)` represented as the 15 nonzero vectors in `F_2^4`.
- Polarity is the standard nondegenerate dot product.
- Variables: 15 point variables for `p` and 15 plane variables for `q`.
- Subset coordinate returns `∞` if dependent or wrong closure rank; otherwise the variable of its closure.
- Constraints:
  - full tropical Plucker for `q` rank 3: 15,015 relations;
  - full incidence `q <= mu_M`: 30,030 relations;
  - full incidence `p <= q`: 1,365 relations;
  - unique-min violation after transform: OR of 5,460 possible winners;
  - normalization: some `p` variable is 0 and some `q` variable is 0.

Results:

| domain | status | elapsed | file |
|---|---:|---:|---|
| finite `{0,1}` | `UNSAT` | 43.7s | `data/pg32_rank1_rank3_K1_finite.json` |
| finite `{0,1,2}` | `unknown` timeout | 218.9s | `data/pg32_rank1_rank3_K2_finite.json` |
| finite `{0,1,2,3}` | `unknown` timeout | 98.4s | `data/pg32_rank1_rank3_K3_finite.json` |
| `{0,1,∞}` | `unknown` timeout | 158.7s | `data/pg32_rank1_rank3_K1_with_inf.json` |

The timeouts are not evidence either way; the Wang completion result is the stronger reason this rank gap should be positive.

## Proposed full-incidence proof route

Let `p <= q <= mu_M`, with ranks `a<b`, and test transformed incidence for
`q^perp <= p^perp`. Fix `A subset T` with

```tex
|A| = r-b-1,     |T| = r-a+1,
U = cl(A),       W = cl(T),
delta = rk(W)-rk(U).
```

If `A` is dependent or `delta <= b-a`, every transformed term is `∞`.

If `delta=b-a+2`, then `G=W^perp` has rank `a-1` and `H=U^perp` has rank `b+1`. For finite terms,

```tex
X_i=(cl(T-i))^perp       rank a,
Y_i=(cl(Ai))^perp        rank b.
```

In the interval `[G,H]`, the `X_i` are the atoms of a simplex over `G`, and `Y_i` is the join of all `X_j`, `j != i`. Choosing representatives over a basis of `G`, the transformed terms are exactly the original full incidence terms for `p <= q`.

The hard case is `delta=b-a+1`. Then `G=W^perp` has rank `a`, `H=U^perp` has rank `b+1`, and all finite transformed terms have common `p`-coordinate `p(G)`. It remains to show

```tex
min_i q((cl(Ai))^perp)
```

has at least two minimizers among finite indices.

Proposed lemma:

**Localized rank-one opposition lemma.** Let `q <= mu_M` be rank `b`. Let `G < H` be flats of ranks `a` and `b+1`, and suppose a chosen basis of `G` is independent in the underlying matroid of `q`. Form the minor
`q_{G,H} := (q / G)|H`, a rank `b-a` quotient of the rank `b+1-a` modular geometry `[G,H]`. Under any lattice anti-isomorphism `[U,W] -> [G,H]`, the flat-opposition transform of `q_{G,H}` is a rank-1 quotient of the trivial valuation on `[U,W]`.

This lemma is essentially the already-proved set-level involution, applied to the minor `q_{G,H}` rather than to the whole matroid. Since `q_{G,H}` is a single quotient of the interval top, the proof only uses the one-point completion plus elementary opposition, not the arbitrary-rank theorem being proved.

Then in the degenerate incidence datum, the finite indices in `T\A` form the circuit of the rank `b-a+1` quotient geometry `W/U` (after removing repetitions/loops; repeated flats already give equal values by flat constancy). A rank-1 quotient of the trivial valuation satisfies exactly the circuit condition that the minimum on every circuit is attained at least twice. This gives the degenerate transformed incidence relation.

If formalized, this proves the full arbitrary-rank order reversal directly, without needing a global partial-flag completion theorem.

