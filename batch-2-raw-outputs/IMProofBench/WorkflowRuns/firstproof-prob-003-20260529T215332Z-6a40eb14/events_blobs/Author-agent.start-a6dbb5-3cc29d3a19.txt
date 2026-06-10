### Council member: gpt-55-pro (models/openai/gpt-55-pro) ###
I would push route 1, but not with a scalar “diagonal reach” \(T(\mathcal D)\). The missing quantitative object seems to be the **capped support function** of the zero-slice.

Let \(\lambda=p/(1-p)\le 1/2\), \(K(\mathcal A)=P(\mathcal A)\), and for \(c\ge0\) define
\[
r_{\mathcal A}(c)=\max_{A\in\mathcal A} c(A),
\qquad
\rho^\lambda_{\mathcal A}(c)
=\max\{c\cdot x:\ x\in K(\mathcal A),\ 0\le x_i\le \lambda\ \forall i\}.
\]
The cap is the key: the zero-slice only has to supply marginals of the form
\(\lambda(1-y)\), never arbitrary points above \(p{\bf1}\).

A concrete lemma I would try to prove is:

\[
\boxed{
\begin{gathered}
\mathcal F\subseteq\mathcal E\subseteq 2^{[n]}\text{ down-sets},\ c\ge0,\\
\rho^\lambda_{\mathcal E}(c)+\lambda r_{\mathcal F}(c)<\lambda c([n])
\quad\Longrightarrow\quad
Z_\lambda(\mathcal E)+\lambda Z_\lambda(\mathcal F)\le (1+\lambda)^n .
\end{gathered}}
\tag{CR}
\]

This would close the slice induction exactly. If
\[
\mathcal D=\mathcal E\cup\{A\cup\{n+1\}:A\in\mathcal F\},
\]
then \(p{\bf1}\in P(\mathcal D)\) iff there is \(y\in P(\mathcal F)\) with
\[
\lambda(1-y)\in P(\mathcal E).
\]
So if \(p{\bf1}\notin P(\mathcal D)\), the down-convex set \(P(\mathcal F)\) is disjoint from the up-convex set
\[
R_\lambda(\mathcal E):=\{y:\lambda(1-y)\in P(\mathcal E)\}.
\]
Separating them by some \(c\ge0\) gives
\[
r_{\mathcal F}(c)<\min_{y\in R_\lambda(\mathcal E)}c\cdot y
=c([n])-\lambda^{-1}\rho^\lambda_{\mathcal E}(c),
\]
which is precisely the hypothesis of (CR). Then
\[
Z_\lambda(\mathcal D)=Z_\lambda(\mathcal E)+\lambda Z_\lambda(\mathcal F)
\le(1+\lambda)^n,
\]
i.e. \(\mu_p(\mathcal D)\le1-p\).

Why this feels like the right invariant: the failed case \(p{\bf1}\in P(\mathcal D_0)\), \(p{\bf1}\notin P(\mathcal D_1)\) is not about whether \(\mathcal D_0\) reaches \(p{\bf1}\); it is about whether it reaches the reflected capped set \(\lambda(1-P(\mathcal D_1))\). Ordinary rank/diagonal capacity loses that information; \(\rho^\lambda\) keeps it.

For proving (CR), split \(\mathcal E,\mathcal F\) again in a coordinate. The exact recursion for \(\rho^\lambda\) is obtained by fixing the capped marginal \(s\in[0,\lambda]\) of that coordinate:
\[
x_{-i}=(1-s)u+s v,\qquad u\in P(\mathcal E_0),\ v\in P(\mathcal E_1),
\]
with the coordinatewise cap \((1-s)u+sv\le\lambda{\bf1}\). This gives a genuine two-slice Bellman induction, with the cap preventing the supercritical escape that breaks scalar HUG. Equality should be forced by dictatorships, matching the known extremal case. I am not certain (CR) is true, but it is the invariant I would now test computationally and try to induct on.

### Council member: opus_47_max (models/anthropic/opus_47_max) ###
I'll focus on Route 1 with a concrete proposal; brief Route 2 at the end.

