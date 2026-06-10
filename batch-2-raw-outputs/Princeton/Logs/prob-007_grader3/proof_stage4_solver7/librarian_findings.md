# Librarian Findings — grader3_9455b6227fa7_proof_stage4_solver7_20260531_030711
**Generated:** 2026-05-31T03:09:33  
**Inputs:** notebook=11360 chars, proof=10052 chars, gap_report=2633 chars  
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
- [monograph] Farb, B. and Margalit, D. / 2011 — A Primer on Mapping Class Groups — Princeton University Press — IDs: no ID — Establishes the Bigon Criterion to formally exclude higher-dimensional non-minimal cells. — search: `farb margalit primer mapping class groups pdf`
- [monograph] Lando, S. K. and Zvonkin, A. K. / 2004 — Graphs on Surfaces and Their Applications — Springer — IDs: no ID — Provides ribbon graph machinery to rigorously prove cap isolation via Eulerian boundary walks. — search: `lando zvonkin graphs on surfaces pdf`
- [book] Chmutov, S., Duzhin, S. and Mostovoy, J. / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — IDs: no ID — Canonically classifies 6-point chord diagrams by crossing counts, fulfilling the exhaustive enumeration requirement. — search: `chmutov duzhin mostovoy vassiliev pdf`

## RELATED
- [book] Hatcher, A. / 2002 — Algebraic Topology — Cambridge University Press — IDs: no ID — Details the finiteness and dimensionality prerequisites required before invoking the Euler-Poincaré formula. — search: `hatcher algebraic topology pdf`
- [book] Diestel, R. / 2017 — Graph Theory — Springer — IDs: no ID — Supplies the planar graph degree-sum and Euler's formula equations to algebraically link leaves and crossings. — search: `diestel graph theory pdf`

## SOMEWHAT RELATED
*(None)*

## NOT MUCH
*(None)*

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [monograph] Farb, B. and Margalit, D. / 2011 — A Primer on Mapping Class Groups — Princeton University Press — IDs: no ID — Establishes the Bigon Criterion to formally exclude higher-dimensional non-minimal cells. — search: `farb margalit primer mapping class groups pdf`
  - **Gap addressed:** Grader B critique — 4. Fallacy: Exclude all higher-dimensional cells, including repeated crossings; and Scaffolding Question 4.
  - **Load-bearing piece:** Section 1.2 ("The Bigon Criterion") proves that any two transversally intersecting arcs not in minimal position must bound an embedded bigon disk, rigorously forbidding repeated crossings in minimal configurations.

- [monograph] Lando, S. K. and Zvonkin, A. K. / 2004 — Graphs on Surfaces and Their Applications — Springer — IDs: no ID — Provides ribbon graph machinery to rigorously prove cap isolation via Eulerian boundary walks. — search: `lando zvonkin graphs on surfaces pdf`
  - **Gap addressed:** Grader B critique — 1. Fallacy: Prove the perimeter-tour lemma for immersed forests with boundary leaves; and Scaffolding Question 1.
  - **Load-bearing piece:** Chapter 1 formalizes the topological boundaries of combinatorial maps and ribbon graphs, proving that the single face of an embedded planar tree corresponds strictly to an Eulerian boundary walk that visits its leaves in cyclic order.

- [book] Chmutov, S., Duzhin, S. and Mostovoy, J. / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — IDs: no ID — Canonically classifies 6-point chord diagrams by crossing counts, fulfilling the exhaustive enumeration requirement. — search: `chmutov duzhin mostovoy vassiliev pdf`
  - **Gap addressed:** Grader B critique — 3. Fallacy: Give an exhaustive enumeration of valid core cells and isotopy classes; and Scaffolding Question 3.
  - **Load-bearing piece:** Chapter 4 systematically introduces chord diagrams and their intersection graphs, directly providing the structural exhaustion of the 15 possible matchings on six boundary points ordered by crossing number.

- [book] Hatcher, A. / 2002 — Algebraic Topology — Cambridge University Press — IDs: no ID — Details the finiteness and dimensionality prerequisites required before invoking the Euler-Poincaré formula. — search: `hatcher algebraic topology pdf`
  - **Gap addressed:** Grader B critique — 8. Slip: State finiteness and two-dimensionality before invoking Euler-Poincaré; and Scaffolding Question 5.
  - **Load-bearing piece:** Theorem 2.44 explicitly details the prerequisites (a finite, finite-dimensional CW complex) required to equate the alternating sum of cell counts to the alternating sum of Betti numbers.

## SUPPORTING

- [book] Diestel, R. / 2017 — Graph Theory — Springer — IDs: no ID — Supplies the planar graph degree-sum and Euler's formula equations to algebraically link leaves and crossings. — search: `diestel graph theory pdf`
  - **Note:** Useful background for addressing Grader B's Scaffolding Question 2 (relating degree-4 internal vertices to component/leaf counts) via standard graph handshaking lemmas, though less directly focused on topological embeddings than Lando/Zvonkin. 

