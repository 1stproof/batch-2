<!-- Generated 2026-05-31T02:10:56 -->
<!-- Source PDF: egge__from_quasisymmetric_expansions_to_schur_expansions.pdf (193323 bytes) -->
<!-- Citation: E. Egge, N. Loehr, G. Warrington (2010). From quasisymmetric expansions to Schur expansions via a modified inverse Kostka matrix. European Journal of Combinatorics. -->

# From quasisymmetric expansions to Schur expansions via a modified inverse Kostka matrix (Egge, Loehr, Warrington, 2010)

## Definitions

*(No labeled definitions in this paper)*

## Lemmas, Theorems, Propositions, Corollaries

- **Proposition 5.** For all n ≥ 1, Kn Kn′ = Ip(n) .
  *Proof:* Uses a sign-reversing involution on pairs of semistandard and special rim-hook tableaux from Eğecioğlu and Remmel, alongside Bender-Knuth bijections.

- **Proposition 6.** Every entry of Kn′ is +1, 0, or −1. Moreover, these entries can be computed by the recursion (4) described below.
  *Proof:* Observes there is at most one valid placement for the final special rim-hook and applies induction.

- **Lemma 9.** For all n ≥ 1, Mn An = Kn .
  *Proof:* Establishes a standardizing bijection between semistandard tableaux and standard tableaux that tracks descent compositions.

- **Theorem 11.** Suppose F is a field, and we have a symmetric function
                          X            X
                     f=        xλ sλ =    y α Qα   (xλ , yα ∈ F ).
                                    λ⊢n               α|=n

The row vectors x = (xλ : λ ⊢ n) and y = (yα : α |= n) satisfy
                                          xMn = y           and   x = yKn∗ .
                     ∗
           P
So, xλ =    α|=n yα Kn (α, λ) for all λ ⊢ n.
  *Proof:* Relates the symmetric and quasisymmetric expansions into a matrix equation and multiplies on the right by the inverse Kostka projection matrix.

- **Lemma 14.** Let S be a special rim-hook tableau of shape λ and content α. Suppose ri−1 and ri
are consecutive rim-hooks in the special rim-hook tableau S. Then either

    1. the last cell of ri is immediately above a cell of ri−1 , or

    2. the last cell of ri−1 is immediately to the left of a cell of ri .
  *Proof:* (no proof in this paper)

- **Theorem 15.** Let α |= n, λ ⊢ n. If (α, λ) is flat, then Kn∗ (α, λ) = Kn′ (α, λ) = ±1. Otherwise,
Kn∗ (α, λ) = 0. In particular, Kn∗ (α, λ) = χ(α = λ) when λ is a hook.
  *Proof:* Applies the pigeonhole principle to prove the formula for the flat case. For the non-flat case, defines a sign-reversing involution on the set of finer realizable compositions by extending or shortening consecutive rim-hooks in the first column.

- **Lemma 18.** Let λ ⊢ n and suppose (c, λc ), c < λc , is an inner corner of dg(λ). Write λ−
for the partition of n − 1 obtained by removing this cell (c, λc ). Then srht(λ) = srht(λ− ) and
srht(λ) = srht(λ− ).
  *Proof:* Constructs a bijection mapping realizable pairs to smaller shapes by shortening a maximal rim-hook and locally rerouting the rest.

- **Theorem 19.** For all partitions λ, the number of flat special rim-hook tableaux of shape λ is
Q k       i
  i=1 DF(λ ).
  *Proof:* Proceeds by induction on the number of parts, iteratively inserting a new special rim-hook along the bottom row and splicing vertical segments.

- **Corollary 20.** Fix k with √n < k ≤ n. The maximum of srht(λ) over all partitions λ ⊢ n
with k parts is attained by λ = ν where ν t = (k, k, . . . , k, n mod k). Writing d = ⌊n/k⌋ and
a = min(k − (n mod k), k − d),
                                       srht(ν) = d!da (d + 1)k−d−a ≤ (d + 1)k .                  (7)
               √
If instead k ≤ n, then the maximum of srht(ν) is k!, and this maximum is obtained for any ν
such that ν1t = · · · = νkt = k.
  *Proof:* Compares arbitrary partitions to the specified almost-rectangular shapes by iteratively moving inner corners to outer corners and tracking the rim-hook counts via Theorem 19.

- **Theorem 21.** Define a generating function A(q) = Pn Pλ⊢n srht(λ)q n . Then
                                                        
                     ∞                 k            k            ∞        k
                                                                X k Y jq j Y 1     k
                                                1     Y 1
                                                                 q (2 )
                                   2
                     X                 Y
            A(q) =         k!q k                              =                         .        (8)
                                             1 − jq j  1 − qj           1 − jq j 1 − qj
                     k=0               j=1         j=1          k=0      j=1      j=1
  *Proof:* Decomposes partitions by their Durfee square size and uses independent choices for column heights and diagonal lengths to construct the generating function.

- **Theorem 24.** For all λ, µ ⊢ n,
                                                                                                     
                                     X                             X
                     hH̃µ , sλ i =          Kn∗ (α, λ)                          q invµ (w) tmajµ (w)  .         (10)
                                     α|=n                              ′
                                                            w∈Sn :IDes (w)=α

So, if λ is a hook, then the coefficient of sλ in H̃µ is the sum of q invµ (w) tmajµ (w) over those
w ∈ Sn such that IDes′ (w) = λ.
  *Proof:* (no proof in this paper)