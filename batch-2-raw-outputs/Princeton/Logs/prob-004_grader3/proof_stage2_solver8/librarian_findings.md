# Librarian Findings — grader3_615170f75a78_proof_stage2_solver8_20260531_013838
**Generated:** 2026-05-31T01:42:41  
**Inputs:** notebook=6868 chars, proof=8591 chars, gap_report=2873 chars  
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
- [Monograph] Herbert Federer / 1969 — Geometric Measure Theory — Springer-Verlag — IDs: no ID — Establishes multilinear comass bounds (Step 2) and the rigorous slicing of integral currents required to preserve mapping degree on piecewise-smooth fibers (Step 1). — search: federer geometric measure theory slicing pdf
- [Book] L. C. Evans, R. F. Gariepy / 1992 — Measure Theory and Fine Properties of Functions — CRC Press — IDs: no ID — Provides the precise regularity conditions and Jacobian integration bounds required to apply the Coarea formula to globally Lipschitz maps with corners (Step 1). — search: evans gariepy measure theory fine properties pdf
- [Book] J. Michael Steele / 1997 — Probability Theory and Combinatorial Optimization — SIAM — IDs: no ID — Exposes the core mathematical fallacy in Step 3 by proving MST bounds control 1-dimensional length rather than 2-dimensional area, fatally undermining the fractional scaling. — search: steele probability theory combinatorial optimization pdf

## RELATED
- [Paper] Larry Guth / 2010 — Metaphors in systolic geometry — Proceedings of the ICM 2010 — IDs: no ID — Formalizes the explicit mechanics of topological product-folding maps and the correct integration of MST bounds with coarea formulas. — search: larry guth metaphors systolic geometry pdf
- [Paper] Mikhail Gromov / 2003 — Isoperimetry of waists and concentration of maps — Geometric and Functional Analysis (GAFA) — IDs: no ID — Introduces waist inequalities to rigorously lower-bound the multi-sheeted transverse volume of generic mapping fibers under dilation constraints. — search: gromov isoperimetry waists concentration maps pdf
- [Book] Mikhail Gromov / 1999 — Metric structures for Riemannian and non-Riemannian spaces — Birkhäuser — IDs: no ID — Details the multilinear algebraic justification for bounding the pullback of differential area forms using uniform bounds on 2-dilation (Step 2). — search: gromov metric structures for riemannian pdf
- [Lecture notes] Leon Simon / 1983 — Lectures on Geometric Measure Theory — Centre for Mathematical Analysis (ANU) — IDs: no ID — Canonical open-access substitute for Federer, explicitly proving that the boundary of a slice is algebraically the slice of the boundary. — search: leon simon lectures geometric measure theory pdf

## SOMEWHAT RELATED
- [Paper] Larry Guth / 2011 — Volumes of balls in large Riemannian manifolds — Annals of Mathematics — IDs: no ID — Underlying literature for the "1D tree counterexample" (IPT-61), showing how mapping to metric trees bypasses naive geometric projection constraints. — search: larry guth volumes balls large riemannian pdf
- [Paper] Mikhail Gromov / 1999 — Metric inequalities with scalar curvature — Geometric and Functional Analysis (GAFA) — IDs: no ID — Analyzes macroscopic dimension and area-contracting mappings, highlighting that bounded 2-dilation does not prevent 1-dimensional distances from shrinking arbitrarily. — search: gromov metric inequalities scalar curvature pdf

## NOT MUCH
- [Book] V. Guillemin, A. Pollack / 1974 — Differential Topology — Prentice-Hall — IDs: no ID — Offers classical smooth transversality arguments for invariant mapping degrees, but relies on smooth strata and fails at the piecewise-smooth corners critiqued by Grader B. — search: michael hutchings differential topology notes pdf

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- **[Monograph] Herbert Federer / 1969 — Geometric Measure Theory — Springer-Verlag**
  - **Addresses:** Grader B critique: Fallacy 1 and Scaffolding Question 1.
  - **Load-bearing piece:** Section 4.3 (Slicing) rigorously establishes the algebraic identity for slicing integral currents ($\partial \langle T, f, y \rangle = \langle \partial T, f, y \rangle$), which is the exact machinery required to preserve mapping degrees on regular fibers of piecewise-smooth maps.

