<!-- Generated 2026-05-31T01:50:37 -->
<!-- Source PDF: gromov__metric_structures_for_riemannian_and_non_riemannia.pdf (1204331 bytes) -->
<!-- Citation: Gromov, M. (1999). Metric Structures for Riemannian and Non-Riemannian Spaces. Birkhäuser. -->

# Metric Structures for Riemannian and Non-Riemannian Spaces (Gromov, 1999)

## Definitions
- **1.1. Definition:** The dilatation of a mapping / between metric spaces X, Y is the (possibly infinite) number




where "oJ" stands for the metrics (distances) distx in X and disty in Y.
The local dilatation of / at 2: is the number

                        diU(/) = l i m d i l ( / | B ( . , . ) ) .
A map / is called Lipschitz if dil(/) < OD; it is called X-Lipschitz if dil(/) <
A, in which case, the infimal such A is called the Lipschitz constant of / .
- **1.2. Definition:** The length of a Lipschitz map / : [a, 6] —^X is the
number

                                       J a

If / is merely continuous, we can define £{f) as the supremum of all sums
of the form Yl'i^od{f{U), fiU+i)) where a = to < ti < -- - < tn^i = 6 is a
finite partition of [a,b].
- **1.3. Definition:** A length structure on a set X consists of a family C{I) of mappings / : / —^ X for each interval I and a map i of C = [jC{I) into R having the following properties: (a) Positivity: We have £(/) > 0 for each f e C, and £{f) = 0 if and only if / is constant (we assume of course that the constant functions belong to C). (6) Restriction, juxtaposition: If / C J, then the restriction to / of any member of C{J) is contained in C{I). If / G C([a,6]) and g E C{[b,c]), then the function h obtained by juxtaposition of / and g lies in C{[a, c]) and i{h) = £{f) + ({g). (c) Invariance under change of parameter: If (/? is a homeomorphism from / onto J and if / G C(J), then f o ip e C{I) and eifoip) = e{f). (d) Continuity: For each / = [a, 6], the map 11-> £{f\[a,t]) is continuous.
- **1.7. Definition:** A metric space (X^d) is a path metric space if the distance between each pair of points equals the infimum of the lengths of curves joining the points (i.e., ii d = di).
- **1.9. Definition:** A minimizing geodesic in a path metric space {X,d) is any curve f: I -^ X such that d{f{t)J{t'))   = \t - f\ for each t,t' e L A geodesic in X is any curve f: I -^ X whose restriction to any sufficiently small subinterval in / is a minimizing geodesic.

## Lemmas, Theorems, Propositions, Corollaries
- **1.6. Proposition:** //, for each interval I, the function i is lower semicontinuous on C{I) with respect to the compact-open topology, then £ = i.
  *Proof:* Approximates curve lengths using a finite partition and bounding sub-paths, relying on the uniform continuity and lower semicontinuity of the length function.
- **1.8. Theorem:** The following properties of a metric space (X, d) are equivalent: 1. For arbitrary points x,y ^ X and e > 0, there is a z such that sup(d(x, z), d{z, y)) < - d{x, y) + e, 2. For arbitrary x^y E X and ri,r2 > 0 with ri + r2 < d{x^y), we have d{B{x, ri), B{y, r2)) < d{x, y) - ri - r2, for d{B^,B2)=         inf      dix',y'). y' e B2 Every path metric space has these properties, and conversely, if (X, d) is complete and satisfies (1) or (2), then it is a path metric space.
  *Proof:* Iteratively constructs a dense sequence of dyadic approximate midpoints using the distance property, which extend to a continuous length-minimizing curve by completeness.
- **Hopf—Rinow theorem.** If (X, d) is a complete, locally compact path metric space, then 1. Closed balls are com,pact, or, equivalently, each hounded, closed domain is compact. 2. Each pair of points can he joined hy a minimizing geodesic.
  *Proof:* First proves that closed balls are compact by contradiction, extracting a convergent subsequence via a diagonal argument. Then extracts a length-minimizing geodesic by applying Ascoli's theorem to arc-length parameterized curves and using the lower semicontinuity of length.
- **Lemma:** / / {X, d) is a compact path metric space and a, 6 € X, then there exists a curve of length d{a^ b) joining a and b.
  *Proof:* Parameterizes approximate paths by arc length and extracts a uniformly convergent sequence via Ascoli's theorem to find a minimizer.