## REDUNDANT
*(None)*

## PERIPHERAL
*(None)*

## UNFAMILIAR
*(None)*

---

# Stage 3 — Chapter Picker

## A Primer on Mapping Class Groups (Farb, B. and Margalit, D., Princeton University Press, 2011)
_(Establishes the Bigon Criterion to formally exclude higher-dimensional non-minimal cells. — search: `farb margalit primer mapping class groups pdf`)_

Here are the specific sections from Farb and Margalit's *A Primer on Mapping Class Groups* that directly address the grader's flagged gaps regarding higher-dimensional cells and arc intersections:

- **Chapter 1, Section 1.2 (approx.) — Intersection Numbers and the Bigon Criterion**
  - **Which gap it addresses:** Fallacy 4 (Exclude all higher-dimensional cells, including repeated crossings), Scaffolding Question 4 (Why does a pair of arcs crossing twice create a closed bigon?), and the open combinatorial exhaustion in OC-5.
  - **Why:** This section establishes the Bigon Criterion (Theorem 1.7 for closed curves, with the direct analogue for proper arcs). It formally proves that two transverse arcs intersect minimally in their isotopy class if and only if they do not bound a topological bigon. This is the exact mathematical hammer needed to prove that any repeated crossing between two intervals structurally guarantees an internal bigon, causing an empty real-axis boundary ($\partial A = \emptyset$) and completely ruling out configurations with $\ge 3$ crossings.

- **Chapter 1, Section 1.1 (approx.) — Surfaces and Euler Characteristic** 
  - **Which gap it addresses:** Fallacy 8 (State finiteness and two-dimensionality before invoking Euler-Poincaré) and Scaffolding Question 5.
  - **Why:** While a standard algebraic topology theorem, Farb and Margalit cover the Euler-Poincaré relation and surface classifications as prerequisites. Citing this explicitly addresses the grader's requirement to formally state the finite two-dimensional bounds of the CW complex before algebraic extraction of the Betti numbers. 

*(Note: The other gaps involving the planar forest perimeter tours and specific $K_{2,3}$ bipartite graph embeddings are graph-theoretic and planar combinatorial properties, which are better closed by citing a standard graph theory text rather than Farb and Margalit.)*

## Graphs on Surfaces and Their Applications (Lando, S. K. and Zvonkin, A. K., Springer, 2004)
_(Provides ribbon graph machinery to rigorously prove cap isolation via Eulerian boundary walks. — search: `lando zvonkin graphs on surfaces pdf`)_

Here are the specific chapters and sections from Lando and Zvonkin (2004) that will provide the exact combinatorial machinery needed to formalize the geometric claims and close the graders' gaps:

- **Chapter 1, Section 1.2–1.3 (approx.) Maps and Ribbon Graphs**
  - **Which gap it addresses:** Grader B1 (Perimeter-tour lemma for immersed forests) and Grader B2 (Cap isolation justification).
  - **Why:** This section establishes the rigorous equivalence between topological maps on surfaces and ribbon graphs (fatgraphs). By modeling the internal crossings as 4-valent vertices of a ribbon graph, the "complement-boundary arcs" in your CW complex become precisely the boundary components (faces) of the ribbon graph. The standard theorem here proves that the boundary walk of a ribbon graph natively forms an Eulerian circuit, eliminating the need for "informal cyclic-order language."

- **Chapter 2, Section 2.1 (approx.) Plane Trees and their Contours**
  - **Which gap it addresses:** Grader A (Explicitly mapping $M_1$ and $M_2$) and Grader B5 (Derive the validity of each 2-cell from complement regions).
  - **Why:** This chapter details the combinatorics of the "contour walk" of plane trees. Applying the formal contour walk algorithm allows you to algebraically output the exact cyclic permutation of leaves for the 2-cells $M_1$ and $M_2$ without relying on ambiguous geometric tracing, immediately satisfying Grader A's request to close the "geometric loophole." 

- **Chapter 6 (approx.) Chord Diagrams and Intersection Graphs**
  - **Which gap it addresses:** Grader B3 (Exhaustive enumeration of valid core cells) and Grader B4 (Exclude repeated crossings / bigons).
  - **Why:** The matchings with endpoints on the real line perfectly map to the book’s machinery on chord diagrams (often covered in the context of Vassiliev invariants). You can use this to rigorously prove that any pair of chords intersecting more than once (a bigon) inherently creates a face in the ribbon graph that does not contain any boundary vertices, systematically ruling out all non-minimal isotopy classes without hand-waving "central internal regions."

## Introduction to Vassiliev Knot Invariants (Chmutov, S., Duzhin, S. and Mostovoy, J., Cambridge University Press, 2012)
_(Canonically classifies 6-point chord diagrams by crossing counts, fulfilling the exhaustive enumeration requirement. — search: `chmutov duzhin mostovoy vassiliev pdf`)_

