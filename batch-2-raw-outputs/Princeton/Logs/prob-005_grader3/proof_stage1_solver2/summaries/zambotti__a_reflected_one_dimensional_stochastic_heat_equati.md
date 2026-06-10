<!-- Generated 2026-05-31T01:16:49 -->
<!-- Source PDF: zambotti__a_reflected_one_dimensional_stochastic_heat_equati.pdf (374764 bytes) -->
<!-- Citation: Zambotti, L. (2001). A reflected one-dimensional stochastic heat equation as symmetric Dirichlet process. Probability Theory and Related Fields. -->

# A reflected one-dimensional stochastic heat equation as symmetric Dirichlet process, Zambotti, L. (2001).

## Definitions
- **Definition 1.1.** Let x ∈ L2 (0, 1). An adapted process u, defined on a complete filtered probability space (Ω, F , (Ft )t , P), is a weak solution of (1.6) if
       • a.s. u ∈ C(]0, T ] × [0, 1]) and E[kut − xk2 ] → 0 as t ↓ 0
       • a.s. for dt-a.e. t the process (u(t, r), r ∈ [0, 1]) has a family of local times
         [0, 1] × R ∋ (r, t) 7→ ℓat,θ , a ∈ R, such that
                  Z θ                    Z
                      g(u(t, r)) dr =       g(a) ℓat,θ da,  θ ∈ [0, 1], t ≥ 0,
                 0                  R
       for all bounded Borel g : R 7→ R.
     • there is a Brownian sheet W such that for all h ∈ Cc2 ((0, 1)) and 0 < ε ≤ t
                    1 t ′′                      1 t
                      Z                          Z Z         Z 1
    hut − uε , hi =      hh , us iL2 (0,1) ds +       f (da)     h′ (θ) ℓas,θ dθ ds
                    2 ε                         2 ε R         0
                      Z tZ 1                                                        (1.7)
                    +        h(θ) W (ds, dθ)
                       ε     0
- **Definition 4.3.** A sequence of Hilbert spaces Hn converges to a hilbert H if there is a family of linear maps {Φn : H → Hn } such that:
                           lim kΦn (x)kHn = kxkH ,       x∈H                       (4.4)
                          n→+∞
A sequence (xn )n , xn ∈ Hn , converges strongly to a vector x ∈ H if there exists a sequence (x̃n )n in H such that x̃n → x in H and
                           lim    lim kΦm (x̃n ) − xm kHm = 0                      (4.5)
                         n→+∞ m→+∞
and (xn )n converge weakly to x if
                                 lim hxn , zn iHn = hx, ziH                        (4.6)
                                 n→+∞
for any z ∈ H and sequence (zn )n , zn ∈ Hn , such that zn → z strongly.
- **Definition 4.5.** If E n is a quadratic form on Hn , then E n Mosco-converges to the quadratic form E on H if the two following conditions hold:
Mosco I. For any sequence xn ∈ Hn , converging weakly to x ∈ H,
                                   E(x, x) ≤ lim E n (xn , xn ).                       (4.8)
                                                n→+∞
Mosco II. For any x ∈ H, there is a sequence xn ∈ Hn converging strongly to x ∈ H such that
                             E(x, x) = lim E n (xn , xn ).                   (4.9)
                                                n→+∞
- **Definition 5.4.** There is a core K ⊂ D(E) such that for any x ∈ K there exists a sequence xn ∈ D(Λn ) converging strongly to x and such that E(x, x) =
 lim Λn (xn , xn ).
n→+∞

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 2.1.** Let Γ := {γ : N∗ 7→ N : k γk < +∞}. Then there exists a complete orthonormal system (Hγ )γ∈Γ in L2 (µ) such that
                               X
                  E 0 (ϕ, ϕ) =      Λγ hϕ, Hγ i2L2 (µ) , ∀ϕ ∈ D(E 0),
                                  γ∈Γ
where Λγ is given by                              X
                                        Λγ :=          γk λ−1
                                                           k .                   (2.3)
                                                k∈N∗
In particular, the embedding D(E 0 ) 7→ L (µ) is compact.
                                                 2
  *Proof:* (no proof in this paper)
- **Proposition 2.2.** For all t > 0 the operator Pt0 : L2 (µ) 7→ L2 (µ) is Hilbert-Schmidt, i.e.                           ∞
                X
                     −2Λγ t
                              Y        1
                    e       =          −2tπ 2 k 2 < +∞,      t > 0.              (2.4)
                γ∈Γ           k=1
                                  1−e
In particular, the series
                                            X
                            p0t (x, y) :=         e−Λγ t Hγ (x) Hγ (y)
                                            γ∈Γ
converges in L2 (µ ⊗ µ) and yields an integral representation of Pt0 :
                      Z
            Pt0 ϕ(x) = ϕ(y) p0t (x, y) µ(dy),
                                                   µ−a.e. x, ∀ ϕ ∈ L2 (µ).
  *Proof:* Relies on Euler's generating function for the sequence counting eigenvalues, evaluating it at $r = e^{-2t\pi^2}$ to show convergence.
