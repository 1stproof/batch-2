<!-- Generated 2026-05-31T02:13:30 -->
<!-- Source PDF: haglund__the_q_t_catalan_numbers_and_the_space_of_diagonal.pdf (1191147 bytes) -->
<!-- Citation: J. Haglund (2008). The q,t-Catalan Numbers and the Space of Diagonal Harmonics. AMS University Lecture Series. -->

# The q,t-Catalan Numbers and the Space of Diagonal Harmonics (Haglund, 2008)

## Definitions
- **Definition 1.13.** Two simple functions on partitions we will often use are
                             X               X  λ′  
                                                    i
                      n(λ) =     (i − 1)λi =
                               i              i
                                                   2
                             Y
                                  ni
                        zλ =     i ni !,
                                               i
where ni = ni (λ) is the number of parts of λ equal to i.
- **Definition 3.1.** Given π ∈ L+
       n,n , define the bounce path of π to be the path
described by the following algorithm.
Start at (0, 0) and travel North along π until you encounter the beginning of an E
step. Then turn East and travel straight until you hit the diagonal y = x. Then
turn North and travel straight until you again encounter the beginning of an E step
of π, then turn East and travel to the diagonal, etc. Continue in this way until you
arrive at (n, n).
- **Definition 3.3.** Let L+                                       +
                           n,n (k) denote the set of all π ∈ Ln,n which begin with
                                                                 +
exactly k N steps followed by an E step. By convention L0,0 (k) consists of the
empty path if k = 0 and is empty otherwise. Set
                           X
(3.5)      Fn,k (q, t) =          q area(π) tbounce(π) , Fn,0 = χ(n = 0).
                         π∈L+
                            n,n (k)
- **Definition 3.14.** Let π ∈ L+
                              n,n . Let

                  dinv(π) = |{(i, j) : 1 ≤ i < j ≤ n            ai = aj }|
                                + |{(i, j) : 1 ≤ i < j ≤ n         ai = aj + 1}|.
- **Definition 4.18.** Let dinv(π) be the number of pairs (i, j), 1 ≤ i < j ≤ n,
such that either
      (1) ai (π) = aj (π) and rowi is an N row
           or
      (2) ai (π) = aj (π) + 1 and rowj is an N row.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.1.** Both inv and maj are Mahonian, i.e.
                      X                     X
(1.1)                     q inv(σ) = [n]! =   q maj(σ) .
                            σ∈Sn                      σ∈Sn
  *Proof:* Uses an insertion-based induction over permutation lengths to trace the shifts in inversions and major index.
- **Proposition 1.1.1.** We have maj(σ) = inv(φ(σ)). Furthermore, Ides(σ) =
Ides(φ(σ)), and φ fixes σn .
  *Proof:* Inductively tracks newly generated blocks and inversion swaps in Foata's map φ.
- **Theorem 1.2.** For n, k ∈ N,
                                   
                              n+k     X
(1.6)                               =    q |λ| ,
                               k       k      λ⊆n

where the sum is over all partitions λ whose Ferrers graph fits inside a k × n
rectangle, i.e. for which λ1 ≤ n and ℓ(λ) ≤ k.
  *Proof:* Sets up a generating function recurrence over restricted partition sizes to yield the Gaussian identity.
- **Theorem 1.3.** Both inv and maj are multiset Mahonian, i.e. given α ∈ Ns+1 ,
                                                   
                 X                      n             X
(1.10)               q inv(σ) =                     =   q maj(σ) ,
                                  α0 , . . . , αs
                        σ∈Mα                                         σ∈Mα

where the sums are over all elements σ ∈ Mα .
  *Proof:* (no proof in this paper)
- **Theorem 1.6.** (MacMahon [Mac60, p. 214])
                                                                
                             X
                                        maj(σ(π))        1    2n
(1.15)                              q               =            .
                                                      [n + 1] n
                           π∈L+
                              n,n
  *Proof:* Bijectively shifts maximal off-diagonal lattice points to subtract 1 from the major index.
- **Proposition 1.6.1.**
                                   n
                                   X
(1.20)                  Cn (q) =         q k−1 Ck (q)Cn−k (q),       n ≥ 1.
                                   k=1
  *Proof:* Recursively decomposes the path at its first return to the main diagonal.
- **Theorem 1.8.**
                             X ∞
                   a              (a)n n (az)∞
