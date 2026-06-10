<!-- Generated 2026-05-31T02:10:07 -->
<!-- Source PDF: haglund__the_delta_conjecture.pdf (348754 bytes) -->
<!-- Citation: J. Haglund, J. Remmel, A. T. Wilson (2018). The Delta Conjecture. Transactions of the AMS. -->

# The Delta Conjecture

## Definitions

*(none)*

## Lemmas, Theorems, Propositions, Corollaries

- **Conjecture 1.1 (Delta Conjecture).** For any integers n > k ≥ 0,
                                                                                                      
                                                                                                      
                                                                                                      
                                                                                                    P 
(7)   Δ ek en =             q dinv(P ) tarea(P )                              1 + z/tai (P )       x  
                  P ∈LD n                          i: ai (P )>ai−1 (P )                                n−k−1
                                                                                  z

                                                       
                                                                            
(8)          =         q dinv(P ) tarea(P )            1 + z/q di (P )+1 xP          .
               P ∈LD n                      i∈Val(P )                          n−k−1
                                                                                               z
Equivalently, we can replace the left-hand side with Δek en for integers n ≥ k ≥ 0,
multiply both right-hand sides by (1 + z), and then take the coeﬃcient of z n−k .
  *Proof:* (no proof in this paper)

- **Proposition 3.1.** For integers n > k ≥ 0,

                                                                        −
(19)          Risen,k (x; q, t) =                       q dinv(P ) tarea ((P,R)) xP
                                    (P,R)∈LD Rise
                                             n,n−k−1
                                                                        −
(20)                           =                        q dinv(P ) tarea ((P,F )) xP .
                                    (P,F )∈LD Fall
                                              n,n−k−1
                                                              −
(21)           Valn,k (x; q, t) =                       q dinv ((P,V )) tarea(P ) xP .
  *Proof:* Follows directly from the preceding combinatorial definitions of the modified area and dinv statistics.

- **Proposition 3.2.** We can construct bijections

(24)                         φn,k : LDFall
                                      n,n−k−1 → LD n,k ,
                                                   Stack


(25)                         ψn,k : LDVal
                                      n,n−k−1 → LD n,k
                                                   Stack

such that
(26)                        area(φn,k ((P, F ))) = area− ((P, F )),
(27)                      hdinv(φn,k ((P, F ))) = dinv(P ),
(28)                        area(ψn,k ((P, F ))) = area(P ),
(29)                     wdinv(ψn,k ((P, V ))) = dinv− ((P, V )),

and xP is preserved. As a result,
                                               
(30)                 Risen,k (x; q, t) =                 q hdinv(P ) tarea(P ) xP ,
                                           P ∈LD Stack
                                                 n,k
                                               
(31)                  Valn,k (x; q, t) =                 q wdinv(P ) tarea(P ) xP .
  *Proof:* Constructs bijections by removing specific east steps and moving squares in the leaning stack to translate statistics to the stack model.

- **Proposition 3.3.** We can construct a bijection θn,k : LDStack
                                                       n,k   → LDDense
                                                                 n,k   such
that
(32)                          area(θn,k (P )) = area(P ),
(33)                        wdinv(θn,k (P )) = wdinv(P ).
As a result,
                                            
(34)               Valn,k (x; q, t) =                 q wdinv(P ) tarea(P ) xP .
  *Proof:* Constructs a bijection by contracting every north step of the path that shares a row with a vertical square of the leaning stack.

- **Proposition 3.4.** For any integers 1 ≤ k ≤ n,
                                                                 ⎛  ⎞k+1   
                                                                           
                                                   1  n ⎝                  
(35)      Risen,k (x; 1, 1) + Risen,k (x; 1, 1) =             ei ui ⎠      
                                                  k+1 k                    
                                                          i≥0               n
                                                                                 u
                                                   1  n
(36)                                            =       en [(k + 1)X].
  *Proof:* Expresses the left-hand side using the number of Dyck paths with specified vertical run lengths and evaluates via Cauchy's Formula.

- **Theorem 4.1.** The coeﬃcients of the monomial quasisymmetric function M1n are
equal in each of the following:
(41)
                                                                                    
  Risen,k (x; q, 0), Risen,k (x; 0, q), Valn,k (x; q, 0), Δ ek en  t=0 ,   Δ ek en  q=0, t=q .
  *Proof:* (immediate from Proposition 4.1)

- **Proposition 4.1.** We have the following.
                                                   
(47)                  Risen,k (x; q, 0)|Mα =                q dinv(π) ,
                                               π∈OP α,k+1
                                                   
(48)                  Risen,k (x; 0, q)|Mα =                q maj(π) ,
                                               π∈OP α,k+1
                                                   
(49)                   Valn,k (x; q, 0)|Mα =                q inv(π) ,
                                               π∈OP α,k+1
                                                   
(50)                   Valn,k (x; 0, q)|Mα =                q minimaj(π) .
  *Proof:* Maps labeled paths from the leaning stacks, decorated rises, and densely labeled models to ordered multiset partitions, verifying translation of the statistics. Defers the highly technical proof of (50) relating to minimaj to Appendix A.

- **Proposition 4.2.** We have
(54)
                                                                                        
             q minimaj(π) =                 q dinv(π) =                q maj(π) =                q inv(π) .
π∈OP α,k+1                     π∈OP α,k+1                 π∈OP α,k+1                π∈OP α,k+1
  *Proof:* (no proof in this paper)

