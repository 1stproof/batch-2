# Librarian Findings — grader3_4eb567f8c5cc_proof_stage4_solver6_20260531_015458
**Generated:** 2026-05-31T02:05:40  
**Inputs:** notebook=18993 chars, proof=8056 chars, gap_report=4093 chars  
**Date restriction:** none (FP v2 — recent works allowed)  

---

## Citation IDs (aggregator-only)
```json
{
  "arxiv": [
    "1609.07058",
    "1902.08966"
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
    "1105.6158",
    "1609.07058",
    "1902.08966"
  ],
  "arxiv_dropped_2026": [],
  "doi": [],
  "isbn": []
}
```

---

# Stage 1 — Gauntlet (aggregator output)

## VERY RELATED
- [Paper] M. Zabrocki / 2019 — A module for the Delta conjecture — arXiv — IDs: arxiv:1902.08966 — Constructs the true anti-commutative super-coinvariant algebra and the exact fermionic lowering operators the proof attempts to invoke. — search: zabrocki a module for the delta conjecture pdf
- [Paper] J. Haglund, B. Rhoades, M. Shimozono / 2018 — Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture — Advances in Mathematics — IDs: arxiv:1609.07058 — Constructs the purely commutative quotient ring misattributed by the proof, alongside explicit discrete combinatorial statistics on OSPs. — search: haglund rhoades shimozono ordered set partitions pdf
- [Book] S.-J. Cheng, W. Wang / 2012 — Dualities and Representations of Lie Superalgebras — AMS Graduate Studies in Mathematics — IDs: no ID — Details the explicit kernel of the $GL(1|1)$ lowering operator, mathematically invalidating the proof's claim of a positive-degree $d=0$ collapse. — search: cheng wang dualities representations lie superalgebras pdf
- [Paper] A. Berele, A. Regev / 1987 — Hook Young diagrams with applications to combinatorics and to representations of Lie superalgebras — Advances in Mathematics — IDs: no ID — Establishes the canonical hook-vanishing theorem and super-character specializations essential for the proof's $1|1$ evaluation. — search: berele regev hook young diagrams pdf

## RELATED
- [Monograph] F. Bergeron / 2009 — Algebraic Combinatorics and Coinvariant Spaces — CRC Press — IDs: no ID — Formalizes the multivariate diagonal coinvariant spaces, resolving the proof's permutation-standard representation mismatch and $GL_m$ decomposition errors. — search: bergeron algebraic combinatorics coinvariant spaces pdf
- [Paper] J. Haglund, J. Remmel, A. T. Wilson / 2018 — The Delta Conjecture — Transactions of the AMS — IDs: no ID — Defines the rigorous discrete combinatorial statistics on Ordered Set Partitions required to replace the proof's flawed continuous derivatives. — search: haglund remmel wilson delta conjecture pdf

## SOMEWHAT RELATED
- [Book] I. G. Macdonald / 1995 — Symmetric Functions and Hall Polynomials (2nd Edition) — Oxford University Press — IDs: no ID — Provides the foundational algebraic background and determinantal formulas for evaluating Schur functions on hybrid supersymmetric alphabets. — search: macdonald symmetric functions hall polynomials pdf

## NOT MUCH
*(No entries in this category)*

---

# Stage 2 — Narrower (draw 0, canonical)

## LOAD-BEARING

- [Paper] M. Zabrocki / 2019 — A module for the Delta conjecture — arXiv — IDs: arxiv:1902.08966 — Constructs the true anti-commutative super-coinvariant algebra and the exact fermionic lowering operators the proof attempts to invoke.
  - **Addresses:** Grader A's "Broken $d=0$ Collapse (Fallacy)" and Grader B's "Fallacy: The identification of the specialized invariant ideal with the super-coinvariant ideal is unproved."
  - **Load-bearing piece:** The section explicitly constructing the module $V_n$ (the super-coinvariant algebra) and defining the exact generators of the invariant ideal involving anti-commuting variables, which fixes the flawed derivation operator kernel claim.

- [Paper] J. Haglund, B. Rhoades, M. Shimozono / 2018 — Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture — Advances in Mathematics — IDs: arxiv:1609.07058 — Constructs the purely commutative quotient ring misattributed by the proof, alongside explicit discrete combinatorial statistics on OSPs.
  - **Addresses:** Grader A's "Misattributed Basis (Fallacy)" and Grader A's "Missing Combinatorial Interpretation (Fallacy)".
  - **Load-bearing piece:** The definition of the commutative quotient ring $R_{n,k}$ and its discrete Artin basis, which clearly distinguishes its structure from the super-coinvariant algebra and provides the derivative-free integer statistics (like $inv$ and $maj$ on OSPs).

- [Paper] A. Berele, A. Regev / 1987 — Hook Young diagrams with applications to combinatorics and to representations of Lie superalgebras — Advances in Mathematics — IDs: no ID — Establishes the canonical hook-vanishing theorem and super-character specializations essential for the proof's $1|1$ evaluation.
  - **Addresses:** Grader B's "Slip: The 1|1 hook-vanishing claim needs the explicit super Schur specialization formula."
  - **Load-bearing piece:** The central theorem defining super Schur functions and characterizing their factorization and exact vanishing on supersymmetric alphabets for non-hook partitions.

- [Monograph] F. Bergeron / 2009 — Algebraic Combinatorics and Coinvariant Spaces — CRC Press — IDs: no ID — Formalizes the multivariate diagonal coinvariant spaces, resolving the proof's permutation-standard representation mismatch and $GL_m$ decomposition errors.
  - **Addresses:** Grader A's "Dimension Mismatch (Slip)" and Grader B's "Fallacy: The replacement of the original variable space by the standard representation is not justified."
  - **Load-bearing piece:** The introductory chapters that rigorously construct the diagonal coinvariant spaces using the full $n$-dimensional permutation representation rather than the $(n-1)$-dimensional standard representation.

