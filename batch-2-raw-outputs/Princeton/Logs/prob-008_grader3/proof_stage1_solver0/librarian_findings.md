# Librarian Findings — grader3_f204b6faaedc_proof_stage1_solver0_20260531_022831
**Generated:** 2026-05-31T02:34:32  
**Inputs:** notebook=9877 chars, proof=9087 chars, gap_report=3943 chars  
**Date restriction:** none (FP v2 — recent works allowed)  

---

## Citation IDs (aggregator-only)
```json
{
  "arxiv": [],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": [
    "978-0-8218-5154-5"
  ]
}
```

## Citation IDs (union: aggregator + all draws)
```json
{
  "arxiv": [],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": [
    "978-0-8218-5154-5"
  ]
}
```

---

# Stage 1 — Gauntlet (aggregator output)

## VERY RELATED
- [book] Maclagan, D., and Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society (Graduate Studies in Mathematics, Vol. 161) — IDs: isbn:978-0-8218-5154-5 — Provides the canonical machinery for local tangent cones and zero-sum vector balancing within a polyhedral fan, directly refuting the proof's flawed local balancing arithmetic (Grader A Fallacy 1 & 2). — search: maclagan sturmfels introduction to tropical geometry pdf
- [paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — SIAM Journal on Discrete Mathematics — IDs: no ID — Establishes the exact equivalence between tropical linear spaces and valuated matroids, providing the algebraic framework needed to correctly classify $\Dr_2(F_7)$ without hallucinating topologies (Grader B Fallacy 1). — search: speyer tropical linear spaces pdf
- [paper] Ardila, F., and Klivans, C. J. / 2006 — The Bergman complex of a matroid and phylogenetic trees — Journal of Combinatorial Theory, Series B — IDs: no ID — Formally describes the polyhedral fan structure of the ambient Bergman complex $\Trop(M)$ using primitive rays and 2D sectors, essential for coordinatizing the Fano plane's tropical lines (Grader A Q1/Q2). — search: ardila klivans bergman complex matroid pdf

## RELATED
- [paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2012 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID — Details explicit combinatorial types and valid tree decompositions of tropical planes, modeling how to mathematically resolve the multiple-ray branching missed by the proof (Grader A Fallacy 2). — search: herrmann jensen joswig sturmfels how to draw tropical planes pdf
- [paper] Dress, A. W. M., and Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID — Introduces orthogonal valuated duality and defines evaluation rules at tropical limits, which is necessary to correctly handle boundary strata and loop-containing flats rigorously (Grader B Fallacy 3). — search: dress wenzel valuated matroids pdf
- [book] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (Second Edition) — Cambridge University Press — IDs: no ID — Supplies the standard poset-theoretic lemmas proving that an order-reversing bijection on a bounded, graded poset must exactly map atoms ($\Dr_1$) to coatoms ($\Dr_2$), fixing an unjustified step (Grader A Slip 3). — search: stanley enumerative combinatorics vol 1 pdf

## SOMEWHAT RELATED
- [book] Oxley, J. G. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID — Standard reference providing the explicit incidence-reversing algebraic polarity of the Fano plane, addressing the critique that the polarity was invoked without formal construction (Grader B Slip 7). — search: oxley matroid theory pdf

## NOT MUCH
*(No unhelpful or irrelevant sources were supplied by the librarians.)*

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [book] Maclagan, D., and Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society (Graduate Studies in Mathematics, Vol. 161) — IDs: isbn:978-0-8218-5154-5 — Provides the canonical machinery for local tangent cones and zero-sum vector balancing within a polyhedral fan, directly refuting the proof's flawed local balancing arithmetic (Grader A Fallacy 1 & 2). — search: maclagan sturmfels introduction to tropical geometry pdf
  - **Gaps addressed:** Grader A Fallacy 1, Grader B Fallacy 4
  - **Load-bearing piece:** Chapter 3 (Tropical Varieties) and Chapter 4 (Local Tangent Cones) provide the formal definitions of zero-sum vector balancing and tangent cone geometry required to rigorously correct the flawed local branching checks.

- [paper] Ardila, F., and Klivans, C. J. / 2006 — The Bergman complex of a matroid and phylogenetic trees — Journal of Combinatorial Theory, Series B — IDs: no ID — Formally describes the polyhedral fan structure of the ambient Bergman complex $\Trop(M)$ using primitive rays and 2D sectors, essential for coordinatizing the Fano plane's tropical lines (Grader A Q1/Q2). — search: ardila klivans bergman complex matroid pdf
  - **Gaps addressed:** Grader A Scaffolding Questions 1 & 2, Grader B Slip 5
  - **Load-bearing piece:** Section 2 details the fine subdivision of the Bergman fan, supplying the specific integer vector arithmetic and primitive ray coordinates for 2D sectors inside matroid fans.

- [paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — SIAM Journal on Discrete Mathematics — IDs: no ID — Establishes the exact equivalence between tropical linear spaces and valuated matroids, providing the algebraic framework needed to correctly classify $\Dr_2(F_7)$ without hallucinating topologies (Grader B Fallacy 1). — search: speyer tropical linear spaces pdf
  - **Gaps addressed:** Grader A Fallacy 2, Grader B Fallacy 1
  - **Load-bearing piece:** Section 3 on the combinatorial characterization of tropical linear spaces maps out their underlying metric tree topologies, directly establishing the bounds to resolve the missing rank-2 structural classification.

- [book] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (Second Edition) — Cambridge University Press — IDs: no ID — Supplies the standard poset-theoretic lemmas proving that an order-reversing bijection on a bounded, graded poset must exactly map atoms ($\Dr_1$) to coatoms ($\Dr_2$), fixing an unjustified step (Grader A Slip 3). — search: stanley enumerative combinatorics vol 1 pdf
  - **Gaps addressed:** Grader A Slip 3, Grader B Fallacy 2
  - **Load-bearing piece:** Chapter 3 (Partially Ordered Sets) contains the precise standard lemmas verifying that an order-reversing bijection on a bounded, graded poset inherently swaps atoms with coatoms.

## SUPPORTING

- [paper] Dress, A. W. M., and Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID — Introduces orthogonal valuated duality and defines evaluation rules at tropical limits, which is necessary to correctly handle boundary strata and loop-containing flats rigorously (Grader B Fallacy 3). — search: dress wenzel valuated matroids pdf
  - Provides foundational valuated duality theorems necessary as background for validating limits and loop-containing flat inclusions on boundary strata.

- [book] Oxley, J. G. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID — Standard reference providing the explicit incidence-reversing algebraic polarity of the Fano plane, addressing the critique that the polarity was invoked without formal construction (Grader B Slip 7). — search: oxley matroid theory pdf
  - Serves as the authoritative background reference to formally construct the incidence-reversing algebraic polarity of the Fano plane.

## REDUNDANT

*(None)*

## PERIPHERAL

- [paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2012 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID — Details explicit combinatorial types and valid tree decompositions of tropical planes, modeling how to mathematically resolve the multiple-ray branching missed by the proof (Grader A Fallacy 2). — search: herrmann jensen joswig sturmfels how to draw tropical planes pdf
  - Focuses on drawing tropical *planes* (rank 3), which represents a strict dimensional mismatch for resolving the needed missing topological classification of tropical *lines* (rank 2, 1-dimensional metric trees) identified in the gaps.

## UNFAMILIAR

*(None)*

---

# Stage 3 — Chapter Picker

## Introduction to Tropical Geometry (Maclagan, D., and Sturmfels, B., American Mathematical Society (Graduate Studies in Mathematics, Vol. 161), 2015)
_(Provides the canonical machinery for local tangent cones and zero-sum vector balancing within a polyhedral fan, directly refuting the proof's flawed local balancing arithmetic (Grader A Fallacy 1 & 2). — search: maclagan sturmfels introduction to tropical geometry pdf)_

Here are the specific chapters and sections from Maclagan & Sturmfels (*Introduction to Tropical Geometry*, 2015) that provide the canonical machinery to correct the fatal geometric and balancing flaws identified by the graders.

**Chapter 3, Section 3.3 (approx.) — The Structure Theorem and the Balancing Condition**
*   **Which gap it addresses:** Grader A Fallacy 1, Grader B Fallacy 4 (Flawed local balancing arithmetic and omitted local directions).
*   **Why:** This section formally defines the zero-sum balancing condition for tropical varieties around codimension-1 faces and introduces the machinery of local tangent cones (star fans). Applying the star fan at the point ray $e_1$ properly identifies the valid internal primitive directions (e.g., $L_j - e_1$), directly refuting the proof's false claim that outgoing edges are artificially forced to equal the global rays $L_1, L_2, L_3$.

**Chapter 4, Section 4.2 (approx.) — Parameterized Tropical Curves / Tropical Curves in $\mathbb{R}^n$**
*   **Which gap it addresses:** Grader A Fallacy 2 (False claims about tree branching topologies and cycles).
*   **Why:** This chapter details how abstract metric graphs (like genus-0 trees) are parameterized and embedded into ambient spaces while preserving the balancing condition at vertices. It provides the exact classification needed to show how a multivalent vertex can perfectly partition leaf rays (like $L_1, L_2, L_3$ and the remaining points) without violating genus-0 tree constraints or creating algebraic cycles.

**Chapter 5, Sections 5.2 & 5.3 (approx.) — Tropical Linear Spaces and Bergman Fans**
*   **Which gap it addresses:** Grader B Fallacies 1 and 3 (Asserted classification of $\Dr_2(F_7)$, failure to address boundary strata/loops in tropical projective space).
*   **Why:** These sections establish the foundational structure of the Dressian and map tropical linear spaces bijectively to valuated matroids. Section 5.2 explicitly addresses tropical projective closures ($\mathbb{TP}^{n-1}$) and how loops in matroid quotients correspond to limit points on the boundary strata. This is required to rigorously classify all valid 1-dimensional fans in $\Dr_2(F_7)$ rather than asserting the families by sight. 

**Chapter 2, Section 2.2 / 2.3 (approx.) — Polyhedral Fans and Lineality Spaces**
*   **Which gap it addresses:** Grader B Scaffolding Q1 and Q3 (Finding primitive internal vectors and local cone configurations).
*   **Why:** To address the arithmetic failures noted by the graders, the proof needs the rigorous polyhedral geometry definitions of cones, primitive integer vectors, and lattice quotients by the all-ones vector $\mathbf{1}$. This provides the strict algebraic justification for computing $(L_1 - e_1) + \dots \equiv 0 \pmod{\mathbf{1}}$ within the ambient Bergman fan.

## Enumerative Combinatorics, Volume 1 (Second Edition) (Stanley, R. P., Cambridge University Press, 2011)
_(Supplies the standard poset-theoretic lemmas proving that an order-reversing bijection on a bounded, graded poset must exactly map atoms ($\Dr_1$) to coatoms ($\Dr_2$), fixing an unjustified step (Grader A Slip 3). — search: stanley enumerative combinatorics vol 1 pdf)_

Here are the specific sections from Stanley's *Enumerative Combinatorics, Volume 1* that address the poset-theoretic gaps in the proof. 

*(Note: As a strictly combinatorial reference, this text does not address the geometric gaps regarding Bergman fans, balancing conditions, or tropical projective closures flagged by the graders. It only rescues the poset logic.)*

- **Chapter 3, Section 3.1: Basic concepts**
  - **Which gap it addresses:** Grader A Slip 3, Grader B Fallacy 2, Grader B Scaffolding Q2.
  - **Why:** This section establishes the fundamental definitions for bounded posets (featuring a minimum $\hat{0}$ and maximum $\hat{1}$), graded posets, rank functions, atoms, and coatoms. It provides the elementary lemmas demonstrating that an order-reversing bijection is an isomorphism to the dual poset $P^*$. Because isomorphisms must preserve maximal chain lengths, the bijection mathematically forces elements covering $\hat{0}$ (atoms / $\Dr_1$) to map exactly to elements covered by $\hat{1}$ (coatoms / $\Dr_2$). 

- **Chapter 3, Section 3.1: Basic concepts (Order Ideals and Filters)**
  - **Which gap it addresses:** Grader B Scaffolding Q5.
  - **Why:** Stanley formally defines principal order ideals (generated by a single element, matching the proof's $I(V)$) and principal dual ideals/filters (matching $F(q)$). Referencing these definitions provides the rigorous order-theoretic framework to justify that an anti-automorphism bijectively swaps principal ideals with principal filters, securing the cardinality contradiction step without relying on the geometric dimension assumptions Grader B critiqued.

## Matroid Theory (2nd Edition) (Oxley, J. G., Oxford University Press, 2011)
_(Standard reference providing the explicit incidence-reversing algebraic polarity of the Fano plane, addressing the critique that the polarity was invoked without formal construction (Grader B Slip 7). — search: oxley matroid theory pdf)_

Here are the specific sections from Oxley's *Matroid Theory* that address the algebraic and matroid-theoretic gaps, followed by a necessary boundary on what the text covers.

**Chapter 1, Section 1.5 (approx.) — Projective Geometries**
- **Which gap it addresses:** Grader B, Slip 7 (The Fano polarity is invoked but not explicitly constructed).
- **Why:** This section introduces the Fano matroid $F_7$ explicitly as the projective plane $PG(2, 2)$ over the finite field $GF(2)$. By defining the matroid via all non-zero vectors in $GF(2)^3$, it provides the exact algebraic coordinates for the 7 points and 7 lines needed to rigorously ground the polarity. 

**Chapter 2, Section 2.2 (approx.) — Duals of Representable Matroids**
- **Which gap it addresses:** Grader B, Slip 7 (The Fano polarity is invoked but not explicitly constructed).
- **Why:** This section establishes the fundamental theorem that the dual of a representable matroid is obtained via the orthogonal complement of its row space. For $F_7$, taking the standard dot product over $GF(2)$ and mapping a 1D span (a point $v$) to its 2D orthogonal complement (the line $v^\perp = \{x \in GF(2)^3 \mid v \cdot x = 0\}$) provides the exact, explicitly constructed incidence-reversing algebraic polarity required to satisfy the critique.

**I do not believe this reference actually addresses any of the remaining named gaps.**
- **Which gap it addresses:** Grader A (1-3) and Grader B (1-6).
- **Why:** Oxley's text is the standard foundational reference for pure classical matroid theory. It predates and entirely excludes tropical geometry, the relative Dressian ($\Dr(M)$), metric trees, polyhedral fan balancing conditions, and tropical linear spaces. You will need a different reference (such as Maclagan and Sturmfels' *Introduction to Tropical Geometry*) to address the flaws in the tropical curve classifications and tangent cone balancing checks.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [book] Maclagan, D., and Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society (Graduate Studies in Mathematics, Vol. 161) — IDs: isbn:978-0-8218-5154-5 — Provides the canonical machinery for local tangent cones and zero-sum vector balancing within a polyhedral fan, directly refuting the proof's flawed local balancing arithmetic (Grader A Fallacy 1 & 2). — search: maclagan sturmfels introduction to tropical geometry pdf
  - **Gap(s):** Grader A Fallacy 1, Grader A Fallacy 2, Grader B Fallacy 4
  - **Location:** Chapter 3 covers tropical curves, balancing conditions, and the geometry of local tangent cones (star/link) within polyhedral fans, providing the exact machinery to compute valid internal branching directions.

- [paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — SIAM Journal on Discrete Mathematics — IDs: no ID — Establishes the exact equivalence between tropical linear spaces and valuated matroids, providing the algebraic framework needed to correctly classify $\Dr_2(F_7)$ without hallucinating topologies (Grader B Fallacy 1). — search: speyer tropical linear spaces pdf
  - **Gap(s):** Grader B Fallacy 1
  - **Location:** The main theorems outlining the parameterization of tropical linear spaces via Plücker relations and valuated matroids offer the algebraic basis necessary to rigorously classify the combinatorial components of $\Dr_2(F_7)$.

- [book] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (Second Edition) — Cambridge University Press — IDs: no ID — Supplies the standard poset-theoretic lemmas proving that an order-reversing bijection on a bounded, graded poset must exactly map atoms ($\Dr_1$) to coatoms ($\Dr_2$), fixing an unjustified step (Grader A Slip 3). — search: stanley enumerative combinatorics vol 1 pdf
  - **Gap(s):** Grader A Slip 3, Grader B Fallacy 2
  - **Location:** Chapter 3 (Posets) explicitly details the structural properties of bounded, graded posets, containing the lemma that an anti-isomorphism strictly reverses ranks, forcing atoms to map to coatoms.

## SUPPORTING

- [paper] Ardila, F., and Klivans, C. J. / 2006 — The Bergman complex of a matroid and phylogenetic trees — Journal of Combinatorial Theory, Series B — IDs: no ID — Formally describes the polyhedral fan structure of the ambient Bergman complex $\Trop(M)$ using primitive rays and 2D sectors, essential for coordinatizing the Fano plane's tropical lines (Grader A Q1/Q2). — search: ardila klivans bergman complex matroid pdf
  - **Note:** Essential background for verifying the fine subdivision of the Bergman fan into sectors and generating the vector sums needed to answer Grader A Q1/Q2.

- [paper] Dress, A. W. M., and Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID — Introduces orthogonal valuated duality and defines evaluation rules at tropical limits, which is necessary to correctly handle boundary strata and loop-containing flats rigorously (Grader B Fallacy 3). — search: dress wenzel valuated matroids pdf
  - **Note:** Provides the foundational axioms on valuated matroids and limits, useful for explicitly resolving boundary strata inclusions (Grader B Fallacy 3).

- [book] Oxley, J. G. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID — Standard reference providing the explicit incidence-reversing algebraic polarity of the Fano plane, addressing the critique that the polarity was invoked without formal construction (Grader B Slip 7). — search: oxley matroid theory pdf
  - **Note:** The definitive textbook to quickly source the standard rigid algebraic construction of the Fano plane polarity to close Grader B Slip 7.

## REDUNDANT

- [paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2012 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID — Details explicit combinatorial types and valid tree decompositions of tropical planes, modeling how to mathematically resolve the multiple-ray branching missed by the proof (Grader A Fallacy 2). — search: herrmann jensen joswig sturmfels how to draw tropical planes pdf
  - **Overlap:** Heavily overlaps with both Speyer (for the combinatorics of tropical planes) and Maclagan-Sturmfels (for tree decompositions and zero-sum balancing in fans).

## PERIPHERAL
*(None)*

## UNFAMILIAR
*(None)*

## Narrower draw 2
## LOAD-BEARING

- [book] Maclagan, D., and Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society (Graduate Studies in Mathematics, Vol. 161) — IDs: isbn:978-0-8218-5154-5
  - **Addresses:** Grader A Fallacy 1, Grader B Fallacy 4, Grader B Q3
  - **Load-bearing piece:** Chapter 3 (specifically Sections 3.3 and 3.4) details the canonical machinery for local tangent cones, weights, and zero-sum vector balancing arithmetic at branching nodes within polyhedral fans.

- [paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — SIAM Journal on Discrete Mathematics — IDs: no ID
  - **Addresses:** Grader B Fallacy 1, Grader A Fallacy 2
  - **Load-bearing piece:** Sections 2 and 3 establish the algebraic equivalence between rank 2 tropical linear spaces, tree topologies, and valuated matroids, directly providing the framework to rigorously classify $\Dr_2(F_7)$.

- [book] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (Second Edition) — Cambridge University Press — IDs: no ID
  - **Addresses:** Grader A Slip 3, Grader B Fallacy 2, Grader B Q2
  - **Load-bearing piece:** Chapter 3 covers bounded, graded posets and provides the foundational order-theoretic lemmas proving that an order-reversing bijection inherently exchanges atoms (rank 1) with coatoms (corank 1).

- [paper] Ardila, F., and Klivans, C. J. / 2006 — The Bergman complex of a matroid and phylogenetic trees — Journal of Combinatorial Theory, Series B — IDs: no ID
  - **Addresses:** Grader A Q1, Grader A Q2
  - **Load-bearing piece:** Section 2 explicitly constructs the polyhedral structure of the Bergman fan $\Trop(M)$ using primitive integer rays and sectors corresponding to flags of flats, which dictates the local primitive inward-pointing vectors.

## SUPPORTING

- [book] Oxley, J. G. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID
  - Provides the explicit standard formulation of the Fano plane polarity and duality requested by Grader B Slip 7.

- [paper] Dress, A. W. M., and Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID
  - Foundational background defining valuated matroid axioms and orthogonal valuated duality, necessary for understanding the limit boundary strata (Grader B Fallacy 3).

## REDUNDANT

- [paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2012 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID
  - Overlaps with Speyer (2008) and Maclagan & Sturmfels (2015) regarding the combinatorial types of tropical lines/planes, though it remains a useful visualization aid for tree topologies. 

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and open-access substitutes that directly address the gaps identified by the graders, particularly concerning the local balancing of tropical curves, the structure of the Bergman fan, and the poset-theoretic mapping between ranks.

**1. Maclagan, D., and Sturmfels, B. / 2015**
- **Title:** Introduction to Tropical Geometry
- **Type:** book
- **Venue:** American Mathematical Society (Graduate Studies in Mathematics, Vol. 161)
- **Main result or relevant chapter/section:** Chapter 3 formalizes polyhedral tropical varieties, local tangent cones (star fans), and the zero-sum balancing condition. Chapter 4 rigorously defines tropical linear spaces.
- **Topic needed for this proof:** The zero-sum balancing condition and local tangent cone analysis for determining valid incoming/outgoing edge directions of a tropical curve inside a fan.
- **Open-access substitute:** (open-access for topic: Local tangent cones and balancing for tropical varieties) — Maclagan, Sturmfels / 2014 / Introduction to Tropical Geometry (Draft) / authors' personal webpages
- **Connection:** Directly addresses Grader A's first gap and Grader B's fourth gap. The proof incorrectly asserts that branching at a point ray is impossible by artificially restricting the outgoing edge directions. Chapter 3 provides the exact machinery to compute the local tangent cones and correctly execute the zero-sum vector balancing that the proof botched.
- **Web search query:** `maclagan sturmfels introduction to tropical geometry draft pdf`
- **Confidence (bibliographic):** HIGH

**2. Speyer, D. E. / 2008**
- **Title:** Tropical Linear Spaces
- **Type:** paper
- **Venue:** SIAM Journal on Discrete Mathematics 22(4)
- **Main result or relevant chapter/section:** Proves that tropical linear spaces satisfy the zero-tension (balancing) condition everywhere and establishes their exact structural equivalence to valuated matroids.
- **Topic needed for this proof:** The structural equivalence between balanced 1-dimensional polyhedral complexes (tropical lines) and rank-2 valuated matroids.
- **Open-access substitute:** (open-access for topic: Equivalence of tropical linear spaces and valuated matroids) — Speyer / 2004 / Tropical Linear Spaces / arxiv
- **Connection:** Grader B challenges the proof's hand-waved classification of $\Dr_2(F_7)$ (Gap B1). Speyer's foundational theorem is required to rigorously classify valid tropical lines within the ambient space, ensuring that local metric graph balancing guarantees a valid valuated matroid globally without the cycles Grader A correctly identified as missing.
- **Web search query:** `speyer tropical linear spaces pdf`
- **Confidence (bibliographic):** HIGH

**3. Ardila, F., and Klivans, C. J. / 2006**
- **Title:** The Bergman complex of a matroid and phylogenetic trees
- **Type:** paper
- **Venue:** Journal of Combinatorial Theory, Series B
- **Main result or relevant chapter/section:** Demonstrates that the Bergman complex of a matroid $M$ is a polyhedral fan whose fine subdivision is isomorphic to the order complex of the lattice of flats of $M$.
- **Topic needed for this proof:** The explicit polyhedral fan structure (rays and 2-dimensional sectors) of the Bergman fan of a matroid constructed from flags of flats.
- **Open-access substitute:** (open-access for topic: Fan structure of the Bergman complex of a matroid) — Ardila, Klivans / 2003 / The Bergman complex of a matroid and phylogenetic trees / arxiv
- **Connection:** Step 2 of the proof explicitly relies on the geometric layout of the ambient Bergman fan $\Trop(F_7)$ to restrict where tropical lines can travel. This paper is the canonical source for the point-and-line ray construction and the 2D sector geometry the proof leverages.
- **Web search query:** `ardila klivans bergman complex matroid pdf`
- **Confidence (bibliographic):** HIGH

**4. Stanley, R. P. / 2011**
- **Title:** Enumerative Combinatorics, Volume 1 (2nd Edition)
- **Type:** book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 3 exhaustively details the structural properties of graded partially ordered sets, rank functions, and dualities.
- **Topic needed for this proof:** The lemma that an order-reversing bijection (anti-automorphism) on a bounded, graded poset necessarily exchanges elements of rank $k$ with elements of corank $k$.
- **Open-access substitute:** (open-access for topic: Dualities and rank functions of bounded graded posets) — Stanley / 2011 / Enumerative Combinatorics Volume 1 (Draft) / math.mit.edu
- **Connection:** Closes Grader A's third gap and Grader B's second gap. The proof nakedly asserts that the involution $\Phi$ must restrict to a bijection between the specific strata $\Dr_2$ and $\Dr_1$. Stanley provides the canonical poset-theoretic justification for why an anti-isomorphism forces the exchange of atoms and coatoms.
- **Web search query:** `stanley enumerative combinatorics vol 1 pdf`
- **Confidence (bibliographic):** HIGH

**5. Oxley, J. G. / 2011**
- **Title:** Matroid Theory (2nd Edition)
- **Type:** book
- **Venue:** Oxford University Press
- **Main result or relevant chapter/section:** Chapter 2 covers duals, projective geometries, and provides an extensive catalogue of structural properties and symmetries for small matroids, including the Fano plane $F_7$.
- **Topic needed for this proof:** The explicit geometric or matrix construction of the Fano plane's incidence-reversing polarity.
- **Open-access substitute:** (open-access for topic: Symmetries and dualities of the Fano matroid) — survey chapters or lecture notes on intro matroid theory often cover this explicitly (e.g., lecture notes by Federico Ardila or similar intro combinatorics courses).
- **Connection:** Grader B notes (Gap B7) that "The Fano polarity is invoked but not explicitly constructed." While well-known to experts, passing verification requires citing the explicit algebraic construction of this polarity, which Oxley provides.
- **Web search query:** `oxley matroid theory pdf`
- **Confidence (bibliographic):** HIGH

**6. Dress, A. W. M., and Wenzel, W. / 1992**
- **Title:** Valuated Matroids
- **Type:** paper
- **Venue:** Advances in Mathematics
- **Main result or relevant chapter/section:** Formally introduces valuated matroids and establishes their cryptomorphisms via valuated bases and circuits, strictly defining evaluation behaviors over the tropical semiring.
- **Topic needed for this proof:** The formal algebraic rules for evaluating degenerate matroid states and resolving boundary bounds (valuations approaching infinity).
- **Connection:** Grader B requests clarification on how boundary strata and loop-containing flat inclusions behave in tropical projective space (Gap B3). Dress and Wenzel's foundational paper is required to defend how the tropical limits algebraically collapse into the posets' lower-dimensional bounding faces. 
- **Web search query:** `dress wenzel valuated matroids pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical published sources and relevant topic-keyed substitutes that address the graders' critiques and supply the missing foundations for the proof.

- **Authors / Year**: Maclagan, D., and Sturmfels, B. / 2015
- **Title**: Introduction to Tropical Geometry
- **Type**: book
- **Venue**: AMS Graduate Studies in Mathematics, Vol. 161
- **External IDs**: isbn:978-0-8218-5154-5
- **Main result or relevant chapter/section**: Chapter 3 covers polyhedral fans and local tangent cones; Chapter 4 covers the balancing condition for tropical curves (metric graphs) and Chapter 4.4 formally defines tropical linear spaces.
- **Topic needed for this proof**: The balancing condition for tropical curves at vertices using local tangent cones, which dictates valid local directions and weights.
- **Open-access substitute for that topic**: (open-access for topic: Draft PDF of Introduction to Tropical Geometry) — Maclagan, Sturmfels / 2014 / Introduction to Tropical Geometry / Authors' personal websites.
- **Connection**: Directly addresses Grader A's critique [Fallacy 1 and 2] by demonstrating that valid internal directions $L_j - e_1$ balance perfectly with the leaf $e_1$, and answers Grader B's Q3 regarding local tangent cones and balancing weights.
- **Web search query**: `maclagan sturmfels introduction to tropical geometry pdf`
- **Confidence (bibliographic)**: HIGH
- **ID confidence**: PARTIAL

- **Authors / Year**: Speyer, D. / 2008
- **Title**: Tropical Linear Spaces
- **Type**: paper
- **Venue**: SIAM Journal on Discrete Mathematics
- **External IDs**: 
- **Main result or relevant chapter/section**: Proves the foundational equivalence between tropical linear spaces, valuated matroids, and the Bergman fans of matroids, including the structure of boundary strata and projective closures.
- **Topic needed for this proof**: The definition of the tropical projective Grassmannian and how boundary strata (including loop-containing flats) are incorporated into tropical linear spaces.
- **Open-access substitute for that topic**: (open-access for topic: arxiv preprint of Tropical Linear Spaces) — Speyer / 2004 / Tropical Linear Spaces / arxiv.
- **Connection**: Addresses Grader B's Fallacy 3 and Scaffolding Q4 regarding boundary strata and loop-containing flat inclusions from tropical projective closure. This is also the canonical literature counterpart to the structural equivalence theorem mistakenly named the "Brandt-Maclagan-Sturmfels anti-isomorphism" in the notebook.
- **Web search query**: `david speyer tropical linear spaces pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Ardila, F., and Klivans, C. J. / 2006
- **Title**: The Bergman complex of a matroid and phylogenetic trees
- **Type**: paper
- **Venue**: Journal of Combinatorial Theory, Series B
- **External IDs**: 
- **Main result or relevant chapter/section**: Geometrically realizes the Bergman fan of a matroid as a polyhedral fan given by the order complex of the lattice of proper flats, explicitly describing its rays and maximal cells.
- **Topic needed for this proof**: The explicit polyhedral geometry, primitive ray vectors, and 2D sector coordinate spaces of the Bergman fan $\Trop(M)$ for matroids.
- **Open-access substitute for that topic**: (open-access for topic: arxiv preprint) — Ardila, Klivans / 2003 / The Bergman complex of a matroid and phylogenetic trees / arxiv.
- **Connection**: Provides the geometric formulation required for Grader A's Scaffolding Q1 and Q2, explicitly detailing how to compute primitive integer vectors and evaluate vector sums modulo $\mathbf{1}$ in the sectors of $\Trop(F_7)$.
- **Web search query**: `ardila klivans bergman complex matroid pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Dress, A. W. M., and Wenzel, W. / 1992
- **Title**: Valuated Matroids
- **Type**: paper
- **Venue**: Advances in Mathematics
- **External IDs**: 
- **Main result or relevant chapter/section**: Introduces valuated matroids as a quantitative generalization of matroids, establishing their cryptomorphic axioms and explicitly defining orthogonal duality $M \mapsto M^\perp$.
- **Topic needed for this proof**: Orthogonal duality of valuated matroids and how it formally reverses the bounded poset of quotients.
- **Open-access substitute for that topic**: 
- **Connection**: Validates the duality mappings currently explored in the notebook (PS-C) and establishes the canonical mathematical existence of the orthogonal valuated duality involution that the proof implicitly relies on.
- **Web search query**: `dress wenzel valuated matroids pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Stanley, R. P. / 2011
- **Title**: Enumerative Combinatorics, Volume 1 (Second Edition)
- **Type**: book
- **Venue**: Cambridge University Press
- **External IDs**: 
- **Main result or relevant chapter/section**: Chapter 3 ("Partially Ordered Sets") comprehensively covers graded posets, rank functions, principal ideals/filters, and the order-theoretic properties of poset isomorphisms and anti-automorphisms.
- **Topic needed for this proof**: The standard order-theoretic properties forcing an order-reversing bijection of a bounded, graded poset to rigidly exchange rank $k$ elements with corank $k$ elements (e.g., atoms with coatoms).
- **Open-access substitute for that topic**: (open-access for topic: PDF draft of Enumerative Combinatorics, Volume 1) — Stanley / 2011 / Enumerative Combinatorics, Volume 1 / Author's MIT webpage.
- **Connection**: Closes Grader A's Slip 3 and Grader B's Scaffolding Q2 and Q5 by providing the definitive mathematical justification for why an involution $\Phi$ must strictly restrict to a bijection mapping $\Dr_2$ directly to $\Dr_1$, preserving the comparison of dimensions.
- **Web search query**: `stanley enumerative combinatorics volume 1 pdf`
- **Confidence (bibliographic)**: HIGH

## Gauntlet draw 2
Here are the canonical references and structural substitutes needed to trace the techniques in the proof and specifically address the grader critiques regarding balancing conditions, the Dressian stratification, and graded poset anti-isomorphisms.

*(Note: The notebook's "Brandt-Maclagan-Sturmfels Theorem" is an AI hallucinated attribution from a previous round. The canonical published sources for the bijection between tropical linear spaces, the relative Dressian, and valuated matroids are Speyer (2008) and Maclagan & Sturmfels (2015).)*

- **Authors / Year** — D. Maclagan, B. Sturmfels / 2015
- **Title** — Introduction to Tropical Geometry
- **Type** — book
- **Venue** — American Mathematical Society (Graduate Studies in Mathematics, Vol. 161)
- **External IDs** — `isbn:978-0-8218-5154-5`
- **Main result or relevant chapter/section** — Chapter 3 rigorously develops tropical curves, polyhedral fans, and the precise zero-sum balancing conditions for vertices and branching nodes. Chapter 4 classifies tropical linear spaces, Bergman fans, and defines the Dressian via its correspondence with valuated matroids.
- **Topic needed for this proof** — The formal geometric balancing condition modulo lineality spaces for tropical curves intersecting polyhedral fan sectors.
- **Open-access substitute for that topic** — (open-access for topic: pre-publication book draft) — Maclagan, Sturmfels / 2014 / Introduction to Tropical Geometry / Authors' personal webpages.
- **Connection** — Directly addresses Grader A's Fallacies 1 and 2 and Grader B's Fallacy 4. The proof fails because it botches the local tangent cone balancing arithmetic at the boundary rays. Chapter 3 shows exactly how to compute these weights and primitive vectors within a fan to verify the missing 7 continuous families.
- **Web search query** — `maclagan sturmfels introduction to tropical geometry pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — D. Speyer / 2008
- **Title** — Tropical Linear Spaces
- **Type** — paper
- **Venue** — SIAM Journal on Discrete Mathematics (Vol. 22, No. 4)
- **Main result or relevant chapter/section** — Proves that tropical linear spaces are uniquely and completely parameterized by valuated matroids (functions satisfying the tropical Plücker relations).
- **Topic needed for this proof** — The reduction of the continuous geometric problem of classifying tropical linear spaces to the finite algebraic problem of classifying valuated matroid structures on the underlying ground set.
- **Open-access substitute for that topic** — (open-access for topic: original preprint) — Speyer / 2004 / Tropical Linear Spaces / arxiv.
- **Connection** — Addresses Grader B's Fallacy 1 ("The classification of $\Dr_2(F_7)$ is asserted rather than proved"). To rigorously classify the rank 2 elements of the Dressian without hallucinating missed families, one must compute the valuated rank-2 matroids covering $F_7$, which this paper operationalizes.
- **Web search query** — `speyer tropical linear spaces pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — F. Ardila, C. Klivans / 2006
- **Title** — The Bergman complex of a matroid and phylogenetic trees
- **Type** — paper
- **Venue** — Journal of Combinatorial Theory, Series B (Vol. 96, No. 1)
- **Main result or relevant chapter/section** — Establishes that the Bergman fan of a matroid $M$ can be realized as a polyhedral fan whose cones are parameterized by chains of flats in the lattice of flats of $M$.
- **Topic needed for this proof** — The geometric coordinatization of the Bergman fan $\Trop(M)$ into rays (points/lines) and 2D sectors (flags) from the matroid's lattice of flats.
- **Connection** — Provides the canonical published support for Step 2 of the proof, which correctly builds the ambient 2D polyhedral fan $\Trop(F_7)$ using rays for points/lines and 2D sectors for their incidence flags.
- **Web search query** — `ardila klivans bergman complex of a matroid pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — R. P. Stanley / 2011 (2nd Edition)
- **Title** — Enumerative Combinatorics, Volume 1
- **Type** — book
- **Venue** — Cambridge University Press
- **Main result or relevant chapter/section** — Chapter 3 (Partially Ordered Sets) details the structural properties of graded posets, including rigorous treatments of length, duality, and order-reversing bijections.
- **Topic needed for this proof** — The standard combinatorial lemmas proving that an order-reversing bijection on a bounded, graded poset must map elements of rank $k$ to elements of corank $k$.
- **Open-access substitute for that topic** — (open-access for topic: author draft) — R. P. Stanley / 2011 / Enumerative Combinatorics, Volume 1 / MIT author webpage.
- **Connection** — Answers Grader B's Scaffolding Question 2 and critique of Step 4. The proof carelessly asserts that $\Phi$ restricts to $\Dr_2 \to \Dr_1$ without proof; citing the bounded graded poset properties from Chapter 3 seals this gap.
- **Web search query** — `stanley enumerative combinatorics vol 1 pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — A. W. M. Dress, W. Wenzel / 1992
- **Title** — Valuated Matroids
- **Type** — paper
- **Venue** — Advances in Mathematics (Vol. 93, No. 2)
- **Main result or relevant chapter/section** — The foundational paper introducing valuated matroids. It establishes the existence of a canonical orthogonal duality $M \mapsto M^\perp$ for valuated matroids.
- **Topic needed for this proof** — The existence and properties of the orthogonal dual involution on the space of valuated matroids.
- **Connection** — This is the actual canonical source for the "orthogonal valuated duality" the notebook is desperately trying to leverage to build the involution $\Psi(N)^\perp$. Any attempt to compute the $\Phi$ mappings algebraicly via coefficients must trace back to the duality defined here.
- **Web search query** — `dress wenzel valuated matroids pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — S. Herrmann, A. Jensen, M. Joswig, B. Sturmfels / 2012
- **Title** — How to draw tropical planes
- **Type** — paper
- **Venue** — Electronic Journal of Combinatorics (Vol. 19, No. 2)
- **Main result or relevant chapter/section** — Computes explicit stratifications and combinatorial types of tropical lines and planes, detailing their topological degrees of freedom.
- **Topic needed for this proof** — The rigorous algorithmic methodology to exhaustively list the tree topologies and parameter spaces of tropical lines within a bounded tropical linear space.
- **Connection** — Directly models how to avoid Grader A's Fallacy 2 (claiming trees cannot branch on multiple rays without creating cycles) by showing correct explicit genus-0 decompositions of tropical lines spanning symmetric arrangements.
- **Web search query** — `herrmann jensen joswig sturmfels how to draw tropical planes pdf`
- **Confidence (bibliographic):** HIGH
