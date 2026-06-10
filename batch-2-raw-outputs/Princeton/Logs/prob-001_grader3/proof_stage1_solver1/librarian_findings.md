# Librarian Findings — grader3_add74b27d4bd_proof_stage1_solver1_20260531_015115
**Generated:** 2026-05-31T02:02:12  
**Inputs:** notebook=11467 chars, proof=8926 chars, gap_report=3202 chars  
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
- [Book] A. S. Kechris / 1995 — Classical Descriptive Set Theory — Springer-Verlag (Graduate Texts in Mathematics, Vol. 156) — IDs: no ID — Provides the necessary topological foundation to prove that $\operatorname{AUT}(\mathcal{B})$ is a closed subspace of $S_\infty$ and translates isolated points to trivial pointwise stabilizers. — search: kechris classical descriptive set theory pdf
- [Paper] C. J. Ash, J. F. Knight, M. Manasse, T. A. Slaman / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic (Vol. 42) — IDs: no ID — The foundational paper proving the AKMS definability theorem, offering the exact cone-relativized and parameterized hypotheses needed to legally deduce the $\Sigma^{in}_1$ definition. — search: generic copies of countable structures ash knight pdf
- [Book] A. Montalbán / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press — IDs: no ID — Rigorously formalizes "copies" via explicit isomorphisms and details how parameters are evaluated and pushed between models, resolving the proof's fallacy regarding structural evaluation. — search: montalban computable structure theory within the arithmetic pdf

## RELATED
- [Book] C. J. Ash, J. F. Knight / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144) — IDs: no ID — Details the generic forcing machinery required to bridge pointwise index existence to uniform definitions, validating the quantifier swap. — search: computable structures hyperarithmetical hierarchy ash knight pdf
- [Survey] V. S. Harizanov / 1998 — Pure computable model theory — Handbook of Recursive Mathematics, Vol. 1 (Elsevier) — IDs: no ID — Outlines the model-theoretic boilerplate for defining the image of relations under an explicit isomorphism and reviews relative intrinsic computability. — search: harizanov pure computable model theory pdf

## SOMEWHAT RELATED
- [Paper] J. Chisholm / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic (Vol. 55) — IDs: no ID — Provides an independent proof of the AKMS theorem, which backstops the central citation and offers an alternative view on managing parameters. — search: effective model theory vs recursive model theory chisholm pdf

## NOT MUCH
- (None)

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [Book] A. S. Kechris / 1995 — Classical Descriptive Set Theory — Springer-Verlag (Graduate Texts in Mathematics, Vol. 156)
  Addresses: Grader B (Slip 1: Justify $\operatorname{AUT}(\mathcal{B})$ is closed in $S_\infty$) and Grader B (Slip 2: Baire argument translating isolated element to identity).
  Section 8 ("Polish Groups") provides the exact topological proofs that pointwise stabilizer subgroups in $S_\infty$ are closed/clopen, and that in any topological group, left-translation homeomorphisms force an isolated point to imply an isolated identity element.

- [Paper] C. J. Ash, J. F. Knight, M. Manasse, T. A. Slaman / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic (Vol. 42)
  Addresses: Grader A (Fallacy 2: Unjustified quantifier swap from pointwise to uniform computability) and Grader B (Slip 4: Exact AKMS theorem stated with cone-relativized and parameterized hypotheses).
  The main generic forcing theorems in this paper provide the exact mechanism to legally bypass the $\Pi^0_2$ verification via forcing on Cohen conditions, directly linking relative intrinsic $\Sigma^0_1$-ness on a cone to existential $L_{\omega_1\omega}$ definability with explicit parameter tuples.

- [Book] A. Montalbán / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press
  Addresses: Grader A (Fallacy 1: Failing to formally quantify over isomorphisms $f: \A \to \B$) and Grader B (Slip 3: Define copies expanded by the parameter tuple).
  Chapter 1's detailed formalization of "presentations" and "copies" explicitly lays out how to rigorously transport named parameters across structures via a formal isomorphism $f: \A \to \B$ without muddying the domain evaluation.

## SUPPORTING

- [Book] C. J. Ash, J. F. Knight / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144)
  Provides standard, comprehensive textbook background on the forcing machinery used to execute the pointwise-to-uniform quantifier swap, acting as a highly accessible supplement to the 1989 AKMS paper.

