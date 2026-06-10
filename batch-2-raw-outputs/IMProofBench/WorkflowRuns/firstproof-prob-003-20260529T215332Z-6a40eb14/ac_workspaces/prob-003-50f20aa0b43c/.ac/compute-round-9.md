# Compute worker reply — round 9
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/ac_workspaces/prob-003-50f20aa0b43c/compute
zip: /data/output/workflow_runs/firstproof-prob-003-20260529T215332Z-6a40eb14/agents/Compute-c3-62df4f/compute_workspace_round_9.zip

---

# Round 9 compute report

I read the current `answer.tex` and `research_notes.tex`.  I did not find a proof of the small-\(p\) lemma, nor a counterexample to the unit-gap inequality.  The main new outputs are:

- literature/PDF notes under `papers/round9/`;
- exact computation script `code/round9_smallp.py`;
- exact data `data/round9/round9_results.json`;
- readable computation summary `data/round9/round9_summary.md`.

## 1. Literature search

I found no theorem that directly implies the unit-gap inequality
\[
\Pr\!\left[\sum b_i(\zeta_i-p)\ge p\right]\ge {p\over q}
\Pr\!\left[\sum b_i(\zeta_i-p)<-q\right],
\qquad 0<p\le 1/3,\quad 0\le b_i\le1.
\]

Most relevant saved files:

- `papers/round9/fokkink-meester-pelekis-2023-optimizing-stakes.pdf`
- `papers/round9/fmp.txt`
- `papers/round9/mattner-2008-lower-bounds-tails-symmetric.pdf`
- `papers/round9/mattner.txt`
- `papers/round9/pinelis-2016-left-tail-domination.pdf`
- `papers/round9/pinelis.txt`
- `papers/round9/kellerer-1964-eudml.html`
- `papers/round9/mathoverflow-278117-convex-combination-bernoulli.html`
- `papers/round9/liggett-celebratio.html`

Precise theorem statements checked:

1. **Fokkink--Meester--Pelekis (2023), Theorem 4.4.**  In their notation
\[
\pi(p,t)=\sup_\gamma \Pr(S_\gamma\ge t),
\]
Theorem 4.4 proves bold play optimality when
\[
{k\over k+1}<p\le {k+1\over k+2}<t .
\]
Thus, in our complement notation \(q=1-p_{\rm orig}\), it proves
\(\Pr_q(S>q)\le q\) only when the first attainable threshold \(t_*(w)>q\) lies beyond the next reciprocal \((k+1)/(k+2)\).  It does **not** cover the near-hypotenuse strip
\[
q<t_*(w)\le {k+1\over k+2},\qquad {k\over k+1}<q<{k+1\over k+2}.
\]
FMP Proposition 4.5 proves the boundary \(p=t=(k+1)/(k+2)\) for \(k>1\) (with the known \(k=1\) exception), and Proposition 4.6 proves one adjacent isolated point.  Page 161 of the extracted text says an “array of triangles along the hypothenuse remains to be filled”; that is exactly the missing region here.

2. **Liggett (1977), “Extensions of the Erdős--Ko--Rado theorem and a statistical application.”**  The relevant application, also quoted in the saved MathOverflow page, is: if \(X_i\) are iid Bernoulli\((p)\), \(p\ge1/2\), and \(S\) is a convex combination, then
\[
\Pr(S\ge 1/2)\ge p .
\]
This is sharp and EKR-based, but it is a fixed \(1/2\)-threshold lower bound.  It does not imply the complement target \(\Pr_q(S>q)\le q\) for \(q\ge2/3\).

3. **Mattner/Kanter.**  Mattner Theorem 2.4 generalizes Kanter’s concentration inequality for sums of independent symmetric random vectors.  Corollary 2.6 gives lower bounds for \(\Pr(|S|>t)\) in terms of Bernoulli convolutions.  The hypotheses are symmetric increments and symmetric concentration windows; our centered Bernoulli increments are asymmetric \((+qb,-pb)\), and the desired estimate is a one-sided two-tail ratio.  I do not see a specialization.

4. **Pinelis.**  Pinelis Theorem 2.4 gives optimal upper bounds for \(E f(S_n)\), for sums of independent nonnegative variables, in generalized decreasing function classes, under first/second moment constraints; Corollary 2.7 gives left-tail bounds.  These bounds are moment-based and are too weak in the pivot-plus-dust equality regime.  They do not compare the two unit-separated tails with constant \(p/q\).

5. **Kellerer.**  I saved the EUDML page for Kellerer’s 1964 paper.  The available PDF in the workspace is image-only.  I found no metadata/theorem statement that can be safely cited as the Bernoulli halfspace inequality.  I would not use Kellerer as a black box unless someone extracts and verifies the exact theorem from the German text.

## 2. Bellman/martingale attempt

Let \(T=\sum_i b_i(\zeta_i-p)\), \(\lambda=p/q\).  For a residual coefficient budget \(R\) and shift \(x\), the exact Bellman value for the shifted two-tail functional is
\[
W_R(x)=\inf_{\substack{0\le b_i\le1\\ \sum b_i=R}}
\left\{
\Pr(T\ge x+p)-\lambda\Pr(T<x-q)
\right\}.
\]
It satisfies the dynamic recurrence
\[
W_0(x)=\mathbf 1_{\{0\ge x+p\}}-\lambda\mathbf 1_{\{0<x-q\}},
\]
and, formally,
\[
W_R(x)=\inf_{0\le b\le \min(1,R)}
\left(q\,W_{R-b}(x+pb)+p\,W_{R-b}(x-qb)\right). \tag{B}
\]
The desired unit-gap lemma is \(W_B(0)\ge0\) for all \(B\).

