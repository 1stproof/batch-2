# Compute worker reply — round 7
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-008-20260529T215332Z-6a40eb14/ac_workspaces/prob-008-5722abb22c2d/compute
zip: /data/output/workflow_runs/firstproof-prob-008-20260529T215332Z-6a40eb14/agents/Compute-c1-ae9fdf/compute_workspace_round_7.zip

---

# Round 7 report

I read the current `answer.tex` and `research_notes.tex`.  The two genuinely open items are exactly the ones isolated there.  My conclusion is:

* The complete-flag adjacent criterion has a clean nonuniform, \(\infty\)-valued reference/proof via Jidong Wang's codimension-one relative Dressian theorem.
* I did not find a proof or exact theorem for the two-rank non-adjacent endpoint criterion.  I ran targeted Z3 searches; no small counterexample was found in the requested rank \((2,4)\) cases, but the theorem remains unproved from this round.

## 1. Complete-flag adjacent criterion: resolved

The relevant reference is:

> Jidong Wang, *Lorentzian polynomials and the incidence geometry of tropical linear spaces*, arXiv:2412.12059.  In the local source `papers/wang_2412.12059_src/arXiv2026.tex`, see Theorem `\ref{thm:dressian-cut-out-by-three-term}`: “Let \(\mu\) be a valuated matroid. Then \(\Dr^1(\mu)\) is cut out by the three-term incidence relations.”  Around line 420 Wang explicitly says this extends Joswig--Loho--Luber--Olarte Theorem 3.10, which treated the uniform finite case.

Wang proves the nonuniform support issues directly.  In the same source, the preceding support lemma proves that a rank \(d-1\) function \(\theta\) satisfying the incidence relations against a rank \(d\) valuated matroid \(\mu\) has matroidal support; the theorem then proves all incidence relations from the three-term ones.  The proof allows \(\infty\)-values and handles degenerate/parallel hyperplanes separately before the concurrent three-term case.

LaTeX-ready replacement statement:

```tex
\begin{proposition}[complete-flag adjacent criterion]
Let \(w_0,\ldots,w_r\) be functions
\[
        w_j:\binom Ej\longrightarrow \mathbb R\cup\{\infty\}
\]
with nonempty ordinary complete-flag support, with \(w_0(\emptyset)=0\),
and with \(w_r\) a valuated matroid.  Suppose that for every
\(1\le j<r\), every \(S\in\binom E{j-1}\), and every distinct
\(x,y,z\notin S\), the adjacent tropical incidence relation
\[
\min\{w_j(Sx)+w_{j+1}(Syz),\,
      w_j(Sy)+w_{j+1}(Sxz),\,
      w_j(Sz)+w_{j+1}(Sxy)\}
\]
is attained at least twice, with the usual all-\(\infty\) convention.
Then each \(w_j\) is a valuated matroid and
\[
        w_0\preceq w_1\preceq\cdots\preceq w_r .
\]
\end{proposition}

\begin{proof}
Descend on \(j\).  Assume \(w_{j+1}\) is a valuated matroid.
Wang's theorem that the codimension-one relative Dressian
\(\Dr^1(w_{j+1})\) is cut out by the three-term incidence relations
applies without a uniformity hypothesis and with \(\infty\)-valued
coordinates.  The displayed adjacent relations are precisely those
three-term incidence relations for a rank \(j\) elementary quotient of
\(w_{j+1}\).  Hence \(w_j\) is a rank \(j\) valuated matroid and
\(w_j\preceq w_{j+1}\).  Starting from the valuated top layer \(w_r\)
and iterating proves this for \(j=r-1,\ldots,1\).  The rank-zero layer
is the trivial valuated matroid and is automatically a quotient of
\(w_1\).  Composition of valuated quotients is
Brandt--Eur--Zhang Corollary 4.3.2, equivalently Jarra--Lorscheid
Theorem 2.17/Proposition 2.21 over the perfect tropical tract.
\end{proof}
```

This is stronger and more precise than citing Murota--Shioura local
\(M^\natural\)-exchange.  Murota--Shioura Theorem 4.2 requires the full
local \(M^\natural\)-exchange package \(L1,L2,L3\) on an
\(M^\natural\)-convex domain; the displayed adjacent flag equations are
only the cross-rank \(L2\)-type equations.  Wang's theorem is exactly the
missing nonuniform adjacent-rank Pluecker-generation result.

Related references:

* Joswig--Loho--Luber--Olarte, *Generalized permutahedra and positive flag Dressians*, IMRN 2023, Theorem 3.10: finite uniform adjacent incidence implies the two adjacent functions are valuated matroids.
* Brandt--Eur--Zhang, *Tropical flag varieties*, Adv. Math. 384 (2021), Definition 4.2.1, Proposition 4.2.3, Theorem 4.3.1, Corollary 4.3.2: incidence-Pluecker relations, valuated flag matroids, tropical linear-space inclusions, and composition of valuated quotients.
* Jarra--Lorscheid, *Flag matroids with coefficients*, Adv. Math. 436 (2024), Theorem 2.17 and Proposition 2.21: over the perfect tropical tract, adjacent quotient chains are flags, but note this assumes the individual layers are already valuated matroids; Wang supplies that missing adjacent Pluecker-generation step.

## 2. Two-rank local quotient criterion

I did not find an exact theorem proving the desired non-adjacent criterion:

\[
\text{individual valuated matroids}
 + \text{ordinary support quotient}
 + \text{nested endpoint incidence }(S\subseteq T)
 \Longrightarrow \text{full BEZ incidence.}
\]

The closest literature I found is useful but not sufficient:

* Brandenburg--Loho--Smith, *Quotients of M-convex sets and M-convex functions*, arXiv:2403.07751, Theorem 1.3 and Remark 5.7.  Their exchange condition (C) is the full BEZ-valuated quotient exchange for arbitrary pairs of bases, and in the valuated matroid case it is equivalent to the minimizer/initial-matroid quotient condition.  However, the nested endpoint equations are only the special case \(|B_p\setminus B_q|=1\) of that exchange condition.  I found no statement in BLS that this restricted local case promotes to full exchange for non-elementary rank gaps.
* Murota--Shioura, *Simpler exchange axioms for M-concave functions on generalized polymatroids*, Theorem 4.2, is not directly applicable: the union of two non-adjacent homogeneous layers is generally not an \(M^\natural\)-convex domain, e.g. the union of the rank \(2\) and rank \(4\) layers of \(U_{4,6}\).
* Murota's multiple exchange theorem still looks like the right possible tool for an induction on \(|B_p\setminus B_q|\), but I did not manage to close the cancellation/monotonicity step.

So I recommend leaving Criterion `\ref{crit:local}` open unless the Author can supply an induction proof.  A safe wording is: “This is not a consequence of the standard local \(M^\natural\)-exchange theorem, since the two-layer domain need not be \(M^\natural\)-convex.”

## 3. Z3 searches for the two-rank criterion

I wrote `code/two_rank_local_criterion_z3.py`.  It encodes:

* rank \(a,b\) variables over \(\{0,\ldots,K,\infty\}\);
* individual tropical Pluecker relations for \(p\) and \(q\);
* ordinary support quotient order using the \(0/\infty\) full incidence condition;
* all nested endpoint incidence relations for values;
* a requested unique-min failure of a non-nested full incidence relation.

For rank \((2,4)\), a failed non-nested relation is, up to relabeling, \(I=\{0\}\), \(J=\{1,2,3,4,5\}\) on \(n=6\), and likewise with one unused element on \(n=7\).  Thus the fixed-relation UNSAT runs are WLOG, not merely partial checks.

| case | alphabet | result | log |
|---|---:|---:|---|
| \(n=6,(a,b)=(2,4)\) | \(\{0,1\}\) finite | UNSAT | `data/two_rank_local_n6_a2_b4_K1_finite.json` |
| \(n=6,(2,4)\) | \(\{0,1,\infty\}\) | UNSAT | `data/two_rank_local_n6_a2_b4_K1_inf.json` |
| \(n=6,(2,4)\), fixed failure WLOG | \(\{0,1,2\}\) finite | UNSAT | `data/two_rank_local_n6_a2_b4_K2_finite_fixed.json` |
| \(n=6,(2,4)\), fixed failure WLOG | \(\{0,1,2,\infty\}\) | UNSAT | `data/two_rank_local_n6_a2_b4_K2_inf_fixed.json` |
| \(n=7,(2,4)\), fixed failure WLOG | \(\{0,1,\infty\}\) | UNSAT | `data/two_rank_local_n7_a2_b4_K1_inf_fixed.json` |
| \(n=7,(2,4)\), fixed failure WLOG | \(\{0,1,2,\infty\}\) | timeout/unknown | `data/two_rank_local_n7_a2_b4_K2_inf_fixed.json` |

No counterexample was found.  The \(n=7,K=2,\infty\) case timed out after 180 seconds.

## 4. Cautionary support check

I also patched `code/complete_flag_adjacent_search.py` to optionally enforce ordinary support-matroid constraints.  Before adding such constraints, the Boolean \(U_{6,6}\) complete-flag search found an invalid “counterexample” with rank-3 finite support
\[
\{024,\ 045,\ 134,\ 245\},
\]
all values equal.  It fails the rank-3 Pluecker relation with \(S=\{4\}\) and \(\{0,1,2,3\}\): only the term \((024,134)\) is finite.  This confirms that the ordinary support hypothesis in the complete-flag criterion is essential, but it is not a counterexample to the criterion as stated.
