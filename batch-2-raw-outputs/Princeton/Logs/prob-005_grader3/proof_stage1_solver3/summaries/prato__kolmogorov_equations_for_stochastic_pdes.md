<!-- Generated 2026-05-31T01:15:20 -->
<!-- Source PDF: prato__kolmogorov_equations_for_stochastic_pdes.pdf (273516 bytes) -->
<!-- Citation: Da Prato, G. (2004). Kolmogorov Equations for Stochastic PDEs. Birkhäuser. -->

# Kolmogorov equations for stochastic PDE’s with multiplicative noise (Da Prato, 2004)

## Definitions
- **Definition 2.** A mild solution of equation (17) is a process X ∈ CW ([0, T ], H) such that
          X(t) = etA x + \int_0^t e(t−s)A σ(X(s))dW (s), t ≥ 0, x ∈ H.

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 1.** Assume that f : [0, +∞) → [0, +∞) fulfills the inequality,
                        f (t) ≤ a(t) + b \int_0^t (t − s)−1/2 f (s)ds,        t ≥ 0,
where a is continuous nonnegative and b is a nonnegative constant. Then we have,
             f (t) ≤ a(t) + b \int_0^t (t − s)−1/2 a(s)ds
                          + \int_0^t e(t−s)πb^2 (a(s) + b \int_0^s (s − σ)−1/2 a(σ)dσ).
If, in particular, a(t) = a we have
                    f (t) ≤ aeπb^2 t + 2ab \int_0^t s−1/2 eπb^2 (t−s) ds     t ≥ 0.
and
                                          f (t) ≤ 3aeπb^2 t                 t ≥ 0.
  *Proof:* Extends Gronwall's lemma by taking the convolution with the fractional term and applying the standard Gronwall inequality.

- **Lemma 3.** Let X ∈ CW ([0, T ], H). Then we have
         E(|WX (t)|2 ) = \int_0^t \sum_{h=1}^∞ e−2π^2 h^2 (t−s) E(|g(X(s))eh |2 )ds.
  *Proof:* Uses independence of the Brownian motions and Parseval's identity to compute the variance of the stochastic convolution.

- **Proposition 4.** Let X ∈ CW ([0, T ], H). Then we have
                   E(|WX (t)|2 ) ≤ 8/\sqrt{π} kgk20 , t ≥ 0.
Moreover, for all X, Y ∈ CW ([0, T ], H) we have,
                 E(|WX (t) − WY (t)|2 )
                 = 8kgk21 / (\pi\sqrt{2\pi}) \int_0^t e−(t−s)π^2 (t − s)−1/2 E[|X(s) − Y (s)|2 )]ds.
  *Proof:* Bounds the variance by integrating the fractional exponent function bound from the previous lemma.

- **Proposition 5.** For any x ∈ H there exists a unique solution X(·, x) of equation (18).
  *Proof:* Applies a standard fixed-point contraction mapping argument to the stochastic integral equation.

- **Proposition 6.** For any T > 0, x ∈ H and n ∈ N, there exists a unique solution X n (·, x) of equation (24). Moreover,
                 lim X n (·, x) = X(·, x),         in CW ([0, T ], H),
                 n→∞
where X(·, x) is the solution of (18).
  *Proof:* (no proof in this paper)

- **Lemma 7.** There exists two positive constants a1 and λ1 such that
                     E(|η z (t, x)|2 ) ≤ a1 |z|2 eλ1 t             t ≥ 0, x ∈ H.
  *Proof:* Bounds the second moment of the directional derivative using the generalized Gronwall inequality from Lemma 1.

- **Lemma 8.** Let z ∈ L2 (0, 1). Then there exists constants a2 > 0 and λ2 > 0 such that
              E(|η z (t, x)|4L2 (0,1) ) ≤ a2 eλ2 t |z|4L2 (0,1) ,     t ≥ 0, x ∈ H.
  *Proof:* Uses Burkholder's inequality on the stochastic integral and applies Gronwall's lemma to the resulting moment estimates.

- **Lemma 9.** Let z ∈ L2 (0, 1). Then there exists constants a3 > 0 and λ3 > 0 such that
  E(|(−A)1/8 η z (t, x)|4L2 (0,1) ) ≤ a3 eλ3 t |(−A)1/8 etA z|4L2 (0,1) ,                    t ≥ 0, x ∈ H.
  *Proof:* Applies Burkholder's inequality to the fractional operator and leverages the bound obtained in Lemma 8.

