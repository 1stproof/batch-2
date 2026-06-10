## Referee report on the revised `answer.tex`

### LaTeX contract

I independently compiled the revised `answer.tex` with `pdflatex` twice. It compiles successfully and produces an **8-page** PDF. The document uses exactly `\documentclass[12pt]{article}`, uses only the permitted `fullpage` layout package, and I found no forbidden margin changes, spacing changes, or in-document font-size changes. The LaTeX contract is satisfied.

### Literature validation

The main bibliographic references are accurate. The ABLM paper is listed as *Communications on Pure and Applied Mathematics* 77(5), 2708–2777, 2024, with DOI 10.1002/cpa.22157; the source also confirms that it treats stochastic heat equations with distributional drifts and includes measure drifts such as \(\delta_0\). ([cris.technion.ac.il](https://cris.technion.ac.il/en/publications/well-posedness-of-stochastic-heat-equationwith-distributional-dri/?utm_source=openai)) K. Lê’s “Stochastic sewing in Banach spaces” is indeed EJP 28, article 26, 2023. ([eprints.whiterose.ac.uk](https://eprints.whiterose.ac.uk/id/eprint/196312/?utm_source=openai)) Bounebache–Zambotti’s “A skew stochastic heat equation” is correctly cited as *Journal of Theoretical Probability* 27(1), 168–201, 2014. ([ideas.repec.org](https://ideas.repec.org/a/spr/jotpro/v27y2014i1d10.1007_s10959-012-0421-8.html?utm_source=openai))

### Review of the revised proof

The revision substantially addresses the earlier objections.

#### 1. Problem statement and interpretation

The previous ambiguity about the weak convergence assumption has now been explicitly handled. The draft states that the convergence
\[
P_t^n\Phi(x)\to P_t\Phi(x)
\]
is interpreted as holding for every deterministic \(x\in E\). This is the correct strength needed for a statement about invariant measures of the whole Markov semigroup. This resolves the earlier concern.

#### 2. Uniform regularized drift estimate

The proof of Lemma 1 is now much more detailed. The Dirichlet heat-kernel estimates, the boundary compensation through \(\rho_\tau(y)\asymp \sqrt{\tau}\wedge d(y)\), the Hardy inequality input, and the weighted estimates are all sufficiently justified for this context.

The conditional Gaussian estimate
\[
\E_s b_n(Z_r(y))b_n(Z_q(z))
\lesssim \rho_{r-s}(y)^{-1/2}\rho_{q-r}(z)^{-1/2}
\]
is now explained clearly via conditioning first on \(\mathcal F_s\) and then on \(\mathcal F_r\). The proof of the \(A^n_{s,t}\) estimate and the \(H\)-valued sewing argument is also now explicit enough. The earlier issue concerning the passage from \(\mathbb E_u\delta A\) to \(\mathbb E_s\delta A\) has been addressed using Jensen/tower conditioning.

The dyadic sewing lemma is proved directly, and the bootstrap
\[
Y_n(h)\le C+Ch^{1/2}Y_n(h)
\]
is now written carefully, including the extension from small to longer intervals. I do not see a remaining blocking gap in this lemma.

#### 3. Reversible reference measure and spectral gap

The construction of \(\pi_n\) and \(\pi\) is correct. The total variation convergence \(\pi_n\to\pi\) is justified by bounded convergence and the zero Lebesgue occupation time of Brownian bridge at a fixed level.

The Galerkin approximation argument has been improved. In particular, the previous concern about using boundedness of \(\Pi_m b_n(\Pi_m u)\) in \(L^\infty\) has been fixed: the revised proof correctly uses \(L^2\)-contraction of \(\Pi_m\) and the \(S_a:H\to E\) bound of order \(a^{-1/4}\).

The Holley–Stroock perturbation argument is standard and applicable because the densities \(d\pi_{n,m}/d\gamma\) are uniformly bounded above and below. Passing the spectral gap from \(m\to\infty\), and then from \(n\to\infty\), is now adequately justified using bounded convergence and total variation convergence.

#### 4. Passage to the limiting semigroup

Proposition 3 is sound. The identities for \(C_b(E)\) functions identify the relevant finite Borel measures on the Polish space \(E\), and the extension from \(C_b(E)\) to \(L^2(\pi)\) via density and \(L^2\)-contractivity is valid. This resolves the previous concern about the limiting reversibility and spectral gap.

#### 5. Fixed-time absolute continuity

This was the most delicate part of the earlier draft. The revised version now gives a convincing adapted-control/entropy argument.

The dyadic control \(F^n\) is predictable, has uniformly bounded expected \(L^2(0,t;H)\)-energy, and its terminal effect telescopes to \(K_t^n\). The proof now explicitly handles partial sums and the convergence
\[
\int_0^t S_{t-s}F_s^n\,ds=K_t^n
\]
in \(E\).

The entropy form of Girsanov is now justified through finite-dimensional Fourier projections, followed by data processing and the fact that the Fourier coordinate sigma-fields generate the Borel sigma-field of \(E\). This resolves the earlier concern about using infinite-dimensional Girsanov too tersely. The localization by \(\tau_R\), lower semicontinuity of relative entropy, and passage \(n\to\infty\) are also valid.

Finally, the Feldman–Hájek comparison between \(\nu_t^x\) and Brownian bridge measure \(\gamma\) is correctly applied: the covariance eigenvalue ratios are bounded away from zero and differ from \(1\) by a square-summable sequence, and \(S_tx\in H_0^1\).

#### 6. Final uniqueness argument

The final argument is correct. Fixed-time absolute continuity gives \(\eta\ll\pi\) for any invariant probability \(\eta\). Reversibility gives \(P_t h=h\) in \(L^1(\pi)\), and the truncation \(h_a=h\wedge a\), combined with the spectral gap, forces each \(h_a\) to be constant. Letting \(a\uparrow\infty\) gives \(h\equiv1\), hence \(\eta=\pi\).

### Overall verdict

The revision resolves the previous substantive objections. The proof now gives a complete rigorous argument under the explicitly stated all-starting-point interpretation of the approximation assumption. I find no remaining mathematical gap that affects validity, and the LaTeX contract is satisfied.