## REDUNDANT

- [Survey] V. S. Harizanov / 1998 — Pure computable model theory — Handbook of Recursive Mathematics, Vol. 1 (Elsevier)
  Overlaps with Montalbán 2021 in providing the model-theoretic boilerplate for defining relations under explicit isomorphisms.

- [Paper] J. Chisholm / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic (Vol. 55)
  Overlaps with the Ash-Knight-Manasse-Slaman 1989 paper by providing an independent but parallel proof of the exact same relativized definability theorem.

## PERIPHERAL

(None)

## UNFAMILIAR

(None)

---

# Stage 3 — Chapter Picker

## Classical Descriptive Set Theory (A. S. Kechris, Springer-Verlag (Graduate Texts in Mathematics, Vol. 156)
  Addresses: Grader B (Slip 1: Justify $\operatorname{AUT}(\mathcal{B})$ is closed in $S_\infty$) and Grader B (Slip 2: Baire argument translating isolated element to identity).
  Section 8 ("Polish Groups") provides the exact topological proofs that pointwise stabilizer subgroups in $S_\infty$ are closed/clopen, and that in any topological group, left-translation homeomorphisms force an isolated point to imply an isolated identity element.

- [Paper] C. J. Ash, J. F. Knight, M. Manasse, T. A. Slaman / 1989, 1995)
_(Generic copies of countable structures — Annals of Pure and Applied Logic (Vol. 42))_

Here are the specific sections from Kechris's *Classical Descriptive Set Theory* that directly address the missing topological justifications in the proof:

- **Chapter or section number + title**: Section 8: "Polish Groups"
- **Which gap it addresses**: Grader B (Slip 1: Justify $\operatorname{AUT}(\mathcal{B})$ is closed in $S_\infty$)
- **Why**: This section formally defines the topology of pointwise convergence on the symmetric group $S_\infty$. It proves that the basic open (and clopen) neighborhoods of the identity are exactly the pointwise stabilizers of finite sets, and demonstrates that the group of automorphisms of any countable first-order structure forms a closed subgroup of $S_\infty$.

- **Chapter or section number + title**: Section 8: "Polish Groups"
- **Which gap it addresses**: Grader B (Slip 2: Baire argument translating isolated element to identity)
- **Why**: It establishes the foundational topological group property that left-translation maps ($x \mapsto gx$) are homeomorphisms. This provides the exact mechanical justification that if the Baire Category Theorem forces a countable completely metrizable space to contain at least one isolated point, translation homeomorphisms map that exact property to the identity element, proving the group is discrete. 