- **Lemma 10.** Let z ∈ L2 (0, 1). Then there exists constants a4 > 0 and λ4 > 0 such that
                E(|η z (t, x)|4L4 (0,1) ) ≤ a4 eλ4 t |z|4L2 (0,1) ,       t ≥ 0, x ∈ H.
  *Proof:* (no proof in this paper)

- **Lemma 11.** There exists constants a5 > 0 and λ5 > 0 such that for all z ∈ L2 (0, 1), we have
                   E(|ζ z (t, x)|2 ) ≤ a5 |z|4L2 (0,1)) eλ5 t ,         t ≥ 0, x ∈ H.
  *Proof:* Estimates the second directional derivative using Parseval's identity and applying Gronwall's lemma.

- **Theorem 13.** Assume that ϕ ∈ Cb2 (H), D2 ϕ(x) is of trace class for any x ∈ H and Tr [D2 ϕ] ∈ Cb (H). Let
                         u(t, x) = E[ϕ(X(t, x))],         t ≥ 0, x ∈ H,
where X(t, x) is the mild solution of (17). Then the following statements hold.
(i) For all t ≥ 0, u(t, ·) ∈ Cb1 (H) and possesses second order derivatives in
    all directions of H.
(ii) For all t > 0 and any x ∈ H we have
                                       |ux (t, x)| ≤ κ eλt kϕk1
      and
                                      |uxx (t, x)| ≤ κ eλt kϕk2 .
(iii) There exists κ1 > 0 such that for all t ≥ 0 and any x ∈ H we have
                                          ∞
                                          X
              Tr [σ 2 (x)uxx (t, x)] =          huxx (t, x)(σ(x)ek , σ(x)ek )i
                                          k=1
                                             λt                        2
                                       ≤ κ1 e kϕk2 (1 + sup kD ϕ(x)kL1 (H) ).
                                                            x∈H
(iv) For all x ∈ D(A), u(·, x) is differentiable in (0, +∞) and fulfills (26).
  *Proof:* Proves existence and bounds of derivatives by directly estimating expectations involving directional derivatives. Concludes by taking the limit of Galerkin approximations to verify the Kolmogorov equation limits.

- **Theorem 14.** Assume that λ > λ, f ∈ Cb2 (H), D2 f (x) is of trace class for any x ∈ H and Tr [D2 f ] ∈ Cb (H). Define
                   Z ∞
            ϕ(x) =        e−λt E[f (X(t, x))]dt, t ≥ 0, x ∈ H,
                         0
Then the following statements hold.
 (i) ϕ ∈ Cb1 (H) and possesses second order derivatives in all directions of H.
(ii) For all x ∈ H we have
                                                   κ
                                 |ux (t, x)| ≤        kϕk1
                                                  λ−λ
     and
                                                   κ
                                |uxx (t, x)| ≤        kϕk2 .
                                                  λ−λ
(iii) There exists κ1 > 0 such that for all x ∈ H we have
                                            ∞
                                            X
               Tr [σ 2 (x)uxx (t, x)] =           huxx (t, x)(σ(x)ek , σ(x)ek )i
                                            k=1
                                             κ1
                                        ≤       kϕk2 (1 + kD2 ϕkHS ).
                                            λ−λ
(ii) We have                                √
                                           a1
                             |ϕx (x)| ≤       kf k1 ,       x ∈ H,
                                          λ−λ
     and
                                                     κ
                   Tr [σ 2 (x)ϕxx (t, x)] ≤               kf k2 ,    x ∈ H.
                                                  (λ − l)
(iv) For all x ∈ D(A) the equation (51) is fulfilled.
  *Proof:* (immediate from Theorem 13)

- **Proposition 15.** For any f ∈ Cb (H) and any λ > 0 we have Fλ (f ) ∈ Cb (H) and the following estimate holds
                                                   1
                              kFλ (f )k0 ≤           kf k0 .
                                                   λ
Moreover there exists a unique closed operator L : D(L) ⊂ Cb (H) → Cb (H) such that for any λ > 0 and any f ∈ Cb (H) we have Fλ (f ) = R(λ, L)f.
  *Proof:* Bounds the resolvent difference using the Lipschitz estimate of the transition semigroup, then applies the Lumer-Phillips theorem.

- **Proposition 17.** Assume that f ∈ Cb2 (H), D2 f (x) is of trace class for any x ∈ H and Tr [D2 f ] ∈ Cb (H). Let moreover λ > 0 and ϕ = R(λ, L). Then ϕ2 ∈ D(L) and
                        L(ϕ2 ) = 2ϕ Lϕ + |σDϕ|2 .
  *Proof:* Evaluates the approximating Kolmogorov operator and uses resolvent identities to pass to the limit as the approximation parameter goes to infinity.

