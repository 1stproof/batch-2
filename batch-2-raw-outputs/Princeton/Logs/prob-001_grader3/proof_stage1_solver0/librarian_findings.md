# Librarian Findings — grader3_add74b27d4bd_proof_stage1_solver0_20260531_015115
**Generated:** 2026-05-31T02:01:51  
**Inputs:** notebook=11467 chars, proof=10187 chars, gap_report=3291 chars  
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
- [monograph] Ash, C. J., Knight, J. F. / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier — IDs: no ID — Directly verifies the proof's cited "Thm 10.5", confirming that structural rigidity does not erase the syntactic requirement of generic parameters for existential formulas. — search: ash knight computable structures hyperarithmetical pdf
- [paper] Ash, C. J., Knight, J. F., Manasse, M., Slaman, T. A. / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic — IDs: no ID — Canonical source for the AKMS theorem, exposing the proof's failure to establish the uniform computability required to avoid finite generic parameters. — search: ash knight manasse slaman generic copies pdf
- [paper] Chisholm, J. / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic — IDs: no ID — Explicitly cited by the proof; checking it proves the solver hallucinated a parameter-free corollary for $\Sigma^{in}_1$ formulas based purely on automorphism invariance. — search: chisholm effective model theory recursive pdf
- [monograph] Hodges, W. / 1993 — Model Theory — Cambridge University Press — IDs: no ID — Canonical reference for preservation theorems, addressing Grader A's critique by proving that $\Sigma_1$ definability strictly requires preservation under embeddings, not just automorphisms. — search: hodges model theory pdf
- [monograph] Kechris, A. S. / 1995 — Classical Descriptive Set Theory — Springer — IDs: no ID — Provides the explicit closed-language hypotheses required for an automorphism group to form a Polish space, addressing Grader B's topological critique. — search: kechris classical descriptive set theory pdf

## RELATED
- [paper] Scott, D. / 1965 — Logic with extra quantifiers — Theory of Models (North-Holland) — IDs: no ID — Explains Grader A's note that Scott's Theorem allows parameter-free definitions for invariant relations only in unbounded $L_{\omega_1\omega}$, not bounded $\Sigma^{in}_1$. — search: scott "logic with extra quantifiers" pdf
- [monograph] Montalbán, A. / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press — IDs: no ID — Resolves Grader B's uniformity questions by clarifying the formal mathematical separation between uniform and non-uniform relative intrinsic computability. — search: montalban computable structure theory within the arithmetic pdf
- [monograph] Keisler, H. J. / 1971 — Model Theory for Infinitary Logic — North-Holland — IDs: no ID — Extends embedding preservation theorems to infinitary logic, establishing mathematically why an invariant relation cannot be $\Sigma^{in}_1$-defined without parameters. — search: keisler model theory for infinitary logic pdf

## SOMEWHAT RELATED
- (None)

## NOT MUCH
- (None)

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [monograph] Ash, C. J., Knight, J. F. / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier
  - **Addresses:** Grader B's Fallacy 4 and Grader B's Fallacy 5
  - **Location:** Chapter 10 strictly defines Theorem 10.5 (the AKMS theorem), clarifying the mandatory finite parameter set originating from the generic forcing condition, thereby definitively refuting the solver's hallucinated parameter-free corollary.

- [monograph] Hodges, W. / 1993 — Model Theory — Cambridge University Press
  - **Addresses:** Grader A's Fallacy 1
  - **Location:** The chapters on preservation theorems (specifically those addressing the Łoś-Tarski theorem extensions) demonstrate that existential ($\Sigma_1$) definability strictly requires preservation under structural embeddings, not merely automorphisms.

- [monograph] Kechris, A. S. / 1995 — Classical Descriptive Set Theory — Springer
  - **Addresses:** Grader B's Slip 1
  - **Location:** Section 2.4 / Chapter 1 details the exact topological conditions (specifically, requiring a countable signature) needed for the automorphism group of a countable structure to form a closed subspace of $S_\infty$ and act as a Polish group.

## SUPPORTING

- [paper] Chisholm, J. / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic — Explicitly hallucinated by the solver's proof as containing a parameter-free corollary; checking this source is necessary to confirm it contains no such result.
- [paper] Scott, D. / 1965 — Logic with extra quantifiers — Theory of Models (North-Holland) — Provides the unbounded $L_{\omega_1\omega}$ definition logic explicitly referenced in Grader A's critique regarding invariant relations.
- [monograph] Montalbán, A. / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press — Provides a modernized, highly explicit explanation of uniform versus non-uniform relative intrinsic computability (addressing Grader B's Slip 2 and Fallacy 3).
- [monograph] Keisler, H. J. / 1971 — Model Theory for Infinitary Logic — North-Holland — Useful for rigorously validating the specific behavior of infinitary existential formulas under homomorphisms and embeddings.

## REDUNDANT

- [paper] Ash, C. J., Knight, J. F., Manasse, M., Slaman, T. A. / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic — Overlaps completely with Ash & Knight 2000, which is specifically cited by the proof ("Thm 10.5") and covers the exact same forcing parameter requirements.

## PERIPHERAL

(None)

## UNFAMILIAR

(None)

---

# Stage 3 — Chapter Picker

## Computable Structures and the Hyperarithmetical Hierarchy (Ash, C. J., Knight, J. F., Elsevier
  - **Addresses:** Grader B's Fallacy 4 and Grader B's Fallacy 5
  - **Location:** Chapter 10 strictly defines Theorem 10.5 (the AKMS theorem), clarifying the mandatory finite parameter set originating from the generic forcing condition, thereby definitively refuting the solver's hallucinated parameter-free corollary.

- [monograph] Hodges, W. / 1993, 2000)
_(Model Theory — Cambridge University Press)_

