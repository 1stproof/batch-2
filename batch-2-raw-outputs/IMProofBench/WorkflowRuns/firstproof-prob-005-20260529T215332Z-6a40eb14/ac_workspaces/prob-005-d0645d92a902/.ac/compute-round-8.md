# Compute worker reply — round 8
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-005-20260529T215332Z-6a40eb14/ac_workspaces/prob-005-d0645d92a902/compute
zip: /data/output/workflow_runs/firstproof-prob-005-20260529T215332Z-6a40eb14/agents/Compute-c0-a79e51/compute_workspace_round_8.zip

---

## Round 8 audit: ABLM approximation, Hilbert drift estimate, and BZ fallback

Files checked: `problem_documents_readonly/answer.tex`, `problem_documents_readonly/research_notes.tex`, `papers/pdf/2011.13498_ABLM2024.pdf`, `papers/text/2011.13498_ABLM2024.txt`, `papers/pdf/1105.2779_BZ2014.pdf`, `papers/text/1105.2779_BZ2014.txt`.

### Bottom line

The Hilbert drift estimate in `answer.tex` is plausibly correct, but the proof as written has two fixable gaps:

1. The passage \(K^n\to K\) is not justified by the displayed semigroup convergence \(P_t^n\Phi(x)\to P_t\Phi(x)\). One must explicitly assume/cite the ABLM Theorem 2.10-style common-noise approximation. Under that stronger approximation, \(K^n\to K\) follows by subtracting the common stochastic convolution, so lower semicontinuity is valid.
2. The line "apply the Hilbert-valued stochastic sewing lemma of Le in semigroup form" is not directly a theorem statement in ABLM/Le. It should be replaced by a short Hilbert \(L^2\) semigroup sewing lemma. The exponent check works: the martingale defect has exponent \(3/4=1/2+1/4\), strictly above the sewing threshold.

I do **not** see a directly citable Bounebache--Zambotti result that replaces the Hilbert drift estimate for all deterministic initial conditions. BZ give a quasi-regular Dirichlet-form solution and a resolvent/transition absolute-continuity statement only in the Dirichlet-form/quasi-everywhere sense; it does not remove the exceptional-set issue for arbitrary invariant measures of the ABLM all-starting semigroup.

### ABLM24 approximation and \(K^n\to K\)

ABLM24 = Athreya--Butkovsky--Le--Mytnik, CPAM 77 (2024), 2708--2777; the local copy is the arXiv text `2011.13498_ABLM2024`. It explicitly says near the start that they deliberately do not treat Dirichlet boundary conditions, so any use here depends on the problem's stipulated Dirichlet extension.

Relevant statements:

- Definition 2.3: a solution is \(u_t(x)=P_tu_0(x)+K_t(x)+V_t(x)\), and for every smooth \(b_n\to b\) in \(B_{q}^{\beta-}\),
  \[
  \sup_{t\le T_0,x\in D, |x|\le N}
  \left|\int_0^t\!\!\int_D p_{t-r}(x,y)b_n(u_r(y))\,dy\,dr-K_t(x)\right|\to0
  \]
  in probability. This is convergence of the additive functional built on the **limit path** \(u\).
- Theorem 2.10: for smooth approximating equations \(u^n\) with \(b_n\to b\) and \(u_0^n\to u_0\), \(u^n\to u\) uniformly in probability on compact time-space sets; part (3) gives the \(V(3/4)\) estimate for the limit.
- Since the approximating equations are driven by the same white noise in Theorem 2.10,
  \[
  K_t^n=u_t^n-P_tu_0^n-V_t,\qquad K_t=u_t-P_tu_0-V_t,
  \]
  so \(K^n\to K\) in probability in the same topology, provided \(u_0^n\to u_0\). Thus the full mild decomposition convergence is an immediate consequence, but it is **not** stated as the displayed semigroup convergence in `answer.tex`.
- Proposition 3.8: for a non-negative finite measure \(b\), every solution belongs to \(V(3/4)\). Its proof uses Theorem 4.7, the stochastic sewing lemma with random controls. This is pointwise in space in ABLM's non-Dirichlet setting.

Recommended edit in `answer.tex`: replace the sentence

> the limit follows by lower semicontinuity along the ABLM approximation of the mild decomposition

by a precise hypothesis/citation:

> We use the Dirichlet extension of ABLM Theorem 2.10 in its common-noise form: \(u^n\to u\) in probability locally uniformly on \((0,T]\times[0,1]\). Since \(K^n=u^n-S_\cdot x-V\) and \(K=u-S_\cdot x-V\), \(K^n\to K\) in probability in \(C([\varepsilon,T];H)\) for every \(\varepsilon>0\). Hence for fixed \(s<t\), \(D_{s,t}^n\to D_{s,t}\) in probability in \(H\), and Fatou gives the \(L^2(H)\) bound for \(K\).

For \(s=0\), use \(K_0=0\) and fixed-time convergence of \(K_t^n\).

### Analytic estimates in Lemma `Hilbert drift estimate`

The Dirichlet variance estimate is correct:
\[
\rho_\tau(y)=\int_0^\tau p_{2a}^D(y,y)\,da \asymp \sqrt{\tau}\wedge d(y),
\qquad d(y)=y\wedge(1-y),
\]
with constants depending at most on the fixed horizon. On the half-line,
\[
p_{2a}^+(y,y)\simeq a^{-1/2}\{1-\exp(-c y^2/a)\},
\]
whose integral is \(\asymp y\) when \(y\le\sqrt\tau\) and \(\asymp\sqrt\tau\) when \(y\ge\sqrt\tau\). Localization/reflection and the finite Green function give the interval estimate with \(d(y)\).

The weighted integral estimates used for \(A^n_{s,t}\) are also correct:
\[
\int_0^1\rho_\tau(y)^{-1/2}\,dy\lesssim \tau^{-1/4},
\]
and
\[
\sup_z\int_0^1 p_a^D(z,y)\rho_\tau(y)^{-1/2}\,dy
\lesssim a^{-1/4}+\tau^{-1/4}.
\]
Indeed \(\rho_\tau^{-1/2}\lesssim \tau^{-1/4}+d^{-1/2}\), while
\(\sup_z\int p_a^D(z,y)d(y)^{-1/2}dy\lesssim a^{-1/4}\) by half-line scaling near the boundary. Constants are harmless on finite horizons.

Then the frozen estimate
\[
\|A^n_{s,t}\|_{L^2(\Omega;H)}\lesssim |t-s|^{3/4}
\]
follows as written. For \(s<r<q<t\), sequential conditioning gives
\[
\mathbb E_s b_n(Z_r(y))b_n(Z_q(z))
\lesssim \rho_{r-s}(y)^{-1/2}\rho_{q-r}(z)^{-1/2},
\]
using only non-negativity and \(\|b_n\|_1=1\). The \(H\)-inner product of heat kernels gives \(p_{2t-r-q}(y,z)\), and the resulting two-time integral scales like
\[
\int_s^t\int_r^t
\bigl((2t-r-q)^{-1/4}+(r-s)^{-1/4}\bigr)(q-r)^{-1/4}\,dq\,dr
\asymp |t-s|^{3/2}.
\]

The Hardy step is valid:
\[
\|\rho_\tau^{-1}S_\tau f\|_2\lesssim \tau^{-1/2}\|f\|_2.
\]
Since \(\rho_\tau^{-1}\lesssim \tau^{-1/2}+d^{-1}\),
\[
\|S_\tau f/d\|_2\lesssim \|\partial_xS_\tau f\|_2\lesssim \tau^{-1/2}\|f\|_2
\]
by Hardy on \(H_0^1(0,1)\) and the Dirichlet heat semigroup gradient bound. Minor edit: in the derivative Gaussian-convolution bound, write \(|h(y)|\), not \(h(y)\), since \(D^n_{s,u}\) has no sign.

### Sewing step: exponent check and fix

The stochastic sewing implication
\[
Y_n(h)\le C+C h^{1/2}Y_n(h)
\]
does follow, but the proof should include the missing Hilbert semigroup sewing lemma.

For \(s<u<t\), the conditional estimate is
\[
\|\mathbb E_u\delta A^n_{s,u,t}\|_H
\lesssim (t-u)^{1/2}\|D^n_{s,u}\|_H.
\]
Taking \(L^2\) and using the tower property,
\[
\|\mathbb E_s\delta A^n_{s,u,t}\|_{L^2(H)}
\le \|\mathbb E_u\delta A^n_{s,u,t}\|_{L^2(H)}
\lesssim Y_n(h)(u-s)^{3/4}(t-u)^{1/2}
\lesssim Y_n(h)(t-s)^{5/4}.
\]
So the drift/mean sewing exponent is \(1+\varepsilon_1=5/4\).