(1.23)      1 φ0     ; q; z =           z =      ,                   |z| < 1, |q| < 1,
                  −               (q)n      (z)∞
                              n=0
                         Q∞
where (a; q)∞ = (a)∞ = i=0 (1 − aq i ).
  *Proof:* Derives an iterative recurrence for a hypergeometric generating function to find the infinite limit.
- **Corollary 1.8.1.** The “q-binomial theorem”.
                          n            
                         X
                              (k
                                  )  n k
(1.27)                      q   2       z = (−z; q)n
                                     k
                                      k=0

and
                                      ∞        
                                      X   n+k                     1
(1.28)                                               zk =              .
                                               k             (z; q)n+1
                                      k=0
  *Proof:* Substitutes specific exponent terms into Cauchy’s q-binomial series.
- **Corollary 1.8.2.**
                        h                                          
                        X
                                  (n−k)(h−k)        n   m     m+n
(1.29)                        q                            =        .
                                                    k h−k      h
                        k=0
  *Proof:* Extracts targeted coefficients from the product of two expanded q-binomial summations.
- **Corollary 1.8.3.**
               h                                                         
               X                      n−1+k             m+h−k     m+n+h
(1.30)               q (m+1)k                                  =          .
                                        k                h−k        h
               k=0
  *Proof:* Uses the infinite q-binomial series expansion and targeted coefficient extraction.
- **Theorem 1.9.** Let n ∈ N. Then
                            a, q −n
                                           
                                             (c/a)n n
(1.31)                2 φ1          ; q; q =       a .
                                 c            (c)n
  *Proof:* (no proof in this paper)
- **Theorem 1.15.**
                                                                     
                                                             m      n
(1.38)                        em (1, q, . . . , q n−1 ) = q ( 2 )
                                                                   m
                                                                         
                                                            n−1+m
(1.39)                        hm (1, q, . . . , q n−1 ) =
                                                                   m
                                                                   nm
                                                          1  −   q
(1.40)                        pm (1, q, . . . , q n−1 ) =             .
                                                           1 − qm
  *Proof:* Instantiates summation variables with geometric q-series to simplify expressions.
- **Theorem 1.19.** The hλ and the mβ are dual with respect to the Hall scalar
product, i.e.
(1.45)                           hhλ , mβ i = χ(λ = β).
  *Proof:* (no proof in this paper)
- **Corollary 1.19.1.**
(1.46)                                 hf, hλ i = f |mλ .
  *Proof:* (immediate from Theorem 1.19)
- **Theorem 1.20.** Let λ, µ ∈ Par. Then
      (1) The Schur functions are orthonormal with respect to the Hall scalar prod-
          uct, i.e.
                                 < sλ , sµ >= χ(λ = µ).
          Thus for any f ∈ Λ,
                                       < f, sλ >= f |sλ .
      (2) Action by ω:
                                         ω(sλ ) = sλ′ .
      (3) (The Jacobi-Trudi identity)
                                                          ℓ(λ)
                                 sλ = det(hλi −i+j )i,j=1 ,
         where we set h0 = 1 and hk = 0 for k < 0. For example,
                                    h2 h3 h4
                          s2,2,1 = h1 h2 h3
                                    0     1 h1
                                 = h2,2,1 − h3,2 − h3,1,1 + h4,1 .
     (4) (The Pieri rule). Let k ∈ N. Then
                                           X
                                  sλ h k =   sγ ,
                                                       γ

         where the sum is over all γ whose Ferrers graph contains λ with |γ/λ| = k
         and such that γ/λ is a “horizontal strip”, i.e. has no two cells in any
         column. Also,
                                           X
                                  sλ e k =   sγ ,
                                                       γ

         where the sum is over all partitions γ whose Ferrers graph contains λ with
         |γ/λ| = k and such that γ/λ is a “vertical strip”, i.e. has no two cells in
         any row. For example,
                        s2,1 h2 = s4,1 + s3,2 + s3,1,1 + s2,2,1
                        s3,1 e2 = s4,2 + s4,1,1 + s3,2,1 + s3,1,1,1 .
     (5) (Principal Specialization).
                                                                Y [n + c(i, j)]
                  sλ (1, q, q 2 , . . . , q n−1 ) = q n(λ)                      ,
                                                                    [h(i, j)]
                                                              (i,j)∈λ

         and taking the limit as n → ∞ we get
                                                     Y                     1
                     sλ (1, q, q 2 , . . .) = q n(λ)                                .
                                                                       1 − q h(i,j)
                                                           (i,j)∈λ

     (6) For any two alphabets Z, W ,
                                               X
