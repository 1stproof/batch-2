<!-- Generated 2026-05-31T02:11:54 -->
<!-- Source PDF: carlsson__a_proof_of_the_shuffle_conjecture.pdf (433098 bytes) -->
<!-- Citation: E. Carlsson, A. Mellit (2018). A proof of the shuffle conjecture. Journal of the American Mathematical Society. -->

# A proof of the shuffle conjecture, E. Carlsson, A. Mellit (2018)

## Definitions
- **Definition 3.1.**                              ÿ
                                  χpπq :“           q invpπ,wq xw .
                                            wPZn
                                               ą0

- **Definition 4.2.** Let Vk “ SymrXs b Qry1 , y2, . . . , yk s, and let
                        Ti “ ∆˚yi yi`1 : Vk Ñ Vk ,     i “ 1, . . . , k ´ 1.
Define operators
                             d` : Vk Ñ Vk`1 ,     d´ : Vk Ñ Vk´1
by
(4.1)                 pd` F qrXs “ T1 T2 ¨ ¨ ¨ Tk pF rX ` pq ´ 1qyk`1sq ,
and
(4.2)               pd´ F qrXs “ ´F rX ´ pq ´ 1qyk s Expr´yk´1Xs|y´1
                                                                               k

for F P Vk .

- **Definition 5.1.** The Dyck path algebra A “ Aq (over R) is the path algebra of the
quiver with vertex set Zě0 , arrows d` from i to i ` 1, arrows d´ from i ` 1 to i for
i P Zě0 , and loops T1 , T2 , . . . , Tk´1 from k to k subject to the following relations:
       pTi ´ 1qpTi ` qq “ 0,    Ti Ti`1 Ti “ Ti`1 Ti Ti`1 ,   Ti Tj “ Tj Ti   p|i ´ j| ą 1q,
            Ti d´ “ d´ Ti , d` Ti “ Ti`1 d` , T1 d2` “ d2` , d2´ Tk´1 “ d2´ ,
                d´ pd` d´ ´ d´ d` qTk´1 “ qpd` d´ ´ d´ d` qd´ pk ě 2q,
                      T1 pd` d´ ´ d´ d` qd` “ qd` pd` d´ ´ d´ d` q,
where in each identity k denotes the index of the vertex where the respective paths
begin. We have used the same letters Ti , d˘ to label the ith loop at every node k to
match with the previous notation. To distinguish between different nodes, we will
use Ti ek where ek is the idempotent associated with node k.

