<!-- Generated 2026-05-31T02:19:20 -->
<!-- Source PDF: rourke__introduction_to_piecewise_linear_topology.pdf (95031 bytes) -->
<!-- Citation: Colin P. Rourke, Brian J. Sanderson (1982). Introduction to Piecewise-Linear Topology. Springer. -->

# Introduction to Piecewise-Linear Topology (Colin P. Rourke, Brian J. Sanderson, 1982)

## Definitions
- **Definition.** The barycentric subdivision K (1) of the simplicial complex K is
constructed as follows. It has precisely one vertex in the interior of each simplex
of K (including having a vertex at each vertex of K). A collection of vertices of
K (1) , in the interior of simplices σ1 , . . . , σr of K, span a simplex of K (1) if and
only if σ1 is a face of σ2 , which is a face of σ3 , etc (possibly after re-ordering
σ1 , . . . , σr ).
- **Definition.** The r th barycentric subdivision of a simplicial complex K for each
r ∈ N is defined recursively to be (K (r−1) )(1) , where K (0) = K.
- **Definition.** If L is a subcomplex of the simplicial complex K, then the regular
neighbourhood N (L) of K is the closure of the set of simplices in K (2) that
intersect L. It is a subcomplex of K (2) .
- **Definition.** A handle structure of an n-manifold M is a decomposition of M into
n + 1 sets H0 , . . . , Hn having disjoint interiors, such that

  • Hi is a collection of disjoint n-balls, known as i-handles, each having a product
    structure Di × Dn−i,
                                          Si−1
  • for each i-handle (Di × Dn−i) ∩ (       j=0 Hj ) = ∂D
                                                            i
                                                                × Dn−i,

  • if Hi = Di ×Dn−i (respectively, Hj = Dj ×Dn−j ) is an i-handle (respectively,
    j-handle) with j < i, then Hi ∩ Hj = Dj × E = F × Dn−i for some (n −
    j − 1)-manifold E (respectively, (i − 1)-manifold F ) embedded in ∂Dn−j
    (respectively, ∂Di ).
- **Definition.** A handlebody of genus g is the 3-manifold with boundary obtained
from a 3-ball B 3 by gluing 2g disjoint closed 2-discs in ∂B 3 in pairs via orientation-
reversing homeomorphisms.
- **Definition.** Let C be a simple closed curve in the interior of the surface F . Let
N (C) ∼
      = S 1 × [−1, 1] be a regular neighbourhood of C. Then a Dehn twist about
C is the map h: F → F which is the identity outside N (C), and inside N (C) sends
(θ, t) to (θ + π(t + 1), t).

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 4.1.** (Regular neighbourhoods are ambient isotopic) Suppose that K ′
is a subdivision of a simplicial complex K. Let L be a subcomplex of K, and let L′
be the subdivision K ′ ∩ L. Then the regular neighbourhood of L in K is ambient
isotopic to the regular neighbourhood of L′ in K ′ .
  *Proof:* (no proof in this paper)
- **Theorem 4.2.** Every pl manifold has a handle structure.
  *Proof:* Constructs handles by taking the closure of the union of second-barycentric subdivision simplices touching the interior vertices of the initial triangulation.
- **Proposition 4.3.** Suppose that P and Q are subcomplexes of a closed manifold
M , with dim(P ) = p, dim(Q) = q and dim(M ) = M . Then there is a homeo-
morphism h: M → M isotopic to the identity such that h(P ) and Q intersect in a
simplicial complex of dimension of at most p + q − m.
  *Proof:* (no proof in this paper)
- **Lemma 4.4.** Any pl homeomorphism ∂Dn → ∂Dn extends to a pl homeomor-
phism Dn → Dn .
  *Proof:* Extends the boundary homeomorphism to the interior radially (conewise) from the origin.
- **Lemma 4.5.** Two homeomorphisms Dn → Dn which agree on ∂Dn are isotopic.
  *Proof:* Applies an analogous conewise extension argument.
- **Proposition 4.6.** A homeomorphism Dn → Dn is isotopic either to the identity
or to r.
  *Proof:* Proceeds by induction on dimension, decomposing boundaries into faces and applying unique conewise extensions to extend isotopies.
- **Proposition 4.7.** Let h1 : Dn → M and h2 : Dn → M be embeddings of the n-ball
into an n-manifold. Then there is a homeomorphism h: M → M isotopic to the
identity such that h ◦ h1 is either h2 or h2 ◦ r.
  *Proof:* (no proof in this paper)
- **Proposition 4.8.** The space obtained by gluing two n-balls along two closed
(n − 1)-balls in their boundaries is homeomorphic to an n-ball.
  *Proof:* (no proof in this paper)
- **Lemma 5.1.** Let H be a connected orientable 3-manifold with a handle structure
consisting of only 0-handles and 1-handles. Then H is a handlebody.
  *Proof:* Regluing the handles sequentially demonstrates that external disc identifications yield a 3-ball and internal ones provide orientation-reversing pairs.
- **Theorem 5.2.** Any closed orientable 3-manifold M has a Heegaard splitting.
  *Proof:* Partitions the manifold's handle structure by grouping 0- and 1-handles into one handlebody, and 2- and 3-handles into a second handlebody.
- **Theorem 5.3.** [Dehn, Lickorish] Any orientation preserving homeomorphism of
a compact orientable surface to itself is isotopic to the composition of a finite
number of Dehn twists.
  *Proof:* (no proof in this paper)
- **Theorem 5.4.** [Lickorish, Wallace] Every closed orientable 3-manifold M is ob-
tained by surgery along some link in S 3 .
  *Proof:* Represents the manifolds via glued Heegaard splittings, factors the gluing differences as Dehn twists, and tracks regular neighborhoods to isolate solid-tori surgeries on $S^3$.