(1.51)                    sλ (Z + W ) =              sβ (Z)sλ′ /β ′ (W ).
                                               β⊆λ

     (7) (The Littlewood-Richardson rule) For all partitions λ, β,


                                                           sγ cγλβ ,
                                                 X
                                       sλ sβ =
                                                   γ

         where cγλ,β is the number of SSYT T of skew shape γ/β and weight λ such
         that if we form the word σ1 σ2 · · · by reading the entries of T across rows
         from right to left, and from bottom to top, then in any initial segment
         σ1 · · · σj there are at least as many i’s as i + 1’s, for each 1 ≤ i. (Such
         words are known as lattice permutations, and the corresponding SSYT are
         called Yamanouchi). Note that this rule contains the Pieri rules above as
         special cases. For a proof of the Littlewood-Richardson rule see [Mac88,
         Chap. 1].
  *Proof:* (no proof in this paper)
- **Theorem 1.23.** [Rob38], [Sch61], [Knu70] There is a bijection between or-
dered two-line arrays A and pairs of SSYT (P, Q) of the same shape. Under this
correspondence, the weight of A1 equals the weight of Q, the weight of A2 is the
weight of P , and Des(Q) = Des(A2 ). If A1 is the identity permutation 12 · · · n,
then we get a bijection between words w and pairs (Pw , Qw ) of tableau of the same
shape, with Pw a SSYT of the same weight as w, and Q a SYT. If the top row
is the identity permutation and the bottom row is a permutation β, then we get a
bijection between permutations β and pairs (Pβ , Qβ ) of SYT of the same shape.
  *Proof:* (no proof in this paper)
- **Theorem 1.27.** The “addition formulas”. Let E = E(t1 , t2 , . . .) and F =
F (w1 , w2 , . . .) be two formal series of rational terms in their indeterminates. Then


                                          n
                                          X
(1.63)                    en [E − F ] =           ek [E]en−k [−F ]
                                          k=0
                                          Xn
(1.64)                    en [E + F ] =           ek [E]en−k [F ]
                                          k=0
                                          Xn
(1.65)                    hn [E − F ] =           hk [E]hn−k [−F ]
                                          k=0
                                          Xn
(1.66)                    hn [E + F ] =           hk [E]hn−k [F ].
                                          k=0



We also have the Cauchy identities

                                           X
(1.67)                      en [EF ] =                  sλ [E]sλ′ [F ]
                                         λ∈Par(n)
                                           X
(1.68)                     hn [EF ] =                   sλ [E]sλ [F ].
                                         λ∈Par(n)
  *Proof:* Evaluates addition and Cauchy formulas via partitioned multinomial expansions.
- **Theorem 1.29.** When expanding the sλ into the pλ basis, the coefficients are
the χλ . To be exact
                              X
                         pµ =     χλ (µ)sλ
                                            λ⊢n
                                            X
                                    sλ =           zµ−1 χλ (µ)pµ .
                                            µ⊢n
  *Proof:* (no proof in this paper)
- **Proposition 1.29.1.** The Hilbert series of V ǫ equals the coefficient of s1n in
the Frobenius series of V , i.e.
(1.82)                           H(V ǫ ; q) = hF(V ; q), s1n i .
  *Proof:* Sums traces corresponding to block diagonal submodules over alternating classes.
- **Theorem 2.1.** For n a positive integer and k, a, b ∈ C with ℜa > 0, ℜb > 0,
and ℜk > −min{1/n, (ℜa)/(n − 1), (ℜb)/(n − 1)},
          Z        Y                  n
                                      Y
(2.1)           |       (xi − xj )|2k   xia−1 (1 − xi )b−1 dx1 · · · dxn
              (0,1)n   1≤i<j≤n             i=1
                             n
                             Y   Γ(a + (i − 1)k)Γ(b + (i − 1)k)Γ(ik + 1)
                         =                                               ,
                             i=1
                                     Γ(a + b + (n + i − 2)k)Γ(k + 1)
where Γ(z) is the gamma function.
  *Proof:* (no proof in this paper)