Here are the specific chapters and sections from Chmutov, Duzhin, and Mostovoy’s *Introduction to Vassiliev Knot Invariants* that will formally close the graders' gaps regarding the 6-point cell enumeration and boundary traces. 

By mapping your "valid $k$-crossing matchings" directly to **degree-3 chord diagrams** and their associated ribbon graphs, you can bypass the need to geometrically trace bigons entirely.

*   **Chapter 3, "Chord Diagrams" (Section 3.1: Basic definitions and examples)**
    *   **Which gap it addresses:** Gap 3 (Exhaustive enumeration of valid core cells) and Scaffolding Question 3 (Classifying pairings of 6 ordered boundary points).
    *   **Why:** This section provides the exhaustive classification of chord diagrams. For degree 3 (6 points), there are exactly $5!! = 15$ distinct pairings with fixed boundary order. The text natively partitions these by intersection count: exactly $C_3 = 5$ non-crossing (Catalan) diagrams, 6 with one crossing, 3 with two crossings, and 1 with three crossings, rigorously vindicating your cell counts ($c_0=5, c_1=6, c_2=3, c_3=1$) without requiring manual topological deduction. 

*   **Chapter 3, "Chord Diagrams" (Section: Intersection graphs)** *(approx.)*
    *   **Which gap it addresses:** Gap 4 (Excluding higher-dimensional cells) and Scaffolding Question 4 (Closed bigons).
    *   **Why:** This defines the intersection graph (circle graph) of a chord diagram, where vertices are chords and edges are crossings. By mapping to standard chord diagrams (where chords are straight segments spanning a disk), it mathematically precludes two chords from crossing more than once. Any configuration where continuous arcs cross twice inherently forms a closed bigon disjoint from the boundary circle, making them trivial isotopy extensions of minimal-crossing chords. 

*   **Chapter 3, "Chord Diagrams" (Section: Chord diagrams and ribbon graphs)** *(approx.)*
    *   **Which gap it addresses:** Grader A's critique (Explicit boundary traces) and Scaffolding Question 1 (Immersed planar forests and complement boundaries).
    *   **Why:** This section outlines the canonical construction that maps any chord diagram to a one-vertex ribbon graph (or thickened surface). The "Euler perimeter tour" the solvers are clumsily trying to execute on planar forests is exactly equivalent to tracing the boundary components of the corresponding ribbon graph. Invoking this maps your boundary-pairing claims directly to established 1-manifold boundary traces, perfectly satisfying Grader A's request for explicit mapping.

## Algebraic Topology (Hatcher, A., Cambridge University Press, 2002)
_(Details the finiteness and dimensionality prerequisites required before invoking the Euler-Poincaré formula. — search: `hatcher algebraic topology pdf`)_

- **Chapter 2, Section 2.2: Computations and Applications**
- **Which gap it addresses:** Slip 8 and Scaffolding Question 5 (Finiteness, two-dimensionality, and Betti number constraints before invoking Euler-Poincaré).
- **Why:** Theorem 2.44 definitively establishes $\chi(X) = \sum (-1)^n c_n = \sum (-1)^n b_n$. It structurally mandates the topological prerequisite of a finite CW complex to well-define homology ranks before computing the Euler characteristic, directly yielding $b_2 \ge 1$ from the sequence $2 = 1 - b_1 + b_2$.

- **Chapter 0: Some Underlying Geometric Notions**
- **Which gap it addresses:** Standard CW complex definitions and preliminary attachment setup.
- **Why:** Initial logic and parameters are validated. Standard cell attachment and characteristic map processing applies globally to the 1-skeleton baseline.

- **I do not believe this reference actually addresses the remaining named gaps.**
- **Which gap it addresses:** Fallacies 1-5, Scaffolding Questions 1-4, Grader A critique (Planar forest perimeters, chord enumerations, bigon isolation).
- **Why:** Hatcher exclusively targets algebraic topology and cellular homology; it contains no combinatorial theory regarding non-crossing planar matchings, immersion parity tracing, or chord diagrams required to close the geometric bounding rules of this specific subcomplex.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [monograph] Farb, B. and Margalit, D. / 2011 — A Primer on Mapping Class Groups — Princeton University Press — IDs: no ID — Establishes the Bigon Criterion to formally exclude higher-dimensional non-minimal cells. — search: `farb margalit primer mapping class groups pdf`
  - **Addresses:** Grader B Critique 4 ("Exclude all higher-dimensional cells") and Grader B Scaffolding 4 ("Why does a pair of arcs crossing twice create a closed bigon?").
  - **The load-bearing piece:** Section 1.2 ("The Bigon Criterion") rigorously proves that any collection of arcs on a surface intersecting non-minimally must enclose a topological bigon, securing the exclusion of higher-crossing cells.

