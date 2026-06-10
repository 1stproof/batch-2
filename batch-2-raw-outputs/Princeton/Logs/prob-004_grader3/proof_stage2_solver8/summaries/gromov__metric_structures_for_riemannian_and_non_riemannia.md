<!-- Generated 2026-05-31T01:48:18 -->
<!-- Source PDF: gromov__metric_structures_for_riemannian_and_non_riemannia.pdf (1204331 bytes) -->
<!-- Citation: Mikhail Gromov (1999). Metric structures for Riemannian and non-Riemannian spaces. Birkhäuser. -->

# Metric Structures for Riemannian and Non-Riemannian Spaces (Gromov, 1999)

## Definitions
- **1.1. Definition.** The dilatation of a mapping / between metric spaces
X, Y is the (possibly infinite) number




where "oJ" stands for the metrics (distances) distx in X and disty in Y.
The local dilatation of / at 2: is the number

                        diU(/) = l i m d i l ( / | B ( . , . ) ) .
A map / is called Lipschitz if dil(/) < OD; it is called X-Lipschitz if dil(/) <
A, in which case, the infimal such A is called the Lipschitz constant of / .
- **1.2. Definition.**      The length of a Lipschitz map / : [a, 6] —^X is the
number

                                       J a

If / is merely continuous, we can define £{f) as the supremum of all sums
of the form Yl'i^od{f{U), fiU+i)) where a = to < ti < -- - < tn^i = 6 is a
finite partition of [a,b].
- **1.3. Definition.** A length structure on a set X consists of a family C{I)
of mappings / : / —^ X for each interval I and a map i of C = [jC{I) into
R having the following properties:

    (a) Positivity: We have £(/) > 0 for each f e C, and £{f) = 0 if and
        only if / is constant (we assume of course that the constant functions
        belong to C).
    (6) Restriction, juxtaposition: If / C J, then the restriction to /
        of any member of C{J) is contained in C{I). If / G C([a,6]) and
        g E C{[b,c]), then the function h obtained by juxtaposition of / and
        g lies in C{[a, c]) and i{h) = £{f) + ({g).

    (c) Invariance under change of parameter: If (/? is a homeomor-
        phism from / onto J and if / G C(J), then f o ip e C{I) and
        eifoip) = e{f).
    (d) Continuity: For each / = [a, 6], the map 11-> £{f\[a,t]) is continuous.
- **1.7. Definition.**     A metric space (X^d) is a path metric space if the
distance between each pair of points equals the infimum of the lengths of
curves joining the points (i.e., ii d = di).
- **1.9. Definition.** A minimizing geodesic in a path metric space {X,d) is
any curve f: I -^ X such that d{f{t)J{t'))   = \t - f\ for each t,t' e L A
geodesic in X is any curve f: I -^ X whose restriction to any sufficiently
small subinterval in / is a minimizing geodesic.

## Lemmas, Theorems, Propositions, Corollaries
- **1.6. Proposition.** //, for each interval I, the function i is lower semi-
continuous on C{I) with respect to the compact-open topology, then £ = i.
  *Proof:* Bounds the length of an approximating curve built from partitions with small increments, showing £ ≤ i using lower semicontinuity.
- **1.8. Theorem.** The following properties of a metric space (X, d) are equiv-
alent:

   1. For arbitrary points x,y ^ X and e > 0, there is a z such that

                          sup(d(x, z), d{z, y)) < - d{x, y) + e,

   2. For arbitrary x^y E X and ri,r2 > 0 with ri + r2 < d{x^y), we have

                        d{B{x, ri), B{y, r2)) < d{x, y) - ri - r2,

         for
                              d{B^,B2)=         inf      dix',y').
                                              y' e B2


Every path metric space has these properties, and conversely, if (X, d) is
complete and satisfies (1) or (2), then it is a path metric space.
  *Proof:* Applies the distance bound iteratively to define a sequence of points on dyadic rationals, which extends to a continuous length-approximating curve by completeness.
- **[FLAG: missing label] Hopf—Rinow theorem.** If (X, d) is a complete, locally compact path met-
ric space, then

   1. Closed balls are com,pact, or, equivalently, each hounded, closed do-
      main is compact.

   2. Each pair of points can he joined hy a minimizing geodesic.
  *Proof:* Establishes compactness of closed balls via a diagonal argument on Cauchy sequences, then proves geodesic existence by applying Ascoli's theorem to extract a converging sequence of length-minimizing curves.
- **[FLAG: missing label] Lemma.** / / {X, d) is a compact path metric space and a, 6 € X, then there
exists a curve of length d{a^ b) joining a and b.
  *Proof:* Uses Ascoli's theorem to extract a uniformly converging curve from an equicontinuous sequence of paths parameterized by arc length.