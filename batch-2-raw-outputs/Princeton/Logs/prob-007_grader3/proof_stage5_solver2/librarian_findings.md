# Librarian Findings — grader3_9455b6227fa7_proof_stage5_solver2_20260531_030711
**Generated:** 2026-05-31T03:09:51  
**Inputs:** notebook=11360 chars, proof=13338 chars, gap_report=2313 chars  
**Date restriction:** none (FP v2 — recent works allowed)  

---

## Citation IDs (aggregator-only)
```json
{
  "arxiv": [
    "math/9811028"
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
    "1103.5628",
    "math/9811028"
  ],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

---

# Stage 1 — Gauntlet (aggregator output)

## VERY RELATED
- [book] Benson Farb, Dan Margalit / 2011 — A Primer on Mapping Class Groups — Princeton University Press — no ID — Establishes the Bigon Criterion to formally rule out multiple crossings between any two intervals in minimal configurations, addressing Fallacy 1 and Scaffolding Q1. — search: `farb margalit primer mapping class groups pdf`
- [book] Sergei K. Lando, Alexander K. Zvonkin / 2004 — Graphs on Surfaces and Their Applications — Springer — no ID — Provides algebraic permutation machinery for ribbon graphs to strictly compute region boundaries without geometric pictures, fixing Slip 5 and Scaffolding Q3. — search: `lando zvonkin graphs on surfaces pdf`
- [book] S. Chmutov, S. Duzhin, J. Mostovoy / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — no ID — Formalizes Gauss diagrams and combinatorial exhaustion of chord diagrams to rule out higher-crossing matchings, answering Fallacies 3 and 4. — search: `chmutov duzhin mostovoy vassiliev pdf`
- [book] Allen Hatcher / 2002 — Algebraic Topology — Cambridge University Press — no ID — Canonical source for the Euler-Poincaré formula (SNT-1) and clarifies the Hurewicz/homology requirements to distinguish homology spheres from actual spheres, addressing Slip 6. — search: `hatcher algebraic topology pdf`
- [paper] Louis H. Kauffman / 1999 — Virtual Knot Theory — European Journal of Combinatorics — arxiv:math/9811028 — Introduces Gauss diagrams to rigorously encode immersed arc crossings and explicitly tracks topological connectivity under smoothings. — search: `kauffman virtual knot theory arxiv pdf`

## RELATED
- [monograph] Louis H. Kauffman / 1987 — On Knots — Princeton University Press — no ID — Details explicit state models and bracket smoothings to mathematically determine arc connectivity upon crossing resolution, addressing Fallacy 2. — search: `kauffman on knots pdf`
- [book] W. B. R. Lickorish / 1997 — An Introduction to Knot Theory — Springer — no ID — Formalizes how topological crossings recombine into disjoint arcs via state smoothings, providing rigorous mechanics for the "unique caps" argument. — search: `lickorish introduction to knot theory pdf`

## SOMEWHAT RELATED
- [paper] D. B. A. Epstein / 1966 — Curves on 2-manifolds and isotopies — Acta Mathematica — no ID — Proves curves can be ambiently isotoped to realize their minimal intersection number, justifying the proof's combinatorial treatment of isotopy classes. — search: `epstein curves on 2-manifolds isotopies pdf`
- [book] V. O. Manturov / 2004 — Knot Theory — CRC Press — no ID — Extensively covers admissibility conditions for Gauss words, providing alternative algebraic machinery to encode planar immersions. — search: `manturov knot theory pdf`

## NOT MUCH
- *(None)*

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [book] Benson Farb, Dan Margalit / 2011 — A Primer on Mapping Class Groups — Princeton University Press — no ID
  - **Addresses:** Fallacy 1, Scaffolding Q1
  - **Load-bearing piece:** Section 1.2 establishes the "Bigon Criterion," formally proving that multiple crossings between two isotopic curves in a minimal configuration must strictly be ruled out.

- [book] S. Chmutov, S. Duzhin, J. Mostovoy / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — no ID
  - **Addresses:** Fallacy 3, Fallacy 4, Scaffolding Q2
  - **Load-bearing piece:** Chapter 4 covers the combinatorial machinery of Gauss diagrams and chord intersection graphs, providing the exact tools needed to exhaust higher-crossing possibilities and encode immersed matching data rigorously.

- [book] Sergei K. Lando, Alexander K. Zvonkin / 2004 — Graphs on Surfaces and Their Applications — Springer — no ID
  - **Addresses:** Slip 5, Scaffolding Q3
  - **Load-bearing piece:** Chapter 1 introduces the algebraic representation of ribbon graphs (fatgraphs) via rotation systems, allowing the exact combinatorial computation of complement region boundary endpoints strictly through permutations instead of geometric pictures.

- [book] Allen Hatcher / 2002 — Algebraic Topology — Cambridge University Press — no ID
  - **Addresses:** Slip 6, Scaffolding Q4
  - **Load-bearing piece:** Section 2.2 details Cellular Homology and the Euler-Poincaré formula, explicitly demonstrating why nontrivial homology (computed via cell counts) does not automatically justify claiming a space is a 2-sphere ($S^2$) without deeper homotopy-theoretic proof (e.g., the Hurewicz theorem).

## SUPPORTING

- [monograph] Louis H. Kauffman / 1987 — On Knots — Princeton University Press — no ID
  - Provides essential background on bracket polynomial state models, which perfectly details how local crossing smoothings recombine endpoints (addressing Fallacy 2 and Scaffolding Q5).
- [paper] D. B. A. Epstein / 1966 — Curves on 2-manifolds and isotopies — Acta Mathematica — no ID
  - Foundational paper useful for verifying that curves can always be ambiently isotoped to realize their minimal geometric intersection number.

## REDUNDANT

- [paper] Louis H. Kauffman / 1999 — Virtual Knot Theory — European Journal of Combinatorics
  - Redundant to Chmutov et al. for Gauss diagram combinatorics and to Kauffman (1987) for local smoothing mechanics.
- [book] W. B. R. Lickorish / 1997 — An Introduction to Knot Theory — Springer — no ID
  - Redundant to Kauffman (1987); covers the exact same state sum crossing-resolution mechanics.
- [book] V. O. Manturov / 2004 — Knot Theory — CRC Press — no ID
  - Redundant to Chmutov et al. for admissibility conditions regarding Gauss words and chord diagram intersections.

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

---

# Stage 3 — Chapter Picker

## A Primer on Mapping Class Groups (Benson Farb, Dan Margalit, Princeton University Press, 2011)
_(no ID)_

Here are the specific sections from Farb and Margalit's *A Primer on Mapping Class Groups* that contain the exact standard machinery needed to close the gaps regarding curve intersections, bigons, and crossing resolutions.

- **Chapter 1, Section 1.2 (approx.): Surfaces and Curves (The Bigon Criterion)**
  - **Which gap it addresses:** Gap 1, Gap 3, and Scaffolding Question 1.
  - **Why:** This section formally establishes the Bigon Criterion, which states that two properly embedded arcs (or simple closed curves) intersect minimally if and only if they do not form any bigons (lenses). Citing this immediately justifies the proof's claim that two valid intervals in minimal isotopy position cannot cross more than once, firmly ruling out closed loops and higher non-minimal isotopy pairings.

- **Chapter 1, Section 1.2.4 (approx.): Surfaces and Curves (Smoothing Intersections)**
  - **Which gap it addresses:** Gap 2 and Scaffolding Question 5.
  - **Why:** This section introduces the topological operation of "smoothing" a crossing between two transversely intersecting arcs. It rigorously details how resolving a crossing recombines the endpoints of the resulting arcs, which provides the precise geometric mapping needed to justify the "unique caps" attaching maps and combinatorial boundary tracking.

- **Chapter 8 (approx.): The Complex of Curves (and the Arc Complex)**
  - **Which gap it addresses:** Gap 3 and Gap 5.
  - **Why:** The problem's CW complex $F_w$ is functionally a relative Arc Complex of a disk with marked boundary points. This chapter provides the formal combinatorial framework for defining simplices and complexes based on isotopy classes of disjoint arcs, demonstrating exactly how to prove completeness of an enumeration and systematic encoding of boundary endpoints without relying on hand-drawn pictures. 

*(Note: Farb & Margalit assumes standard algebraic topology background and does not directly teach how to deduce homology bounds strictly from Euler characteristics, so you will need a standard algebraic topology reference like Hatcher to address Gap 6 and Scaffolding Question 4.)*

## Introduction to Vassiliev Knot Invariants (S. Chmutov, S. Duzhin, J. Mostovoy, Cambridge University Press, 2012)
_(no ID)_

Here are the chapters and sections from the requested reference that address the grader’s identified gaps:

- **Chapter 1 / Section on Gauss Diagrams (approx.)**
  - **Which gap it addresses:** Gap 2 (encoding immersed matchings) and Scaffolding Q1 (ruling out lenses).
  - **Why:** Gauss diagrams provide a purely combinatorial way to encode immersed curves by tracking the preimages of crossings, their signs, and their cyclic order along the arcs. This explicit encoding turns geometric assertions about "closed lenses" (bigons) into rigorous algebraic checks, usually eliminated via combinatorial Reidemeister II moves.

- **Chapter 3: Chord Diagrams**
  - **Which gap it addresses:** Gap 3 (treating isotopy classes as ordinary chord pairings without proving completeness) and Gap 4 (bounding $c_{\ge 3}=0$).
  - **Why:** This chapter rigorously formalizes intervals paired on a 1-manifold (chords on a circle or line) and introduces intersection graphs. It provides the exact combinatorial limits on how multiple chords can mutually intersect, which is necessary to exhaustively classify isotopy classes of higher-crossing matchings.

- **Section on Ribbon Graphs / Fatgraphs (approx. Chapter 7 or 8)**
  - **Which gap it addresses:** Gap 5 (the need for systematic combinatorial verification of region boundaries) and Scaffolding Q3.
  - **Why:** By treating the immersed matching as a ribbon graph, the boundaries of the complement regions map exactly to the boundary cycles of the ribbon graph. This allows the boundary components to be computed purely algebraically using the standard permutation involution of half-edges (e.g., $\sigma \alpha$ cycles), entirely removing the reliance on topological pictures.

- **Chapter 2: Vassiliev Invariants / Vassiliev's Original Approach**
  - **Which gap it addresses:** Gap 2 regarding the "unique caps" smoothing fallacy, and Scaffolding Q5 (how local smoothing affects arcs).
  - **Why:** This chapter details Vassiliev’s original construction of the discriminant space of singular knots (curves with self-intersections). It explicitly models the topological cell complex where facets correspond to resolving (smoothing) crossings, providing the formal boundary maps needed to justify how smoothing a $k$-crossing state dictates the endpoints of the resulting descendant arcs.

## Graphs on Surfaces and Their Applications (Sergei K. Lando, Alexander K. Zvonkin, Springer, 2004)
_(no ID)_

Here are the specific chapters and sections from Lando and Zvonkin's *Graphs on Surfaces and Their Applications* that provide the strict combinatorial machinery needed to close the grader's identified gaps:

- **Chapter 1: Combinatorial Maps / Ribbon Graphs (approx.)**
  - **Which gap it addresses:** Slip 5 (Region-boundary checks need systematic combinatorial verification) and Scaffolding Q3.
  - **Why:** This chapter introduces the algebraic representation of graphs on surfaces using sets of half-edges (darts) and permutations (the rotation system and edge involution). It teaches how to compute the boundary components (faces) of complementary regions purely algebraically by finding the cycle decomposition of the face permutation, entirely replacing the problem's flawed visual "topological traces" with rigorous combinatorial proof.

- **Chapter 6: Chord Diagrams (approx.)**
  - **Which gap it addresses:** Fallacy 3 & 4 (Enumerating isotopy classes as ordinary chord pairings, and ruling out higher crossings), and Scaffolding Q2.
  - **Why:** This chapter rigorously covers the mathematics of chords with endpoints on a circle, Gauss words, and intersection graphs. It provides the formal encoding needed to prove that minimal generic matchings of arcs in a disk are in 1-to-1 bijection with standard chord diagrams (where chords are straight and intersect at most once), definitively ruling out non-minimal topological noise like "bigons" (lens-shaped regions) and combinatorially exhausting all valid crossing classes. 

- **Chapter 6, Section on Gauss diagrams / curves in the plane (approx.)**
  - **Which gap it addresses:** Fallacy 1 (Proving valid intervals cross at most once) and Scaffolding Q1.
  - **Why:** Discusses the mapping of immersed curves to Gauss diagrams. A strict minimal position condition or Reidemeister-type move analysis on planar curves is required to prove that two arcs with fixed endpoints on the boundary cannot cross twice without creating a topologically removable bigon that bounds a disk, enforcing the "cross at most once" property algebraically.

## Algebraic Topology (Allen Hatcher, Cambridge University Press, 2002)
_(no ID)_

Here are the specific sections of Hatcher’s *Algebraic Topology* that address the structural topological gaps, along with a note on the limitations of this specific reference for the combinatorial gaps.

**Chapter 2, Section 2.2: Computations and Applications (specifically the "Cellular Homology" subsection)**
*   **Which gap it addresses:** Gap 6 (Slip: Justifying nontrivial homology) and Scaffolding Question 4 (Euler-characteristic cell counts).
*   **Why:** The proof unlawfully concludes $b_2 \ge 1$ purely from the Euler-Poincaré formula $2 = 1 - b_1 + b_2$. This section details Cellular Homology, showing that to actually establish the Betti numbers (and rule out combinations like $b_1=5, b_2=6$), one cannot just count cells; one must explicitly compute the degrees of the cellular boundary maps $d_n : C_n(X) \to C_{n-1}(X)$ built from the attaching maps of the complex.

**Chapter 4, Section 4.1: Homotopy Groups and Section 4.2: Elementary Methods of Calculation**
*   **Which gap it addresses:** Gap 6 (Slip: The statement that the space is $S^2$ is not justified).
*   **Why:** Even if the homology was rigorously proven to be trivial in dimension 1 and $\mathbb{Z}$ in dimension 2, homology alone does not guarantee the space is $S^2$. You would need to reference the Hurewicz Theorem (4.2) and Whitehead’s Theorem (4.1) to show that if the space is simply connected ($\pi_1(X) = 0$) and has the homology of a 2-sphere, it is weakly homotopy equivalent to $S^2$.

**I do not believe this reference actually addresses any of the remaining named gaps (Gaps 1–5).**
*   **Why:** Gaps 1 through 5, as well as Scaffolding Questions 1, 2, 3, and 5, require arguments involving the combinatorics of chord diagrams, the bigon criterion for immersed 1-manifolds, and local topological smoothing/resolution (e.g., Kauffman bracket-style curve resolutions). Hatcher’s text is a foundational treatise on algebraic topology (homology, cohomology, homotopy) and does not cover the geometric topology of intersecting curves on disks or purely combinatorial matching enumeration.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [book] Benson Farb, Dan Margalit / 2011 — A Primer on Mapping Class Groups — Princeton University Press — no ID — Establishes the Bigon Criterion to formally rule out multiple crossings between any two intervals in minimal configurations, addressing Fallacy 1 and Scaffolding Q1. — search: `farb margalit primer mapping class groups pdf`
  - **Addresses:** Fallacy 1 (and Scaffolding Q1)
  - **Load-bearing piece:** Section 1.2 ("The Bigon Criterion") formally proves that curves/arcs on a surface that intersect minimally cannot bound any closed bigons (lenses), directly forcing arcs to cross at most once.

- [book] Sergei K. Lando, Alexander K. Zvonkin / 2004 — Graphs on Surfaces and Their Applications — Springer — no ID — Provides algebraic permutation machinery for ribbon graphs to strictly compute region boundaries without geometric pictures, fixing Slip 5 and Scaffolding Q3. — search: `lando zvonkin graphs on surfaces pdf`
  - **Addresses:** Slip 5 (and Scaffolding Q3)
  - **Load-bearing piece:** Chapter 1 introduces the classic algebraic permutation machinery (rotation systems) where the cycles of the permutation product $\sigma \alpha$ rigorously and strictly compute the boundaries of faces/complement regions without relying on visual geometric drawings.

- [book] S. Chmutov, S. Duzhin, J. Mostovoy / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — no ID — Formalizes Gauss diagrams and combinatorial exhaustion of chord diagrams to rule out higher-crossing matchings, answering Fallacies 3 and 4. — search: `chmutov duzhin mostovoy vassiliev pdf`
  - **Addresses:** Fallacy 3, Fallacy 4 (and Scaffolding Q2)
  - **Load-bearing piece:** Chapter 4 perfectly formalizes chord diagrams and intersection graphs, providing the exact combinatorial framework required to exhaustively encode crossing sequences along an arc and rule out unlisted higher-crossing matchings.

- [book] Allen Hatcher / 2002 — Algebraic Topology — Cambridge University Press — no ID — Canonical source for the Euler-Poincaré formula (SNT-1) and clarifies the Hurewicz/homology requirements to distinguish homology spheres from actual spheres, addressing Slip 6. — search: `hatcher algebraic topology pdf`
  - **Addresses:** Slip 6 (and Scaffolding Q4)
  - **Load-bearing piece:** While Chapter 2 provides the cellular homology and Euler-characteristic foundations, Chapter 4 provides the Hurewicz and Whitehead theorems which clarify exactly why calculating Betti numbers via Euler characteristics is insufficient on its own to assert a space is homeomorphic to $S^2$ (as simple connectivity must also be proven).

## SUPPORTING

- [monograph] Louis H. Kauffman / 1987 — On Knots — Princeton University Press — no ID — Details explicit state models and bracket smoothings to mathematically determine arc connectivity upon crossing resolution, addressing Fallacy 2. — search: `kauffman on knots pdf`
  - *Note:* Provides standard, crucial background on bracket state smoothings (A- and B-smoothings) to track precisely how local resolutions recombine interval endpoints, which helps fix Fallacy 2 and Scaffolding Q5.

## REDUNDANT

- [book] W. B. R. Lickorish / 1997 — An Introduction to Knot Theory — Springer — no ID — Formalizes how topological crossings recombine into disjoint arcs via state smoothings, providing rigorous mechanics for the "unique caps" argument. — search: `lickorish introduction to knot theory pdf`
  - *Overlap:* Overlaps directly with Kauffman's "On Knots" regarding state smoothings and arc re-connectivity.
- [paper] D. B. A. Epstein / 1966 — Curves on 2-manifolds and isotopies — Acta Mathematica — no ID — Proves curves can be ambiently isotoped to realize their minimal intersection number, justifying the proof's combinatorial treatment of isotopy classes. — search: `epstein curves on 2-manifolds isotopies pdf`
  - *Overlap:* Overlaps directly with Farb & Margalit on the foundational proofs of minimal intersections and the Bigon Criterion.
- [paper] Louis H. Kauffman / 1999 — Virtual Knot Theory — European Journal of Combinatorics — arxiv:math/9811028 — Introduces Gauss diagrams to rigorously encode immersed arc crossings and explicitly tracks topological connectivity under smoothings. — search: `kauffman virtual knot theory arxiv pdf`
  - *Overlap:* Overlaps with Chmutov et al. regarding the formal encoding of topological crossings via Gauss diagrams.
- [book] V. O. Manturov / 2004 — Knot Theory — CRC Press — no ID — Extensively covers admissibility conditions for Gauss words, providing alternative algebraic machinery to encode planar immersions. — search: `manturov knot theory pdf`
  - *Overlap:* Also heavily overlaps with Chmutov et al. on Gauss words, Gauss diagrams, and chord graphs.

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

## Narrower draw 2
## LOAD-BEARING

- [book] Benson Farb, Dan Margalit / 2011 — A Primer on Mapping Class Groups — Princeton University Press — no ID — Establishes the Bigon Criterion to formally rule out multiple crossings between any two intervals in minimal configurations, addressing Fallacy 1 and Scaffolding Q1. — search: `farb margalit primer mapping class groups pdf`
  - **Addressed Gap:** Fallacy 1, Scaffolding Q1
  - **Load-bearing piece:** Section 1.2 details the Bigon Criterion, providing the foundational topological condition that curves minimally intersecting in a disk possess no embedded bigons.

- [book] Sergei K. Lando, Alexander K. Zvonkin / 2004 — Graphs on Surfaces and Their Applications — Springer — no ID — Provides algebraic permutation machinery for ribbon graphs to strictly compute region boundaries without geometric pictures, fixing Slip 5 and Scaffolding Q3. — search: `lando zvonkin graphs on surfaces pdf`
  - **Addressed Gap:** Slip 5, Scaffolding Q3
  - **Load-bearing piece:** Chapter 1 formalizes rotation systems and the permutation-cycle representation of ribbon graphs, demonstrating how to compute complementary region boundaries algebraically.

- [book] S. Chmutov, S. Duzhin, J. Mostovoy / 2012 — Introduction to Vassiliev Knot Invariants — Cambridge University Press — no ID — Formalizes Gauss diagrams and combinatorial exhaustion of chord diagrams to rule out higher-crossing matchings, answering Fallacies 3 and 4. — search: `chmutov duzhin mostovoy vassiliev pdf`
  - **Addressed Gap:** Fallacy 3, Fallacy 4, Scaffolding Q2
  - **Load-bearing piece:** Chapter 4 covers chord diagrams and Gauss diagrams, providing the rigorous combinatorial encoding necessary to exhaustively classify isotopy classes of immersions.

- [book] Allen Hatcher / 2002 — Algebraic Topology — Cambridge University Press — no ID — Canonical source for the Euler-Poincaré formula (SNT-1) and clarifies the Hurewicz/homology requirements to distinguish homology spheres from actual spheres, addressing Slip 6. — search: `hatcher algebraic topology pdf`
  - **Addressed Gap:** Slip 6, Scaffolding Q4
  - **Load-bearing piece:** Section 2.2 explicitly connects cellular counts to homology via the Euler-Poincaré formula, and Section 4.2 (the Hurewicz Theorem) proves what additional simply-connected conditions are required to deduce a space is homeomorphic/homotopy-equivalent to $S^2$.

## SUPPORTING

- [monograph] Louis H. Kauffman / 1987 — On Knots — Princeton University Press — no ID — Details state smoothings (Kauffman bracket mechanics) which formally verify how local resolutions at a crossing connect arc endpoints, supporting the mechanics needed to resolve Fallacy 2 and Scaffolding Q5.
- [paper] D. B. A. Epstein / 1966 — Curves on 2-manifolds and isotopies — Acta Mathematica — no ID — Underpins the foundational assumptions by proving curves can be ambiently isotoped to realize their minimal intersection number without introducing extraneous crossings.

## REDUNDANT

- [book] W. B. R. Lickorish / 1997 — An Introduction to Knot Theory — Springer — no ID — Redundant to Kauffman 1987 (*On Knots*) regarding the mechanics of state smoothings and topological arc reconnections.
- [paper] Louis H. Kauffman / 1999 — Virtual Knot Theory — European Journal of Combinatorics — arxiv:math/9811028 — Redundant to Chmutov et al. (2012) regarding the specific use of Gauss diagrams to encode immersed crossings and endpoints.
- [book] V. O. Manturov / 2004 — Knot Theory — CRC Press — no ID — Redundant to Chmutov et al. (2012) regarding Gauss words and the admissibility of chord diagrams.

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and open-access substitutes that address the specific topological and combinatorial gaps identified by the grader, as well as the standard named theorem (SNT-1) in the proof.

- **Authors / Year** — Allen Hatcher / 2002
- **Title** — Algebraic Topology
- **Type** — book
- **Venue** — Cambridge University Press
- **External IDs** — (none remembered precisely)
- **Main result or relevant chapter/section** — Chapter 2 (Homology) rigorously establishes cellular homology, proving the Euler-Poincaré formula ($\chi(X) = \sum (-1)^k c_k = \sum (-1)^k b_k$) for finite CW complexes, and details the conditions under which a space with nontrivial Betti numbers must be non-contractible.
- **Topic needed for this proof** — The formal prerequisites and boundary map conditions required before Euler-characteristic cell counts can be used to deduce the homology and non-contractibility of a CW complex.
- **Open-access substitute for that topic** — (open-access for topic: cellular homology and euler characteristic) — Hatcher / 2002 / Algebraic Topology / author's personal homepage at Cornell
- **Connection** — This is the canonical source for SNT-1 (Euler-Poincaré Formula) and directly answers Grader Gap 6 (justifying why $S^2$ homology bounds definitively rule out contractibility).
- **Web search query** — `hatcher algebraic topology pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Benson Farb, Dan Margalit / 2011
- **Title** — A Primer on Mapping Class Groups
- **Type** — book
- **Venue** — Princeton University Press (Princeton Mathematical Series)
- **External IDs** — (none remembered precisely)
- **Main result or relevant chapter/section** — Chapter 1 introduces the "Bigon Criterion," proving that two properly embedded arcs or simple closed curves on a surface are in minimal position (intersect minimally) if and only if they do not bound a bigon (a topological lens).
- **Topic needed for this proof** — The geometric principle that if two embedded arcs in a disk intersect more than once, they form a closed lens (bigon) which can be eliminated via isotopy, meaning arcs with alternating endpoints on the boundary cross exactly once in minimal position.
- **Open-access substitute for that topic** — (open-access for topic: bigon criterion for curves on surfaces) — Farb, Margalit / 2011 / A Primer on Mapping Class Groups / pre-publication draft hosted on Margalit's personal webpage
- **Connection** — Directly answers Grader Gap 1 (ruling out two crossings forming a closed lens) and Gap 4 (ruling out non-minimal higher cells by asserting that isotopy classes without bigons have bounded intersections).
- **Web search query** — `farb margalit primer mapping class groups pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — D. B. A. Epstein / 1966
- **Title** — Curves on 2-manifolds and isotopies
- **Type** — paper
- **Venue** — Acta Mathematica 115
- **External IDs** — (none remembered precisely)
- **Main result or relevant chapter/section** — Proves foundational theorems demonstrating that homotopic curves on surfaces can be ambiently isotoped to realize their minimal geometric intersection number, completely avoiding extraneous intersections. 
- **Topic needed for this proof** — The foundational topological proof that configurations of embedded arcs in a disk up to isotopy are completely and uniquely determined by their boundary endpoints and their minimal-intersection chord diagram.
- **Open-access substitute for that topic** — (open-access for topic: minimal intersections of curves on surfaces) — Hass, Scott / 1992 / Intersections of curves on surfaces / Israel Journal of Mathematics
- **Connection** — Answers Grader Gap 3 by mathematically justifying why the proof's enumeration safely treats isotopy classes as ordinary combinatorial chord pairings (i.e., that the classification via endpoints and alternating crossing states is complete).
- **Web search query** — `epstein curves on 2-manifolds isotopies pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Sergei K. Lando, Alexander K. Zvonkin / 2004
- **Title** — Graphs on Surfaces and Their Applications
- **Type** — book
- **Venue** — Springer (Encyclopaedia of Mathematical Sciences)
- **External IDs** — (none remembered precisely)
- **Main result or relevant chapter/section** — Chapter 6 extensively treats "Chord Diagrams" and their intersection graphs, including combinatorial algorithms (often using ribbon graphs or fatgraphs) for tracing the boundary faces (complementary regions) of a set of intersecting chords embedded in a disk.
- **Topic needed for this proof** — A systematic, purely combinatorial encoding for tracing face boundaries and computing the boundary endpoints of every complementary region without relying on geometric pictures.
- **Open-access substitute for that topic** — (open-access for topic: combinatorial face tracing of chord diagrams) — Chmutov, Duzhin, Mostovoy / 2012 / Introduction to Vassiliev Knot Invariants / arxiv:1103.5628 (Part 1 contains extensive, open-access treatments of chord diagrams, intersection graphs, and ribbon surfaces)
- **Connection** — Directly addresses Grader Gap 5 (systematic combinatorial verification of region boundaries) and answers Scaffolding Question 3 on computing complementary regions computationally.
- **Web search query** — `lando zvonkin graphs on surfaces pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Louis H. Kauffman / 1999
- **Title** — Virtual Knot Theory
- **Type** — paper
- **Venue** — European Journal of Combinatorics 20(7)
- **External IDs** — `arxiv:math/9811028`
- **Main result or relevant chapter/section** — Introduces Gauss diagrams (Gauss codes) to rigorously encode immersed arc crossings algebraically, and explicitly defines how local "smoothings" (resolving a crossing) systematically alter the endpoint connections of the resulting combinatorial state.
- **Topic needed for this proof** — Encoding an immersed matching using Gauss codes to record crossing pairs/orders, and characterizing mathematically how local smoothing at a crossing algebraically swaps the endpoints of the resulting arcs.
- **Open-access substitute for that topic** — (open-access for topic: Gauss diagrams and crossing smoothings) — Kauffman / 1998 / Virtual Knot Theory / arxiv:math/9811028
- **Connection** — Addresses Grader Gap 2 (the missing formalization of the "unconstructed smoothing descendant") and answers Scaffolding Questions 2 and 5 (how to encode immersions and how local smoothing explicitly affects endpoints).
- **Web search query** — `kauffman virtual knot theory arxiv pdf`
- **Confidence (bibliographic):** HIGH
- **ID confidence:** HIGH

## Gauntlet draw 1
Here are the canonical references and open-access substitutes that address the specific mathematical gaps identified by the graders, particularly focusing on the combinatorial encodings and topological rules the proof skips.

### 1. Hatcher / 2002
- **Authors / Year:** Allen Hatcher / 2002
- **Title:** Algebraic Topology
- **Type:** book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 2 (Homology), Section 2.2 on Cellular Homology and Theorem 2.44 (the Euler-Poincaré formula). It formally proves that the Euler characteristic derived from cell counts equals the alternating sum of Betti numbers, and explores exactly what topological equivalence conclusions can (and cannot) be drawn from Betti numbers alone.
- **Topic needed for this proof:** The relationship between Euler characteristic, Betti numbers, and the limitations of inferring homeomorphism to $S^2$ strictly from cellular homology counts.
- **Open-access substitute for that topic:** `(open-access for topic: Cellular homology and Euler characteristic) — Hatcher / 2002 / Algebraic Topology / author's webpage (Cornell)`
- **Connection:** Addresses **Slip 6** and **Scaffolding 4**. The proof computes $\chi=2$ and infers $b_2 \ge 1$, which is valid and implies non-trivial homology (and thus non-contractibility). However, the proof unlawfully jumps to asserting the space is homeomorphic to $S^2$. Hatcher clarifies that $b_2=1$ does not guarantee an $S^2$ sphere without proving simple connectivity (via fundamental groups / Whitehead's Theorem) or $b_1=0$.
- **Web search query:** `hatcher algebraic topology pdf`
- **Confidence (bibliographic):** HIGH

### 2. Farb, Margalit / 2011
- **Authors / Year:** Benson Farb, Dan Margalit / 2011
- **Title:** A Primer on Mapping Class Groups
- **Type:** book
- **Venue:** Princeton University Press
- **Main result or relevant chapter/section:** Chapter 1, Section 1.2 ("The Bigon Criterion"). It establishes that two properly embedded simple arcs (or closed curves) in a surface intersect minimally if and only if they do not bound an embedded bigon (a 2-gon). If they do form a bigon, an isotopy can reduce the intersection count.
- **Topic needed for this proof:** The Bigon Criterion for rigorously ruling out multiple crossings between any two intervals in a minimal configuration.
- **Open-access substitute for that topic:** `(open-access for topic: The Bigon Criterion) — Farb, Margalit / 2011 / A Primer on Mapping Class Groups / author's webpage`
- **Connection:** Resolves **Fallacy 1** and **Scaffolding 1**. The proof asserts that "two intervals cannot cross more than once" to ban closed loops upon resolution. The standard formal justification for this in geometric topology is the Bigon Criterion—any multiple crossing of two intervals forms a lens/bigon, meaning the configuration is not in minimal position and forms an invalid isotopy class for the cell. 
- **Web search query:** `farb margalit primer mapping class groups pdf`
- **Confidence (bibliographic):** HIGH

### 3. Lando, Zvonkin / 2004
- **Authors / Year:** Sergei K. Lando, Alexander K. Zvonkin / 2004
- **Title:** Graphs on Surfaces and Their Applications
- **Type:** book
- **Venue:** Springer (Encyclopaedia of Mathematical Sciences)
- **Main result or relevant chapter/section:** Chapter 1 (Combinatorial Maps). Details the rigorous encoding of graphs embedded on surfaces using a pair of permutations (an involution for edges and a rotation system around vertices), proving that the cycles of their product strictly and exhaustively trace the boundary regions (faces).
- **Topic needed for this proof:** Algebraic calculation of boundary complement components for planar embedded graphs using permutation cycles.
- **Open-access substitute for that topic:** `(open-access for topic: Combinatorial maps and boundary region permutations) — Lando, Zvonkin / 2004 / Graphs on Surfaces and Their Applications / author's webpage draft`
- **Connection:** Directly addresses **Slip 5** and **Scaffolding 3**. The proof's step of tracing boundaries by narrating "up $I_1$ left side... down to 6'" is a geometric slip. Lando & Zvonkin provide the algebraic permutation machinery required to trace these region boundaries systematically and combinatorially, satisfying the grader's requirement for rigorous verification.
- **Web search query:** `lando zvonkin graphs on surfaces pdf`
- **Confidence (bibliographic):** HIGH

### 4. Lickorish / 1997
- **Authors / Year:** W. B. R. Lickorish / 1997
- **Title:** An Introduction to Knot Theory
- **Type:** book
- **Venue:** Springer (Graduate Texts in Mathematics)
- **Main result or relevant chapter/section:** Chapter 3 on the Kauffman Bracket. Formalizes how replacing a topological crossing with its A- or B-smoothings cleanly recombines the four incident half-edges into two disjoint arcs, altering the global topological connectivity of the strands.
- **Topic needed for this proof:** The topological mechanics of state smoothings at a crossing and their deterministic effect on arc endpoints.
- **Open-access substitute for that topic:** `(open-access for topic: Kauffman bracket state smoothings) — Kauffman / 1987 / State Models and the Jones Polynomial / Topology (often hosted openly on university sites)`
- **Connection:** Resolves **Fallacy 2** and **Scaffolding 5**. The proof's "unique caps" argument operates by "resolving all other crossings... to reach a valid 1-cell". This assumes a well-defined smoothing descendant. The formal topological framing for this is Kauffman-style state smoothing, which strictly dictates how endpoint connections break and re-pair when a crossing is resolved.
- **Web search query:** `lickorish introduction to knot theory pdf`
- **Confidence (bibliographic):** HIGH

### 5. Chmutov, Duzhin, Mostovoy / 2012
- **Authors / Year:** S. Chmutov, S. Duzhin, J. Mostovoy / 2012
- **Title:** Introduction to Vassiliev Knot Invariants
- **Type:** book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Chapter 4 systematically explores chord diagrams, crossing intersection graphs, and the complete enumeration of topological crossing states. 
- **Topic needed for this proof:** Systematic combinatorial enumeration and classification of higher-crossing chord diagrams.
- **Open-access substitute for that topic:** `(open-access for topic: Enumeration of chord diagrams and crossing graphs) — Chmutov, Duzhin, Mostovoy / 2012 / Introduction to Vassiliev Knot Invariants / arxiv preprint`
- **Connection:** Addresses **Fallacies 3 and 4**. The proof asserts $c_{\ge 3} = 0$ by simply displaying one specific 3-crossing arrangement ($M_{void}$) and claiming it yields an empty boundary. This is entirely ad-hoc. Combinatorial chord diagram exhaustion (as taught in this text) is the canonical method required to systematically map out all possible higher-crossing matching states and unequivocally prove the bounds on $c_2$ and $c_{\ge 3}$.
- **Web search query:** `chmutov duzhin mostovoy vassiliev knot invariants pdf`
- **Confidence (bibliographic):** HIGH

### 6. Manturov / 2004
- **Authors / Year:** V. O. Manturov / 2004
- **Title:** Knot Theory
- **Type:** book
- **Venue:** CRC Press
- **Main result or relevant chapter/section:** Contains extensive chapters on Gauss codes and Gauss diagrams, specifically covering the admissibility conditions for determining when an abstract crossing sequence is realizable as a strict planar immersion without artifacts.
- **Topic needed for this proof:** Encoding immersed arcs using Gauss words and diagrams to record endpoints and crossing orders simultaneously.
- **Open-access substitute for that topic:** `(open-access for topic: Gauss diagrams and planar realizability) — Manturov / 2004 / Knot Theory / author's webpage`
- **Connection:** Addresses **Scaffolding 2**. A Gauss code records exactly the pairing of endpoints, the pairs of crossing arcs, and the specific sequence of crossings along each individual arc. Utilizing this notation provides the exact scaffolding required to algebraically classify the matchings rather than just enumerating isotopy classes by eye.
- **Web search query:** `manturov knot theory pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here is a curated selection of literature aimed directly at closing the gaps identified by the graders. The critique zeroes in on topological curve systems (specifically how to rigorously exclude bigons/lenses and systematically encode immersions) and standard algebraic topology (where the proof incorrectly asserts that $\chi=2$ immediately yields a sphere).

- **Authors / Year** — Benson Farb, Dan Margalit / 2011
- **Title** — *A Primer on Mapping Class Groups*
- **Type** — book
- **Venue** — Princeton Mathematical Series, Vol. 49
- **External IDs** — 
- **Main result or relevant chapter/section** — Chapter 1 (specifically Section 1.2 on Intersection Numbers and the "Bigon Criterion") proves that two transversally intersecting curves/arcs in a surface form a bigon (a 2-gon or lens) if and only if they are not in minimal position. 
- **Topic needed for this proof** — The Bigon Criterion for rigorously proving that intervals in a minimal-crossing matching cross at most once.
- **Open-access substitute for that topic** — (open-access for topic: Bigon criterion for curves on surfaces) — Farb & Margalit / 2011 / *A Primer on Mapping Class Groups* / Authors' pre-publication draft hosted on Margalit's website
- **Connection** — **Fallacy 1** states the proof fails to establish that valid intervals cross at most once. The Bigon Criterion provides the exact topological machinery needed to prove that arcs in minimal configurations cannot form closed lenses (bigons).
- **Web search query** — `farb margalit primer mapping class groups pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — S.V. Chmutov, S.V. Duzhin, J. Mostovoy / 2012
- **Title** — *Introduction to Vassiliev Knot Invariants*
- **Type** — book
- **Venue** — Cambridge University Press
- **External IDs** — 
- **Main result or relevant chapter/section** — Chapter 4 ("Chord Diagrams") and Chapter 5 ("Gauss Diagrams"). These chapters formalize the combinatorial representation of generically immersed 1-manifolds (curves with crossings) by encoding the cyclic order of endpoints and the pairing of crossing preimages.
- **Topic needed for this proof** — Encoding the endpoints and internal crossing orders of generic curve immersions into rigorous Gauss words/chord diagrams.
- **Open-access substitute for that topic** — (open-access for topic: Gauss diagrams and chord diagram encodings of curve immersions) — Chmutov, Duzhin, Mostovoy / 2012 / *Introduction to Vassiliev Knot Invariants* / arxiv draft
- **Connection** — **Fallacies 3 & 4** and **Scaffolding Q2**. The proof treats isotopy classes as informal sketches. Gauss diagram encodings mathematically exhaust all possible immersions (including $\ge 3$ crossing cells), directly addressing the grader's demand for a complete, rigorous enumeration that doesn't rely on pictures.
- **Web search query** — `chmutov duzhin mostovoy vassiliev pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — S. Lando, A. Zvonkin / 2004
- **Title** — *Graphs on Surfaces and Their Applications*
- **Type** — monograph
- **Venue** — Springer (Encyclopaedia of Mathematical Sciences, Vol. 141)
- **External IDs** — 
- **Main result or relevant chapter/section** — Chapter 1 ("Graphs and Surfaces") and Chapter 2 ("Combinatorial Maps") detail the theory of ribbon graphs (fatgraphs). They provide the exact algebraic permutations (the face-walk algorithms) required to compute the boundary components of regions defined by embedded graph skeletons without relying on geometry.
- **Topic needed for this proof** — Combinatorially computing the complementary region boundaries of immersed networks via ribbon graph permutations.
- **Open-access substitute for that topic** — (open-access for topic: ribbon graph permutations and face boundary traces) — Lando, Zvonkin / 2004 / *Graphs on Surfaces and Their Applications* / Course notes often host excerpts of chapter 1 & 2
- **Connection** — **Slip 1** and **Scaffolding Q3**. The proof currently relies on manual, geometric "tracing" of regions (e.g., "1' up $I_1$ left side..."). Ribbon graph boundary permutations (the product of vertex rotations and edge involutions) would translate this intuitive tracing into a purely algebraic, combinatorial verification that satisfies the grader.
- **Web search query** — `lando zvonkin graphs on surfaces pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Louis H. Kauffman / 1987
- **Title** — *On Knots*
- **Type** — monograph
- **Venue** — Annals of Mathematics Studies 115, Princeton University Press
- **External IDs** — 
- **Main result or relevant chapter/section** — Chapters 2 and 3 discuss state models and the Kauffman bracket, detailing explicitly what happens to the topological connectivity of loops and arcs when a localized crossing is "smoothed" (resolved).
- **Topic needed for this proof** — The topological tracking of boundary component connectivity under local crossing smoothings.
- **Open-access substitute for that topic** — (open-access for topic: crossing smoothings and state curves) — Kauffman / 2004 / *State Models and Knot Polynomials* / Various survey PDFs by Kauffman
- **Connection** — **Fallacy 2** and **Scaffolding Q5**. The proof claims a "unique caps" isolation argument through crossing resolution, but does not formalize how the local smoothing dynamically alters the global endpoints. Kauffman's state-model formalism handles exactly this type of local-to-global descendant tracking.
- **Web search query** — `kauffman on knots pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year** — Allen Hatcher / 2002
- **Title** — *Algebraic Topology*
- **Type** — book
- **Venue** — Cambridge University Press
- **External IDs** — 
- **Main result or relevant chapter/section** — Chapter 2 covers cellular homology, Betti numbers, and the Euler characteristic formula ($\chi = \sum (-1)^n c_n = \sum (-1)^n b_n$). Chapter 4 covers the Hurewicz Theorem and Whitehead's Theorem, explaining what is actually required for a space with the homology of $S^2$ to be genuinely homeomorphic or homotopy-equivalent to $S^2$.
- **Topic needed for this proof** — The Hurewicz theorem and the distinction between a space having the Euler characteristic/homology of a sphere versus actually being a sphere.
- **Open-access substitute for that topic** — (open-access for topic: cellular homology and Hurewicz theorem) — Hatcher / 2002 / *Algebraic Topology* / Author's personal webpage
- **Connection** — **Slip 2** and **Scaffolding Q4**. The proof computes $\chi = 2$ and $b_2 \ge 1$ and blindly asserts "the complex topologically forms the 2-sphere $S^2$." The grader correctly flags this as mathematically unjustified. Hatcher is the standard text outlining the missing steps (e.g., proving simple connectivity and trivial $H_1$ to promote homology to homotopy via Hurewicz). 
- **Web search query** — `hatcher algebraic topology pdf`
- **Confidence (bibliographic):** HIGH
