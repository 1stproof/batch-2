<!-- Generated 2026-05-31T02:32:12 -->
<!-- Source PDF: boutonnet__properly_proximal_von_neumann_algebras.pdf (411215 bytes) -->
<!-- Citation: R. Boutonnet, A. Ioana, J. Peterson (2021). Properly proximal von Neumann algebras. Duke Mathematical Journal 170. -->

```markdown
# Properly proximal von Neumann algebras (Boutonnet, Ioana, Peterson 2021)

## Definitions
- **Definition 2.2.** [OP10a] A trace preserving action $\sigma : \Gamma \curvearrowright (Q, \tau)$ on a tracial von Neumann algebra $(Q, \tau)$ is weakly compact if there exists a state $\phi$ on $B(L^2(Q))$ such that $\phi|_Q = \tau$ and $\phi \circ \text{Ad}(u) = \phi$, for every $u \in \mathcal{U}(Q) \cup \sigma(\Gamma)$. A regular inclusion of tracial von Neumann algebras $Q \subset M$ is weakly compact if the action $\mathcal{N}_M(Q) \curvearrowright Q$ is weakly compact, where $\mathcal{N}_M(Q) = \{u \in \mathcal{U}(M) \mid uQu^* = Q\}$ denotes the normalizer of $Q$ in $M$.
- **Definition 2.3.** Consider a tracial von Neumann algebra $M$ with two von Neumann subalgebras $P, Q \subset M$. We say that a corner of $P$ embeds into $Q$ inside $M$, and write $P \prec_M Q$ if one of the following equivalent statements holds.
  (i) There exists projections $p \in P$, $q \in Q$, a *-homomorphism $\phi : pPp \rightarrow qQq$ and a non-zero element $v \in qMp$ such that $\phi(x)v = vx$ for all $x \in pPp$;
 (ii) There exists no net of unitaries $(u_n) \subset \mathcal{U}(P)$ such that $\lim_n \|E_Q(xu_ny)\|_2 = 0$ for all $x, y \in M$;
- **Definition 3.1.** Given a discrete group $\Gamma$, a boundary piece is a closed subset $X \subset \partial\Gamma$ which is invariant under the left and right $\Gamma$-actions.
- **Definition 3.4.** Fix a discrete group $\Gamma$, a closed set $X \subset \partial\Gamma$ and a bounded net of vectors $\xi_n \in \ell^2(\Gamma)$. We say that $(\xi_n)_n$ has
     • positive mass on $X$ if there exists $\varepsilon > 0$ such that for any neighborhood $U$ of $X$ inside $\Delta\Gamma$, we have $\|P_U(\xi_n)\| > \varepsilon$ for all $n$ large enough;
     • full mass on $X$ if for any neighborhood $U$ of $X$ inside $\Delta\Gamma$, we have $\lim \sup_n \|\xi_n - P_U(\xi_n)\| = 0$.
- **Definition 3.5.** In the above setting, an operator $T \in B(\ell^2\Gamma)$ is said to be compact towards $X$ if for any bounded net of vectors $\xi_n \in \ell^2\Gamma$ with full mass on $X$, we have $\lim_n \|T\xi_n\| = 0$. We denote by $K(\Gamma; X)$ the set of all operators that are compact towards $X$, and note that it is a hereditary $C^*$-subalgebra of $B(\ell^2\Gamma)$.
- **Definition 3.7.** A point $\omega \in \Delta\Gamma$ (i.e. an ultrafilter on $\Gamma$) is called an $\eta$-proximal element if for all $h \in \Gamma$, we have $\lim_{g \to \omega} ((gh) \cdot \eta - g \cdot \eta) = 0$, in the weak-* topology. We denote by $\partial_\eta\Gamma \subset \Delta\Gamma$ the set of $\eta$-proximal elements.
- **Definition 3.12.** A two-sided array of $\Gamma$ into $\pi$ is a map $b : \Gamma \rightarrow \mathcal{H}$ such that $\sup_{g \in \Gamma} \|b(sgt) - \pi_s(b(g))\| < \infty$, for all $s, t \in \Gamma$.
- **Definition 4.1.** We say that a discrete group $\Gamma$ is a properly proximal group if it admits a finite family of continuous actions on compact spaces $\Gamma \curvearrowright K_i$, $i \geq 0$, and probability measures $\eta_i \in \text{Prob}(K_i)$, $i \geq 0$, such that:
     • For all $i$, there is no $\Gamma$-invariant Borel probability measure on $K_i$;
     • $\cup_i \partial_{\eta_i}\Gamma = \partial\Gamma$.
- **Definition 5.1.** [AD87] A continuous action $\Gamma \curvearrowright K$ on a compact space is said to be amenable if there exists a net of continuous maps $P_n : K \rightarrow \text{Prob}(\Gamma)$ such that $\lim \sup_n \sup_{x \in K} \|P_n(gx) - g \cdot P_n(x)\|_1 = 0$, for all $g \in \Gamma$.
- **Definition 5.2.** Given a group $\Gamma$ and a boundary piece $X \subset \partial\Gamma$, we say that $\Gamma$ is bi-exact towards $X$ if the left $\Gamma$-action on the Gelfand spectrum of $C(X)^\Gamma_r$ is amenable.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1.** For any $d \geq 2$, the von Neumann algebra of $\Gamma := \text{SL}_d(\mathbb{Z})$ does not admit a weakly compact Cartan subalgebra. Moreover, for any free ergodic p.m.p. action $\sigma : \Gamma \curvearrowright (X, \mu)$, the crossed product $L^\infty(X, \mu) \rtimes \Gamma$ admits a weakly compact Cartan subalgebra $A$ if and only if $\sigma$ is weakly compact and, in this case, $A$ is unitary conjugate with $L^\infty(X, \mu)$.
  *Proof:* (no proof in this paper)
- **Corollary 1.2.** Let $\sigma : \text{SL}_d(\mathbb{Z}) \curvearrowright (X, \mu)$ and $\sigma' : \text{SL}_{d'}(\mathbb{Z}) \curvearrowright (X', \mu')$ be free ergodic profinite p.m.p. actions, for some $d, d' \geq 3$. If $L^\infty(X) \rtimes \text{SL}_d(\mathbb{Z})$ is isomorphic to $L^\infty(X') \rtimes \text{SL}_{d'}(\mathbb{Z})$, then $d = d'$ and the actions $\sigma$ and $\sigma'$ are virtually conjugate.
  *Proof:* (no proof in this paper)
- **Theorem 1.4.** Any properly proximal group $\Gamma$ satisfies the conclusions of Theorem 1.1.
  *Proof:* (no proof in this paper)
- **Theorem 1.5.** Let $\Gamma$ be a properly proximal, weakly amenable group. Then $L\Gamma$ has no Cartan subalgebra and $\Gamma$ is $\mathcal{C}$-rigid.
  *Proof:* (no proof in this paper)
- **Proposition 1.6.** Groups in the following classes are properly proximal:
     • Non-amenable bi-exact groups;
     • Non-elementary convergence groups;
     • Lattices in non-compact semi-simple Lie groups of arbitrary rank;
     • Groups admitting a proper cocycle into a non-amenable representation.
Moreover, the class of properly proximal groups is stable under commensurability up to finite kernels and under direct products. In contrast, properly proximal groups are never inner amenable, and therefore no infinite direct product of non-trivial groups is properly proximal.
  *Proof:* (no proof in this paper)
- **Lemma 2.1.** A compact Hausdorff space carries a diffuse Borel probability measure if and only if it contains a perfect set.
  *Proof:* Recursively partitions the perfect set to build a continuous surjection onto $\{0,1\}^\mathbb{N}$ and pulls back a diffuse measure.
- **Lemma 2.4.** Consider a tracial von Neumann algebra $M$ with two von Neumann subalgebras $P, Q \subset M$. Then $P \prec_M Q$ if and only if there exists a $P$-central state $\Phi : \langle M, e_Q \rangle \rightarrow \mathbb{C}$ which is normal on $M$ and does not vanish on $Me_QM$.
  *Proof:* (no proof in this paper)
- **Lemma 3.6.** Any approximate unit $(e_i)_{i \in I}$ of $I_0(X)$ is an approximate unit for $I(X)$. In particular, $I(X) = A_\Gamma \cap K(\Gamma; X)$.
  *Proof:* Expresses the ideals via left/right translates of $I_0(X)$ and evaluates net cutoffs over neighborhood projections.
- **Lemma 3.8.** The set $\partial_\eta\Gamma$ enjoys the following properties.
   (1) It is a closed subset of $\Delta\Gamma$.
   (2) It is left and right $\Gamma$-invariant.
   (3) If $\eta$ is $\Gamma$-invariant, then $\partial_\eta\Gamma = \Delta\Gamma$. Otherwise, $\partial_\eta\Gamma \subset \partial\Gamma$.
  *Proof:* Formulates the proximal elements as precisely the points where the continuously extended probability orbit map is right-invariant.
- **Lemma 3.9.** Assume that the measure $\eta$ is not $\Gamma$-invariant, so that $X := \partial_\eta\Gamma$ is indeed a boundary piece. Denote by $\lambda$ and $\rho$ the left and right actions of $\Gamma$ on $C(X)$, respectively. Then there exists a unital completely positive map $\theta : C(K) \rightarrow C(X)$ such that for all $g \in \Gamma$, $f \in C(K)$, we have $\theta(g.f) = \lambda_g(\theta(f))$ and $\rho_g(\theta(f)) = \theta(f)$.
  *Proof:* Integrates against the translates of the probability measure and restricts the limit maps to the closed boundary piece.
- **Lemma 3.10.** Assume that $\eta$ is not $\Gamma$ invariant and write $X := \partial_\eta\Gamma$. Denote by $C(X)^\Gamma_r$ the $C^*$-algebra of right-$\Gamma$-invariant continuous functions on $X$. We have the following two facts:
     • If there is no $\Gamma$-invariant probability measure on $K$, then there is no left-$\Gamma$-invariant state on $C(X)^\Gamma_r$,
     • If the action $\Gamma \curvearrowright K$ is topologically amenable, then the left $\Gamma$- action $\Gamma \curvearrowright C(X)^\Gamma_r$ is amenable.
  *Proof:* Transports invariant states backward via the map $\theta$ and uses the spectrum of the $C^*$-algebra to lift topological amenability.
- **Lemma 3.11.** For every boundary piece $X \subset \partial\Gamma$ there exists a continuous action of $\Gamma$ on a compact space $K$, with a probability measure $\eta \in \text{Prob}(K)$ such that $X = \partial_\eta\Gamma$. Moreover the action $\Gamma \curvearrowright K$ may be chosen so that:
     • If there is no left $\Gamma$-invariant state on $C(X)^\Gamma_r$ then there is no $\Gamma$-invariant probability measure on $K$;
     • If the action $\Gamma \curvearrowright C(X)^\Gamma_r$ is amenable then $\Gamma \curvearrowright K$ is topologically amenable.
  *Proof:* Embeds the quotient algebras over $\Delta\Gamma$ to construct a compact spectrum $K$ mapping into the boundary, using the Dirac mass to identify the exact pieces and exact group structures to preserve amenability.
- **Lemma 3.13.** If $b : \Gamma \rightarrow \mathcal{H}$ is an unbounded array then $X := \{\omega \in \Delta\Gamma \mid \lim_{g \rightarrow \omega} \|b(g)\| = +\infty\}$ is a non-empty boundary piece. Moreover there exists a unital completely positive map $\theta : B(\mathcal{H}) \rightarrow C(X)$ such that $\theta \circ \text{Ad}(\pi(g)) = \lambda_g \circ \theta$ and $\rho_g \circ \theta = \theta$, for all $g \in \Gamma$.
  *Proof:* Builds equivariant unit vector states out of normalized array points to evaluate the completely positive operators over the boundary.
- **Lemma 3.14.** Let $\pi : \Gamma \rightarrow U(\mathcal{H})$ be a representation. Let $U$ be a neighborhood of $X(\pi)$. Then there exists a weak operator topology neighborhood $O$ of $0 \in B(\mathcal{H})$ such that $\pi^{-1}(O) \subset U$.
  *Proof:* Follows directly from compactness of the boundary complement where the representation extends continuously.
- **Lemma 3.15.** Let $\pi : \Gamma \rightarrow U(\mathcal{H})$ be a representation. Let $(c_n)$ be a uniformly bounded net in $L\Gamma$. The following conditions are equivalent:
  (i) $(c_n)$ has full mass on $X(\pi)$.
 (ii) For all other representation $(\rho, K)$, all $\xi, \eta \in \mathcal{H} \otimes K \otimes \ell^2(\Gamma)$ and all uniformly bounded net $(d_n) \subset L\Gamma$ we have $\lim_{n \rightarrow \infty} \langle c_n\xi d_n, \eta \rangle = 0$.
(iii) $\lim_{n \rightarrow \infty} \langle c_n(\xi \otimes \delta_e)c^*_n, \eta \otimes \delta_e \rangle = 0$ for all $\xi, \eta \in \mathcal{H} \otimes \mathcal{H}$.
(iv) $\lim_{n \rightarrow \infty} \langle c_n(\xi \otimes \delta_e)c^*_n, \eta \otimes \delta_e \rangle = 0$ for all vectors $\xi, \eta \in \mathcal{H} \otimes \mathcal{H}$ of the form $\xi = \xi_0 \otimes \xi_0$, $\eta = \eta_0 \otimes \eta_0$, with $\xi_0, \eta_0 \in \mathcal{H}$.
  *Proof:* Projects out mass away from WOT-neighborhoods via Fourier coefficients to constrain cross terms toward zero.
- **Proposition 3.16 (Weak mixing/compact dichotomy).** Let $B \subset L\Gamma$ be a von Neumann subalgebra, and $\mathcal{G} \subset \mathcal{U}(B)$ a group which generates $B$ as a von Neumann algebra. The following are equivalent:
  (i) Some net of unitaries $(u_n) \subset \mathcal{G}$ has full mass on $X(\pi)$.
 (ii) The $L\Gamma$-bimodule $\mathcal{H} \otimes \mathcal{H} \otimes \ell^2\Gamma$ has no non-zero $B$-central vectors.
  *Proof:* Translates full mass criteria to central vectors, and uses bounds on combined matrix elements of unitaries to extract weakly closed limits when full mass is avoided.
- **Theorem 4.3.** Consider a discrete countable group $\Gamma$, and let $X \subset \partial\Gamma$ be a boundary piece. The following facts are equivalent.
  (i) There are continuous actions $\Gamma \curvearrowright K_i, i = 1, \dots, k$ on compact spaces $K_i$ with probability measures $\eta_i \in \text{Prob}(K_i)$ such that there is no $\Gamma$-invariant probability measure on any $K_i$ and such that $X \subset \cup_{i=1}^k \partial_{\eta_i}\Gamma$.
 (ii) There is a single continuous action $\Gamma \curvearrowright K$ on a compact space $K$ with a probability measure $\eta \in \text{Prob}(K)$ such that there is no $\Gamma$-invariant probability measure on $K$ and $X = \partial_\eta \Gamma$.
(iii) There is no left-$\Gamma$-invariant state on $C(X)^\Gamma_r$;
(iv) There is no left-$\Gamma$-invariant state on $(C(X)^{**})^\Gamma_r$.
In particular, if $X = \partial\Gamma$, all these conditions are equivalent to proper proximality of $\Gamma$.
  *Proof:* Employs the Hahn-Banach separation theorem on the crossed product to force weak-* invariant elements toward norm separation. Uses quasi-central approximate units to extract right-invariant functions contradicting invariant state existence.
- **Lemma 4.4.** If $X$ is a Banach space and $(x_i)$ is a net of elements in $X$ which converges *-weakly to an element $x \in X^{**}$, then we have $\inf\{\|y\| \mid y \in \text{conv}(\{x_i\})\} \leq \|x\|$.
  *Proof:* Disproves larger bounds on the infimum by separating the elements linearly via the Hahn-Banach separation theorem.
- **Lemma 4.5.** Let $A$ be a unital $C^*$-algebra with a closed ideal $I \subset A$. Suppose $\Gamma$ is a countable group which acts on $A$ by *-automorphisms which preserve $I$. If $I_0 \subset I$ is a countable set, then there exists an increasing sequence $\alpha_n \in I$, with $0 \leq \alpha_n \leq 1$, such that $\|(1 - \alpha_n)a\| \rightarrow 0$ for all $a \in I_0$, and such that $\|\alpha_n - g \cdot \alpha_n\| \rightarrow 0$ for all $g \in \Gamma$.
  *Proof:* Leverages Arveson's results on approximate units naturally quasi-central relative to crossed products.
- **Proposition 4.7.** If $\Gamma$ admits a proper two-sided array into a non-amenable representation then it is properly proximal.
  *Proof:* Pushes left-invariant limits forward through array maps to obtain a globally invariant state inside the non-amenable space for a contradiction.
- **Proposition 4.10.** We have the following stability properties.
     (1) A direct product of finitely many properly proximal groups is again properly proximal;
     (2) A co-amenable subgroup (e.g. a finite index subgroup) of a properly proximal group is properly proximal.
     (3) The class of properly proximal groups is stable under commensurability up to finite kernels.
  *Proof:* Direct products inherit proximality from coordinating covers; subgroups preserve the lack of invariant measures via bounded conditional expectation averages.
- **Proposition 4.11.** Properly proximal groups are not inner amenable.
  *Proof:* Restricts global inner amenable states of the function algebra directly to invariant states on the proper proximality boundary layer.
- **Lemma 4.12.** Take a subgroup $\Gamma < G$ and denote by $\pi : \Delta\Gamma \rightarrow \Delta G$ the continuous map extending the embedding. Assume that $G$ acts continuously on a compact space $K$ and consider also the restricted $\Gamma$ action on $K$. Then for any $\eta \in \text{Prob}(K)$, we have $\partial_\eta\Gamma \supset \pi^{-1}(\partial_\eta G)$. In the case where $\Gamma$ is discrete inside $G$, then $\pi$ is an embedding and the formula can be read as $\partial_\eta\Gamma \supset \partial_\eta G \cap \Delta\Gamma$.
  *Proof:* Synthesizes exact point separations via disjoint group neighborhoods for continuous lift embeddings into the spectrum.
- **Lemma 4.13.** Consider an almost $k$-simple, connected, simply connected algebraic group $G$ over a local field $k$. Then there are finitely many proper parabolic $k$-subgroups $P_i < G$ and measures $\eta_i \in \text{Prob}(G(k)/P_i(k))$ such that $\partial G = \cup_i \partial_{\eta_i} G$.
  *Proof:* Evaluates continuous Cartan component scaling upon the unipotent subgroup. Uses norm decay on root-spaces to force bounded sets sequentially into neighborhoods of standard flag varieties dynamically.
- **Proposition 4.14.** Consider finitely many local fields $k_i$, and semi-simple connected $k_i$-groups $G_i$. Set $G_i := G_i(k_i)$ for each $i$ and take a discrete subgroup $\Gamma$ in $G := \Pi_i G_i$ whose projection on each $G_i$ is Zariski dense. Then $\Gamma$ is properly proximal. In particular, lattices in semi-simple algebraic groups over local fields are properly proximal.
  *Proof:* Isolates non-compact limits mapping densely into simply connected simple parts. Relies on Furstenberg limits mapped into finite parabolic collections bounding any invariant measure options dynamically.
- **Corollary 4.15.** A finitely generated subgroup $\Gamma < \text{GL}_d(\mathbb{Q})$ with trivial solvable radical is properly proximal.
  *Proof:* Diagonally embeds into local fields directly separating finite components over algebraic limits satisfying lattice configurations.
- **Theorem 4.16.** Assume that $\Gamma$ is a properly proximal group. Consider a trace preserving action $\sigma : \Gamma \curvearrowright (Q, \tau)$ on a tracial von Neumann algebra. Denote $M := Q \rtimes \Gamma$. Then any weakly compact von Neumann subalgebra $P \subset M$ such that $\mathcal{N}_M(P)''$ contains $L\Gamma$ admits a corner that embeds into $Q$ inside $M$.
  *Proof:* Integrates weak compactness states factoring against limits onto the algebraic trace structure. Leverages Popa's non-embedding intertwining constraints to pull an impossible left-invariant boundary functional.
- **Theorem 4.17.** Assume that $\Gamma$ is properly proximal and weakly amenable. Consider a trace preserving action $\Gamma \curvearrowright (Q, \tau)$ on a tracial von Neumann algebra. Denote $M := Q \rtimes \Gamma$. Then for any amenable von Neumann subalgebra $P \subset M$ such that $\mathcal{N}_M(P)''$ contains $L\Gamma$ we have that $P \prec_M Q$. In particular, $\Gamma$ is Cartan-rigid.
  *Proof:* Embeds via the canonical dual co-action into the tensor construction evaluated structurally in Proposition 4.18.
- **Proposition 4.18.** Consider a group $\Gamma$ which is both properly proximal and weakly amenable. Consider also any tracial von Neumann algebra $B$ and set $M := B \overline{\otimes} L\Gamma$. Let $A \subset M$ be an amenable von Neumann subalgebra and assume that for any $g \in \Gamma$, there exists a unitary $w_g \in \mathcal{U}(B)$ such that $w_g \otimes u_g$ belongs to $\mathcal{N}_M(A)''$. Then $A \prec_M B$.
  *Proof:* Employs Popa-Vaes structures mapping normalizable approximations across basic constructions toward non-central representations. Evaluates failed embeddings as mapping structural projections onto proper invariant distributions impossible over proximal states.
- **Theorem 5.4.** Take a countable group $\Gamma$ with a non-empty boundary piece $X \subset \partial\Gamma$. The following assertions are equivalent.
  (i) $\Gamma$ is bi-exact towards $X$;
 (ii) There exists an amenable action $\Gamma \curvearrowright K$ and $\eta \in \text{Prob}(K)$ such that $X \subset \partial_\eta \Gamma$;
(iii) $\Gamma$ is exact and there exists a map $\mu : \Gamma \rightarrow \text{Prob}(\Gamma)$ such that $\lim_{g \rightarrow \omega} \|\mu(sgt) - s \cdot \mu(g)\|_1 = 0$, for all $s, t \in \Gamma$, $\omega \in X$.
  *Proof:* Slices amenable functions over compact representations sequentially, cutting away neighborhoods to push asymptotically equivariant measures uniformly out to the restricted domain limits.
- **Lemma 5.5.** Consider an exact group $\Gamma$ and a boundary piece $X \subset \partial\Gamma$. Then $\Gamma$ is bi-exact towards $X$ if and only if there exists a u.c.p. map $\theta : C^*_\lambda(\Gamma) \otimes_{\text{min}} C^*_\rho(\Gamma) \rightarrow B(\ell^2\Gamma)$ such that $\theta(x \otimes y) - xy \in K(\Gamma; X)$ (see Definition 3.5) for all $x \in C^*_\lambda(\Gamma)$, $y \in C^*_\rho(\Gamma)$.
  *Proof:* Duplicates the characterization from [BO08, Lemma 15.1.4].
- **Theorem 5.6.** Consider a group $\Gamma$ with a boundary piece $X \subset \partial\Gamma$. Assume that $\Gamma$ is bi-exact towards $X$. For any net of unitaries $(u_n) \subset \mathcal{U}(L\Gamma)$ with positive mass on $X$ (viewed as a net in $\ell^2\Gamma$), the relative commutant $(u_n)' \cap L\Gamma$ has an amenable direct summand.
  *Proof:* Integrates limits over compact bounded states intersecting exactness projections onto the minimal algebraic tensor products. Distinguishes limits isolating spatial state embeddings mapping centrally onto commutant features.
- **Proposition 5.7.** Consider a discrete group $\Gamma$ and a boundary piece $X \subset \partial\Gamma$. The following are equivalent.
  (i) There exists a map $\mu : \Gamma \rightarrow \text{Prob}(\Gamma)$ as in Theorem 5.4.(iii) ;
 (ii) There exists a two-sided array into the regular representation $b : \Gamma \rightarrow \ell^2(\Gamma)$ which is proper towards $X$, meaning that the corresponding boundary piece introduced in Lemma 3.13 contains $X$;
(iii) There exists a unitary representation $\rho : \Gamma \rightarrow U(K)$, weakly contained in the regular representation of $\Gamma$, and an array $q : \Gamma \rightarrow K$ which is proper towards $X$.
  *Proof:* States standard equivalences identical to [PV14b, Proposition 2.7].
- **Proposition 5.8.** Consider a discrete group $\Gamma$ and finitely many boundary pieces $X_i \subset \partial\Gamma$, $i = 1, \dots, n$. Assume that for each $i$, $\Gamma$ is bi-exact towards $X_i$. Then $\Gamma$ is bi-exact towards $\cup_i X_i$.
  *Proof:* Constructs a direct sum array aggregating the proper vector arrays evaluated separately for each restricted piece.
- **Corollary 5.9 (Ozawa).** The group $\Gamma := \mathbb{Z}^2 \rtimes \text{SL}_2(\mathbb{Z})$ is bi-exact.
  *Proof:* Applies bi-exact union bounds decomposing actions covering separately the projective subsets and the ambient flag variety.
- **Lemma 6.1.** Fix a tuple $\bar{k} = (k_1, \dots, k_l)$. Then for any neighborhood $U \subset \Delta\Gamma$ of $X_{\bar{k}}$, there exists $C > 0$ such that $\{g \in \Gamma \mid \frac{s_{k_j}(g)}{s_{k_j+1}(g)} \geq C \text{ for all } j\} \subset U$.
  *Proof:* Employs KAK factorization to show hypothetical violations mapping boundary flags away yield disjoint projections contradictory to the quasi-invariant flag density functions.
- **Corollary 6.2.** For all $\omega \in \partial\Gamma$ and $1 \leq i \leq n$, if $\lim_{g \rightarrow \omega} s_i(g)/s_{i+1}(g) = +\infty$, then $\omega \in X_i$. So the sets $X_i$ cover the Stone-\v{C}ech boundary: $\partial\Gamma = \cup_{i=1}^{d-1} X_i$.
  *Proof:* Deduced natively from determinant constraints enforcing at least one isolated ratio bound mapping structurally onto the separated sets via Lemma 6.1.
- **Proposition 6.3.** $\text{SL}_3(\mathbb{Z})$ is bi-exact towards $X_0$.
  *Proof:* Projects the solvable parabolic mapping directly onto amenability bounds.
- **Corollary 6.4.** Denote by $\Lambda$ either the top-left copy of $\text{SL}_2(\mathbb{Z})$ or the copy of $\mathbb{Z}^2$ inside $\Gamma := \text{SL}_3(\mathbb{Z})$:
$\Lambda = \begin{pmatrix} * & * & 0 \\ * & * & 0 \\ 0 & 0 & 1 \end{pmatrix} \simeq \text{SL}_2(\mathbb{Z}) \quad \text{or} \quad \Lambda = \begin{pmatrix} 1 & 0 & * \\ 0 & 1 & * \\ 0 & 0 & 1 \end{pmatrix} \simeq \mathbb{Z}^2.$
Then for any diffuse subalgebra $A$ of $L\Lambda$ the relative commutant $A' \cap L\Gamma$ is amenable.
  *Proof:* Verifies unity bounds on internal matrix ranks enforcing proper boundary sequence mapping via unbounded elements scaling outward appropriately.
- **Proposition 6.6.** For all $d \geq 3$, consider inside $\Gamma_d := \text{PSL}_d(\mathbb{Z})$ the following subgroup $\Lambda_d$ isomorphic to $\mathbb{Z}^{d-1}$:
$\Lambda_d := \left\{ \pm \begin{pmatrix} I_{d-1} & u \\ 0 & 1 \end{pmatrix} , u \in \mathbb{Z}^{d-1} \right\} \simeq \mathbb{Z}^{d-1}$
Then $L(\Lambda_d)$ is a maximal abelian subalgebra inside $L(\Gamma_d)$ and the inclusion $L(\Lambda_3) \subset L(\Gamma_3)$ is not isomorphic with the inclusion $L(\Lambda_d) \subset L(\Gamma_d)$ for any $d \geq 4$.
  *Proof:* Establishes infinite conjugacy classes to confirm maximal abelienness natively while showing dimension inflation centralizes against discrete non-amenable matrices uniquely.
- **Lemma 6.7.** Fix $d \geq 3$ and denote by $\Gamma := \text{GL}_d(\mathbb{Z})$ and by $\Lambda \simeq \mathbb{Z}^{d-1}$ the subgroup
$\Lambda = \left\{ \begin{pmatrix} I_{d-1} & u \\ 0 & 1 \end{pmatrix} , u \in \mathbb{Z}^{d-1} \right\} \simeq \mathbb{Z}^{d-1}.$
Then for all $g \in \Gamma$ such that $\{s g s^{-1}, s \in \Lambda\}$ is finite we have either $g \in \Lambda$, or $-g \in \Lambda$.
  *Proof:* Evaluates direct conjugations projecting arbitrary scalar variations across the vector coordinates to generate unbounded sequence options whenever disjoint components remain active.
```