## Focused findings on the flat-coordinate duality lemma

I read `problem_documents_readonly/problem.txt`, `answer.tex`, and `research_notes.tex`, then downloaded and inspected the requested sources.  The key conclusion is:

**I did not find a literature theorem that directly implies the missing lemma for an arbitrary modular geometric lattice with a flat-lattice anti-automorphism.**  The standard duality theorems prove ordinary ground-set-complement duality for valuated flag matroids, but the proposed map
\[
  p^\perp(A)=\bar p((\operatorname{cl} A)^\perp)
\]
is not ordinary matroid duality unless the flat opposition is induced by Boolean set complement or an equivalent element-level complement.  I also did not find a proof that a smaller/nested set of incidence relations generates the full Brandt--Eur--Zhang incidence relations.

The computation below found no counterexamples.

## Literature inspected

Files downloaded/converted:

- `papers/brandt_eur_zhang_2005.13727.pdf`, `.txt`, and source in `papers/bez_src/`.
- `papers/hirai_1802.08809.pdf`, `.txt`, and source in `papers/hirai_src/`.
- Additional relevant: `papers/jarra_lorscheid_2204.04658.pdf/.txt` (flag matroids with coefficients), `papers/haque_1211.2841.pdf/.txt`, `papers/murota_compression_2005.12526.pdf/.txt`.

Precise BEZ statements:

