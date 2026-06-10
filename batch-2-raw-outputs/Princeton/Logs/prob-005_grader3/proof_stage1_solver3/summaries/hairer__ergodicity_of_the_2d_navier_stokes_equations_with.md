<!-- Generated 2026-05-31T01:15:11 -->
<!-- Source PDF: hairer__ergodicity_of_the_2d_navier_stokes_equations_with.pdf (784144 bytes) -->
<!-- Citation: Hairer, M., Mattingly, J. C. (2006). Ergodicity of the 2D Navier-Stokes equations with degenerate forcing. Annals of Mathematics. -->

# Ergodicity of the 2D Navier-Stokes equations with degenerate forcing (Hairer & Mattingly, 2006)

## Definitions
- **Definition 3.1.** Let {dn }∞n=0 be an increasing sequence of (pseudo-)metrics on a Polish space X . If limn→∞ dn (x, y) = 1 for all x = y, then {dn } is a totally separating system of (pseudo-)metrics for X .
- **Definition 3.6.** A Markov transition semigroup on a Polish space X is said to be strong Feller at time t if Pt ϕ is continuous for every bounded measurable function ϕ : X → R.
- **Definition 3.8.** A Markov transition semigroup Pt on a Polish space X is called asymptotically strong Feller at x if there exists a totally separating system of pseudo-metrics {dn } for X and a sequence tn > 0 such that
(3.4)              inf lim sup sup  Ptn (x, · ) − Ptn (y, · ) dn = 0 ,
                  U ∈Ux   n→∞   y∈U
It is called asymptotically strong Feller if this property holds at every x ∈ X .
- **Definition 4.6.** A step with increment   ∈ Z0 starting from j ∈ Z2 is forbidden if either |j| = | | or j and   are collinear.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 2.1.** Let Z0 satisfy the following two assumptions:
A1. There exist at least two elements in Z0 with diﬀerent Euclidean norms.
A2. Integer linear combinations of elements of Z0 generate Z2 .
Then, (2.1) has a unique invariant measure in H.
  *Proof:* Combines Corollary 4.2 and Proposition 4.4.
- **Theorem 2.3.** There are two qualitatively diﬀerent ways in which the hypotheses of Theorem 2.1 can fail. In each case there is a unique invariant measure supported on H̃, the smallest closed linear subspace of H which is invariant under (2.1).
   • In the ﬁrst case the elements of Z0 are all collinear or of the same Euclidean length. Then H̃ is the ﬁnite-dimensional space spanned by {fk | k ∈ Z0 }, and the dynamics restricted to H̃ is that of an Ornstein-Uhlenbeck process.
   • In the second case let G be the smallest subgroup of Z2 containing Z0 . Then H̃ is the space spanned by {fk | k ∈ G \ {(0, 0)}}. Let k1 , k2 be two generators for G and deﬁne vi = 2πki /|ki |2 , then H̃ is the space of functions that are periodic with respect to the translations v1 and v2 .
  *Proof:* (immediate from Proposition 4.4)
- **Lemma 3.3.** Let d be a continuous pseudo-metric on a Polish space X and let µ1 and µ2 be two positive measures on X with equal mass. Then,  µ1 − µ2  d = |||µ1 − µ2 |||d .
  *Proof:* Uses Monge-Kantorovich duality on the separable metric quotient space defined by the pseudo-metric equivalence relation.
- **Lemma 3.4.** Let {dn } be a bounded and increasing family of continuous pseudo-metrics on a Polish space X and deﬁne d(x, y) = limn→∞ dn (x, y). Then, limn→∞  µ1 − µ2  dn =  µ1 − µ2  d for any two positive measures µ1 and µ2 with equal mass.
  *Proof:* Extracts a weakly converging optimal coupling subsequence and applies the dominated convergence theorem.
- **Corollary 3.5.** Let X be a Polish space and let {dn } be a totally separating system of pseudo-metrics for X . Then,  µ1 − µ2  TV = limn→∞  µ1 − µ2  dn for any two positive measures µ1 and µ2 with equal mass on X .
  *Proof:* Applies Lemma 3.4 to the discrete metric representing the total variation distance.
- **Lemma 3.7.** A point x ∈ supp(µ) if and only if µ(U ) > 0 for every open set U containing x.
  *Proof:* (no proof in this paper)
- **Proposition 3.11.** A semigroup Pt on a Hilbert space H is strong Feller if, for all ϕ : H → R with  ϕ ∞ = supx∈H |ϕ(x)| and  ∇ϕ ∞ ﬁnite one has
(3.5)                     |∇Pt ϕ(x)| ≤ C( x ) ϕ ∞ ,
where C : R+ → R is a ﬁxed nondecreasing function.
  *Proof:* (no proof in this paper)
- **Proposition 3.12.** Let tn and δn be two positive sequences with {tn } nondecreasing and {δn } converging to zero. A semigroup Pt on a Hilbert space H is asymptotically strong Feller if, for all ϕ : H → R with  ϕ ∞ and  ∇ϕ ∞ ﬁnite,
(3.6)              |∇Ptn ϕ(x)| ≤ C( x )  ϕ ∞ + δn  ∇ϕ ∞
for all n, where C : R+ → R is a ﬁxed nondecreasing function.
  *Proof:* Approximates Lipschitz continuous functions by Fréchet differentiable ones to extend the assumed derivative bound limit over a totally separating system.