## SUPPORTING

- [Book] S.-J. Cheng, W. Wang / 2012 — Dualities and Representations of Lie Superalgebras — AMS Graduate Studies in Mathematics — IDs: no ID — Details the explicit kernel of the $GL(1|1)$ lowering operator, mathematically invalidating the proof's claim of a positive-degree $d=0$ collapse.
  - **Note:** Useful background for calculating the exact highest-weight structures and character recovery of $GL(1|1)$ modules.

- [Book] I. G. Macdonald / 1995 — Symmetric Functions and Hall Polynomials (2nd Edition) — Oxford University Press — IDs: no ID — Provides the foundational algebraic background and determinantal formulas for evaluating Schur functions on hybrid supersymmetric alphabets.
  - **Note:** Standard text for checking the Cauchy identity rules and symmetric function properties invoked early in the proof.

## REDUNDANT

- [Paper] J. Haglund, J. Remmel, A. T. Wilson / 2018 — The Delta Conjecture — Transactions of the AMS — IDs: no ID — Defines the rigorous discrete combinatorial statistics on Ordered Set Partitions required to replace the proof's flawed continuous derivatives.
  - **Overlap:** Overlaps with Haglund, Rhoades, Shimozono (2018) which also covers the requisite discrete combinatorial statistics on OSPs for the combinatorial interpretation gap.

## PERIPHERAL

*(No entries)*

## UNFAMILIAR

*(No entries)*

---

# Stage 3 — Chapter Picker