*(Note: The other gaps flagged by the graders—such as the Ash-Knight-Manasse-Slaman theorem, relative intrinsic computability, and uniform versus pointwise computability bounds—belong entirely to computable structure theory and are outside the scope of Kechris's descriptive set theory text.)*

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [Book] A. S. Kechris / 1995 — Classical Descriptive Set Theory — Springer-Verlag (Graduate Texts in Mathematics, Vol. 156) — IDs: no ID — Provides the necessary topological foundation to prove that $\operatorname{AUT}(\mathcal{B})$ is a closed subspace of $S_\infty$ and translates isolated points to trivial pointwise stabilizers. — search: kechris classical descriptive set theory pdf
  - **Gap addressed:** Grader B critique, Areas for Improvement 1 ("Slip: The proof should explicitly justify that $\operatorname{AUT}(\mathcal B)$ is closed in $S_\infty$") and 2 ("Slip: The Baire argument should explicitly translate an isolated group element to the identity").
  - **Load-bearing piece:** Sections 8 and 9 (Polish Groups and The Symmetric Group) contain the exact theorems showing that automorphism groups of countable structures form closed subgroups of $S_\infty$ and that topological homogeneity translates any isolated point to an isolated identity element.

- [Paper] C. J. Ash, J. F. Knight, M. Manasse, T. A. Slaman / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic (Vol. 42) — IDs: no ID — The foundational paper proving the AKMS definability theorem, offering the exact cone-relativized and parameterized hypotheses needed to legally deduce the $\Sigma^{in}_1$ definition. — search: generic copies of countable structures ash knight pdf
  - **Gap addressed:** Grader A critique, Area for Improvement 2 ("Fallacy: The unjustified quantifier swap... which skips the necessary prerequisites for the AKMS theorem") and Grader B critique, Area for Improvement 4 ("Slip: The exact AKMS theorem should be stated with its cone-relativized and parameterized hypotheses").
  - **Load-bearing piece:** The Main Theorem (Theorem 2.1 / Section 2) details the forcing machinery over generic copies required to convert relative intrinsic $\Sigma^0_1$ properties (with a fixed parameter tuple) into a formal $L_{\omega_1\omega}$ $\Sigma_1$ structural definition.

- [Book] A. Montalbán / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press — IDs: no ID — Rigorously formalizes "copies" via explicit isomorphisms and details how parameters are evaluated and pushed between models, resolving the proof's fallacy regarding structural evaluation. — search: montalban computable structure theory within the arithmetic pdf
  - **Gap addressed:** Grader A critique, Area for Improvement 1 ("Fallacy: Failing to formally quantify over isomorphisms $f: \A \to \B$") and Grader B critique, Area for Improvement 3 ("Slip: The proof should define copies expanded by the parameter tuple $\bar c\cup\bar v$").
  - **Load-bearing piece:** Chapter 1 sets up the strict formal framework for evaluating formulas and pushing explicit parameter evaluations across isomorphic models via explicit domain mappings $f: \A \to \B$.

## SUPPORTING

- [Survey] V. S. Harizanov / 1998 — Pure computable model theory — Handbook of Recursive Mathematics, Vol. 1 (Elsevier) — IDs: no ID — Outlines the model-theoretic boilerplate for defining the image of relations under an explicit isomorphism and reviews relative intrinsic computability. — search: harizanov pure computable model theory pdf
  - *Note:* Provides a solid, condensed handbook-level survey of how parameters and explicit isomorphisms are formally handled in the literature, useful as a general backdrop if Montalbán's exact framing is not used.

## REDUNDANT

- [Book] C. J. Ash, J. F. Knight / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144) — IDs: no ID — Details the generic forcing machinery required to bridge pointwise index existence to uniform definitions, validating the quantifier swap. — search: computable structures hyperarithmetical hierarchy ash knight pdf
  - *Overlap:* Covers the identical definability machinery and forcing framework as the primary Ash-Knight-Manasse-Slaman (1989) load-bearing paper, just in textbook form.

- [Paper] J. Chisholm / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic (Vol. 55) — IDs: no ID — Provides an independent proof of the AKMS theorem, which backstops the central citation and offers an alternative view on managing parameters. — search: effective model theory vs recursive model theory chisholm pdf
  - *Overlap:* Redundant with Ash-Knight-Manasse-Slaman (1989), as it is the independent co-discovery of the identical definability theorem needed for Grader A gap 2 and Grader B gap 4.

## PERIPHERAL

(None)

## UNFAMILIAR

(None)

## Narrower draw 2
## LOAD-BEARING

- [Book] A. S. Kechris / 1995 — Classical Descriptive Set Theory — Springer-Verlag (Graduate Texts in Mathematics, Vol. 156) — IDs: no ID
  - **Addresses:** Grader B critique — Gap 1 ("Slip: The proof should explicitly justify that $\operatorname{AUT}(\mathcal B)$ is closed in $S_\infty$") and Gap 2 ("Slip: The Baire argument should explicitly translate an isolated group element to the identity").
  - **The load-bearing piece:** Chapter 1, Sections 8 (Baire Category) and 9 (Polish Groups) provide the exact topological machinery showing pointwise stabilizers correspond to basic open sets and that a discrete Polish group must have an isolated identity element.

- [Paper] C. J. Ash, J. F. Knight, M. Manasse, T. A. Slaman / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic (Vol. 42) — IDs: no ID
  - **Addresses:** Grader A critique — Gap 2 ("Fallacy: The unjustified quantifier swap from pointwise computability... skipping the necessary prerequisites for the AKMS theorem") and Grader B critique — Gap 4 ("Slip: The exact AKMS theorem should be stated with its cone-relativized and parameterized hypotheses").
  - **The load-bearing piece:** The main definability theorem and its generic forcing proof explicitly bridge how pointwise $\Delta^0_1$ evaluation over a generic sequence yields uniform relative intrinsic $\Sigma^0_1$ status, which then translates to $L_{\omega_1\omega}$ definability.

