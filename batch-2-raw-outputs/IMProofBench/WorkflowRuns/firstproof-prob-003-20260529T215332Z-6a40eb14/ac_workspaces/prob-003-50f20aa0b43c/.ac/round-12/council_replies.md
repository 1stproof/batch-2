### Council member: gpt-55-pro (models/openai/gpt-55-pro) ###
I would not try to adapt the FMP endpoint injection as a pointwise map on a fixed cyclic load vector; the false \(2/7\) examples rule that out. The version that still looks viable to me is a **Palm/exposure endpoint count**, where the injection is allowed to change the random allocation.

Here is the exact reduction I would isolate.

**Exposure/crossing lemma.**  Fix \(p=r/b\). Expose the weights in some order. After weights \(<i\) have been placed, let \(A_j\) be the partial load of the \(r\)-arc starting at \(j\), and define
\[
C_i=\#\{j: p-w_i\le A_j<p\}.
\]
When \(w_i\) is placed uniformly, arc \(j\) ceases to be light iff \(A_j\in[p-w_i,p)\) and the new atom lands inside that arc, an event of probability \(r/b=p\). Hence
\[
\mathbb E[N_i\mid\mathcal F_{i-1}]
=N_{i-1}-p\,C_i,
\]
where \(N_i=\#\{j:L_j^{(i)}<p\}\). Therefore
\[
\mathbb E N_{\rm final}=b-p\sum_i \mathbb E C_i.
\]
So the cyclic inequality is equivalent to
\[
\sum_i \mathbb E C_i\ge b. \tag{CI}
\]

Equivalently, in the Bernoulli language, for any chosen ordering and
\(S_{i-1}=\sum_{k<i}w_k v_k\),
\[
\Pr(S_n<p)=1-p\sum_i
\Pr\bigl(S_{i-1}\in[p-w_i,p)\bigr). \tag{*}
\]
Thus the whole theorem is equivalent to the “crossing intensity” bound
\[
\sum_i\Pr\bigl(S_{i-1}\in[p-w_i,p)\bigr)\ge1. \tag{CI'}
\]
This is where I would try to insert an FMP-style endpoint injection: not from light arcs to good arcs in the same configuration, but from each currently light arc to a future/potential threshold crossing under insertion of the next atom. Pointwise failures then become irrelevant, because the charge is over exposure states, not final load vectors. I would try decreasing order of the \(w_i\)’s first; large weights then contribute early through bands containing \(0\), and small weights reduce to a renewal/local-time estimate near level \(p\).

On the HUG/Bellman side, I think one should avoid a one-boundary induction: it is structurally unable to pass the subcritical line. With \(h=1\), put
\[
X_{\mathbf b}=\sum_i b_i(\zeta_i-p),\qquad
F_{\mathbf b}(x)=
q\Pr(X_{\mathbf b}\ge p+x)-p\Pr(X_{\mathbf b}<-q+x).
\]
HUG is \(F_{\mathbf b}(0)\ge0\). Peeling a coefficient \(c\) gives the exact harmonic recursion
\[
F_{\mathbf b}(x)=qF_{\mathbf b'}(x+pc)+pF_{\mathbf b'}(x-qc),
\]
with base
\[
F_{\varnothing}(x)=q{\bf1}_{x\le -p}-p{\bf1}_{x>q}.
\]
The existing subcritical proof is precisely the fact that if \(x\le q-pB\), the recursion never samples the negative base region \(x>q\). Moreover, any scalar positivity domain \(x\le\rho(B)\) propagated by this recursion must satisfy
\[
\rho(B)\le \rho(B-c)-pc,\qquad \rho(0)=q,
\]
hence \(\rho(B)\le q-pB\). So a supercritical Bellman proof needs an extra state, e.g. boundary-strip/local-time terms. Formula \((*)\) suggests the right extra state is exactly the accumulated crossing intensity through \([p-w_i,p)\). This also aligns naturally with the cyclic endpoint picture.

### Council member: opus_47_max (models/anthropic/opus_47_max) ###
# Council reply

## Cyclic expected inequality

By linearity of expectation plus rotational symmetry, $\mathbb{E}\#\{j: L_j < r/b\} = b\Pr[\sum w_i v_i < p]$, so your cyclic bound is *identically* the original conjecture, not a relaxation. FMP's endpoint trick does succeed despite pointwise failure of a similar count, so an argument in that flavor is in principle available — but the equivalence means it cannot be logically easier than HUG.

**Candidate injection.** Work in $\Omega = \{(\sigma, j)\}$ with uniform measure. For each light pair $(\sigma, j)$ map to $(\sigma', j)$ where $\sigma'$ rotates $\sigma$ to slide the heaviest weight into $[j, j+r)$. Required amortization: each $(\sigma', j)$ in the image is hit by $\le \lfloor q/p \rfloor$ preimages. I have not verified this; the "single heaviest" rule is too crude with several comparable large weights and probably needs an auction/lex refinement.

## Supercritical HUG: martingale picture

The base case is the real obstruction: $V(0, h, T) = -p$ for $T > h$.

**Key observation.** Track $(B, h, T, m)$ with $m = pB$. Under one-coordinate exposure with $c \in [0, h]$:
- $\zeta=0$ branch (prob $q$): $(B-c, T, m-pc)$, so $T - m \to T - m + pc$;
- $\zeta=1$ branch (prob $p$): $(B-c, T-c, m-pc)$, so $T - m \to T - m - qc$.

**So $T - m$ is a martingale** with step variance $pqc^2$. Unrolling the recursion gives exactly
$$V(\text{config}) = \mathbb{E}[V_{\text{term}}(T_0 - S)], \quad V_{\text{term}}(x) := q\mathbf 1\{x \le 0\} - p\mathbf 1\{x > h\}.$$
Your subcritical $\delta \le qh - pB$ is exactly $T_0 \le h$ at termination.

**Lemma to attempt.** *Find $\phi: \mathbb{R} \to \mathbb{R}$ with $\phi \le V_{\text{term}}$ pointwise, $\phi(ph) \ge 0$, and $\phi(x) \le q\phi(x+pc) + p\phi(x-qc)$ for all $c \in [0, h]$.*

**No-go for convex $\phi$.** Any continuous convex $\phi$ with $\phi(0) \le 0$ and $\phi(h) \le -p$ satisfies $\phi(ph) \le -p^2 < 0$ by the chord inequality. The downward jump in $V_{\text{term}}$ at $h$ obstructs convex one-variable barriers.

**Plausible fixes**, in priority order:
1. **State $M_2 = \sum_i b_i^2$.** Track $(B, T - m, M_2)$ with $M_2 \to M_2 - c^2$ per step. Chebyshev on the residual sum bounds the right-tail mass — precisely the information missing from a one-variable convex barrier.
2. **Two-variable barrier $\phi(x, B)$.** Try $\phi(x, B) = g(x) - \alpha B^\beta$ with $\beta \in [1/2, 1]$ and tune $(\alpha, \beta, g)$ to absorb the $h$-discontinuity.
3. **Non-convex piecewise $\phi$.** Try $\phi(x) = -p(x - ph)/(qh)$ on $[0,h]$ extended piecewise; verify sub-harmonicity by case analysis on whether $x \pm pc$ and $x \mp qc$ straddle $h$.

I would prioritize (1): $M_2$ directly controls the walk's variance budget, hence the probability the walk overshoots $h$ — which is the precise quantitative obstruction.

## Adjacent literature

- **Jogdeo & Samuels (1968)**, "Monotone convergence of binomial probabilities": $\Pr[\mathrm{Bin}(n,p) \ge np] \ge 1/2$ via parameter monotonicity; a weighted analogue would *be* your missing lemma.
- **Hoeffding (1956)**, "On the distribution of the number of successes": variance-extremal characterization of $\sum \mathrm{Ber}(p_i)$ at fixed mean — useful for Pinelis-style bounds on the supercritical excursion.
- Worth searching: a Pelekis paper (~2014–2017) giving lower bounds on $\Pr[\sum w_i v_i \ge \mathbb{E}]$ for weighted Bernoulli sums. My memory is vague (so: uncertain), but if such a result exists it may bear here.

My honest read: the martingale picture diagnoses the failure mode correctly (walk overshoot of $h$), but the right barrier needs an extra state coordinate. I would test (1) numerically at small $(B,h)$ and verify $p=2/7$ cyclic by direct enumeration in parallel; either result will sharpen which framework can close.

### Council member: gemini-31-pro (models/gemini/gemini-31-pro) ###
Here are two rigorous routes to bypass the barrier you’ve hit in the supercritical regime. The core realization is that **pointwise induction fails precisely where analytic concentration takes over**. 

### 1. The Hybrid HUG Route: Large Weights via Induction, Dust via Analysis

Your shifted induction perfectly solves the **subcritical** regime ($B \le qh/p$). The reason it fails in the **supercritical** regime ($B > qh/p$) is that induction is too conservative to capture the rapid Gaussian/Poisson decay of the tails for diffuse "dust." 

You do not need a Bellman function for the supercritical regime; you can solve it by splitting the proof into two domains:

**Step A (The Pivot/Dust Dichotomy):** 
Sort the remaining weights. If there is a weight large enough to serve as a pivot such that the remainder is subcritical, your existing shifted induction handles it exactly. 
If no such pivot exists, the configuration must be highly diffuse (a "dust" or cap-vector configuration) where $\max b_i \le \epsilon \sum b_i$. 

**Step B (Analytic Domination for Dust):** 
In the dust regime, $R = \sum b_i \zeta_i$ is highly concentrated around $\mu = pB$. Look at the two thresholds in HUG:
* Upper threshold: $\mu + ph$
* Lower threshold: $\mu - qh$

Because $p \le 1/3$, we have $q \ge 2p$. Thus, **the lower threshold is at least twice as far from the mean as the upper threshold.** 
For diffuse weights, standard large deviation bounds (e.g., Bennett's or Pinelis' left-tail bounds) scale with the square of the deviation. Therefore, the lower tail is bounded by the *square* (or fourth power, depending on variance) of the upper tail bound:
\[
\Pr(R \le \mu - qh) \lesssim \exp\left(-\frac{q^2 h^2}{2\sigma^2}\right) \le \left[ \exp\left(-\frac{p^2 h^2}{2\sigma^2}\right) \right]^4 \approx \Pr(R \ge \mu + ph)^4
\]
Since the upper tail probability is strictly less than 1, its fourth power is exponentially smaller. As $\max b_i \to 0$, $q \Pr(\text{Upper}) \gg p \Pr(\text{Lower})$ holds with massive room to spare. 
**Skeleton:** Formalize this by tuning $\epsilon$. If $\max b_i > \epsilon h$, peel it via induction. If $\max b_i \le \epsilon h$, terminate the induction and apply the analytic relative-tail bound.

### 2. The FMP Adaptation via the Cyclic / Size-Biased Identity

If you prefer to push the Cyclic Expectation form, your identity $\Pr(W \ge p) - p = \sum w_i D_i$ has a beautiful continuous cyclic analog that mirrors the Fokkink–Meester–Pelekis (FMP) injection.

In the cyclic model, let $L_j$ be the load of the interval of length $p$, and let $M_j = 1 - L_j$ be the load of its complement. Your identity becomes:
\[
\mathbb{E} \sum_j (M_j \mathbf{1}_{L_j \ge p} - L_j \mathbf{1}_{L_j < p}) = \mathbb{E} \sum_j \mathbf{1}_{L_j \ge p} - r \ge 0
\]
In FMP, they establish bold play by shifting winning sets to losing sets. Here, you can do this in expectation.
Because $p \le 1/3$, the complement interval has length $1-p \ge 2p$. This means the complement interval containing $M_j$ can be partitioned into $k = \lfloor (1-p)/p \rfloor \ge 2$ disjoint intervals of length $p$, say $J_{j,1}, \dots, J_{j,k}$.

Therefore, $M_j \ge \sum_{s=1}^k L(J_{j,s})$, which gives:
\[
\mathbb{E}[ M_j \mathbf{1}_{L_j \ge p} ] \ge \sum_{s=1}^k \mathbb{E}[ L(J_{j,s}) \mathbf{1}_{L_j \ge p} ]
\]
By the exchangeability/stationarity of the random cyclic allocation, the joint moments of the loads of shifted intervals depend only on their relative distances. You can use this shift-invariance to fractionally match the deficit $\mathbb{E}[L_j \mathbf{1}_{L_j < p}]$ against the $k \ge 2$ available success regions provided by the complement mass $M_j$, exactly recovering the FMP $k \to k+1$ fractional matching argument, but smoothed via expectation.