- **Definition 7.1.** Consider A and A˚ as algebras over Qpq, tq, and let Ã “ Ãq,t be
the quotient of the free product of A and A˚ by the relations
                                  d˚´ “ d´ ,       Ti˚ “ Ti´1 ,    e˚i “ ei ,
                  zi`1 d` “ d` zi ,       yi`1 d˚` “ d˚` yi ,     z1 d` “ ´y1d˚` tq k`1 ,

## Lemmas, Theorems, Propositions, Corollaries
- **Proposition 2.2.** For every Dyck path π
                                          touch1 pπ 1 q “ touchpπq.
  *Proof:* Uses a translated copy of the Dyck path to reconstruct the sizes of the gaps between touch points from the bounce statistic.

- **Proposition 2.4.** For any composition α we have
                             ÿ                ÿ
(2.5)           Dα pq, tq “        tbouncepπq   q invpπ,wq xw ,
                                    touch1 pπq“α           wPWP 1π

where Dα pq, tq is the right hand side of (2.2).
  *Proof:* (no proof in this paper)

- **Proposition 3.2.** The expression for χpπq above is symmetric in the variables
x1 , x2 , x3 , . . ., so that Definition 3.1 correctly defines an element of SymrXs.
  *Proof:* Follows [HHL05a] by showing invariance under transpositions of adjacent variables via induction on the size of the set of attacked pairs.

- **Proposition 3.3.** 
                                       χpπq “ χpπ op q.
  *Proof:* (no proof in this paper)

- **Proposition 3.4.** 
                               ω̄χpπq “ p´1q|π| q ´ areapπq χpπq.
  *Proof:* Expresses χpπq via Gessel's quasisymmetric functions on a super alphabet and evaluates at X “ 0, Y “ ´X.

- **Proposition 3.5.** 
                                                           ÿ
                  χpπqrpq ´ 1qXs “ pq ´ 1q|π|                        q invpπ,wq xw ,
                                                         |π|
                                                   wPZą0 no attack

where “no attack” means that the summation is only over vectors w such that wi ‰
wj for pi, jq P Areapπq.
  *Proof:* Evaluates the super alphabet expansion at X “ qX, Y “ X and applies an involution to cancel terms with the same absolute value.

- **Proposition 3.7.** We have that χpπ, wtq is symmetric in the xi variables, and so
defines an element of SymrXs.
  *Proof:* Expresses χpπ, wtq recursively by turning corners of the Dyck path inside out, reducing it to the symmetric unweighted version.

- **Proposition 4.1.** We have the following relations:
                  p∆uv ´ qqp∆uv ` 1q “ 0,            p∆˚uv ´ 1qp∆˚uv ` qq “ 0,
               ∆uv ∆vw ∆uv “ ∆vw ∆uv ∆vw ,           ∆˚uv ∆˚vw ∆˚uv “ ∆˚vw ∆˚uv ∆˚vw .
  *Proof:* (no proof in this paper)

- **Theorem 4.4.** For any Dyck path π of size n, let ǫ1 ¨ ¨ ¨ ǫ2n denote the corresponding
sequence of plus and minus symbols where a plus denotes an east step, and a minus
denotes a north step reading π from bottom left to top right. Then
                                    χpπq “ dǫ1 ¨ ¨ ¨ dǫ2n p1q
as an element of V0 “ SymrXs.
  *Proof:* Defines characteristic functions for partial Dyck paths, then relates the raising and lowering operators to their recursive steps. Employs swapping operators and modified Demazure-Lusztig operators to compute the evaluation coefficients.

- **Corollary 4.6.** The following procedure computes χpπ, 0q: start with 1 P SymrXs “
                                                  1
V0 , follow the path from right to left applying q´1 rd´ , d` s for each corner of w, and
d´ (d` ) for each North (resp. East) step which is not a side of a corner.
  *Proof:* (immediate from Theorem 4.4)

- **Proposition 4.8.** For any w P Dk , σ as above and m special suppose that m ` 1 is
not special or σ ´1 pmq ă σ ´1 pm ` 1q. Then we have
                                       χ1τm σ pwq “ ∆zm ,zm`1 χ1σ ,
where τm is the transposition m Ø m ` 1, pτm σqi “ τm pσi q for i “ 1, . . . , k.
  *Proof:* Decomposes the sum into equivalence classes based on the positions of the swapped elements, showing the operator matches the symmetric evaluation on runs of non-attacking labels.

- **Proposition 4.10.** Denote Xr “ yk ` x1 ` ¨ ¨ ¨ ` xr , X´1 “ 0. We have
                             hi rp1 ´ qqXr s ´ hi rp1 ´ qqXr´1 s
                      fi,r “                                     .
                                            1´q
  *Proof:* Proceeds by induction on r, applying the swapping operator to verify the recurrence step.

- **Theorem 4.11.** If α is a composition of length l, we have
                                  Dα pq, tq “ dl´ pNα q.
where Nα P Vl is defined by the recursion relations
                                                         ta´1              ÿ lpβq´1
(4.17)      NH “ 1,     Nr1,αs “ d` Nα ,      Naα “           rd´ , d` s        d´  Nαβ .
                                                         q´1             β|ùa´1
  *Proof:* Reconstructs the bounce and touch statistics of Dyck paths extended by steps, showing the combinatorial operations translate to the given algebraic recurrence.

- **Proposition 4.14.** Let π be Dyck path of size N ending with k East steps, and let
pǫ1 , ..., ǫ2N ´k , `k q denote the corresponding sequence of plus and minus symbols, as
in Theorem 4.4. Then for f P Vk , we have
                                                                           ˇ
                                      pf q r´1s “ p´1qN q areapπq f r´q k sˇ
                      `                   ˘
(4.18)                  dǫ 1 ¨ ¨ ¨ dǫ
                            2N´k                                        yi “qi´1 .
  *Proof:* Uses induction on the sequence of operators, analyzing the terminal step to verify the evaluation homomorphism.

- **Theorem 5.2.** The operators (5.1) define a representation of A on V˚ . Furthermore,
we have an isomorphism of representations
                                                   „
                                         ϕ : Ae0 Ý
                                                 Ñ V˚
which sends e0 to 1 P V0 , and maps ek Ae0 isomorphically onto Vk .
  *Proof:* Verifies the operators satisfy the path algebra relations and constructs elements corresponding to the variables. Shows a canonical basis of the algebra maps to the Hall-Littlewood basis to establish the isomorphism.

- **Lemma 5.3.** The operators Ti and d˘ satisfy the relations of Definition 5.1.
  *Proof:* Directly calculates the commutation relations and zero-identities of the operators using plethystic substitutions.

- **Lemma 5.4.** For F P Vk we have
                                                                               1
(5.4)        pd´ d` ´ d` d´ qF “ pq ´ 1qT1 T2 ¨ ¨ ¨ Tk´1 p´yk F q,         yi “ Ti yi`1 Ti .
                                                                               q
  *Proof:* Uses a twisted action of symmetric functions to commute with the operators, reducing the identities to evaluation on variables by homogeneity.

- **Lemma 5.5.** For k P Zą0 define elements y1 , . . . , yk P ek Aek by solving for yi F in
the identities (5.4). Then the following identities hold in A:
                                yi Tj “ Tj yi       for i R tj, j ` 1u,
                 yi d´ “ d´ yi ,       d` yi “ T1 T2 ¨ ¨ ¨ Ti yi pT1 T2 ¨ ¨ ¨ Ti q´1 d` ,
                                    yi yj “ yj yi    for any i, j.
  *Proof:* Expands the identities established for individual generators to the rest via the T-operators and algebraic manipulations.

- **Lemma 5.6.** The elements of the form
                                          a1        a
(5.6)                                 dm            k`m k`m
                                       ´ y1 ¨ ¨ ¨ yk`m d`   e0
with ak`1 ě ak`2 ě ¨ ¨ ¨ ě ak`m form a basis of Ae0 . Furthermore, the representation
ϕ maps these elements to a basis of V˚ .
  *Proof:* Applies reduction rules and a lexicographical argument to prove spanning, and identifies the images as multiples of the Hall-Littlewood basis.

- **Theorem 6.1.** There is an action of A˚ on V˚ given by the assignment
(6.2)     Ti˚ “ Ti´1 ,   d˚´ “ d´ ,     e˚i “ ei ,   pd˚` F qrXs “ γF rX ` pq ´ 1qyk`1s,
where F P Vk and γ is the operator which sends yi to yi`1 for i “ 1, . . . , k and yk`1
to ty1 . Furthermore, it satisfies the additional relations
(6.3) zi`1 d` “ d` zi ,     yi`1 d˚` “ d˚` yi ,   z1 d` “ ´y1 d˚` tq k`1 ,    d˚` dm        m`1
                                                                                   ` p1q “ d`   p1q
for any m ě 0.
  *Proof:* Constructs the conjugated operators and confirms their identities by systematically verifying intertwining properties with twisted multiplications across multiple propositions.

- **Proposition 6.2.** 
                 d˚` Ti´1 “ Ti`1
                              ´1 ˚
                                 d` ,       T1´1 d˚2   ˚2
                                                  ` “ d` ,         d˚` yi “ yi`1d˚` .
  *Proof:* Directly follows from the definition of the conjugated operators and basic algebraic manipulation.

- **Proposition 6.3.** 
(6.5)            d´ pd˚` d´ ´ d´ d˚` qTk´1
                                       ´1
                                           “ q ´1 pd˚` d´ ´ d´ d˚` qd´       pk ě 2q.
  *Proof:* Reformulates the identity and evaluates it on symmetric polynomials, demonstrating it vanishes due to antisymmetry properties.

- **Proposition 6.4.** 
                      T1´1 pd˚` d´ ´ d´ d˚` qd˚` “ q ´1 d˚` pd˚` d´ ´ d´ d˚` q.
  *Proof:* Evaluates both sides on powers of variables and verifies the equality using generating function identities.

- **Proposition 6.5.** 
                          z1 d` “ ´y1 d˚` tq k`1 ,          zi`1 d` “ d` zi .
  *Proof:* Verifies intertwining properties with twisted multiplications and symmetric functions, reducing the check to evaluations on basic polynomials.

- **Proposition 6.6.** For a composition α of length k let
                                            yα “ y1α1 ´1 ¨ ¨ ¨ ykαk ´1 P Vk .
Then the following recursions hold:
                         t1´a ˚                   ÿ              lpβq´1
   y1α “ d˚` yα , yaα “       pd` d´ ´ d´ d˚` q        q 1´lpβq d´      pyαβ q pa ą 1q.
                         q´1                    β|ùa´1
  *Proof:* Evaluates the explicit formulas for the operators, matching the extracted coefficients to the symmetric functions using previously established identities.

- **Theorem 7.3.** The operations Ti , d´ , d` , d˚` , ei define an action of Ã on V˚ .
Furthermore, the kernel of the natural map Ãe0 Ñ V˚ that sends f e0 to f p1q is
given by Ie0 where I Ă Ã is the ideal generated by
(7.1)                            I “ xd˚` dm    m`1
                                           ` ´ d`   |         m ě 0y.
In particular, we have an isomorphism V˚ – Ãe0 {Ie0 .
  *Proof:* Shows surjectivity via module maps and proceeds by induction on the total degree of the operators to prove the quotient space is isomorphic.

- **Theorem 7.4.** There exists a unique antilinear degree-preserving automorphism
N : V˚ Ñ V˚ satisfying
     N p1q “ 1,     N Ti “ Ti´1 N ,     N d´ “ d´ N ,     N d` “ d˚` N ,     N yi “ zi N .
Moreover, we have
    (i) N is an involution, i.e. N 2 “ Id.
   (ii) For any composition α we have
                                                ř
                                    N pyαq “ q pαi ´1q Nα .
   (iii) On V0 “ SymrXs, we have N “ ∇ω̄, where ω̄ is the involution sending q,
         t, X to q ´1 , t´1 , ´X resp. (see (6.1)).
  *Proof:* Extends the natural involution on the algebra to the vector space, confirming it matches the algebraic relations and reduces to the standard symmetric function operator.

- **Theorem 7.5.** For a composition α of length k, we have
                               ∇Cα1 ¨ ¨ ¨ Cαk p1q “ Dα pX; q, tq.
  *Proof:* Translates the lowering operator sequence applied to the composition algebraically via the involution to exactly match the compositional shuffle conjecture.