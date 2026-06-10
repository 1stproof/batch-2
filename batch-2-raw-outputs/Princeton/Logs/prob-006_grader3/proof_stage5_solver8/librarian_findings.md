# Librarian Findings — grader3_acd8bd225c74_proof_stage5_solver8_20260531_013326
**Generated:** 2026-05-31T01:37:37  
**Inputs:** notebook=14800 chars, proof=8278 chars, gap_report=3504 chars  
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
- [book] R. A. Horn, C. R. Johnson / 1985 — Matrix Analysis — Cambridge University Press — IDs: no ID — Provides the Schur complement continuous determinant condition for block matrix positive definiteness, structurally coupling the central deficit weight to the surrounding branches. — search: horn johnson matrix analysis pdf
- [book] S. Boyd, L. Vandenberghe / 2004 — Convex Optimization — Cambridge University Press — IDs: no ID — Demonstrates that continuous partial minimization of a coupled block quadratic form intrinsically yields the Schur complement, directly resolving Grader A's decoupled optimization fallacy. — search: boyd vandenberghe convex optimization pdf
- [book] J. H. Conway, N. J. A. Sloane / 1988 — Sphere Packings, Lattices and Groups — Springer — IDs: no ID — Formally establishes that any strictly positive definite integral quadratic form unconditionally evaluates to at least 1 for non-zero vectors, answering Grader B's discrete bounding question. — search: conway sloane sphere packings lattices and groups pdf
- [book] A. E. Brouwer, W. H. Haemers / 2011 — Spectra of Graphs — Springer Universitext — IDs: no ID — Details the rigorous algebraic decomposition of a graph's Laplacian quadratic form into edge-difference squares and isolated vertex capacities, justifying the proof's topological expansion. — search: brouwer haemers spectra of graphs pdf

