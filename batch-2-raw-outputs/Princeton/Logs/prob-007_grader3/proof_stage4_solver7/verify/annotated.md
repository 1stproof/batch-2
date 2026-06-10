**Annotated Proof**

**Step 1: Euler contour walks of planar trees**
*Claim:* The topological boundary of a tree component's regular complement neighborhood strictly traces an Euler perimeter tour.
*Citation:* [CONFIDENT] Lando, S. K. and Zvonkin, A. K., Graphs on Surfaces and Their Applications, Chapter 1, "because ribbon graph faces canonically form Eulerian boundary walks cyclically visiting the immersed tree's leaves"

**Step 2: Degree constraints on planar forests**
*Claim:* Internal arc crossings act strictly as degree-4 vertices, inherently increasing a component's leaf count to at least 4.
*Citation:* [APPROX] Diestel, R., Graph Theory, Chapter 1, "because standard degree-sum formulas (the handshaking lemma) algebraically link internal degree-4 crossings to boundary leaves"

**Step 3: Exhaustive enumeration of core cells**
*Claim:* The configuration space of the 6 core endpoints is completely enumerated by crossing subsets.
*Citation:* [APPROX] Chmutov, S., Duzhin, S. and Mostovoy, J., Introduction to Vassiliev Knot Invariants, Chapter 3, "because degree-3 chord diagrams exhaustively classify the 15 possible matchings on 6 points by crossing counts"

**Step 4: Exclusion of internal intersection regions**
*Claim:* Multiple crossed intervals bounding an internal central region force an empty boundary ($\partial A = \emptyset$), which is forbidden.
*Citation:* [CONFIDENT] Farb, B. and Margalit, D., A Primer on Mapping Class Groups, Section 1.2, "because the Bigon Criterion mathematically forbids non-minimally intersecting transverse arcs from lacking boundary vertices"

**Step 5: Euler-Poincaré homology relation**
*Claim:* The Euler-Poincaré relation dictates $b_2 \ge 1$ from the Euler characteristic $\chi=2$ and $b_0=1$.
*Citation:* [CONFIDENT] Hatcher, A., Algebraic Topology, Section 2.2 (Theorem 2.44), "because finite, finite-dimensional CW complexes structurally obey the Euler-Poincaré formula equating alternating cell and Betti sums"

**Coverage Summary**
- Steps confidently cited: 3
- Steps approximately cited: 2
- Steps unable to locate: 0

**Notes**
- The algebraic step solving $2 = 1 - b_1 + b_2 \implies b_2 = 1 + b_1$ to show $b_2 \ge 1$ relies simply on the fact that Betti numbers are non-negative ranks of homology groups; it is considered routine and left unannotated.