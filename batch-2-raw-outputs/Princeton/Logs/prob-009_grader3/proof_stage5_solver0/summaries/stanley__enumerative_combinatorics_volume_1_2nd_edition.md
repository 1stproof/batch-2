<!-- Generated 2026-05-31T02:13:30 -->
<!-- Source PDF: stanley__enumerative_combinatorics_volume_1_2nd_edition.pdf (4628311 bytes) -->
<!-- Citation: R. P. Stanley (2011). Enumerative Combinatorics, Volume 1 (2nd Edition). Cambridge University Press. -->

# Enumerative Combinatorics, Volume 1 (2nd Edition)

## Definitions
- **1.4.10 Definition.** Let $w = w_1 w_2 \cdots w_n \in S_n$. We say that the function $f : [n] \to \mathbb{N}$ is $w$-compatible if the following two conditions hold.
 (a) $f(w_1) \ge f(w_2) \ge \cdots \ge f(w_n)$
 (b) $f(w_i) > f(w_{i+1})$ if $w_i > w_{i+1}$ (i.e., if $i \in D(w)$)

## Lemmas, Theorems, Propositions, Corollaries
- **1.1.8 Proposition.** The infinite series $\sum_{j\ge 0} F_j(x)$ converges if and only if $\lim_{j\to \infty} \deg F_j(x) = \infty$.
  *Proof:* (no proof in this paper)

- **1.1.9 Proposition.** The infinite product $\prod_{j\ge 1} (1 + G_j(x))$, where $G_j(0) = 0$, converges if and only if $\lim_{j\to \infty} \deg G_j(x) = \infty$.
  *Proof:* (no proof in this paper)

- **1.2.1 Proposition.** Let $v = (a_1, \dots, a_d) \in \mathbb{N}^d$, and let $e_i$ denote the $i$th unit coordinate vector in $\mathbb{Z}^d$. The number of lattice paths in $\mathbb{Z}^d$ from the origin $(0, 0, \dots, 0)$ to $v$ with steps $e_1, \dots, e_d$ is given by the multinomial coefficient $\binom{a_1+\dots+a_d}{a_1,\dots,a_d}$.
  *Proof:* Maps the sequence of lattice path steps directly to coordinate choices, proving equivalence to multiset permutations.

- **1.3.1 Proposition.** (a) The map $\hat{S}_n \to S_n$ defined above is a bijection.
 (b) If $w \in S_n$ has $k$ cycles, then $\hat{w}$ has $k$ left-to-right maxima.
  *Proof:* Defined by the fundamental bijection identifying left-to-right maxima as the starting elements of cycles in standard form.

- **1.3.2 Proposition.** The number of permutations $w \in \mathfrak{S}_S$ of type $(c_1, \dots, c_n)$ is equal to $n!/1^{c_1} c_1! 2^{c_2} c_2! \cdots n^{c_n} c_n!$.
  *Proof:* Parenthesizes permutations to group cycle lengths, then counts permutations of the ordered disjoint cycles by length and starting elements.

- **1.3.3 Theorem.** We have $\sum_{n\ge 0} Z_n x^n = \exp \left( t_1 x + t_2 \frac{x^2}{2} + t_3 \frac{x^3}{3} + \cdots \right)$.
  *Proof:* Expands the exponential into a product of sums, equating the resulting coefficients to the explicit count derived in Proposition 1.3.2.

- **1.3.6 Lemma.** The numbers $c(n, k)$ satisfy the recurrence $c(n, k) = (n - 1)c(n - 1, k) + c(n - 1, k - 1), n, k \ge 1,$ with the initial conditions $c(n, k) = 0$ if $n < k$ or $k = 0$, except $c(0, 0) = 1$.
  *Proof:* Tracks whether a newly inserted element $n$ forms its own cycle or is inserted into an existing cycle of a permutation on $n-1$ elements.

- **1.3.7 Proposition.** Let $t$ be an indeterminate and fix $n \ge 0$. Then $\sum_{k=0}^n c(n, k)t^k = t(t + 1)(t + 2) \cdots (t + n - 1)$.
  *Proof:* Demonstrated via four distinct methods: semi-combinatorial recurrences, exponential generating functions evaluated with the cycle indicator, and two explicit bijections mapping cycles to integer sequences.