**Why scalar invariants fail.** The natural strengthening $\mu_p>1-p\Rightarrow T(\mathcal{D})\ge\lambda=p/(1-p)$ FAILS at $m=3, p=1/3, \mathcal{D}=\{|A|\le 1\}$: $\mu_p=20/27>2/3$ but $T=1/3=p$, not $\lambda=1/2$. So $T$ pegs at $p$ across an open range of $\mu_p$; any scalar "$T$ vs $\mu_p$" tradeoff has a discontinuity at the dictator boundary, killing simple slice inductions.

**Concrete proposal: reduce to shifted (left-compressed) down-sets, then close by an explicit mixture.**

*Reduction step.* Given a witness $w\ge 0$, $\sum w_i=1$, $\max_{A\in\mathcal{D}}w(A)<p$, sort $w_1\le\cdots\le w_m$. The standard combinatorial shift $S_{ij}$ ($i<j$) preserves: (a) down-set property; (b) $\mu_p$ (size-preserving, hence product measure preserved); (c) the bound $\max_\mathcal{D}w(A)<p$, since $w_i\le w_j\Rightarrow w(S_{ij}A)\le w(A)$. Iterate to a left-compressed $\mathcal{D}$ with sorted $w$. The marginal vector $d_i=\mu_p\{A\in\mathcal{D}:i\in A\}$ then satisfies $d_1\ge\cdots\ge d_m$; coordinate $m$ becomes the binding constraint.

*Lemma to attempt.* For $p\le1/3$ and any left-compressed down-set $\mathcal{D}\subseteq 2^{[m]}$ with $\mu_p(\mathcal{D})>1-p$, the mixture
$$\nu=(1-\alpha)\cdot\bigl(\mu_p|_{\mathcal{D}\cap\{m\notin A\}}\text{-conditional}\bigr)+\alpha\cdot\bigl(\text{uniform on }\mathcal{D}\cap\{m\in A\}\bigr)$$
has all marginals $\ge p$ for some $\alpha\in[p,1]$.

The $m$-marginal is $\alpha\ge p$ by construction. Other coordinates use the explicit colex structure: the $m$-present slice is the colex-initial segment of $\binom{[m]}{k^*}$ ending at $m$, where $k^*=\max|A|_\mathcal{D}$. The lemma asserts: for $p\le1/3$, the loss from boosting the $m$-marginal by mixing with the small uniform piece is compensated by the gain on coords $i<m$. The arithmetic works because $\lambda\le 1/2$ balances the boost.

Dictator $\mathcal{D}_m$ saturates: $\mu_p=1-p$, no excess, $\alpha=p$, all other marginals at boundary. The "dictator+singleton" perturbation is exactly the regime where the lemma is most delicate, and the regime your sharpness examples live in.

I haven't worked the closing step in full, but it reduces to a finite combinatorial computation on colex-initial segments — tractable, in the style of Frankl 1976 [Frankl]. Key sanity check: for symmetric $\mathcal{D}=\{|A|\le k^*\}$ this becomes a binomial-tail identity that's easy to verify by hand.

**Route 2 (briefly).** When $a|b$, Baranyai's 1-factorization gives the deterministic count for free (your reciprocal proof). For $a\nmid b$ the natural replacement is a Rödl/Pippenger near-1-factorization of $\binom{[b]}{a}$: $(1+o(1))\binom{b-1}{a-1}$ near-parallel classes, each forcing one heavy block. The deficit at $(a,b)=(3,10)$ (35 vs 36) is essentially the integer rounding loss in the nibble. Closing the finite gap needs either (i) a discharging step across overlapping near-classes, or (ii) an entropy/Loomis–Whitney bound on $\mathbb{E}[N(\mathbf{X})]$ exploiting negative covariance of color loads. I don't see a clean concrete lemma here, and the asymptotic-packing-plus-finite-correction structure feels less tractable than Route 1's direct combinatorial reduction.