- **Theorem 2.2.** Define a q, t extension of the Hall scalar product by
                                                                  ℓ(λ)
                                                                  Y 1 − q λi
(2.3)                      hpλ , pµ iq,t = χ(λ = µ)zλ                                 .
                                                                  i=1
                                                                         1 − tλi

Then the following conditions uniquely define a family of symmetric functions
{Pλ (X; q, t)}, λ ∈ Par(n) with coefficients in Q(q, t).
         •
                                                     X
(2.4)                                      Pλ =             cλ,µ mµ ,
                                                     µ≤λ

              where cλ,µ ∈ Q(q, t) and cλ,λ = 1.
         •
(2.5)                              hPλ , Pµ iq,t = 0           if λ 6= µ.
  *Proof:* (no proof in this paper)
- **Theorem 2.4.**
                                                                                k−1
                                  1
                                       Z                            Y           Y
                                                  Pλ (X; q, t)                     (xi − q r xj )(xi − q −r xj )
                                  n!     (0,1)n                  1≤i<j≤n r=0
                                                                      Yn
                                                                    ×     xia−1 (xi ; q)b−1 dq x1 · · · dq xn
                                                                      i=1
        n
        Y Γq (λi + a + (i − 1)k)Γq (b + (i − 1)k)                     Y         Γq (λi − λj + (j − i + 1)k)
= qF
        i=1
                  Γq (λi + a + b + (n + i − 2)k)                                  Γq (λi − λj + (j − i)k)
                                                                 1≤i<j≤n

where k ∈ N, F = kn(λ) + kan(n − 1)/2 + k 2 n(n − 1)(n − 2)/3, t = q k ,

(2.6)                       Γq (z) = (1 − q)1−z (q; q)∞ /(q z ; q)∞
is the q-gamma function and
                       Z 1             ∞
                                       X
(2.7)                      f (x)dq x =   f (q i )(q i − q i+1 )
                              0                       i=0

is the q-integral.
  *Proof:* (no proof in this paper)
- **Theorem 2.6.** let λ, µ ∈ Par.
     (1) Let z be a real parameter. Then
                                          Y l′       ′
                                            t − qa z
                             
                              1−z
(2.10)                   Pλ       ; q, t =              .
                              1−t          1 − q a tl+1
                                                             x∈λ

     (2) (Koornwinder-Macdonald Reciprocity). Assume n ≥ max(ℓ(λ), ℓ(µ)). Then
                   Q            a l+1
                                            Pn n−i λ           
                      x∈µ (1 − q t    )Pλ    i=1 t q i ; q, t
(2.11)                          Q       l′   a′ n
                                  x∈µ (t − q t )

         is symmetric in µ, λ, where as usual we let µi = 0 for i > ℓ(µ), λi = 0 for
         i > ℓ(λ).
     (3) For any two sets of variables X, Y ,
                                          (1 − q a tl+1 )
                             XQ
                     1−t