For the martingale defect,
\[
\|\delta A^n_{s,u,t}\|_{L^2(H)}
\le \|A^n_{s,t}\|+\|A^n_{s,u}\|+\|A^n_{u,t}\|
\lesssim (t-s)^{3/4},
\]
hence
\[
\|\delta A^n_{s,u,t}-\mathbb E_s\delta A^n_{s,u,t}\|_{L^2(H)}
\lesssim (t-s)^{3/4}.
\]
This is \(1/2+\varepsilon_2\) with \(\varepsilon_2=1/4>0\), so the martingale part is safely above the stochastic sewing threshold.

Precise compact fix: insert a lemma of the following form.

> **Hilbert semigroup stochastic sewing.** Let \(H\) be a Hilbert space and \(S_t\) contractions. For adapted \(H\)-valued \(A_{s,t}\), define \(\delta^S A_{s,u,t}=A_{s,t}-S_{t-u}A_{s,u}-A_{u,t}\). If the sewn integral \(D_{s,t}\) exists and, for midpoints \(u=(s+t)/2\),
> \[
> \|\mathbb E_s\delta^S A_{s,u,t}\|_{L^2(H)}\le \Gamma_1(t-s)^{1+\varepsilon_1},\quad
> \|\delta^S A_{s,u,t}\|_{L^2(H)}\le \Gamma_2(t-s)^{1/2+\varepsilon_2},
> \]
> then
> \[
> \|D_{s,t}-A_{s,t}\|_{L^2(H)}
> \le C\{\Gamma_1(t-s)^{1+\varepsilon_1}+\Gamma_2(t-s)^{1/2+\varepsilon_2}\}.
> \]
> Proof: fix terminal \(T\), set \(B^T_{s,t}=S_{T-t}A_{s,t}\) and \(I_t^T=S_{T-t}K_t\), apply the dyadic proof of Le/ABLM to \(B^T\). In \(L^2(H)\), martingale differences are orthogonal, so the BDG step is immediate.

Applying this on intervals of length \(\le h\) gives
\[
\|D^n_{s,t}-A^n_{s,t}\|_{L^2(H)}
\lesssim |t-s|^{3/4}+Y_n(h)|t-s|^{5/4}.
\]
Together with \(\|A^n_{s,t}\|_{L^2(H)}\lesssim |t-s|^{3/4}\), this yields
\[
Y_n(h)\le C+Ch^{1/2}Y_n(h),
\]
and absorption for small \(h\). Larger intervals can be handled by semigroup additivity; the constant then depends on \(T\) and the chosen local \(h\), but remains uniform in \(n\).

### Bounebache--Zambotti fallback

BZ = Bounebache--Zambotti, *A skew stochastic heat equation*, JTP 27 (2014), 168--201; local file `papers/text/1105.2779_BZ2014.txt`.

Their Gibbs measure is
\[
\nu(dx)\propto \exp\left(-\int_0^1 f(x_r)\,dr\right)\mu(dx).
\]
For \(f=-2{\bf 1}_{\{a>0\}}\), this is exactly the proposed \(\pi\propto \exp(2\Lambda)\gamma\), and their local-time drift formally matches \(+\delta_0(u)\).

Relevant statements:

- Proposition 2.5: there is a measurable resolvent kernel \(\rho_\lambda(x,dy)\) with \(\rho_\lambda(x,dy)\ll\nu(dy)\) for all \(x\), but the representation \(R_\lambda\varphi(x)=\int\varphi\,d\rho_\lambda(x,\cdot)\) is asserted only \(\nu\)-a.e. In the proof they get an exceptional set \(N\), prove the property on \(N^c\), and set \(\rho_\lambda(x,\cdot)\equiv0\) on \(N\). Thus this is not an all-starting-point absolute continuity result for the actual process.
- Proposition 2.7: \(P_t\) is Hilbert--Schmidt on \(L^2(\nu)\) and has an \(L^2(\nu\otimes\nu)\) density \(p_t(x,y)\), again as an \(L^2\)/\(\nu\)-a.e. statement.
- Proposition 3.1: the quasi-regular Dirichlet-form process is a weak solution of (1.6).
- Propositions 3.5 and 3.6 identify the Fukushima drift and noise outside an exceptional set.

They explicitly say in the introduction that for general \(f\) uniqueness for (1.6) is out of reach. I found no irreducibility theorem and no all-deterministic-start uniqueness/absolute-continuity theorem for the infinite-dimensional skew SPDE. Therefore BZ cannot directly replace the Hilbert drift estimate unless one adds new work proving that the ABLM process is the strict all-starting-points BZ process and that it enters \(N^c\) immediately, or that arbitrary invariant measures do not charge BZ exceptional sets.