- **1.3.10 Proposition.** Let $n, k \in \mathbb{P}$. The number of integer sequences $(a_1, \dots, a_n)$ such that $0 \le a_i \le n - i$ and exactly $k$ values of $a_i$ equal $0$ is $c(n, k)$.
  *Proof:* Evaluates the fourth bijective proof of Proposition 1.3.7 at $t=1$.

- **1.3.11 Corollary.** The number of $w \in S_n$ with $k$ left-to-right maxima is $c(n, k)$.
  *Proof:* (immediate from 1.3.1)

- **1.3.12 Proposition.** Let $T_n = \{(a_1, \dots, a_n) : 0 \le a_i \le n - i\} = [0, n - 1] \times [0, n - 2] \times \cdots \times [0, 0]$. The map $I : S_n \to T_n$ that sends each permutation to its inversion table is a bijection.
  *Proof:* Established by providing a sequential insertion algorithm that builds a unique permutation from its inversion table.

- **1.3.13 Corollary.** Let $\text{inv}(w)$ denote the number of inversions of the permutation $w \in S_n$. Then $\sum_{w\in S_n} q^{\text{inv}(w)} = (1 + q)(1 + q + q^2) \cdots (1 + q + q^2 + \cdots + q^{n-1})$.
  *Proof:* Expresses the total inversions as a sum over the inversion table entries and factors the resulting multivariate geometric series.

- **1.3.14 Proposition.** For any $w = w_1 w_2 \cdots w_n \in S_n$ we have $\text{inv}(w) = \text{inv}(w^{-1})$.
  *Proof:* Follows immediately from the definition of inversions for a permutation and its inverse.

- **1.4.1 Proposition.** Let $S = \{s_1, \dots, s_k\}_< \subseteq [n - 1]$. Then $\alpha(S) = \binom{n}{s_1, s_2 - s_1, s_3 - s_2, \dots, n - s_k}$.
  *Proof:* Chooses strictly increasing subsequences for the regions bounded by the descent set, leading to a product of binomial coefficients.

- **1.4.3 Proposition.** The number of permutations $w \in S_d$ with $k$ excedances, as well as the number with $k + 1$ weak excedances, is equal to the Eulerian number $A(d, k + 1)$.
  *Proof:* Obtained by establishing a bijection between descents and excedances via reversed permutations and complements.

- **1.4.4 Proposition.** For every $d \ge 0$ we have $\sum_{m\ge 0} m^d x^m = \frac{A_d(x)}{(1 - x)^{d+1}}$.
  *Proof:* Proceeds by induction on $d$, differentiating the series and equating coefficients to Eulerian number recurrences.

- **1.4.5 Proposition.** We have $\sum_{d\ge 0} A_d(x) \frac{t^d}{d!} = \frac{1 - x}{1 - x e^{(1-x)t}}$.
  *Proof:* Multiplies the identity from Proposition 1.4.4 by $t^d/d!$, sums over $d$, and simplifies the resulting double sum into an exponential form.

- **1.4.6 Proposition.** We have $\sum_{w\in S_n} q^{\text{maj}(w)} = (n)!$.
  *Proof:* Constructs a recursive bijection separating permutations into compartments, cyclically shifting them to translate major index into inversion count.

- **1.4.8 Theorem.** Let $\phi$ be the bijection defined in the proof of Proposition 1.4.6. Then for all $w \in S_n$, $ID(w) = ID(\phi(w))$. In other words, $\phi$ preserves the inverse descent set.
  *Proof:* Proves by induction that the recursive bijection preserves reading sets by tracking the relative order of elements across cyclic shifts.

- **1.4.9 Corollary.** The three pairs of statistics $(\text{inv}, \text{maj})$, $(\text{inv}, \text{imaj})$, and $(\text{maj}, \text{imaj})$ have symmetric joint distributions.
  *Proof:* Derives the symmetry by composing the inverse operation with the major-to-inversion bijection, which preserves the inverse descent set.

- **1.4.11 Lemma.** Given $f : [n] \to \mathbb{N}$, there is a unique permutation $w \in S_n$ for which $f$ is $w$-compatible.
  *Proof:* Constructs an ordered partition from the function's level sets and sorts elements within each block.