This is the cleanest Bellman state I found, but I do not have a closed-form lower solution for (B).  The obstruction to the naive shifted invariant is explicit: \(W_0(x)<0\) for every \(x>q\).  The natural stable domain
\[
x\le q-pR
\]
is preserved by both branches in (B), but it contains \(x=0\) only when \(R\le q/p\).  That is exactly the easy regime where the lower tail is empty; it misses the hard large-\(B\) dust regime.

The middle interval is algebraically unavoidable.  If
\[
U=\Pr(T\ge x+p),\quad L=\Pr(T<x-q),\quad M=\Pr(x-q\le T<x+p),
\]
then
\[
q(U-\lambda L)=U+pM-p. \tag{M}
\]
So the two-tail inequality is equivalent to \(U+pM\ge p\).  Exposing one coefficient \(b\) transforms this into the two shifted states \(x+pb\) and \(x-qb\), giving the four boundary strips already noted in earlier rounds.  I tried to use (M) as a middle-interval buffer, but no pointwise super/sub-harmonic inequality closed: the failure branch pushes \(x\) upward, and after enough failures one reaches the negative terminal zone \(x>q\).

Thus the likely proof target is not a scalar shifted invariant.  It must either solve/estimate the two-variable Bellman problem \(W_R(x)\), or exploit a non-Bellman fact about fixed nonadaptive coefficient sequences.

## 3. Computation

The exact margin tested for unit-gap was
\[
\Delta=\Pr[S\ge p(B+1)]-{p\over q}\Pr[S<p(B+1)-1].
\]
All reported values below are exact rational arithmetic.

No unit-gap counterexample was found on sorted rational grids with denominators \(8\) and \(12\), arities up to \(8\) and \(7\) respectively, restricted to the nontrivial region \(B>q/p\).  A random rational search with denominators \(24,30,36,42,60\), arities up to \(14\), and 6000 trials per \(p\), also found no smaller margins.

Best exact grid margins by \(p\):

| \(p\) | min \(\Delta\) | one witness \(b_i\) |
|---:|---:|---|
| \(1/6\) | \(763/3888\) | \(1/8,1,1,1,1,1\) |
| \(1/5\) | \(113/625\) | \(1/8,1,1,1,1\) |
| \(1/4\) | \(5/32\) | \(1/8,1,1,1\) |
| \(2/7\) | \(18/343\) | \(5/8,1,1\) |
| \(3/10\) | \(69/1000\) | \(3/8,1,1\) |
| \(1/3\) | \(1/9\) | \(1/8,1,1\) |

These minima are boundary-chamber examples with \(B\) just above \(q/p\), consistent with round 7.

### Endpoint influence

For \(D_t=\{A:w(A)<t\}\), I tested \(I_t(D_t)\ge1\) at \(t=p\) over all integer partitions of denominators \(18,24\).  No violation was found.  The all-weight search always has equality at the single atom \([1]\).  In the capped regime \(w_i<p\), the smallest influences found were all strictly \(>1\); examples:

| \(p\) | capped min \(I_p(D_p)\) |
|---:|---:|
| \(1/6\) | \(109375/34992\) |
| \(1/5\) | \(1536/625\) |
| \(1/4\) | \(2197935/1048576\) |
| \(2/7\) | \(600/343\) |
| \(3/10\) | \(39089103543/25000000000\) |
| \(1/3\) | \(86528/59049\) |

So endpoint influence remains a plausible diagnostic, but it is not yet a proof because it gives only endpoint slope and not jump control of the moving threshold.

### Coalescence strengthenings

I tested capped partition grids with denominators \(12,15\), proper blocks of size \(2,\dots,n-1\), and \(n\le10\).  No counterexample to “some proper block has nonnegative coalescence gain” was found.  No counterexample to the pair-gain dichotomy was found.

The equal-quarter trap remains the key exact obstruction to pairwise coalescence:
\[
p={3\over10},\quad q={7\over10},\quad w=(1/4,1/4,1/4,1/4).
\]
Here
\[
\Phi_q(w)=6517/10000,\qquad q-\Phi_q(w)=483/10000,
\]
and every pair has negative gain
\[
\Delta_{ij}=-147/10000.
\]
But coalescing any three coordinates has gain \(+483/10000\), taking the value up to \(q\).  The same pattern occurs at \(p=2/7\), where \(\Phi=1625/2401\), all pair gains are \(-50/2401\), and a three-block gain is \(90/2401=q-\Phi\).

For the infinite equal-weight chamber \(w_i=1/n\), \(1/n<p<1/(n-1)\),
\[
\Phi_q(w)=q^n+npq^{n-1},\qquad
\Delta_{\text{pair}}=p q^{n-2}\bigl(n-2-(n-1)q\bigr)<0,
\]
while \(\Phi_q(w)<q\).  This is still a counterexample to pair existence, not to the lemma.

## 4. Recommendations for `answer.tex`

1. Do **not** cite Kellerer, Kanter/Mattner, Pinelis, Eaton, or Liggett as proving the small-\(p\) lemma.  They are adjacent but do not imply the sharp two-tail/unit-gap inequality.

2. Keep FMP as the closest literature connection, with the exact theorem and the explicit near-hypotenuse gap.  The desired complement inequality would follow from the missing FMP strip \(\pi(q,t)\le q\) for all \(q\ge2/3\), \(t>q\).

3. If no final proof is found, the final answer should honestly state that the classification is proved outside the unresolved small-\(p\) lemma plus the listed positive families.  The full interval \([0,1/3]\) should remain a conjectural/conditional assertion.

4. The best remaining proof directions are:
   - solve the two-variable Bellman recurrence \(W_R(x)\);
   - prove a block-coalescence theorem with direct treatment of reciprocal-chamber traps;
   - turn endpoint influence \(I_p(D_p)\ge1\) into a threshold-flow proof with jump control.