- **Theorem 5.1.** For any symmetric function f ∈ Λ(k) ,
                                                f [[n]q ]en [X[k + 1]q ]
(55)                           Δf en |t=1/q =                            .
                                                    q k(n−1) [k + 1]q
  *Proof:* Evaluates Macdonald polynomials at $t=1/q$ for hook shapes and applies Cauchy's Formula to sum over Schur functions.

- **Corollary 5.1.** q k(n−1)−(2) Δek en        is a Schur positive symmetric polynomial.
                                           t=1/q
  *Proof:* Combines Theorem 5.1 with a Schur positivity result of Garsia, Leven, Wallach, and Xin, showing polynomiality via the q-Lucas Theorem.

- **Theorem 6.1.** For any positive integer n,
(69)                  Δe1 en = Risen,0 (x; q, t) + Risen,1 (x; q, t)
                                  n/2 
                                                       
                                                      n−m
(70)                         =           s2m ,1n−2m         [p]q,t .
                                 m=0                  p=m
  *Proof:* Proven by evaluating the symmetric side with a reciprocity identity (Proposition 6.1) and resolving the combinatorial side using LLT polynomials (Proposition 6.2).

- **Proposition 6.1.** For any positive integer n,
                                     n/2 
                                                          
                                                         n−m
(71)                     Δe1 en =           s2m ,1n−2m          [p]q,t .
                                    m=0                  p=m
  *Proof:* Applies Haglund's reciprocity rule for the delta operator and evaluates principal specializations for Schur functions of hook shape.

- **Lemma 6.1.** (Corollary 2 in [Hag04]). For positive integers d, n, and any symmetric function f ∈ Λ(n) ,
                                       
(72)                      Δed−1 en , f =  Δωf ed , sd .
  *Proof:* (no proof in this paper)

- **Lemma 6.2.** (Carré and Leclerc [CL95], van Leeuwen [vL00]). For any S ∈ Stackn,1
and D ∈ LD(S), the coeﬃcient of sλ in the Schur expansion of LLTS,D (x; q) is
equal to the sum
                                  
(85)                                q hdinv(P )
                                       P
                                                                 (λ)
over all P ∈ LD(S) with D(P ) = D such that xP =                      λi
                                                                 i=1 xi      and w(P ) is Ya-
manouchi.
  *Proof:* (no proof in this paper)

- **Proposition 6.2.** For any positive integer n,
                                                          n/2 
                                                                                
                                                                               n−m
(80)          Risen,0 (x; q, t) + Risen,1 (x; q, t) =             s2m ,1n−2m         [p]q,t .
                                                          m=0                  p=m
  *Proof:* Relates the polynomials to symmetric LLT polynomials on two-column diagrams. Restricts to Yamanouchi words using Lemma 6.2 and completely classifies the allowable XY diagrams to compute the coefficients.

- **Conjecture 7.1 (4-Variable Catalan Conjecture).** We have
                                                          
(97)         Catn (q, t, z, w)|zk w  = Cat n (q, t, z, w) zk w 
                                                                  
(98)                                 = Δhk ∇en−k , s +1,1n−k− −1
                                                                  
(99)                                 = Δhk Δ en−k− −1 en−k , en−k .

Furthermore, each of these expressions is k,  -symmetric.
  *Proof:* (no proof in this paper)

- **Conjecture 7.2 (Touchpoint 4-Variable Catalan Conjecture).** For integers n ≥ k,
 , r ≥ 0, we have
                                                                
(102)          Catn,r (q, t, z, w)|zk w  = Cat n,r (q, t, z, w) zk w 
                                                                        
(103)                                    = Δh  ∇En− ,r , sk+1,1n−k− −1
                                                                        
(104)                                    = Δh  Δ en−k− −1 En− ,r , en−  ,

where the polynomials En,r are deﬁned in [Hag04].
  *Proof:* (no proof in this paper)

- **Conjecture 7.3 (Compositional 4-Variable Catalan Conjecture).** For integers n >
k,   ≥ 0, and a composition α   n −  , we have
                                                                   
(107)              Cat n,α (q, t, z) zk = Δh  ∇Cα , sk+1,1n−k− −1
                                                                   
(108)                                   = Δh  Δ en−k− −1 Cα , en−  .
  *Proof:* (no proof in this paper)

- **Proposition 7.1.** For integers m ≥ k > 0, a symmetric function f ∈ Λ(m) , and
any operator Γ deﬁned by ΓH̃μ = gμ H̃μ for some gμ ∈ Q(q, t), we have
                                                          
(109)               Γ∇f, sk+1,1m−k−1 = ΓΔ em−k−1 f, em .
  *Proof:* Employs the known scalar product of modified Macdonald polynomials with hook-shaped Schur functions.

- **Conjecture 7.4.** We have

(111)
                                                                                             
                                                                                             
   Δh  Δ en−k−1 en =           q dinv(P ) tarea(P ) xP                      1 + zt−ai (P )    .
                     P ∈PF n,                          i:ai (P )>ai−1 (P )                    k
                                                                                           z
  *Proof:* (no proof in this paper)

- **Conjecture 7.5.** We have
                                            
(112)                   Δh  ∇En,r =                   q dinv(P ) tarea(P ) xP .
                                         P ∈PF n, 
                                        touch(P )=r
  *Proof:* (no proof in this paper)