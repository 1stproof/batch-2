# Round 32 report: averaged tightening `(AT)`

## 1. Counterexample search

I did **not** find a genuine hard-regime degree-one counterexample to `(AT)`.  The strongest negative result from this round is narrower: the obvious low-`G` null-sheet/flap constructions do not globalize as simple product models under the hard side-length assumption.

I normalized the stress case to
\[
S=(1,1,L,L),\qquad |Q|\sim L^2,
\]
and wrote `R_i=L^{r_i}`.  In the hard regime `r_1<0` and `r_3+r_4<2`.  A coordinate-product flap family would have a two-dimensional sheet factor on which `G=(f_1,f_2)` is constant or nearly constant, and a two-dimensional normal factor on which `F=(f_3,f_4)` covers the central parameter square `Q`.  Since `Dil_2(f) <= C`, the normal factor must have area `\gtrsim |Q|`, i.e. exponent at least `2`.  But every coordinate two-product has exponent at most `r_3+r_4<2`.  Thus every coordinate-product null-flap model is blocked.

The check is saved at:

- `code/round32_product_flap_check.py`
- `data/round32_product_flap_check.txt`

For the standard stress exponents
\[
R=(L^{-1/5},L^{13/15},L^{13/15},L^{13/15}),
\]
the script prints that all coordinate normal pairs have exponent at most `26/15 < 2`, so none can cover `Q` with bounded `2`-dilation.

I also checked the two most tempting low-energy flap types conceptually:

1. **Closed or interior f-null sheets.**  These can often be filled by a short source homotopy, e.g. to an `x_1` face, at cost `\lesssim R_1 Mass(N_y)` when their boundary does not sweep through the opposite `x_1` face.  They are not a convincing obstruction to the theorem; in a volume-contradiction setup their total coarea mass is limited.

2. **Relative flaps with boundary on short faces.**  These are the genuinely dangerous ones, because the short homotopy creates a seam on the swept boundary.  However, the product version again requires an `F`-normal coordinate two-plaque of area `\gtrsim |Q|`, contradicting `R_3R_4 \ll S_3S_4`.  A non-product/snake version is not ruled out by this bookkeeping, but constructing it would amount to a new hard-regime degree-one map.  I did not find one.

The local affine obstruction from earlier rounds remains valid: a physical pointwise sweep of all of `Z_y` cannot be paid by `R_1 E_y` plus averaged plaque-bad probability.  But I found no way to promote that local obstruction to a global pair map of degree one in the hard regime.

## 2. Proposed correction/proof route

I now think the safest route is to **stop trying to prove ordinary `(AT)` for the full geometric fiber** and replace it by an essential/dual version that ignores `f`-null sheets.  This is not just aesthetic: null sheets are exactly what make a pointwise chain homotopy false, while they do not contribute to the target filling obstruction.

Here is the clean insertable replacement.

**Definition (essential filling over `f`).**  For central regular `y`, define
\[
\operatorname{EFill}_f(y)=\inf \{ \operatorname{Mass} C:
 C\in I_3(R,\partial R),\quad f_\#(\partial C)=\pm P_y
 \text{ in } I_2(S,\partial S)\}.
\]
Equivalently, `C` need not fill the entire current `Z_y`; it only has to carry, after applying `f`, a relative filling boundary equal to the target plane `P_y`.

The target calibration still gives the same lower bound:
\[
\operatorname{EFill}_f(y)\ge c S_1S_2S_3
\]
for central `y`, because `f_# C` fills `P_y` and `Dil_3(f) <= 1`.

**Lemma to prove (essential averaged tightening).**  With the notation of `answer.tex`, let
\[
A^{ess}_\Omega=\int_\Omega \operatorname{EFill}_f(y)\,dy.
\]
For measurable near-minimizing essential chains `C_y^0`, meaning
\[
f_\#(\partial C_y^0)=\pm P_y,\qquad
\Mass C_y^0\le 2\operatorname{EFill}_f(y),
\]
one should prove
\[
A^{ess}_\Omega
\le C\left(R_1 I+{I^2\over S_1|Q|}\right)
 +{C\over |Q|}\int_Q\int_\Omega
    \operatorname{Mass}(C_y^0\llcorner {\mathcal B}_z)\,dy\,dz. \tag{EAT}
\]
This is enough for the theorem by the same absorption argument currently used for `(AT)`, because the exact-plaque Fubini estimate gives
\[
{1\over |Q|}\int_Q\int_\Omega
    \operatorname{Mass}(C_y^0\llcorner {\mathcal B}_z)\,dy\,dz
\le C {R_3R_4\over S_3S_4} A^{ess}_\Omega,
\]
and this term is absorbable in the hard regime exactly as before.  This is the important correction: if the bad term uses ordinary fillings of the whole `Z_y`, low-energy null sheets may leave a non-absorbable `Fill_R(Z_y)` on the right.  The bad term should be measured on an essential auxiliary chain, not on a full filling of every geometric sheet.