- **1.4.12 Lemma.** (a) For $w \in S_d$ and $m \ge 0$ we have
 $\#A_m(w) = \binom{m + d - 1 - \text{des}(w)}{d} = \binom{m - \text{des}(w)}{d}$
 and
 $\sum_{m\ge 1} \#A_m(w) \cdot x^m = \frac{x^{1+\text{des}(w)}}{(1 - x)^{d+1}}$.
 (If $0 \le m < \text{des}(w)$, then we set $\binom{m-\text{des}(w)}{d} = 0$.)
 (b) For $f : [n] \to \mathbb{N}$ write $|f| = \sum_{i=1}^n f(i)$. Then for $w \in S_n$ we have
 $\sum_{f\in A(w)} q^{|f|} = \frac{q^{\text{maj}(w)}}{(1 - q)(1 - q^2) \cdots (1 - q^n)}$.
  *Proof:* Reduces strict inequalities at descents to weak inequalities by subtracting descent counts, then evaluates the resulting multiset combinations and geometric series.

- **1.5.1 Proposition.** Let $S_{132}(n)$ denote the set of 132-avoiding $w \in S_n$. Then $\sum_{w\in S_{132}(n)} q^{\text{inv}(w)} = \sum_\lambda q^{|\lambda|}$, where $\lambda$ ranges over all integer sequences $\lambda_1 \ge \cdots \ge \lambda_n \ge 0$ satisfying $\lambda_i \le n - i$, and where $|\lambda| = \sum \lambda_i$.
  *Proof:* (immediate from the preceding characterization of 132-avoiding diagrams)

- **1.5.3 Proposition.** (a) The number of increasing binary trees with $n$ vertices is $n!$.
 (b) The number of such trees for which exactly $k$ vertices have left successors is the Eulerian number $A(n, k + 1)$.
 (c) The number of complete (i.e., every vertex is either an endpoint or has two successors) increasing binary trees with $2n + 1$ vertices is equal to the number $E_{2n+1}$ of alternating permutations in $S_{2n+1}$.
  *Proof:* Directly translates the conditions on double rises, falls, peaks, and valleys via the established bijection mapping permutations to increasing binary trees.

- **1.5.5 Proposition.** (a) The number of unordered increasing trees on $n + 1$ vertices is $n!$.
 (b) The number of such trees for which the root has $k$ successors is the signless Stirling number $c(n, k)$.
 (c) The number of such trees with $k$ endpoints is the Eulerian number $A(n, k)$.
  *Proof:* Relies on the bijection mapping left-to-right minima and descents of a permutation to the root successors and endpoints of an unordered increasing tree.

- **1.6.1 Proposition.** We have $\sum_{n\ge 0} E_n \frac{x^n}{n!} = \sec x + \tan x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + \frac{x^6}{6!} + \frac{x^7}{7!} + \frac{x^8}{8!} + \cdots$.
  *Proof:* Splits the permutation around the largest element to derive a recurrence, yielding a separable differential equation for the exponential generating function.

- **1.6.2 Proposition.** We have $f(n) = E_n$ (an Euler number).
  *Proof:* Constructs a differential equation for the exponential generating function by conditioning on the number of subtrees of the root.

- **1.6.3 Theorem.** The $ab$-index $\Psi_n$ can be written as a polynomial $\Phi_n$ in the variables $c = a+b$ and $d = ab + ba$. This polynomial is a sum of $E_n$ monomials.
  *Proof:* Follows by grouping the terms of the ab-index into equivalent descent sets based on min-max tree operators.

- **1.6.4 Proposition.** Let $S, T \subseteq [n - 1]$. If $\omega(S) \subset \omega(T)$, then $\beta_n(S) < \beta_n(T)$.
  *Proof:* Expands the cd-index into characteristic monomials and constructs specific trees to show strict inequality when inclusion is proper.

- **1.6.5 Corollary.** Let $S \subseteq [n - 1]$. Then $\beta_n(S) \le E_n$, with equality if and only if $S = \{1, 3, 5, \dots \} \cap [n - 1]$ or $S = \{2, 4, 6, \dots \} \cap [n - 1]$.
  *Proof:* (immediate from 1.6.4)

- **1.7.1 Proposition.** Let $M = \{1^{a_1}, \dots, m^{a_m}\}$ be a multiset of cardinality $n = a_1 + \dots + a_m$. Then $\sum_{w\in S_M} q^{\text{inv}(w)} = \binom{n}{a_1, \dots, a_m}$.
  *Proof:* Provided via two methods: verifying recurrences for the q-multinomial coefficients, and explicitly standardizing multiset permutations to track inversions.

- **1.7.2 Proposition.** The number of $k$-dimensional subspaces of $\mathbb{F}_q^n$ is $\binom{n}{k}$.
  *Proof:* Counts the number of ordered bases of a $k$-dimensional subspace and divides by the number of bases per subspace.

