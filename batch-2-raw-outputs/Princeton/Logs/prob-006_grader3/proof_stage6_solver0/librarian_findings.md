# Librarian Findings — grader3_acd8bd225c74_proof_stage6_solver0_20260531_013326
**Generated:** 2026-05-31T01:36:25  
**Inputs:** notebook=14800 chars, proof=8363 chars, gap_report=2685 chars  
**Date restriction:** none (FP v2 — recent works allowed)  

---

## Citation IDs (aggregator-only)
```json
{
  "arxiv": [],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

## Citation IDs (union: aggregator + all draws)
```json
{
  "arxiv": [],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

---

# Stage 1 — Gauntlet (aggregator output)

## VERY RELATED
- [Paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society — IDs: no ID — (Defines the exact recursive continued-fraction calculus for tree intersection matrices, structurally proving effective branch weights remain strictly greater than 1.) — search: neumann a calculus for plumbing pdf
- [Book] J.W.S. Cassels / 1978 — Rational Quadratic Forms — London Mathematical Society Monographs (Academic Press) — IDs: no ID — (Provides the explicit geometry of numbers and diophantine bounding algebra required to rigorously quantify the integer gap strictly above a continuous real minimum.) — search: geometry of numbers quadratic forms notes pdf
- [Paper] U. Fincke, M. Pohst / 1985 — Improved methods for calculating vectors of short length in a lattice, including a complexity analysis — Mathematics of Computation — IDs: no ID — (Supplies the canonical algebraic inequalities for bounding evaluations over an integer lattice using Cholesky factorization diagonals.) — search: fincke pohst calculating vectors lattice pdf
- [Book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences — SIAM — IDs: no ID — (Proves Schur complements of strictly diagonally dominant M-matrices preserve strict diagonal dominance, structurally resolving the proof's boundary collapse oversight.) — search: berman plemmons nonnegative matrices pdf

## RELATED
- [Book] J.H. Conway, N.J.A. Sloane / 1999 — Sphere Packings, Lattices and Groups (3rd Edition) — Springer — IDs: no ID — (Foundational proof that strictly positive-definite, integer-valued quadratic forms structurally assign a norm of at least 1 to all non-zero vectors.) — search: elkies lattices linear codes invariants pdf
- [Paper] F. Dörfler, F. Bullo / 2013 — Kron reduction of graphs with applications to electrical networks — IEEE Transactions on Circuits and Systems I: Regular Papers — IDs: no ID — (Provides the canonical topological induction proving that sequential leaf-to-root Schur complementation mathematically preserves the quadratic energy form.) — search: kron reduction of graphs dorfler bullo pdf
- [Book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory — Springer — IDs: no ID — (Details explicit block-matrix Schur complements and rigorous zero-energy propagation lemmas for connected trees to finalize the boundary step.) — search: spielman spectral and algebraic graph theory pdf
- [Monograph] H. B. Laufer / 1971 — Normal Two-Dimensional Singularities — Annals of Mathematics Studies 71, Princeton University Press — IDs: no ID — (Canonical topological source for the recursive evaluation algorithm of intersection matrix determinants on weighted trees.) — search: neumann calculus for plumbing applied to topology pdf

## SOMEWHAT RELATED
- [Monograph] D. Eisenbud, W. D. Neumann / 1985 — Three-dimensional link theory and invariants — Princeton University Press — IDs: no ID — (Rigorously evaluates positive-definite intersection forms of weighted trees via recursive continued-fraction identities.) — search: neumann a calculus for plumbing pdf
- [Book] R.B. Bapat / 2010 — Graphs and Matrices — Springer — IDs: no ID — (Supplies standard linear algebra formulas for inverses of tree matrices and block matrix Schur reductions over graphs.) — search: bapat graphs and matrices springer pdf
- [Book] N. Bourbaki / 1968 — Lie Groups and Lie Algebras, Chapters 4-6 — Springer — IDs: no ID — (Classifies connected graphs supporting positive-definite symmetric integer forms, proving non-zero vectors strictly bound away from zero.) — search: borcherds lie groups notes berkeley pdf

## NOT MUCH
- [Monograph] K. Murota / 2003 — Discrete Convex Analysis — SIAM Monographs on Discrete Mathematics and Applications — IDs: no ID — (Offers a modern proximity bounding framework for separable integer convex optimization, but direct diophantine inequalities are structurally simpler for this proof.) — search: discrete convex analysis murota pdf

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [Paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society — IDs: no ID
  - **Addresses:** Grader B's "Slip: The boundary collapse requires proving effective branch weights are strictly >1."
  - **Load-bearing piece:** The section on continued fractions for plumbing graphs proves that recursive continued fractions $[w_1, \dots, w_k]$ with topological components $w_i \ge 2$ fundamentally yield evaluations strictly $> 1$.

- [Paper] U. Fincke, M. Pohst / 1985 — Improved methods for calculating vectors of short length in a lattice, including a complexity analysis — Mathematics of Computation — IDs: no ID
  - **Addresses:** Grader A's "absence of explicit diophantine bounding algebra" and Grader B's "Fallacy: Step 5 asserts an integer minimum gap without proving any quantitative bound."
  - **Load-bearing piece:** Section 2 supplies the explicit algebraic inequalities bounding exact integer lattice displacement variances strictly above continuous minima using Cholesky decomposition diagonals.

- [Paper] F. Dörfler, F. Bullo / 2013 — Kron reduction of graphs with applications to electrical networks — IEEE Transactions on Circuits and Systems I: Regular Papers — IDs: no ID
  - **Addresses:** Grader B's "Slip: The Schur complement/factorization identity needs a clear induction proof."
  - **Load-bearing piece:** The main theorems on Kron reduction provide the exact topological induction proving that sequentially Schur complementing leaf nodes structurally preserves the graph Laplacian's quadratic energy form.

## SUPPORTING

- [Book] J.H. Conway, N.J.A. Sloane / 1999 — Sphere Packings, Lattices and Groups (3rd Edition) — Springer — IDs: no ID
  - Directly addresses Grader B's Scaffolding Question 1 by formally establishing that strictly positive-definite integral lattices assign a minimum norm $\ge 1$ to all non-zero vectors.

- [Book] J.W.S. Cassels / 1978 — Rational Quadratic Forms — London Mathematical Society Monographs (Academic Press) — IDs: no ID
  - Excellent background on the geometry of numbers to back up the diophantine gap bounds evaluated over integer lattices.

- [Book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences — SIAM — IDs: no ID
  - Useful background confirming that Schur complements of strictly diagonally dominant M-matrices mathematically preserve strict diagonal dominance, aiding the boundary oversight.

- [Book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory — Springer — IDs: no ID
  - Provides reliable auxiliary proofs for rigorous block matrix Schur reductions on connected tree graphs.

- [Book] R.B. Bapat / 2010 — Graphs and Matrices — Springer — IDs: no ID
  - Supplies standard linear algebraic formulas and topological properties for inverses of graph matrices and sub-branch absorption.

## REDUNDANT

- [Monograph] H. B. Laufer / 1971 — Normal Two-Dimensional Singularities — Annals of Mathematics Studies 71, Princeton University Press — IDs: no ID
  - Overlaps directly with Neumann 1981 in establishing the recursive continued-fraction calculus bounding effective weights for tree intersection matrices.

- [Monograph] D. Eisenbud, W. D. Neumann / 1985 — Three-dimensional link theory and invariants — Princeton University Press — IDs: no ID
  - Overlaps with Neumann 1981, covering the same rigorous topological bounds for positive-definite intersection forms of weighted trees.

## PERIPHERAL

- [Book] N. Bourbaki / 1968 — Lie Groups and Lie Algebras, Chapters 4-6 — Springer — IDs: no ID
  - While it classifies connected ADE graphs supporting positive-definite integer forms, it does not provide the Cholesky/Schur fractional bounding algebra required for this proof's specific continuous-to-discrete gap.

- [Monograph] K. Murota / 2003 — Discrete Convex Analysis — SIAM Monographs on Discrete Mathematics and Applications — IDs: no ID
  - Offers a proximity bounding framework for integer convex optimization, but the explicit Diophantine lattice bounds from Fincke-Pohst are structurally simpler and much better suited for addressing the quadratic deficit well here.

## UNFAMILIAR

*(None)*

---

# Stage 3 — Chapter Picker

## Sphere Packings, Lattices and Groups (3rd Edition) (J.H. Conway, N.J.A. Sloane, Springer, 1999)
_(IDs: no ID)_

Here are the most relevant chapters from Conway & Sloane’s *Sphere Packings, Lattices and Groups* to resolve the specific grader critiques.

**Chapter 2: Coverings, Lattices and Quantizers**
* **Which gap it addresses:** Grader B's Scaffolding Question 1 ("Why does an integer-valued positive definite bilinear form assign norm at least 1...").
* **Why:** This chapter formally introduces integral lattices. It establishes the elementary but fundamental property that if a positive definite symmetric bilinear form on a free abelian group (a lattice) maps pairs to integers (i.e., its Gram matrix is integral), the associated quadratic form $Q(x) = x \cdot x$ strictly produces non-negative integers. For any non-zero vector, the smallest strictly positive integer is strictly bounded below by 1. 

**Chapter 4: Certain Important Lattices and Their Properties**
* **Which gap it addresses:** Grader A's Critique 2 & Grader B's Scaffolding Questions 4 & 5 (the Step 5 Diophantine bounding and integer minimum gap).
* **Why:** By completing the square over the lattice, the functional $E_v(a) = a \cdot a - a \cdot v$ rewrites identically as $(a - v/2)^2 - v^2/4$. Minimizing this is formally equivalent to finding the shortest vector in a shifted lattice (a coset translation by half a lattice vector). This chapter extensively works out exact algebraic integer-displacements and minimal norms for the cosets/glue vectors of ADE root lattices (which precisely correspond to positive definite tree graphs), providing the blueprint for bounding the integer distance to fractional continuous minimizers.

**Chapter 15: On the Classification of Integral Quadratic Forms**
* **Which gap it addresses:** Grader B's Scaffolding Questions 2 & 3 (Schur complement / positive definiteness of effective branch weights).
* **Why:** This chapter provides the exhaustive conditions for an integral symmetric matrix to be positive definite. The recursive elimination of leaf weights into "effective rational weights" is a standard Cholesky factorization of the Gram matrix; the results here govern the bounds of principal minors and invariants, directly justifying why positive definiteness forces the effective branch weights to structurally exceed 1 (preventing the Step 4 boundary collapse).

**Chapter 21: Voronoi Cells of Lattices and Quantization Errors**
* **Which gap it addresses:** (beyond grader's named gaps) Structural rigorous isolation of the $a_v \notin \{0, 1\}$ domain constraint.
* **Why:** When $a_v \notin \{0, 1\}$, the evaluated vector is physically forced outside the immediate Voronoi cell of the continuous fractional minimizer $v/2$. This chapter's formalization of relevant vectors, holes, and lattice quantization establishes exactly how far a discrete lattice point must be from a given continuous coordinate depending on its structural bounds, which is exactly the continuous-to-discrete bounding algebra the solver skipped.

## Rational Quadratic Forms (J.W.S. Cassels, London Mathematical Society Monographs (Academic Press), 1978)
_(IDs: no ID)_

Here are the specific chapters and concepts from Cassels’s *Rational Quadratic Forms* (1978) that address the operational slips and structural fallacies flagged by the graders.

*Note: Since the book treats quadratic forms from the perspective of number theory and algebraic lattices rather than graph theory, you will need to map the "weighted trees" directly to their corresponding integral lattices.*

**Chapter 12 (approx.) — Reduction of Positive Definite Forms**
- **Which gap it addresses:** Grader A's Fallacy (Step 5 integer minimum gap without quantitative bounds) & Grader B's Scaffolding Q4.
- **Why:** This chapter covers the definitive bounding algebra for positive definite forms over integer lattices (including Minkowski and Korkine-Zolotareff reduction theory). It establishes strict geometric constants and algorithms for finding the true minimum of a quadratic form over $\mathbb{Z}^n$, which is exactly what the proof needs to rigorously prove the discrete variance "overrides" the displaced continuous negative well in Step 5, rather than relying on rhetorical leaps. 

**Chapter 1 (approx.) — Generalities / Diagonalization of Quadratic Spaces**
- **Which gap it addresses:** Grader B's Gap 3 (Schur complement/factorization identity needs a clear proof) & Scaffolding Q2.
- **Why:** The chapter covers the classical algorithmic procedure for completing the square (Lagrange's diagonalization) for symmetric bilinear forms. It formally relates the resulting recursive diagonal coefficients to the ratios of the determinants of principal minors. This is the exact algebraic mechanism behind the "effective weight" elimination steps acting on the graph Laplacian in Step 3. 

**Chapter on Forms over $\mathbb{Z}$ / Integral Lattices (approx. Chapter 8 or 9)**
- **Which gap it addresses:** Grader B's Scaffolding Q1 (Why does an integer-valued positive definite bilinear form assign norm at least 1 to every nonzero vector?).
- **Why:** This section formalizes the basic structural properties of positive definite integral lattices. It proves that since the quadratic space maps vectors in $\mathbb{Z}^V$ to integers, and the form is strictly positive definite, the value $x \cdot x$ for any non-zero element must strictly fall in the positive integers ($\mathbb{Z}_{>0}$). Therefore, $x \cdot x \ge 1$ is mathematically forced globally. 

**I do not believe this reference actually addresses:**
- **Grader A's Point 1 (Step 4 boundary collapse) & Grader B's Gap 4:** While Cassels explains lattice structures, the topological constraint that "effective branch weights are strictly $>1$" is an idiosyncratic consequence of the problem's specific graph-theoretic hypotheses ($w(x) \ge d_T(x)$ for $x \neq v$). You will not find graph leaf-reduction sequences or tree connectivity topology in Cassels; that requires a standard induction specific to the combinatorial tree structure.

## Nonnegative Matrices in the Mathematical Sciences (A. Berman, R. J. Plemmons, SIAM, 1994)
_(IDs: no ID)_

Here is a targeted selection from Berman and Plemmons based on the specific mathematical structures (Stieltjes/M-matrices) present in your graph Laplacian-like matrix.

**Chapter 6: M-Matrices**
*   **Which gap it addresses:** Grader B Gap 3 (Schur complement/factorization identity) and Grader B Gap 4 (boundary collapse / effective branch weights bounds).
*   **Why:** The problem's intersection matrix $M$ (where off-diagonals are $-1$ or $0$ and it is positive definite) is the exact definition of a *Stieltjes matrix*, which is a symmetric M-matrix. Chapter 6 contains the foundational theorems proving that the Schur complement of any M-matrix is also an M-matrix, and that Gaussian elimination without pivoting preserves this property. This rigorously justifies both the exact recursive Cholesky factorization identity and the strictly positive bounds on the recursive pivots (your "effective branch weights" $W(u)$).

**I do not believe this reference actually addresses any of the named gaps regarding discrete/Diophantine bounds.**
*   **Which gap it addresses:** Grader A Gap 2 and Grader B Gap 2 (the missing Diophantine bounding algebra / integer minimum gap).
*   **Why:** *Nonnegative Matrices in the Mathematical Sciences* is strictly a continuous matrix theory text focused on Perron-Frobenius theory, invariant cones, and M-matrices. It contains absolutely no tools for bounding discrete integer quadratic forms over lattices or resolving diophantine displacement variances, which are the core algebraic fallacies flagged in Step 5 of the proof. You will need a reference in geometry of numbers (e.g., Cassels) or discrete optimization to close those gaps.

## Algebraic Graph Theory (C. Godsil, G. Royle, Springer, 2001)
_(IDs: no ID)_

I do not believe this reference actually addresses any of the named gaps. 

**Why:** The proof is stuck on finding explicit Diophantine lower bounds for integer displacements in a generalized, weighted graph Laplacian, as well as recursive Schur complement identities for its branch structures. Godsil and Royle’s *Algebraic Graph Theory* is a foundational text focusing on the continuous spectra of standard adjacency and Laplacian matrices (where $w(x) = d(x)$), eigenvalue interlacing, and graph automorphisms. It does not contain diophantine bounding algebra, integer minimum gaps for quadratic forms, or the specialized intersection matrix theory (e.g., ADE classification or singularity resolution lattices) required to isolate and bound discrete solutions over $\mathbb{Z}$.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

**[Paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society**
- **Gap addressed:** Grader A critique 1 (Step 4 boundary collapse oversight) and Grader B critique 4 (proving effective branch weights are strictly >1).
- **Justification:** Section 2 directly resolves the boundary failure by analyzing positive-definite tree intersection matrices via recursive continued fractions, structurally proving that any dynamically updated effective branch weight must remain strictly $> 1$.

**[Paper] U. Fincke, M. Pohst / 1985 — Improved methods for calculating vectors of short length in a lattice, including a complexity analysis — Mathematics of Computation**
- **Gap addressed:** Grader A critique 2 (absence of explicit diophantine bounding algebra) and Grader B critique 2 (quantitative bound on the integer minimum gap).
- **Justification:** Section 2 provides the exact algebraic machinery required, deriving rigorous diophantine inequalities that bound coordinate displacement variances directly against the continuous minimum of a Cholesky-factorized quadratic form over an integer lattice.

**[Paper] F. Dörfler, F. Bullo / 2013 — Kron reduction of graphs with applications to electrical networks — IEEE Transactions on Circuits and Systems I: Regular Papers**
- **Gap addressed:** Grader B critique 3 (The Schur complement/factorization identity needs a clear induction proof).
- **Justification:** Section III supplies the canonical graph-theoretic topological induction, proving that step-by-step leaf elimination (Kron reduction) preserves the global quadratic form exactly as a recursive Schur complement.

## SUPPORTING

- **[Book] J.H. Conway, N.J.A. Sloane / 1999 — Sphere Packings, Lattices and Groups (3rd Edition)**
  *Provides the foundational lattice theory baseline verifying that strictly positive-definite integer forms assign a norm $\ge 1$ to all non-zero vectors.*
- **[Book] J.W.S. Cassels / 1978 — Rational Quadratic Forms**
  *Offers classical background on the geometry of numbers useful for verifying the general structure of integer gaps in quadratic forms.*
- **[Book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory**
  *Covers standard block-matrix Schur complements and connected tree evaluations to support algebraic graph reductions.*
- **[Book] R.B. Bapat / 2010 — Graphs and Matrices**
  *Standard reference for linear algebra applied to trees, supplying standard facts about inverse structures and minors.*
- **[Book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences**
  *Supports boundary collapse logic by proving that off-diagonal tree matrices (M-matrices) strictly preserve their diagonal dominance under Schur complementation.*

## REDUNDANT

- **[Monograph] H. B. Laufer / 1971 — Normal Two-Dimensional Singularities**
  *Overlaps with Neumann 1981; both evaluate the tree intersection determinants via identical plumbing calculus topological limits.*
- **[Monograph] D. Eisenbud, W. D. Neumann / 1985 — Three-dimensional link theory and invariants**
  *Overlaps with Neumann 1981; reiterates the same recursive continued-fraction identities for tree matrix evaluations.*

## PERIPHERAL

- **[Book] N. Bourbaki / 1968 — Lie Groups and Lie Algebras, Chapters 4-6**
  *Classifies roots of ADE graphs, but fundamentally lacks the explicit step-by-step diophantine bounding bounds needed to bridge the interior variance gap.*
- **[Monograph] K. Murota / 2003 — Discrete Convex Analysis**
  *Highly abstract modern optimization framework that applies to lattice proximity, but is wildly oversized and indirect for standard quadratic bounding algebra.*

## UNFAMILIAR

*(None — parametric memory is sufficient to confidently bucket the provided sources.)*

## Narrower draw 2
## LOAD-BEARING

- [Paper] U. Fincke, M. Pohst / 1985 — Improved methods for calculating vectors of short length in a lattice, including a complexity analysis — Mathematics of Computation — IDs: no ID — (Supplies the canonical algebraic inequalities for bounding evaluations over an integer lattice using Cholesky factorization diagonals.) — search: fincke pohst calculating vectors lattice pdf
  - **Addresses gap:** Grader A critique, Item 2 ("absence of explicit diophantine bounding algebra") and Grader B critique, Area for Improvement 2 ("asserts an integer minimum gap without proving any quantitative bound").
  - **Load-bearing piece:** Section 2 provides the explicit Diophantine bounding algebra (the Fincke-Pohst algorithm) required to strictly bound the exact minimum of a quadratic form over an integer lattice via the diagonals of its Cholesky factorization.

- [Paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society — IDs: no ID — (Defines the exact recursive continued-fraction calculus for tree intersection matrices, structurally proving effective branch weights remain strictly greater than 1.) — search: neumann a calculus for plumbing pdf
  - **Addresses gap:** Grader B critique, Area for Improvement 4 ("The boundary collapse requires proving effective branch weights are strictly >1") and Grader B critique, Scaffolding Question 3.
  - **Load-bearing piece:** Section 1 details the recursive continued-fraction calculus for tree intersection matrices, demonstrating how sequential structural elimination of leaves preserves effective branch weights that are strictly greater than 1.

- [Paper] F. Dörfler, F. Bullo / 2013 — Kron reduction of graphs with applications to electrical networks — IEEE Transactions on Circuits and Systems I: Regular Papers — IDs: no ID — (Provides the canonical topological induction proving that sequential leaf-to-root Schur complementation mathematically preserves the quadratic energy form.) — search: kron reduction of graphs dorfler bullo pdf
  - **Addresses gap:** Grader B critique, Area for Improvement 3 ("The Schur complement/factorization identity needs a clear induction proof").
  - **Load-bearing piece:** Section III establishes the formal topological induction proving that sequential Schur complementation (Kron reduction) identically preserves the quadratic energy form over trees.

## SUPPORTING

- [Book] J.W.S. Cassels / 1978 — Rational Quadratic Forms — London Mathematical Society Monographs (Academic Press) — IDs: no ID — (Provides the explicit geometry of numbers and diophantine bounding algebra required to rigorously quantify the integer gap strictly above a continuous real minimum.) — search: geometry of numbers quadratic forms notes pdf
  - *Note:* Useful background reference for the geometry of numbers regarding bounds on discrete minima over shifted lattices.

- [Book] J.H. Conway, N.J.A. Sloane / 1999 — Sphere Packings, Lattices and Groups (3rd Edition) — Springer — IDs: no ID — (Foundational proof that strictly positive-definite, integer-valued quadratic forms structurally assign a norm of at least 1 to all non-zero vectors.) — search: elkies lattices linear codes invariants pdf
  - *Note:* Directly answers Grader B critique, Scaffolding Question 1 by formally establishing that integer-valued positive definite forms give non-zero vectors a norm $\ge 1$.

- [Book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory — Springer — IDs: no ID — (Details explicit block-matrix Schur complements and rigorous zero-energy propagation lemmas for connected trees to finalize the boundary step.) — search: spielman spectral and algebraic graph theory pdf
  - *Note:* Supplies fundamental tree Laplacians and zero-energy propagation lemmas to help patch the boundary collapse oversight flagged in Grader A critique, Item 1.

## REDUNDANT

- [Monograph] H. B. Laufer / 1971 — Normal Two-Dimensional Singularities — Annals of Mathematics Studies 71, Princeton University Press — IDs: no ID — (Canonical topological source for the recursive evaluation algorithm of intersection matrix determinants on weighted trees.) — search: neumann calculus for plumbing applied to topology pdf
  - *Overlap:* Covers the same territory as Neumann (1981) regarding recursive continued fractions for evaluating determinants on weighted trees.

- [Monograph] D. Eisenbud, W. D. Neumann / 1985 — Three-dimensional link theory and invariants — Princeton University Press — IDs: no ID — (Rigorously evaluates positive-definite intersection forms of weighted trees via recursive continued-fraction identities.) — search: neumann a calculus for plumbing pdf
  - *Overlap:* Fully encompassed by Neumann's earlier 1981 load-bearing paper on effective branch weights.

- [Book] R.B. Bapat / 2010 — Graphs and Matrices — Springer — IDs: no ID — (Supplies standard linear algebra formulas for inverses of tree matrices and block matrix Schur reductions over graphs.) — search: bapat graphs and matrices springer pdf
  - *Overlap:* Redundant to Dörfler & Bullo (2013) and Godsil & Royle (2001) for Schur complementation identities.

## PERIPHERAL

- [Book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences — SIAM — IDs: no ID — (Proves Schur complements of strictly diagonally dominant M-matrices preserve strict diagonal dominance, structurally resolving the proof's boundary collapse oversight.) — search: berman plemmons nonnegative matrices pdf
  - *Note:* Discusses M-matrices and diagonal dominance, but does not provide the precise graph-theoretic induction logic strictly necessary for completing the exact factorization on this specific tree formulation.

- [Book] N. Bourbaki / 1968 — Lie Groups and Lie Algebras, Chapters 4-6 — Springer — IDs: no ID — (Classifies connected graphs supporting positive-definite symmetric integer forms, proving non-zero vectors strictly bound away from zero.) — search: borcherds lie groups notes berkeley pdf
  - *Note:* Classifies positive-definite spaces (e.g., Dynkin/Coxeter graphs), but lacks explicit mechanical tools needed to close functional bounding gaps or compute diophantine gap limits.

## UNFAMILIAR

- [Monograph] K. Murota / 2003 — Discrete Convex Analysis — SIAM Monographs on Discrete Mathematics and Applications — IDs: no ID — (Offers a modern proximity bounding framework for separable integer convex optimization, but direct diophantine inequalities are structurally simpler for this proof.) — search: discrete convex analysis murota pdf
  - *Note:* I do not remember the contents well enough to determine if its framework resolves the integer variance bound in a manner fitting this specific proof.

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and topic-keyed substitutes to help you close the gaps identified by the graders. The near-miss proof essentially reconstructs the **Schur complement (Kron reduction) of an M-matrix** and implicitly attempts the **Fincke-Pohst algorithm** for lattice bounding, but skips the requisite diophantine algebra.

Here is the literature to formalize these steps.

### 1. The Effective Weight Lower Bound & Boundary Collapse
**Grader Target:** Grader A (Slip 1: boundary collapse ignores $W(y)=1, a_y=-1$) and Grader B (Slip 4: proving effective weights are strictly $>1$). 

- **Authors:** Berman, A. / Plemmons, R. J.
- **Year:** 1994
- **Title:** Nonnegative Matrices in the Mathematical Sciences
- **Type:** Book
- **Venue:** SIAM (Classics in Applied Mathematics series)
- **Main result or relevant chapter/section:** Chapter 6 comprehensively develops the theory of non-singular **M-matrices** (symmetric positive-definite matrices with non-positive off-diagonals). It proves that any principal submatrix or Schur complement of an M-matrix is strictly an M-matrix itself.
- **Topic needed for this proof:** The theorem that Schur complements of strictly diagonally dominant M-matrices preserve strict diagonal dominance, algebraically guaranteeing that the sequence of pivot weights $W(u)$ remains strictly bounded away from $1$.
- **Open-access substitute for that topic:** (open-access for topic: Schur complements of M-matrices) — Gallier, J. / 2010 / "Schur Complements and Applications" / University of Pennsylvania lecture notes
- **Connection:** This is the missing theoretical hammer for Step 4. Because your tree Laplacian is a positive definite M-matrix (due to $w(x) \ge d(x)$), Berman & Plemmons provides the immediate proof that $W(u) > 1$ universally, rescuing your boundary collapse deduction $a_y(W(y)a_y+1) = 0 \implies a_y = 0$.
- **Web search query:** `berman plemmons nonnegative matrices pdf`
- **Confidence (bibliographic):** HIGH

### 2. The Diophantine Integer Minimum Bounding
**Grader Target:** Grader A (Fallacy 2: absence of explicit diophantine bounding algebra) and Grader B (Question 4: how to compute exact minimum over integers).

- **Authors:** Fincke, U. / Pohst, M.
- **Year:** 1985
- **Title:** Improved methods for calculating vectors of short length in a lattice, including a complexity analysis
- **Type:** Paper
- **Venue:** Mathematics of Computation
- **Main result or relevant chapter/section:** Introduces the canonical "sphere decoding" algorithm for finding the minima of integral quadratic forms. It explicitly demonstrates how to use the diagonal elements of a Cholesky factorization to strictly bound the discrete lattice values above the continuous continuous minimum.
- **Topic needed for this proof:** The exact diophantine bounding inequalities $(x_k - \sum q_{ij} x_j)^2 \ge \delta$ that rigorously evaluate the jump from a continuous Cholesky minimum to the nearest discrete integer lattice vector.
- **Open-access substitute for that topic:** (open-access for topic: Fincke-Pohst method and integer bounding using Cholesky diagonals) — Agrell, E. et al. / 2002 / "Closest Point Search in Lattices" / IEEE Transactions on Information Theory (widely hosted on authors' university pages).
- **Connection:** Your Step 5 successfully identifies the continuous minimum $-\frac{w(v) - \Delta}{4}$, but then rhetorically waves away the jump to the integers. The diophantine inequalities in Fincke-Pohst are precisely the "explicit bounding algebra" Grader A demands to prove that the constrained topological sum physically overrides this negative well.
- **Web search query:** `fincke pohst calculating vectors lattice pdf`
- **Confidence (bibliographic):** HIGH

### 3. Tree Induction and the Factorization Identity
**Grader Target:** Grader B (Slip 3: The Schur complement/factorization identity needs a clear induction proof).

- **Authors:** Dörfler, F. / Bullo, F.
- **Year:** 2013
- **Title:** Kron reduction of graphs with applications to electrical networks
- **Type:** Paper
- **Venue:** IEEE Transactions on Circuits and Systems I: Regular Papers
- **Main result or relevant chapter/section:** Provides the formal topological induction proving that sequentially taking Schur complements (Kron reduction) of a tree Laplacian structurally preserves the global quadratic form while updating the effective edge/node weights.
- **Topic needed for this proof:** The exact algebraic induction establishing that recursive leaf-to-root Schur complementation on a tree explicitly preserves the quadratic energy form without loss.
- **Open-access substitute for that topic:** (open-access for topic: exact topological induction of graph Kron reduction) — Dörfler, F. / 2012 / "Kron reduction of graphs with applications to electrical networks" / arxiv survey preprint.
- **Connection:** Instead of inventing the induction logic for Step 3 yourself, cite the Kron reduction of trees. It maps perfectly to your recursive elimination of sub-branches, satisfying the grader's request for a clear, canonical induction proof of the continuous factorization. 
- **Web search query:** `kron reduction of graphs dorfler bullo pdf`
- **Confidence (bibliographic):** HIGH

### 4. Continuous Fractions and Tree Intersections
**Grader Target:** General framing and the $W(u)$ recursive calculus.

- **Authors:** Eisenbud, D. / Neumann, W. D.
- **Year:** 1985
- **Title:** Three-dimensional link theory and invariants
- **Type:** Monograph
- **Venue:** Princeton University Press (Annals of Mathematics Studies)
- **Main result or relevant chapter/section:** The appendix / plumbing sections rigorously evaluate the positive definite intersection forms of weighted trees. They establish that diagonalizing the intersection form equates to evaluating the determinant via the exact recursive continued-fraction identity $W(u) = w(u) - \sum \frac{1}{W(child)}$.
- **Topic needed for this proof:** The canonical topological evaluation of tree intersection matrices via recursive, effective fractional weights.
- **Open-access substitute for that topic:** (open-access for topic: calculus of tree intersection forms via continued fractions) — Neumann, W. D. / 1981 / "A calculus for plumbing applied to the topology of complex surface singularities..." / Transactions of the AMS (freely available via AMS portal)
- **Connection:** Grounds your Step 3 "effective recursive weight $W(u)$" in canonical algebraic topology. When you define the weights recursively up the branches to the root, you are executing Neumann's calculus of plumbing graphs; citing this tells the grader that the root Schur complement $\Delta > 0$ is a standard, fully verified property of positive-definite trees.
- **Web search query:** `neumann a calculus for plumbing pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the foundational texts and specific references that address the structural setup of your tree’s quadratic form, alongside the discrete bounding algebra necessary to close the Grader’s gaps (particularly the Diophantine bounding for Step 5 and the Schur induction for Step 3).

The matrix you are analyzing (diagonal weights $w(x)$, off-diagonals $-1$ for edges, positive definite) is identically the **intersection matrix of a weighted tree / plumbing graph**. This structure is heavily studied in low-dimensional topology (resolution of singularities) and algebraic graph theory.

### 1. Conway, J.H., Sloane, N.J.A. / 1999
* **Title:** Sphere Packings, Lattices and Groups (3rd Edition)
* **Type:** Book
* **Venue:** Springer Grundlehren der mathematischen Wissenschaften 290
* **Main result or relevant chapter/section:** Chapter 2 covers the properties of positive definite quadratic forms on integral lattices, establishing that for any Gram matrix with integer entries, the associated quadratic form takes strictly integer values.
* **Topic needed for this proof:** The foundational proof that any strictly positive definite integer-valued symmetric bilinear form must assign a norm of $\ge 1$ to all non-zero vectors.
* **Open-access substitute for that topic:** (open-access for topic: integral positive definite quadratic forms and minimum norm) — Elkies / 2000 / Lattices, Linear Codes, and Invariants / Harvard course notes pdf
* **Connection:** Directly answers Grader B's Scaffolding Question 1 ("Why does an integer-valued positive definite bilinear form assign norm at least 1 to every nonzero vector?"). This justifies the exact starting point of the "Weight 1 Dichotomy" in Step 1.
* **Web search query:** `elkies lattices linear codes invariants pdf`
* **Confidence (bibliographic):** HIGH

### 2. Neumann, W.D. / 1981
* **Title:** A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves
* **Type:** Paper
* **Venue:** Transactions of the American Mathematical Society, Vol. 268
* **Main result or relevant chapter/section:** Defines the "plumbing calculus" for weighted trees. Theorem 4.1 and the subsequent sections outline how to sequentially reduce a weighted tree via continued fractions (the exact operation $W(u) = w(u) - \sum \frac{1}{W(z)}$) to determine the signature and positive definiteness of the intersection matrix. 
* **Topic needed for this proof:** The proof that sequential elimination of tree leaves yields effective weights defined by a strictly decreasing continued fraction recurrence, and that global positive definiteness mandates these effective weights remain $> 1$.
* **Open-access substitute for that topic:** (open-access for topic: continued fractions and intersection forms of plumbing trees) — Nemethi / 2005 / On the Ozsvath-Szabo invariant of negative definite plumbed 3-manifolds / arxiv 
* **Connection:** Resolves Grader B's Slips 3 and 4, and Scaffolding Questions 2 and 3. The effective weight recurrence is a standard topological result for tree intersection forms; citing this formalizes the induction and the strict $>1$ bound on the branches.
* **Web search query:** `nemethi plumbed 3-manifolds invariant pdf`
* **Confidence (bibliographic):** HIGH

### 3. Bapat, R.B. / 2010
* **Title:** Graphs and Matrices
* **Type:** Book
* **Venue:** Springer Universitext
* **Main result or relevant chapter/section:** Chapter 2 and Chapter 9 cover inverses of tree matrices and block matrix Schur complement reductions over graphs. It gives explicit formulas for reducing a tree graph matrix to a single root vertex by absorbing branches into recursive Schur complements.
* **Topic needed for this proof:** Inductive Schur complement factorization of a tree's weighted adjacency matrix into coupled parabolas.
* **Open-access substitute for that topic:** (open-access for topic: Schur complements and inverses of tree matrices) — Fiedler, Markham / 1994 / A classification of matrices of class Z / survey or related matrix theory notes
* **Connection:** Supplies the rigorous linear algebra framework for Step 3, addressing Grader B’s critique that "The Schur complement/factorization identity needs a clear induction proof." 
* **Web search query:** `bapat graphs and matrices springer pdf`
* **Confidence (bibliographic):** HIGH

### 4. Cassels, J.W.S. / 1978
* **Title:** Rational Quadratic Forms
* **Type:** Book
* **Venue:** London Mathematical Society Monographs (Academic Press)
* **Main result or relevant chapter/section:** Chapter 2 covers the Geometry of Numbers, specifically Diophantine bounding for quadratic forms. It establishes how to bound the discrete minimum of a quadratic form over a lattice strictly above its continuous minimum using the arithmetic distance to the continuous minimizer.
* **Topic needed for this proof:** Quantitative lower bounds for the evaluation of a quadratic form over integers strictly separated from the continuous real minimum.
* **Open-access substitute for that topic:** (open-access for topic: bounding discrete minima of quadratic forms via geometry of numbers) — Micciancio, Goldwasser / 2002 / Complexity of Lattice Problems: A Cryptographic Perspective / book draft or lecture notes
* **Connection:** This is the precise mathematical tool needed to fix Grader A's Step 5 Fallacy (the missing "explicit diophantine bounding algebra") and Grader B's Scaffolding Question 4 ("How do you compute the exact minimum of a quadratic polynomial over integers"). Because the continuous minimum in your proof occurs at fractional coordinates $\frac{a_v}{W(y)}$, bounding the minimum over $\mathbb{Z}$ requires quantifying the strictly positive gap $(a_y - \frac{a_v}{W(y)})^2 \ge \delta^2 > 0$.
* **Web search query:** `geometry of numbers quadratic forms notes pdf`
* **Confidence (bibliographic):** HIGH

### 5. Murota, K. / 2003
* **Title:** Discrete Convex Analysis
* **Type:** Monograph
* **Venue:** SIAM Monographs on Discrete Mathematics and Applications
* **Main result or relevant chapter/section:** Sections on separable convex functions over integer lattices (L-convexity and M-convexity). Shows how the global minimum of a network-structured quadratic objective over $\mathbb{Z}^V$ decomposes into local proximity bounds around the continuous optimum.
* **Topic needed for this proof:** Proximity bounds showing that the integer minimum of a coupled graph quadratic functional is forced strictly higher than the continuous minimum when boundary terms $a_v$ are fixed.
* **Open-access substitute for that topic:** (open-access for topic: proximity bounds in integer convex optimization) — Hochbaum / 2007 / Complexity and algorithms for nonlinear optimization problems / survey 
* **Connection:** Provides a modern optimization framework for Step 5. By defining your discrete functional as a separable convex quadratic optimization over the tree, Murota’s theorems provide the exact algebraic identities needed to prove the positive variance globally outscales the central negative well.
* **Web search query:** `discrete convex analysis murota pdf`
* **Confidence (bibliographic):** PARTIAL

## Gauntlet draw 2
Here are the canonical references and openly hosted topic-keyed substitutes that bear directly on the gaps in your near-miss proof. The literature on resolution graphs of surface singularities and the geometry of numbers deals exactly with evaluating positive-definite integer symmetric bilinear forms on weighted trees.

**1. H. B. Laufer / 1971**
- **Title:** Normal Two-Dimensional Singularities (approx.)
- **Type:** Monograph
- **Venue:** Annals of Mathematics Studies 71, Princeton University Press
- **Main result or relevant chapter/section:** Chapter 3 establishes the exact leaf-to-root evaluation algorithm for the determinant of intersection matrices on weighted trees, which corresponds identically to the recursive effective weight formula $W(u) = w(u) - \sum 1/W(z)$ used in Step 3 of the proof.
- **Topic needed for this proof:** Recursive Schur complement (continued fraction) reduction for computing determinants of tree intersection matrices, which bounds effective branch weights.
- **Open-access substitute for that topic:** (open-access for topic: plumbing calculus and tree intersection matrix determinant reduction) — W. D. Neumann / 1981 / A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves / Trans. Amer. Math. Soc.
- **Connection:** Closes Grader B's **Slip 3** (Schur factorization identity) and **Slip 4** (proving effective weights $>1$). In singularity theory, positive definiteness mathematically guarantees the recursion structurally maintains $W(u) > 1$ globally (up to the deficit vertex), strictly grounding your continuous Cholesky factorization in established discrete tree logic.
- **Web search query:** `neumann calculus for plumbing applied to topology pdf`
- **Confidence (bibliographic):** HIGH

**2. J. H. Conway, N. J. A. Sloane / 1999**
- **Title:** Sphere Packings, Lattices and Groups
- **Type:** Book
- **Venue:** Springer
- **Main result or relevant chapter/section:** Chapters 2 and 21 detail the geometry of numbers, explicitly handling the Closest Vector Problem (CVP) and bounding the minimum of shifted quadratic forms over integer lattices via covering radii and Voronoi cells.
- **Topic needed for this proof:** Explicit Diophantine bounding algebra to calculate the exact positive gap between a continuous fractional quadratic minimum and the nearest valid integer lattice evaluations.
- **Open-access substitute for that topic:** (open-access for topic: shifted lattice minima and discrete geometry of numbers) — N. Elkies / Lattices, Linear Codes, and Invariants / Harvard course notes (math.harvard.edu/~elkies).
- **Connection:** Resolves Grader A and B's **Fallacy in Step 5**. The proof claims the integer variance "structurally overrides" the negative continuous minimizer ($-1/4W(y)$) but omits the quantitative bound. You must use closest-vector lattice bounds (or completing the square on $\mathbb{Z}$) to explicitly write out the diophantine inequality proving the strictly positive integer gap. 
- **Web search query:** `elkies lattices linear codes invariants pdf`
- **Confidence (bibliographic):** HIGH

**3. C. Godsil, G. Royle / 2001**
- **Title:** Algebraic Graph Theory
- **Type:** Book
- **Venue:** Springer Graduate Texts in Mathematics
- **Main result or relevant chapter/section:** Chapter 9 covers Laplacians of trees, and Chapter 2 covers interlacing, equitable partitions, and explicit block-matrix Schur complements, showing how matrix properties interact with connected graph topologies. 
- **Topic needed for this proof:** Schur complements of graph matrices and the propagation of zero-energy vectors to adjacent vertices.
- **Open-access substitute for that topic:** (open-access for topic: Schur complements and zero-energy propagation in algebraic graph theory) — D. Spielman / 2019 / Spectral and Algebraic Graph Theory / Yale draft book.
- **Connection:** Closes Grader A's operational **Slip in Step 4** (the boundary collapse oversight). Using standard Schur complement properties for tree components, if a quadratic form defined over a connected tree block evaluates to zero, you can invoke the zero-energy propagation lemma to rigorously push the $a_y = 0$ collapse all the way to the leaves, rather than relying on the incomplete $a_y(W(y)a_y+1)=0$ local argument.
- **Web search query:** `spielman spectral and algebraic graph theory pdf`
- **Confidence (bibliographic):** HIGH

**4. N. Bourbaki / 1968**
- **Title:** Lie Groups and Lie Algebras, Chapters 4-6
- **Type:** Book
- **Venue:** Springer
- **Main result or relevant chapter/section:** Chapter 6 ("Root Systems") classifies all connected graphs supporting a positive definite symmetric bilinear integer form, establishing that such forms fundamentally bound non-zero integer vectors strictly away from zero (the elements of the root lattice), and classifying valid weights via generalized Coxeter graphs (ADE Dynkin diagrams).
- **Topic needed for this proof:** Lower bounds and the existence of root vectors for strictly positive definite integer quadratic forms on trees.
- **Open-access substitute for that topic:** (open-access for topic: positive definite symmetric bilinear forms on graphs and root systems) — R. E. Borcherds / Lie Groups / UC Berkeley math course notes.
- **Connection:** Answers Grader B's **Scaffolding Question 1** and the foundational premise of Step 1. The proof uses $x \cdot x \ge 1$ for all non-zero vectors. Because the form is integer-valued and positive definite, it is a classic result of positive definite lattices that the minimum non-zero norm is an integer strictly greater than 0.
- **Web search query:** `borcherds lie groups notes berkeley pdf`
- **Confidence (bibliographic):** HIGH