- **Proposition 2.3.** The embedding D(E 0 ) 7→ L2 (µ) is not Hilbert-Schmidt.
  *Proof:* Uses the generating function of eigenvalue counts to show the associated series diverges near 1.
- **Lemma 2.4.** The symmetric positive bilinear form (E, K) is closable in L2 (ν). We denote by (E, D(E)) the closure.
  *Proof:* Follows from the closability of the Gaussian Dirichlet form and the uniform bounds relating the reference measures.
- **Proposition 2.5.** There exists a measurable kernel (ρλ (x, dy), λ > 0, x ∈ H) such that                 Z
               Rλ ϕ(x) =     ϕ(y) ρλ (x, dy),      ν−a.e. x, ∀ ϕ ∈ L2 (ν),
and such that for all λ > 0 and for all x ∈ H we have ρλ (x, dy) ≪ ν(dy).
  *Proof:* Uses the quasi-continuity of the resolvent kernel and the Hilbert-Schmidt property of the transition semigroup to establish absolute continuity.
- **Theorem 2.6.** Let (T, D(T )) a self-adjoint linear operator on the separable Hilbert space H such that T ≥ 0 and (λ − T )−1 is a compact operator for some λ > 0. We denote by S n the family of n-dimensional subspace of H, and for n ≥ 1 we let λn the number defined as follows
                                                      hu, T uiH
                           λn := sup        inf                 .                  (2.6)
                                 G∈S n u∈(G∩D(T ))\{0} hu, uiH
Then there exists a complete orthonormal system (ψn )n≥1 such that
                               T ψn = λn ψn ,         n ≥ 1.
In other words, the sequence (λn )n≥1 is the non-decreasing enumeration of the eigenvalues of T , each repeated a number of times equal to its multiplicity. Moreover the sup in (2.6) is attained for G equal to the span of {ψ1 , . . . , ψn }.
  *Proof:* (no proof in this paper)
- **Proposition 2.7.** The operator Pt : L2 (ν) 7→ L2 (ν) is Hilbert-Schmidt and there exists a function pt ∈ L2 (ν ⊗ ν) such that
                       Z
             Pt ϕ(x) = ϕ(y) pt(x, y) ν(dy),  ν−a.e. x, ∀ ϕ ∈ L2 (ν).
  *Proof:* Applies the Minimax principle to bound the eigenvalues of the Ornstein-Uhlenbeck operator, proving the semigroup is Hilbert-Schmidt.
- **Proposition 3.1.** The Dirichlet form (E, D(E)) is quasi-regular and the associated Markov process is a weak solution of equation (1.6).
  *Proof:* Applies the Fukushima decomposition and integration by parts to identify the martingale and local-time terms, and uses Kolmogorov's criterion to establish path continuity.
- **Lemma 3.2.** The Dirichlet form (E, D(E)) is quasi-regular.
  *Proof:* Deduces quasi-regularity directly from the quasi-regularity of the stochastic heat equation's Dirichlet form.
- **Proposition 3.3.** Almost surely, for a.e. t there exists a bi-continuous family of local times [0, 1] ∋ (r, a) 7→ ℓat,r of (ut (θ), θ ∈ [0, 1]).
  *Proof:* Follows from the absolute continuity of the transition semigroup with respect to the law of a Brownian bridge.
- **Proposition 3.4.** For any h ∈ D(A) and ϕ ∈ Cb1 (H)
                                            Z                       
                                    ′′                       a
   E[ρ(β) ∂h ϕ(β)] = E ρ(β) ϕ(β) −hh , βi +       f (da) hr ℓ (dr) .                 (3.3)
                                                     R×[0,1]
  *Proof:* Combines the occupation time formula with a Cameron-Martin shift and differentiates with respect to the perturbation parameter.
- **Proposition 3.5.** There is an exceptional set N such that for all x ∈ H \ N, Px -a.s. for all t ≥ 0
                        1 t ′′             1
                         Z                   Z          Z
               [U h ]
              Nt      =     hh , us i ds +                 f (da) h′r ℓas,r ds dr (3.4)
                        2 0                2 ]0,t]×[0,1] R
where a.s. for all s > 0
             Z     Z                    Z 1
                       ′       a
           −          hr ϕ(a) ℓs,r dr =     hr ϕ(us (r)) dr,   ∀ ϕ ∈ Cb (R).
               [0,1]   R                   0
  *Proof:* Applies the Fukushima decomposition to linear functions, using the integration by parts formula to calculate the Revuz measure of the bounded-variation part.
- **Proposition 3.6.** There exists a Brownian sheet (W (t, θ), t ≥ 0, θ ∈ [0, 1]), such that
                             Z tZ 1
                    [U h ]
                  Mt       =        hθ W (ds, dθ), h ∈ H.                     (3.6)
                                             0      0
  *Proof:* Computes the quadratic variation of the continuous martingale part via its Revuz measure and applies Lévy's theorem.
