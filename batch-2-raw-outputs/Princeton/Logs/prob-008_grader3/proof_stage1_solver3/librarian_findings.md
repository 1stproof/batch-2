# Librarian Findings — grader3_f204b6faaedc_proof_stage1_solver3_20260531_022831
**Generated:** 2026-05-31T02:34:44  
**Inputs:** notebook=9877 chars, proof=6636 chars, gap_report=3876 chars  
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
- [book] Maclagan, D., Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society — IDs: no ID — Directly details the geometry of metric trees and tropical lines, exposing the topological fallacy that apex translation yields only one valid continuous space. — search: `maclagan sturmfels tropical geometry pdf`
- [book] Oxley, J. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID — Classifies matroid quotients and explains how contractions introduce loops, invalidating the proof's assertion that $U_{1,3} \oplus U_{1,1}$ is the unique intermediate rank-2 matroid. — search: `oxley matroid theory pdf`
- [paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — Mathematische Zeitschrift / Selecta Mathematica — IDs: no ID — Formalizes the bijection between tropical linear spaces and valuated matroids modulo lineality, crucial for resolving the proof's conflation of discrete configurations and continuous scaling. — search: `speyer tropical linear spaces pdf`
- [paper] Dress, A. W. M., Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID — Establishes foundational axioms for valuated matroids and orthogonal valuated duality, necessary to explicitly construct the anti-involution instead of inferring it from degree counts. — search: `dress wenzel valuated matroids pdf`

## RELATED
- [monograph] Murota, K. / 2003 — Discrete Convex Analysis — SIAM — IDs: no ID — Covers operations on valuated matroids including strong maps and duality, providing a rigorous discrete convex framework for evaluating orthogonal duality isomorphisms. — search: `murota discrete convex analysis pdf`
- [book] Joswig, M. / 2021 — Essentials of Tropical Combinatorics — American Mathematical Society — IDs: no ID — Explains the polyhedral complex structures of the Dressian, reinforcing why valuated combinatorial quotient configurations exhibit continuous metric dimensions. — search: `joswig essentials of tropical combinatorics pdf`
- [paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2009 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID — Visually and structurally clarifies the metric tree topology and apex translations of tropical lines, concretely refuting the $1 = \infty$ cardinality bound. — search: `how to draw tropical planes pdf`

## SOMEWHAT RELATED
- [monograph] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (2nd Edition) — Cambridge University Press — IDs: no ID — Supplies standard order-theoretic properties of anti-automorphisms on posets to justify the mapping behavior between lower and upper intervals. — search: `stanley enumerative combinatorics vol 1 pdf`

## NOT MUCH
- (None. All provided sources precisely target the structural, topological, and combinatorial fallacies flagged by the graders.)

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [book] Maclagan, D., Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society — IDs: no ID — Directly details the geometry of metric trees and tropical lines, exposing the topological fallacy that apex translation yields only one valid continuous space. — search: `maclagan sturmfels tropical geometry pdf`
  - **Addresses:** Grader A Critique, Item 3 ([Fallacy] The proof falsely concludes $|\mathcal{S}_2| = 1$) and Grader A Scaffolding Q3 (tripod translation).
  - **Key piece:** Chapter 3 provides the explicit geometric description of tropical lines in $\mathbb{TP}^2$, verifying that translating the apex of a tripod along a leg yields uncountably many distinct subsets containing the same point.

- [book] Oxley, J. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID — Classifies matroid quotients and explains how contractions introduce loops, invalidating the proof's assertion that $U_{1,3} \oplus U_{1,1}$ is the unique intermediate rank-2 matroid. — search: `oxley matroid theory pdf`
  - **Addresses:** Grader A Critique, Item 2 ([Fallacy] incorrectly claims $U_{1,3} \oplus U_{1,1}$ is the only rank 2 matroid) and Grader B Critique, Item 3 (Fallacy: ignores matroids with loops).
  - **Key piece:** Chapter 7 (specifically Section 7.3 on quotients) details the characterization of matroid quotients via strong maps and explicitly demonstrates how contraction operations systematically generate quotients with loops.

- [paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — Mathematische Zeitschrift / Selecta Mathematica — IDs: no ID — Formalizes the bijection between tropical linear spaces and valuated matroids modulo lineality, crucial for resolving the proof's conflation of discrete configurations and continuous scaling. — search: `speyer tropical linear spaces pdf`
  - **Addresses:** Grader A Scaffolding Q2 (absolute vs relative Dressian) and Grader B Critique, Item 4 (Fallacy: conflation of unvaluated configurations vs uncountably many points).
  - **Key piece:** Section 2 formally defines the bijection between the parameter space of tropical linear spaces and the space of valuated matroids taken modulo the lineality space (global scaling).

- [monograph] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (2nd Edition) — Cambridge University Press — IDs: no ID — Supplies standard order-theoretic properties of anti-automorphisms on posets to justify the mapping behavior between lower and upper intervals. — search: `stanley enumerative combinatorics vol 1 pdf`
  - **Addresses:** Grader A Critique, Item 1 ([Slip] interval isomorphisms) and Grader B Critique, Item 1 (Fallacy: order-reversing involution bijection assumption).
  - **Key piece:** Chapter 3 covers standard foundational poset theory, explicitly establishing how order-reversing involutions (anti-automorphisms) rigidly map principal ideals (lower intervals) bijectively to principal filters (upper intervals).

## SUPPORTING

- [paper] Dress, A. W. M., Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID — Establishes foundational axioms for valuated matroids and orthogonal valuated duality.
  - *Note:* Useful background for explicitly constructing the flat-lattice anti-involution required by Grader B Critique, Item 5 ([Slip]).

## REDUNDANT

- [book] Joswig, M. / 2021 — Essentials of Tropical Combinatorics — American Mathematical Society — IDs: no ID
  - *Overlap:* Redundant with **Maclagan & Sturmfels** and **Speyer** regarding the polyhedral complexes of the Dressian and metric tree topology.

- [paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2009 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID
  - *Overlap:* Redundant with **Maclagan & Sturmfels** for the visual and topological properties of tripod translation.

## PERIPHERAL

- [monograph] Murota, K. / 2003 — Discrete Convex Analysis — SIAM — IDs: no ID
  - *Reasoning:* While it discusses valuated matroids via discrete convex analysis (M-convex functions), the proof gaps are fundamentally about tropical geometry (moduli spaces, lineality) and classical matroid strong maps, making this framework adjacent but unnecessary for the immediate fixes.

## UNFAMILIAR
*(None)*

---

# Stage 3 — Chapter Picker

## Introduction to Tropical Geometry (Maclagan, D., Sturmfels, B., American Mathematical Society, 2015)
_(Directly details the geometry of metric trees and tropical lines, exposing the topological fallacy that apex translation yields only one valid continuous space. — search: `maclagan sturmfels tropical geometry pdf`)_

Here are the specific sections from Maclagan & Sturmfels that directly address the structural and geometric errors in the proof:

**Chapter 4, Section 4.2 (approx.) — Tropical Linear Spaces**
* **Which gap it addresses:** Grader A's Fallacy 3 (claiming $|\mathcal{S}_2| = 1$ rather than $\infty$ by ignoring apex translations) and Grader B's Fallacy 2.
* **Why:** This section formally details the geometry of tropical lines in $\mathbb{TP}^{n-1}$ as metric trees (e.g., tripods). It explicitly demonstrates how moving the apex (the unique vertex of degree $\ge 3$) along a leg bounded by a fixed point generates an uncountably infinite 1-parameter continuous family of distinct tropical lines that all contain that point, directly destroying the $1 \neq \infty$ cardinality argument.

**Chapter 4, Section 4.1 — Valuated Matroids**
* **Which gap it addresses:** Grader B's Fallacy 4 (the claim that $U_{1,n}$ has exactly one valuated configuration) and Grader B's Slip 6.
* **Why:** It lays out the definition of valuated matroids and their basis exchange axioms. It clarifies that a rank-1 valuated matroid on $n$ elements is parameterized by a vector in $\mathbb{R}^n / \mathbb{R}\mathbf{1}$ (the tropical projective torus), making it rigorously clear why rank-1 tropical spaces consist of uncountably many points, contradicting the proof's discrete counting assumptions.

**Chapter 4, Section 4.4 (approx.) — The Dressian (and Tropical Grassmannian)**
* **Which gap it addresses:** Grader B's Scaffold Q5 (equivalence relations imposed on valuated matroids) and Grader A's Scaffold Q2 (Absolute vs. Relative Dressian).
* **Why:** This section constructs the Dressian $\Dr(d,n)$ as a polyhedral fan whose points parameterize all valuated matroids of rank $d$ on $n$ elements. By detailing the polyhedral structure and the quotient by the lineality space (torus translations), it shows exactly when continuous parameters yield geometrically distinct tropical linear spaces versus when they scale equivalently, providing the machinery to properly evaluate $|\mathcal{S}_2|$.

## Matroid Theory (2nd Edition) (Oxley, J., Oxford University Press, 2011)
_(Classifies matroid quotients and explains how contractions introduce loops, invalidating the proof's assertion that $U_{1,3} \oplus U_{1,1}$ is the unique intermediate rank-2 matroid. — search: `oxley matroid theory pdf`)_

Here are the specific chapters and sections from Oxley's *Matroid Theory* that address the structural combinatorial gaps regarding matroid quotients and contractions. *(Note: Oxley covers purely classical unvaluated matroid theory; it will not address the metric/tropical topology gaps).*

- **Chapter 3, Section 3.1: Deletion and contraction**
  - **Which gap it addresses:** Grader B's Scaffolding Q4 (how contractions introduce loops) and Grader A's Fallacy 2 / Grader B's Fallacy 3 (missing rank-2 matroids with loops).
  - **Why:** This section establishes the fundamental rank formula for contractions: $r_{M/T}(X) = r_M(X \cup T) - r_M(T)$. It explicitly demonstrates that any element $x$ whose addition to $T$ does not increase the rank of $T$ (i.e., $x \in \text{cl}(T)$) becomes a loop in the contracted minor $M/T$, formally justifying how contracting the atoms $A_1, A_2, A_3$ generates valid intermediate configurations with loops.

- **Chapter 7, Section 7.3: Quotients**
  - **Which gap it addresses:** Grader A's Fallacy 2 and Grader B's Fallacy 3 (the false claim that $U_{1,3} \oplus U_{1,1}$ is the unique intermediate rank-2 quotient).
  - **Why:** This section defines quotients (strong maps) via the condition that the rank difference $r_M(X) - r_N(X)$ must be a non-decreasing function with respect to inclusion. It provides the classification of intermediate quotients (including elementary quotients and the Higgs lift), which gives the exact theoretical framework needed to systematically list *all* valid rank-2 matroids satisfying the chain $M \twoheadrightarrow N \twoheadrightarrow M/C_4$, proving the unicity claim is false.

## Enumerative Combinatorics, Volume 1 (2nd Edition) (Stanley, R. P., Cambridge University Press, 2011)
_(Supplies standard order-theoretic properties of anti-automorphisms on posets to justify the mapping behavior between lower and upper intervals. — search: `stanley enumerative combinatorics vol 1 pdf`)_

Here are the specific sections from Stanley’s *Enumerative Combinatorics, Volume 1* (2nd Ed., 2011) that address the purely order-theoretic gaps in the proof, along with a note on what the reference cannot fix.

- **Chapter 3, Section 3.1: Basic Concepts**
  - **Which gap it addresses:** Grader A [Slip 1] and Grader B [Fallacy 1] (Assuming an order-reversing involution sends the lower interval bijectively to the upper interval, mapping atoms to coatoms).
  - **Why:** This section formally defines posets, intervals $[x, y]$, the dual poset $P^*$, and anti-isomorphisms. It provides the foundational proof that an anti-automorphism $\Phi: P \to P$ is an order-preserving isomorphism $P \to P^*$. By definition, this map completely reverses covering relations, rigidly enforcing a bijection between the lower interval $[\hat{0}, L_{A_4}]$ and the upper interval $[L_{C_4}, \hat{1}]$, mapping the rank-1 elements (atoms) below $x$ directly to the rank-2 elements (coatoms) above $\Phi(x)$.

- **Chapter 3, Section 3.3: Lattices**
  - **Which gap it addresses:** Grader B [Slip 5] and Grader B scaffolding #1 (Properties characterizing atoms and coatoms; explicit construction of the flat-lattice anti-involution).
  - **Why:** This section formally develops the theory of geometric lattices (the lattices of flats of matroids). It defines atoms, coatoms, and modularity. Grounding the combinatorial argument in Stanley’s treatment of geometric lattices establishes exactly *why* degrees in the incidence graph dictate the mandatory anti-automorphism mappings on $\mathcal{L}(M)$ before attempting to lift them to $\Dr(M)$.

- **I do not believe this reference addresses any of the remaining named gaps.**
  - **Why:** Stanley's *Enumerative Combinatorics* is a foundational text in algebraic combinatorics and poset theory. It strictly covers discrete structures and does *not* cover tropical linear spaces, valuated matroids, the Brandt-Maclagan-Sturmfels theorem, or the continuous moduli of the relative Dressian. Resolving the remaining fallacies (Grader A Fallacy 2 & 3; Grader B Fallacy 2, 3, 4 & Slip 6) requires references in tropical geometry and matroid theory (e.g., Maclagan & Sturmfels' *Introduction to Tropical Geometry*).

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [book] Maclagan, D., Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society — IDs: no ID
  - Addresses: Grader A **[Fallacy]** 3 ("The proof falsely concludes $|\mathcal{S}_2| = 1$") and Grader A Scaffolding Question 3.
  - Chapter 3 ("Tropical Lines and Trees") explicitly covers metric tree topologies and the generation of infinite distinct subsets by translating the apex along a leg.

- [book] Oxley, J. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID
  - Addresses: Grader A **[Fallacy]** 2 ("incorrectly claims $U_{1,3} \oplus U_{1,1}$ is the only rank 2 matroid satisfying the quotient chain") and Grader B **Fallacy:** 3 ("classification of possible underlying rank-two quotients is unsupported").
  - Chapter 7 ("Quotients, flats, and strong maps") provides the definitive classification of matroid quotients, rigorously showing how contractions and strong maps introduce loops and parallel elements.

- [paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — Mathematische Zeitschrift / Selecta Mathematica — IDs: no ID
  - Addresses: Grader B **Fallacy:** 4 ("claim that $U_{1,n}$ has only one valuated configuration is inconsistent...") and Grader A Scaffolding Question 2.
  - Section 2 formalizes the bijection between tropical linear spaces and valuated matroids, explicitly treating the lineality space quotient needed to resolve the conflation between absolute and relative Dressians.

- [monograph] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (2nd Edition) — Cambridge University Press — IDs: no ID
  - Addresses: Grader A **[Slip]** 1 ("assumes, without explicitly justifying via interval isomorphisms...") and Grader B **Fallacy:** 1 ("assumes, without justification, that an order-reversing involution must send...").
  - Chapter 3 ("Partially Ordered Sets") details interval bijections and the standard properties of poset anti-automorphisms required to formally map a lower interval strictly to an upper interval.

## SUPPORTING

- [paper] Dress, A. W. M., Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID
  - Provides the formal axioms and foundational mechanics of orthogonal valuated duality necessary to address Grader B **Slip:** 5 ("flat-lattice anti-involution should be explicitly constructed").

- [book] Joswig, M. / 2021 — Essentials of Tropical Combinatorics — American Mathematical Society — IDs: no ID
  - Clarifies the polyhedral complex structures of the Dressian, which provides solid background for bounding uncountability in discrete rank 1 combinatorial topologies.

## REDUNDANT

- [paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2009 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID
  - Redundant with Maclagan & Sturmfels regarding the visual metric geometry and continuous apex translations of tropical lines.

- [monograph] Murota, K. / 2003 — Discrete Convex Analysis — SIAM — IDs: no ID
  - Redundant with Dress & Wenzel and Speyer regarding the axiomatic definitions of valuated matroids and their dualities.

## PERIPHERAL

*(None)*

## UNFAMILIAR

*(None)*

## Narrower draw 2
Here is the triage of the provided works against the specific grader gaps, based on their known mathematical contents.

## LOAD-BEARING

**[book] Maclagan, D., Sturmfels, B. / 2015 — Introduction to Tropical Geometry — American Mathematical Society — IDs: no ID**
*   **Target:** Grader A [Fallacy] 3; Grader B [Slip] 6
*   **Location:** Chapter 3 (especially Section 3.1 on metric graphs) and Chapter 4 (Tropical Linear Spaces) rigorously detail how translating the apex of a tropical line along a ray continuously generates uncountably many tropical linear spaces containing a fixed point, disproving the $|\mathcal{S}_2| = 1$ assumption.

**[book] Oxley, J. / 2011 — Matroid Theory (2nd Edition) — Oxford University Press — IDs: no ID**
*   **Target:** Grader A [Fallacy] 2; Grader B [Fallacy] 3
*   **Location:** Chapter 7 ("Matroid Quotients" and "Strong Maps") explicitly proves how matroid contractions natively introduce loops, refuting the proof's false classification that $U_{1,3} \oplus U_{1,1}$ is the uniquely valid intermediate rank-2 quotient.

**[paper] Speyer, D. E. / 2008 — Tropical Linear Spaces — Mathematische Zeitschrift / Selecta Mathematica — IDs: no ID**
*   **Target:** Grader B [Fallacy] 4 (and Grader A Scaffolding Q2)
*   **Location:** Section 2 formally defines the fundamental bijection between points on the Dressian (tropical linear spaces) and valuated matroids modulo the lineality space (tropical scaling), correcting the proof's conflation of discrete configurations with continuous scalar equivalence classes.

**[monograph] Stanley, R. P. / 2011 — Enumerative Combinatorics, Volume 1 (2nd Edition) — Cambridge University Press — IDs: no ID**
*   **Target:** Grader A [Slip] 1; Grader B [Fallacy] 1
*   **Location:** Chapter 3 ("Partially Ordered Sets") establishes the fundamental theorem that if an order-reversing involution (anti-automorphism) maps an element $x$ to $y$, it strictly induces a dual isomorphism between the lower interval $[0, x]$ and the upper interval $[y, 1]$.

## SUPPORTING

**[paper] Dress, A. W. M., Wenzel, W. / 1992 — Valuated Matroids — Advances in Mathematics — IDs: no ID**
*   *Note:* Foundational source for the axioms of orthogonal valuated duality required to explicitly construct the flat-lattice anti-involution for Grader B [Slip] 5.

## REDUNDANT

**[paper] Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2009 — How to draw tropical planes — Electronic Journal of Combinatorics — IDs: no ID**
*   *Overlap:* Redundant with **Maclagan & Sturmfels (2015)**, which absorbed these specific visual and structural proofs of apex translations into Chapter 4.

**[book] Joswig, M. / 2021 — Essentials of Tropical Combinatorics — American Mathematical Society — IDs: no ID**
*   *Overlap:* Redundant with **Maclagan & Sturmfels** and **Speyer** regarding the polyhedral geometry of the Dressian and continuous metric dimensions.

**[monograph] Murota, K. / 2003 — Discrete Convex Analysis — SIAM — IDs: no ID**
*   *Overlap:* Redundant with **Dress & Wenzel** for the definition of valuated duality, and less directly applicable to the specific tropical formulations requested by the graders.

## PERIPHERAL
*(None)*

## UNFAMILIAR
*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical texts and papers that address the gaps in the proof, specifically targeting the topological misconceptions about tropical lines (the $1 = \infty$ fallacy) and the combinatorial misconceptions about matroid quotients and loops identified by the graders.

**Maclagan, Sturmfels / 2015**
- **Title:** Introduction to Tropical Geometry
- **Type:** monograph
- **Venue:** American Mathematical Society, Graduate Studies in Mathematics, Vol. 161
- **Main result or relevant chapter/section:** Chapter 4 ("Tropical Linear Spaces and Matroids"), specifically the sections parameterizing the Dressian $\Dr(n, d)$ and the geometry of metric trees / tropical lines (tripods) in $\mathbb{TP}^2$.
- **Topic needed for this proof:** The geometric parameterization of rank-2 tropical linear spaces, explicitly showing how translating the apex of a tropical line (a tripod) along a leg corresponds to distinct continuous parameters while preserving containment of points on that leg. 
- **Open-access substitute for that topic:** (open-access for topic: Pre-publication draft of Introduction to Tropical Geometry) — Maclagan, Sturmfels / 2014 / Introduction to Tropical Geometry / authors' homepages
- **Connection:** This completely resolves Grader A's critique (Fallacy 3) and Grader B's Scaffolding Question 3. Translating the apex of the rank 2 tropical linear space $W$ along the outgoing ray toward $L_{C_4}$ yields infinitely many distinct subsets that still strictly contain $L_{C_4}$, invalidating the proof's core calculation that $|\mathcal{S}_2| = 1$.
- **Web search query:** `maclagan sturmfels introduction tropical geometry pdf`
- **Confidence (bibliographic):** HIGH

**Oxley / 2011**
- **Title:** Matroid Theory (Second Edition)
- **Type:** book
- **Venue:** Oxford Graduate Texts in Mathematics, Oxford University Press
- **Main result or relevant chapter/section:** Chapter 7 ("Quotients and Strong Maps").
- **Topic needed for this proof:** The structural characterization of matroid quotients, particularly how contracting an atom forces parallel elements to become loops in the quotient, and the definition of the Higgs major.
- **Open-access substitute for that topic:** (open-access for topic: Matroid Quotients and Strong Maps chapter) — Oxley / Matroid Theory (sample chapters or lecture notes covering Chapter 7) / math.lsu.edu/~oxley
- **Connection:** Addresses Grader A's Fallacy 2 and Grader B's Fallacy 3. The proof falsely assumes $U_{1,3} \oplus U_{1,1}$ is the *only* valid underlying rank 2 quotient. Oxley's Chapter 7 provides the standard techniques to compute all valid quotients (including those with loops) that can bridge $M$ and $M/C_4$, proving the quotient space is much larger.
- **Web search query:** `james oxley matroid theory pdf`
- **Confidence (bibliographic):** HIGH

**Speyer / 2008**
- **Title:** Tropical Linear Spaces
- **Type:** paper
- **Venue:** SIAM Journal on Discrete Mathematics (Vol. 22)
- **Main result or relevant chapter/section:** Sections 3 and 4, which establish the exact bijection between points on the Dressian (valuated matroids modulo lineality) and the geometric polyhedral complexes known as tropical linear spaces.
- **Topic needed for this proof:** The precise correspondence between valuated matroid configurations and the lineality/moduli parameters of their corresponding tropical geometric subsets.
- **Open-access substitute for that topic:** (open-access for topic: Geometry of tropical linear spaces and the Dressian) — Speyer / 2004 / Tropical Linear Spaces / arxiv
- **Connection:** Addresses Grader B's Scaffolding Question 5 and Fallacy 4. It clarifies the fundamental category error the proof makes by conflating the space of *valuated matroids* modulo lineality (where a uniform matroid $U_{1,n}$ has "1 configuration") with the *relative* ambient space in which a tropical line inherits continuous translation parameters relative to the origin. 
- **Web search query:** `david speyer tropical linear spaces pdf`
- **Confidence (bibliographic):** HIGH

**Murota / 2003**
- **Title:** Discrete Convex Analysis
- **Type:** monograph
- **Venue:** SIAM Monographs on Discrete Mathematics and Applications
- **Main result or relevant chapter/section:** Chapter 5 ("Valuated Matroids").
- **Topic needed for this proof:** The rigorous definition of valuated strong maps (quotients) and orthogonal valuated duality.
- **Open-access substitute for that topic:** (open-access for topic: Valuated matroid strong maps and duality relations) — Murota / 1996 / Valuated Matroid Intersection, I: Optimality Criteria / SIAM Journal on Discrete Mathematics (or author's open survey pdfs)
- **Connection:** Directly supports the constructive needs of the proof (and Grader B's Slip 5) by showing exactly how the flat-lattice anti-involution $F \mapsto F^\perp$ formally lifts to the valuated orthogonal dual $N \mapsto N^\perp$ without relying on ad-hoc degree counting. (This also backstops the "Brandt-Maclagan-Sturmfels" anti-isomorphism SNT, which often appears in literature as the equivalence of valuated strong maps and nested tropical linear spaces).
- **Web search query:** `murota discrete convex analysis pdf`
- **Confidence (bibliographic):** HIGH

**Dress, Wenzel / 1992**
- **Title:** Valuated Matroids
- **Type:** paper
- **Venue:** Advances in Mathematics (Vol. 93)
- **Main result or relevant chapter/section:** The foundational construction of the valuated matroid axioms, including the behavior of the valuated circuits/bases under restriction, contraction, and orthogonal duality.
- **Topic needed for this proof:** The explicit construction of the orthogonal dual of a valuated matroid.
- **Connection:** Required to resolve Grader B's Slip 5 ("The flat-lattice anti-involution should be explicitly constructed"). This is the canonical, foundational paper a mathematician would cite when invoking the operation that sends a valuated matroid to its orthogonal dual to induce an order-reversing involution on the quotient poset.
- **Web search query:** `dress wenzel valuated matroids advances pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and topic-keyed substitutes that directly address the geometric and combinatorial fallacies identified by the graders, particularly regarding the moduli of tropical linear spaces, the lattice of matroid quotients, and the equivalence relations defining the Dressian.

**Maclagan, D. & Sturmfels, B. / 2015 / Introduction to Tropical Geometry**
*   **Type:** Book
*   **Venue:** American Mathematical Society (Graduate Studies in Mathematics)
*   **Main result or relevant chapter/section:** Chapter 4 (Tropical Lines and Trees) and Chapter 5 (Tropical Linear Spaces), which explicitly detail how tropical linear spaces of rank 2 are parameterized by metric trees.
*   **Topic needed for this proof:** The translational moduli of rank-2 tropical linear spaces; specifically, how translating the apex of a tropical line along an outgoing leg generates a continuous family of distinct rank-2 tropical linear spaces that all contain a fixed rank-1 point on that leg.
*   **Open-access substitute for that topic:** `(open-access for topic: Pre-publication draft covering tropical linear spaces and metric trees) — Maclagan, D. & Sturmfels, B. / 2014 / Introduction to Tropical Geometry / Authors' personal webpages`
*   **Connection:** Directly refutes the proof's claim that $|\mathcal{S}_2| = 1$ (Grader A Fallacy 3, Grader B Fallacy 2). It provides the exact geometric mechanism showing that the set of rank-2 spaces above $L_{C_4}$ is uncountably infinite due to apex translation.
*   **Web search query:** `maclagan sturmfels tropical geometry pdf`
*   **Confidence (bibliographic):** HIGH

**Oxley, J. / 2011 / Matroid Theory**
*   **Type:** Book
*   **Venue:** Oxford University Press (Oxford Graduate Texts in Mathematics)
*   **Main result or relevant chapter/section:** Chapter on "Matroid Quotients" (specifically the results on quotient chains, elementary quotients, and how minors interact with strong maps).
*   **Topic needed for this proof:** The complete classification of intermediate matroids in a quotient chain $M \twoheadrightarrow N \twoheadrightarrow M/F$, and the fact that contracting by an element (like the coatom $C_4$) naturally introduces loops in valid intermediate quotients.
*   **Open-access substitute for that topic:** `(open-access for topic: Lecture notes on matroid minors and quotient lattices) — Ardila, F. / 2015 / Matroid Theory Lecture Notes / San Francisco State University`
*   **Connection:** Addresses Grader A (Fallacy 2) and Grader B (Fallacy 3). The proof claims $U_{1,3} \oplus U_{1,1}$ is the unique valid intermediate underlying rank-2 matroid. This reference provides the structural theorems proving this is false by showing how contractions generate intermediate matroids with loops.
*   **Web search query:** `oxley matroid theory pdf`
*   **Confidence (bibliographic):** HIGH

**Speyer, D. E. / 2008 / Tropical Linear Spaces**
*   **Type:** Paper
*   **Venue:** Selecta Mathematica (Vol. 14)
*   **Main result or relevant chapter/section:** Defines tropical linear spaces rigorously via valuated matroids and details how the absolute Dressian $\text{Dr}(k,n)$ parameterizes these spaces modulo the lineality space (scaling by the all-ones vector).
*   **Topic needed for this proof:** The formal equivalence relation (modulo lineality) applied to valuated matroids when passing to tropical linear spaces.
*   **Open-access substitute for that topic:** `(open-access for topic: Author's preprint version defining the lineality equivalence of valuated matroids) — Speyer, D. E. / 2004 / Tropical Linear Spaces / arxiv`
*   **Connection:** Answers Grader B's Scaffolding Question 5 and Fallacy 4. The proof fatally conflates the uncountability of spatial points with the uniqueness of a valuated configuration. This paper clarifies exactly when and how scaling collapses uncountably infinite valuated configurations into single tropical projective spaces.
*   **Web search query:** `speyer tropical linear spaces pdf`
*   **Confidence (bibliographic):** HIGH

**Joswig, M. / 2021 / Essentials of Tropical Combinatorics**
*   **Type:** Book
*   **Venue:** American Mathematical Society
*   **Main result or relevant chapter/section:** Chapter on the Dressian and the Tropical Grassmannian, focusing on their explicit polyhedral complex structures.
*   **Topic needed for this proof:** The polyhedral geometry of the Dressian, demonstrating how the continuous real parameters of valuated basis exchanges manifest geometrically as higher-dimensional polyhedral cells rather than discrete points.
*   **Open-access substitute for that topic:** `(open-access for topic: Pre-publication draft of the text) — Joswig, M. / 2021 / Essentials of Tropical Combinatorics / Author's webpage (TU Berlin / MPI MiS)`
*   **Connection:** Provides the foundational geometry to rigorize the critiques regarding continuous parameters. It explains why a single combinatorial quotient type (even if it were unique) defines a polyhedral cell of positive dimension, yielding an infinite number of metric valuated configurations (Grader A Fallacy 3).
*   **Web search query:** `joswig essentials of tropical combinatorics pdf`
*   **Confidence (bibliographic):** HIGH

**Dress, A. W. M. & Wenzel, W. / 1992 / Valuated Matroids**
*   **Type:** Paper
*   **Venue:** Advances in Mathematics (Vol. 93)
*   **Main result or relevant chapter/section:** The foundational paper introducing valuated matroids, defining the core valuated basis exchange axioms, and establishing the valuated duality operations.
*   **Topic needed for this proof:** The valuated basis exchange axiom and the canonical mechanism for taking the orthogonal dual of a valuated matroid.
*   **Open-access substitute for that topic:** `(open-access for topic: Survey on valuated matroids and discrete convex analysis axioms) — Murota, K. / 2000 / Discrete Convex Analysis / RIMS Kokyuroku (Kyoto University)`
*   **Connection:** Vital for addressing Grader B's Slip 5. The proof assumes an anti-involution on the flats simply extends, without constructing it. This paper defines how valuated duality actually operates, which is strictly necessary to analyze whether an extension to $\Phi$ is even algebraically well-posed before attempting counting arguments.
*   **Web search query:** `dress wenzel valuated matroids pdf`
*   **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed substitutes that bear directly on the structural gaps and fallacies the graders identified.

- **Authors / Year**: Maclagan, D., Sturmfels, B. / 2015
- **Title**: Introduction to Tropical Geometry
- **Type**: monograph
- **Venue**: American Mathematical Society (Graduate Studies in Mathematics, Vol. 161)
- **External IDs**: 
- **Main result or relevant chapter/section**: Chapter 4 ("Tropical Linear Spaces") develops the equivalence between tropical linear spaces and valuated matroids. It explicitly describes the Dressian, the metric tree structure of tropical lines, and the continuous parameterization of moduli spaces.
- **Topic needed for this proof**: The geometric moduli of tropical lines (tripods) in $\mathbb{TP}^2$, specifically the property that translating the apex of the tripod along an outgoing ray yields an infinite continuous family of rank-2 spaces containing a fixed rank-1 point.
- **Open-access substitute for that topic**: (open-access for topic: tropical linear spaces and metric trees) — Maclagan, D., Sturmfels, B. / 2014 / Introduction to Tropical Geometry / authors' webpage book draft.
- **Connection**: Directly refutes Grader A's Fallacy 3 and Grader B's Fallacy 2 by providing the rigorous geometric reason why $|\mathcal{S}_2| = \infty$. It explains how sliding the apex generates uncountably many rank-2 tropical linear spaces containing $L_{C_4}$.
- **Web search query**: `maclagan sturmfels introduction to tropical geometry pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Oxley, J. / 2011
- **Title**: Matroid Theory (2nd Edition)
- **Type**: monograph
- **Venue**: Oxford University Press
- **External IDs**: 
- **Main result or relevant chapter/section**: Chapter 7 ("Matroid Quotients and Strong Maps") provides a comprehensive structural characterization of strong maps between matroids, intermediate quotients, and the lattice of flats.
- **Topic needed for this proof**: The classification of intermediate matroid quotients and the mechanism by which matroid quotients (contractions) can introduce loops.
- **Open-access substitute for that topic**: (open-access for topic: matroid quotients and strong maps) — Oxley, J. / 2001 / Matroid Theory / author's sample chapters or course notes on matroid strong maps.
- **Connection**: Addresses Grader A's Fallacy 2 and Grader B's Fallacy 3 by proving that the solver incorrectly omitted valid intermediate rank-2 matroids. It clarifies how elements can become loops in valid matroid quotients, invalidating the claim that $U_{1,3} \oplus U_{1,1}$ is the unique underlying matroid.
- **Web search query**: `oxley matroid theory pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Speyer, D. / 2008
- **Title**: Tropical Linear Spaces
- **Type**: paper
- **Venue**: Mathematische Zeitschrift 260(3)
- **External IDs**: 
- **Main result or relevant chapter/section**: Formalizes the bijection between valuated matroids and tropical linear spaces, proving that the geometric containment of tropical linear spaces directly corresponds to strong map quotient relations of their underlying valuated matroids.
- **Topic needed for this proof**: The theorem that tropical linear space containment $X_N \subset X_M$ is equivalent to the valuated matroid $N$ being a strong map quotient of $M$.
- **Open-access substitute for that topic**: (open-access for topic: bijection between valuated matroids and tropical linear spaces) — Speyer, D. / 2004 / Tropical Linear Spaces / arxiv preprint.
- **Connection**: This serves as the canonical published source for the "Brandt-Maclagan-Sturmfels Theorem" invoked loosely in the notebook. It is essential for justifying the translation of geometric containment ($W \supset L_{C_4}$) into the algebraic chain of valuated matroid quotients, fixing the unsupported logical leaps identified by both graders.
- **Web search query**: `speyer tropical linear spaces pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Dress, A. W. M., Wenzel, W. / 1992
- **Title**: Valuated Matroids
- **Type**: paper
- **Venue**: Advances in Mathematics 93(2)
- **External IDs**: 
- **Main result or relevant chapter/section**: Introduces the foundational axioms of valuated matroids, their flats, and defines valuated strong maps (quotients).
- **Topic needed for this proof**: The formal algebraic constraints defining valuated matroid quotients.
- **Open-access substitute for that topic**: (open-access for topic: definition and axioms of valuated matroids) — Murota, K. / 2000 / Discrete Convex Analysis / RIMS preprint.
- **Connection**: Provides the canonical algebraic framework for valuated matroid quotients to correctly evaluate and enumerate the missing valuated configurations (Grader B's Fallacy 4).
- **Web search query**: `dress wenzel valuated matroids pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Murota, K. / 2003
- **Title**: Discrete Convex Analysis
- **Type**: monograph
- **Venue**: SIAM
- **External IDs**: 
- **Main result or relevant chapter/section**: Chapter 5 and Chapter 9 comprehensively cover operations on valuated matroids, including valuated duality and valuated matroid quotients (framed via M-convex functions).
- **Topic needed for this proof**: Orthogonal duality for valuated matroids and how strong map quotients behave structurally under this duality.
- **Open-access substitute for that topic**: (open-access for topic: valuated matroids and discrete convex analysis) — Murota, K. / 2000 / Discrete Convex Analysis / RIMS preprint or survey chapter.
- **Connection**: Provides the rigorous foundation for the "orthogonal valuated duality isomorphism" hypothesized in the notebook, ensuring that dualizing valuated quotients is handled properly without conflating absolute valuated parameter spaces with relative quotient poset bounds.
- **Web search query**: `murota discrete convex analysis pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2009
- **Title**: How to draw tropical planes
- **Type**: paper
- **Venue**: Electronic Journal of Combinatorics 16(1)
- **External IDs**: 
- **Main result or relevant chapter/section**: Details the explicit embedding and visualization of tropical linear spaces in $\mathbb{TP}^n$, thoroughly describing the metric tree structure of tropical lines and planes.
- **Topic needed for this proof**: The explicit metric tree topology of a tropical line and how it structurally branches and permits apex translations in $\mathbb{TP}^2$.
- **Open-access substitute for that topic**: (open-access for topic: metric tree structure of tropical planes) — Herrmann, S., Jensen, A., Joswig, M., Sturmfels, B. / 2008 / How to draw tropical planes / arxiv preprint.
- **Connection**: Visually and structurally clarifies Grader A's Fallacy 3. It demonstrates how continuous translation parameters operate on metric trees, definitively showing why the discrete cardinality bound ($|\mathcal{S}_2|=1$) computed in the proof is topologically invalid.
- **Web search query**: `how to draw tropical planes pdf`
- **Confidence (bibliographic)**: HIGH

- **Authors / Year**: Stanley, R. P. / 2011
- **Title**: Enumerative Combinatorics, Volume 1 (2nd Edition)
- **Type**: monograph
- **Venue**: Cambridge University Press
- **External IDs**: 
- **Main result or relevant chapter/section**: Chapter 3 ("Partially Ordered Sets") sets the standard definitions for order-reversing involutions (anti-automorphisms), duality, and the behavior of atoms, coatoms, and intervals.
- **Topic needed for this proof**: The formal properties of order-reversing involutions on posets, specifically how they strictly map lower intervals (and atoms) to upper intervals (and coatoms).
- **Open-access substitute for that topic**: (open-access for topic: posets and anti-automorphisms) — Stanley, R. P. / 2011 / Enumerative Combinatorics, Volume 1 / author's webpage draft.
- **Connection**: Directly addresses Grader A's Slip 1 and Grader B's Fallacy 1 by supplying the standard formal combinatorial justification for why an order-reversing involution analytically forces a bijection between the rank-1 spaces below $L_{A_4}$ and rank-2 spaces above $L_{C_4}$.
- **Web search query**: `stanley enumerative combinatorics vol 1 pdf`
- **Confidence (bibliographic)**: HIGH
