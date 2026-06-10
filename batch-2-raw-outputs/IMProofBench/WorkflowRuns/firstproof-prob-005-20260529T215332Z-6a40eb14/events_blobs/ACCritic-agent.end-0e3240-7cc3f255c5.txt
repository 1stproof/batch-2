## Referee report on revised `answer.tex`

### Verdict

The revision fixes several of the earlier presentation issues, but the proof is **still not answer-ready**. The main remaining problem is the newly added “Dirichlet replacement” proof of the \(V(3/4)\) drift estimate. This estimate is essential for the dyadic Girsanov argument, but the verification in `answer.tex` is not rigorous and appears to contain a serious gap in the claimed sewing-increment estimate (6). In particular, the displayed heat-kernel bound (3) does **not** imply the random-control estimate (6), and the natural kernel inequality needed for that implication fails near the Dirichlet boundary.

ABLM’s published paper proves the relevant \(V(3/4)\) statement for non-negative finite measure drifts in its covered settings, but those settings are \(\mathbb R\), periodic, and Neumann; ABLM explicitly state that they do not treat Dirichlet boundary conditions because the local nondeterminism bound degenerates near the boundary. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf)) The class \(\mathcal V(\kappa)\) is indeed the class controlling \(K_t-P_{t-s}K_s\), and ABLM Proposition 3.8 does state that every solution with non-negative finite measure drift belongs to \(\mathcal V(3/4)\), but again in their non-Dirichlet framework. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))

### LaTeX contract

I compile-checked the revised `answer.tex`. It compiles successfully with `pdflatex`, produces a 5-page PDF, uses exactly

```latex
\documentclass[12pt]{article}
```

and uses only the permitted `fullpage` package for layout. I did not find prohibited line-spacing, margin, or font-size changes. The LaTeX contract appears satisfied.

### Previous concerns: status

1. **Dirichlet \(V(3/4)\) estimate.**  
   The author attempted to address this by adding a boundary-compensation argument. This remains the central unresolved gap.

2. **Girsanov/state-space rigor.**  
   The revised proof is much better here. Conditional on the \(V(3/4)\) estimate, the dyadic adapted-control construction and the transfer from \(H\)-laws to \(E=C_0([0,1])\)-laws are now mostly acceptable.

3. **Extension of symmetry to \(L^1\) densities.**  
   The revised conclusion now includes a detailed-balance extension argument. This is terse but essentially fixable.

4. **Regularized reversible semigroups.**  
   The revised proof gives a clearer gradient-form explanation. It is still somewhat compressed, but this is not the main obstruction.

### Main mathematical issue: the proof of the Dirichlet \(V(3/4)\) estimate

The added section tries to prove

\[
 \|K_t(r)-S_{t-s}K_s(r)\|_{L^m}\lesssim |t-s|^{3/4}
\]

for the Dirichlet problem by replacing ABLM’s uniform local nondeterminism with boundary-weighted estimates involving

\[
 \rho_\tau(y)=\int_0^\tau p_{2a}(y,y)\,da
 \asymp \sqrt{\tau}\wedge d(y).
\]

The estimate \(\rho_\tau(y)\asymp \sqrt{\tau}\wedge d(y)\) is plausible. The first weighted integral estimate

\[
\sup_x\int_0^1 p_a(x,y)\rho_\tau(y)^{-1/2}\,dy
\lesssim a^{-1/4}+\tau^{-1/4}
\]

is also plausible and may be enough for the moment estimate (5).

However, the proof of the sewing-increment estimate

\[
 |\,\mathbb E_u\delta A^{T,n}_{s,u,t}(x)\,|
 \le C\,\lambda^T_{s,u}(x)(t-u)^{1/2} \tag{6}
\]

is not justified. In the non-Dirichlet ABLM proof, the derivative of the one-dimensional Gaussian smoothing contributes a factor \((r-u)^{-1/2}\) uniformly in the spatial point. This uniformity is what allows the positive drift increment to factor into the random control \(\lambda^T_{s,u}(x)\). The proof of ABLM Proposition 3.8 uses exactly this type of random-control sewing estimate. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/206080/7/Comm%20Pure%20Appl%20Math%20-%202023%20-%20Athreya%20-%20Well%E2%80%90posedness%20of%20stochastic%20heat%20equation%20with%20distributional%20drift%20and%20skew.pdf))

In the Dirichlet case, the derivative factor is instead roughly

\[
 \rho_{r-u}(y)^{-1}\asymp (\sqrt{r-u}\wedge d(y))^{-1},
\]