- **Lemma 4.1.** There is a canonical identification between the Hilbert spaces L2 (ν) and L2 (νn ) for all n ∈ N and for positive constants c, C
                         c                                C
                           k · k2L2 (ν) ≤ k · k2L2 (νn ) ≤ k · k2L2 (ν) .  (4.3)
                         C                                c
  *Proof:* Relies on the uniform upper and lower bounds on the Radon-Nikodym densities of the regularized measures.
- **Lemma 4.2.** The symmetric positive bilinear forms (E n , K) is closable in L2 (νn ). We denote by (E n , D(E n )) the closure.
  *Proof:* Identical to the proof of Lemma 2.4.
- **Lemma 4.4.** (1) The sequence of Hilbert spaces L2 (νn ) converges to L2 (ν), by choosing Φn equal to the natural identification of equivalence classes in L2 (νn ) and L2 (ν).
      (2) un ∈ L2 (νn ) converges strongly to u ∈ L2 (ν) if and only if un → u in L2 (ν).
      (3) un ∈ L2 (νn ) converges weakly to u ∈ L2 (ν) if and only if un → u weakly in L2 (ν).
  *Proof:* Uses dominated convergence based on the uniformly bounded pointwise limits of the regularized potentials.
- **Theorem 4.6.** The Mosco convergence is equivalent to the strong convergence of the associated resolvents.
  *Proof:* (no proof in this paper)
- **Proposition 4.7.** The Dirichlet form E n on L2 (νn ) Mosco-converges to E on L2 (ν).
  *Proof:* Proves Mosco I using the integration by parts formula to express the limit of the perturbed forms, and verifies Mosco II trivially since the domains coincide.
- **Proposition 4.8.** The sequence Pnνn converges weakly to Pν in C([0, T ] × [0, 1]).
  *Proof:* Obtains finite-dimensional convergence from the Mosco convergence of the Dirichlet forms and establishes tightness via Kolmogorov's continuity criterion using Sobolev embeddings.
- **Lemma 5.1.** The process (Xt )t≥0 is associated with the Dirichlet form
                              1
                                Z
                   D(u) :=        (u̇)2 exp(−α1]−∞,0] ) dx
                              2 R
in L2 (exp(−α1]−∞,0] ) dx), where α ∈ R is defined by 1−e
                                                                     −α
                                                      1+e−α
                                                            = β.
  *Proof:* Identifies the process as a semimartingale via the Fukushima decomposition, and applies absolute continuity to the explicit Markov transition density.
- **Theorem 5.2.** The form Λn , defined in (5.3), is a regular Dirichlet form in L2 (πn ), and the associated Markov process is a weak solution of (5.7). Moreover such solution is unique in law.
  *Proof:* Uses Fukushima decomposition and Tanaka's formula to relate the local time terms to the Revuz measures. Applies Girsanov theorem to reduce uniqueness to independent skew-Brownian motions.
- **Proposition 5.3.** The sequence of Hilbert spaces (L2 (πn ))n converges to L2 (ν) in the sense of Definition 4.3.
  *Proof:* Defines projection maps via conditional expectations and applies uniform integrability alongside dominated convergence to show norm convergence.
- **Theorem 5.5.** The conditions Mosco I and Mosco II’ are equivalent to the Mosco convergence.
  *Proof:* (no proof in this paper)
- **Theorem 5.6.** The Dirichlet form Λn Mosco-converges to Λ as n → +∞.
  *Proof:* Regularizes the step functions and verifies Mosco II' on a dense subset of exponential functions. Proves Mosco I by bounding the liminf and managing cross-terms using the local time continuity for the projected Brownian bridges.
- **Lemma 5.7.** Let un ∈ L2 (πn ) be a sequence which converges weakly to u ∈ L2 (ν), and such that lim inf n Λn (un , un ) < +∞, then there is a subsequence of (un ◦ Pn )n converging to u in L2 (ν).
  *Proof:* Extracts a strongly convergent subsequence by exploiting the compact inclusion of the domain of the unperturbed Ornstein-Uhlenbeck Dirichlet form.
- **Lemma 5.8.** The sequence Qnπn converges weakly to Pν in C([0, T ]; H −1(0, 1)).
  *Proof:* Proves tightness by lifting to a Sobolev space embedding, and uses properties of conditional expectations to derive convergence of finite-dimensional distributions.
- **Lemma 6.1.** Let (Xt )t≥0 be the stationary Markov process associated with D, i.e. such that the law of X0 is γ. Suppose that there exist η ∈ ]0, 1[, ζ > 0 and p > 1 such that                                  (                  )
                         1                     2        1
                  ζ>           ,  p > max         ,              ,
                      1 + 32 η               1 − ζ η − 23 1−ζ
                                                           ζ
and                           Z
                                      kxkpW η,p (0,1) γ(dx) = Cη,p < +∞.                              (6.1)
                                  H
Then there exist θ ∈ ]0, 1[, ξ > 1 and K > 0, all depending only on (η, ζ, p), such that                       h                     i
                         E kXt − Xs kpC θ ([0,1]) ≤ K |t − s|ξ .
  *Proof:* Employs the Lyons-Zheng decomposition to bound increments in a negative Sobolev space. Interpolates this with stationary spatial regularity to achieve Hölder continuity via Sobolev embeddings.