- BEZ Definition 4.2.1 defines the full tropical incidence-Plucker relations
  \[
    \bigoplus_{j'\in J'\setminus I'} P_{I'\cup j'}P_{J'\setminus j'},
    \qquad |I'|=r-1,\ |J'|=s+1.
  \]
- BEZ Definition 4.2.2 defines valuated matroid quotients by the valuated exchange inequality.
- BEZ Proposition 4.2.3 states that points on \(FlDr(r,s;n)\) are exactly pairs of valuated matroids forming a valuated quotient; in particular the displayed incidence relations are sufficient and necessary.
- BEZ Theorem 4.3.1 states \(\mu \twoheadleftarrow \nu\) iff \(\overline{\operatorname{trop}}(\mu)\subseteq \overline{\operatorname{trop}}(\nu)\), and hence valuated flag matroids are exactly flags of projective tropical linear spaces.
- BEZ Corollary 4.3.2 records composition, minors, and ordinary duality behavior for quotients.  This is ordinary duality \(\mu^*([n]\setminus I)=\mu(I)\), not the flat-opposition map in the manuscript.

Hirai:

- Hirai Theorem 4.26 constructs a complete valuated matroid from a uniform semimodular lattice.
- Hirai Theorem 4.30 constructs the uniform semimodular lattice \(L(\omega)=T(\omega)\cap \mathbb Z^E\) from an integer-valued valuated matroid.
- Hirai Lemma 4.31 identifies intervals \([x,x+\mathbf 1]\) with flat lattices of initial matroids.
- Hirai Theorem 5.3 identifies modular valuated matroids with Euclidean buildings of type A.

These are strong single-valuated-matroid/building results, but I found no quotient/flag or opposition theorem there that gives the relative Dressian involution.

Flag matroids with coefficients:

- Jarra--Lorscheid Theorem 2.4 gives the cryptomorphism for flag \(F\)-matroids: a sequence is a flag iff \(C^*(M_i)\subseteq V^*(M_j)\) for \(i<j\).
- Proposition 2.11 proves ordinary duality of quotients: \(N\twoheadrightarrow M\) iff \(M^*\twoheadrightarrow N^*\).
- Theorem 2.13 gives ordinary duality for flag \(F\)-matroids.
- Proposition 2.21 identifies BEZ valuated flag matroids with flag matroids over the tropical hyperfield.

Again, this proves ordinary ground-set duality for flags with coefficients, but not the closure-and-flat-opposition operation needed here.

Haque's unpublished paper has Lemma 1 and Theorem 1 giving ordinary tropical duality and incidence relations for flags.  This is subsumed by BEZ Theorem 4.3.1.  I would not cite Haque as the main support, especially because BEZ explicitly flags an error in a different part of Haque's polytope argument.

## Direct proof attempt

The ordinary Boolean/ground-set-complement proof is completely clear.  If \(p,q\) have ranks \(a<b\), then the relation
\[
  \mathcal I_{a,b}(p,q;S,T)
\]
is sent by ordinary duality to
\[
  \mathcal I_{n-b,n-a}(q^*,p^*;E\setminus T,E\setminus S),
\]
because the term indexed by \(i\in T\setminus S\) becomes
\[
  q^*((E\setminus T)\cup i)+p^*((E\setminus S)\setminus i)
  =q(T\setminus i)+p(S\cup i).
\]
This proves relation-by-relation invariance for ordinary flag duality and matches Jarra--Lorscheid/BEZ.

For the manuscript's flat opposition, the analogous proof would need the following additional finite "dualizing frame" lemma.

Given dual-rank incidence data \(S',T'\), with \(|S'|=r-b-1\), \(|T'|=r-a+1\), one needs to realize the finite terms
\[
  q(\operatorname{cl}(S'\cup i)^\perp)
  +p(\operatorname{cl}(T'\setminus i)^\perp)
\]
as the terms of some original incidence relation \(\mathcal I_{a,b}(p,q;S,T)\), after perhaps deleting all-\(\infty\) terms.  Concretely, one wants a term-index bijection \(i\mapsto \phi(i)\) and subsets \(S,T\) such that
\[
  \operatorname{cl}(S\cup \phi(i))
    =\operatorname{cl}(T'\setminus i)^\perp,\qquad
  \operatorname{cl}(T\setminus \phi(i))
    =\operatorname{cl}(S'\cup i)^\perp.
\]
In the Boolean case this is exactly \(S=E\setminus T'\), \(T=E\setminus S'\), \(\phi(i)=i\).

For nested data \(S'\subseteq T'\) with the expected ranks, this should follow from a projective-frame statement in the modular interval
\[
  [\operatorname{cl}(T')^\perp,\operatorname{cl}(S')^\perp],
\]
where the atoms corresponding to deletions from \(T'\) are replaced by a dual frame.  I did not find a citable statement or complete proof of this frame lemma.  More importantly, BEZ's incidence relations allow arbitrary, non-nested \(S',T'\).  I found no proof that the nested incidence relations generate the full valuated quotient condition, and the current notes already warn that weaker interval-minimum conditions are insufficient.

So the exact remaining obstruction is:

1. Prove the above dualizing-frame realization for arbitrary subset-indexed incidence relations in a modular geometric lattice; or
2. Prove/cite that the full quotient flag Dressian is generated, modulo Plucker relations and flat-constancy, by the nested relations where the interval-frame argument applies.

Without one of these, I would not claim the lemma is closed.

## Computational testing

Script: `code/flat_duality_tests.py`.

It checks:

- flat closures and supplied opposition maps;
- standard 3-term tropical Plucker relations;
- all subset-indexed incidence relations \(\mathcal I_{a,b}\), not interval summaries;
- quotient-of-\(M\) via incidence with the trivial rank-\(r\) valuation \(\mu_M\);
- transformed individual quotients and transformed quotient pairs.

Primary log: `data/flat_duality_tests_round1.json`.

Targeted log: `data/direct_sum_rank2_finite_012.json`.

Summary:

| Matroid | Search | Quotients found | Pair/flag checks | Failures |
|---|---:|---:|---:|---:|
| Boolean \(U_{4,4}\) | exhaustive over \(\{0,1,\infty\}\) | ranks \(0..4\): \(1,66,210,66,1\) | exhaustive where small, sampled 2000 pairs otherwise | 0 |
| \(U_{2,4}\) | exhaustive over \(\{0,1,\infty\}\) | rank 1: 10 | all rank pairs exhaustive | 0 |
| \(U_{2,5}\) | exhaustive over \(\{0,1,\infty\}\) | rank 1: 12 | all rank pairs exhaustive | 0 |
| Fano \(PG(2,2)\) with dot-product polarity | exhaustive over \(\{0,1,\infty\}\) | ranks 1,2: 51 each | rank (1,2): 445 valid sampled flags | 0 |
| \(U_{2,3}\oplus U_{2,3}\) | exhaustive for ranks 1,3; sampled rank 2 over \(\{0,1,\infty\}\) | ranks 1,3: 120 each; rank 2 sample: 46 | sampled nontrivial pairs | 0 |
| \(U_{2,3}\oplus U_{2,3}\), rank 2 only | exhaustive finite \(\{0,1,2\}^{11}\) up to projective normalization | 632 rank-2 quotients | dual quotient check | 0 |
| \(PG(2,3)\) with dot-product polarity | random over \(\{0,1,\infty\}\) | sparse: rank 1: 2, rank 2: 3 | all found pairs | 0 |

No counterexample was found.  The tests support the candidate, including non-adjacent ranks in the sampled pair checks, but they do not replace the missing arbitrary subset-indexed incidence proof.

## Recommended next step

The most promising route is to formulate and prove the "dualizing frame" lemma above in pure modular-geometric-lattice language.  If it can be proved for arbitrary \(S',T'\), the flat-coordinate duality lemma follows relation-by-relation from BEZ Proposition 4.2.3.  If it can only be proved for nested \(S'\subseteq T'\), then the remaining task is a separate algebraic/tropical generation theorem for incidence relations after imposing Plucker and flat-constancy.