which cannot simply be pulled out of the spatial integral. To obtain (6), one would need a strong weighted bridge inequality of the form

\[
\int p_{T-r}(x,y)\rho_{r-u}(y)^{-1}
       S_{r-u}f(y)\,dy
\lesssim
(r-u)^{-1/2}S_{T-u}f(x)
\]

for non-negative \(f\). The displayed estimate (3) only proves a bound with \(f\equiv1\); it does not imply this weighted inequality with an arbitrary positive drift increment \(f=K_u-S_{u-s}K_s\).

Worse, the natural inequality above fails near the Dirichlet boundary. On the half-line model, take \(f(z)=z\), \(x=\varepsilon\), \(T-r=a\ll \varepsilon^2\), and \(\tau=r-u\) fixed with \(\varepsilon\ll\sqrt{\tau}\). Then \(S_\tau f(y)=y\), \(\rho_\tau(y)^{-1}\asymp 1/y\) near the boundary, and \(p_a(x,\cdot)\) is concentrated near \(y=x\). Thus the left side is of order \(1\), while the right side is of order \(\tau^{-1/2}S_{a+\tau}f(x)\asymp \varepsilon/\sqrt{\tau}\), which tends to \(0\) as \(\varepsilon\downarrow0\). Therefore the claimed random-control estimate cannot follow from the displayed boundary-compensation estimates as written.

This is not a cosmetic omission: estimate (6) is the bridge between the preliminary moment estimate and the stochastic sewing argument. Without a valid replacement for (6), the proof of (B) is incomplete, and without (B), the fixed-time absolute-continuity lemma is unsupported.

### Other issues in the Dirichlet replacement section

- The proof says estimates (5) and (6) are “precisely the two analytic inputs” in ABLM Proposition 3.8 and that the rest “carries over.” This is too compressed for a new boundary case. Since ABLM explicitly excluded Dirichlet boundary conditions, a rigorous solution must either prove the full adapted replacement or state it as an additional assumption.

- The positivity/random-control statement
  \[
  \lambda^T_{s,u}(x)=S_{T-u}K_u(x)-S_{T-s}K_s(x)\ge0
  \]
  is asserted but not proved in the Dirichlet limiting setting. ABLM prove the analogous monotonicity by approximation and positivity of the drift; if this is to be reused, the Dirichlet approximation and convergence hypotheses needed for that argument must be spelled out.

- The phrase “let \(b_n\ge0\) be smooth with \(\int b_n=1\)” is insufficient for uniform estimates unless one assumes the relevant uniform Besov/measure norm bounds. For the Gaussian mollifiers \(G_{1/n}\) this may be repairable, but the statement as written is broader than justified.

### Reversible Gibbs measure and spectral gap

This part is mostly sound.

The Gibbs measure

\[
\pi(dv)=Z^{-1}\exp\left(2\int_0^1{\bf1}_{\{v(r)>0\}}\,dr\right)\gamma(dv)
\]

has the correct formal sign and factor. The total-variation convergence \(\pi_n\to\pi\) is valid, using that Brownian bridge paths spend zero Lebesgue time at level zero.

The passage of invariance, reversibility, and the spectral gap from \((P_t^n,\pi_n)\) to \((P_t,\pi)\) is plausible under assumption (A). The Holley–Stroock argument is appropriate because the densities \(d\pi_n/d\gamma\) are uniformly bounded above and below.

This section is not the source of the fatal gap.

### Fixed-time absolute continuity

Conditional on (B), the dyadic adapted-control argument is good. The construction of \(F\), the energy estimate, the telescoping identity, and the localized Girsanov argument are essentially correct. The state-space transfer from \(H\) to \(E=C_0([0,1])\) has also been addressed.

But because (B) has not been rigorously established, Lemma 1 remains unproved.

### Final uniqueness argument

Assuming Proposition 1 and Lemma 1, the uniqueness argument is essentially correct. The extension of detailed balance from bounded continuous functions to bounded Borel functions could use a few more details, but it is a standard monotone-class/regularity argument and is not fatal.

### Conclusion

The revision addresses several earlier technical presentation issues, but the core new ingredient—the Dirichlet \(V(3/4)\) estimate—is not proved. The claimed derivation of the sewing-increment estimate (6) from the boundary-weighted heat-kernel estimate (3) is invalid as written and appears to fail near the Dirichlet boundary. Since this estimate is essential for fixed-time absolute continuity and hence for uniqueness, the solution is not complete.