- [monograph] Lando, S. K. and Zvonkin, A. K. / 2004 — Graphs on Surfaces and Their Applications — Springer — IDs: no ID — Provides ribbon graph machinery to rigorously prove cap isolation via Eulerian boundary walks. — search: `lando zvonkin graphs on surfaces pdf`
  - **Addresses:** Grader B Critique 1 ("Prove the perimeter-tour lemma for immersed forests with boundary leaves"), Grader B Critique 2 ("Justify cap isolation using that lemma"), and Grader B Scaffolding 1.
  - **The load-bearing piece:** Chapter 1 systematically develops ribbon graphs (fatgraphs) and proves that the boundaries of faces for an immersed tree strictly trace an Eulerian boundary walk of its leaves, supplying the formal theorem to replace the proof's informal "cyclic-order language."

- [book] Chmutov, S., Duzhin, S. and Mostovoy, J. / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — IDs: no ID — Canonically classifies 6-point chord diagrams by crossing counts, fulfilling the exhaustive enumeration requirement. — search: `chmutov duzhin mostovoy vassiliev pdf`
  - **Addresses:** Grader B Critique 3 ("Give an exhaustive enumeration of valid core cells and isotopy classes") and Grader B Scaffolding 3 ("How can all pairings of six ordered boundary points be classified by crossing number?").
  - **The load-bearing piece:** Chapter 4 exhaustively classifies all order-3 (6-point) chord diagrams via their intersection graphs and explicitly enumerates them by crossing counts, closing the combinatorial completeness gap.

- [book] Hatcher, A. / 2002 — Algebraic Topology — Cambridge University Press — IDs: no ID — Details the finiteness and dimensionality prerequisites required before invoking the Euler-Poincaré formula. — search: `hatcher algebraic topology pdf`
  - **Addresses:** Grader B Critique 8 ("State finiteness and two-dimensionality before invoking Euler-Poincaré"), Grader B Scaffolding 5, and the canonical citation for SNT-1.
  - **The load-bearing piece:** Section 2.2 (Theorem 2.44) explicitly bounds cellular homology for finite, finite-dimensional CW complexes and formally dictates how Euler characteristic constraints non-negative Betti numbers.

## SUPPORTING

- [book] Diestel, R. / 2017 — Graph Theory — Springer — IDs: no ID — Supplies the planar graph degree-sum and Euler's formula equations to algebraically link leaves and crossings. — search: `diestel graph theory pdf`
  - *Note:* Directly answers Grader B Scaffolding 2 by providing the standard handshaking lemma ($\sum \deg(v) = 2|E|$) linking degree-1 boundary leaves to internal degree-4 crossings.

## REDUNDANT
*(None)*

## PERIPHERAL
*(None)*

## UNFAMILIAR
*(None)*

## Narrower draw 2
## LOAD-BEARING

- [monograph] Farb, B. and Margalit, D. / 2011 — A Primer on Mapping Class Groups — Princeton University Press — IDs: no ID — Establishes the Bigon Criterion to formally exclude higher-dimensional non-minimal cells. — search: `farb margalit primer mapping class groups pdf`
  * **Gap addressed:** Grader B, Fallacy 4 ("Exclude all higher-dimensional cells, including repeated crossings") and Scaffolding Question 4 ("Why does a pair of arcs crossing twice create a closed bigon?").
  * **Justification:** Chapter 1 introduces the "Bigon Criterion," which mathematically proves that any two curves (arcs) intersecting non-minimally in their isotopy class must bound an internal bigon disc.

- [monograph] Lando, S. K. and Zvonkin, A. K. / 2004 — Graphs on Surfaces and Their Applications — Springer — IDs: no ID — Provides ribbon graph machinery to rigorously prove cap isolation via Eulerian boundary walks. — search: `lando zvonkin graphs on surfaces pdf`
  * **Gap addressed:** Grader B, Fallacy 1 ("Prove the perimeter-tour lemma for immersed forests with boundary leaves") and Fallacy 2 ("Justify cap isolation using that lemma").
  * **Justification:** Chapter 1 formalizes "ribbon graphs" (fatgraphs) and proves how the Eulerian walks around their perimeters inherently dictate the disjoint boundary faces/complement regions of the immersed network.

- [book] Chmutov, S., Duzhin, S. and Mostovoy, J. / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — IDs: no ID — Canonically classifies 6-point chord diagrams by crossing counts, fulfilling the exhaustive enumeration requirement. — search: `chmutov duzhin mostovoy vassiliev pdf`
  * **Gap addressed:** Grader B, Fallacy 3 ("Give an exhaustive enumeration of valid core cells and isotopy classes") and Scaffolding Question 3 ("How can all pairings of six ordered boundary points be classified by crossing number?").
  * **Justification:** Chapter 4 covers "Chord Diagrams" and their intersection graphs, offering the exact algebraic and combinatorial machinery to canonically exhaust all matchings of points on a circle/boundary by crossing number.