- **Theorem 3.16.** Let Pt be a Markov semigroup on a Polish space X and let µ and ν be two distinct ergodic invariant probability measures for Pt . If Pt is asymptotically strong Feller at x, then x ∈ supp µ ∩ supp ν.
  *Proof:* Uses the triangle inequality on invariant measures and applies Corollary 3.5 to reach a contradiction from the asymptotic limit bound.
- **Corollary 3.17.** If Pt is an asymptotically strong Feller Markov semigroup and there exists a point x such that x ∈ supp µ for every invariant probability measure µ of Pt , then there exists at most one invariant probability measure for Pt .
  *Proof:* (immediate from Theorem 3.16)
- **Theorem 4.1.** The transition semigroup on H̃ generated by the solutions to (2.1) is asymptotically strong Feller.
  *Proof:* (immediate from Proposition 3.12 and Proposition 4.3)
- **Corollary 4.2.** There exists exactly one invariant probability measure for (2.1) restricted to H̃.
  *Proof:* Combines Corollary 3.17 with an Itô formula bound and limits on the hitting probabilities to demonstrate that 0 is in the support of every invariant measure.
- **Proposition 4.3.** For every η > 0, there exist constants C, δ > 0 such that for every Fréchet diﬀerentiable function ϕ from H̃ to R one has the bound
(4.1)           ∇Pn ϕ(w)  ≤ C exp(η w 2 )  ϕ ∞ +  ∇ϕ ∞ e−δn ,
for every w ∈ H̃ and n ∈ N.
  *Proof:* Constructs an approximate integration by parts formula to express transition semigroup derivatives. Binds the terms using the Cameron-Martin variation cost from Proposition 4.14 and the residual error decay from Proposition 4.13.
- **Proposition 4.4.** If there exist a1 , a2 ∈ Z0 such that |a1 | = |a2 | and such that a1 and a2 are not collinear, then Z∞ =  Z0  . Otherwise, Z∞ = Z0 . In either case, one always has that Z∞ = Z̃∞ .
  *Proof:* Analyzes the geometry of reachable frequency modes by constructing paths of non-forbidden steps. Proves that sequences avoiding collinear and equal-length jumps can encompass the generated subgroup lattice.
- **Corollary 4.5.** One has Z∞ = Z2 \ {(0, 0)} if and only if the following holds:
  1. Integer linear combinations of elements of Z0 generate Z2 .
  2. There exist at least two elements in Z0 with nonequal Euclidean norm.
  *Proof:* (immediate from Proposition 4.4)
- **Lemma 4.7.** For every R0 > 0, there exists R1 > 0 such that every j ∈  Z0   with |j| ≤ R0 can be reached from the origin by a path with steps in Z0 (some steps may be forbidden) which never exits the ball of radius R1 .
  *Proof:* (no proof in this paper)
- **Lemma 4.8.** There exists L > 0 such that the set Z∞ contains all elements of the form n1 a1 + n2 a2 with n1 and n2 in Z \ [−L, L].
  *Proof:* Avoids forbidden steps by constructing a trajectory moving along one basis vector past a sufficiently large threshold before iterating the other.
- **Lemma 4.9.** Assume that there exists an integer R > 1 such that Z∞ contains {j ∈  Z0   | |j|2 ≥ R}. Then Z∞ also contains {j ∈  Z0   | |j|2 ≥ R − 1}.
  *Proof:* Constructs an intermediate step to a larger radius before returning, leveraging non-collinear basis elements to bypass forbidden move constraints.
- **Lemma 4.10.** The solution of the 2D Navier-Stokes equations in the vorticity formulation (2.1) satisﬁes the following bounds:
   1. There exist positive constants C and η0 , depending only on Q and ν, such that
                                  t                          
(4.6) E exp η sup  wt  2 + ν         wr  21 dr − E0 (t − s)
                  t≥s             s
                                                        ≤ C exp ηe−νs  w0  2 ,
        for every s ≥ 0 and for every η ≤ η0 . Here and in the sequel, the notation
         w 1 =  ∇w  is used.
  2. There exist constants η1 , a, γ > 0, depending only on E0 and ν, such that
                           N            
(4.7)              E exp η    wn   − γN ≤ exp aη w0  2 ,
                                  2
                            n=0
        holds for every N > 0, every η ≤ η1 , and every initial condition w0 ∈ H.
   3. For every η > 0, there exists a constant C = C(E0 , ν, η) > 0 such that the Jacobian J0,t satisﬁes almost surely
                                       t                 
(4.8)                 J0,t   ≤ exp η      ws  21 ds + Ct ,
                                         0
        for every t > 0.
  4. For every η > 0 and every p > 0, there exists C = C(E0 , ν, η, p) > 0 such that the Hessian satisﬁes
                              E Ks,t  p ≤ C exp η w0  2 ,
        for every s > 0 and every t ∈ (s, s + 1).
  *Proof:* Derives a priori energy bounds using Itô's formula and exponential martingale estimates. Employs Sobolev interpolation to extend these norm bounds to the system's Jacobian and Hessian flows.