- **Theorem 18.** There is an invariant measure µ for Rt . Moreover, for any β ∈ [0, 1/4) we have
                                      Z
                                          |(−A)β x|2 µ(dx) < +∞.
                                      H
Finally, if 1/g is bounded the invariant measure µ is unique.
  *Proof:* Bounds the moments of the solution and fractional powers of the operator. Applies the Krylov-Bogoliubov theorem to show existence and Doob's theorem for uniqueness.

- **Proposition 20.** Set
 Λ = {ϕ ∈ Cb2 (H) : D2 ϕ(x) ∈ L1 (H) for all x ∈ H and Tr [D2 ϕ] ∈ Cb (H)}
and                                 [
                             Γ :=         R(λ, L)(Λ).
                                    λ>0
Then Γ is a core for Lµ .
   Moreover if ϕ ∈ Γ we have ϕ2 ∈ D(Lµ ) and the following identity holds
                         Lµ (ϕ2 ) = 2ϕ Lµ ϕ + |σDϕ|2 .
  *Proof:* Shows the range of the resolvent is dense and applies the Lumer-Phillips theorem to verify the core property.

- **Proposition 21.** The operator
                 D : Γ ⊂ L2 (H, µ) → L2 (H, µ; H), ϕ 7→ Dϕ,
is uniquely extendible to a linear bounded operator D : D(Lµ ) → L2 (H, µ; H), where D(Lµ ) is endowed with the graph norm of Lµ . Moreover, the following identity holds
               Z                    Z
                                  1
                  Lµ ϕ ϕ dµ = −        |σDϕ|2 dµ, ϕ ∈ D(Lµ ).
                H                 2 H
  *Proof:* Integrates the generator identity for the squared function with respect to the invariant measure and uses density to extend the operator.

- **Proposition 22.** Let ϕ ∈ L2 (H, µ) and t ≥ 0. Then, for any T > 0, the linear operator
      σDRt : D(Lµ ) ⊂ L2 (H, µ) → L2 (0, T ; L2 (H, µ; H)), ϕ → σDRt ϕ,
is uniquely extendible to a linear bounded operator, still denoted by σDRt , from L2 (H, µ) into L2 (0, T ; L2 (H, µ; H)). Moreover the following identity holds
              Z                   Z t        Z                    Z
                   (Rt ϕ)2 dµ +         ds       |σDRs ϕ|2 dµ =       ϕ2 dµ.
               H                   0         H                    H
  *Proof:* Integrates the chain rule for the transition semigroup with respect to time and the invariant measure.

- **Lemma 23.** Let {ϕn } ⊂ Γ and let G ∈ L2 (H, µ; H) be such that
                              lim Dϕn = G      in L2 (H, µ; H).
                              n→∞
Then, for any t ≥ 0 we have
              lim DRt ϕn = E[Xx∗ (t, x)G(X(t, x))]           in L2 (H, µ; H).
             n→∞
In particular, if Dϕn → 0 in L2 (H, µ; H) we have DRt ϕn → 0 in L2 (H, µ; H) for all t > 0.
  *Proof:* Estimates expectation differences using the invariance of the measure and the directional derivative bound.

- **Proposition 24.** Dµ is closable. Moreover, if ϕ belongs to the domain of the closure Dµ of Dµ and Dµ ϕ = 0 we have that Dµ Rt ϕ = 0 for any t > 0.
  *Proof:* Applies the integrated chain rule and Lemma 23 to show that a sequence vanishing in probability implies its gradient vanishes almost everywhere.

- **Proposition 25.** We have D(Lµ ) ⊂ W 1,2 (H, µ) with continuous embedding. Moreover, the following identity holds
             Z                     Z
                                1
                 Lµ ϕ ϕ dµ = −         |σDϕ|2 dµ, ϕ ∈ D(Lµ ).
               H                2 H
  *Proof:* Uses the gradient identity and the closedness of the gradient operator to show Cauchy sequences converge in the Sobolev space.

- **Proposition 26.** Assume that kg 0 k20 ≤ 18 π 4 . Then, for any ϕ ∈ W 1,2 (H, ν) we have
             Z                                    Z
                             a1
               |ϕ − ϕ|2 dµ ≤    kgk20 k1/gk20      |g(x)Dϕ|2 dµ,
             H               ω                   H
where ϕ = H ϕdµ and ω = π 2 − 8π −2 kg 0 k20 .
  *Proof:* Integrates the time-evolution bound of the gradient against the invariant measure to establish the variance bound.