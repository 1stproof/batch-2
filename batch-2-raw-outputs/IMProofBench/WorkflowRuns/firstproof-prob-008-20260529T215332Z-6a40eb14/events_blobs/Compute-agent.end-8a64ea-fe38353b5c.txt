## Round 6 literature audit: `local flag criterion`

### Files inspected / retrieved

Local copies now present:

- `papers/brandt_eur_zhang_2005.13727.pdf`, `.txt`, and source at `papers/src/bez/extract/BEZ_TropFlagVar.tex`.
- `papers/jarra_lorscheid_2204.04658.pdf`, `.txt`, and arXiv source at `papers/src/jarra_lorscheid/main.tex`.
- `papers/murota_shioura_2017_wp.pdf`, `.txt`: Tokyo Tech working paper version of Murota--Shioura, *Simpler Exchange Axioms for M-concave Functions on Generalized Polymatroids*.
- `papers/murota_shioura_1999_mcg.pdf`, `.txt`: Murota--Shioura, *M-convex Function on Generalized Polymatroid*.
- `papers/murota_independent_sets_try.pdf`, `.txt`: Murota, *Matroid valuation on independent sets*.

I could not access the SIAM book text directly: the SIAM chapter endpoint returned HTTP 403. The 2018 Murota--Shioura paper restates the relevant local exchange theorem explicitly, so the book is not needed for that point. Also, the DOI in `references.bib` for Murota--Shioura 2018 appears wrong: the article DOI is `10.1007/s13160-017-0285-5`, not `...0279-3`.

### Exact primary-source statements

**Brandt--Eur--Zhang, Tropical flag varieties.**