- **Proposition 4.11.** Let Pt denote the semigroup generated by the solutions to (2.1) on H. There exists an N∗ = N∗ (E0 , ν) such that if Z0 contains {k ∈ Z2 , 0 < |k| ≤ N∗ }, then for any η > 0 there exist positive constants c and γ so that
             |∇Pt ϕ(w)| ≤ c exp η w 2          ϕ ∞ + e−γt  ∇ϕ ∞ .
  *Proof:* Utilizes a finite-dimensional Bismut-Elworthy-Li type formula on an adapted Wiener path variation. Controls directly forced low modes while relying on the stable deterministic dynamics to exponentially contract the unforced high modes.
- **Theorem 4.12.** Denote by M the Malliavin matrix over the time interval [0, 12 ] and deﬁne H̃ as above. For every α, η, p and every orthogonal projection π  on a ﬁnite number of Fourier modes, there exists C̃ such that
(4.17)             P  M ϕ, ϕ  < ε ϕ 21 ≤ C̃εp exp η w0  2 ,
holds for every (random) vector ϕ ∈ H̃ satisfying  π  ϕ  ≥ α ϕ 1 almost surely, for every ε ∈ (0, 1), and for every w0 ∈ H̃.
  *Proof:* (no proof in this paper)
- **Proposition 4.13.** For any η > 0, there exist constants β > 0 and C > 0 such that
                                             C exp(η w0  2 )
(4.18)                          E ρN  10 ≤
                                                  2N
holds for every N > 0. (Note that by increasing β further, the 2N in the denominator could be replaced by K N for an arbitrary K ≥ 2 without altering the value of C.)
  *Proof:* Bounds the expected residual error decay rate by recursively applying the regularized inverse Malliavin matrix bounds to low modes. Leverages the spatial Laplacian's dissipative contraction on the unforced high modes.
- **Proposition 4.14.** For any η > 0, there exists a constant C so that
                 N             2  C η w0  2  
                                             ∞
                                                           1
(4.19)       E     v0,s dW (s)  ≤ 2 e            E ρn  10 5 .
                 0                β
                                                 n=0
(Note that the power 10 in this expression is arbitrary and can be brought as close to 2 as one wishes.)
  *Proof:* Estimates the Cameron-Martin cost by controlling the Skorokhod integral of the non-adapted variation path. Applies the Itô isometry for the Malliavin derivative alongside bounds on the Jacobian, Hessian, and Malliavin matrix.
- **Proposition 4.15.** For every η > 0 and every γ > 0, there exist constants Cη,γ such that for every Fréchet diﬀerentiable function ϕ from H̃ to R,
    ∇Pn ϕ(w)  ≤ exp(η w 2 ) Cη,γ        Pn |ϕ|2 (w) + γ n   Pn  ∇ϕ 2 (w) ,
for every w ∈ H̃ and n ∈ N.
  *Proof:* Applies the Cauchy-Schwarz inequality to the bounded expectations of the variation path integral and the residual error terms.
- **Lemma 4.16.** For every two constants γ, η > 0 and every p ≥ 1, there exists a constant β0 > 0 such that
                       E  ρn+1  p | Fn ≤ γeη wn    ρn  p
                                                    2
holds almost surely whenever β ≤ β0 .
  *Proof:* Combines bounds on the Jacobian for unforced high modes and the regularized Malliavin inverse for low modes to sequentially contract the residual.
- **Lemma 4.17.** For every p ≥ 1, every T > 0, and every two constants γ, η > 0, there exists an orthogonal projector π  onto a ﬁnite number of Fourier modes such that
(4.23)                E (1 − π  )J0,T  p ≤ γ exp η w0  2 ,
(4.24)                E J0,T (1 − π  ) p ≤ γ exp η w0  2 .
  *Proof:* Differentiates the energy bounds of the linearized flow modes via Sobolev interpolation and integration by parts. Shows that the dissipative damping ensures high-frequency perturbations remain exponentially suppressed.
- **Lemma 4.18.** Fix ξ ∈ H̃ and deﬁne
                             ζ = β(β + M0 )−1 Jˆ0 ξ .
Then, for every two constants γ, η > 0 and every low-mode orthogonal projector π  , there exists a constant β > 0 such that
                            E π  ζ p ≤ γeη w0    ξ p .
  *Proof:* Bounds the application of the regularized inverse matrix by splitting the analysis into subsets based on high and low concentration. Utilizes Malliavin matrix eigenvalue estimates from Theorem 4.12 on the high-probability sets.
- **Lemma A.1.** There exist constants η0 > 0 and C > 0, such that for every t > 0 and every η ∈ (0, η0 ], the bound
(A.5)                  E exp(η wt  2 ) ≤ C exp(ηe−νt  w0  2 )
holds.
  *Proof:* Applies Itô's formula to the squared norm and leverages exponential martingale inequality estimates.