A dual form may be easier to prove and avoids seam terms.  For near-dual relative two-forms `omega_y` with `||d omega_y||_infty <= 1`, prove after averaging in `y,z` that
\[
\int_\Omega \langle P_y,\eta_y\rangle\,dy
\lesssim R_1I+{I^2\over S_1|Q|}
 +{1\over |Q|}\int_Q\int_\Omega
   \int_{C_y^0\cap {\mathcal B}_z} |d\omega_y|\,dy\,dz,
\]
where the left side is the dual essential filling functional.  The point is that the chain homotopy acts on cochains/forms, not by sharply cutting `C_y^0`; hence no `partial(C_y^0 | B_z)` seam appears.  This is the most precise route I see.

## 3. Literature search

No copy or theorem statement of Guth's missing preprint was located.

New round-specific files are under `data/round32_lit/`, with the script:

- `code/round32_lit_search.py`
- `data/round32_lit/round32_lit_search_summary.json`

This pass checked: arXiv exact title, Crossref, OpenAlex, Semantic Scholar, OpenLibrary, MIT DSpace search, HathiTrust, WorldCat, Stanford SearchWorks, GitHub code search page, Internet Archive advanced search exact/variant text, and Wayback CDX inventories for old Guth MIT/Stanford/NYU personal-page patterns.

Concrete results:

- arXiv exact title: `totalResults=0` in `data/round32_lit/arxiv_exact.xml`.
- Internet Archive exact title/text and variant text searches: `numFound=0` in `ia_title_exact.json`, `ia_text_exact.json`, `ia_text_variant.json`.
- OpenLibrary exact title: `numFound=0`.
- Crossref/OpenAlex returned unrelated items only.
- Semantic Scholar returned HTTP 429 in this pass; previous rounds already saved negative/irrelevant Semantic Scholar searches.
- Wayback CDX produced only one suggestive archived Guth URL, `Listofpapers.pdf`; downloaded as `papers/round32/Listofpapers_20180806.pdf`, extracted to `data/round32_lit/Listofpapers_20180806.txt`.  It is a seminar reading list, not Guth's publication list, and contains no dilation/rectangle preprint.

One adjacent item found by web search is EMS Magazine problem 280 by Fedor Manin, saved in `data/round32_lit/ems_problem_280_note.txt`.  It distinguishes relative degree-one maps, whose `2`-dilation has a boundary-degree lower bound, from merely surjective Kaufman-style maps with `Dil_2 -> 0`.  This is not the missing theorem, but it is useful cautionary evidence: low-rank/null-sheet constructions are easy for surjectivity and much harder under the pair/degree condition.

## 4. Recommended edits to `answer.tex`

I recommend replacing the current ordinary `(AT)` paragraph by a conditional statement using essential filling.  Suggested text:

```tex
For central regular y define
\[
\operatorname{EFill}_f(y)=\inf\{\Mass C:
 C\in I_3(R,\partial R),\ f_\#(\partial C)=\pm P_y
 \text{ in }I_2(S,\partial S)\}.
\]
The same calibration as in Lemma \ref{central}, together with
\(\Dil_3(f)\le1\), gives
\[
\operatorname{EFill}_f(y)\ge cS_1S_2S_3
\]
for a.e. central \(y\).
The remaining missing estimate is the essential averaged tightening estimate
\[
\int_\Omega\operatorname{EFill}_f(y)\,dy
\le C\left(R_1I+{I^2\over S_1q}\right)
 +{C\over q}\int_Q\int_\Omega
       \Mass(C_y^0\llcorner{\mathcal B}_z)\,dy\,dz, \tag{EAT}
\]
where \(C_y^0\) is a measurable near-minimizer for
\(\operatorname{EFill}_f(y)\).
Unlike a pointwise deformation of \(Z_y\), (EAT) ignores \(f\)-null sheets
and asks only for a controlled chain whose boundary carries the target plane.
A proof should be dual or cellular: it must avoid sharp restrictions of
\(C_y^0\), because those create uncontrolled seam boundaries.
```

Then replace every later use of `A_Omega = int Fill_R(Z_y)` in the lower-bound part by
\[
A^{ess}_\Omega=\int_\Omega\operatorname{EFill}_f(y)\,dy.
\]
The algebra after the estimate is unchanged.

I would not claim `(EAT)` is proved yet.  But it is a better target than `(AT)`: it removes the low-energy null-sheet/flap objection while retaining exactly the target lower bound needed for the theorem.