- [Book] A. Montalbán / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press — IDs: no ID
  - **Addresses:** Grader A critique — Gap 1 ("Fallacy: Failing to formally quantify over isomorphisms $f: \A \to \B$") and Grader B critique — Gap 3 ("Slip: The proof should define copies expanded by the parameter tuple").
  - **The load-bearing piece:** Part I (specifically Chapters 1 and 2) rigorously formalizes the "pulling back" of relations and parameters from generic copies via explicit isomorphisms and details expansions by finite parameter tuples.

## SUPPORTING

- [Survey] V. S. Harizanov / 1998 — Pure computable model theory — Handbook of Recursive Mathematics, Vol. 1 (Elsevier) — IDs: no ID
  - Provides excellent background model-theoretic boilerplate for defining the image of relations under explicit isomorphisms.

## REDUNDANT

- [Book] C. J. Ash, J. F. Knight / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144) — IDs: no ID
  - Overlaps heavily with the 1989 AKMS paper regarding the generic forcing machinery and the proof of the AKMS theorem.

- [Paper] J. Chisholm / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic (Vol. 55) — IDs: no ID
  - Overlaps with the 1989 AKMS paper by providing an independent but functionally identical proof of the main definability theorem.

## PERIPHERAL
(None)

## UNFAMILIAR
(None)

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the foundational works from descriptive set theory and computable structure theory that bear directly on the topological and definability gaps identified by the graders. 

### Descriptive Set Theory (Topology of $S_\infty$ and Automorphism Groups)

To address **Grader B’s slips 1 and 2**, the proof needs standard references for the topology of the symmetric group $S_\infty$, why $\AUT(\mathcal{A})$ is closed, and why Baire Category Theorem translates isolated points into trivial stabilizers. 

**Authors / Year:** A. S. Kechris / 1995
**Title:** Classical Descriptive Set Theory
**Type:** Book / Monograph
**Venue:** Springer-Verlag (Graduate Texts in Mathematics, Vol. 156)
**Main result or relevant chapter/section:** Chapter 1 (Section 8 on Polish Groups, Section 9 on the Baire Category Theorem). Section 8 explicitly constructs the topology of pointwise convergence on $S_\infty$, proves it is a Polish group, establishes that automorphism groups of countable structures are exactly its closed subgroups, and shows that basic open neighborhoods of the identity are pointwise stabilizers of finite tuples.
**Topic needed for this proof:** The topological formalization of $S_\infty(\mathcal{B})$, the proof that $\AUT(\mathcal{B})$ is closed, and the group-theoretic translation of an isolated point to the open identity subgroup.
**Open-access substitute for that topic:** (open-access for topic: Topology of Polish groups and $S_\infty$) — S. Gao / 2008 / Invariant Descriptive Set Theory / author's webpage book draft.
**Connection:** Resolves Grader B’s Scaffolding Questions 1, 2, and 3. Citing this provides the one-line justifications for why $\AUT(\B)$ is a closed topological group and why an isolated element immediately means some finite tuple has a strictly trivial pointwise stabilizer.
**Web search query:** `kechris classical descriptive set theory pdf`
**Confidence (bibliographic):** HIGH

### Computable Structure Theory (AKMS Theorem and Quantifier Swaps)

To address **Grader A’s critical fallacies (1 and 2)** and **Grader B’s slips (3 and 4)**, the proof must bridge the gap between "pointwise computability on a cone" and "uniform structural definability." The shift from $\forall \B \exists e$ to $\exists e \forall \B$ requires generic forcing, which is the core machinery of the AKMS theorem.