- **[Book] L. C. Evans, R. F. Gariepy / 1992 — Measure Theory and Fine Properties of Functions — CRC Press**
  - **Addresses:** Grader B critique: Slip 5 and Scaffolding Question 2.
  - **Load-bearing piece:** Chapter 3 provides the precise measure-theoretic regularity hypotheses (via Rademacher's theorem and Jacobian integrability) justifying the application of the general Coarea formula to globally Lipschitz maps with non-smooth corners.

- **[Book] J. Michael Steele / 1997 — Probability Theory and Combinatorial Optimization — SIAM**
  - **Addresses:** Grader A critique: Fallacy 1 and Scaffolding Question 3 (and Grader B critique: Fallacy 2).
  - **Load-bearing piece:** The chapters on Euclidean combinatorial optimization (such as the BHH theorem) prove that Minimum Spanning Tree/TSP bounds rigorously control 1-dimensional length scaling, structurally invalidating the proof's attempt to extrapolate a non-linear fractional bound for *2-dimensional* transverse area.

## SUPPORTING

- **[Paper] Larry Guth / 2010 — Metaphors in systolic geometry — Proceedings of the ICM 2010**
  Provides necessary geometric context for the "topological product-folding maps" and how transversal folding physically relates to fractional algebraic exponents (Grader B Scaffolding Q4 and Q5).
- **[Paper] Mikhail Gromov / 2003 — Isoperimetry of waists and concentration of maps — Geometric and Functional Analysis (GAFA)**
  Provides the rigorous foundation for waist inequalities, which govern the volume of generic multi-sheeted fibers under macroscopic metric constraints.

## REDUNDANT

- **[Lecture notes] Leon Simon / 1983 — Lectures on Geometric Measure Theory — Centre for Mathematical Analysis (ANU)**
  Overlaps with Federer (1969); both cover the exact slicing theory of integral currents required for the sliced relative degree-one statement (Grader B Fallacy 1).
- **[Book] Mikhail Gromov / 1999 — Metric structures for Riemannian and non-Riemannian spaces — Birkhäuser**
  Overlaps with Federer (1969); both cover the multilinear algebra and comass inequalities required to bound pullbacks of differential area forms (Grader B Slip 6 and Scaffolding Q3).

## PERIPHERAL

- **[Paper] Larry Guth / 2011 — Volumes of balls in large Riemannian manifolds — Annals of Mathematics**
  Addresses the mapping to metric trees (IPT-61), which relates to a retired coordinate projection attempt rather than the current active Coarea/slicing formulation.
- **[Paper] Mikhail Gromov / 1999 — Metric inequalities with scalar curvature — Geometric and Functional Analysis (GAFA)**
  Explores area contraction and 1-dimensional distance limits, but has no specific bearing on the Coarea/MST slicing mechanics under active critique.
- **[Book] V. Guillemin, A. Pollack / 1974 — Differential Topology — Prentice-Hall**
  Relies entirely on smooth strata and transversality; it is mathematically invalid on the piecewise-smooth maps with corners actively contested by Grader B.

## UNFAMILIAR
*(None)*

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [Monograph] Herbert Federer / 1969 — Geometric Measure Theory — Springer-Verlag
  - **Gap Addressed:** Grader B - Area for Improvement 1 ("The sliced relative degree-one statement is not proved") and Scaffolding Question 1.
  - **Load-bearing piece:** Chapter 4 (specifically Section 4.3 on Slicing) establishes the foundational theorem for integral currents proving that the boundary of a generic slice is algebraically the slice of the boundary, which rigorously preserves relative topological degree.

- [Book] L. C. Evans, R. F. Gariepy / 1992 — Measure Theory and Fine Properties of Functions — CRC Press
  - **Gap Addressed:** Grader B - Slip 5 and Scaffolding Question 2 ("What hypotheses are needed to apply the coarea formula to a piecewise smooth map with corners?").
  - **Load-bearing piece:** Chapter 3 covers the Area and Coarea formulas, establishing the exact Rademacher regularity and Jacobian integration requirements to validly apply coarea integration to globally Lipschitz maps over domains with corners.

- [Book] J. Michael Steele / 1997 — Probability Theory and Combinatorial Optimization — SIAM
  - **Gap Addressed:** Grader A - Scaffolding Question 3 ("What rigorously named topological theorem dictates non-linear fractional scaling for transverse connecting walls?") and Grader B - Scaffolding Question 4.
  - **Load-bearing piece:** The chapter addressing the Beardwood-Halton-Hammersley theorem establishes the strict limits of Euclidean minimum spanning trees, explicitly confirming whether MST techniques can control 2-dimensional area or only 1-dimensional length for dense transverse point connections.

## SUPPORTING

- [Paper] Larry Guth / 2010 — Metaphors in systolic geometry — Proceedings of the ICM 2010
  - *Note:* Useful for framing the integration of topological constraints over coarea fibers via specific product-folding examples, informing Grader B's Scaffolding Question 5.

- [Paper] Mikhail Gromov / 2003 — Isoperimetry of waists and concentration of maps — Geometric and Functional Analysis (GAFA)
  - *Note:* Provides necessary background intuition on waist inequalities for lower-bounding the transverse multi-sheeted volume of generic mapping fibers.

## REDUNDANT

- [Lecture notes] Leon Simon / 1983 — Lectures on Geometric Measure Theory — Centre for Mathematical Analysis (ANU)
  - *Overlap:* Redundant with Federer's *Geometric Measure Theory*; both cover the machinery of slicing integral currents needed for the degree-one fiber maps.

- [Book] Mikhail Gromov / 1999 — Metric structures for Riemannian and non-Riemannian spaces — Birkhäuser
  - *Overlap:* Redundant with Federer regarding multilinear algebraic justifications for bounding pullbacks of coordinate area forms (Grader B - Scaffolding Question 3).

## PERIPHERAL

- [Paper] Larry Guth / 2011 — Volumes of balls in large Riemannian manifolds — Annals of Mathematics
  - *Note:* Explains the retired "1D tree counterexample" (IPT-61), which is not relevant to addressing the algebraic and measure-theoretic gaps in the current active integration proof.

- [Paper] Mikhail Gromov / 1999 — Metric inequalities with scalar curvature — Geometric and Functional Analysis (GAFA)
  - *Note:* Focuses on macroscopic area-contracting limits and scalar curvature rather than the highly specific fiber integration and Cartesian product constraints required here.

- [Book] V. Guillemin, A. Pollack / 1974 — Differential Topology — Prentice-Hall
  - *Note:* Restricted to smooth transversality methods which fundamentally fail on the piecewise smooth manifolds with corners specifically critiqued by Grader B. 

## UNFAMILIAR
*(None)*

## Narrower draw 2
## LOAD-BEARING

- [Monograph] Herbert Federer / 1969 — Geometric Measure Theory — Springer-Verlag — IDs: no ID — Establishes multilinear comass bounds (Step 2) and the rigorous slicing of integral currents required to preserve mapping degree on piecewise-smooth fibers (Step 1). — search: federer geometric measure theory slicing pdf
  - **Gap:** Grader B Critique 1 ("Fallacy: The sliced relative degree-one statement is not proved") & Grader B Scaffolding 1.
  - **Load-bearing piece:** Section 4.3 on the slicing of integral currents rigorously establishes the commutation formula $\partial \langle T, f, y \rangle = \langle \partial T, f, y \rangle$, which mathematically ensures that restricting the map to almost every fiber preserves the required degree-one boundary constraints.

- [Book] L. C. Evans, R. F. Gariepy / 1992 — Measure Theory and Fine Properties of Functions — CRC Press — IDs: no ID — Provides the precise regularity conditions and Jacobian integration bounds required to apply the Coarea formula to globally Lipschitz maps with corners (Step 1). — search: evans gariepy measure theory fine properties pdf
  - **Gap:** Grader B Critique 5 ("Slip: Lipschitz and coarea hypotheses for piecewise smooth maps with corners should be stated carefully") & Grader B Scaffolding 2.
  - **Load-bearing piece:** Chapter 3 details Rademacher's theorem and the Area/Coarea formulas for globally Lipschitz functions, explicitly providing the measure-theoretic hypotheses required to integrate over mappings with piecewise smooth corners.

- [Book] J. Michael Steele / 1997 — Probability Theory and Combinatorial Optimization — SIAM — IDs: no ID — Exposes the core mathematical fallacy in Step 3 by proving MST bounds control 1-dimensional length rather than 2-dimensional area, fatally undermining the fractional scaling. — search: steele probability theory combinatorial optimization pdf
  - **Gap:** Grader A Scaffolding 3 ("What rigorously named topological theorem dictates non-linear fractional scaling for transverse connecting walls?") & Grader B Critique 2.
  - **Load-bearing piece:** The chapter on Euclidean functionals and asymptotic bounds proves that Minimum Spanning Trees strictly govern 1-dimensional lengths (scaling as $\sim \sqrt{N}$ in 2D), directly contradicting the proof's attempt in Step 3 to use MSTs to bound 2-dimensional transverse area connectivity.

- [Book] Mikhail Gromov / 1999 — Metric structures for Riemannian and non-Riemannian spaces — Birkhäuser — IDs: no ID — Details the multilinear algebraic justification for bounding the pullback of differential area forms using uniform bounds on 2-dilation (Step 2). — search: gromov metric structures for riemannian pdf
  - **Gap:** Grader B Critique 6 ("Slip: The projection-area and comass inequalities need short justifications") & Grader B Scaffolding 3.
  - **Load-bearing piece:** The sections on mass/comass duality and systolic metric geometry outline the explicit multilinear algebraic facts needed to bound the exact wedge product norm (and pullbacks of coordinate area forms) under a uniform 2-dilation limit.

## SUPPORTING

- [Paper] Larry Guth / 2010 — Metaphors in systolic geometry — Proceedings of the ICM 2010 — IDs: no ID — Formalizes the explicit mechanics of topological product-folding maps and the correct integration of MST bounds with coarea formulas. — search: larry guth metaphors systolic geometry pdf
  - *Note:* Provides excellent background on how macroscopic folding maps behave topologically, giving necessary context for answering Grader B Scaffolding 4.

- [Paper] Mikhail Gromov / 2003 — Isoperimetry of waists and concentration of maps — Geometric and Functional Analysis (GAFA) — IDs: no ID — Introduces waist inequalities to rigorously lower-bound the multi-sheeted transverse volume of generic mapping fibers under dilation constraints. — search: gromov isoperimetry waists concentration maps pdf
  - *Note:* Provides the actual waist inequalities that might correctly bound multi-sheeted fiber volumes (unlike the fundamentally flawed MST approach in Step 3), addressing the overall intent of Grader B Critique 2.

## REDUNDANT

- [Lecture notes] Leon Simon / 1983 — Lectures on Geometric Measure Theory — Centre for Mathematical Analysis (ANU) — IDs: no ID — Canonical open-access substitute for Federer, explicitly proving that the boundary of a slice is algebraically the slice of the boundary. — search: leon simon lectures geometric measure theory pdf
  - *Overlap:* Redundant with Federer (1969). Both establish the exact same integral current slicing theorems required to close Grader B Critique 1.

## PERIPHERAL

- [Paper] Larry Guth / 2011 — Volumes of balls in large Riemannian manifolds — Annals of Mathematics — IDs: no ID — Underlying literature for the "1D tree counterexample" (IPT-61), showing how mapping to metric trees bypasses naive geometric projection constraints. — search: larry guth volumes balls large riemannian pdf
- [Paper] Mikhail Gromov / 1999 — Metric inequalities with scalar curvature — Geometric and Functional Analysis (GAFA) — IDs: no ID — Analyzes macroscopic dimension and area-contracting mappings, highlighting that bounded 2-dilation does not prevent 1-dimensional distances from shrinking arbitrarily. — search: gromov metric inequalities scalar curvature pdf
- [Book] V. Guillemin, A. Pollack / 1974 — Differential Topology — Prentice-Hall — IDs: no ID — Offers classical smooth transversality arguments for invariant mapping degrees, but relies on smooth strata and fails at the piecewise-smooth corners critiqued by Grader B. — search: michael hutchings differential topology notes pdf

## UNFAMILIAR
*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and open-access substitutes that trace the techniques attempted in the proof and directly address the gaps identified by the graders. 

### 1. Evans & Gariepy (Coarea Formula for Lipschitz Maps)
* **Authors / Year:** L. C. Evans, R. F. Gariepy / 1992
* **Title:** Measure Theory and Fine Properties of Functions
* **Type:** Book
* **Venue:** CRC Press
* **Main result or relevant chapter/section:** Chapter 3 develops the area and coarea formulas for Lipschitz functions between Euclidean spaces, establishing that fibers of such maps are almost-everywhere rectifiable sets with well-defined Hausdorff measures.
* **Topic needed for this proof:** The Coarea formula for globally Lipschitz maps (which includes piecewise smooth maps with corners).
* **Open-access substitute for that topic:** (open-access for topic: Coarea formula for Lipschitz maps) — L. Simon / 1983 / Lectures on Geometric Measure Theory / Centre for Mathematical Analysis (ANU)
* **Connection:** Directly addresses **Grader B's Question 2**. The proof's invocation of the coarea formula in Step 1 is valid because a piecewise smooth map defined on a rectangular domain with corners is globally Lipschitz, satisfying the foundational hypotheses outlined here.
* **Web search query:** `evans gariepy measure theory fine properties pdf`
* **Confidence (bibliographic):** HIGH

### 2. Federer (Slicing Integral Currents)
* **Authors / Year:** Herbert Federer / 1969
* **Title:** Geometric Measure Theory
* **Type:** Monograph
* **Venue:** Springer-Verlag
* **Main result or relevant chapter/section:** Section 4.3 (Slicing) rigorously defines the intersection and slice of an integral current by a Lipschitz map. Theorem 4.3.2 proves that the slice of an integral current is an integral current, and crucially, that the boundary of the slice is exactly the slice of the boundary.
* **Topic needed for this proof:** The slicing theorem for integral currents to preserve boundary conditions and relative mapping degrees on generic fibers.
* **Open-access substitute for that topic:** (open-access for topic: Slicing of integral currents) — L. Simon / 1983 / Lectures on Geometric Measure Theory / Centre for Mathematical Analysis (ANU)
* **Connection:** Answers **Grader B's Question 1** and addresses **Grader A's topological decoupling**. By treating the domain $R$ as an integral current, slicing guarantees that the generic rectifiable fiber $\Sigma_y$ has a rigorous boundary restricted strictly to the pulled-back boundary faces of $R$, legally preserving the relative cycle and the degree of the restriction $f_{34}$.
* **Web search query:** `federer geometric measure theory slicing pdf`
* **Confidence (bibliographic):** HIGH

### 3. Steele (Geometric Lower Bounds for Connecting Walls)
* **Authors / Year:** J. Michael Steele / 1997
* **Title:** Probability Theory and Combinatorial Optimization
* **Type:** Book
* **Venue:** SIAM
* **Main result or relevant chapter/section:** Chapter 2 develops the classic minimum spanning tree (MST) and traveling salesperson (TSP) geometric lower bounds, proving that constructing 1-dimensional connections between $N$ separated points within a bounded domain of area $A$ requires a total length bounded strictly below by $\Omega(\sqrt{N A})$.
* **Topic needed for this proof:** Geometric lower bounds for minimum connecting networks (TSP/MST) in planar rectangular cross-sections.
* **Open-access substitute for that topic:** (open-access for topic: Geometric lower bounds for connecting networks) — J. M. Steele / 1981 / Subadditive Euclidean Functionals and Nonlinear Growth in Geometric Probability / Annals of Probability
* **Connection:** Exposes the critical fallacy flagged by **Grader A (Fallacy 1)** and answers **Grader B's Question 4**. The physical 1D length of transverse connecting walls depends *only* on the cross-section domain it lives in ($R_1 \times R_2$) and the multiplicity $N$; it cannot depend on the target base space parameter $S_2$. Steele's bounds physically contradict the proof's fabricated assertion that the localized fiber area intrinsically scales with $S_2^{1/2}$.
* **Web search query:** `steele probability theory combinatorial optimization pdf`
* **Confidence (bibliographic):** HIGH

### 4. Guth (Topological Folding Bounds via Coarea)
* **Authors / Year:** Larry Guth / 2010
* **Title:** Metaphors in systolic geometry
* **Type:** Paper
* **Venue:** Proceedings of the International Congress of Mathematicians (ICM) 2010
* **Main result or relevant chapter/section:** Sections 3 and 4 formalize the geometry of "topological folding." Guth demonstrates that maps reducing distances must heavily fold fibers, bounding the unavoidable transverse area of these high-multiplicity fibers using coarea formulas chained with geometric graph connections (MST bounds).
* **Topic needed for this proof:** Integrating coarea slicing with geometric connecting bounds to measure the minimal transverse area generated by topological folding.
* **Open-access substitute for that topic:** (open-access for topic: Topological folding and area lower bounds via coarea) — L. Guth / 2010 / Metaphors in systolic geometry / arxiv preprint
* **Connection:** Provides the correct, rigorous mathematical framework that Step 3 of the proof attempts to mimic. It details how actual topological folding bounds are derived from connecting graphs and correctly integrated over base spaces to force macroscopic volumetric lower bounds, avoiding the algebraic fabrications the grader flagged.
* **Web search query:** `guth metaphors in systolic geometry pdf`
* **Confidence (bibliographic):** HIGH

### 5. Gromov (Multilinear Area Bounds for Bounded Dilation)
* **Authors / Year:** Mikhail Gromov / 1999
* **Title:** Metric structures for Riemannian and non-Riemannian spaces
* **Type:** Book
* **Venue:** Birkhäuser
* **Main result or relevant chapter/section:** Chapter 4 explores maps bounded by $k$-dilation (and volume-expanding maps), utilizing multi-linear algebra (comass bounds) and coarea inequalities to tightly bound the geometry of fibers and the integrability of pulled-back forms.
* **Topic needed for this proof:** Bounding the pullback of differential area forms using uniform bounds on 2-dilation (comass of the differential).
* **Open-access substitute for that topic:** (open-access for topic: Comass norms and multilinear algebra in geometric measure theory) — F. Morgan / 1988 / Geometric Measure Theory: A Beginner's Guide (Chapter 1) 
* **Connection:** Answers **Grader B's Question 3** and **Grader A's Slip 2**. It provides the standard multilinear algebraic justification for why the hypothesis $\Dil_2(f) \le 1$ translates mathematically to bounding the pullback of the $dx_3 \wedge dx_4$ area form, controlling the projection-area arrays without requiring global pointwise orthogonality.
* **Web search query:** `gromov metric structures for riemannian pdf`
* **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and topic-keyed substitutes that address the specific geometric measure theory frameworks and topological scaling arguments attempted in this proof. 

**1. Leon Simon / 1983**
- **Title:** Lectures on Geometric Measure Theory
- **Type:** lecture notes
- **Venue:** Proceedings of the Centre for Mathematical Analysis, Australian National University
- **Main result or relevant chapter/section:** Chapter 7 (specifically Section 28 on "Slicing") proves the slicing theorem for integral currents, strictly establishing that the boundary of a slice is the slice of the boundary ($\partial \langle T, f, y \rangle = (-1)^k \langle \partial T, f, y \rangle$). 
- **Topic needed for this proof:** The precise conditions under which slicing an integral current by a Lipschitz map produces a generic relative cycle whose topological boundary behaves algebraically.
- **Open-access substitute for that topic:** (open-access for topic: integral current slicing and relative cycles) — Simon / 1983 / Lectures on Geometric Measure Theory / ANU CMA (the original book is fully open access on the university's archive).
- **Connection:** Directly answers **Grader B’s Scaffolding Q1**. The proof's Step 1 asserts that the slice $\Sigma_y$ has boundary strictly contained in specific faces of $\partial R$, thus inducing a degree-1 restriction. Simon’s slicing formulas are the required foundational machinery to rigorously justify this topological transfer.
- **Web search query:** `leon simon lectures geometric measure theory pdf`
- **Confidence (bibliographic):** HIGH

**2. Herbert Federer / 1969**
- **Title:** Geometric Measure Theory
- **Type:** book
- **Venue:** Springer-Verlag
- **Main result or relevant chapter/section:** Section 1.8 develops the multilinear algebra of comass, multivectors, and calibrations. 
- **Topic needed for this proof:** The rigorous relationship between the pointwise norm of a 2-vector (or 2-form) and the sum of its scalar orthogonal area projections ($\sum |dx_i \wedge dx_j|$).
- **Open-access substitute for that topic:** (open-access for topic: linear algebra of comass and calibrated geometries) — F. R. Harvey, H. B. Lawson / 1982 / Calibrated Geometries / Acta Mathematica.
- **Connection:** Addresses **Grader A’s Slip (and Q2)**, as well as **Grader B’s Q3**. The proof claims in Step 2 that bounding the comass of $df_1 \wedge df_2$ allows one to directly bound the sum of the scalar area projections $A_{ij}(y)$. Federer shows that bounding the comass controls the wedge product, but equating the wedge norm to the sum of scalar area projections requires the tangent plane of the fiber to be globally orthogonal to the coordinate axes—a condition the proof assumes without justification.
- **Web search query:** `harvey lawson calibrated geometries acta pdf`
- **Confidence (bibliographic):** HIGH

**3. Lawrence C. Evans, Ronald F. Gariepy / 1992**
- **Title:** Measure Theory and Fine Properties of Functions
- **Type:** book
- **Venue:** CRC Press
- **Main result or relevant chapter/section:** Chapter 3 ("Area and Coarea Formulas") provides the definitive rigorous proofs of the Coarea formula for Lipschitz functions.
- **Topic needed for this proof:** The exact regularity constraints and Jacobian integration bounds required to apply the Coarea formula to piecewise smooth maps with corners.
- **Open-access substitute for that topic:** (open-access for topic: coarea formula for Lipschitz continuous maps) — Nicola Fusco / 2000 / The Coarea Formula / Course notes or modern survey.
- **Connection:** Addresses **Grader B’s Scaffolding Q2**. The proof loosely invokes Coarea for maps with corners in Step 1. Evans & Gariepy details how Rademacher's theorem and the definition of the generalized Jacobian must be carefully handled on the singular strata (corners) where the classical derivative fails. Furthermore, it clarifies **Grader A's Q1** by showing the Coarea integrand depends strictly on the local Jacobian over the domain $R$, meaning the base integration parameters ($S_1, S_2$) cannot algebraically back-propagate into the intrinsic area of a single localized fiber.
- **Web search query:** `evans gariepy measure theory fine properties pdf`
- **Confidence (bibliographic):** HIGH

**4. Larry Guth / 2011**
- **Title:** Volumes of balls in large Riemannian manifolds
- **Type:** paper
- **Venue:** Annals of Mathematics, Vol. 173
- **Main result or relevant chapter/section:** Employs sweeping mapping bounds, "pancaking" arguments, and explicit constructions of mappings to metric trees to show how preserving lower-dimensional topology forces multi-sheet folding and mass concentration.
- **Topic needed for this proof:** Using 1-dimensional metric tree constructions to bound mapping volumes and generate counterexamples to macroscopic capacity bounds.
- **Open-access substitute for that topic:** (open-access for topic: macroscopic volume bounds and mappings to metric trees) — Guth / 2006 / Volumes of balls in large Riemannian manifolds / arxiv.
- **Connection:** This is the underlying literature for the "1D tree counterexample" previously discovered in the investigator's notebook (IPT-61). Guth’s framework formalizes why mapping a domain to a heavily compressed target using 1D metric trees allows one to bypass naive volume projection constraints. 
- **Web search query:** `larry guth volumes balls large riemannian pdf`
- **Confidence (bibliographic):** HIGH

**5. Mikhail Gromov / 2003**
- **Title:** Isoperimetry of waists and concentration of maps
- **Type:** paper
- **Venue:** Geometric and Functional Analysis (GAFA), Vol. 13
- **Main result or relevant chapter/section:** Establishes "waist inequalities," which strictly bound the volume of generic fibers (waists) for continuous maps from higher-dimensional spaces to lower-dimensional spaces.
- **Topic needed for this proof:** Quantitative lower bounds on the generalized transverse volume of generic mapping fibers under dilation constraints.
- **Open-access substitute for that topic:** (open-access for topic: waist inequalities and fiber volume lower bounds) — Gromov / 2003 / Isoperimetry of waists and concentration of maps / IHES website or arxiv.
- **Connection:** Addresses **Grader B’s Scaffolding Q4 and Q5**. The proof's Step 3 realizes that the fibers must "fold" massively to cover the target space while fitting inside $R$, and attempts to ad-hoc a localized geometric deficit. Gromov's waist inequality is the exact formal mathematical framework designed to bound the area of these multi-sheeted connecting walls without relying on fabricated fractional exponents.
- **Web search query:** `gromov isoperimetry waists concentration maps pdf`
- **Confidence (bibliographic):** HIGH

**6. J. Michael Steele / 1997**
- **Title:** Probability Theory and Combinatorial Optimization
- **Type:** monograph
- **Venue:** SIAM
- **Main result or relevant chapter/section:** Chapter 2 covers the Beardwood–Halton–Hammersley theorem and asymptotic bounds for the Euclidean Minimum Spanning Tree (MST) and Traveling Salesman Problem (TSP).
- **Topic needed for this proof:** The geometric scaling limit proving that the length of a minimum spanning tree connecting $N$ generic points in a planar rectangle of area $A$ is proportional to $\sqrt{N \cdot A}$.
- **Connection:** In Step 3, the proof invokes a "minimum spanning tree (TSP) bound" to connect the folded transverse walls, claiming this yields a fractional scaling exponent. Steele provides the exact bounding theorem the solver is blindly referring to. Crucially, applying this MST bound directly exposes the fallacy identified by **Grader A**: the MST bounds *1-dimensional length* ($\sim \sqrt{N}$), not *2-dimensional area*. When integrating this 1D length over a 2D base ($S_1 \times S_2$), it yields a 3-volume scaling, not a 4-volume scaling, completely breaking the proof's dimensional homogeneity.
- **Web search query:** `steele probability theory combinatorial optimization pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the foundational works and monographs that address the gaps in the proof, specifically targeting the functional machinery of the Coarea formula, intersection theory on sliced fibers, and the geometric measure theory (GMT) limits of bounding lower-dimensional connectivity under area-contraction ($\Dil_2$) constraints.

**Federer, H. / 1969**
*   **Title:** Geometric Measure Theory
*   **Type:** monograph
*   **Venue:** Springer-Verlag (Grundlehren der mathematischen Wissenschaften)
*   **Main result or relevant chapter/section:** Chapter 1 (Section 1.8) details the multilinear algebra of comass and bounding wedge products. Chapter 4 rigorously develops the slicing of integral currents by Lipschitz maps, proving that slicing commutes with the boundary operator ($\partial\langle T, f, y\rangle = \langle \partial T, f, y\rangle$).
*   **Topic needed for this proof:** The preservation of topological boundary conditions and relative degree when slicing integral currents.
*   **Open-access substitute for that topic:** (open-access for topic: lectures on geometric measure theory and slicing of integral currents) — Simon, L. / 1983 / Lectures on Geometric Measure Theory / Centre for Mathematical Analysis, Australian National University
*   **Connection:** Directly addresses Grader B's Scaffolding Questions 1 and 3, and the critique that the "sliced relative degree-one statement is not proved." Federer provides the rigorous GMT framework to show that generic rectifiable slices inherit the boundary restriction and mapping degree of the bulk manifold.
*   **Web search query:** `leon simon lectures geometric measure theory pdf`
*   **Confidence (bibliographic):** HIGH

**Evans, L. C., Gariepy, R. F. / 1992**
*   **Title:** Measure Theory and Fine Properties of Functions
*   **Type:** book
*   **Venue:** CRC Press
*   **Main result or relevant chapter/section:** Chapter 3 provides the definitive, accessible proof of the Coarea formula for general locally Lipschitz maps between Euclidean spaces.
*   **Topic needed for this proof:** The hypotheses and precise statement for applying the Coarea formula to piecewise smooth maps on domains with corners (which are locally Lipschitz).
*   **Open-access substitute for that topic:** (open-access for topic: coarea formula for Lipschitz functions) — Hajłasz, P. / Sobolev Spaces / lecture notes (often hosted on author's university webpage)
*   **Connection:** Addresses Grader B's Slip 5 and Scaffolding Question 2. A piecewise smooth map on a rectangle is uniformly Lipschitz, satisfying the exact hypotheses required to integrate fiberward areas against the 4-volume via the Coarea formula.
*   **Web search query:** `evans gariepy measure theory fine properties pdf`
*   **Confidence (bibliographic):** HIGH

**Gromov, M. / 1999**
*   **Title:** Metric inequalities with scalar curvature
*   **Type:** paper
*   **Venue:** Geometric and Functional Analysis (GAFA), Vol. 9
*   **Main result or relevant chapter/section:** Introduces "macroscopic dimension" and systematically explores mapping degrees and volumetric limits under area-contracting ($\Dil_2 \le 1$) constraints. 
*   **Topic needed for this proof:** The geometric limits of area-contracting map constraints, specifically that $\Dil_2 \le 1$ does *not* imply a bound on 1-dimensional distances ($\Dil_1$).
*   **Open-access substitute for that topic:** (open-access for topic: macroscopic dimension and area-contracting maps) — Guth, L. / 2011 / Volumes of balls in large Riemannian manifolds / Annals of Mathematics (preprint version)
*   **Connection:** This exposes the core mathematical fallacy noted by Grader A and B regarding the transverse wall length gap. Because $\Dil_2(f) \le 1$ does not prevent 1-dimensional curves from shrinking arbitrarily, the points/sheets of the generic fiber can cluster arbitrarily close in the transverse domain, yielding no uniform lower bound for transverse connecting area.
*   **Web search query:** `gromov metric inequalities scalar curvature pdf`
*   **Confidence (bibliographic):** HIGH

**Guillemin, V., Pollack, A. / 1974**
*   **Title:** Differential Topology
*   **Type:** book
*   **Venue:** Prentice-Hall
*   **Main result or relevant chapter/section:** Chapter 2 (Intersection Theory) and Chapter 3 (Orientations), particularly the sections proving that the topological degree of a map is invariant and can be computed via transversality on generic preimage slices.
*   **Topic needed for this proof:** The smooth transversality argument for slicing mapping degrees.
*   **Open-access substitute for that topic:** (open-access for topic: intersection theory and degree of smooth maps) — Hutchings, M. / Introduction to Differential Topology / UC Berkeley course notes
*   **Connection:** Offers a classical differential topology alternative to GMT (Federer) for answering Grader B's Scaffolding Question 1. If $f$ is smoothed, generic slices are transverse manifolds that strictly inherit the degree mapping behavior.
*   **Web search query:** `michael hutchings differential topology notes pdf`
*   **Confidence (bibliographic):** HIGH

**Guth, L. / 2010**
*   **Title:** Metaphors in systolic geometry
*   **Type:** survey
*   **Venue:** Proceedings of the International Congress of Mathematicians (ICM) 2010
*   **Main result or relevant chapter/section:** Section on "Product folding maps" demonstrates explicit constructions mapping topological products to lower-dimensional spines while preserving specific degree and geometric bounds.
*   **Topic needed for this proof:** The explicit construction of product-folding maps to test volumetric capacity bounds.
*   **Connection:** Addresses Grader A's critique that the $S_2^{1/2}S_3^{3/2}$ scaling relies on an "unconstructed existential claim." The Falsifier log explicitly invokes Guth's product-folding maps; this paper outlines the mechanics of those maps, proving whether the topological multiplicity genuinely forces transverse geometric scaling or can be trivially collapsed.
*   **Web search query:** `larry guth metaphors systolic geometry pdf`
*   **Confidence (bibliographic):** HIGH

**Steele, J. M. / 1997**
*   **Title:** Probability Theory and Combinatorial Optimization
*   **Type:** monograph
*   **Venue:** SIAM
*   **Main result or relevant chapter/section:** Chapter 3 covers Euclidean Traveling Salesman bounds, showing that connecting $N$ optimally dispersed points in an area $A$ requires a spanning network of length $O(\sqrt{N \cdot A})$.
*   **Topic needed for this proof:** Bounds on the length of connecting networks (minimum spanning trees) for $N$ points in a planar rectangle.
*   **Connection:** Directly answers Grader B's Scaffolding Question 4 ("What quantitative lower bound on transverse area follows when many sheets..."). It clarifies that the $\sqrt{N}$ length bound is a *worst-case maximum* (or average uniform case), but without a metric lower bound (which $\Dil_2$ fails to provide), points can clump arbitrarily close, meaning the *minimum* spanning network has no uniform lower bound, severely challenging Step 3's logical gap.
*   **Web search query:** `steele probability theory combinatorial optimization pdf`
*   **Confidence (bibliographic):** HIGH