- **1.7.3 Proposition.** Fix $j, k \in \mathbb{N}$. Then $\sum_{n\ge 0} p(j, k, n)q^n = \binom{j+k}{j}$.
  *Proof:* Identifies the generating function with the number of row-reduced echelon matrices of a given rank by mapping their free parameters to integer partitions.

- **1.8.1 Proposition.** For each $i \in \mathbb{P}$, fix a set $S_i \subseteq \mathbb{N}$. Let $S = (S_1, S_2, \dots )$, and define $P(S)$ to be the set of all partitions $\lambda$ such that if the part $i$ occurs $m_i = m_i(\lambda)$ times, then $m_i \in S_i$. Define the generating function in the variables $q = (q_1, q_2, \dots )$, $\sum_{\lambda\in P(S)} q_1^{m_1(\lambda)} q_2^{m_2(\lambda)} \cdots$. Then $F(S, q) = \prod_{i\ge 1} \left( \sum_{j\in S_i} q_i^j \right)$.
  *Proof:* Follows by direct expansion of the product and equating the resulting coefficients to the multiplicity conditions of the partitions.

- **1.8.2 Corollary.** Preserve the notation of the previous proposition, and let $p(S, n)$ denote the number of partitions of $n$ belonging to $P(S)$, that is, $p(S, n) = \#\{\lambda \vdash n : \lambda \in P(S)\}$. Then $\sum_{n\ge 0} p(S, n)q^n = \prod_{i\ge 1} \left( \sum_{j\in S_i} q^{ij} \right)$.
  *Proof:* (immediate from 1.8.1)

- **1.8.3 Proposition.** For any partition $\lambda = (\lambda_1, \lambda_2, \dots )$ we have $\sum_{i\ge 1} (i - 1)\lambda_i = \sum_{i\ge 1} \binom{\lambda_i'}{2}$.
  *Proof:* Counts a weighted sum over the squares of the Young diagram by adding either along the rows or the columns.

- **1.8.4 Proposition.** Let $c(n)$ denote the number of self-conjugate partitions $\lambda$ of $n$, i.e., $\lambda = \lambda'$. Then $\sum_{n\ge 0} c(n)q^n = (1 + q)(1 + q^3)(1 + q^5) \cdots$.
  *Proof:* Establishes a bijection mapping the diagonal hooks of self-conjugate partitions to partitions with distinct odd parts.

- **1.8.5 Proposition.** Let $q(n)$ denote the number of partitions of $n$ into distinct parts and $p_{\text{odd}}(n)$ the number of partitions of $n$ into odd parts. Then $q(n) = p_{\text{odd}}(n)$ for all $n \ge 0$.
  *Proof:* Proved via generating functions, a bijection using binary expansions of multiplicities, and a diagram-cutting bijection utilizing shifted hooks.

- **1.8.6 Proposition.** (a) We have $\prod_{i\ge 1} \frac{1}{(1 - xq^i)} = \sum_{k\ge 0} \frac{x^k q^k}{(1 - q)(1 - q^2) \cdots (1 - q^k)}$.
 (b) We have $\prod_{i\ge 1} \frac{1}{(1 - xq^i)} = \sum_{k\ge 0} \frac{x^k q^{k^2}}{(1 - q) \cdots (1 - q^k)(1 - xq) \cdots (1 - xq^k)}$.
 (c) We have $\prod_{i\ge 1} (1 + xq^i) = \sum_{k\ge 0} \frac{x^k q^{\binom{k+1}{2}}}{(1 - q)(1 - q^2) \cdots (1 - q^k)}$.
  *Proof:* Derives the formulas by identifying the generating functions with specific partition statistics: number of parts, Durfee square size (rank), and distinct parts.

- **1.8.7 Proposition.** We have
 $\prod_{k\ge 1} (1 - x^k) = \sum_{n\in\mathbb{Z}} (-1)^n x^{n(3n-1)/2}$
 $= 1 + \sum_{n\ge 1} (-1)^n ( x^{n(3n-1)/2} + x^{n(3n+1)/2} )$
 $= 1 - x - x^2 + x^5 + x^7 - x^{12} - x^{15} + x^{22} + x^{26} - \cdots$.
  *Proof:* Applies a sign-reversing involution on the Ferrers diagram by moving the last row to the diagonal or vice-versa, leaving only pentagonal numbers as fixed points.