- Definition 4.2.1 defines the tropical incidence-Pluecker relations
  \[
  \bigoplus_{j'\in J'\setminus I'} P_{I'\cup j'}P_{J'\setminus j'}
  \]
  for all \(I'\in {[n]\choose r-1}\), \(J'\in {[n]\choose s+1}\). These are the full, arbitrary incidence relations, not only the nested ones.
- Definition 4.2.2 defines a valuated quotient \(\mu\twoheadleftarrow\nu\) by the valuated basis-exchange inequality.
- Proposition 4.2.3: a pair is a point of \(FlDr(r,s;n)\) iff the two coordinates are valuated matroids forming a valuated quotient. In the proof they identify the full incidence-Pluecker relations with the quotient inequalities.
- Theorem 4.3.1: \(\mu\twoheadleftarrow\nu\) iff \(\overline{\operatorname{trop}}(\mu)\subseteq\overline{\operatorname{trop}}(\nu)\). For a sequence, being a valuated flag matroid is equivalent to a chain of projective tropical linear spaces.
- Corollary 4.3.2(1): valuated quotients compose.

**Jarra--Lorscheid, Flag matroids with coefficients.**

- Definition 2.1: a quotient \(N\twoheadrightarrow M\) of \(F\)-matroids is defined by the Pluecker flag relations for all tuples \(y_1,\ldots,y_{w+1},x_1,\ldots,x_{r-1}\). Again, this is the full relation.
- Theorem 2.17: for a perfect tract, a sequence is a flag \(F\)-matroid iff adjacent quotients \(M_{i+1}\twoheadrightarrow M_i\) hold; equivalently, covector sets form a chain.
- Proposition 2.21: BEZ valuated flag matroids are exactly flag \(\mathbb T\)-matroids under the tropical-hyperfield translation. Remark 2.22 says this recovers BEZ Theorem 4.3.1 and Proposition 4.2.3.

Important limitation: Theorem 2.17 and Proposition 2.21 assume the individual \(M_i\) are already \(F\)-matroids / valuated matroids. They do not by themselves prove that arbitrary tropical coordinate vectors satisfying only adjacent three-term incidence are valuated matroids.

**Joswig--Loho--Luber--Olarte, Generalized permutahedra and positive flag Dressians.**

- Section 3.2 defines adjacent-rank quotients by ordinary support quotient plus the three-term tropical incidence relations
  \[
  \min(\mu(Si)+\nu(Sjk),\,\mu(Sj)+\nu(Sik),\,\mu(Sk)+\nu(Sij)).
  \]
- Theorem 10: for finite functions on all \(d\)- and \(d+1\)-subsets, these adjacent three-term incidence relations imply that both functions are valuated matroids.
- Lemma 8 and Proposition 9: for a finite uniform valuated matroid, iterated truncations and elongations form a full valuated flag, giving the Dressian-to-flag-Dressian embedding.

Limitation: Theorem 10 is stated for finite functions on uniform supports. It is not a direct nonuniform/\(\infty\)-coordinate theorem.

**Murota--Shioura, Simpler exchange axioms.**

- Theorem 2.1: for \(f:\mathbb Z^n\to\mathbb R\cup\{-\infty\}\), \(M^\natural\)-concavity is equivalent to several exchange systems; condition (v) is: domain is \(M^\natural\)-convex and \(f\) satisfies the local exchange axioms \(L1,L2,L3\).
- Theorem 4.2 restates the same local criterion: \(f\) satisfies \(M^\natural\)-EXC iff \(\operatorname{dom} f\) is \(M^\natural\)-convex and \(f\) satisfies \(M^\natural\)-EXC\(_{\rm loc}\).
- Theorem 1.2 / Theorem 4.4: under extra domain hypotheses, e.g. integral polymatroid, \(L1,L2\) or even the simpler \(P1\) axiom suffices.

Critical limitation for `answer.tex`: these theorems apply to a single function on an \(M^\natural\)-convex/g-polymatroid domain. The union of only two non-adjacent rank layers is generally not such a domain. For example, \(\{\emptyset,\{1,2\}\}\) already fails \(M^\natural\)-convex exchange. Therefore the sentence in `answer.tex` lines 91--94 saying that two basis layers in quotient order form a \(0\)-\(1\) generalized polymatroid is false for rank gap \(>1\). The Murota--Shioura theorem does not justify the first assertion of the lemma as written.

**Murota, Matroid valuation on independent sets.**

- Theorem 2.1: ordinary valuated truncation and elongation of a valuated matroid are valuated matroids.
- Corollary 3.4 and Theorem 3.5: independent-set valuations satisfying the augmentation/exchange axioms are cryptomorphic to valuated matroids; this is the relevant "well-layered map" bridge.
- Theorem 4.1: relative truncation/elongation variants also yield valuated matroids.

These support the truncation/elongation side of formula (1), but the relative endpoint \(h_r=\mu_M\) uses the extra quotient hypothesis \(\nu\preceq\mu_M\), as already sketched in `answer.tex`.

### Verdict on the current lemma

I would not leave Lemma `local flag criterion` as stated.

The safe parts are:

1. Full arbitrary incidence (A), together with individual Pluecker relations, is exactly the BEZ/Jarra--Lorscheid valuated quotient condition.
2. If a sequence is already a sequence of valuated matroids and adjacent pairs are quotients, then it is a complete valuated flag over the tropical tract: Jarra--Lorscheid Theorem 2.17 plus Proposition 2.21, or BEZ Theorem 4.3.1 plus quotient composition.
3. In the finite uniform adjacent-rank case, adjacent three-term incidence relations alone imply the individual Pluecker relations by Joswig--Loho--Luber--Olarte Theorem 10.
4. Formula (1) is the expected valuated Higgs/truncation-elongation completion. Murota 1997 proves the basic truncation/elongation pieces; the top endpoint and relative support need the quotient-to-\(\mu_M\) argument already present in `answer.tex`.

The unsafe part is:

- The first assertion "nested relations (N) imply all arbitrary incidence relations (A)" for an arbitrary two-step quotient with rank gap \(b-a>1\) is not established by the cited sources. The proof route through Murota--Shioura is invalid because the two-layer support is not generally an \(M^\natural\)-convex/g-polymatroid domain. I did not find a primary theorem saying that endpoint nested flag relations alone generate arbitrary endpoint incidence for nonuniform \(\infty\)-valued supports.

I ran a small sanity check with Z3 for finite uniform cases \(n=6,7\), ranks \((2,4),(2,5),(3,5)\), values in \(\{0,1\}\) and some \(\{0,1,2\}\). It found no counterexample to nested-implies-arbitrary. This is only evidence; it is not a substitute for a theorem, and it does not repair the citation.

### Suggested replacement text for `answer.tex`

Replace the current lemma with a more conservative one:

```tex
\begin{lemma}[safe local flag input]\label{lem:localflag}
Let \(g_0,\ldots,g_r\) be nonzero tropical coordinate vectors whose
ordinary supports form a complete ordinary flag matroid with rank \(0\)
bottom and top support \(M\).

If each \(g_j\) is a valuated matroid and each adjacent pair
\((g_j,g_{j+1})\) satisfies the adjacent Pluecker flag relations
\[
 \min\{g_j(Sx)+g_{j+1}(Syz),
        g_j(Sy)+g_{j+1}(Sxz),
        g_j(Sz)+g_{j+1}(Sxy)\}
\]
with the minimum attained at least twice for all finite terms, then
\((g_0,\ldots,g_r)\) is a complete valuated flag matroid.
Consequently \(g_i\preceq g_j\) for all \(i<j\).

In the finite uniform adjacent-rank case, the hypothesis that the
\(g_j\) are valuated matroids may be omitted, by
Joswig--Loho--Luber--Olarte, Theorem 10.
\end{lemma}
```

Then cite:

```tex
By Jarra--Lorscheid, Theorem 2.17, adjacent quotients over the perfect
tropical tract imply a flag \(\mathbb T\)-matroid; by Proposition 2.21
this is the same as a BEZ valuated flag matroid.  Equivalently, by
BEZ Theorem 4.3.1 and Corollary 4.3.2, adjacent inclusions of tropical
linear spaces compose.
```

For formula (1), I recommend a separate lemma:

```tex
\begin{lemma}[Higgs completion inside \(M\)]
If \(\nu\preceq\mu_M\) has rank \(k\), the functions \(h_j\) defined by
(1) form a complete valuated flag from rank \(0\) to rank \(r=\rk M\),
with \(h_k=\nu\) and \(h_r\) projectively equal to \(\mu_M\).
\end{lemma}
```

Proof references/text:

- For \(j\le k\), cite Murota 1997, Theorem 2.1, for valuated truncation.
- For \(j\ge k\), either cite the \(M^\natural\)-concave/Higgs convolution viewpoint (Murota 1997 Theorem 3.5/Corollary 3.4, plus the quotient endpoint) or keep the direct proof. The direct endpoint proof in `answer.tex` is useful and should stay.
- To get all quotient relations once adjacent layers are known, cite Jarra--Lorscheid Theorem 2.17/Proposition 2.21 or BEZ Corollary 4.3.2.

### Bottom line

The literature supports an adjacent/full-flag criterion, and it supports the Higgs completion strategy. It does **not** support the current two-step "nested relations imply arbitrary incidence" assertion under the stated hypotheses. I recommend deleting that assertion or labeling it as a separate conjectural/local-generation lemma unless a dedicated reference is found.