- [book] Hatcher, A. / 2002 — Algebraic Topology — Cambridge University Press — IDs: no ID — Details the finiteness and dimensionality prerequisites required before invoking the Euler-Poincaré formula. — search: `hatcher algebraic topology pdf`
  * **Gap addressed:** Grader B, Slip 8 ("State finiteness and two-dimensionality before invoking Euler-Poincaré") and Scaffolding Question 5.
  * **Justification:** Chapter 2 ("Homology") explicitly provides the standard proof of the Euler-Poincaré formula (Theorem 2.44) directly detailing the structural requirements for finite CW complexes.

## SUPPORTING

- [book] Diestel, R. / 2017 — Graph Theory — Springer — IDs: no ID — Supplies the planar graph degree-sum and Euler's formula equations to algebraically link leaves and crossings. — search: `diestel graph theory pdf`
  * **Note:** Useful for providing the fundamental graph invariants needed for Grader B, Scaffolding Question 2, but secondary to the primary topological machinery needed to validate the region boundaries.

## REDUNDANT

*(None)*

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and topic-keyed open-access substitutes that address the specific topological and combinatorial gaps flagged by the graders. 

To lock down this proof, the candidate must discard the informal "Euler perimeter tour" language and replace it with formal ribbon graph (fatgraph) boundary walk lemmas, explicitly invoke the Bigon Criterion for mapping class groups to exclude higher cells, and properly frame the domain as the combinatorics of chord diagrams.

### 1. Finiteness and the Euler-Poincaré Formula (Gap B.8)
The grader correctly points out that invoking $\chi(X) = \sum (-1)^k b_k$ without establishing finiteness is a structural gap. Hatcher’s text is the canonical citation for this.

* **Authors / Year:** Allen Hatcher / 2002
* **Title:** Algebraic Topology
* **Type:** book
* **Venue:** Cambridge University Press
* **Main result or relevant chapter/section:** Chapter 2 (Homology), Section 2.2 (Cellular Homology). Theorem 2.44 rigorously proves that for a *finite* CW complex, the Euler characteristic (alternating sum of cells) is equal to the alternating sum of the Betti numbers.
* **Topic needed for this proof:** The Euler-Poincaré formula specifically for finite CW complexes.
* **Open-access substitute for that topic:** (open-access for topic: Euler characteristic and Betti numbers) — Hatcher / 2002 / Algebraic Topology / canonical author-hosted PDF at Cornell.
* **Connection:** Directly addresses Gap B.8. The solver must establish that the alternating core configuration space yields a finite number of valid cells before calculating $\chi = 5 - 6 + 3$ and deducting $b_2 \geq 1$.
* **Web search query:** `hatcher algebraic topology pdf`
* **Confidence (bibliographic):** HIGH

### 2. Double Crossings and the Bigon Criterion (Gap B.4 & Scaffolding Q4)
To formally exclude $\geq$ 3-cells, the solver cannot just say "repeated crossings yield empty boundaries." They need the standard geometric lemma proving that non-minimal topological intersections strictly bound 2-cells (bigons). 

* **Authors / Year:** Benson Farb, Dan Margalit / 2012
* **Title:** A Primer on Mapping Class Groups
* **Type:** monograph
* **Venue:** Princeton University Press (Princeton Mathematical Series)
* **Main result or relevant chapter/section:** Chapter 1 (Surfaces and simple closed curves), Section 1.2. specifically details "The Bigon Criterion" (Proposition 1.7), which proves that if two transverse arcs intersect non-minimally, their union strictly contains an embedded bigon (a topological disk bounded by exactly one arc segment from each curve).
* **Topic needed for this proof:** The bigon criterion for non-minimally intersecting transverse arcs.
* **Open-access substitute for that topic:** (open-access for topic: The Bigon Criterion) — Farb, Margalit / 2011 / A Primer on Mapping Class Groups (preprint draft) / authors' personal webpages.
* **Connection:** Directly addresses Gap B.4 (Why does a pair of arcs crossing twice create a closed bigon?). Applying the bigon criterion proves that if two intervals cross more than once, they form an internal trapped region whose real-axis boundary is strictly empty, strictly violating the $\partial A$ conditions of the complex and systematically ruling out higher-dimensional non-minimal matchings.
* **Web search query:** `farb margalit primer mapping class groups pdf`
* **Confidence (bibliographic):** HIGH

### 3. Region Boundaries and Ribbon Graph Euler Tours (Gap B.1 & B.2)
The candidate uses an informal "Euler perimeter tour of a tree" to prove cap isolation. This must be formalized using ribbon graphs (fatgraphs), where the "leaves on a boundary" dictate a strict cyclic structure on the boundary components.