### Council member: gemini-31-pro (models/gemini/gemini-31-pro) ###
I strongly recommend focusing on **Route 1 (Down-set convex hull)**. You correctly identified that the naive slice induction hits a wall because knowing $p \mathbf{1} \in P(\mathcal{D}_0)$ and $p \mathbf{1} \notin P(\mathcal{D}_1)$ is insufficient. The quantitative state you need to close this is the **maximal diagonal coordinate** of the convex hull. 

Here is the exact kinematic update for that state, the reason a naive 1D envelope fails, and the precise lemma you can prove.

### 1. The Exact Slicing Kinematics
For any down-set $\mathcal{D}$, define its diagonal reach as:
$$ V(\mathcal{D}) = \max \{t \ge 0 : t\mathbf{1} \in P(\mathcal{D})\} $$
Under the slice decomposition $\mathcal{D} = \mathcal{D}_0 \cup \{A \cup \{n\} : A \in \mathcal{D}_1\}$, let $u = V(\mathcal{D}_0)$ and $v = V(\mathcal{D}_1)$ (where $v \le u$). The diagonal reach of the full down-set is exactly:
$$ z = V(\mathcal{D}) = \frac{u}{1+u-v} $$
*(Proof sketch: $P(\mathcal{D})$ contains points of the form $(1-w)(x_0, 0) + w(x_1, 1)$. To find the maximal $z\mathbf{1}$, set $x_0 = u\mathbf{1}$ and $x_1 = v\mathbf{1}$. Setting all coordinates equal requires $z = (1-z)u + zv$, yielding $z = \frac{u}{1+u-v}$.)*

This explicitly quantifies your blind spot: a supercritical 0-slice ($u \ge p$) will still be dragged down to $z < p$ if the 1-slice is too sparse—specifically, whenever $v < p - \frac{1-p}{p}(u-p)$.

### 2. The "Frankenstein" Obstruction
You might be tempted to define a dimension-free bounding function $M(x)$ such that $\mu_p(\mathcal{D}) \le M(V(\mathcal{D}))$ and attempt to solve the 1D Bellman inequality $M(z) \ge (1-p)M(u) + p M(v)$. 

This continuous approach is doomed. The Bellman envelope implicitly allows "Frankenstein" down-sets that mix an $n=3$ zero-slice with an $n=1$ one-slice. Because the 1-slice $\mathcal{D}_1$ has bounds strictly dictated by its ambient dimension $n-1$, stripping away $n$ allows impossible probability mass to leak into the subcritical region $z < p$. 

### 3. The Concrete Lemma to Prove
To close the induction, you must carry the dimension $n$ as part of the state, applying it to the partition function $Z_\lambda(\mathcal{D}) = \sum_{A\in\mathcal{D}} \lambda^{|A|}$ (where $\lambda = \frac{p}{1-p} \le 1/2$).

**Proposed Lemma:**
For each integer $n \ge 1$ and $x \in [0,1]$, define the maximal partition function:
$$ Z_n(x) = \max_{\mathcal{D} \subseteq 2^{[n]}} \{ Z_\lambda(\mathcal{D}) : V(\mathcal{D}) \le x \} $$
Prove by induction on $n$ that $Z_n(x) \le (1+\lambda)^{n-1}$ for all $x < p$.

The inductive step relies on bounding $Z_n(z)$ via:
$$ Z_n(z) \le \sup_{0 \le v \le u \le 1} \left\{ Z_{n-1}(u) + \lambda Z_{n-1}(v) \;\middle|\; \frac{u}{1+u-v} \ge z \right\} $$
By tracking $n$ explicitly, the boundary conditions remain rigid. For example, if $v=0$, the only valid down-set in $n-1$ variables is the empty set, meaning $Z_{n-1}(0)$ is strictly $0$ (not $(1+\lambda)^{n-2}$). This seals the leak that breaks the continuous induction. 

*(Tip: Under the mapping $S(x) = \frac{x}{1-x}$, the nonlinear update simplifies beautifully to $S(z) = S(u)\frac{1+S(v)}{1+S(u)}$, which may help structure the algebraic bounds).*

This gives you a rigorous, scalar-driven DP state to execute Route 1.