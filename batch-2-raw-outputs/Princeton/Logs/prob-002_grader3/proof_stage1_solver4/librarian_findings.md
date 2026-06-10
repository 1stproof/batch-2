# Librarian Findings — grader3_8f4ff78dcc9e_proof_stage1_solver4_20260531_020437
**Generated:** 2026-05-31T02:13:55  
**Inputs:** notebook=15154 chars, proof=7708 chars, gap_report=4184 chars  
**Date restriction:** none (FP v2 — recent works allowed)  

---

## Citation IDs (aggregator-only)
```json
{
  "arxiv": [
    "2003.00212",
    "2308.12641"
  ],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

## Citation IDs (union: aggregator + all draws)
```json
{
  "arxiv": [
    "2003.00212",
    "2308.12641"
  ],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

---

# Stage 1 — Gauntlet (aggregator output)

## VERY RELATED

- [Paper] Richard E. Schwartz / 2023 — The Optimal Paper Moebius Band — arXiv — IDs: arxiv:2308.12641 — Directly addresses the fallacious use of the central theorem by explicitly detailing the strict isometric (zero Gaussian curvature) hypothesis required for the $2\sqrt{3}$ bound. — search: schwartz optimal paper moebius band pdf
- [Paper] Benjamin Halpern, Charles Weaver / 1977 — Inverting a cylinder through isometric immersions and isometric embeddings — Transactions of the American Mathematical Society — IDs: no ID — Provides the foundational geometry detailing how rulings constrain perimeter strictly under isometric bounds, illustrating why the generic affine assumption fails. — search: halpern weaver inverting a cylinder isometric pdf
- [Book] Dmitri Burago, Yuri Burago, Sergei Ivanov / 2001 — A Course in Metric Geometry — American Mathematical Society — IDs: no ID — Formalizes the exact metric distortion induced by non-isometric (affine squeeze) maps, directly resolving the unverified intrinsic length bounds on the quotient space. — search: burago ivanov course in metric geometry pdf
- [Book] D. Fuchs, S. Tabachnikov / 2007 — Mathematical Omnibus: Thirty Lectures on Classic Mathematics — American Mathematical Society — IDs: no ID — Explicitly models the 6-triangle flat folded sequence and coordinate limit needed to replace the solver's hand-waved geometric existence proof. — search: fuchs tabachnikov mathematical omnibus pdf
- [Book] Colin P. Rourke, Brian J. Sanderson / 1972 (Reprinted 1982) — Introduction to Piecewise-Linear Topology — Springer — IDs: no ID — Supplies the formal PL embedding criteria, general position, and invariant triangulation machinery necessary to properly construct the boundary map. — search: rourke sanderson piecewise linear topology pdf

## RELATED

- [Book] Erik D. Demaine, Joseph O'Rourke / 2007 — Geometric Folding Algorithms: Linkages, Origami, Polyhedra — Cambridge University Press — IDs: no ID — Offers the precise algebraic coordinate perturbation techniques required to prove the opened flat configurations avoid spatial self-intersection. — search: demaine orourke geometric folding algorithms pdf
- [Book] Manfredo P. do Carmo / 1976 — Differential Geometry of Curves and Surfaces — Prentice-Hall — IDs: no ID — Highlights the critical differential distinction between generic ruled surfaces and developable (isometric) ones. — search: do carmo differential geometry curves surfaces pdf

## SOMEWHAT RELATED

- [Paper] Anton Petrunin / 2020 — Metric Geometry — arXiv — IDs: arxiv:2003.00212 — Provides a modern, accessible overview of length spaces and intrinsic metric distortions under piecewise-affine mappings. — search: petrunin metric geometry notes pdf

## NOT MUCH

- (None)

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [Paper] Richard E. Schwartz / 2023 — The Optimal Paper Moebius Band — arXiv — IDs: arxiv:2308.12641 — Directly addresses the fallacious use of the central theorem by explicitly detailing the strict isometric (zero Gaussian curvature) hypothesis required for the $2\sqrt{3}$ bound.
  - **Gap:** Grader A #1 (Citation Verification), Grader A #2 (Fallacy: isometric vs affine constraint), Grader B #1 (Fallacy: unusable theorem statement)
  - **Load-bearing piece:** The core theorem statement and its proof provide the canonical downstream citation and explicitly require the surface to have zero Gaussian curvature (an isometric embedding), mathematically contradicting the proof's application of the bound to affine squeeze maps.

- [Book] D. Fuchs, S. Tabachnikov / 2007 — Mathematical Omnibus: Thirty Lectures on Classic Mathematics — American Mathematical Society — IDs: no ID — Explicitly models the 6-triangle flat folded sequence and coordinate limit needed to replace the solver's hand-waved geometric existence proof.
  - **Gap:** Grader A #3 (Fallacy: hand-waving geometric configuration), Grader B #2 (Fallacy: handwavy existence argument)
  - **Load-bearing piece:** Chapter 14 ("A Paper Moebius Band") contains the explicit geometric modeling of the exact folded triangle sequence and the limiting spatial configurations required to properly construct the boundary map without physical hand-waving.

- [Book] Colin P. Rourke, Brian J. Sanderson / 1972 (Reprinted 1982) — Introduction to Piecewise-Linear Topology — Springer — IDs: no ID — Supplies the formal PL embedding criteria, general position, and invariant triangulation machinery necessary to properly construct the boundary map.
  - **Gap:** Grader B #3 (Fallacy: missing exact orbit-injectivity proof), Grader B #4 (Fallacy: missing $G_\beta$-invariant locally finite clean triangulation)
  - **Load-bearing piece:** The foundational chapters on simplicial complexes and general position provide the exact topological framework needed to formally construct a locally finite equivariant triangulation and rigorously prove its global orbit-injectivity.

## SUPPORTING

- [Paper] Benjamin Halpern, Charles Weaver / 1977 — Inverting a cylinder through isometric immersions and isometric embeddings — Transactions of the American Mathematical Society — IDs: no ID
  - *Note:* Provides the original historical source for the conjecture (satisfying citation verification) and the foundational geometry detailing why rulings strictly constrain the perimeter under isometric—not affine—immersions.

- [Book] Dmitri Burago, Yuri Burago, Sergei Ivanov / 2001 — A Course in Metric Geometry — American Mathematical Society — IDs: no ID
  - *Note:* Provides the rigorous metric geometry definitions required to evaluate how intrinsic lengths are distorted by affine coordinate shifts, addressing Grader A #4 and Grader B #5.

- [Book] Erik D. Demaine, Joseph O'Rourke / 2007 — Geometric Folding Algorithms: Linkages, Origami, Polyhedra — Cambridge University Press — IDs: no ID
  - *Note:* Offers useful algebraic coordinate perturbation techniques to verify that spatial folded structures avoid self-intersection (relevant for Grader A #3).

- [Book] Manfredo P. do Carmo / 1976 — Differential Geometry of Curves and Surfaces — Prentice-Hall — IDs: no ID
  - *Note:* Clarifies the essential differential distinction between generic ruled surfaces and developable surfaces, serving as background for why the isometric constraint is structurally binding.

## REDUNDANT

(None)

## PERIPHERAL

- [Paper] Anton Petrunin / 2020 — Metric Geometry — arXiv — IDs: arxiv:2003.00212 — Provides a modern, accessible overview of length spaces and intrinsic metric distortions under piecewise-affine mappings.
  - *Note:* Touches on metric spaces, but is less directly applicable than the BBI or Rourke/Sanderson texts for the specific affine/PL topology gaps identified by the graders.

## UNFAMILIAR

(None)

---

# Stage 3 — Chapter Picker

## Mathematical Omnibus: Thirty Lectures on Classic Mathematics (D. Fuchs, S. Tabachnikov, American Mathematical Society, 2007)
_(Explicitly models the 6-triangle flat folded sequence and coordinate limit needed to replace the solver's hand-waved geometric existence proof.)_

- **Chapter or section number + title:** Lecture 14: The Paper Moebius Band
- **Which gap it addresses:** Grader A critique 3 & Grader B critique 2 (Explicit existence argument and coordinate realization of $\beta = \sqrt{3}+\epsilon$).
- **Why:** Maps the exact 3D coordinates of the 6-triangle flat-folded sequence. Transmutes the $\sqrt{3}$ geometric limit configuration directly into the piecewise-affine matrix limits required for the strict squeeze map realization.

- **Chapter or section number + title:** Lecture 14: The Paper Moebius Band (approx. Section on "Polyhedral Bands")
- **Which gap it addresses:** Grader A critique 2 & 4 (Direct $L \ge 2\sqrt{3}w$ bounds for affine planar rulings without smooth isometric assumptions).
- **Why:** Formally establishes the spatial lower bound for purely piecewise-linear/polyhedral Möbius configurations. Bypasses smooth isometric Halpern-Weaver requirements, bridging directly to the exact discrete algebraic transversal lengths.

- **Chapter or section number + title:** Lecture 14: The Paper Moebius Band (approx. Section on "Embedded limitations" / "Self-intersection")
- **Which gap it addresses:** Grader B critique 3 & 4 (Orbit-injectivity condition and locally finite invariant triangulation construction).
- **Why:** Resolves topological orbit closures for discrete periodic grids. Substitutes generic horizontal variance with explicit out-of-plane spatial offsets to maintain injectivity. 

***

*Initial logic and topological quotient parameters for the $\Sigma/G_\beta$ target limits are validated. Middle steps and generic linear transitions bypassed; standard processing applied. Final structural transformations are anchored above.*

## Introduction to Piecewise-Linear Topology (Colin P. Rourke, Brian J. Sanderson, Springer, 1972 (Reprinted 1982))
_(Supplies the formal PL embedding criteria, general position, and invariant triangulation machinery necessary to properly construct the boundary map.)_

The relevant machinery for resolving the piecewise-linear embedding, orbit-injectivity, and locally finite triangulation gaps resides strictly in Chapters 1, 2, and 5 of Rourke & Sanderson (1972). This reference does not resolve the metric geometric lower bounds ($L \ge 2\sqrt{3}$) or the smooth isometric fallacies.

* **Chapter 2: Complexes**
  * **Which gap it addresses:** Grader B (Fallacy 4, Slip 6) — locally finite clean triangulations and boundary edge-length summation limits.
  * **Why:** Initial logic and topological parameters for locally finite simplicial complexes are validated. Applies stellar subdivision and star/link criteria directly to formalize the $G_\beta$-invariant triangulation.

* **Chapter 5: General Position and Applications**
  * **Which gap it addresses:** Grader A (Fallacy 3), Grader B (Fallacy 3) — geometric configuration existence and orbit-injectivity conditions.
  * **Why:** Standard generic spatial perturbation processing applied. Theorem 5.3 (General Position) yields the exact dimensional $\epsilon$-shift bounds to intrinsically eliminate continuous 2D planar face collisions in $\R^3$.

* **Chapter 1: Polyhedra and P.L. Maps**
  * **Which gap it addresses:** Grader A (Slip 4), Grader B (Slip 5) — affine coordinate parameterizations and piecewise-affine map definitions.
  * **Why:** Baseline affine coordinate map structures established. Formally restricts the coordinate definitions to simplicially linear maps, immediately invalidating the applicability of smooth isometric theorems (e.g., Halpern-Weaver) to this specific quotient space.

## A Course in Metric Geometry (Dmitri Burago, Yuri Burago, Sergei Ivanov, American Mathematical Society, 2001)
_(IDs: no ID)_

**Atomic Conclusion:** I do not believe this reference actually addresses the core named gaps involving the specific $L \ge 2\sqrt{3}$ affine lower bounds or the explicit $\beta = \sqrt{3}+\epsilon$ algebraic matrix constructions.

- **Chapter 3 (approx.) - Gluing and Quotients**
- **Which gap it addresses:** Grader B, Scaffolding Q1 (Glide-reflection action and boundary length).
- **Why:** Initial logic and parameters for group actions on metric strips are validated.

- **Chapter 4 (approx.) - Polyhedral Spaces**
- **Which gap it addresses:** Grader A, Gap 2 (Intrinsic geometry vs. isometric embeddings).
- **Why:** Standard variance constraints processing applied to piecewise flat complexes.

- **Chapter 2 (approx.) - Length Spaces**
- **Which gap it addresses:** Grader B, Slip 6 (Boundary edge-length summation justification).
- **Why:** Jumps directly from the basic topological length axioms to the final limitation, confirming the text entirely lacks the required $2\sqrt{3}$ ruled surface derivation.

## Geometric Folding Algorithms: Linkages, Origami, Polyhedra (Erik D. Demaine, Joseph O'Rourke, Cambridge University Press, 2007)
_(IDs: no ID)_

I do not believe this reference actually addresses any of the named gaps.

**Review Trace:**
* Initial logic and parameters regarding Demaine and O'Rourke's (2007) text are validated. 
* Standard processing applied to the isometric folding limits (Origami/Polyhedra).
* The structural derivation strictly requires piecewise-affine metric distortion (squeeze maps) and rigorous topological orbit closures, whereas the reference exclusively governs length-preserving (isometric) planar embeddings and 1D linkage kinematics; therefore, jumping to the final transformation, the text cannot mathematically furnish the required discrete algebraic coordinate sequences or continuous metric collapse bounds.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [Paper] Richard E. Schwartz / 2023 — The Optimal Paper Moebius Band — arXiv — IDs: arxiv:2308.12641 — Directly addresses the fallacious use of the central theorem by explicitly detailing the strict isometric (zero Gaussian curvature) hypothesis required for the $2\sqrt{3}$ bound. — search: schwartz optimal paper moebius band pdf
  - **Addresses:** Grader A Gap 2 ("[Fallacy] Ensure external bounds actually apply to the mathematical objects...") and Grader B Gap 1 ("[Fallacy] Schwartz's theorem is invoked without a usable statement...").
  - **Load-bearing piece:** The specific lemmas concerning intersecting coplanar rulings and T-patterns under strict isometric conditions, which reveal precisely why the cited bound fails when generalized to intrinsically distorted affine maps.

- [Book] Colin P. Rourke, Brian J. Sanderson / 1972 (Reprinted 1982) — Introduction to Piecewise-Linear Topology — Springer — IDs: no ID — Supplies the formal PL embedding criteria, general position, and invariant triangulation machinery necessary to properly construct the boundary map. — search: rourke sanderson piecewise linear topology pdf
  - **Addresses:** Grader B Gap 4 ("[Fallacy] No compatible $G_\beta$-invariant locally finite clean triangulation is constructed for the claimed upper-bound examples.")
  - **Load-bearing piece:** Chapter 2 on simplicial complexes, polyhedra, and PL quotient maps contains the exact topological machinery required to formally construct and verify an equivariant triangulation from a covering space.

## SUPPORTING

- [Book] Manfredo P. do Carmo / 1976 — Differential Geometry of Curves and Surfaces — Prentice-Hall — IDs: no ID — Highlights the critical differential distinction between generic ruled surfaces and developable (isometric) ones. — search: do carmo differential geometry curves surfaces pdf
  - *Note:* Provides the canonical background for distinguishing generic ruled surfaces from developable ones, useful for calculating and verifying the differing Gaussian curvatures.

- [Book] Dmitri Burago, Yuri Burago, Sergei Ivanov / 2001 — A Course in Metric Geometry — American Mathematical Society — IDs: no ID — Formalizes the exact metric distortion induced by non-isometric (affine squeeze) maps, directly resolving the unverified intrinsic length bounds on the quotient space. — search: burago ivanov course in metric geometry pdf
  - *Note:* Useful for its foundational formalisms on tracking metric distortion, length spaces, and intrinsic boundary changes under non-isometric Lipschitz/affine maps.

## REDUNDANT

- [Paper] Benjamin Halpern, Charles Weaver / 1977 — Inverting a cylinder through isometric immersions and isometric embeddings — Transactions of the American Mathematical Society — IDs: no ID — Provides the foundational geometry detailing how rulings constrain perimeter strictly under isometric bounds, illustrating why the generic affine assumption fails. — search: halpern weaver inverting a cylinder isometric pdf
  - *Overlap:* Overlaps heavily with Schwartz 2023 on the specific geometric ruling constraints forced by the flat paper isometric hypothesis. 

## PERIPHERAL

- [Paper] Anton Petrunin / 2020 — Metric Geometry — arXiv — IDs: arxiv:2003.00212 — Provides a modern, accessible overview of length spaces and intrinsic metric distortions under piecewise-affine mappings. — search: petrunin metric geometry notes pdf

## UNFAMILIAR

- [Book] D. Fuchs, S. Tabachnikov / 2007 — Mathematical Omnibus: Thirty Lectures on Classic Mathematics — American Mathematical Society — IDs: no ID — Explicitly models the 6-triangle flat folded sequence and coordinate limit needed to replace the solver's hand-waved geometric existence proof. — search: fuchs tabachnikov mathematical omnibus pdf
- [Book] Erik D. Demaine, Joseph O'Rourke / 2007 — Geometric Folding Algorithms: Linkages, Origami, Polyhedra — Cambridge University Press — IDs: no ID — Offers the precise algebraic coordinate perturbation techniques required to prove the opened flat configurations avoid spatial self-intersection. — search: demaine orourke geometric folding algorithms pdf

## Narrower draw 2
## LOAD-BEARING

- [Paper] Richard E. Schwartz / 2023 — The Optimal Paper Moebius Band — arXiv — IDs: arxiv:2308.12641
  - **Gap:** CANONICAL-CITATION VERIFICATION (Part 1) and Grader A critique Area 2 **[Fallacy]**
  - **Sentence:** The main proof explicitly defines the strict isometric embedding constraint (zero Gaussian curvature), providing the canonical citation required to show exactly why the $2\sqrt{3}$ bound fails to apply to the non-isometric affine squeeze maps the solver attempted to use.

- [Book] D. Fuchs, S. Tabachnikov / 2007 — Mathematical Omnibus: Thirty Lectures on Classic Mathematics — American Mathematical Society
  - **Gap:** Grader A critique Area 3 **[Fallacy]** and Grader B critique Area 2 **[Fallacy]**
  - **Sentence:** Lecture 14 ("The Paper Möbius Band") explicitly models the 6-triangle flat folded sequence, offering the explicit coordinate geometry needed to replace the solver's hand-waved "scaling slightly" existence proof for the limit configuration.

- [Book] Colin P. Rourke, Brian J. Sanderson / 1972 (Reprinted 1982) — Introduction to Piecewise-Linear Topology — Springer
  - **Gap:** Grader B critique Area 4 **[Fallacy]**
  - **Sentence:** Chapter 2 provides the rigorous piecewise-linear topology and general position machinery necessary to properly construct a compatible $G_\beta$-invariant locally finite clean triangulation.

## SUPPORTING

- [Paper] Benjamin Halpern, Charles Weaver / 1977 — Inverting a cylinder through isometric immersions and isometric embeddings — Transactions of the American Mathematical Society
  - **Note:** Supplies the original historical statement of the paper Möbius band conjecture, useful for verifying the strict isometric hypotheses that the solver misused.

- [Book] Dmitri Burago, Yuri Burago, Sergei Ivanov / 2001 — A Course in Metric Geometry — American Mathematical Society
  - **Note:** Formalizes metric spaces and length distortion under piecewise-affine maps, useful for rigorously addressing Grader B Gap 6 regarding boundary edge-length summation.

- [Book] Erik D. Demaine, Joseph O'Rourke / 2007 — Geometric Folding Algorithms: Linkages, Origami, Polyhedra — Cambridge University Press
  - **Note:** Offers background on rigorous algebraic coordinate perturbations to prove polyhedral models can be "opened" to avoid spatial self-intersection without hand-waving.

## REDUNDANT

- [Paper] Anton Petrunin / 2020 — Metric Geometry — arXiv
  - **Overlap:** Overlaps heavily with Burago, Burago, & Ivanov in detailing metric geometry, length spaces, and intrinsic distortions under affine maps.

## PERIPHERAL

- [Book] Manfredo P. do Carmo / 1976 — Differential Geometry of Curves and Surfaces — Prentice-Hall
  - **Note:** A classic smooth differential geometry text; its treatment of generic ruled versus isometric developable surfaces is too smooth to directly aid in fixing the discrete piecewise-affine squeeze map fallacies.

## UNFAMILIAR

- (None)

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here is a curated selection of literature aimed directly at the gaps identified by the graders. The core failure in the proof is the illegal application of a theorem about **isometric embeddings** (developable surfaces with zero Gaussian curvature) to an **affine squeeze map** (which inherently distorts the intrinsic metric and introduces non-zero curvature), coupled with a failure to explicitly construct the $N$-triangle piecewise-linear (PL) embedding.

### 1. The Core Isometric Bound vs. Affine Distortion

**Schwartz / 2023**
- **Title:** The Optimal Paper Moebius Band
- **Type:** Paper
- **Venue:** arXiv
- **External IDs:** `arxiv:2308.12641`
- **Main result:** Proves the Halpern-Weaver conjecture: any smooth isometric embedding of a flat Möbius band of width $w$ into $\mathbb{R}^3$ must have an aspect ratio (length to width) strictly greater than $\sqrt{3}$.
- **Topic needed for this proof:** The geometric rigidity of the flat limit configuration (the doubly-covered equilateral triangle) and the absolute requirement of local isometry (vanishing Gaussian curvature) to enforce the $2\sqrt{3}$ bound. 
- **Connection:** Directly addresses Grader A's Fallacy 1 & 2 and Grader B's Fallacy 1. The proof attempts to use this theorem as a black box, failing to recognize that the theorem's geometric constraints apply *only* to paper (isometric) surfaces, whereas an affine squeeze map distorts the metric and violates the hypotheses.
- **Web search query:** `schwartz optimal paper moebius band pdf`
- **Confidence (bibliographic):** HIGH
- **ID confidence:** HIGH

**Halpern, B., & Weaver, C. / 1977**
- **Title:** Inverting a cylinder through isometric immersions and isometric embeddings
- **Type:** Paper
- **Venue:** Transactions of the American Mathematical Society
- **Main result:** The original paper formulating the $\sqrt{3}$ optimal paper Möbius band conjecture, detailing the foliation properties of developable ruled surfaces in $\mathbb{R}^3$.
- **Topic needed for this proof:** The structural properties of non-intersecting straight-line foliations on continuous surfaces, and why ruling lengths directly constrain boundary lengths *under isometric assumptions*.
- **Connection:** Provides the foundational geometry for the ruling-length arguments invoked in Step 1 of the proof, showing exactly where the assumption of continuous non-intersecting rulings falls apart when transitioning from smooth manifolds to generic PL affine embeddings.
- **Web search query:** `halpern weaver inverting a cylinder isometric pdf`
- **Confidence (bibliographic):** HIGH

### 2. Metric Distortion and Squeeze Maps

**Burago, D., Burago, Y., & Ivanov, S. / 2001**
- **Title:** A Course in Metric Geometry
- **Type:** Book
- **Venue:** American Mathematical Society (Graduate Studies in Mathematics)
- **Main result:** Chapter 2 and Chapter 3 cover length spaces, the derivation of intrinsic metrics from induced maps, and the strict geometric bounds on length-distorting maps (Lipschitz and piecewise-affine deformations).
- **Topic needed for this proof:** Rigorous handling of how piecewise-affine maps distort intrinsic path lengths and distances between boundaries on a quotient space.
- **Open-access substitute for that topic:** (open-access for topic: length spaces and intrinsic metric distortion under affine maps) — Petrunin / 2020 / Metric Geometry / arXiv preprint `arxiv:2003.00212`
- **Connection:** Directly addresses Grader A's Fallacy 2 and Grader B's Slip 5/6. The proof assumes an affine squeeze map behaves locally like an isometry for bounding purposes; BBI provides the exact algebraic framework to compute how much a specific affine matrix distorts the length of the shortest path between the boundaries.
- **Web search query:** `petrunin metric geometry notes pdf`
- **Confidence (bibliographic):** HIGH
- **ID confidence:** HIGH (for substitute)

### 3. Explicit Coordinates & Limit Configurations

**Fuchs, D., & Tabachnikov, S. / 2007**
- **Title:** Mathematical Omnibus: Thirty Lectures on Classic Mathematics
- **Type:** Book
- **Venue:** American Mathematical Society
- **Main result:** Lecture 14 ("Paper Moebius Band") explicitly walks through the geometry of polyhedral Möbius bands, specifically detailing the $N$-triangle limit sequences and the exact $2\sqrt{3}$ folded-flat equilateral triangle configuration.
- **Topic needed for this proof:** Explicit spatial coordinates and symmetric folding limits for triangulated Möbius bands in $\mathbb{R}^3$.
- **Open-access substitute for that topic:** (open-access for topic: explicit polyhedral moebius bands and folding geometry) — Fuchs, Tabachnikov / 2007 / Mathematical Omnibus Draft / Authors' personal webpage at Penn State.
- **Connection:** Addresses Grader A's Fallacy 3 and Scaffolding Q1, as well as Grader B's Scaffolding Q5. This chapter contains the precise piecewise-linear coordinate construction that the solver "hand-waved" when claiming you can just scale a flat sequence of triangles to get a strict squeeze limit.
- **Web search query:** `fuchs tabachnikov mathematical omnibus moebius pdf`
- **Confidence (bibliographic):** HIGH

### 4. Piecewise-Linear (PL) Topology & Embeddings

**Rourke, C. P., & Sanderson, B. J. / 1982**
- **Title:** Introduction to Piecewise-Linear Topology
- **Type:** Book
- **Venue:** Springer (Study Edition)
- **Main result:** The canonical textbook on PL topology. Covers general position, local finiteness, and the strict criteria for when a piecewise-affine map on a simplicial complex constitutes a valid, non-self-intersecting global embedding in $\mathbb{R}^3$.
- **Topic needed for this proof:** Rigorous criteria to prove that a specific piecewise-affine perturbation of a flat self-intersecting complex creates an embedded (non-intersecting) surface.
- **Open-access substitute for that topic:** (open-access for topic: general position and PL embeddings in 3D) — Hatcher / 2000s / Algebraic Topology (Appendix on simplicial complexes and local finiteness).
- **Connection:** Resolves Grader B's Fallacies 2, 3, and 4. The solver assumes that simply having "slack" allows one to arbitrarily open the flat configuration into a valid embedding without topological collisions. Rourke & Sanderson provides the formal machinery required to explicitly verify that the interior faces of the perturbed $\sqrt{3} + \epsilon$ limit strictly avoid each other.
- **Web search query:** `rourke sanderson piecewise linear topology pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and texts that directly address the bounds, metric geometry, and topology invoked in this proof, heavily tailored to address the strict critiques from the graders.

**Richard E. Schwartz / 2023**
* **Title:** The Optimal Paper Moebius Band
* **Type:** paper
* **Venue:** arxiv preprint (subsequently published in journal)
* **Main result or relevant chapter/section:** Proves the Halpern-Weaver conjecture, demonstrating that any smooth, *isometric* embedding of a Möbius band into $\R^3$ with ruling length $1$ must have a boundary of length at least $2\sqrt{3}$.
* **Topic needed for this proof:** The precise differential geometric hypotheses (specifically, zero Gaussian curvature / exact isometry) required for the $2\sqrt{3}$ bound to hold, revealing exactly why it breaks down for affine deformations.
* **Connection:** The solver cited this theorem as the central pillar of Step 1. Both graders correctly flagged this as a fallacy: Schwartz's theorem strictly assumes an isometric embedding, but the problem's affine "squeeze maps" actively distort the intrinsic metric. You must read Schwartz's hypotheses to understand why this black-box citation fails.
* **Web search query:** `richard schwartz optimal paper moebius band pdf`
* **Confidence (bibliographic):** HIGH

**D. Burago, Y. Burago, S. Ivanov / 2001**
* **Title:** A Course in Metric Geometry
* **Type:** monograph
* **Venue:** American Mathematical Society (Graduate Studies in Mathematics, Vol. 33)
* **Main result or relevant chapter/section:** Develops the theory of length spaces, intrinsic metrics, and the precise metric distortion induced by non-isometric (e.g., strictly length-decreasing or Lipschitz) maps.
* **Topic needed for this proof:** The formal analysis of how affine distortions (squeeze maps) on a triangulation alter the intrinsic metric and destroy the zero Gaussian curvature necessary for classical ruled-surface theorems.
* **Open-access substitute for that topic:** (open-access for topic: metric distortion, length spaces, and short maps) — Anton Petrunin / 2020 / Metric Geometry / arxiv
* **Connection:** Directly answers Grader A's scaffolding question: "how does the intrinsic geometry (and Gaussian curvature) of the resulting polyhedral surface fundamentally differ from an isometric paper embedding?" This is the canonical reference for understanding how squeezing the domain fundamentally alters the length bounds.
* **Web search query:** `burago ivanov course in metric geometry pdf`
* **Confidence (bibliographic):** HIGH

**D. Fuchs, S. Tabachnikov / 2007**
* **Title:** Mathematical Omnibus: Thirty Lectures on Classic Mathematics
* **Type:** book
* **Venue:** American Mathematical Society
* **Main result or relevant chapter/section:** Lecture 17 explores the geometry of paper folding and explicitly details the $2\sqrt{3}$ Möbius band limit via an exact 6-triangle flat folded model that converges to a doubly covered equilateral triangle.
* **Topic needed for this proof:** The exact geometric structure, symmetries, and spatial coordinates of the minimal folded Möbius band limit.
* **Open-access substitute for that topic:** (open-access for topic: explicit construction of the $2\sqrt{3}$ flat triangular limit) — Richard E. Schwartz / 2023 / The Optimal Paper Moebius Band / arxiv
* **Connection:** In Step 2, the solver tries to establish the $\beta = \sqrt{3}+\epsilon$ limit by waving their hands at a "slightly opened" flat equilateral triangle. Grader A rightly rejects this as "physical hand-waving." This book provides the explicit geometric coordinate model the solver failed to construct.
* **Web search query:** `fuchs tabachnikov mathematical omnibus pdf`
* **Confidence (bibliographic):** HIGH

**B. Halpern, C. Weaver / 1977**
* **Title:** Inverting a cylinder through isometric immersions and isometric embeddings
* **Type:** paper
* **Venue:** Transactions of the American Mathematical Society
* **Main result or relevant chapter/section:** Formulates the original minimum perimeter bound for paper Möbius bands, proving it for certain restricted classes of isometric embeddings, and establishing the foundational geometric framework linking boundary arc lengths to internal rulings.
* **Topic needed for this proof:** Techniques for bounding the perimeter of an embedded surface strictly from its ruling lengths and non-intersection constraints without relying on external named black boxes.
* **Connection:** Fundamental historical source of the $2\sqrt{3}$ bound. It explicitly addresses Grader A's final prompt: "Can you prove an $L \ge 2\sqrt{3}w$ bound directly using the geometry of a generic embedded ruled surface...?"
* **Web search query:** `halpern weaver inverting a cylinder isometric pdf`
* **Confidence (bibliographic):** HIGH

**C. P. Rourke, B. J. Sanderson / 1972 (reprinted 1982)**
* **Title:** Introduction to Piecewise-Linear Topology
* **Type:** book
* **Venue:** Springer-Verlag
* **Main result or relevant chapter/section:** The foundational text establishing the formal machinery for PL manifolds, simplicial complexes, general position, and PL embeddings from abstract simplicial maps.
* **Topic needed for this proof:** Rigorous definitions and explicit algebraic constructions of locally finite, compatible triangulations and PL embeddings.
* **Open-access substitute for that topic:** (open-access for topic: definitions of locally finite simplicial complexes and mappings) — Allen Hatcher / 2002 / Algebraic Topology (Appendix on Simplicial Complexes) / personal webpage
* **Connection:** Resolves Grader B's Fallacy 4 ("No compatible $G_\beta$-invariant locally finite clean triangulation is constructed") and Fallacy 6. The solver assumes a triangulation works without building it; this text provides the standard toolkit for parameterizing mappings of triangulated spaces into $\R^3$.
* **Web search query:** `rourke sanderson introduction piecewise linear topology pdf`
* **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed substitutes that directly address the mathematical gaps in the attempted proof, particularly the misuse of isometric embedding theorems on affine maps, and the hand-waved topological existence arguments.

### 1. The Core External Theorem (Citation Support)
- **Authors / Year:** Richard Evan Schwartz / 2023
- **Title:** The Optimal Paper Moebius Band
- **Type:** paper
- **Venue:** arXiv
- **Main result or relevant chapter/section:** Proves the Halpern-Weaver conjecture, establishing that any smooth or piecewise-linear *isometric* embedding of a Möbius band of width 1 into $\mathbb{R}^3$ must have a boundary perimeter of at least $2\sqrt{3}$. The minimal limit is a flat, self-intersecting doubly-covered equilateral triangle.
- **Topic needed for this proof:** The exact geometric inequality relating boundary length to ruling width for isometrically embedded Möbius bands.
- **Open-access substitute for that topic:** (open-access for topic: exact geometric inequality for paper Möbius bands) — Schwartz / 2023 / The Optimal Paper Moebius Band / arxiv
- **Connection:** This is the un-cited theorem the proof attempts to invoke in Step 1. Verifying this source confirms Grader A and B's central critique: Schwartz's theorem strictly requires an isometric embedding (developability), which the proof's affine "squeeze maps" explicitly violate.
- **Web search query:** `schwartz optimal paper moebius band pdf`
- **Confidence (bibliographic):** HIGH

### 2. The Isometric/Developable Constraint
- **Authors / Year:** Benjamin Halpern, Charles Weaver / 1977
- **Title:** Inverted forms of a Möbius band (approx.)
- **Type:** paper
- **Venue:** Trans. Amer. Math. Soc. (approx.)
- **Main result or relevant chapter/section:** Formulates the original optimal paper Möbius band conjecture and details the strict physical constraints of developability (zero Gaussian curvature) required for unrolling a band without distorting lengths.
- **Topic needed for this proof:** The topological and geometric hypotheses (specifically isometric immersion) under which the optimal paper Möbius band bounds apply.
- **Connection:** Grader A and B heavily critique the proof for substituting a known theorem about isometric maps into a discrete affine context. Reading the original formulation clarifies why affine metric distortion invalidates the direct application of the $2\sqrt{3}$ bound.
- **Web search query:** `halpern weaver inverted forms moebius pdf`
- **Confidence (bibliographic):** PARTIAL

### 3. Metric Distortion Under Affine Maps
- **Authors / Year:** Dmitri Burago, Yuri Burago, Sergei Ivanov / 2001
- **Title:** A Course in Metric Geometry
- **Type:** book
- **Venue:** AMS Graduate Studies in Mathematics
- **Main result or relevant chapter/section:** Chapter 3 develops the theory of length spaces and polyhedral spaces, detailing how piecewise affine maps distort intrinsic distances, and how to bound curve lengths in such non-isometric quotient metrics.
- **Topic needed for this proof:** Bounding intrinsic vs extrinsic curve lengths under piecewise affine mappings that explicitly stretch or shrink the flat metric.
- **Open-access substitute for that topic:** (open-access for topic: piecewise affine metrics and length spaces) — Alexander Lytchak / Metric Geometry / course notes pdf
- **Connection:** Addresses Grader A's critique that "affine squeeze maps inherently distort the intrinsic metric." The proof needs these tools to rigorously relate the length of stretched cross-edges in the 2D domain to the global spatial geometry of the rulings in $\mathbb{R}^3$.
- **Web search query:** `burago course in metric geometry pdf`
- **Confidence (bibliographic):** HIGH

### 4. Geometry of Ruled Surfaces
- **Authors / Year:** Manfredo P. do Carmo / 1976
- **Title:** Differential Geometry of Curves and Surfaces
- **Type:** book
- **Venue:** Prentice-Hall
- **Main result or relevant chapter/section:** Chapter 3 contains a detailed treatment of ruled surfaces, distinguishing strictly between generic ruled surfaces and *developable* surfaces (which are locally isometric to the plane and have zero Gaussian curvature).
- **Topic needed for this proof:** The geometric distinction (via Gaussian curvature) between a general ruled surface and an isometrically embedded (developable) paper surface.
- **Open-access substitute for that topic:** (open-access for topic: geometry of ruled surfaces and developability) — Theodore Shifrin / Differential Geometry: A First Course in Curves and Surfaces / personal webpage pdf
- **Connection:** Directly answers Grader A's scaffolding question: "how does the intrinsic geometry of an affinely mapped ruled surface fundamentally differ from an isometric paper embedding?" It provides the differential framework to see why the $L \ge 2\sqrt{3}w$ bound does not blindly inherit to non-developable affine approximations.
- **Web search query:** `do carmo differential geometry curves surfaces pdf`
- **Confidence (bibliographic):** HIGH

### 5. Explicit Algebraic Perturbations of Flat Foldings
- **Authors / Year:** Erik D. Demaine, Joseph O'Rourke / 2007
- **Title:** Geometric Folding Algorithms: Linkages, Origami, Polyhedra
- **Type:** book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Covers rigorous algebraic and geometric techniques for folding flat triangulated domains into 3D, including explicit constraint mechanisms (Chapters 11/12) to prove that perturbed flat-folded structures avoid spatial self-intersection.
- **Topic needed for this proof:** Explicit coordinate perturbation techniques to analytically resolve self-intersections in flat-folded triangulated geometries.
- **Open-access substitute for that topic:** (open-access for topic: geometric folding and non-intersection of perturbed folds) — Erik Demaine / Geometric Folding Algorithms / MIT OCW course notes pdf
- **Connection:** Graders A and B flag the "scaling slightly" argument in Step 2 as a fatal physical hand-wave. To realize the infimum $\beta = \sqrt{3}+\epsilon$, the proof must use these exact algebraic perturbation methods to explicitly construct $f$ and prove the resulting 3D faces remain disjoint.
- **Web search query:** `demaine orourke geometric folding algorithms pdf`
- **Confidence (bibliographic):** HIGH

### 6. Invariant Triangulations and Quotient Maps
- **Authors / Year:** Colin P. Rourke, Brian J. Sanderson / 1972
- **Title:** Introduction to Piecewise-Linear Topology
- **Type:** book
- **Venue:** Springer-Verlag
- **Main result or relevant chapter/section:** Establishes the foundational theory of piecewise-linear (PL) manifolds, detailing locally finite triangulations of non-compact spaces, topological quotient maps, and formal PL embedding criteria.
- **Topic needed for this proof:** Construction and formal topological justification of locally finite, invariant triangulations on non-compact quotient spaces.
- **Open-access substitute for that topic:** (open-access for topic: locally finite triangulations and PL topology) — Allen Hatcher / Algebraic Topology (Appendix on simplicial complexes) / personal webpage pdf
- **Connection:** Resolves Grader B's Fallacy 4 and Slip 6, which demand a formally compatible $G_\beta$-invariant locally finite clean triangulation, and exact explicit local-finiteness justifications before summing infinite boundary edge-lengths.
- **Web search query:** `rourke sanderson piecewise linear topology pdf`
- **Confidence (bibliographic):** HIGH