* **Authors / Year:** Sergei K. Lando, Alexander K. Zvonkin / 2004
* **Title:** Graphs on Surfaces and Their Applications
* **Type:** monograph
* **Venue:** Springer (Encyclopaedia of Mathematical Sciences)
* **Main result or relevant chapter/section:** Chapter 1 (Graphs on Surfaces) and Chapter 2 (Combinatorics of Trees). Rigorously defines ribbon graphs (fatgraphs), how degree conditions dictate the cyclic order of half-edges, and proves that a planar embedded tree natively possesses a single boundary face (boundary walk) that strictly tours the leaves in cyclic order.
* **Topic needed for this proof:** Face boundary walks of planar ribbon graphs.
* **Open-access substitute for that topic:** (open-access for topic: Ribbon graphs and boundary walks) — Standard lecture notes on fatgraphs or the authors' pre-publication draft (often excerpted openly). 
* **Connection:** Addresses Gaps B.1 and B.2 by providing the established mathematical machinery to replace the candidate's informal logic. An immersed planar forest with leaves on the real line is a ribbon graph; its complement regions correspond exactly to the ribbon graph's boundary walks.
* **Web search query:** `lando zvonkin graphs on surfaces pdf`
* **Confidence (bibliographic):** HIGH

### 4. Combinatorial Enumeration of Matchings (Gap B.3 & Scaffolding Q3)
To exhaustively list the cells of the 6-point alternating core, the candidate should map it to the standard theory of chord diagrams (which natively classify planar matchings and crossings).

* **Authors / Year:** S. Chmutov, S. Duzhin, J. Mostovoy / 2012
* **Title:** Introduction to Vassiliev Knot Invariants
* **Type:** book
* **Venue:** Cambridge University Press
* **Main result or relevant chapter/section:** Chapter 4 (Chord Diagrams). Rigorously defines chord diagrams (matchings on $N$ points), intersection graphs, and their crossing numbers.
* **Topic needed for this proof:** Combinatorial enumeration and intersection properties of chord diagrams.
* **Open-access substitute for that topic:** (open-access for topic: Combinatorics of chord diagrams) — Chmutov, Duzhin, Mostovoy / 2011 / Introduction to Vassiliev Knot Invariants / arxiv preprint (the canonical draft is universally available on ArXiv).
* **Connection:** Addresses Gap B.3 and Scaffolding Q3. A 6-point matching on a boundary line is identically a chord diagram of degree 3. The combinatorics of such diagrams (exactly 15 total perfect matchings: 5 non-crossing, 6 with one crossing, 3 with two, 1 with three) is standard literature. Citing this bypasses the need for the candidate to prove the configuration bounds from scratch.
* **Web search query:** `chmutov duzhin mostovoy vassiliev knot invariants pdf`
* **Confidence (bibliographic):** HIGH