**Authors / Year:** A. Montalbán / 2021
**Title:** Computable Structure Theory: Within the Arithmetic
**Type:** Book / Monograph
**Venue:** Cambridge University Press
**Main result or relevant chapter/section:** Chapter 2 (The space of structures) and Chapter 3 (Definability and Forcing). Chapter 3 contains a modern, explicit treatment of forcing over the space of structures to convert pointwise descriptive properties (like a relation being $\Delta^0_1$ across all generic copies) into uniform existential infinitary definability ($\Sigma^{in}_1$). 
**Topic needed for this proof:** The generic forcing argument required to legitimately swap quantifiers from pointwise computability ($\forall \B \exists e$) to uniform relative intrinsic computability ($\exists e \forall \B$) over a cone.
**Open-access substitute for that topic:** (open-access for topic: Computable structure theory forcing and definability) — A. Montalbán / 2021 / Computable Structure Theory: Within the Arithmetic / author's webpage draft.
**Connection:** Directly answers Grader A's Fallacy 2 and Scaffolding Question 2/3. The proof illegally skips the forcing argument that uniformizes the Turing index. Montalbán's text provides the exact generic forcing machinery needed to justify how continuous evaluation on a Polish space forces a uniform index on a cone.
**Web search query:** `montalban computable structure theory within arithmetic pdf`
**Confidence (bibliographic):** HIGH

**Authors / Year:** C. J. Ash, J. Knight / 2000
**Title:** Computable Structures and the Hyperarithmetical Hierarchy
**Type:** Book / Monograph
**Venue:** Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144)
**Main result or relevant chapter/section:** Chapter 10 ("Relatively intrinsically $\Sigma^0_\alpha$ relations"). This chapter thoroughly defines how structures are expanded by finite parameters, how relations are transported via explicit isomorphisms $f: \mathcal{A} \to \mathcal{B}$, and provides the canonical proof of the AKMS theorem.
**Topic needed for this proof:** The rigorous formalization of transporting parameter tuples via an explicit isomorphism $f$, and the exact parameterized statement of the AKMS theorem.
**Open-access substitute for that topic:** (open-access for topic: Transporting relations across isomorphic copies and the AKMS theorem) — V. S. Harizanov / 1998 / Pure Computable Model Theory / Handbook of Recursive Mathematics.
**Connection:** Resolves Grader A’s Fallacy 1 and Grader B’s Slips 3, 4, and 5. It shows exactly how to define the image of relation $R$ in an isomorphic structure $\mathcal{B}$ using the isomorphism $f$, explicitly tracking the expanded parameters $\bar{c} \cup \bar{v}$.
**Web search query:** `ash knight computable structures hyperarithmetical pdf`
**Confidence (bibliographic):** HIGH