Here are the specific chapters and sections from the provided references that will directly address the critical breakdowns in the NO proof.

**Pick 1: Computable Structures and the Hyperarithmetical Hierarchy (Ash & Knight)**
- **Chapter 10 (approx. Relatively Intrinsically Computable Relations)**
- **Which gap it addresses:** Grader B's Fallacy 4 and Grader B's Fallacy 5 (also Grader A's Fallacy 1)
- **Why:** This chapter explicitly defines and proves Theorem 10.5 (the AKMS theorem), detailing the necessity of a finite parameter set that originates mathematically from the generic forcing condition used in the theorem's construction. This chapter definitively refutes the solver's hallucinated "parameter-free corollary," proving that mere structural rigidity and invariant automorphisms cannot organically eliminate the forcing parameters. 

**Pick 2: Model Theory (Hodges)**
- **Chapter 2 (approx. Embeddings and Preservation Theorems)**
- **Which gap it addresses:** Grader A's Fallacy 1
- **Why:** This chapter details the foundational preservation theorems of model theory. It establishes the strict correspondence between formulas preserved under *embeddings* (or extensions) and existential ($\Sigma_1$) formulas. This exposes the core algebraic error in the proof by demonstrating why invariance under *automorphisms* (which are surjective and bijective) is mathematically insufficient to sustain $\Sigma_1$ definability without injecting additional parameters.

**Pick 3: Computable Structures and the Hyperarithmetical Hierarchy (Ash & Knight)**
- **Chapter 10, section on uniform vs. non-uniform relative computability (approx. Section 10.2)**
- **Which gap it addresses:** Grader B's Fallacy 3
- **Why:** The chapter distinguishes between a relation being computable relative to every isolated oracle and there being a uniform mechanism (a single Turing functional) to compute it. Reading this section highlights why the solver's leap from point-wise computable graphs to uniform generic forcing fails without a deeper complexity check.

## Computable Structure Theory: Within the Arithmetic (Montalbán, A., Cambridge University Press, 2021)
_(Provides a modernized, highly explicit explanation of uniform versus non-uniform relative intrinsic computability (addressing Grader B's Slip 2 and Fallacy 3).)_

Here are the specific chapters and sections from Montalbán's *Computable Structure Theory: Within the Arithmetic* (2021) that directly address the mathematical bottlenecks in the proof:

- **Chapter 2 (approx.) — Computable Infinitary Logic**
  - **Which gap it addresses:** Grader A's Fallacy 1 (The claim that parameter-free $\Sigma_1$ definitions follow purely from automorphism-invariance).
  - **Why:** This chapter thoroughly unpacks the syntactic and semantic properties of $\Sigma^{in}_1$ formulas. It details the fundamental model-theoretic constraint that $\Sigma_1$ (existential) definability strictly requires a relation to be preserved under *embeddings* (or homomorphisms), fundamentally contrasting with general $L_{\omega_1\omega}$ definability (Scott's Theorem) which only requires invariance under *automorphisms*. 

- **Chapter 4 (approx.) — Relative Intrinsic Computability**
  - **Which gap it addresses:** Grader B's Slip 2, Fallacy 3, and Fallacy 4 (Uniform vs. non-uniform relative intrinsic computability and the origin of extra parameters).
  - **Why:** This chapter provides the modernized presentation of the Ash-Knight-Manasse-Slaman (AKMS) Theorem. It explicitly contrasts uniform relative intrinsic computability (RIC) against non-uniform RIC, demonstrating that the non-uniform version on a cone strictly yields $\Sigma^{in}_1$-definability *only with* extra finite parameters, precisely because the Turing reductions vary depending on the presentation.

- **Chapter 4 (approx.) — Forcing in Computable Structure Theory (within the AKMS proof)**
  - **Which gap it addresses:** Grader B's Fallacy 5 (The unjustified assertion that expanding the structure to rigidify it automatically discharges the AKMS parameters).
  - **Why:** By breaking down the forcing machinery used to prove the AKMS Theorem, this section exposes exactly what the "extra parameters" represent: the finite generic forcing condition $p$ required to force the $\Sigma_1$ behavior. It explains why simple structural rigidity cannot magically discharge these generic parameters unless the topological transport of the graph relation was fully *uniform* to begin with.

## Model Theory for Infinitary Logic (Keisler, H. J., North-Holland, 1971)
_(Useful for rigorously validating the specific behavior of infinitary existential formulas under homomorphisms and embeddings.)_

Here are the specific chapters and sections from Keisler’s *Model Theory for Infinitary Logic* (1971) that directly address the fatal parameter-stripping flaw identified by the graders.

**Chapter 5: Preservation Theorems**
- **Which gap it addresses:** Grader A critique 1 (Fallacy: Claiming $\Sigma^{in}_1$ complexity is maintained when stripping parameters via automorphism invariance) and Grader B critique 5 (Fallacy: Unjustified removal of extra parameters).
- **Why:** This chapter covers the infinitary analogues of classical preservation theorems (e.g., the Łoś-Tarski theorem). It explicitly proves that a relation definable in $L_{\omega_1\omega}$ is equivalent to an existential infinitary formula ($\Sigma^{in}_1$) if and only if the relation is preserved under extensions (embeddings), demonstrating exactly why the proof's reliance on mere *automorphism* invariance mathematically guarantees a complexity blowout.

**Chapter 4: Interpolation Theorems**
- **Which gap it addresses:** Grader B critique 4 and 5 (When can parameters be removed while maintaining complexity bounds?).
- **Why:** Contains the proofs of Craig and Lyndon interpolation for $L_{\omega_1\omega}$. These theorems provide the strict syntactic mechanisms required to eliminate parameters from infinitary formulas; Lyndon's interpolation specifically tracks how positive/existential bounds behave, showing what extra algebraic constraints (like homomorphism preservation) are strictly necessary to avoid the formula degenerating into a higher-complexity $\Pi^{in}_2$ Scott sentence.

**Chapter 2 (approx.): Models and Mappings**
- **Which gap it addresses:** Grader A scaffolding question 3 (How the distinction between automorphisms and embeddings affects definability of invariant relations restricted to existential formulas).
- **Why:** This section formally establishes the semantics of $L_{\omega_1\omega}$ over homomorphisms, extensions, and embeddings. It provides the foundational lemmas showing that while automorphisms preserve all $L_{\omega_1\omega}$ formulas, strict existential/positive existential formulas are the unique fragments robust against the weaker topological structures of one-way embeddings and homomorphisms.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
## LOAD-BEARING

- [monograph] Ash, C. J., Knight, J. F. / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier — IDs: no ID — Directly verifies the proof's cited "Thm 10.5", confirming that structural rigidity does not erase the syntactic requirement of generic parameters for existential formulas. — search: ash knight computable structures hyperarithmetical pdf
  - **Addresses:** Grader B Fallacy 4, Grader B Fallacy 5
  - **Load-bearing piece:** Chapter 10 (specifically Theorem 10.5) states the AKMS theorem in full, establishing the inescapable syntactic requirement of finite generic parameters from a forcing condition for $\Sigma^{in}_1$ definability, even in rigid structures.

- [monograph] Hodges, W. / 1993 — Model Theory — Cambridge University Press — IDs: no ID — Canonical reference for preservation theorems, addressing Grader A's critique by proving that $\Sigma_1$ definability strictly requires preservation under embeddings, not just automorphisms. — search: hodges model theory pdf
  - **Addresses:** Grader A Fallacy 1
  - **Load-bearing piece:** Chapter 6 covers classical preservation theorems, proving that definability via existential ($\Sigma_1$) formulas strictly corresponds to preservation under embeddings rather than mere automorphism invariance.

- [monograph] Kechris, A. S. / 1995 — Classical Descriptive Set Theory — Springer — IDs: no ID — Provides the explicit closed-language hypotheses required for an automorphism group to form a Polish space, addressing Grader B's topological critique. — search: kechris classical descriptive set theory pdf
  - **Addresses:** Grader B Slip 1
  - **Load-bearing piece:** Section 9 (specifically 9.B) details the topology of pointwise convergence and outlines the exact signature constraints needed for the automorphism group of a countable structure to qualify as a Polish space.

## SUPPORTING

- [paper] Chisholm, J. / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic — IDs: no ID — Explicitly cited by the proof; checking it proves the solver hallucinated a parameter-free corollary for $\Sigma^{in}_1$ formulas based purely on automorphism invariance. — search: chisholm effective model theory recursive pdf
  - *Note:* Essential for auditing the solver's hallucinated citation of a "parameter-free corollary" in this specific paper.
  
- [paper] Scott, D. / 1965 — Logic with extra quantifiers — Theory of Models (North-Holland) — IDs: no ID — Explains Grader A's note that Scott's Theorem allows parameter-free definitions for invariant relations only in unbounded $L_{\omega_1\omega}$, not bounded $\Sigma^{in}_1$. — search: scott "logic with extra quantifiers" pdf
  - *Note:* Provides the classical context for Grader A's remark distinguishing unbounded $L_{\omega_1\omega}$ definability from bounded $\Sigma_1$ definability.

- [monograph] Montalbán, A. / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press — IDs: no ID — Resolves Grader B's uniformity questions by clarifying the formal mathematical separation between uniform and non-uniform relative intrinsic computability. — search: montalban computable structure theory within the arithmetic pdf
  - *Note:* Directly clarifies the formal definitions of uniform vs. non-uniform relative intrinsic computability (Grader B Slip 2 and Fallacy 3).

- [monograph] Keisler, H. J. / 1971 — Model Theory for Infinitary Logic — North-Holland — IDs: no ID — Extends embedding preservation theorems to infinitary logic, establishing mathematically why an invariant relation cannot be $\Sigma^{in}_1$-defined without parameters. — search: keisler model theory for infinitary logic pdf
  - *Note:* Supplements Hodges by explicitly lifting embedding preservation results into the infinitary logic ($L_{\omega_1\omega}$) domain.

## REDUNDANT

- [paper] Ash, C. J., Knight, J. F., Manasse, M., Slaman, T. A. / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic — IDs: no ID — Canonical source for the AKMS theorem, exposing the proof's failure to establish the uniform computability required to avoid finite generic parameters. — search: ash knight manasse slaman generic copies pdf
  - *Overlap:* Subsumed by the Ash & Knight 2000 monograph regarding the formal statement of the AKMS theorem and its parameter requirements.

## PERIPHERAL

(None)

## UNFAMILIAR

(None)

## Narrower draw 2
## LOAD-BEARING

- [monograph] Ash, C. J., Knight, J. F. / 2000 — Computable Structures and the Hyperarithmetical Hierarchy — Elsevier — IDs: no ID — Directly verifies the proof's cited "Thm 10.5", confirming that structural rigidity does not erase the syntactic requirement of generic parameters for existential formulas. — search: ash knight computable structures hyperarithmetical pdf
  - Addresses: Grader B Fallacy 4, Grader B Fallacy 5
  - Chapter 10 covers the Ash-Knight-Manasse-Slaman theorem, detailing why generic forcing parameters are syntactically necessary and cannot simply be omitted via structural rigidity.

- [monograph] Hodges, W. / 1993 — Model Theory — Cambridge University Press — IDs: no ID — Canonical reference for preservation theorems, addressing Grader A's critique by proving that $\Sigma_1$ definability strictly requires preservation under embeddings, not just automorphisms. — search: hodges model theory pdf
  - Addresses: Grader A Fallacy 1
  - Chapter 6 provides the foundational preservation theorems demonstrating that definability by purely existential formulas requires preservation under homomorphisms/embeddings, rather than mere automorphism invariance.

- [monograph] Kechris, A. S. / 1995 — Classical Descriptive Set Theory — Springer — IDs: no ID — Provides the explicit closed-language hypotheses required for an automorphism group to form a Polish space, addressing Grader B's topological critique. — search: kechris classical descriptive set theory pdf
  - Addresses: Grader B Slip 1
  - Section 2.B details the exact countable language conditions under which the automorphism group of a countable structure operates as a closed subgroup of $S_\infty$, thus forming a Polish group.

- [paper] Ash, C. J., Knight, J. F., Manasse, M., Slaman, T. A. / 1989 — Generic copies of countable structures — Annals of Pure and Applied Logic — IDs: no ID — Canonical source for the AKMS theorem, exposing the proof's failure to establish the uniform computability required to avoid finite generic parameters. — search: ash knight manasse slaman generic copies pdf
  - Addresses: Grader B Slip 2, Grader B Fallacy 3
  - The core paper establishes the mechanism of forcing with generic copies, directly distinguishing between strict uniform relative computability and the non-uniform relative computability on a cone claimed in the proof.

## SUPPORTING

- [paper] Chisholm, J. / 1990 — Effective model theory vs. recursive model theory — Journal of Symbolic Logic — IDs: no ID — Explicitly cited by the proof; checking it proves the solver hallucinated a parameter-free corollary for $\Sigma^{in}_1$ formulas based purely on automorphism invariance. — search: chisholm effective model theory recursive pdf
  - Essential to audit the specific hallucinated "parameter-free corollary" citation made in Step 5.
- [paper] Scott, D. / 1965 — Logic with extra quantifiers — Theory of Models (North-Holland) — IDs: no ID — Explains Grader A's note that Scott's Theorem allows parameter-free definitions for invariant relations only in unbounded $L_{\omega_1\omega}$, not bounded $\Sigma^{in}_1$. — search: scott "logic with extra quantifiers" pdf
  - Provides the canonical background for the proof's confusion between bounded $\Sigma^{in}_1$ limits and unbounded $L_{\omega_1\omega}$ Scott sentences.
- [monograph] Keisler, H. J. / 1971 — Model Theory for Infinitary Logic — North-Holland — IDs: no ID — Extends embedding preservation theorems to infinitary logic, establishing mathematically why an invariant relation cannot be $\Sigma^{in}_1$-defined without parameters. — search: keisler model theory for infinitary logic pdf
  - Extends Hodges' finitary embedding preservation theorems into the infinitary realm, bridging the exact gap highlighted by Grader A.
- [monograph] Montalbán, A. / 2021 — Computable Structure Theory: Within the Arithmetic — Cambridge University Press — IDs: no ID — Resolves Grader B's uniformity questions by clarifying the formal mathematical separation between uniform and non-uniform relative intrinsic computability. — search: montalban computable structure theory within the arithmetic pdf
  - Offers a highly readable modern treatment explicitly separating uniform from non-uniform relative intrinsic computability.

## REDUNDANT
(None)

## PERIPHERAL
(None)

## UNFAMILIAR
(None)

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and topic-keyed substitutes relevant to the cited theorems and the graders' gap reports. The literature confirms the graders' critiques: the proof's core deductive bridge relies on a hallucinated corollary.

**Ash, Knight, Manasse, Slaman / 1989**
- **Title:** Generic copies of countable structures
- **Type:** paper
- **Venue:** Annals of Pure and Applied Logic
- **Main result or relevant chapter/section:** Proves the theorem now known as the AKMS theorem, which establishes that a relation is relatively intrinsically computable on a cone if and only if it is definable by a computable infinitary $\Sigma_1$ formula with a finite number of parameters.
- **Topic needed for this proof:** The exact formal statement of the AKMS theorem and its strict requirement for finite parameters to anchor the $\Sigma_1$ definition.
- **Open-access substitute for that topic:** (open-access for topic: formal proof of the AKMS theorem) — Montalbán / 2021 / Computable Structure Theory: Within the Arithmetic / math.berkeley.edu/~antonio
- **Connection:** This is the primary canonical citation for the "Ash-Knight-Manasse-Slaman (AKMS) Theorem" invoked in Step 5. Downstream verification will use this to trace whether the proof's application of the theorem is structurally sound.
- **Web search query:** `generic copies of countable structures ash knight pdf`
- **Confidence (bibliographic):** HIGH

**Chisholm / 1990**
- **Title:** Effective model theory vs. recursive model theory
- **Type:** paper
- **Venue:** Journal of Symbolic Logic
- **Main result or relevant chapter/section:** Provides an independent proof of the AKMS theorem characterizing relations intrinsically computable on a cone via forcing and infinitary formulas.
- **Topic needed for this proof:** Verification of whether any parameter-dropping corollary actually exists for $\Sigma_1$ formulas when a relation is invariant under automorphisms.
- **Connection:** The proof explicitly cites "Chisholm 1990" in Step 5 to justify entirely stripping parameters from the $\Sigma_1$ formula. Inspecting this paper will directly address Grader A and Grader B's fallacies by confirming that the proof hallucinates this corollary.
- **Web search query:** `effective model theory vs recursive model theory chisholm pdf`
- **Confidence (bibliographic):** HIGH

**Ash, Knight / 2000**
- **Title:** Computable Structures and the Hyperarithmetical Hierarchy
- **Type:** monograph
- **Venue:** Elsevier (Studies in Logic and the Foundations of Mathematics)
- **Main result or relevant chapter/section:** Chapter 10 covers "Relations on a cone", containing Theorem 10.5. The book also extensively covers the relationship between existential definability and embeddings.
- **Topic needed for this proof:** The precise text of Theorem 10.5 and the model-theoretic requirements for parameter-free existential definability.
- **Open-access substitute for that topic:** (open-access for topic: intrinsic computability and forcing) — Knight / 2002 / computable structure theory course notes / nd.edu/~jknight
- **Connection:** The proof explicitly cites "Ash-Knight Thm 10.5" as the source for the false parameterless corollary. Checking this chapter will CONTRADICT the proof's claim and support Grader A's critique that preservation under *embeddings* (not just automorphisms) is the actual mathematical requirement for parameter-free $\Sigma_1$ definitions.
- **Web search query:** `ash knight computable structures hyperarithmetical hierarchy pdf`
- **Confidence (bibliographic):** HIGH

**Hodges / 1993**
- **Title:** Model Theory
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** The section on preservation theorems establishes that a formula is equivalent to an existential ($\Sigma_1$) formula if and only if it is preserved under embeddings.
- **Topic needed for this proof:** The fundamental distinction between preservation under automorphisms (invariance) and preservation under embeddings, particularly concerning existential formulas.
- **Open-access substitute for that topic:** (open-access for topic: preservation theorems for existential formulas) — Marker / 2002 / model theory lecture notes / math.uic.edu
- **Connection:** Directly addresses Grader A's critique and scaffolding questions. It explains why rigidity (invariance under automorphisms) does not mathematically grant parameter-free $\Sigma_1$ definability, using standard counterexamples like $(\mathbb{N}, S)$ where the automorphism group is trivial but embeddings are proper/non-surjective.
- **Web search query:** `hodges model theory pdf`
- **Confidence (bibliographic):** HIGH

**Kechris / 1995**
- **Title:** Classical Descriptive Set Theory
- **Type:** monograph
- **Venue:** Springer (Graduate Texts in Mathematics)
- **Main result or relevant chapter/section:** Develops the theory of Polish spaces and groups. The chapter on Polish groups covers the topology of pointwise convergence on automorphism groups of countable structures; also includes the Baire Category Theorem application showing that countable Polish spaces must contain isolated points.
- **Topic needed for this proof:** The topological properties of automorphism groups over countable structures and the deduction that a countable Polish group must be discrete.
- **Open-access substitute for that topic:** (open-access for topic: Polish spaces and Baire Category Theorem) — Gao / 2008 / Invariant Descriptive Set Theory / personal webpage drafts
- **Connection:** Justifies the topological deductions in Step 1 and Step 2 of the proof. Addresses Grader B's request to state the exact closed-language hypotheses needed for the automorphism group of a structure to form a Polish space.
- **Web search query:** `kechris classical descriptive set theory pdf`
- **Confidence (bibliographic):** HIGH

**Montalbán / 2021**
- **Title:** Computable Structure Theory: Within the Arithmetic
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant chapter/section:** A comprehensive modern textbook synthesis of computable structure theory, featuring detailed, structural expositions on relations on a cone, forcing, and the AKMS theorem.
- **Topic needed for this proof:** Modern definitions of relative intrinsic computability on a cone and whether uniform computability is intrinsically required or produced.
- **Open-access substitute for that topic:** (open-access for topic: textbook coverage of computable structure theory) — Montalbán / 2021 / Computable Structure Theory: Within the Arithmetic / math.berkeley.edu/~antonio
- **Connection:** Addresses Grader B's concerns about uniform vs. non-uniform relative computability and clarifies the precise version of "relative intrinsic computability on a cone" being applied in the proof's logic.
- **Web search query:** `montalban computable structure theory within the arithmetic pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and topic-keyed substitutes that address the specific gaps and fallacies identified by the graders, particularly the failure of the parameter-removal step for $\Sigma_1$ formulas and the foundational topological/computability definitions.

### 1. The Ash-Knight-Manasse-Slaman Theorem (and the alleged corollary)
**Authors:** C. J. Ash, J. Knight
**Year:** 2000
**Title:** Computable Structures and the Hyperarithmetical Hierarchy
**Type:** book
**Venue:** Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144)
**Main result or relevant chapter/section:** Chapter 10 covers "Relative Intrinsic Computability" and contains the definitive exposition of the Ash-Knight-Manasse-Slaman (AKMS) Theorem, establishing the equivalence between relations being relatively intrinsically $\Sigma^0_\alpha$ on a cone and definability via computable infinitary $\Sigma_\alpha$ formulas with a finite set of parameters.
**Topic needed for this proof:** The exact conditions of the AKMS theorem and whether the required finite parameters can be dropped for relations invariant under automorphisms.
**Open-access substitute for that topic:** (open-access for topic: Modern treatment of the AKMS theorem and relative intrinsic computability) — A. Montalbán / 2021 / *Computable Structure Theory: Within the Arithmetic* / Author's webpage draft (UC Berkeley).
**Connection:** The proof fatally cites a "known corollary" of Ash-Knight Theorem 10.5 claiming parameters can be dropped for $\Sigma^{in}_1$ formulas purely based on automorphism invariance. Checking this canonical source will reveal this corollary is hallucinated; parameter-free definability usually applies to the full infinitary logic $L_{\omega_1\omega}$ (via Scott formulas), not strictly existential formulas, confirming Grader A's critique.
**Web search query:** `montalban computable structure theory within the arithmetic pdf`
**Confidence:** HIGH

### 2. The Chisholm Paper (Independent proof of AKMS)
**Authors:** J. Chisholm
**Year:** 1990
**Title:** Effective Model Theory vs. Recursive Model Theory
**Type:** paper
**Venue:** Journal of Symbolic Logic, Vol. 55, No. 3
**Main result or relevant chapter/section:** Gives an independent proof of the AKMS theorem (that a relation is intrinsically computable on a cone iff it is definable by a computable infinitary formula with finitely many parameters) using forcing.
**Topic needed for this proof:** The precise parameter dependence in forcing definitions of intrinsically computable relations.
**Connection:** The proof explicitly names "Chisholm 1990" as a source for the parameter-omission step. Locating this paper will show that the grader is correct: Chisholm does *not* prove that automorphism-invariance alone allows the omission of parameters for $\Sigma_1$ formulas, exposing the missing bridge identified by Grader B (Fallacy 5).
**Web search query:** `chisholm effective model theory vs recursive model theory pdf`
**Confidence:** HIGH

### 3. Model Theoretic Preservation Theorems (The $\Sigma_1$ definability gap)
**Authors:** W. Hodges
**Year:** 1993
**Title:** Model Theory
**Type:** book
**Venue:** Cambridge University Press (Encyclopedia of Mathematics and its Applications)
**Main result or relevant chapter/section:** The chapter on "Constructing Models" (specifically sections dealing with preservation theorems and the Los-Tarski theorem). It proves that a formula is preserved under *substructures/embeddings* if and only if it is equivalent to an existential ($\Sigma_1$) formula.
**Topic needed for this proof:** The strict model-theoretic distinction between relations preserved by automorphisms (which yield general $L_{\omega_1\omega}$ definitions) and those preserved by embeddings (which yield $\Sigma_1$ definitions).
**Open-access substitute for that topic:** (open-access for topic: Preservation theorems and existential definability) — D. Marker / 2002 / *Model Theory: An Introduction* / widely circulated course notes or early drafts.
**Connection:** This directly resolves Grader A's first scaffolding question and critique. The proof's assumption that $\Sigma^{in}_1$ complexity is maintained when dropping parameters via automorphism invariance is false; dropping to $\Sigma_1$ strictly requires evaluating embeddings.
**Web search query:** `hodges model theory pdf` (or `anand pillay model theory notes pdf` for a fast open-access model theory substitute)
**Confidence:** HIGH

### 4. Polish Groups and the Baire Category Theorem
**Authors:** A. S. Kechris
**Year:** 1995
**Title:** Classical Descriptive Set Theory
**Type:** book
**Venue:** Springer (Graduate Texts in Mathematics)
**Main result or relevant chapter/section:** Chapter 1 (Basic Concepts) and Chapter 3 (Baire Category). Contains the standard proofs that a non-empty completely metrizable space satisfies the Baire Category Theorem, and that any countable Polish space must contain isolated points. 
**Topic needed for this proof:** The topological deduction that a countable Polish group has an isolated identity element, which thus enforces a trivial stabilizer for some finite tuple.
**Open-access substitute for that topic:** (open-access for topic: Countable Polish groups and discrete topologies) — S. Gao / 2008 / *Invariant Descriptive Set Theory* / Author's webpage draft.
**Connection:** Addresses Grader B's Slips 1 & 2 and the first scaffolding question. It provides the canonical justification for Step 1 of the NO Proof, verifying that if $\AUT(\A)$ is indeed a Polish group under the pointwise convergence topology, its countability forces it to be discrete.
**Web search query:** `kechris classical descriptive set theory pdf`
**Confidence:** HIGH

### 5. Computable Structure Theory / Forcing and Uniformity
**Authors:** C. J. Ash, J. Knight, M. Manasse, T. Slaman
**Year:** 1989
**Title:** Generic Copies of Countable Structures
**Type:** paper
**Venue:** Annals of Pure and Applied Logic, Vol. 42
**Main result or relevant chapter/section:** Introduces the formal forcing apparatus for generic copies of computable structures, which is the foundational mechanism for proving theorems about relations computable on a cone.
**Topic needed for this proof:** The distinction between "computable relative to an oracle" and "uniformly computable by a single functional", and how the generic forcing condition fixes finite parameters.
**Connection:** Grader B's Critique 3 and 4 challenge whether the proof establishes *uniform* computability of the transported graph relation. The original AKMS paper rigorously explains how uniformity is forced locally by a finite condition (the parameters $\bar{p}$), proving why the parameters appear in the resulting formula and why dropping them breaks the uniformity.
**Web search query:** `ash knight manasse slaman generic copies pdf`
**Confidence:** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed substitutes that bear directly on the proof’s claims and the graders' gap reports. 

### 1. The Core AKMS Theorem & The Uniformity Gap

**Ash, C. J., Knight, J. F., Manasse, M., & Slaman, T. A. / 1989**
- **Title:** Generic copies of countable structures
- **Type:** paper
- **Venue:** Annals of Pure and Applied Logic 42
- **Main result or relevant section:** Proves the AKMS theorem, which characterizes relatively intrinsically $\Sigma^0_\alpha$ relations on a cone in terms of definability by computable infinitary $\Sigma_\alpha$ formulas. 
- **Topic needed for this proof:** The structural necessity of generic parameters; the theorem shows that the forcing construction intrinsically yields a finite parameter tuple unless the relation is *uniformly* relatively intrinsically computable.
- **Open-access substitute:** (open-access for topic: AKMS theorem forcing and parameter generation) — Montalbán / 2021 / *Computable Structure Theory: Within the Arithmetic* / draft on author's personal webpage
- **Connection:** Addresses Grader B’s critique about uniformity. The proof asserts the transported graph is computable relative to $\mathcal{B} \oplus C$, but fails to prove it uses a *uniform* Turing index across all copies. Without uniform computability, the AKMS machinery unconditionally forces parameters into the defining formula.
- **Web search query:** `ash knight manasse slaman generic copies pdf`
- **Confidence (bibliographic):** HIGH

**Chisholm, J. / 1990**
- **Title:** Effective model theory vs. recursive model theory
- **Type:** paper
- **Venue:** Journal of Symbolic Logic 55(3)
- **Main result or relevant section:** Independently proves the AKMS theorem (sometimes called the Ash-Knight-Chisholm Theorem) mapping relatively intrinsically computable relations to infinitary syntax.
- **Topic needed for this proof:** The precise conditions under which extra constants can be eliminated from the syntactic definition.
- **Open-access substitute:** (open-access for topic: Effective model theory and intrinsic relations) — Knight / 2002 / *Computable structure theory* / draft chapter for Handbook of Computability Theory
- **Connection:** The proof explicitly cites "Chisholm 1990" in Step 5 to justify entirely omitting parameters for invariant relations. Retrieving this source verifies Grader A and B's critiques: Chisholm makes no such parameter-free allowance for bounded-complexity ($\Sigma^{in}_1$) formulas.
- **Web search query:** `chisholm effective model theory recursive pdf`
- **Confidence (bibliographic):** HIGH

### 2. The $\Sigma^{in}_1$ Parameter-Dropping Fallacy

**Ash, C. J. & Knight, J. F. / 2000**
- **Title:** Computable Structures and the Hyperarithmetical Hierarchy
- **Type:** monograph
- **Venue:** Elsevier (Studies in Logic and the Foundations of Mathematics, Vol. 144)
- **Main result or relevant section:** Chapter 10 covers the full theoretical framework of $\Sigma^c_\alpha$ formulas, relatively intrinsically computable relations, and the exact statement of "Thm 10.5". 
- **Topic needed for this proof:** The exact text of Theorem 10.5 regarding $\Sigma^c_\alpha$ definability and the strictly limited conditions under which structural rigidity allows parameter reduction.
- **Open-access substitute:** (open-access for topic: computable infinitary formulas and parameters) — Ash Knight Computable Structures and the Hyperarithmetical Hierarchy / excerpted chapters on university repositories
- **Connection:** The proof fatally attempts to invoke "Ash-Knight Thm 10.5" to drop parameters from the existential definition simply because the structure was rigidified. The book confirms Grader B's fallacy detection: structural rigidity creates invariance but does not erase the syntactic requirement of generic parameters for non-uniform enumerations.
- **Web search query:** `ash knight computable structures hyperarithmetical pdf`
- **Confidence (bibliographic):** HIGH

**Scott, D. / 1965**
- **Title:** Logic with extra quantifiers
- **Type:** paper
- **Venue:** Theory of Models (Proceedings of the 1963 International Symposium at Berkeley), North-Holland
- **Main result or relevant section:** Proves Scott's Isomorphism Theorem, demonstrating that countable structures and their automorphism orbits can be defined up to isomorphism by parameter-free sentences in $L_{\omega_1\omega}$.
- **Topic needed for this proof:** The distinction between defining invariant orbits in unbounded $L_{\omega_1\omega}$ versus bounded complexity levels like $\Sigma_1$.
- **Open-access substitute:** (open-access for topic: Scott's Isomorphism Theorem and invariant relations) — Marker / 2016 / *Lectures on Infinitary Model Theory* / ASL Lecture Notes draft
- **Connection:** Directly answers Grader A's primary fallacy. The proof's author misremembered Scott's Theorem (which does allow parameter-free definitions for invariant relations, but at vastly higher complexities, often $\Pi^{in}_2$ or higher) as applying to purely positive existential ($\Sigma^{in}_1$) definitions.
- **Web search query:** `scott "logic with extra quantifiers" pdf`
- **Confidence (bibliographic):** HIGH

**Keisler, H. J. / 1971**
- **Title:** Model Theory for Infinitary Logic
- **Type:** monograph
- **Venue:** North-Holland
- **Main result or relevant section:** Establishes the core preservation theorems for $L_{\omega_1\omega}$, defining the structural behaviors of existential and universal infinitary formulas.
- **Topic needed for this proof:** The infinitary analogue of the Łoś–Tarski preservation theorem, which proves that $\Sigma_1$ definability strictly requires preservation under *embeddings*, not merely automorphisms.
- **Open-access substitute:** (open-access for topic: infinitary preservation theorems) — Marker / 2016 / *Lectures on Infinitary Model Theory* / ASL Lecture Notes in Logic draft
- **Connection:** Validates Grader A’s scaffolding questions. It proves mathematically why an arbitrary relation that is invariant under automorphisms cannot be existentially defined without parameters unless it is also invariant under all self-embeddings.
- **Web search query:** `keisler model theory for infinitary logic pdf`
- **Confidence (bibliographic):** HIGH

### 3. The Polish Space / Topological Discreteness Claims

**Kechris, A. S. / 1995**
- **Title:** Classical Descriptive Set Theory
- **Type:** book
- **Venue:** Springer Graduate Texts in Mathematics 156
- **Main result or relevant section:** Chapter 8 covers the Baire Category Theorem and shows that a countable Polish space must be discrete; Chapter 9 covers Polish groups and establishes that the topology of pointwise convergence on $\text{Aut}(\mathcal{A})$ is Polish.
- **Topic needed for this proof:** The explicit countability and closed-language hypotheses required for an automorphism group to form a completely metrizable Polish space, and the equivalence between topological isolation and trivial pointwise stabilizers.
- **Open-access substitute:** (open-access for topic: Polish topology on automorphism groups of countable structures) — Gao / 2008 / *Invariant Descriptive Set Theory* / draft on author's webpage
- **Connection:** Closes Grader B's first slip. The proof asserts $\text{Aut}(\mathcal{A})$ is a Polish space without checking if $\mathcal{A}$'s language is countable (a strict requirement for the topology of pointwise convergence to be Polish). It correctly cites the Baire Category Theorem (Step 1/2) but drops the language hypothesis. 
- **Web search query:** `kechris classical descriptive set theory pdf`
- **Confidence (bibliographic):** HIGH

**Montalbán, A. / 2021**
- **Title:** Computable Structure Theory: Within the Arithmetic
- **Type:** monograph
- **Venue:** Cambridge University Press
- **Main result or relevant section:** Part II develops the modern synthesis of computable infinitary logic, focusing heavily on the distinction between uniform relative intrinsic computability (which avoids finite generic parameters) and non-uniform relative intrinsic computability (which strictly requires them).
- **Topic needed for this proof:** The formal separation between uniform and non-uniform relative intrinsic phenomena.
- **Open-access substitute:** (open-access for topic: uniform vs non-uniform relative intrinsic computability) — Montalbán / 2021 / *Computable Structure Theory: Within the Arithmetic* / author's personal webpage draft
- **Connection:** Resolves Grader B's scaffolding question ("What is the difference between ‘each object is computable relative to an oracle’ and ‘one functional uniformly computes all objects’?"). The solver assumes that merely guaranteeing *some* Turing index for the automorphism locally implies parameter-free definability globally, which Montalbán explicitly demonstrates is false.
- **Web search query:** `montalban computable structure theory within the arithmetic pdf`
- **Confidence (bibliographic):** HIGH