(2.12)        hn XY          =      Qx∈λ                  P (X; q, t)Pλ (Y ; q, t)
                                                 a+1 tl ) λ
                     1−q              x∈λ (1 − q
                                λ⊢n
                                X
(2.13)              en [XY ] =      Pλ (X; q, t)Pλ′ (Y ; t, q).
                                         λ⊢n


     (4) Define a q, t version of the involution ω as follows.
                                                        1 − qk
(2.14)                    ωq,t pk [X] = (−1)k−1                pk [X].
                                                        1 − tk
          Note this implies
                                               
                                          1−t
(2.15)                    ωq,t pk       X       = (−1)k−1 pk [X].
                                          1−q
          Then
                                             Y 1 − q l+1 ta
(2.16)               ωq,t Pλ [X; q, t] =                          Pλ′ [X; t, q].
                                                   1 − q l ta+1
                                            x∈λ′
  *Proof:* (no proof in this paper)
- **Theorem 2.8.** For all µ ⊢ n,
(2.39)                              F(V (µ); q, t) = H̃µ ,
where H̃µ = H̃µ [X; q, t] is the “modified Macdonald polynomial” defined as
                                       X
(2.40)                           H̃µ =    K̃λ,µ (q, t)sλ .
                                          λ⊢n
  *Proof:* (no proof in this paper)
- **Corollary 2.8.1.** For all µ ⊢ n, dim V (µ) = n!.
  *Proof:* Replaces s_lambda with f_lambda inside the evaluated Frobenius series at q=t=1.
- **Theorem 2.14.** (Haiman, [Hai02]).
                                           X Tµ M H̃µ Πµ Bµ
(2.52)                   F(DHn ; q, t) =                       .
                                                    wµ
                                           µ⊢n
  *Proof:* (no proof in this paper)
- **Theorem 2.16.** Let µ, λ ∈ P ar, z ∈ R. Then
               H̃µ [1 + z(M Bλ − 1); q, t]   H̃λ [1 + z(M Bµ − 1); q, t]
(2.55)              Q            a′ l′     =      Q            a′ l′
                                                                         .
                      x∈µ (1 − zq t )               x∈λ (1 − zq t )
  *Proof:* Cross-multiplies polynomial evaluations under Koornwinder-Macdonald substitutions.
- **Proposition 2.17.1.**
                                  X Tµ M H̃µ Πµ Bµ
(2.64)                    ∇en =                         ,         n > 0.
                                              wµ
                                  µ⊢n

Hence Theorem 2.14 is equivalent to
(2.65)                              F(DHn ; q, t) = ∇en .
  *Proof:* Substitutes parameters into hn[-XY] with reciprocal symmetries to match the nabla evaluation.
- **Theorem 3.2.**
(3.3)                                  Cn (q, t) = Fn (q, t).
  *Proof:* (no proof in this paper)
- **Corollary 3.2.1.**
                                                X
(3.4)                     H(DHnǫ ; q, t) =             q area(π) tbounce(π) .
                                              π∈L+
                                                 n,n
  *Proof:* (no proof in this paper)
- **Theorem 3.4.** For 1 ≤ k ≤ n,
                            n−k
                            X  r + k − 1           k
(3.6)         Fn,k (q, t) =                tn−k q (2) Fn−k,r (q, t).
                            r=0
                                   r
  *Proof:* Splits paths at the second bounce to generate scaled generating functions over the remaining segments.
- **Corollary 3.4.1.**
(3.10)
               n                                                                       b−1
                                                                                       Y                    
               X   X
                                          α2 +2α3 +...+(b−1)αb
                                                                       Pb
                                                                              (α2i )         αi + αi+1 − 1
   Fn (q, t) =                        t                            q    i=1                                  ,
                                                                                       i=1
                                                                                                 αi+1
              b=1 α1 +α2 +...+αb =n
                          αi >0

where the inner sum is over all compositions α of n into b positive integers.
  *Proof:* (immediate from Theorem 3.4)
- **Theorem 3.5.** For any integers k, m ≥ 1,
(3.11)
                          m  
         1 − qk                                           1 − qr
                        X                                                 
                              r + k − 1 m−r (r2)
   ∇em X          , em =                t  q      ∇em−r X          , em−r .
         1−q             r=1
                                  r                       1−q
  *Proof:* (no proof in this paper)
- **Corollary 3.5.1.** For all 0 ≤ k ≤ n,
                                              1 − qk
                                                              
                                   k
(3.12)       Fn,k (q, t) = tn−k q (2) ∇en−k X          , en−k .
                                               1−q
  *Proof:* Verifies the target plethystic formulation satisfies identical boundary and recurrence conditions.
- **Proposition 3.5.1.**
(3.16)           H̃µ [(1 − t)(1 − q k ); q, t] = Πµ hk [(1 − t)Bµ ](1 − q k ).
  *Proof:* Evaluates reciprocity identities on specialized one-part hooks.
- **Corollary 3.5.2.** For n ≥ 1, k ≥ 0,
                    1 − qk        (1 − q k )H̃µ hk [(1 − t)Bµ ]Πµ
                             X
(3.18)       en X           =                                     .
                     1−q                         wµ
                                          µ⊢n
  *Proof:* Combines the generalized en[XY] plethystic expansion with evaluations from Proposition 3.5.1.
- **Theorem 3.6.** For 1 ≤ k ≤ n,
                                      k     X (1 − q k )Tµ2 hk [(1 − t)Bµ ]Πµ
(3.20)         Fn,k (q, t) = tn−k q (2)                                       .
                                                             wµ
                                           µ⊢n−k
  *Proof:* Expands nabla en-k into the plethystic hook identity utilizing Corollary 3.5.2.
- **Proposition 3.6.1.**
                                                    1 − qk
                                                                     
                                         k
(3.25)           h∇En,k , en i = tn−k q (2) ∇en−k X          , en−k
(3.26)                         = Fn,k (q, t).
  *Proof:* Associates q-Taylor coefficients to plethystic functions matching the recursive property.
- **Proposition 3.9.1.** For any λ ∈ Par(n),
                                       
                                  n−1      X
(3.35)      h∇En,n−1 , sλ i = t                                         q maj(T )−n+1 .
                                   1    T ∈SY T (λ)
                                                n is above n − 1 in T
  *Proof:* (no proof in this paper)
- **Theorem 3.10.** For 1 ≤ k ≤ n,
                                                              
                       n                       [k] 2n − k − 1 (k−1)n
(3.42)               q ( 2 ) Fn,k (q, 1/q) =                  q      .
                                               [n]   n−k
  *Proof:* Applies induction using the diagonal return recurrences on q-binomials.
- **Corollary 3.10.1.**
                                                                  
                                  n                        1    2n
(3.49)                          q ( 2 ) Fn (q, 1/q) =              .
                                                        [n + 1] n
  *Proof:* (immediate from Theorem 3.10)
- **Theorem 3.12.**
                                X                    X
(3.53)                                q area(π) =            q bounce(π) .
                            π∈L+
                               n,n                  π∈L+
                                                       n,n
  *Proof:* Maps multisets of row lengths onto non-ascending compositions to match marginal generating counts.
- **Theorem 3.15.**
                X                      X
(3.56)            q dinv(π) tarea(π) =   q area(π) tbounce(π) .
                   π∈L+
                      n,n                     π∈L+
                                                 n,n
  *Proof:* Constructs a bijection traversing area sequences between peaks to cleanly swap offset inversions.
- **Corollary 3.16.1.**
                                              X
(3.59)                    Cn (q, t) =                  q dinv(π) tarea(π) .
                                            π∈L+
                                               n,n
  *Proof:* (immediate from Theorem 3.2)
- **Theorem 3.20.** If
                                               X
(3.64)                    (F ◦q G)(z) =              fn G(z)G(qz) · · · G(q n−1 z),
                                                n
                          n
            P
where F =        n fn z       , then
(3.65)                                 F ◦q G = z and G ◦q−1 F = z
are equivalent to each other and also to
(3.66)            (Φ ◦q−1 F ) ◦q G = Φ = (Φ ◦q G) ◦q−1 F                             for all Φ.
  *Proof:* (no proof in this paper)
- **Theorem 3.21.** Define h∗n (q), n ≥ 0 via the equation
             ∞                   ∞
                                           n
                                       q −( 2 ) h∗n (q)z n H(−q −1 z)H(−q −2 z) · · · H(−q −n z).
             X                   X
(3.67)             ek z k =
             k=0                 n=0

Then for n ≥ 0, h∗n (q) has the explicit expression
                                       X
(3.68)                      h∗n (q) =       q area(π) eβ(π) .
                                                    π∈L+
                                                       n,n
  *Proof:* (no proof in this paper)
- **Theorem 3.22.** Let ck , k ≥ 0 be a set of variables. Define h∗n (c, q), n ≥ 0 via
the equation
           ∞                     ∞
                                           n
                                       q −( 2 ) h∗n (c, q)z n H(−q −1 z)H(−q −2 z) · · · H(−q −n z).
           X                     X
(3.70)           e k ck z k =
           k=0                   n=0

Then for n ≥ 0, h∗n (c, q) has the explicit expression
                                               n
                                               X             X
(3.71)                         h∗n (c, q) =          ck                q area(π) eβ(π) .
                                               k=0        π∈L+
                                                             n,n (k)
  *Proof:* Employs Garsia's q-Lagrange equivalence on power series parameterized by Dyck path factorization.
- **Corollary 3.22.1.** For 1 ≤ k ≤ n,
                        X n
(3.79)             zk =     q ( 2 )−n+k Fn,k (q −1 , 1)z n (z)n .
                                         n≥k
  *Proof:* (immediate from Theorem 3.22)
- **Theorem 3.23.** Let ck , k ≥ 0 be a set of variables. Then
(3.93)
 ∞
 X
    e k ck z k =
k=0
   ∞                                                                  n
                                                                                                         1 − qk
                                                                                                                 
             −(n
               2) n
                                                                                   k
                                                                            e c q (2) q ∇e
  X                                                                   X
                         −1            −2                   −n
         q      z H(−q        z)H(−q        z) · · · H(−q        z)          k k             n−k       X          .
   n=0
                                                                                                         1−q
                                                                      k=0
  *Proof:* (immediate from Theorem 3.22)
- **Theorem 3.24.**
                                                                 1 − q n+1
                                                                            
                        n                              1
(3.94)                q ( 2 ) F(DHn ; q, 1/q) =             en X             ,
                                                    [n + 1]        1−q
or, equivalently by the Cauchy identity (1.67),
                                                              1 − q n+1
                                                                         
                D n                          E     1
(3.95)            q ( 2 ) F(DHn ; q, 1/q), sλ =         sλ′               .
                                                [n + 1]         1−q
  *Proof:* Employs symmetric polynomial evaluations at t=1/q that collapse the series onto Schur bases.
- **Theorem 4.2.** For all 0 ≤ d ≤ n,
(4.3)                         Sn,d (q, t) = h∇en , en−d hd i .
  *Proof:* (no proof in this paper)
- **Theorem 4.3.** Theorem 4.2 is equivalent to the statement that for all 0 ≤ d ≤
n − 1,
(4.6)                      S̃n,d (q, t) = ∇en , sd+1,1n−d−1 .
  *Proof:* Exerts an area-preserving bijection toggling the highest North-East pair to a diagonal step.
- **Lemma 4.5.** (The “boundary lemma”). Given a, b, c ∈ N, let boundary(a, b, c)
be the path whose σ word is 2c 1b 0a . Then
                                                         
                            X          ′       a+b+c
(4.15)                          q area (π) =             ,
                             π
                                                a, b, c

where the sum is over all paths π from (0, 0) to (c + b, a + b) consisting of a N steps,
b D steps and c E steps, and area′ (π) is the number of lower triangles between π
and boundary(a, b, c).
  *Proof:* Translates lower triangles into bounded coinversions and factors the results via multinomial identities.
- **Theorem 4.6.** Let n, k, d ∈ N with 1 ≤ k ≤ n. Then
(4.19)                                Sn,n,k (q, t) = δn,k ,
and for 0 ≤ d < n,
                                  min(k,n−d)            n−k          
                           n−k
                                     X           k (p2) X p + j − 1
(4.20) Sn,d,k (q, t) = t                            q                 Sn−k,d+p−k,j (q, t),
                                                 p      j=0
                                                              j
                                 p=max(1,k−d)

with the initial conditions
(4.21)                       S0,0,k = δk,0 ,     Sn,d,0 = δn,0 δd,0 .
  *Proof:* Truncates paths above the first peak to trace lost steps into generating subset components.
- **Theorem 4.7.** For all 0 ≤ d < n,
                          n−d                                                          
                          X              X                     β0 + α1     βb + αb − 1 (α21 )+...+(α2b )
(4.26)    Sn,d (q, t) =                                                                q
                                                                  β0           βb
                          b=1 α1 +...+αb =n−d, αi >0
                                β0 +β1 +...+βb =d, βi ≥0

                                                                            b−1
                                                                            Y                           
                                                                                  βi + αi+1 + αi − 1
                          tβ1 +2β2 +...+bβb +α2 +2α3 +...+(b−1)αb                                        .
                                                                            i=1
                                                                                    βi , αi+1 , αi − 1
  *Proof:* Generates exact polynomials via boundary lemma configurations inserted among separated bounce sections.
- **Theorem 4.8.** For 1 ≤ k ≤ n and 0 ≤ d ≤ n,
                                                                                  
                 (n
                     )−(d2)                     (k−1)(n−d) [k] 2n − k − d − 1   n
(4.27)         q   2        Sn,d,k (q, 1/q) = q                                    .
                                                           [n]     n−k          d
  *Proof:* Sums inductive recurrence components explicitly using q-binomial factorizations to clear alternating parameters.
- **Corollary 4.8.1.** For 0 ≤ d ≤ n,
                                                                           
                   n    d                           1         2n − d
(4.39)           q ( 2 )−(2) Sn,d (q, 1/q) =                                .
                                               [n − d + 1] n − d, n − d, d
  *Proof:* (immediate from Theorem 4.8)
- **Theorem 4.10.** For all 1 ≤ k ≤ n and 0 ≤ d ≤ n,
(4.47)                          h∇En,k , en−d hd i = Sn,d,k (q, t).
  *Proof:* Demonstrates that the required scalar product perfectly satisfies the q-Schroder algebraic recurrence limits.
- **Theorem 4.11.** For all λ, β ∈ Par,
(4.49)                               h∆sλ ∇en , sβ i ∈ N[q, t].
  *Proof:* (no proof in this paper)
- **Theorem 4.14.** For 1 ≤ k ≤ n,
(4.52)                          h∇En,k , sn i = χ(n = k),
and in addition, if |λ| = m > 0,
                                                         1 − qk
                                                                         
                                       n−k
(4.53)         h∆sλ ∇En,k , sn i = t          ∆hn−k em X          , sλ ,
                                                                      ′
                                                         1−q
or equivalently, by (3.18),
                                     X (1 − q k )hk [(1 − t)Bµ ]hn−k [Bµ ]Πµ K̃λ′ ,µ
(4.54)    h∆sλ ∇En,k , sn i = tn−k                                                     .
                                                               wµ
                                     µ⊢m
  *Proof:* (no proof in this paper)
- **Corollary 4.14.1.** For 1 ≤ k ≤ n and 0 ≤ d ≤ n,
                                                 1 − qk
                                                                 
                              n−k
(4.55)      Sn,d,k (q, t) = t       ∆hn−k en−d X          , sn−d .
  *Proof:* (no proof in this paper)
- **Corollary 4.14.2.** For 0 ≤ d ≤ n,
(4.56)                   Sn,d (q, t) = h∆hn en+1−d , sn+1−d i .
  *Proof:* (no proof in this paper)
- **Theorem 4.16.** Given positive integers n, m, λ ⊢ m, z ∈ R, and a symmetric
function P ∈ Λn ,
          m    
                                 1 − qp                     1 − qz
                                                                          
         X    z (p2)
(4.57)           q    ∆em−p en X         , P = ∆ωP em X              , sm .
         p=1
              p                  1−q                         1−q
  *Proof:* (no proof in this paper)
- **Corollary 4.16.1.** Given positive integers n, m, and P ∈ Λn ,
(4.58)                        ∆em−1 en , P = h∆ωP em , sm i .
  *Proof:* (immediate from Theorem 4.16)
- **Theorem 4.19.** Given π ∈ L+
                                 n,n,d , the following “sweep” algorithm is a bijective
map which creates a path φ(π) ∈ L+
                                 n,n,d with the following properties.

(4.61)             dinv(π) = area(φ(π)) and area(π) = bounce(φ(π)).
Moreover, the N -area vector of π equals the bounce vector of φ(π), and the D-area
vector of π equals the shift vector of φ(π).
Algorithm φ [(dinv, area) → (area, bounce)]:
Input: the path π of height h.
We create the path φ(π) by starting at the lattice point (n, n) at the
end of φ and appending steps one by one, ending at (0, 0).
Initialize φ to ∅.
For v = h to −1;
     For w = n to 1;
          If aw (π) = v and roww is an N row then append an E step to φ;
          If aw (π) = v + 1 and roww is a D row then append a D step to φ;
          If aw (π) = v + 1 and roww is an N row then append an N step to φ;
    repeat;
repeat;
  *Proof:* Iterates a backwards height-wise scan to convert row lengths into interleaved bounce constraints and boundary steps. Reconstructs the original sequence via a deterministic inverse scan, showing the map is bijective.
- **Corollary 4.19.1.** For 0 ≤ d ≤ n,
                                   X
(4.62)            Sn,d,k (q, t) =                           q dinv(π) tarea(π) ,
                                               +
                                          π∈L
                                               n,n,d
                                       k rows of length 0



where the sum is over all π ∈ L+
                               n,n,d having exactly k rows of length 0.
  *Proof:* (immediate from Theorem 4.19)
- **Corollary 4.19.2.** For 0 ≤ d ≤ n,

(4.63)                          Sn,d (q, 1) = Sn,d (1, q).
  *Proof:* (immediate from Theorem 4.19)
- **Theorem 4.21.** For n ∈ N,
                                                   Y
(4.64)                  lim Sn+d,d (q, t) =                 (1 + q i tj z)|zn .
                       d→∞
                                                  i,j≥0
  *Proof:* Drives the shifted limit through Haiman's geometric expansion to yield a localized generating product.