## Algebraic Combinatorics and Coinvariant Spaces (F. Bergeron, CRC Press, 2009)
_(Formalizes the multivariate diagonal coinvariant spaces, resolving the proof's permutation-standard representation mismatch and $GL_m$ decomposition errors.)_

Based on the parametric memory of François Bergeron's 2009 text, the proof has entirely abandoned the canonical bosonic structure of $R_n^{(m)}$ to hallucinate an invalid superspace shortcut. Bergeron provides the correct $GL_m \times S_n$ module structures and discrete combinatorial models directly.

Here are the specific chapters to point the mathematician toward:

- **Chapter 2 (approx.) — Coinvariant Spaces**
  - **Which gap it addresses:** Grader A Gap 4 & Grader B Gap 1 (Replacement of the original variable space by the standard representation).
  - **Why:** This chapter introduces the foundational step of decoupling the "center of mass." Bergeron explicitly shows how quotienting by the degree-1 invariants (e.g., $p_1 = \sum x_i$) natively restricts the $n$-dimensional permutation representation to the $(n-1)$-dimensional standard representation without breaking the ring properties.

- **Chapter 4 (approx.) — Multivariate Coinvariant Spaces**
  - **Which gap it addresses:** Grader B Gap 2 ($S_n$-invariance proving $GL(E)$ decomposition) and Grader B Gap 5/6 (Recovering individual graded coefficients).
  - **Why:** Bergeron formally develops the $GL_m \times S_n$ module structure on the ring of $m$-variate polynomials. He details how the ideal generated by symmetric invariants naturally commutes with the continuous $GL_m$ action, allowing the multivariate Frobenius characteristic to exactly map $S_n$ irreducible multiplicities (like hooks) to multi-graded Schur expansions.

- **Chapter 4 (approx.) — Multivariate Coinvariant Spaces (Combinatorics of $m$-Parking Functions)**
  - **Which gap it addresses:** Grader A Gap 1 (Missing Combinatorial Interpretation) and Grader B Gap 7 (Highest-weight source is not a combinatorial condition).
  - **Why:** This section provides the actual, discrete combinatorial interpretation for the Hilbert series of $R_n^{(m)}$. Bergeron introduces $m$-parking functions and higher-order discrete statistics (like generalized `dinv` and `area`), demonstrating how to construct a genuine combinatorial framework that avoids the logically broken continuous derivation-operator constraints the proof relies on. 

*(Note: I do not believe this reference addresses Grader A Gap 1/2 regarding the explicit explicit kernel of the $GL(1|1)$ lowering operator, because Bergeron 2009 strictly focuses on the purely commutative/bosonic diagonal coinvariants. The AI's importation of the super-coinvariant algebra is a fundamentally disjoint technique that the text will inherently ignore in favor of $m$-parking functions.)*

## Dualities and Representations of Lie Superalgebras (S.-J. Cheng, W. Wang, AMS Graduate Studies in Mathematics, 2012)
_(Details the explicit kernel of the $GL(1|1)$ lowering operator, mathematically invalidating the proof's claim of a positive-degree $d=0$ collapse.)_

Here are the specific sections from Cheng & Wang (2012) that directly address the graders' identified gaps.

**Chapter 2 (approx.) — The General Linear Lie Superalgebra $\mathfrak{gl}(m|n)$**
*   **Which gap it addresses:** Grader B (Slip 3 and Fallacy 5) — Super Schur specialization formula and the inability to recover individual hook multiplicities merely from 2-dimensional $GL(1|1)$ characters.
*   **Why:** This chapter details the highest-weight representation theory for $\mathfrak{gl}(m|n)$, including explicit constructions of Kac modules. It shows that the super-character (super-trace) of a 2-dimensional $\mathfrak{gl}(1|1)$ hook module evaluates to a binomial difference (e.g., $q^k z^d - q^{k-1} z^{d+1}$), proving that you cannot isolate individual multidegrees without algebraic decomposition, validating Grader B's critique.

**Chapter 3 (approx.) — Super Schur-Weyl Duality**
*   **Which gap it addresses:** Grader B (Fallacy 2) — The assertion that $S_n$-invariance of the ideal trivially dictates the required $GL(E)$-module quotient decomposition in superspace.
*   **Why:** This chapter formalizes the commuting actions of the symmetric group $S_n$ and $\mathfrak{gl}(m|n)$ on the super tensor space $(\mathbb{C}^{m|n})^{\otimes n}$. It proves the precise conditions under which taking $S_n$-coinvariants algebraically guarantees a decomposition into super-Schur functors, providing the exact algebraic justification the proof skipped.

**Chapter 4 (approx.) — Howe Duality for Lie Superalgebras (Oscillator Representations)**
*   **Which gap it addresses:** Grader A (Fallacy 2) — The broken $d=0$ collapse and the exact formula/kernel of the $GL(1|1)$ lowering operator. 
*   **Why:** This section constructs the realization of Lie superalgebras via differential operators acting on the super-polynomial ring $\mathbb{C}[x] \otimes \Lambda(\theta)$. It explicitly represents the odd lowering generator of $\mathfrak{gl}(1|1)$ as $Q = \sum \theta_i \frac{\partial}{\partial x_i}$ and proves its algebraic kernel; this confirms Grader A's critique that the kernel on the purely bosonic subspace consists strictly of constants, thereby invalidating the proof's claim that this condition yields positive-degree permutations.

## Symmetric Functions and Hall Polynomials (2nd Edition) (I. G. Macdonald, Oxford University Press, 1995)
_(Provides the foundational algebraic background and determinantal formulas for evaluating Schur functions on hybrid supersymmetric alphabets.)_

Here are the specific chapters and sections from Macdonald's text that address the foundational algebraic flaws in the proof, along with a note on what the text cannot resolve.

- **Chapter I, Section 3 - Schur functions (approx.)**
  - **Which gap it addresses:** Grader B's Slip 3 ("The 1|1 hook-vanishing claim needs the explicit super Schur specialization formula") and Scaffolding Q1 ("character of a nonempty hook Schur functor on a superspace").
  - **Why:** The extensive examples at the end of this section construct Schur functions on supersymmetric/hybrid alphabets (often denoted $s_\lambda(x/y)$ or $s_\lambda(X \cup -Y)$). It contains the foundational algebraic proof that the super-Schur function identically vanishes unless $\lambda$ fits inside an $(m,n)$-hook. For an alphabet with one commuting and one anti-commuting variable ($1|1$), it rigorously proves the non-zero evaluations strictly limit to hook partitions and provides their exact two-term polynomial evaluation.

- **Chapter I, Section 4 - Orthogonality (approx.)**
  - **Which gap it addresses:** Grader B's Fallacy 2 ("`S_n`-invariance of the ideal does not prove the required `GL(E)`-module quotient decomposition").
  - **Why:** This section covers the classical Cauchy identities (e.g., the expansion of $\prod (1-x_iy_j)^{-1} = \sum s_\lambda(x)s_\lambda(y)$), which serve as the rigorous algebraic backbone for decomposing the symmetric algebra $\operatorname{Sym}(V \otimes E)$ into $GL(V) \times GL(E)$ modules. Citing this properly is necessary to justify how quotienting by a purely spatial $S_n$-invariant ideal interacts with the $GL(E)$ multi-graded character structure.

- **I do not believe this reference actually addresses Grader A's combinatorial gaps.**
  - **Which gap it addresses:** Grader A's Fallacy 1 (Missing Combinatorial Interpretation), Fallacy 2 (Broken $d=0$ Collapse), and Fallacy 3 (Misattributed Basis).
  - **Why:** Macdonald's 1995 text establishes the classical algebraic ring of symmetric functions. It predates the modern combinatorial developments of the super-coinvariant algebra $SR_n$, Ordered Set Partitions (OSPs), and the Haglund-Rhoades-Shimozono commutative basis by several decades, so it contains no mechanisms to fix the broken discrete combinatorial rules or derivative kernels.

---

# Stage 2 — Narrower (additional draws, for variance)
## Narrower draw 1
Here is the triage of the provided works against the specific grader gaps.

## LOAD-BEARING

- **[Paper] M. Zabrocki / 2019 — A module for the Delta conjecture — arXiv — IDs: arxiv:1902.08966**
  - **Addresses:** Grader B Gap 4 ("Identification of specialized invariant ideal with the super-coinvariant ideal is unproved") and Grader A Gap 1 ("Missing Combinatorial Interpretation").
  - **Load-bearing piece:** Sections 2 and 3 define the precise structure of the super-coinvariant algebra (using both commuting and anti-commuting variables) and introduce the explicit fermionic derivation operators needed to track the OSP basis properly.

- **[Paper] J. Haglund, B. Rhoades, M. Shimozono / 2018 — Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture — Advances in Mathematics — IDs: arxiv:1609.07058**
  - **Addresses:** Grader A Gap 3 ("Misattributed Basis") and Grader B Gap 6 ("A total ordered-set-partition dimension count cannot determine individual graded hook coefficients").
  - **Load-bearing piece:** The construction of the generalized coinvariant algebra $R_{n,k}$ exactly demonstrates how to form a purely commutative quotient ring with an OSP basis, supplying the discrete combinatorial statistics (like `inv` and `maj`) that the proof is missing.

- **[Paper] A. Berele, A. Regev / 1987 — Hook Young diagrams with applications to combinatorics and to representations of Lie superalgebras — Advances in Mathematics — IDs: no ID**
  - **Addresses:** Grader B Gap 3 ("The 1|1 hook-vanishing claim needs the explicit super Schur specialization formula").
  - **Load-bearing piece:** The fundamental theorem establishing the explicit formula for super-Schur polynomials and proving they strictly vanish for any partition containing a $(2,2)$ box (i.e., non-hooks).

- **[Monograph] F. Bergeron / 2009 — Algebraic Combinatorics and Coinvariant Spaces — CRC Press — IDs: no ID**
  - **Addresses:** Grader A Gap 4 ("Dimension Mismatch") and Grader B Gap 2 ("$S_n$-invariance of the ideal does not prove the required $GL(E)$-module quotient decomposition").
  - **Load-bearing piece:** The first two chapters meticulously formalize the $GL_m \times S_n$ module structure on the diagonal coinvariant spaces, formally distinguishing the use of the $n$-dimensional permutation variables from the $(n-1)$-dimensional standard variables.

## SUPPORTING

- **[Book] S.-J. Cheng, W. Wang / 2012 — Dualities and Representations of Lie Superalgebras — AMS Graduate Studies in Mathematics — IDs: no ID**
  - Verifies Grader A Gap 2 ("Broken $d=0$ Collapse") and Grader B Gap 5 by providing the fundamental highest-weight representation theory and the exact kernel formula for the $GL(1|1)$ lowering operator.

- **[Paper] J. Haglund, J. Remmel, A. T. Wilson / 2018 — The Delta Conjecture — Transactions of the AMS — IDs: no ID**
  - Provides essential background on the discrete combinatorial statistics on Ordered Set Partitions which could be used to resolve Grader A Gap 1 without appealing to continuous derivatives.

- **[Book] I. G. Macdonald / 1995 — Symmetric Functions and Hall Polynomials (2nd Edition) — Oxford University Press — IDs: no ID**
  - The canonical reference for Cauchy's formula, symmetric invariants, and evaluating symmetric functions on super-alphabets to support character manipulation.

## REDUNDANT
*(No entries in this category)*

## PERIPHERAL
*(No entries in this category)*

## UNFAMILIAR
*(No entries in this category)*

## Narrower draw 2
## LOAD-BEARING

- [Paper] M. Zabrocki / 2019 — A module for the Delta conjecture — arXiv — IDs: arxiv:1902.08966 — Constructs the true anti-commutative super-coinvariant algebra and the exact fermionic lowering operators the proof attempts to invoke.
  - **Gaps addressed:** Grader A Gap 2 (Broken $d=0$ Collapse) and Grader B Gap 4 (Identification of the specialized invariant ideal with the super-coinvariant ideal is unproved).
  - **Load-bearing piece:** Section 3 explicitly constructs the super-coinvariant algebra, details the exact kernel of the fermionic lowering operators, and maps its Frobenius characteristic to the Delta conjecture without forcing $d=0$ degrees to trivially vanish.

- [Paper] J. Haglund, B. Rhoades, M. Shimozono / 2018 — Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture — Advances in Mathematics — IDs: arxiv:1609.07058 — Constructs the purely commutative quotient ring misattributed by the proof, alongside explicit discrete combinatorial statistics on OSPs.
  - **Gaps addressed:** Grader A Gap 3 (Misattributed Basis) and Grader A Gap 1 (Missing Combinatorial Interpretation).
  - **Load-bearing piece:** Section 4 defines the commutative generalized coinvariant algebra quotient ring (distinguishing it from the super-coinvariant algebra) and provides the precise discrete statistics (inversions and major index on Ordered Set Partitions) required to build a combinatorial rule without using continuous derivatives.

- [Paper] A. Berele, A. Regev / 1987 — Hook Young diagrams with applications to combinatorics and to representations of Lie superalgebras — Advances in Mathematics — IDs: no ID — Establishes the canonical hook-vanishing theorem and super-character specializations essential for the proof's $1|1$ evaluation.
  - **Gaps addressed:** Grader B Gap 3 (The `1|1` hook-vanishing claim needs the explicit super Schur specialization formula) and Grader B Gap 5 (Hook multiplicities are not recovered merely from two-dimensional `GL(1|1)` characters).
  - **Load-bearing piece:** The core theorems formally establish the explicit specialization formulas for Schur functions evaluated on the $1|1$ superspace, verifying both the structural vanishing of non-hooks and the exact bivariate polynomials generated.

- [Monograph] F. Bergeron / 2009 — Algebraic Combinatorics and Coinvariant Spaces — CRC Press — IDs: no ID — Formalizes the multivariate diagonal coinvariant spaces, resolving the proof's permutation-standard representation mismatch and $GL_m$ decomposition errors.
  - **Gaps addressed:** Grader A Gap 4 (Dimension Mismatch) and Grader B Gap 2 (`S_n`-invariance of the ideal does not prove the required `GL(E)`-module quotient decomposition).
  - **Load-bearing piece:** Chapter 3 rigorously sets up the multi-variate diagonal coinvariant spaces over the $n$-dimensional permutation representation (not the $n-1$ standard representation) and justifies the $GL_m \times S_n$ Cauchy decomposition of the quotient.

## SUPPORTING

- [Paper] J. Haglund, J. Remmel, A. T. Wilson / 2018 — The Delta Conjecture — Transactions of the AMS — IDs: no ID — Defines the rigorous discrete combinatorial statistics on Ordered Set Partitions required to replace the proof's flawed continuous derivatives.
  - *Note:* Useful background for translating the "highest-weight source" condition (Grader B Gap 7) into explicit, well-defined discrete macroscopic combinatorial conditions (like `mac` or `maj` on OSPs).

- [Book] S.-J. Cheng, W. Wang / 2012 — Dualities and Representations of Lie Superalgebras — AMS Graduate Studies in Mathematics — IDs: no ID — Details the explicit kernel of the $GL(1|1)$ lowering operator, mathematically invalidating the proof's claim of a positive-degree $d=0$ collapse.
  - *Note:* Provides formal textbook verification of the Lie superalgebra representation theory and the precise action of $GL(1|1)$ lowering operators on polynomial modules.

## REDUNDANT
*(No overlapping load-bearing entries)*

## PERIPHERAL

- [Book] I. G. Macdonald / 1995 — Symmetric Functions and Hall Polynomials (2nd Edition) — Oxford University Press — IDs: no ID — Provides the foundational algebraic background and determinantal formulas for evaluating Schur functions on hybrid supersymmetric alphabets.
  - *Note:* While a foundational text for symmetric functions, the specific superspace evaluations needed for Grader B Gap 3 are much more directly and canonically addressed by Berele-Regev.

## UNFAMILIAR
*(None)*

---

# Stage 1 — Gauntlet (raw draws, for variance)
## Gauntlet draw 0
Here are the canonical references and topic-keyed substitutes that directly address the structures the proof attempts to invoke, focusing heavily on the representation theory of superspaces and the actual combinatorial statistics on ordered set partitions.

**1. Symmetric Functions and Hall Polynomials (2nd Edition)**
- **Authors / Year** — I. G. Macdonald / 1995
- **Type** — Book
- **Venue** — Oxford Mathematical Monographs
- **Main result or relevant chapter/section** — Chapter I, Section 3 (specifically Examples 23 and 24) establishes the canonical theory of supersymmetric functions $s_\lambda(X/Y)$. It proves the fundamental vanishing theorem: $s_\lambda(X/Y) = 0$ unless $\lambda$ is contained in the $(k, l)$ fat hook (where $k$ is the number of even variables and $l$ the number of odd variables).
- **Topic needed for this proof** — The explicit super Schur specialization formula evaluated on $\mathbb{C}^{1|1}$ that proves the module vanishes for non-hooks.
- **Open-access substitute for that topic** — (open-access for topic: Schur function evaluations on superspaces) — M. Moens, J. van der Jeugt / 2003 / A determinantal formula for supersymmetric Schur polynomials / arxiv
- **Connection** — Directly addresses Grader B's Scaffolding Question 1 and Slip 3 regarding the requirement for an explicit formula proving the 1|1 hook-vanishing claim.
- **Web search query** — `macdonald symmetric functions and hall polynomials pdf`
- **Confidence (bibliographic):** HIGH

**2. Hook Young diagrams with applications to combinatorics and to representations of Lie superalgebras**
- **Authors / Year** — A. Berele, A. Regev / 1987
- **Type** — Paper
- **Venue** — Advances in Mathematics, 64(2)
- **Main result or relevant chapter/section** — Introduces the representation theory of the general linear Lie superalgebra $GL(k|l)$. It explicitly details how the Schur functors $S^\lambda(V_0 \oplus V_1)$ decompose and gives the super-character formulas for evaluating representations with $k$ commuting and $l$ anti-commuting variables.
- **Topic needed for this proof** — The exact super-character formula of a nonempty hook Schur functor evaluated on a superspace with one even and one odd variable (yielding the dimension-2 binomial character $q^k z^d + q^{k-1} z^{d+1}$).
- **Connection** — Addresses Grader B's Fallacy 5 and Scaffolding Q2: the characters yield binomials, so hook multiplicities cannot be trivially pulled from evaluating superspaces as single scalars without a graded extraction mechanism.
- **Web search query** — `berele regev hook young diagrams superspace pdf`
- **Confidence (bibliographic):** HIGH

**3. Algebraic Combinatorics and Coinvariant Spaces**
- **Authors / Year** — F. Bergeron / 2009
- **Type** — Book / Monograph
- **Venue** — CMS Treatise in Mathematics, CRC Press
- **Main result or relevant chapter/section** — Chapter 3 provides the definitive treatment of the multivariate diagonal coinvariant spaces $R_n^{(m)}$. It explicitly constructs the quotient by symmetric invariants, establishes the $GL_m \times S_n$ module structure, and details how multiplicities of $S_n$-irreducibles manifest as universal polynomial functions of $m$.
- **Topic needed for this proof** — The justification for the $GL(E)$ module quotient decomposition and the effect of substituting alternate representations into the universal graded characters.
- **Open-access substitute for that topic** — (open-access for topic: multivariate diagonal coinvariants and their universal characters) — F. Bergeron / 2008 (approx.) / Multivariate Diagonal Coinvariant Spaces for Complex Reflection Groups / arxiv
- **Connection** — Resolves Grader B's Fallacies 1 and 2, explaining exactly why $S_n$-invariance permits the $GL(E)$ quotient decomposition, and structurally critiques the proof's dimension mismatch ($V$ vs polynomial ring variables) highlighted in Grader A's Slip 4.
- **Web search query** — `bergeron algebraic combinatorics and coinvariant spaces pdf`
- **Confidence (bibliographic):** HIGH

**4. A module for the Delta conjecture**
- **Authors / Year** — M. Zabrocki / 2019
- **Type** — Paper (Preprint)
- **Venue** — arxiv
- **Main result or relevant chapter/section** — Constructs the specific super-coinvariant algebra $SR_n = \mathbb{C}[x_n] \otimes \Lambda[\theta_n] / I$ referenced implicitly by the proof. It defines the lowering operator $Q = \sum \theta_i \partial_{x_i}$ and conjectures that the dimension of this super-coinvariant module is exactly the number of ordered set partitions (Fubini numbers).
- **Topic needed for this proof** — The exact algebraic generators of the super-coinvariant ideal and the structural action of the $GL(1|1)$ lowering operator on the mixed polynomial-Grassmann basis.
- **Connection** — Exposes the fatal algebraic flaw identified in Grader A's Fallacy 2: because $Q$ kills a pure polynomial if and only if it is a constant, declaring elements annihilated by $Q$ as "highest weight sources" zeroes out the pure polynomial component, utterly breaking the $d=0$ Mahonian collapse. 
- **Web search query** — `zabrocki a module for the delta conjecture pdf`
- **Confidence (bibliographic):** HIGH

**5. Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture**
- **Authors / Year** — J. Haglund, B. Rhoades, M. Shimozono / 2018
- **Type** — Paper
- **Venue** — Advances in Mathematics
- **Main result or relevant chapter/section** — Constructs the quotient ring $R_{n,k}$ using purely commuting variables modulo relations like $x_i^k = 0$, proving its dimension is governed by ordered set partitions and giving a generalized MacMahon formula. 
- **Topic needed for this proof** — The structural definition of the $R_{n,k}$ basis to explicitly contrast it with super-commutative Grassmann rings.
- **Connection** — Directly verifies Grader A's Fallacy 3 and Scaffolding Q2. The proof falsely attributes Zabrocki's anti-commutative Grassmann super-coinvariant basis to this paper, which fundamentally deals with a purely commutative ring. 
- **Web search query** — `haglund rhoades shimozono ordered set partitions pdf`
- **Confidence (bibliographic):** HIGH

**6. The Delta Conjecture**
- **Authors / Year** — J. Haglund, J. Remmel, A. T. Wilson / 2018
- **Type** — Paper
- **Venue** — Transactions of the AMS
- **Main result or relevant chapter/section** — Introduces the Delta Conjecture predicting the Frobenius characteristic of a module whose dimension is the number of ordered set partitions. Defines the rigorous, discrete combinatorial statistics (`inv`, `maj`, `des`, and `minimaj`) on ordered set partitions that strictly evaluate to the graded Hilbert series without continuous derivations.
- **Topic needed for this proof** — The specific, discrete combinatorial mappings on Ordered Set Partitions that natively track the polynomial degree and exterior degree.
- **Connection** — Addresses Grader A's Fallacy 1 and Scaffolding Q3, as well as Grader B's Scaffolding Q4 and Q5. The proof's reliance on "annihilation by a fermionic derivation" is a continuous evaluation mechanism; to fix the proof, the author must discard the continuous derivatives and directly map $k$ and $d$ to the discrete `inv` and `dim` block statistics established in this paper.
- **Web search query** — `haglund remmel wilson delta conjecture pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 1
Here are the canonical references and topic-keyed substitutes that directly address the gaps in the proof, particularly the continuous-to-discrete translation on Ordered Set Partitions (OSPs), the proper structure of the super-coinvariant algebra, and the supersymmetric Schur evaluations requested by the graders.

- **Authors / Year:** M. Zabrocki / 2019
- **Title:** A module for the Delta conjecture
- **Type:** Paper
- **Venue:** arXiv preprint
- **External IDs:** `arxiv:1902.08966`
- **Main result or relevant chapter/section:** Constructs an explicit $S_n$-module using one set of commuting (bosonic) variables and one set of anti-commuting (fermionic) variables, proving its structure forms the super-coinvariant algebra whose Frobenius characteristic yields the Delta conjecture symmetric functions.
- **Topic needed for this proof:** The rigorous formulation of the super-coinvariant algebra $SR_n$ over $E = \mathbb{C}^{1|1}$ and its connection to the combinatorial OSP module.
- **Connection:** Directly addresses Grader A's Critique 3 and Grader B's Critique 4. The proof hallucinated that the Haglund-Rhoades-Shimozono paper handled the super-coinvariant algebra directly; Zabrocki's paper is the actual canonical source that constructs the true superspace module (1 bosonic + 1 fermionic set of variables) and links it to Delta conjecture combinatorics.
- **Web search query:** `zabrocki a module for the delta conjecture pdf`
- **Confidence (bibliographic):** HIGH
- **ID confidence:** HIGH

- **Authors / Year:** J. Haglund, B. Rhoades, M. Shimozono / 2018
- **Title:** Macdonald polynomials, coinvariant algebras, and the Delta conjecture
- **Type:** Paper
- **Venue:** Advances in Mathematics
- **Main result or relevant chapter/section:** Constructs the *commutative* quotient ring $R_{n,k}$ and provides a complete discrete combinatorial basis using Ordered Set Partitions weighted by explicit integer statistics (inversions and major index) that match the bigraded Hilbert series.
- **Topic needed for this proof:** The extraction of discrete combinatorial statistics (maj and inv on OSPs) that natively index the quotient basis without relying on derivation operators.
- **Open-access substitute for that topic:** (open-access for topic: discrete combinatorial statistics on OSPs for generalized coinvariant algebras) — J. Haglund, B. Rhoades, M. Shimozono / 2017 / Macdonald polynomials, coinvariant algebras, and the Delta conjecture / authors' personal webpages or arxiv.
- **Connection:** Resolves Grader A's Critique 1 ("Missing Combinatorial Interpretation") and Grader B's Critique 7 ("Highest-weight source is not translated"). This paper shows how to replace continuous algebraic conditions (like annihilation by derivations) with explicit, verifiable discrete integer statistics on OSPs.
- **Web search query:** `haglund rhoades shimozono macdonald polynomials coinvariant pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** S.-J. Cheng, W. Wang / 2012
- **Title:** Dualities and Representations of Lie Superalgebras
- **Type:** Book
- **Venue:** AMS Graduate Studies in Mathematics
- **Main result or relevant chapter/section:** The chapters on the general linear superalgebra $\mathfrak{gl}(m|n)$ and super-Howe duality explicitly detail the action of the superalgebra lowering/raising operators (e.g., $E_{21} = \sum \theta_i \frac{\partial}{\partial x_i}$) on the symmetric superalgebra $\operatorname{Sym}(\mathbb{C}^{m|n} \otimes \mathbb{C}^k)$.
- **Topic needed for this proof:** The explicit formulation of the $GL(1|1)$ lowering operator and the proof that its kernel on pure polynomial (bosonic) spaces strictly restricts to constants.
- **Open-access substitute for that topic:** (open-access for topic: explicit Lie superalgebra action and Howe duality on polynomial-exterior tensor spaces) — S.-J. Cheng, W. Wang / 2012 / Howe duality for Lie superalgebras / survey available on authors' webpages.
- **Connection:** Directly answers Grader A's Scaffolding Question 1 and validates Grader A's Critique 2. The proof's claim that $d=0$ collapses back to the Mahonian distribution via the derivation kernel is algebraically false; this reference provides the explicit kernel calculation proving why $Q(P)=0$ annihilates positive-degree pure polynomials.
- **Web search query:** `cheng wang dualities and representations lie superalgebras pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** I. G. Macdonald / 1995
- **Title:** Symmetric Functions and Hall Polynomials (2nd Edition)
- **Type:** Book
- **Venue:** Oxford University Press
- **Main result or relevant chapter/section:** Chapter I, Section 3 (Examples) and the Appendix on supersymmetric functions rigorously derive the evaluations of Schur functions on superspaces, specifically yielding the exact formula $s_{(a, 1^b)}(q|z) = q^a z^b + q^{a-1} z^{b+1}$ for a single commuting and single anti-commuting variable.
- **Topic needed for this proof:** The exact algebraic formula and vanishing conditions for the super-Schur specialization of a hook shape at $GL(1|1)$.
- **Open-access substitute for that topic:** (open-access for topic: combinatorial characterization and evaluation formulas for supersymmetric Schur polynomials) — J. R. Stembridge / 1985 / A characterization of supersymmetric polynomials / Journal of Algebra (often openly hosted by institutions).
- **Connection:** Answers Grader B's Critique 3 and Scaffolding Question 1. The proof lazily claims hook Schur functions evaluated at $\mathbb{C}^{1|1}$ yield exactly dimension 2 without providing the graded character. Macdonald's evaluation formula is strictly required to prove how the bigraded components map back to the quotient dimensions.
- **Web search query:** `macdonald symmetric functions and hall polynomials pdf`
- **Confidence (bibliographic):** HIGH

- **Authors / Year:** F. Bergeron / 2009
- **Title:** Algebraic Combinatorics and Coinvariant Spaces
- **Type:** Book
- **Venue:** CRC Press (CMS Treatises in Mathematics)
- **Main result or relevant chapter/section:** The chapters on multi-variate diagonal coinvariant spaces explicitly define $R_n^{(m)}$, detail the ideal generated by symmetric invariants, and establish the structural stabilization of the $S_n \times GL_m$ module hook multiplicities for $m$ large enough.
- **Topic needed for this proof:** The rigorous $S_n \times GL_m$-module decomposition of the multivariate coinvariant space and the independence of hook multiplicities $c_\lambda(n)$ from the ambient space dimension $m$.
- **Open-access substitute for that topic:** (open-access for topic: stabilization of module structures and multiplicities in multivariate coinvariant spaces) — F. Bergeron / 2011 / Multivariate Diagonal Coinvariant Spaces for Complex Reflection Groups / Advances in Mathematics (author's webpage draft).
- **Connection:** Addresses Grader B's Critiques 1, 2, and 4. The solver makes unverified leaps regarding how $S_n$-invariance of the ideal guarantees specific continuous $GL(E)$ decompositions, and how replacing variable counts behaves. Bergeron provides the rigorous justification for transferring these universal coefficients across dimensions.
- **Web search query:** `bergeron algebraic combinatorics coinvariant spaces pdf`
- **Confidence (bibliographic):** HIGH

## Gauntlet draw 2
Here are the canonical references and topic-keyed substitutes that directly address the gaps your grader identified, particularly concerning the misattributed commutative quotient, the vanishing of super-Schur functions, and the representation theory of $\mathfrak{gl}(1|1)$.

**1. Haglund, Rhoades, Shimozono / 2018**
- **Title:** Ordered set partitions, generalized coinvariant algebras, and the Delta Conjecture
- **Type:** Paper
- **Venue:** Advances in Mathematics (Vol. 329)
- **External IDs:** `arxiv:1609.07058`
- **Main result or relevant section:** Constructs a purely *commutative* generalized coinvariant algebra $R_{n,k}$ whose dimension is the number of ordered set partitions with $k$ blocks. Crucially, it provides the explicit, discrete combinatorial statistics (`inv` and `maj` on OSPs) that yield its graded Hilbert series without invoking differential operators.
- **Topic needed for this proof:** Discrete, derivative-free combinatorial statistics on ordered set partitions that recover the graded dimensions of quotient rings.
- **Connection:** Addresses **Grader A's Critiques 1 and 3**. The proof falsely claims this paper constructs a basis for the *super*-coinvariant algebra. It actually constructs a commutative quotient ring. Furthermore, this paper provides the explicit discrete combinatorial rules (answering Scaffolding Question A3) that the proof is currently missing.
- **Web search query:** `haglund rhoades shimozono ordered set partitions pdf`
- **Confidence (bibliographic):** HIGH
- **ID confidence:** HIGH

**2. Zabrocki / 2019**
- **Title:** A module for the Delta conjecture
- **Type:** Paper
- **Venue:** arxiv preprint (later published in a slightly modified form)
- **External IDs:** `arxiv:1902.08966`
- **Main result or relevant section:** Explicitly defines the true super-coinvariant algebra $SR_n$ as the quotient of the tensor product of commuting variables $\mathbb{C}[x_1, \dots, x_n]$ and anti-commuting variables $\Lambda(\theta_1, \dots, \theta_n)$ by the diagonal invariants. It formulates the conjecture that the dimension of this specific module is the total number of ordered set partitions $\text{OSP}(n)$.
- **Topic needed for this proof:** The exact algebraic definition of the super-coinvariant ideal $SR_n$ and its bi-graded Frobenius characteristic.
- **Connection:** Addresses **Grader A's Critique 3** and **Grader B's Critique 4**. If the investigator wants to use the actual super-coinvariant algebra rather than the commutative $R_{n,k}$ ring, this is the foundational paper they must cite. It also defines the explicit fermionic operators the proof currently waves its hands at.
- **Web search query:** `zabrocki a module for the delta conjecture pdf`
- **Confidence (bibliographic):** HIGH
- **ID confidence:** HIGH

**3. Berele, Regev / 1987**
- **Title:** Hook Young diagrams with applications to combinatorics and to representations of Lie superalgebras
- **Type:** Paper
- **Venue:** Advances in Mathematics (Vol. 64)
- **Main result or relevant section:** Proves the foundational "hook-vanishing theorem": the super Schur function $s_\lambda(x|y)$ in $m$ bosonic and $n$ fermionic variables is identically zero unless $\lambda$ fits inside the $(m, n)$ fat hook. For $m=1, n=1$, this strictly restricts non-vanishing components to standard hook shapes. It also provides the explicit specialization formulas (e.g., $s_{(k, 1^d)}(q|z)$).
- **Topic needed for this proof:** The strict vanishing of super Schur functions outside the $(m, n)$ fat hook and their explicit evaluation formulas.
- **Connection:** Resolves **Grader B's Critique 3** and answers **Scaffolding Question B1**. The proof asserts the $1|1$ hook-vanishing property as magic; this paper is the canonical algebraic proof of that structural property.
- **Web search query:** `berele regev hook young diagrams pdf`
- **Confidence (bibliographic):** HIGH

**4. Cheng, Wang / 2012**
- **Title:** Dualities and Representations of Lie Superalgebras
- **Type:** Book
- **Venue:** AMS Graduate Studies in Mathematics (Vol. 144)
- **Main result or relevant section:** Chapter 2 covers the representation theory of the general linear superalgebra $\mathfrak{gl}(m|n)$, including highest-weight modules and the explicit action of the odd (fermionic) generators.
- **Topic needed for this proof:** The algebraic action and kernel of fermionic lowering operators (like $Q = \sum \theta_i \partial_{x_i}$) on highest-weight modules.
- **Open-access substitute for that topic:** (open-access for topic: lecture notes on Lie superalgebras and highest-weight modules) — Shun-Jen Cheng, *Lectures on Lie Superalgebras* (often available via institutional pages) or Kac's foundational 1977 paper "Lie Superalgebras".
- **Connection:** Directly bears on **Grader A's Critique 2** (the "Broken $d=0$ Collapse"). The grader points out that $Q = \sum \theta_i \partial_{x_i}$ annihilating a pure polynomial forces the polynomial to be a constant. Reviewing the $\mathfrak{gl}(1|1)$ operator actions in this text will prove the grader right: the proof's translation of "highest-weight source" to the $d=0$ case is algebraically fatal.
- **Web search query:** `cheng wang dualities representations lie superalgebras pdf`
- **Confidence (bibliographic):** HIGH

**5. Bergeron / 2009**
- **Title:** Algebraic Combinatorics and Coinvariant Spaces
- **Type:** Monograph
- **Venue:** CRC Press / CMS Treatises in Mathematics
- **Main result or relevant section:** Extensively details the multivariate diagonal coinvariant spaces $R_n^{(m)}$. Specifically, Chapter 3 establishes the standard presentation of the invariant ideal, the decomposition into $S_n$-isotypic components vs $GL_m$ characters, and the distinction between the $n$-dimensional permutation representation and the $(n-1)$-dimensional standard representation (achieved via translation invariance).
- **Topic needed for this proof:** The structural definition of multigraded coinvariant spaces, including the distinction between permutation and standard representations.
- **Open-access substitute for that topic:** (open-access for topic: survey on multigraded diagonal coinvariant spaces) — Bergeron / 2011 / Multivariate Diagonal Coinvariant Spaces for Complex Reflection Groups / arxiv:1105.6158 (or author's UQAM webpage).
- **Connection:** Addresses **Grader A's Critique 4** and **Grader B's Critiques 1 & 2**. The proof conflates $n$ variables per set with the $(n-1)$-dimensional standard representation. This source standardizes the exact quotients required to achieve the correct modules.
- **Web search query:** `bergeron algebraic combinatorics coinvariant spaces pdf`
- **Confidence (bibliographic):** HIGH

**6. Macdonald / 1995**
- **Title:** Symmetric Functions and Hall Polynomials (2nd Edition)
- **Type:** Book
- **Venue:** Oxford University Press
- **Main result or relevant section:** Chapter I, Section 3 (Examples on supersymmetric functions) and Section 5 (Hook shapes). It rigorously defines symmetric functions over alphabets with negative/odd signs (i.e., $X \cup Y$ or $X - Y$) and evaluates characters on these hybrid alphabets.
- **Topic needed for this proof:** Formulaic substitution of bosonic and fermionic variables into the universal Schur functions.
- **Open-access substitute for that topic:** (open-access for topic: determinantal formulas for supersymmetric Schur polynomials) — Moens, Van der Jeugt / 2003 / A determinantal formula for supersymmetric Schur polynomials / Journal of Algebraic Combinatorics.
- **Connection:** Supports the baseline operation in Step 3 of the proof (evaluating a symmetric function on the superspace $E = \mathbb{C}^{1|1}$). This is the canonical reference to justify that the universal character coefficients remain intact when evaluating at $x_1=q, x_2=z$.
- **Web search query:** `macdonald symmetric functions hall polynomials pdf`
- **Confidence (bibliographic):** HIGH