### 5. Planar Face Limits for 4-Valent Graphs (Scaffolding Q2 & Gap A)
To rigorously map the $M_1, M_2, M_3$ cells without hand-waving "geometric loops" (Grader A's critique), the relation between the crossings and regions needs standard planar graph theory.

* **Authors / Year:** Reinhard Diestel / 2017
* **Title:** Graph Theory
* **Type:** book
* **Venue:** Springer (Graduate Texts in Mathematics)
* **Main result or relevant chapter/section:** Chapter 4 (Planar Graphs). Establishes Euler's formula for the plane ($V - E + F = C + 1$) and maps the exact relation between a graph's connected components, bounded faces, and vertex degrees. 
* **Topic needed for this proof:** Euler's formula and face boundary mapping for planar multigraphs.
* **Open-access substitute for that topic:** (open-access for topic: Euler's formula for planar graphs) — Diestel / Graph Theory / Electronic edition universally hosted on the author's webpage.
* **Connection:** Addresses Scaffolding Q2. By treating the arc-intervals as edges and the crossings strictly as degree-4 vertices, Euler's formula algebraically forces the exact number of complement regions, structurally guaranteeing the 2-cell maps without relying exclusively on topological tracing.
* **Web search query:** `diestel graph theory pdf`
* **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and topic-keyed substitutes that directly address the graders' critiques, focusing on the topology of immersed curves, planar forests (ribbon graphs), and the Euler-Poincaré prerequisites. 

- **Authors / Year** — Farb, B., & Margalit, D. / 2011
- **Title** — A Primer on Mapping Class Groups
- **Type** — book
- **Venue** — Princeton University Press
- **Main result or relevant chapter/section** — Section 1.2 ("Intersection Numbers") formalizes the **Bigon Criterion** (Proposition 1.7), which proves that if two transverse immersed curves (or arcs with endpoints on a boundary) intersect more times than their minimal geometric intersection number, they must form a bigon (an embedded disk bounded by one subarc from each). 
- **Topic needed for this proof** — The bigon criterion for immersed curves to rigorously prove that non-minimal repeated crossings inevitably form an internal closed loop bounding a disk.
- **Open-access substitute for that topic** — (open-access for topic: Bigon criterion for arcs on surfaces) — Farb, B., & Margalit, D. / 2011 / A Primer on Mapping Class Groups / Authors' webpage draft (margalit/primer)
- **Connection** — Directly answers Grader B's Point 4 ("Why does a pair of arcs crossing twice create a closed bigon?") and provides the strict topological machinery to formally exclude higher-dimensional cells ($c_{\ge 3}$) that arise from redundant arc crossings.
- **Web search query** — `primer mapping class groups margalit pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Lando, S. K., & Zvonkin, A. K. / 2004
- **Title** — Graphs on Surfaces and Their Applications
- **Type** — book
- **Venue** — Springer (Encyclopaedia of Mathematical Sciences)
- **Main result or relevant chapter/section** — Chapter 1 introduces ribbon graphs (fatgraphs) and proves that the boundary components of a regular neighborhood of a cellularly embedded graph perfectly correspond to Eulerian boundary walks around its spanning trees and edges.
- **Topic needed for this proof** — Formal topological equivalence between the complement-region boundaries of an immersed planar forest and the Eulerian boundary walks (perimeter tours) of that forest.
- **Open-access substitute for that topic** — (open-access for topic: Eulerian boundary walks on ribbon graphs and planar trees) — Zvonkin, A. K. / 1997 / Matrix Integrals and Map Enumeration: An Accessible Introduction / Math. Comput. Modelling
- **Connection** — Closes Grader B's Points 1 and 2 by providing the canonical lemma for the "perimeter-tour" algorithm, replacing the proof's informal language about cyclic leaf orders with rigorous ribbon graph boundary walks. It also gives the exact formal algorithm needed to satisfy Grader A's request to explicitly trace $M_1$ and $M_2$.
- **Web search query** — `matrix integrals map enumeration zvonkin pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Chmutov, S., Duzhin, S., & Mostovoy, J. / 2012
- **Title** — Introduction to Vassiliev Knot Invariants
- **Type** — book
- **Venue** — Cambridge University Press
- **Main result or relevant chapter/section** — Chapter 4 is a comprehensive treatment of chord diagrams (1-manifolds with boundary on a line/circle). It details their intersection graphs, explicitly classifying chord pairings by crossing number and proving structural constraints on their complement regions.
- **Topic needed for this proof** — Combinatorial classification of chord diagrams by crossing number and intersection graph structure.
- **Open-access substitute for that topic** — (open-access for topic: Combinatorial classification of chord diagram crossings) — Chmutov, Duzhin, Mostovoy / 2012 / Introduction to Vassiliev Knot Invariants / Author's webpage draft (math.ohio-state.edu/~chmutov)
- **Connection** — Answers Grader B's Point 3 ("exhaustive enumeration of valid core cells"). Instead of manually deducing $\binom{6}{4}$ subsets, you can cite standard chord-diagram combinatorics (the Touchard-Riordan distribution for $n=3$ chords) to canonically state the known unconstrained counts for 6 points are exactly 5 (0-crossings), 6 (1-crossing), 3 (2-crossings), and 1 (3-crossings), before applying the problem's boundary constraints to cull the 3-crossing case.
- **Web search query** — `introduction to vassiliev knot invariants chmutov pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Hatcher, A. / 2002
- **Title** — Algebraic Topology
- **Type** — book
- **Venue** — Cambridge University Press
- **Main result or relevant chapter/section** — Chapter 2 (Homology), Theorem 2.44 explicitly proves the Euler-Poincaré formula $\chi(X) = \sum (-1)^n c_n = \sum (-1)^n b_n$. The theorem text and accompanying remarks strictly delineate that this equation is only valid if the CW complex is finite-dimensional and has finitely many cells.
- **Topic needed for this proof** — The specific finiteness and dimensionality prerequisites required to invoke the Euler-Poincaré theorem for a CW complex.
- **Open-access substitute for that topic** — (open-access for topic: Euler-Poincare formula prerequisites for CW complexes) — Hatcher, A. / 2002 / Algebraic Topology / Cornell University author webpage
- **Connection** — Addresses Grader B's Point 8 ("State finiteness and two-dimensionality before invoking Euler-Poincaré"). The proof currently calculates $\chi=2$ and immediately asserts $b_2 \ge 1$; referencing Hatcher allows you to insert the required structural sentence explicitly verifying that the exhausted cell list implies a finite, 2-dimensional CW complex.
- **Web search query** — `algebraic topology hatcher pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed open-access substitutes that directly address the structural gaps and scaffolding questions identified by the graders. 

**1. Lando, S. K. and Zvonkin, A. K. / 2004**
- **Title:** Graphs on Surfaces and Their Applications
- **Type:** Book
- **Venue:** Springer
- **Main result or relevant chapter:** Chapter 1 introduces the theory of ribbon graphs (fatgraphs) and rigorously proves that the topological boundary of a regular planar neighborhood of a tree traces an Eulerian contour walk (or perimeter tour), cyclically visiting the tree's leaves.
- **Topic needed for this proof:** The topological boundary of a thickened planar forest strictly forms a cyclic Euler contour walk that pairs its boundary leaves.
- **Open-access substitute for that topic:** (open-access for topic: Ribbon graph boundaries and contour walks of trees) — Chmutov, S., Duzhin, S., and Mostovoy, J. / 2012 / Introduction to Vassiliev Knot Invariants / author's webpage draft
- **Connection:** Directly answers Grader B's Scaffolding Question 1 ("For an immersed planar forest... how do complement-boundary arcs pair the leaves?"). This provides the canonical mechanism to prove the "perimeter-tour lemma" mathematically rather than relying on informal cyclic-order language, strictly verifying the cap isolation step.
- **Web search query:** `lando zvonkin graphs on surfaces pdf`
- **Confidence (bibliographic):** HIGH

**2. Farb, B. and Margalit, D. / 2011**
- **Title:** A Primer on Mapping Class Groups
- **Type:** Book
- **Venue:** Princeton University Press
- **Main result or relevant chapter:** Chapter 1 establishes the Bigon Criterion, proving that a pair of transverse simple arcs on a surface is in minimal position (has minimal crossings) if and only if they do not bound an embedded closed bigon (a 2-gon).
- **Topic needed for this proof:** The Bigon Criterion for transverse curves on surfaces to rule out non-minimal isotopy classes.
- **Open-access substitute for that topic:** (open-access for topic: Bigon criterion for curves on surfaces) — Farb, B. and Margalit, D. / 2011 / A Primer on Mapping Class Groups / author's webpage draft
- **Connection:** Answers Grader B's Scaffolding Question 4 ("Why does a pair of arcs crossing twice create a closed bigon?"). The proof currently asserts that higher-dimensional cells ($c_{\ge 3}$) vanish without proving why multiple crossings between the same intervals are forbidden. The Bigon Criterion mathematically secures this exclusion.
- **Web search query:** `farb margalit primer mapping class groups pdf`
- **Confidence (bibliographic):** HIGH

**3. Chmutov, S., Duzhin, S., and Mostovoy, J. / 2012**
- **Title:** Introduction to Vassiliev Knot Invariants
- **Type:** Book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter:** Chapter 4 formally maps points on a line to chord diagrams, rigorously classifying pairings of ordered points by their number of transversal internal crossings (intersection graphs).
- **Topic needed for this proof:** Formal combinatorial enumeration and crossing-classification of chord diagrams.
- **Open-access substitute for that topic:** (open-access for topic: Enumeration and intersection graphs of chord diagrams) — Chmutov, S., Duzhin, S., and Mostovoy, J. / 2012 / Introduction to Vassiliev Knot Invariants / author's webpage draft
- **Connection:** Answers Grader A's critique of the "geometric loophole" and Grader B's Scaffolding Question 3. Instead of waving off the verification of $M_1$ and $M_2$ with "the exact same tree Euler tour algorithm," the intersection graph framework of chord diagrams canonically maps out all 15 matchings on 6 points and strictly partitions them by crossing count. 
- **Web search query:** `chmutov duzhin mostovoy vassiliev pdf`
- **Confidence (bibliographic):** HIGH

**4. Diestel, R. / 2016 (approx.)**
- **Title:** Graph Theory
- **Type:** Book
- **Venue:** Springer
- **Main result or relevant chapter:** Chapters 1 and 4 combine the degree-sum formula (Handshaking Lemma) with Euler's formula for planar graphs ($V - E + F = 1 + C$) to algebraically relate vertices, edges, and structural components.
- **Topic needed for this proof:** Euler's formula and vertex-degree sum constraints applied to immersed planar graphs.
- **Open-access substitute for that topic:** (open-access for topic: Planar graph degree sums and Euler's formula) — Diestel, R. / Graph Theory / author's free electronic edition
- **Connection:** Answers Grader B's Scaffolding Question 2. The author asserts that internal crossings act strictly as degree-4 vertices and logically links this to leaf count, but fails to write the graph equations explicitly. Using $\sum \deg(v) = 2E$ where $V = V_{\text{leaves}} + V_{\text{crossings}}$ formalizes the exact relation between leaves, crossings, edges, and components.
- **Web search query:** `diestel graph theory pdf`
- **Confidence (bibliographic):** HIGH

**5. Hatcher, A. / 2002**
- **Title:** Algebraic Topology
- **Type:** Book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter:** Chapter 2 (Section 2.2, Theorem 2.44) proves the Euler-Poincaré formula, establishing that the Euler characteristic derived from finite cell counts ($\chi = \sum (-1)^k c_k$) is identically equal to the alternating sum of the Betti numbers ($\chi = \sum (-1)^k b_k$). 
- **Topic needed for this proof:** The algebraic bounding of Betti numbers from the Euler-Poincaré formula for finite, connected CW complexes.
- **Open-access substitute for that topic:** (open-access for topic: Euler-Poincare formula and Betti numbers) — Hatcher, A. / 2002 / Algebraic Topology / author's webpage draft
- **Connection:** Resolves Grader B's Scaffolding Question 5 and verifies "SNT-1". It supplies the necessary formal backing for the final topological deduction ($b_2 \ge 1$), correctly validating that $\chi=2$ over a connected 1-skeleton algebraically requires non-trivial second homology.
- **Web search query:** `hatcher algebraic topology pdf`
- **Confidence (bibliographic):** HIGH