**Authors / Year:** C. J. Ash, J. Knight, M. Manasse, T. Slaman / 1989
**Title:** Generic copies of countable structures
**Type:** Paper
**Venue:** Annals of Pure and Applied Logic (Vol. 42)
**Main result or relevant chapter/section:** The original foundational paper proving the AKMS definability theorem: A relation $R$ on a countable structure is relatively intrinsically $\Sigma^0_1$ (c.e.) on a cone if and only if it is definable by a computable $\Sigma_1$ infinitary formula using a finite set of parameters.
**Topic needed for this proof:** The canonical citation for the theorem invoked in Step 5 of the proof.
**Open-access substitute for that topic:** N/A (The original paper is widely hosted, but Harizanov's survey above covers the exact statement).
**Connection:** Provides the foundational citation requested by the Verification grader. Stating the specific hypotheses from this paper will force the author to properly relativize the cone and name the parameters.
**Web search query:** `ash knight manasse slaman generic copies pdf`
**Confidence (bibliographic):** HIGH

**Authors / Year:** V. S. Harizanov / 1998
**Title:** Pure computable model theory
**Type:** Survey / Handbook chapter
**Venue:** Handbook of Recursive Mathematics, Vol. 1 (Elsevier)
**Main result or relevant chapter/section:** A comprehensive survey that explicitly details the "boilerplate" for relative intrinsic computability. It carefully spells out the formalisms of how domains, relations, and automorphisms are evaluated when passing from an abstract structure $\mathcal{A}$ to a specific model $\mathcal{B}$ via an isomorphism $f$.
**Topic needed for this proof:** Formal model-theoretic boilerplate for defining the image of a relation under an explicit isomorphism.
**Connection:** Directly addresses Grader A's first scaffolding question: "How must you formally define the image of a relation $R$ in an isomorphic structure $M'$ using an explicit isomorphism $f$?"
**Web search query:** `harizanov pure computable model theory pdf`
**Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and topic-keyed substitutes that directly address the gaps in the NO proof, particularly the topological behavior of $\operatorname{AUT}(\mathcal{B})$ and the modern computable structure theory (CST) formalities for copies, parameters, and the AKMS theorem.

- **Authors / Year:** A.S. Kechris / 1995
- **Title:** Classical Descriptive Set Theory
- **Type:** Book
- **Venue:** Springer (Graduate Texts in Mathematics, Vol. 156)
- **Main result or relevant chapter/section:** Chapter I (Sections 8 and 9) develops the topology of Polish groups and $S_\infty$. It contains the explicit proofs that $\operatorname{AUT}(\mathcal{M})$ for a countable structure is exactly a closed subgroup of $S_\infty$ (under the pointwise convergence topology), and the Baire Category Theorem application showing that a countable Polish space must contain an isolated point.
- **Topic needed for this proof:** The topological formalization of $S_\infty$ showing that closed subgroups are Polish, basic open neighborhoods correspond to pointwise stabilizers of finite sets, and countable Polish spaces have isolated points.
- **Open-access substitute for that topic:** (open-access for topic: Polish spaces and the descriptive set theory of topological groups) — S. Gao / 2008 / Invariant Descriptive Set Theory / book draft (homepages or lecture notes from various universities often host drafts of this or similar DST notes).
- **Connection:** This book is the mandatory citation for resolving Grader B’s Slips 1 and 2. It rigorously justifies why $\operatorname{AUT}(\mathcal{B})$ is a closed Polish subspace, why a countable completely metrizable space must have an isolated point, and how basic open neighborhoods mapping to finite stabilizers allow you to translate an isolated point (a singleton in the topology) to a trivial pointwise stabilizer for a specific finite tuple.
- **Web search query:** `classical descriptive set theory kechris pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** C.J. Ash, J.F. Knight, M. Manasse, T.A. Slaman / 1989
- **Title:** Generic copies of countable structures
- **Type:** Paper
- **Venue:** Annals of Pure and Applied Logic (Vol. 42)
- **Main result or relevant chapter/section:** Proves the "AKMS Theorem" (sometimes called the Ash-Knight-Manasse-Slaman definability theorem), which equates a relation being relatively intrinsically $\Sigma^0_\alpha$ on a cone with it being definable by a computable infinitary $\Sigma_\alpha$ formula ($L_{\omega_1\omega}$) using a finite parameter tuple.
- **Topic needed for this proof:** The exact formal statement of the AKMS theorem linking relative intrinsic computability (on a cone) to infinitary definability, specifically how parameters are bound across generic copies.
- **Connection:** Addresses Grader B’s Slip 4. The proof references this theorem loosely, but must cite its precise cone-relativized and parameterized hypotheses to legally deduce the $\Sigma^{in}_1$ definition. 
- **Web search query:** `generic copies of countable structures ash knight pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** A. Montalbán / 2021
- **Title:** Computable Structure Theory: Within the Arithmetic
- **Type:** Book
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** Part I (specifically the initial chapters on "Copies and Definability") strictly formalizes what a "copy" of a structure means. It defines a copy of $\mathcal{A}$ via an explicit isomorphism $f: \mathcal{A} \to \mathcal{B}$ where the domain of $\mathcal{B}$ is $\omega$. It defines the pullback of relations (e.g., $R^\mathcal{B} = f(R^\mathcal{A})$) and how parameters $\bar{c}$ are evaluated in $\mathcal{B}$ strictly as $f(\bar{c})$. 
- **Topic needed for this proof:** The rigorous formalization of "copies" via explicit isomorphisms and how finite parameter tuples and relations are pushed forward / pulled back between abstract structures.
- **Open-access substitute for that topic:** (open-access for topic: early chapters defining copies, parameter transport, and structural complexity) — A. Montalbán / 2021 / Computable Structure Theory: Within the Arithmetic / book draft available on author's Berkeley webpage.
- **Connection:** Directly resolves Grader A’s Fallacy 1 and Grader B’s Slip 3. The grader rightly points out that in an abstract structure $\mathcal{B}$, "$\bar{c}^\mathcal{B}$" is mathematically undefined without fixing an isomorphism $f: \mathcal{A} \to \mathcal{B}$. You must write $\pi^\mathcal{B}(f(\bar{c})) = f(\bar{v})$. Montalbán's text provides the modern, rigorous template for this notation.
- **Web search query:** `computable structure theory within the arithmetic montalban pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** C.J. Ash, J. Knight / 2000
- **Title:** Computable Structures and the Hyperarithmetical Hierarchy
- **Type:** Monograph
- **Venue:** Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144)
- **Main result or relevant chapter/section:** The chapters on forcing in computable structure theory. It details the precise mechanism (often using Cohen generics) for how pointwise computability ($\forall \mathcal{B} \exists e$) is elevated to uniform computability ($\exists e \forall \mathcal{B}$) over generic copies. 
- **Topic needed for this proof:** The forcing mechanism required to bridge pointwise index existence with a uniform enumeration across all generic copies.
- **Open-access substitute for that topic:** (open-access for topic: forcing and uniform computability in model theory) — V.S. Harizanov / 1998 / Pure computable model theory / Handbook of Recursive Mathematics chapter.
- **Connection:** This is the core reference for Grader A’s Fallacy 2. The jump from "every generic copy has an index" to "there is a single index defining the relation uniformly" requires a forcing step that the proof skips. If a property requires a $\Pi^0_2$ verification check to select the correct Turing index, you cannot unconditionally assemble it into a uniform algorithmic reduction without this topological/forcing guarantee. 
- **Web search query:** `pure computable model theory harizanov pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** J. Chisholm / 1990
- **Title:** Effective model theory vs. recursive model theory
- **Type:** Paper
- **Venue:** Journal of Symbolic Logic (Vol. 55)
- **Main result or relevant chapter/section:** An independent proof of the AKMS theorem, specifically emphasizing the difference between effective (pointwise) model theory and recursive (uniform/definability) model theory.
- **Topic needed for this proof:** The independent formulation of the definability theorem for relatively intrinsically c.e. relations.
- **Connection:** Since the proof notes the theorem was "independently Chisholm", citing this ensures full bibliographic compliance for the AKMS/Chisholm theorem and offers a slightly different, highly constructive proof perspective on managing parameters.
- **Web search query:** `effective model theory vs recursive model theory chisholm pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and open-access substitutes that directly address the gaps flagged by the graders, particularly regarding the topology of the symmetric group, the formalities of parameter transportation across isomorphic copies, and the exact hypotheses of the AKMS theorem.

- **Authors / Year:** C. J. Ash, J. F. Knight, M. Manasse, T. A. Slaman / 1989
- **Title:** Generic copies of countable structures
- **Type:** paper
- **Venue:** Annals of Pure and Applied Logic 42
- **External IDs:** 
- **Main result or relevant chapter/section:** Proves the exact theorem that a relation is relatively intrinsically $\Sigma^0_1$ (computably enumerable) on a cone if and only if it is definable by a computable infinitary $\Sigma_1$ formula ($L_{\omega_1\omega}^c$) with finitely many parameters.
- **Topic needed for this proof:** The precise cone-relativized formulation of the AKMS definability theorem, and the requirement that the relation must be semantically invariant under automorphisms fixing the parameters.
- **Open-access substitute for that topic:** (open-access for topic: Proof and exact statement of the AKMS definability theorem) — Antonio Montalbán / 2021 / Computable Structure Theory: Within the Arithmetic (Draft) / UC Berkeley personal webpage
- **Connection:** Directly addresses Grader B’s Critique 4 (the exact AKMS theorem with its cone-relativized and parameterized hypotheses) and Critique 5 (justifying the invariance of $R$).
- **Web search query:** `generic copies of countable structures ash knight pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Alexander S. Kechris / 1995
- **Title:** Classical Descriptive Set Theory
- **Type:** book
- **Venue:** Springer-Verlag (Graduate Texts in Mathematics 156)
- **External IDs:** 
- **Main result or relevant chapter/section:** Sections 8 and 9 cover Polish groups, specifically the topology of the symmetric group $S_\infty(\omega)$. It establishes that basic open neighborhoods of the identity are pointwise stabilizers of finite sets, and proves that Baire's Category Theorem forces any countable completely metrizable space to have isolated points.
- **Topic needed for this proof:** The topological formalization of $S_\infty(A)$, the proof that closed subgroups of $S_\infty$ are Polish, and the explicit translation of an isolated point in a topological group to an isolated identity.
- **Open-access substitute for that topic:** (open-access for topic: Polish groups, Baire Category Theorem, and the topology of $S_\infty$) — Arnold W. Miller / Descriptive Set Theory and Forcing / author's personal webpage
- **Connection:** Addresses Grader B’s Critiques 1 and 2 (justifying $\operatorname{AUT}(\B)$ is closed in $S_\infty$ and explicitly translating an isolated group element to the isolated identity element using the homeomorphism of left-multiplication).
- **Web search query:** `kechris classical descriptive set theory pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** Antonio Montalbán / 2021
- **Title:** Computable Structure Theory: Within the Arithmetic
- **Type:** book
- **Venue:** Cambridge University Press
- **External IDs:** 
- **Main result or relevant chapter/section:** Chapters 1 and 2 rigorously treat the transportation of relations and parameters across copies using explicit formal isomorphisms $f: \A \to \B$, avoiding the ambiguity of abstractly "evaluating" an unnamed parameter. It also carefully distinguishes pointwise computability from uniform computability.
- **Topic needed for this proof:** The formal notation and mechanism for defining copies expanded by parameter tuples $\bar{c} \cup \bar{v}$ and pushing those parameters through an isomorphism $f$.
- **Open-access substitute for that topic:** (open-access for topic: Parameter transport and isomorphisms in computable copies) — Antonio Montalbán / 2021 / Computable Structure Theory: Within the Arithmetic (Draft) / UC Berkeley personal webpage (`math.berkeley.edu/~antonio/...`)
- **Connection:** Explicitly closes Grader A’s Critique 1 (the missing formal quantification over isomorphisms $f: \A \to \B$) and Grader B’s Critique 3 (defining copies expanded by the parameter tuple).
- **Web search query:** `montalban computable structure theory within the arithmetic pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** C. J. Ash, J. F. Knight / 2000
- **Title:** Computable Structures and the Hyperarithmetical Hierarchy
- **Type:** book
- **Venue:** Elsevier (Studies in Logic and the Foundations of Mathematics 144)
- **External IDs:** 
- **Main result or relevant chapter/section:** Chapters 10 and 11 develop the forcing machinery required to bridge the gap between "for all generic copies there exists a Turing index" (pointwise) to "there exists a uniform syntactic definition" (uniform).
- **Topic needed for this proof:** The metatheorem/forcing logic explaining why you cannot simply swap $\forall \B \exists e$ to $\exists e \forall \B$ without invoking the invariance of the relation to bypass the uncomputable $\Pi^0_2$ index verification.
- **Open-access substitute for that topic:** (open-access for topic: Forcing in computable structure theory to bridge pointwise indices to uniform definitions) — B. F. Csima / 2023 / Computable Structure Theory Lecture Notes / University of Waterloo webpage
- **Connection:** Crucial for Grader A’s Critique 2 and Scaffolding Question 3 (the "fallacy" of the quantifier swap from pointwise to uniform computability). The proof skips the forcing justification that allows AKMS to legally execute this swap. 
- **Web search query:** `computable structures hyperarithmetical hierarchy ash knight pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** John Chisholm / 1990
- **Title:** Effective Model Theory vs. Recursive Model Theory
- **Type:** paper
- **Venue:** Journal of Symbolic Logic 55
- **External IDs:** 
- **Main result or relevant chapter/section:** Provides the independent, simultaneous proof of the AKMS theorem, often cited alongside it. Chisholm's formulation is sometimes preferred for highlighting the step-by-step passage from semantic structural constraints (isolated bases) to syntactic formulas.
- **Topic needed for this proof:** The independent verification of the passage from relative intrinsic computability to $\Sigma^{in}_1$ definability over finite bases.
- **Connection:** Backstops the AKMS citation (Step 5 in the near-miss proof) and provides an alternative phrasing that often clarifies Grader B's Scaffolding Question 5 (how relative intrinsic c.e.-ness forces existential infinitary definability).
- **Web search query:** `effective model theory vs recursive model theory chisholm pdf`
- **Confidence (bibliographic):** HIGH