## RELATED
- [lecture notes] A. Némethi / 1999 — Five lectures on normal surface singularities — Bolyai Society Mathematical Studies — IDs: no ID — Contextualizes the exact topological plumbing calculus and discrete functionals applied over intersection matrices of weighted trees. — search: nemethi five lectures normal surface singularities pdf
- [paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society — IDs: no ID — Maps the explicit algebraic trade-offs and global definiteness determinants between a deficit central weight and high-capacity leaf vertices. — search: neumann calculus for plumbing pdf
- [book] A. Schrijver / 1986 — Theory of Linear and Integer Programming — Wiley — IDs: no ID — Quantifies the strictly positive energy gap accrued when a continuous minimum avoids lattice points, necessary to balance the integer evaluation against the negative well. — search: conforti cornuejols zambelli integer programming pdf
- [book] R. B. Bapat / 2010 — Graphs and Matrices — Springer Universitext — IDs: no ID — Provides an alternative canonical derivation expanding the tree quadratic form into independent edge-square terms and isolated vertex-capacity terms. — search: spielman spectral and algebraic graph theory pdf

## SOMEWHAT RELATED
- [book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory — Springer — IDs: no ID — Standard foundational reference proving that the quadratic form natively equates to the sum of squared differences across edges. — search: spielman spectral and algebraic graph theory pdf
- [book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences — SIAM — IDs: no ID — Demonstrates that symmetric strictly positive definite matrices with non-positive off-diagonals are M-matrices with non-negative inverses, providing bounding controls. — search: berman plemmons nonnegative matrices pdf

## NOT MUCH
- *(No further canonical sources were independently cited across the reports.)*

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [book] R. A. Horn, C. R. Johnson / 1985 — Matrix Analysis — Cambridge University Press — IDs: no ID — Provides the Schur complement continuous determinant condition for block matrix positive definiteness, structurally coupling the central deficit weight to the surrounding branches. — search: horn johnson matrix analysis pdf
  - **Gap:** Grader A SQ2, Grader B SQ5
  - **Load-bearing piece:** Section 7.7 covers positive definite block matrices and their exact equivalent conditions via the continuous Schur complement, linking the distinguished vertex submatrix directly to the surrounding branches.

- [book] S. Boyd, L. Vandenberghe / 2004 — Convex Optimization — Cambridge University Press — IDs: no ID — Demonstrates that continuous partial minimization of a coupled block quadratic form intrinsically yields the Schur complement, directly resolving Grader A's decoupled optimization fallacy. — search: boyd vandenberghe convex optimization pdf
  - **Gap:** Grader A Fallacy 1 ("Decoupled Optimization (Fallacy)"), Grader B SQ4
  - **Load-bearing piece:** Appendix A.5.5 explicitly proves that partially minimizing a block quadratic form over a subset of branch variables natively yields the coupled Schur complement, preventing the artificial negative minimum generated by decoupling.

- [book] J. H. Conway, N. J. A. Sloane / 1988 — Sphere Packings, Lattices and Groups — Springer — IDs: no ID — Formally establishes that any strictly positive definite integral quadratic form unconditionally evaluates to at least 1 for non-zero vectors, answering Grader B's discrete bounding question. — search: conway sloane sphere packings lattices and groups pdf
  - **Gap:** Grader B SQ1
  - **Load-bearing piece:** Chapter 2 formally details the bounding geometry of positive definite integral lattices, establishing that since $x^T M x \in \mathbb{Z}$ and is strictly $> 0$ for $x \neq 0$, it is bounded below by exactly 1.

- [book] A. E. Brouwer, W. H. Haemers / 2011 — Spectra of Graphs — Springer Universitext — IDs: no ID — Details the rigorous algebraic decomposition of a graph's Laplacian quadratic form into edge-difference squares and isolated vertex capacities, justifying the proof's topological expansion. — search: brouwer haemers spectra of graphs pdf
  - **Gap:** Grader B SQ2, Grader B Slip 2
  - **Load-bearing piece:** Chapter 2 constructs the graph Laplacian and incidence matrices, proving the canonical quadratic form identity as the sum of squared edge differences.

## SUPPORTING

- [book] A. Schrijver / 1986 — Theory of Linear and Integer Programming — Wiley — IDs: no ID — Quantifies the strictly positive energy gap accrued when a continuous minimum avoids lattice points, necessary to balance the integer evaluation against the negative well. — search: conforti cornuejols zambelli integer programming pdf
  - *Note: Useful for addressing Grader B Fallacy 5 by providing the Diophantine bounds when transitioning from continuous negative minima to discrete evaluations.*

- [paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society — IDs: no ID — Maps the explicit algebraic trade-offs and global definiteness determinants between a deficit central weight and high-capacity leaf vertices. — search: neumann calculus for plumbing pdf
  - *Note: Offers direct topological context for the exact intersection matrices and positive definiteness constraints specific to these weighted trees.*

- [lecture notes] A. Némethi / 1999 — Five lectures on normal surface singularities — Bolyai Society Mathematical Studies — IDs: no ID — Contextualizes the exact topological plumbing calculus and discrete functionals applied over intersection matrices of weighted trees. — search: nemethi five lectures normal surface singularities pdf
  - *Note: General background verifying the use of graph configurations and topological slack capacities.*

- [book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences — SIAM — IDs: no ID — Demonstrates that symmetric strictly positive definite matrices with non-positive off-diagonals are M-matrices with non-negative inverses, providing bounding controls. — search: berman plemmons nonnegative matrices pdf
  - *Note: Connects the positive definite tree intersection matrix structure natively to M-matrices, which implies bounding controls.*

## REDUNDANT

- [book] R. B. Bapat / 2010 — Graphs and Matrices — Springer Universitext — IDs: no ID — Provides an alternative canonical derivation expanding the tree quadratic form into independent edge-square terms and isolated vertex-capacity terms. — search: spielman spectral and algebraic graph theory pdf
  - *Overlap: Brouwer & Haemers covers the identical Laplacian quadratic form expansion needed to address Grader B SQ2.*

- [book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory — Springer — IDs: no ID — Standard foundational reference proving that the quadratic form natively equates to the sum of squared differences across edges. — search: spielman spectral and algebraic graph theory pdf
  - *Overlap: Brouwer & Haemers establishes the identical sum-of-squares edge expansions required.*

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

---

# Stage 3 — Chapter Picker

## Matrix Analysis (R. A. Horn, C. R. Johnson, Cambridge University Press, 1985)
_(Provides the Schur complement continuous determinant condition for block matrix positive definiteness, structurally coupling the central deficit weight to the surrounding branches. — search: horn johnson matrix analysis pdf)_

Here are the specific chapters and sections from Horn & Johnson's *Matrix Analysis* (1985) that will directly close the mathematical gaps regarding positive definiteness and matrix partitioning.

**Chapter 7, Section 7.7 — Partitioned Matrices and Schur Complements (approx.)**
*   **Which gap it addresses:** Grader A's Question 2 ("continuous determinant condition") and Grader B's Question 5 ("quantitative inequalities positive definiteness imposes on a block matrix").
*   **Why:** This section establishes the fundamental theorem that a block matrix $M = \begin{pmatrix} A & B \\ B^T & C \end{pmatrix}$ is positive definite if and only if $C \succ 0$ and the Schur complement $A - B C^{-1} B^T \succ 0$. By partitioning the tree's intersection matrix such that the 1x1 block $A$ is the weight of the central vertex $w(v)$ and $C$ represents the branches, this theorem provides the exact algebraic inequality coupling the central deficit to the leaf weights (via $C^{-1}$), directly resolving the "Decoupled Optimization" fallacy.

**Chapter 7, Section 7.2 — Characterizations (Sylvester's Criterion / Principal Submatrices) (approx.)**
*   **Which gap it addresses:** Grader B's Fallacy 6 ("The use of positive definiteness to control branch minima is completely unproved") and Grader B's Question 4.
*   **Why:** This section formally proves that every principal submatrix of a positive definite matrix is itself strictly positive definite. You must cite this to justify mathematically why the disconnected branches $B_i$ formed by removing $v$ act as valid, independent positive definite systems whose local quadratic forms $Q_{B_i}(x)$ can be optimized over the integers.

**Chapter 7, Section 7.1 — Positive Definite Matrices: Definitions and Basic Properties**
*   **Which gap it addresses:** Grader B's Question 1 ("Why does an integer-valued positive definite quadratic form satisfy $Q(x)\ge 1$ for every nonzero integral vector?").
*   **Why:** It lays out the definition that $x^T M x > 0$ for all non-zero real vectors. Because the tree yields an integer matrix, any non-zero integer vector $x \in \mathbb{Z}^V$ must produce an integer scalar. Thus, the strict positivity constraint fundamentally forces the discrete lattice threshold $Q(x) \ge 1$, sealing the problem's baseline bounding step.

## Convex Optimization (S. Boyd, L. Vandenberghe, Cambridge University Press, 2004)
_(Demonstrates that continuous partial minimization of a coupled block quadratic form intrinsically yields the Schur complement, directly resolving Grader A's decoupled optimization fallacy. — search: boyd vandenberghe convex optimization pdf)_

Here are the specific sections in Boyd and Vandenberghe’s *Convex Optimization* that provide the rigorous continuous-domain algebra needed to fix the decoupled optimization fallacy and establish the block-matrix bounds.

- **Appendix A.5.5 — Schur complement**
  - **Which gap it addresses:** Grader B’s Scaffold Question 5 (quantitative inequalities imposed on block matrices) and Grader A’s Scaffold Question 2 (continuous determinant condition).
  - **Why:** This section provides the foundational theorem that a symmetric block matrix is positive definite if and only if its principal submatrix is positive definite and its Schur complement is strictly positive definite. By framing the tree's intersection matrix as a block matrix with the unique deficit vertex $v$ separated from the branch/leaf variables, this provides the exact algebraic coupling between the central weight $w(v)$ and the leaf weights that the proof currently drops.

- **Section 3.2.5 — Minimizing over some variables**
  - **Which gap it addresses:** Grader A's "Decoupled Optimization (Fallacy)" and Scaffold Question 3 (optimizing the coupled expression to find the true minimum).
  - **Why:** This section explicitly derives how the continuous partial minimization of a block quadratic form over a subset of variables yields the Schur complement. Instead of throwing away the leaf capacities $c_y x_y^2$ to minimize an isolated parabola (which caused the artificial negative well), applying this result proves that the fully coupled, unconstrained continuous branch minimization is structurally identical to the Schur complement. Since Appendix A.5.5 dictates the Schur complement must be strictly positive due to the graph's positive definiteness, this guarantees the continuous floor—and thus the discrete integer minimum above it—must heavily exceed the negative deficit, directly bridging the gap.

## Sphere Packings, Lattices and Groups (J. H. Conway, N. J. A. Sloane, Springer, 1988)
_(Formally establishes that any strictly positive definite integral quadratic form unconditionally evaluates to at least 1 for non-zero vectors, answering Grader B's discrete bounding question. — search: conway sloane sphere packings lattices and groups pdf)_

Here are the specific chapters and sections from Conway & Sloane's *Sphere Packings, Lattices and Groups* that directly address the grader gaps:

**Chapter 2: Coverings, Lattices and Quantizers (approx.)**
- **Which gap it addresses:** Grader B's Q1 ("Why does an integer-valued positive definite quadratic form satisfy $Q(x)\ge1$ for every nonzero integral vector?").
- **Why:** This chapter formally defines integral lattices and their associated Gram matrices. It provides the foundational proof that for any lattice equipped with an integral quadratic form, the squared norm $N(x) = x \cdot x$ evaluates strictly to integers. Combined with positive definiteness ($N(x) > 0$ for $x \ne 0$), this algebraically forces the absolute minimum for non-zero vectors to be $\ge 1$, directly closing the discrete bounding gap.

**Chapter 4: Certain Important Lattices and Their Properties**
- **Which gap it addresses:** Grader A's Q2 and Grader B's Q5 (Determinant conditions, positive definiteness constraints on trees, and block matrices).
- **Why:** This chapter deeply analyzes the root lattices ($A_n, D_n, E_n$) whose Gram matrices correspond precisely to the intersection matrices of weighted trees (Coxeter-Dynkin diagrams). It establishes the quantitative inequalities and determinant restrictions that a global positive-definite matrix imposes on its local structural branches, directly answering how positive definiteness restricts the relationship between the central vertex and leaf weights.

**Chapter 2 (or Chapter 20 approx.): The Closest Point Problem and Voronoi Cells**
- **Which gap it addresses:** Grader A's Fallacy 1 and Grader B's Q4 (Bounding branch minima and computing the minimum of a quadratic expression with a linear term over an integer lattice).
- **Why:** Evaluating a positive definite branch quadratic form against a linear pull is algebraically equivalent to completing the square to find the distance to a non-lattice point in continuous space. The sections on the "Closest Point Problem" and Voronoi decoding formally detail how to bound the strict positive error between the continuous relaxation (the "negative well") and the true discrete integer minimum.

## Spectra of Graphs (A. E. Brouwer, W. H. Haemers, Springer Universitext, 2011)
_(Details the rigorous algebraic decomposition of a graph's Laplacian quadratic form into edge-difference squares and isolated vertex capacities, justifying the proof's topological expansion. — search: brouwer haemers spectra of graphs pdf)_

Here are the specific chapters and sections from Brouwer and Haemers' *Spectra of Graphs* that provide the rigorous algebraic machinery to close the named gaps.

*   **Chapter 1, Section: "The Laplacian" (approx. Sec 1.3)**
    *   **Which gap it addresses:** Grader B, Gap 2 (Derivation of the expansion of $E_v$) and Grader B Scaffolding Q2.
    *   **Why:** This section provides the foundational algebraic derivation of the Laplacian quadratic form via the oriented incidence matrix $B$, proving $x^T L x = \sum_{u \sim v} (x_u - x_v)^2$. Factoring the global positive definite matrix as a standard Laplacian plus a diagonal weight excess matrix directly yields the required rigorous expansion into edge-square differences and isolated vertex capacities.

*   **Chapter 2, Section: "Interlacing" and Block Matrices (approx. Sec 2.1 - 2.5)**
    *   **Which gap it addresses:** Grader A, Gap 1 (Decoupled Optimization), Grader A Scaffolding Q2, and Grader B, Gap 6 (Use of positive definiteness to control branch minima).
    *   **Why:** This chapter covers Cauchy eigenvalue interlacing and bounds for principal submatrices. By framing the tree's intersection matrix as a block matrix with the unique deficit vertex $v$ separated from its disconnected branches, the global positive-definiteness dictates a strict inequality on the Schur complement: $w(v) > \sum \text{Branch}_{i}^{-1}(root, root)$. This continuous determinant constraint is the exact mechanism needed to couple the isolated branch parabolas back to the global weight limit, preventing the "decoupled optimization" fallacy.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [book] R. A. Horn, C. R. Johnson / 1985 — Matrix Analysis — Cambridge University Press — IDs: no ID — Provides the Schur complement continuous determinant condition for block matrix positive definiteness, structurally coupling the central deficit weight to the surrounding branches. — search: horn johnson matrix analysis pdf
  - **Addresses:** Grader A Scaffolding 2, Grader B Fallacy 6, and Grader B Scaffolding 5
  - **Load-bearing piece:** Chapter 7 details positive definite block matrices and formalizes the Schur complement condition necessary to globally couple the branch matrix determinants to the central deficit vertex.

- [book] S. Boyd, L. Vandenberghe / 2004 — Convex Optimization — Cambridge University Press — IDs: no ID — Demonstrates that continuous partial minimization of a coupled block quadratic form intrinsically yields the Schur complement, directly resolving Grader A's decoupled optimization fallacy. — search: boyd vandenberghe convex optimization pdf
  - **Addresses:** Grader A Fallacy 1 (Decoupled Optimization) and Grader A Scaffolding 3
  - **Load-bearing piece:** Appendix A.5.5 establishes that partial continuous minimization over a subset of variables in a positive definite quadratic form structurally yields the Schur complement, providing the exact coupled branch optimization required.

- [book] J. H. Conway, N. J. A. Sloane / 1988 — Sphere Packings, Lattices and Groups — Springer — IDs: no ID — Formally establishes that any strictly positive definite integral quadratic form unconditionally evaluates to at least 1 for non-zero vectors, answering Grader B's discrete bounding question. — search: conway sloane sphere packings lattices and groups pdf
  - **Addresses:** Grader B Scaffolding 1
  - **Load-bearing piece:** Chapter 2 confirms that the minimum norm of any non-zero vector in a strictly positive definite integral lattice is $\ge 1$, formally justifying the discrete lower bound.

- [book] A. E. Brouwer, W. H. Haemers / 2011 — Spectra of Graphs — Springer Universitext — IDs: no ID — Details the rigorous algebraic decomposition of a graph's Laplacian quadratic form into edge-difference squares and isolated vertex capacities, justifying the proof's topological expansion. — search: brouwer haemers spectra of graphs pdf
  - **Addresses:** Grader B Slip 2 and Grader B Scaffolding 2
  - **Load-bearing piece:** The section on Laplacian matrices rigorously derives the expansion of a graph's quadratic form into the sum of edge-incident squared differences and residual vertex capacities.

## SUPPORTING

- [book] A. Schrijver / 1986 — Theory of Linear and Integer Programming — Wiley — IDs: no ID — Quantifies the strictly positive energy gap accrued when a continuous minimum avoids lattice points, necessary to balance the integer evaluation against the negative well. — search: conforti cornuejols zambelli integer programming pdf
  - Provides the fundamental theory for bounding the gap between a continuous minimum and an integer lattice minimum (addresses Grader B Fallacy 5).

- [paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society — IDs: no ID — Maps the explicit algebraic trade-offs and global definiteness determinants between a deficit central weight and high-capacity leaf vertices. — search: neumann calculus for plumbing pdf
  - Contextualizes the exact algebraic trade-offs and topological plumbing calculus specific to the weighted tree intersection matrices used in the problem.

- [book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences — SIAM — IDs: no ID — Demonstrates that symmetric strictly positive definite matrices with non-positive off-diagonals are M-matrices with non-negative inverses, providing bounding controls. — search: berman plemmons nonnegative matrices pdf
  - Establishes properties of M-matrices which govern the signs of the inverses of positive definite tree intersection forms, useful for verifying algebraic balance limits.

## REDUNDANT

- [book] R. B. Bapat / 2010 — Graphs and Matrices — Springer Universitext — IDs: no ID — Provides an alternative canonical derivation expanding the tree quadratic form into independent edge-square terms and isolated vertex-capacity terms. — search: spielman spectral and algebraic graph theory pdf
  - Overlaps with Brouwer & Haemers on the standard algebraic derivation expanding the tree quadratic form into independent edge-square terms.

- [book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory — Springer — IDs: no ID — Standard foundational reference proving that the quadratic form natively equates to the sum of squared differences across edges. — search: spielman spectral and algebraic graph theory pdf
  - Overlaps with Brouwer & Haemers by providing the foundational proof that a graph's quadratic form natively equates to the sum of squared differences.

## PERIPHERAL

- [lecture notes] A. Némethi / 1999 — Five lectures on normal surface singularities — Bolyai Society Mathematical Studies — IDs: no ID — Contextualizes the exact topological plumbing calculus and discrete functionals applied over intersection matrices of weighted trees. — search: nemethi five lectures normal surface singularities pdf
  - While it discusses intersection matrices of weighted trees, it focuses on geometry/singularity theory rather than the explicit discrete algebraic and optimization bounds flagged by the graders.

## UNFAMILIAR

*(None)*

## Narrower draw 2
Here is the triaged list of sources, categorized against the specific critiques and scaffolding questions raised by the graders.

## LOAD-BEARING

- **[book] R. A. Horn, C. R. Johnson / 1985 — Matrix Analysis — Cambridge University Press — IDs: no ID — Provides the Schur complement continuous determinant condition for block matrix positive definiteness, structurally coupling the central deficit weight to the surrounding branches. — search: horn johnson matrix analysis pdf**
  - **Gap addressed:** Grader B Scaffolding 5 ("What quantitative inequalities does positive definiteness impose on a block matrix with one distinguished vertex?").
  - **Load-bearing piece:** Section 7.7 directly establishes the Schur complement continuous determinant conditions, explicitly detailing how the block matrix structure restricts a distinguished vertex against the positive definiteness of the remaining branches.

- **[book] S. Boyd, L. Vandenberghe / 2004 — Convex Optimization — Cambridge University Press — IDs: no ID — Demonstrates that continuous partial minimization of a coupled block quadratic form intrinsically yields the Schur complement, directly resolving Grader A's decoupled optimization fallacy. — search: boyd vandenberghe convex optimization pdf**
  - **Gap addressed:** Grader A Fallacy 1 ("Decoupled Optimization (Fallacy)") and Grader A Scaffolding 3 ("optimize the coupled expression").
  - **Load-bearing piece:** Appendix A.5.5 formally proves that the continuous partial minimization of a symmetric block quadratic form over a subset of unconstrained real variables exactly yields the Schur complement, providing the canonical means to optimize the coupled expression without discarding topological weights.

- **[book] J. H. Conway, N. J. A. Sloane / 1988 — Sphere Packings, Lattices and Groups — Springer — IDs: no ID — Formally establishes that any strictly positive definite integral quadratic form unconditionally evaluates to at least 1 for non-zero vectors, answering Grader B's discrete bounding question. — search: conway sloane sphere packings lattices and groups pdf**
  - **Gap addressed:** Grader B Scaffolding 1 ("Why does an integer-valued positive definite quadratic form satisfy $Q(x) \ge 1$ for every nonzero integral vector?").
  - **Load-bearing piece:** Chapter 2 ("Integral Lattices") covers the fundamental definitions of positive definite integral quadratic forms, mathematically proving that evaluating such a form on any non-zero point in the integer lattice yields a strictly positive integer, bounded below by 1.

- **[book] A. E. Brouwer, W. H. Haemers / 2011 — Spectra of Graphs — Springer Universitext — IDs: no ID — Details the rigorous algebraic decomposition of a graph's Laplacian quadratic form into edge-difference squares and isolated vertex capacities, justifying the proof's topological expansion. — search: brouwer haemers spectra of graphs pdf**
  - **Gap addressed:** Grader B Slip 2 ("Derive the expansion of $E_v$") and Grader B Scaffolding 2 ("rewritten as edge-square terms plus vertex capacity terms").
  - **Load-bearing piece:** Chapter 2 (specifically sections discussing the Laplacian) provides the canonical derivation that formally expands a weighted graph's quadratic form into the sum of squared edge differences combined with independent diagonal vertex capacity terms.

## SUPPORTING

- **[book] A. Schrijver / 1986 — Theory of Linear and Integer Programming — Wiley — IDs: no ID — Quantifies the strictly positive energy gap accrued when a continuous minimum avoids lattice points, necessary to balance the integer evaluation against the negative well. — search: conforti cornuejols zambelli integer programming pdf**
  - *Note:* Provides necessary mathematical context for bounding the strictly positive gap between discrete integer limits and continuous negative wells, aiding Grader B Fallacy 5.
- **[lecture notes] A. Némethi / 1999 — Five lectures on normal surface singularities — Bolyai Society Mathematical Studies — IDs: no ID — Contextualizes the exact topological plumbing calculus and discrete functionals applied over intersection matrices of weighted trees. — search: nemethi five lectures normal surface singularities pdf**
  - *Note:* Useful background confirming the typical structure of these exact symmetric discrete functionals on plumbing intersection matrices.
- **[paper] W. D. Neumann / 1981 — A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves — Transactions of the American Mathematical Society — IDs: no ID — Maps the explicit algebraic trade-offs and global definiteness determinants between a deficit central weight and high-capacity leaf vertices. — search: neumann calculus for plumbing pdf**
  - *Note:* Contextualizes the exact topological constraints applied to leaf vertices and central deficit vertices, though the direct linear algebra gaps are covered by standard texts.

## REDUNDANT

- **[book] R. B. Bapat / 2010 — Graphs and Matrices — Springer Universitext — IDs: no ID — Provides an alternative canonical derivation expanding the tree quadratic form into independent edge-square terms and isolated vertex-capacity terms. — search: spielman spectral and algebraic graph theory pdf**
  - *Overlap:* Redundant with Brouwer & Haemers; covers the exact same fundamental expansion of the Laplacian quadratic form.
- **[book] C. Godsil, G. Royle / 2001 — Algebraic Graph Theory — Springer — IDs: no ID — Standard foundational reference proving that the quadratic form natively equates to the sum of squared differences across edges. — search: spielman spectral and algebraic graph theory pdf**
  - *Overlap:* Redundant with Brouwer & Haemers; also provides the graph expansion into squared edge differences.

## PERIPHERAL

- **[book] A. Berman, R. J. Plemmons / 1994 — Nonnegative Matrices in the Mathematical Sciences — SIAM — IDs: no ID — Demonstrates that symmetric strictly positive definite matrices with non-positive off-diagonals are M-matrices with non-negative inverses, providing bounding controls. — search: berman plemmons nonnegative matrices pdf**
  - *Note:* While true that intersection matrices of this type are related to M-matrices, invoking M-matrix theory is not concretely necessary to resolve any of the explicit step-by-step optimization gaps identified by the graders.

## UNFAMILIAR

*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and open-access substitutes that directly address the mathematical gaps in the attempted proof. The fallacies identified by the graders center on an aggressive decoupling of the quadratic sum—discarding leaf terms to bound isolated parabolas inherently creates an artificial, unrecoverable negative well. Fixing this requires exact coupled continuous minimization (via Schur complements) and leveraging the properties of integer lattices and M-matrices.

- **Authors / Year** — R. A. Horn, C. R. Johnson / 1985
- **Title** — Matrix Analysis
- **Type** — book
- **Venue** — Cambridge University Press
- **Main result or relevant chapter/section** — Chapter 7 (Positive Definite Matrices) establishes that a block matrix is strictly positive definite if and only if both its principal block and the corresponding Schur complement are strictly positive definite.
- **Topic needed for this proof** — The Schur complement continuous determinant condition for block matrix positive definiteness.
- **Open-access substitute for that topic** — (open-access for topic: Schur complements and positive definite block matrices) — Gallier / 2010 / The Schur Complement and Symmetric Positive Definite Matrices / Penn + `cis.upenn.edu/~jean`
- **Connection** — Directly answers Grader A's Question 2. The global positive definiteness structurally forces the Schur complement $w(v) - \sum (A_{B_i}^{-1})_{rr}$ to be strictly positive, which inherently couples the branch capacities to the central vertex weight and mathematically precludes the artificial negative gap the proof hallucinated.
- **Web search query** — `horn johnson matrix analysis pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — S. Boyd, L. Vandenberghe / 2004
- **Title** — Convex Optimization
- **Type** — book
- **Venue** — Cambridge University Press
- **Main result or relevant chapter/section** — Appendix A.5.5 proves that executing a continuous partial minimization of a coupled block quadratic form over a subset of variables explicitly yields the Schur complement of the system.
- **Topic needed for this proof** — Evaluating the exact partial minimum of a coupled quadratic form over continuous variables using the Schur complement.
- **Open-access substitute for that topic** — (none needed, authors host the canonical manuscript openly) — Boyd, Vandenberghe / 2004 / Convex Optimization / Stanford + `stanford.edu/~boyd/cvxbook`
- **Connection** — Resolves Grader A's "Decoupled Optimization" fallacy (Question 3). By simultaneously minimizing the full branch quadratic expression via its Schur complement, the proof can bound the functional without violently discarding the leaf weights that govern the structural positivity.
- **Web search query** — `boyd vandenberghe convex optimization pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — A. Berman, R. J. Plemmons / 1994
- **Title** — Nonnegative Matrices in the Mathematical Sciences
- **Type** — book
- **Venue** — SIAM
- **Main result or relevant chapter/section** — Chapter 6 proves that symmetric Z-matrices (symmetric matrices with non-positive off-diagonals) are strictly positive definite if and only if they are nonsingular M-matrices, meaning their matrix inverses are entirely element-wise non-negative (Stieltjes matrices).
- **Topic needed for this proof** — Element-wise inverse non-negativity for strictly positive definite matrices with non-positive off-diagonals.
- **Open-access substitute for that topic** — (open-access for topic: Inverse positivity of symmetric M-matrices) — Fiedler, Ptak / 1962 / On matrices with non-positive off-diagonal elements and positive principal minors / Czechoslovak Mathematical Journal + `dml.cz`
- **Connection** — Answers Grader B's Question 5 about quantitative matrix inequalities. The strict element-wise non-negativity of the inverse provides the monotonic bounding required to ensure the continuous branch optimizations do not diverge toward negative infinity.
- **Web search query** — `berman plemmons nonnegative matrices pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — C. Godsil, G. Royle / 2001
- **Title** — Algebraic Graph Theory
- **Type** — book
- **Venue** — Springer (Graduate Texts in Mathematics 207)
- **Main result or relevant chapter/section** — Chapter 13 (The Laplacian of a Graph) proves that the quadratic form associated with a graph natively equates to the sum of squared differences across edges, cleanly splitting off isolated vertex weight terms when the diagonal exceeds the degree.
- **Topic needed for this proof** — Algebraic expansion of a weighted graph's quadratic form into a sum of squared edge differences and vertex capacities.
- **Open-access substitute for that topic** — (open-access for topic: graph Laplacian quadratic form expansion) — Spielman / 2019 / Spectral and Algebraic Graph Theory / Yale + `cs.yale.edu/homes/spielman/sagt`
- **Connection** — Answers Grader B's Question 2 by validating the exact topological expansion assumed in Case 1, correctly rewriting the initial matrix interactions into structurally independent, non-negative squared terms.
- **Web search query** — `spielman spectral and algebraic graph theory pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — J. H. Conway, N. J. A. Sloane / 1988
- **Title** — Sphere Packings, Lattices and Groups
- **Type** — book
- **Venue** — Springer-Verlag
- **Main result or relevant chapter/section** — Chapter 2 formally details that an integral lattice equipped with a strictly positive definite quadratic form identically satisfies $Q(x) \ge 1$ for all non-zero integer vectors, as the norm fundamentally evaluates to positive integers.
- **Topic needed for this proof** — The universal lower bound $Q(x) \ge 1$ for non-zero vectors in a strictly positive definite integral lattice.
- **Open-access substitute for that topic** — (open-access for topic: strictly positive definite integral lattices and minimum nonzero vectors) — Regev / 2004 / Lattices in Computer Science / Tel Aviv + `cims.nyu.edu/~regev`
- **Connection** — Addresses Grader B's Question 1 by supplying the foundational lattice-theoretic citation for why the discrete integral quadratic form unconditionally bridges the threshold to 1, a property the proof claimed but omitted citing.
- **Web search query** — `conway sloane sphere packings lattices and groups pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — A. Némethi / 1999
- **Title** — Five lectures on normal surface singularities
- **Type** — lecture notes
- **Venue** — Bolyai Society Mathematical Studies (Low Dimensional Topology)
- **Main result or relevant chapter/section** — Details the canonical topological plumbing calculus for surface resolution graphs, demonstrating exactly how a finite tree (with vertex capacities and negative unit edges) acts as a definite intersection matrix governing integer "fundamental cycles."
- **Topic needed for this proof** — Integer decompositions governed by the algebraic capacity of a positive-definite plumbing graph.
- **Open-access substitute for that topic** — (none needed, standardly available on author's home institution page via Renyi Institute)
- **Connection** — Contextualizes the entire proof environment. The stated hypothesis (finite tree, vertex weights $\ge 2$, off-diagonals $-1$) is the strict algebraic dual of the intersection graph for resolving a complex surface singularity. Recalling the exact fundamental cycle algebraic machinery helps bypass the author's flawed manual node decoupling.
- **Web search query** — `nemethi five lectures normal surface singularities pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical reference works and topic-keyed substitutes that directly address the mathematical gaps identified by the graders.

The structural gaps in this proof center on the failure to rigorously couple the localized branch minimizations with the global positive-definite constraint (Grader A), and skipping the formal algebraic justification for expanding the tree quadratic form (Grader B). 

### 1. The Continuous Determinant / Positive Definiteness Coupling
**Authors / Year:** Horn, R. A., and Johnson, C. R. / 2012 (2nd Ed., or 1985 1st Ed.)
**Title:** Matrix Analysis
**Type:** Book
**Venue:** Cambridge University Press
**Main result or relevant chapter/section:** Chapter 7 (specifically Section 7.7 on Positive Definite Matrices and Schur Complements). It proves that a block matrix is positive definite if and only if both the principal submatrix and its Schur complement are strictly positive definite.
**Topic needed for this proof:** The continuous determinant condition that couples the central weight $w(v)$ to the inverse matrices of the disjoint branches via the strict positivity of the Schur complement.
**Open-access substitute for that topic:** (open-access for topic: Schur complements and block positive-definiteness) — Boyd, S., and Vandenberghe, L. / 2004 / Convex Optimization / Appendix A.5.5 (freely hosted on author's Stanford webpage).
**Connection:** Directly answers Grader A’s Scaffolding Question #2 and Critique #1. The proof fails because it treats the branch submatrices and the central weight $w(v)$ as independent entities. Horn & Johnson provides the exact continuous determinant constraint: $w(v) > \sum e_{r_i}^T (M_{B_i})^{-1} e_{r_i}$, which algebraically restricts how small the continuous minima of the branches can be before global positive definiteness collapses.
**Web search query:** `boyd vandenberghe convex optimization pdf`
**Confidence (bibliographic):** HIGH

### 2. The "Topological Expansion" of the Quadratic Form
**Authors / Year:** Bapat, R. B. / 2010
**Title:** Graphs and Matrices
**Type:** Book
**Venue:** Springer Universitext
**Main result or relevant chapter/section:** Chapter 4 (The Laplacian Matrix). This chapter covers the expansion of quadratic forms over graphs, demonstrating how any form $x^T L x$ strictly telescopes into sums of squared edge-differences $\sum_{i \sim j} (x_i - x_j)^2$, and how adding diagonal weights transforms it into a Schrödinger operator with vertex capacities.
**Topic needed for this proof:** The algebraic derivation expanding an integer-weighted graph quadratic form into independent edge-square terms and isolated vertex-capacity terms.
**Open-access substitute for that topic:** (open-access for topic: Laplacian quadratic form expansion and edge incidence matrices) — Spielman, D. A. / 2019 / Spectral and Algebraic Graph Theory / Yale University course drafts.
**Connection:** Addresses Grader B's Scaffolding Question #2 and Critique #2 ("Derive the expansion of $E_v$ rather than asserting it in one line"). Bapat provides the canonical linear algebra justification for rewriting the global intersection form via the edge incidence matrix.
**Web search query:** `spielman spectral and algebraic graph theory pdf`
**Confidence (bibliographic):** HIGH

### 3. Positive Definiteness and the Minimum Non-Zero Integer Vector
**Authors / Year:** Conway, J. H., and Sloane, N. J. A. / 1998
**Title:** Sphere Packings, Lattices and Groups
**Type:** Book
**Venue:** Springer (Grundlehren der mathematischen Wissenschaften)
**Main result or relevant chapter/section:** Chapter 2 (Properties of Lattices). Covers the theory of integral positive definite quadratic forms, structurally proving that because the integer lattice is a discrete subgroup of $\mathbb{R}^n$, the minimum of any strictly positive-definite integral quadratic form over non-zero vectors is bounded away from $0$ (and specifically $\ge 1$ for strictly integer forms).
**Topic needed for this proof:** The foundational proof that a positive definite quadratic form over the integers evaluates to strictly $\ge 1$ for all non-zero vectors.
**Open-access substitute for that topic:** (open-access for topic: minimum norm of integral positive definite lattices) — Elkies, N. / Lattices, Linear Codes, and Invariants / Harvard Math 250a Lecture Notes.
**Connection:** Answers Grader B's Scaffolding Question #1. The proof's opening assumption "By the strict positive definiteness... $Q(x) \ge 1$" requires formal justification, as it bridges the gap between a continuous property (eigenvalues $> 0$) and a discrete lower bound. 
**Web search query:** `elkies lattices linear codes invariants pdf`
**Confidence (bibliographic):** HIGH

### 4. Plumbed Trees and Intersection Matrix Functionals
**Authors / Year:** Némethi, A. / 1999
**Title:** Five lectures on normal surface singularities
**Type:** Lecture notes / Survey
**Venue:** Proceedings of the Summer School in Low dimensional topology, Budapest (later hosted on Renyi Institute webpage)
**Main result or relevant chapter/section:** Lectures 1 and 2 detail the calculus of plumbing graphs (weighted trees where edges are $-1$ and vertices are $w(v)$). It explicitly treats the positive-definite intersection lattices $L(T)$ and constructs the exact discrete functionals (like the canonical class / degree functional) over the vertex capacities that this proof is struggling to optimize.
**Topic needed for this proof:** Bounding discrete linear-quadratic functionals over positive-definite intersection lattices of weighted trees.
**Open-access substitute for that topic:** (open-access for topic: intersection matrices of plumbing graphs and their definiteness) — Neumann, W. D. / 1998 / Topology of hypersurface singularities / Park City Mathematics Series.
**Connection:** This is the exact topological/algebraic setting of the user's problem. Némethi's notes show how mathematicians actually bound $x \cdot x - x \cdot v$ on such trees, utilizing the fundamental cycles and Laufer's algorithm rather than trying to decouple the branches into unconstrained parabolas (which Grader A correctly flagged as a Fallacy).
**Web search query:** `nemethi five lectures normal surface singularities pdf`
**Confidence (bibliographic):** HIGH

### 5. Gap Between Continuous and Integer Quadratic Minima
**Authors / Year:** Schrijver, A. / 1986
**Title:** Theory of Linear and Integer Programming
**Type:** Book
**Venue:** Wiley
**Main result or relevant chapter/section:** Chapters 16 and 17 (Integer Linear Programming and Lattices). Discusses the bounds between continuous convex optimization and discrete integer evaluation, detailing how to quantify the "gap" when an unconstrained continuous minimum does not land on a lattice point.
**Topic needed for this proof:** Bounding the strictly positive integer gap when minimizing a strictly convex quadratic function over a lattice, given a known continuous minimum.
**Open-access substitute for that topic:** (open-access for topic: discrete versus continuous gaps in integer programming) — Conforti, M., Cornuéjols, G., and Zambelli, G. / 2014 / Integer Programming / Chapter 4 and 6 (pre-publication drafts openly hosted by authors).
**Connection:** Addresses Grader A's Critique #1 and #2. The author evaluates an isolated parabola $x_{r_i}^2 - (2k-1)x_{r_i}$ and finds a discrete minimum at $k$, yielding $-(k^2-k)$, but completely fails to balance this against the coupled system (the unquantified remainder). Schrijver's techniques are necessary to algebraically prove that the forced shift from the continuous optimum back to the integers strictly accrues enough positive energy to escape the negative well.
**Web search query:** `conforti cornuejols zambelli integer programming pdf`
**Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed substitutes that address the specific structural gaps, algebraic fallacies, and missing definitions identified by the graders. 

The underlying mathematical object you are studying is the **intersection matrix of a weighted tree**, heavily used in the topology of plumbed 3-manifolds and the resolution of surface singularities. The proof’s fatal flaw—decoupling the central vertex’s negative well from the leaf capacities—violates the global determinant constraints of these matrices.

### 1. The Matrix Expansion and Graph Laplacian
**Authors / Year:** Brouwer, A.E. and Haemers, W.H. / 2011
**Title:** Spectra of Graphs
**Type:** Book
**Venue:** Springer Universitext
**Main result or relevant chapter/section:** Chapter 1 and 2 cover the exact relationship between the adjacency matrix, the degree matrix, and the Graph Laplacian ($L = D - A$). It proves the foundational identity that the quadratic form $x^T L x$ is identically equal to $\sum_{i \sim j} (x_i - x_j)^2$.
**Topic needed for this proof:** The algebraic decomposition of a graph’s quadratic form into a sum of edge-difference squares and diagonal vertex capacities.
**Open-access substitute for that topic:** (open-access for topic: author-hosted complete book draft) — Brouwer / 2011 / Spectra of Graphs / personal homepage.
**Connection:** **Addresses Grader B’s Q2 and Slip 2.** The grader asks how to rewrite a tree quadratic form as edge-square terms plus vertex capacities without skipping steps. By expressing your matrix $M$ as $L + D_{w-d}$ (where $D_{w-d}$ is a diagonal matrix of the topological slack $w(x)-d(x)$), the asserted one-line expansion of $E_v(a)$ becomes a rigorously cited, standard matrix identity.
**Web search query:** `brouwer haemers spectra of graphs pdf`
**Confidence (bibliographic):** HIGH

### 2. Coupled Optimization and Positive Definiteness
**Authors / Year:** Horn, R.A. and Johnson, C.R. / 2012
**Title:** Matrix Analysis (2nd Edition)
**Type:** Book
**Venue:** Cambridge University Press
**Main result or relevant chapter/section:** Chapter 7 (Positive Definite Matrices), specifically the section on the **Schur Complement**. It proves that a block matrix $M = \begin{pmatrix} A & B \\ B^T & C \end{pmatrix}$ is positive definite if and only if $C$ is positive definite and the Schur complement $A - B C^{-1} B^T$ is strictly positive definite.
**Topic needed for this proof:** Schur complement conditions for bounding the central vertex weight against the inverse of the surrounding branch matrices.
**Open-access substitute for that topic:** (open-access for topic: Schur complements and definiteness) — Gallier, J. / 2010 / The Schur Complement and Symmetric Positive Definite (and Semidefinite) Matrices / UPenn lecture notes.
**Connection:** **Addresses Grader A’s Q2 and Grader B’s Q5.** This is the exact tool to resolve the "Decoupled Optimization (Fallacy)." You cannot throw away the leaf weights to minimize the branch; the positive definiteness of the tree inherently couples them. For the Grader A counterexample star-graph (center $w(v)=2$, $d(v)=6$, leaf weights $4$), the Schur complement on the leaves is $w(v) - \sum \frac{1}{w(l_i)} = 2 - 6(1/4) = 0.5 > 0$. The graph is strictly positive definite *because* the leaf weights are large enough to absorb the central deficit. You must optimize the coupled system, not the isolated parabola.
**Web search query:** `gallier schur complement positive definite pdf`
**Confidence (bibliographic):** HIGH

### 3. Integer Definite Quadratic Forms
**Authors / Year:** Conway, J.H. and Sloane, N.J.A. / 1999
**Title:** Sphere Packings, Lattices and Groups (3rd Edition)
**Type:** Monograph
**Venue:** Springer Grundlehren der mathematischen Wissenschaften
**Main result or relevant chapter/section:** Chapter 2 (Lattices and Quantizing) and Chapter 15. The text establishes that any strictly positive definite integral lattice structurally bounded away from zero must have a minimum non-zero integer norm of at least 1 (and classifies those attaining exactly 1 or 2).
**Topic needed for this proof:** The minimal non-zero norm of a positive definite integral quadratic form.
**Open-access substitute for that topic:** (open-access for topic: Integral lattices and minimum norm) — Elkies, N. / 1998 / Lattices, Linear Codes, and Invariants / Harvard Math 250 lecture notes.
**Connection:** **Addresses Grader B’s Q1.** The grader specifically asks why $Q(x) \ge 1$ for all non-zero integer vectors. This is a foundational property of definite integer lattices (there are no integer vectors strictly between 0 and 1). Citing this formalizes the opening line of your proof and secures the discrete lattice floor you are trying to balance against the negative deficit well.
**Web search query:** `elkies lattices minimal norm pdf`
**Confidence (bibliographic):** HIGH

### 4. Intersection Lattices of Trees (The Geographic Context)
**Authors / Year:** Neumann, W.D. / 1981
**Title:** A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves
**Type:** Paper
**Venue:** Transactions of the American Mathematical Society, Vol. 268
**Main result or relevant chapter/section:** Develops the explicit criteria for when the intersection matrix of a star-shaped weighted tree (a "plumbing graph") is positive/negative definite, mapping the exact algebraic trade-offs between a deficit central weight and high-capacity leaves.
**Topic needed for this proof:** Definiteness criteria and determinants for intersection matrices of plumbing trees with a central deficit vertex.
**Open-access substitute for that topic:** (open-access for topic: intersection matrices of plumbing graphs) — Némethi, A. / 1999 / "Five lectures on normal surface singularities" / Colloquia Mathematica Societatis János Bolyai (often hosted as a survey preprint on the author's site).
**Connection:** **Addresses Grader A’s Q1 and Q3.** The problem you are trying to solve is natively a problem about plumbing graphs. Neumann’s paper shows exactly how to compute the coupled integer minimum you need for Case 2. By looking at how topologists resolve these intersection matrices (often using "continued fraction" expansions down the branches), you will see exactly how to prevent dropping the $\sum c_y x_y^2$ terms, allowing you to bridge the artificial negative well.
**Web search query:** `neumann calculus for plumbing pdf`
**Confidence (bibliographic):** HIGH

---
### Research Librarian Advice for the Re-write:
Grader A is entirely correct about the fatal algebraic fallacy in **Case 2**. You established a continuous functional with a negative well $-(k^2-k)$ at the root of the branch, and then minimized the branch by setting the internal edges to zero, pushing the vector out to the leaves. But you *dropped* the leaf capacity penalty $c_l x_l^2$ during the minimization, treating it as an afterthought. 

To fix this, you must use the **Schur Complement** (Horn & Johnson). The positive definiteness of the tree inherently guarantees that the positive coefficient of the leaf weights structurally dwarfs the negative linear pull from the center when coupled together. Optimize the matrix block-by-block dynamically from the leaves inward, rather than decoupling the branch.
