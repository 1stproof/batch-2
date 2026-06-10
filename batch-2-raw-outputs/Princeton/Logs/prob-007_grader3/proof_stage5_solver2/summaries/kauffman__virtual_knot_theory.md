<!-- Generated 2026-05-31T03:11:58 -->
<!-- Source PDF: kauffman__virtual_knot_theory.pdf (790637 bytes) -->
<!-- Citation: Louis H. Kauffman (1999). Virtual Knot Theory. European Journal of Combinatorics. -->

# Virtual Knot Theory. Louis H. Kauffman (1999). European Journal of Combinatorics.

## Definitions
- **Definition.** A single component Gauss code g is said to be evenly intersticed if there is an even number of labels in between the two appearances of any label.
- **Definition.** A Gauss code g is said to be prime if it cannot be written as the juxtaposition of two Gauss codes on disjoint collections of labels. A non-prime code is said to be composite.
- **Definition.** Let N(G) denote the number of vertices in the 4-valent graph G. A Vassiliev invariant v is said to be of graphical finite type n if v(G) = 0 whenever N(G) > n. Note that this definition says nothing about the number of virtual crossings in the graph G.

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 1.** If g is a single component planar Gauss code, then g is evenly intersticed.
  *Proof:* Applies the Jordan curve theorem to the planar embedding.

- **Theorem 2.** If K is a virtual knot whose underlying Gauss code is planar and whose sign sequence is standard, then K is equivalent to a classical knot.
  *Proof:* Uses the reconstruction algorithm to dictate planar positions for virtual arcs, moving them into embedded orientations via virtual equivalence.

- **Lemma 3.** If g is a planar Gauss code, then g ∗ is dually paired.
  *Proof:* (no proof in this paper)

- **Lemma 4.** If an evenly intersticed Gauss code g has g ∗ dually paired, then g is the Gauss code of a planar shadow.
  *Proof:* (no proof in this paper)

- **Lemma 5.** 
                                IQ(Kvxv ) = IQ(Kx )
where x denotes a crossing in the diagram K, vxv denotes that x is flanked by virtuals, and Kx denotes the diagram obtained by smoothing the flanking virtuals, and switching the intermediate crossing.
  *Proof:* (no proof in this paper)

- **Theorem 6.** If K and K ′ are classical knot diagrams such that K and K ′ are equivalent under extended virtual Reidemeister moves, then K and K ′ are equivalent under classical Reidemeister moves.
  *Proof:* Relies on the fact that an isomorphism induced by extended virtual moves preserves longitudes, thereby classifying classical knots.

- **Lemma 7.** < Kvxv >=< Kx > where x denotes a crossing in the diagram K, vxv denotes that x is flanked by virtuals, and Kx denotes the diagram obtained by smoothing the flanking virtuals, and leaving the crossing the same.
  *Proof:* Verified purely diagrammatically via reduction loops.

- **Theorem 8.** With Z(K) defined as above and K a classical knot or link, Z(K) = d < K > where d = −A2 − A−2 .
  *Proof:* (no proof in this paper)

- **Proposition 9.** The invariant of virtual regular isotopy Z(K) is described by the following state summation.
                                 X                Y
                       Z(K) =           < K|S >         d(C)
                                    S             C∈S

where the terms in this formula are as defined above. Note that Z(K) reduces to d < K > when K is a classical diagram.
  *Proof:* (no proof in this paper)

- **Lemma 10.** Let FK (x) = fK (ex ) denote the power series resulting from substitution of ex for the variable A in the Laurent polynomial fK (A) (defined in section 2). Write this power series in the form
                                      X
                                      ∞
                           FK (x) =         vm (K)xm .
                                      m=0

Then the numerical invariants vk (K) are of finite graphical type k.
  *Proof:* Factors the difference polynomial between oriented node evaluations to demonstrate direct divisibility by the number of component nodes.

- **Proposition 11.** Let G be a graph with n vertices so that N(G) = n, configured as a virtual diagram in the plane. Let (G|+) denote the diagram G with a specific crossing of positive type and (G|−) the diagram identical to G except that the crossing has been switched to one of negative type. Let (G|∗) denote the result of replacing this crossing by a graphical vertex. Let v be a Vassiliev invariant of type n = N(G). Then v(G|+) = v(G|−). Thus a Vassiliev invariant of type n is independent of the settings of the crossings (plus or minus) in a diagram for G.
  *Proof:* Direct evaluation of the Vassiliev difference definition by noting the $(n+1)$-vertex term vanishes.

- **Corollary 12.** If G and v are as in Proposition 11 , and G is a classical diagram (free of virtual crossings) then v(G) does not depend upon the classical embedding of G in R3 that is indicated by the diagram.
  *Proof:* (immediate from Proposition 11)

- **Theorem 13.** With notation as above, the following recursion formula holds for the Vassiliev invariants vn (G).

                               X
                               n−1
                  vn (G∗ ) =         cn,k (vk (G0 ) + 2n−k vk (G∞ ))
                               k=0

where

                   (2n−k (1 + (−1)n−k+1 )/(n − k)! = cn,k .
The value of v0 (K) on a virtual diagram without graphical nodes depends only on the number of components in the diagram, and is independent of the configuration of virtual crossings. Specifically,

                               v0 (K) = (−2)µ(K)−1
where µ(K) denotes the number of link components in K.
  *Proof:* Translates polynomial difference states into an algebraic equation before evaluating the binomial expansion. Derives the base condition by assessing the classical crossings against virtual crossings via a matrix model evaluated at $A=1$.

- **Corollary 14.** The Vassiliev invariants vn (G) in the series FK (x) depend only on the chord diagram associated with G when G is a virtual diagram with n graphical nodes. Hence the weight systems for the invariants vn (G) do not depend upon virtual crossings.
  *Proof:* (immediate from Theorem 13)