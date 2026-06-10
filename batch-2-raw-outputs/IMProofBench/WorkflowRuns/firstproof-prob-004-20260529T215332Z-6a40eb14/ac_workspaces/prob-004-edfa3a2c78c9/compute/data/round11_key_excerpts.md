# thesis

## p. 22
The next simplest case of Problem 1 is to estimate the 2-dilation of diffeomor-
phisms between 4-dimensional rectangles. We will construct a variety of non-linear
diffeomorphisms with small 2-dilation, generalizing the snake map in various ways.
The results of Theorems 1.6 through 1.9 imply a variety of lower bounds for the
2-dilation of any diffeomorphism. Nevertheless, these results are far from solving
Problem 1 up to a constant factor. I do not even have a guess of what the right
answer might be. As a very partial result, we will solve the problem in the special
case that R is the unit cube.

Theorem 1.11. If there is a 2-contracting diffeomorphismfrom the unit 4-cube to
S, then S2S3S42< C. On the other hand, if S 2S3S42< c, then there is a 2-contracting
diffeomorphismfrom the unit 4-cube to S.

   In the last chapter of the thesis, we pursue a connection between area-contracting
maps and the topology of 3-manifolds. The bridge connecting these topics is the
following result.

Theorem 1.12. Let X be a 3-dimensionalsimplicial complex. We give X a metric by
putting the standard metric on each simplex. Let M be a completehyperbolicmanifold
(of any dimension). Then any continuous map f from X to M can be homotoped to a
map f with 2-dilation bounded by C.

   In the 1970's, Thurston invented a simplex-straightening argument which shows
that f can be homotoped to a map that has bounded 2-dilation on each 2-simplex
and bounded 3-dilation on each 3-simplex. We prove our theorem by adding an
additional argument to Thurston's, which allows us to bound the 2-dilation on each
3-simplex. Although we have made only a small, technical improvement I found the
proof surprisingly difficult.
   Given this theorem, we can apply geometrical estimates for 2-dilation to bound
the homotopy invariants of arbitrary smooth maps to hyperbolic manifolds. By this
method, we will prove two topological theorems.
   The first theorem concerns estimates for a generalization of the Hopf invariant.
Recall that if ac is a 2-form on S2 with integral 1, then the Hopf invariant of a map

                                         22

## p. 139
Chapter 8

Partial Results On 2-Contracting
Diffeomorphisms Between
4-Dimensional Rectangles

In Chapter 2, we estimated the smallest (n-1)-dilation of all diffeomorphisms between
n-dimensional rectangles R and S, up to a constant factor. The next simplest case
is to consider the 2-dilation of diffeomorphisms between 4-dimensional rectangles. In
this case, I am not able to give a complete solution. In this chapter, we will give
some partial results. In the first part we prove some lower bounds for the 2-dilation.
In the second part, we construct a variety of non-linear diffeomorphisms with small
2-dilation, generalizing the snake map.

   These partial results show that the case of 2-contracting diffeomorphisms between
4-dimensional rectangles is more complicated in some ways than the case of (n-1)-
contracting maps. We'll say more about this point at the end of the chapter. Also,
the partial results allow us to solve the problem in the special case that R is a cube.


Theorem 8.1. If there is a 2-contracting diffeomorphismfrom the unit 4-cube to S
then S2S3S42< C. On the other hand, if S 2S3S42< c, then there is a 2-contracting
diffeomorphismfrom the unit 4-cube to S.

                                          139

## p. 140
8.1        Lower bounds for the 2-dilation
A. Embedding inequalities
    A 2-contracting diffeomorphism from R to S is a special case of a 2-expanding
embedding of S into R. We solved the k-expanding embedding problem in Chapter
6. In particular, there is a 2-expanding embedding of S into R roughly if and only if
the following inequalities hold.
   A1.R 1R 2 > S1S2.
   A2.R 1 R 2 R 3 > S1S2S3.
   A3.R2R 2 R3 > S2S2S3.
   A4.R 1 R2 R 3 R 4 > S1S2S3S4.
   A5.R13R 2R 3 R 4 > S1S2S3S4.

B. Boundary inequalities
   A 2-contracting diffeomorphism from R to S restricts to a 2-contracting diffeo-
morphism from the boundary of R to the boundary of S. These two boundaries are
bilipshitz to ellipsoids. We will now solve the problem of deciding whether there is a
2-contracting diffeomorphism between two ellipsoids up to a constant factor.

Proposition 8.1.1. Let E be the ellipsoid with principal axes R1 < R2 < R3 < R4 ,
and let F be the ellipsoid with principal axes S1 < S2 < S3 < S 4 . There is a 2-
contracting diffeomorphismfrom E to F approximatelyif and only if the following
inequalities hold.
   B1. R 2 R 3 > S 2S 3 .
   B2. R2R 3 R 4 > S22S3S4.
   Ba. If R > S 2S3 , then R2 R3R 4 > S2/2 S33/2S
                                                4.

   B3b. If R 2 < S 2 S3, then R 3 R4 > S 3 S4 .

Proof. Inequalities B1 and B2 are quite similar to results we have proven about 3-
dimensional rectangles.
   The 2-width of the ellipsoid E is roughly R 2 R3. It is not any bigger, because the
function   4   has level sets with volume less than CR 2 R 3. It is not smaller, because

                                             140

## p. 141
it contains a set quasi-isometric to the rectangle R2 x R3 x R4 which has 2-width
greater than cR2 R3. If there is a 2-contracting diffeomorphismfrom E to F, then the
2-width of E is at least as big as the 2-width of F. This proves inequality B1.
   The ellipsoid F contains N disjoint subsets each quasi-isometric to a cube with
side length S2, where N is at least cS 3 S 4/S22. The inverse image of each of these
subsets in E has 2-width at least cS 2 . According to the width-volume inequality for
subsets of ellipsoids, the volume of each of these inverse images is at least cR-2 S24. (In
Chapter 3 we proved a width-volume inequality for subsets of rectangles. In section
5.1, we used a simple trick to show that the same inequality holds for subsets of
ellipsoids.) It follows that the total volume of the inverse images of all the cubes is
at least cR- 1S 2S 3 S4 . Since these inverse images are disjoint subsets of E, their total
volume is bounded by CR2 R 3 R 4 . This proves inequality B2.
   The ellipsoid F also contains a subset quasi-isometric to the product of a rectangle
with dimensions S3 x S4 with a circle of length S2. We are going to estimate the volume
of the inverse image of this set. We view the set as a family of circles. The transverse
area to this family of circles increases under inverse image, since our diffeomorphism
is 2-contracting.

   We will use the isoperimetric inequality to estimate the length of the inverse image
of each circle. We restrict our attention to the circles which go through the central
sub-rectangle of S3 x S4 with dimensions 1/3S3 x 1/3S4 . Each of these circles has
filling area greater than cS 2 S3 . Therefore, the inverse image of each circle in E has
filling area greater than cS 2 S3 .
   We will estimate the length of the inverse image using the isoperimetric inequality
in E. If c is a curve in E of length L < cR2, then it sits inside of a ball that is
bilipshitz to Euclidean. Therefore it has filling area less than CL2 . If R' > S2S3,
then the inverse image of each circle has filling area greater than c(S 2S 3 ). Therefore
the inverse image of each circle must have length at least c(S 2S3 )1/ 2.        Since the
transverse area measure increases, the inverse image of our solid torus has volume at
least CS /2S3/2S 4 . Since this inverse image is a subset of E, its volume is bounded by
CR 2R 3 R 4 . This proves inequality B3a.

                                            141

## p. 142
On the other hand, if R2 < S2 S 3 , then the inverse image of each circle must have
length at least cR2 . As we saw above, if the length is less than cR2, then the filling
area is less than CL2 < R2 < S2 S3 . Therefore, the inverse image of the solid torus
must have volume at least cR 2S3 S4 . Since this inverse image is a subset of U, it
follows that R 3 R4 > cS3 S4 . This proves inequality B3b.
    This concludes the proof of the necessity of inequalities B1, B2, and B3. Next,
if these inequalities hold, we construct a diffeomorphism from E to F with 2-dilation
bounded by C.
    Case a.       > S2S3.
    Let G be the ellipsoid with principal axes ((SS23)1/2, (S2S3)1/2, S2 1/2S3/24).   There
is a diffeomorphism from G to F with 2-dilation less than C. Removing a line from G
                                                                                 2 X
and expanding the metric we get the rectangle with dimensions S21/2S31/2X S21/2S31/

S-1/23/2S4.      The volume of this rectangle is S5/2533/254.By inequality 3A., this is
less than the volume of E. Also, by the assumption R22> S2 S3 , the rectangle is thin
compared to E, and it admits an expanding embedding into E. The inverse map of
this embedding is a 2-contracting diffeomorphism from a subset of E to the comple-
ment of a line in G. We extend this diffeomorphism by mapping the rest of E to (a
tiny neighborhood of) this line. Since the line is 1-dimensional, this map can be made
2-contracting.
   Case b. R2 < S2 S3 .
   In this case, we have the following three inequalities: R2 R3 > S2S3, 22R3 R4 >
S2S 3 S4 , and R 3 R4   > S3S4 . According to Theorem 2.1, there is a diffeomorphism
from the rectangle R 2 x R3 x R4 to the rectangles S2 x S3 x S4 with 2-dilation less
than C. The double of this diffeomorphism is a diffeomorphism from E to F, with
2-dilation less than C.                                                                  O

   Finally, we notice that inequality B3 gives the upper bound that we need for
Theorem 8.1. Suppose that there is a 2-contracting diffeomorphism from the unit
cube to S. We know from inequality B1 that 1 > cS2 S3 . Therefore, when we apply
                                                                                   4.
inequality B3, we are in the first case. The inequality tells us that 1 > cS21/2S33/2S
Therefore, S 2 S3542< C.

                                            142

## p. 143
C. Other inequalities
    In Chapter 7, using rational homotopy invariants, we proved two more inequalities
about 2-contracting diffeomorphisms. If there is a 2-contracting diffeomorphism from
R to S, then we proved that R1R2 R2R4 > cS1S2S32S4, and R1R2R2R4 > cSlS2               S 4.
The second of these inequalities follows from the inequalities in parts A. and B., but
the inequality R 1 R 2 R2R 4 > cS 1 S2 S32S4 does not.
   The proof of this last inequality is based on the linear isoperimetric inequality. We
might expect to get sharper information by using the exact isoperimetric inequality,
and not only its linearization. Inequality B3 above follows from this line of thinking.
Ideally, I would like to know the isoperimetric profile function Ik(A) which is defined
to be the largest filling (k+1)-volume of any relative k-cycle in the rectangle R. (There
are a number of variations of this function: one can study real cycles or integral cycles,
oriented cycles or non-oriented cycles, relative cycles or absolute cycles, and so on.)
While I am not able to compute this function, even up to a constant factor, we will
prove an isoperimetric estimate that gives some more information than the linear
isoperimetric inequality from Chapter 7.

Proposition 8.1.2. Let C be an oriented relative2-cycle in the rectangleR with area
less than (1/2)R1 R 2. Then C has an oriented filling with volume less than CR1R22.

Proof. We are going to construct this filling C by the same method that we used in
Chapter 7. First we approximate C by a rectilinear cycle C'. (Recall that a rectilinear
cycle is made up of polyhedra each of which is a rectangle parallel to the coordinate
axes.) If C' is sufficiently close, we can construct a 3-chain with boundary C - C'
and with arbitrarily small volume. Therefore, it suffices to find a filling of C' with
volume less than CR 1 R.      If the approximation is sufficiently close, we can assume
that the projection of C' to the (l 1, x2)-plane has area at most (2/3)R1 R 2.
   Now we consider the filling Fp(C') defined in section 7.4. For a random point
p, the average volume of this filling is less than C area(C')R 3 , which is less than
CR 1R 2 R3 . Now let S be the subset of [0, R1] x [0, R 2] disjoint from the projection of
C'. Because the area of C is less than (1/2)R 1 R 2, we can assume that the area of S is

                                             143

## p. 144
at least (1/3)R 1 R 2. For a random point p in S x [0, R 3 ], the average volume of Fp(C')
is less than C area(C')R 2 . In particular, we can choose p so that the volume of Fp(C')
is less than CR 1R.    (The reason for this better estimate is as follows. The definition
of Fp(A) for a 2-face A in C' depends on whether (P1,P2) lies in the projection of A
onto [0, R1] x [0, R 2]. If it does, the volume of Fp(A) can be very large, and if we
know it doesn't, we get a better estimate for the volume of Fp(A).)                        O

   Using this isoperimetric inequality, we can prove another estimate about the 2-
dilation of diffeomorphisms.

Proposition 8.1.3. Suppose there is a 2-contractingdiffeomorphismfrom R to S. If
CR1 R2 < S1S 2 S3 , then R 3 R 4 > cS3S4.

Proof. For each pair (y3, y4) in [0, S3] x [0, S4], we consider the plane [0, SI] x [0, S2] x
{y3} x {y4 }. This plane is a relative 2-cycle in S. If we choose (y3, y4) in the central
sub-rectangle [(1/3)S3, (2/3)S3] x [(1/3)S 4 , (2/3)S4], then the filling volume of this
cycle is at least cS1S2S3.
   We consider the inverse image of one of these 2-cycles in R. It must also have
filling volume at least cS1S 2 S3 , which is greater than CR1R 2. According to the last
proposition, the 2-cycle itself must therefore have area at least cRlR 2.
   Let U be the inverse image of [0, S1]x [0, S2]x [(1/3)S3, (2/3)S3 ] x [(1/3)S4, (2/3)S4 ].
This set is fibered by the inverse image of the 2-cycles above, each of which has area
at least cR 1R 2 . The area transverse to these fibers in U is larger than in the cor-
responding region of S, because our diffeomorphism is 2-contracting. Therefore, the
volume of U is at least c(RIR 2 )(S3S 4 ). Since U is a subset of R, its volume is less
than R1R2R3 R4. Therefore, R 3 R 4 > cS 3S 4 .                                             El


8.2      Variations of the snake map
In this section, we will describe five non-linear maps between 4-dimensional rectangles,
generalizing the snake map in various ways. Each map takes the boundary of the
domain to the boundary of the range, has degree 1, and has 2-dilation less than C. By

                                            144

## p. 145
slightly perturbing them, it is possible to construct diffeomorphisms with 2-dilation
less than C.
    1. Snake Map
    This degree 1 map takes
    R1 x R 2 x R3 x R 4
    onto
    R1 x R2 x      -1R3 x AR 4 .
    The constant A is allowed to take any value between 1 and R 3 /R 2.
    Construction:
    Let I be a quasi-isometric embedding of A-1R3 x AR4 into R 3 x R 4. Let the set
U C R be the union of {O} x {O} x R3 x R4 with R1 x R 2 x image(I).
    Step 1. There is a Lipshitz retraction of R onto U. (This uses the fact that
R 2 < A-1R 3 .)

    Step 2. There is a 2-contracting retraction of U onto R 1 x R 2 x image(I).
    Step 3. There is a quasi-isometric diffeomorphism from R1 x R 2 x image(I) onto
R1 x R 2 x A-1R3 x AR 4.
    2. Codimension 1 Snake Map
    This degree 1 map takes
    R1 x R 2 x R3 x R4
    onto
    R1 x A-1R 2 x AR 3 x A-1R4 .

    The constant A is allowed to take any value which is bigger than 1, smaller than
(R 4 /R 3 )1 / 2 , and smaller than (R 2 /R 1).
    Construction:
    In section 2.1, we constructed a snake map S, which gives a 2-contracting dif-
feomorphism from R 1 x R 2 x R3 to R 1 x A-1R2 x AR3.        (The constant A must be
at least 1 and at most R 2 /R 1 , which we have already assumed.) The Lipshitz con-
stant of S is at most A. Therefore, the map F(xl, x2, x3, X4) = (S(X1,x 2, x 3), A-1x 4)
is also 2-contracting.     The map F is a diffeomorphism from R 1 x R2 x R3 x R4 to
R1 x A-IR 2 x AR3 x A-1R4 .

                                                  145

## p. 146
3. A map that stretches the short side of the domain
    This degree 1 map takes
    R1 x R2 x R3 X R4
    onto
    AR1 x A-3R 2 x AR3 x         - 1 R4 .
    The constant A is allowed to take any value which is at least 1, smaller than
(R2/R 1 )1 /4 , and smaller than (R 4 /R 3)1 / 2 .
    Construction:
   Let I be a quasi-isometric embedding of A-2R 2 x A2 R 3 x R 4 into R2 x R 3 x R4 .
Let U be the union of R1 x image(I) with {O} x R2 x R3 x R4.
   Step 1. There is a Lipshitz retraction of R onto U.
   Step 2. There is a retraction of U onto R1 x image(I), which has 2-dilation
bounded by A2 . Moreover, at any point of U, either this map is 2-contracting, or else
the derivative of the retraction maps into the 3-plane spanned by a0/x   2, 0/9x 3, and

O/3x4.
   Step 3. There is a quasi-isometric mapping from R1 x image(I) to R1 x A-2R 2 x
A2 R 3 x R4 , which preserves the coordinate xl.
   Step 4. Compose with the linear map from R1 x A-2R2 x A2 R3 x R 4 to AR1 x
A-3R2 x AR 3 x A- 1R 4. This linear map is 2-contracting. Moreover, its restriction to
the 3-plane xl = 0 has 2-dilation A-2. Therefore, the composition of all four maps is
2-contracting.
   Technical remark: If we take I to be a quasi-isometric embedding of A-2R 2 x
AR3 x AR4 into R 2 x R 3 x R4, then the same argument gives us a map from R to
AR1 x A- 3 R 2 x R3      R4. By an argument interpolating between these cases, we get
a map to AR1 x A-3R2 x A x B, where A4 < (R 2 /R 1 ), R3 < A < (R3 R4 )1 / 2 and
R3 R4 = AB.
   4. Pinching Map
   This degree 1 map takes
   R1 x R2 x R 3 x R4
   onto

                                                 146


                                                 -     ---                                I

## p. 147
AxAxAxB,
   for any numbers A and B satisfying the following conditions.
   1. R 1 >A.

   2. R 2 R 3 R4 > A 2 B.
   Construction:
   Let I be a quasi-isometric embedding of A x A x B into R 2 x R 3 x R 4 . The
conditions above guarantee that such an embedding exists.
   Let U be the union of A x image(I) with {O} x R 2 x R 3 x R 4.
   Step 1. There is a Lipshitz retraction of R onto U.
   Step 2. There is a retraction of U onto A x image(I). This retraction has no
bound on its 2-dilation, but it does have the following good property. For each point
in U, either the retraction is 2-contracting or else that point is mapped into the plane
x1 = 0 and its tangent space is mapped into the tangent space of that plane.
   Step 3. There is a quasi-isometric map from A x image(I) to A x A x A x B,
which preserves the coordinate xl.
   Step 4. There is a degree 1 Lipshitz pinch map from this rectangle onto itself,
whose restriction to the plane xl = 0 is p(O, x2, x3,
                                                  X4 ) = (0, 0, 0, x4 ).

   This pinching maps collapses all of the region with large 2-dilation to the line
Xl =   2 =   3 =   0. Since this line is one-dimensional, the 2-dilation of the composition
is less than C everywhere.

   This pinching map provides the non-linear diffeomorphism that we need to prove
Theorem 8.1. Let A be equal to S1/2 S3/2, and let B be equal to S2' 12 S/ 2 S4 . There
is a 2-contracting linear diffeomorphism from A x A x A x B to S. There is a 2-
contracting pinching map from the unit cube to A provided that 1 > CA 2 = CS2 S 3 ,
and that 1 > CA2 B = CS/ 2 S 3/2 S 4. Since the second inequality implies the first
inequality, there is a 2-contracting diffeomorphism from the unit cube to S whenever
S 2 533 4 < C. This finishes the proof of Theorem 8.1.

   5. Double Pinching Map
   This degree 1 map takes
   R1 x R 2 x R 3 x R4

                                             147

## p. 148
onto
    R1/A x A x A x B,
    for any numbers A and B satisfying the following conditions.
    1. R 1 < A.

    2. A 2 < R 2 R3 .
    3. A 3 B < R 1 R2 R3 R4 .
    Construction:
    Let I be a quasi-isometric embedding of R 1 x A 2 /R 1 x AB/R 1 into R 2a x R 3 x R4 .
The conditions 1, 2, and 3 above guarantee that such an embedding exists.
    Let U be the union of R 1 x image(I) with {O} x R 2 x R 3 x R4 .
    Step 1. There is a Lipshitz retraction of R onto U.
    Step 2. There is a retraction of U onto R 1 x image(I). This retraction has no
bound on its 2-dilation, but it does have the following good property. For each point
in U, either the retraction is 2-contracting or else that point is mapped into the plane
xl = 0 and its tangent space is mapped into the tangent space of that plane.
    Step 3. There is a quasi-isometric diffeomorphism from R 1 x image(I) to R 1 x
R1 x A 2 /R 1 x AB/R 1, which preserves the coordinate              xl.
    Step 4. There is a degree 1 Lipshitz pinch map from this rectangle onto itself,
whose restriction to the plane xl = 0 is p(O, x 2, x 3 , x4 ) = (0, 0, x 3, x 4 ).
    Step 5. Compose with the linear map 2-contracting map from this rectangle to
R2/A x A x A x B. This map preserves the 2-plane x1 = 0, x 2 = 0.
    Step 6. There is a Lipshitz pinch map p from this rectangle to itself, whose
restriction to the 2-plane x1 = 0, x 2 = 0 is given by p(O, 0, x 3 , x 4 ) = (0, 0, 0, x 4).
   The composition of all of these maps is a degree 1 map from R 1 x R 2 x R 3 x R4
to R2/A x A x A x B, with 2-dilation less than C.
   Final Remarks
   In the first part of this chapter, we gave lower bounds for the 2-dilation of dif-
feomorphisms from R to S. Let L(R, S) be the lower bound for the 2-dilation of any
diffeomorphism from R to S which we proved in section 1. In the second section of
this chapter, we constructed several non-linear diffeomorphisms with small 2-dilation.

                                               148


                                                            _·
                                                                 ----

## p. 149
Let U(R, S) be the smallest 2-dilation of any diffeomorphism from R to S that we
constructed (including the composition of the diffeomorphisms we constructed with
one another or with linear maps). It turns out that U(R, S)/L(R, S) can be arbitrar-
ily large. To be frank, I think that the techniques in this thesis are not even close to
estimating the best 2-dilation of diffeomorphisms between 4-dimensional rectangles.
    The partial results in this chapter do show that this problem is more complicated
in certain ways than the problem of estimating the best (n-1)-dilation between n-
dimensional rectangles.    We recall from Chapter 2 that, up to a constant factor,
this best (n-1)-dilation is equal to the maximum value of a list of monomials in the
variables Qi = Si/Ri.
    Our upper and lower bounds show that the best 2-dilation of diffeomorphisms
from R to S cannot be determined, even up to a constant factor, by the quotients
Qi = Si/Ri. We need to look at the actual side lengths Ri and Si, not just the
quotients Si/R   in order to calculate the smallest 2-dilation of any diffeomorphism
from R to S. (In contrast, we proved in Chapter 6 that if we want to know whether
there is a k-expanding embedding of S into R, then up to a constant factor, we only
need to look at the quotients Qi.)
   Now we describe another way that the 2-dilation problem is more complicated
than the (n-1)-dilation problem. Let Pi = logR, let i = logSi, and let Dk,,(p, oa)be
the logarithm of the best k-dilation of any diffeomorphism from R to S. The func-
tion D,,_-, is roughly equal to the maximum of a list of linear functions. Therefore,
it is approximately equal to a concave function. The function D 2 ,4 is not even ap-
proximately a concave function. We can find two points with D 2,4 less than 0, and
with D2 ,4 taking arbitrarily large values on the line between these points. This fact
has the following geometrical interpretation. There are several different strategies for
constructing a 2-contracting diffeomorphism between 4-dimensional rectangles. Us-
ing two different strategies, we can show that D 2 ,4 is less than zero at two different
points. The fact that D2 ,4 takes arbitrarily large values on the line between these
points shows that there is no way to "interpolate" between these two strategies.


                                          149

## p. 130
... <    , for any number         less than R 1. Therefore, using the estimates for rational
homotopy invariants in the last section and the proposition above, we can prove
inequalities for the k-dilation of diffeomorphisms between rectangles.
    As far as I can see, the complete list of inequalities that can be proved in this way
is a combinatorial mess. I don't know how to write the list in closed form. Therefore,
let me instead record the inequalities that we can prove for small values of k and n.
We assume throughout that there is a k-contracting diffeomorphism from R to S.
                                 The three-dimensional case
   k=2
   We get one inequality by looking at the double.
   R 1 R2R 3 > CS1 S22S3 -
                                 The four-dimensional case
   k=2
   By looking at the boundary we get one inequality.
   R 2 R32R 4 > cS 2 S32S4.

   By looking at the double, we get two more inequalities.
   R 1 R 2R3R4 > CSlS2 S32S4 .
   R 1R32RR    4   > CS 1S22S32S4 .

   k=3
   We get no inequalities.
                                 The five-dimensional case
   k=2
   By looking at the boundary, we get two inequalities.
   R 2 R 3 R4R 5 > cS2 S3 S42S5.
   R 2 R32R42R
            5 > CS2 S32S42S
                         5.

   By looking at the double we get four more inequalities.
   R 1 R 2 R2R4 R 5 > cSlS 2 S32S4S 5.
   R 1 R 2 R 3 R4R 5 > cS1 S2 S3 S42S5 .
   R 1R 2 R3R4R 5 > CS1S2 SS42S5 .
   R 1 R2RRR2
         RR2R~4R5> CS2S2S2
                   CSlS2S34S5.
                            5

                                              130


                                                                          __

## p. 191
Appendix B

Literature on Area-Contracting
Maps

In this appendix, we will survey all of the results that I know in the mathematical
literature which relate to area-contracting maps. I would be very interested to learn
of more. One goal of this appendix is to give some context for the results in the thesis.
    All of the results we have mentioned in the thesis come from remarks in two papers
by Gromov.
    In appendix 1 of the paper "Filling Riemannian Manifolds" [12], Gromov discusses
the k-width. Using Almgren's Morse theory (see B below), he gives the sharp value
for the k-width of the unit n-sphere, and also estimates the k-width of (M, g) in terms
of sectional curvature and injectivity radius. Then he gives his elementary estimate
for the k-width of the unit sphere, by repeatedly using the isoperimetric inequality.
(We repeat this argument in Proposition 3.1.1.) This argument shows in particular
that the unit ball in the n-dimensional space 1C(n) has k-width at least c(n). Gromov
raised the problem whether c(n) is bounded below as n goes to infinity (for a fixed k).
Such a bound would imply that every closed Riemannian k-manifold with the volume
of every 1-ball less than   (k) has filling radius less than 1. (I believe this problem is
still open.)
    There is a scattered discussion of k-dilation in the long essay "Carnot-Caratheodory
spaces as seen from within" [10]. This essay is mostly about generalizations of

                                           191

## p. 201
Appendix C

Open Questions

Since so little is known about area-contracting maps, there are naturally many open
questions. I have picked out four questions that seem important to me.
   1. The sponge problem
   If U is an open set in R" with very small volume, say less than e(n), then is there
a 1-expanding embedding of U into the unit ball?
   The width-volume inequality gives a very weak result in this direction. With a
very small extra effort, the width-volume inequality shows that for each k there is
a k-expanding embedding of U into Bk x Rn-Ck, where Bk denotes the unit ball in
1Rk. The sponge conjecture asks for an embedding obeying a stronger condition into
a smaller region.
   This question is related to estimates for the Lipshitz constant of a diffeomorphism
from the unit n-sphere to (Sn, g). Suppose that the target sphere contains disjoint
metric balls B(xi, Ri). Then any diffeomorphismfrom the unit n-sphere to the tar-
get sphere must have Lipshitz constant at least c('      Rin)/n. Let L be largest lower
bound obtained from this estimate after considering all sets of disjoint balls in (Sn, g).
Then is there a diffeomorphism from the unit sphere to the target sphere with Lip-
shitz constant less than CL? An affirmative answer to this question would imply an
affirmative answer to the sponge problem, as well as other corollaries.
   2. The extension problem for k-contracting maps
   Given a map F from the unit sphere in R to RN with k-dilation 1, can F be

                                           201

## p. 203
(We can also consider degree 1 maps in place of diffeomorphisms.)
     I have proven a weak result in this direction, [16]. In 3-dimensional space, if there
is a 2-contracting diffeomorphism from U to the unit ball, then there is a degree 1
map from the boundary of U to the unit sphere with Lipshitz constant less than 400.
     What if there is a k-contracting diffeomorphism from U to some rectangle R?
     b. The extension problem can be seen as a kind of isoperimetric inequality. Sup-
pose that there is a k-contracting diffeomorphismfrom the unit sphere to the bound-
ary of U. Is there a diffeomorphism from the unit ball to U with k-dilation less than
C?

     c. In Chapter 4, we proved that the boundary of U contains disjoint sets Si, so
that the volume of U is less than C E (n-2)-width)(Si) n /n- 2 . Suppose that U contains
disjoint sets Ui with Ek-width(Ui)     q greater   than 1. What can we conclude about
the boundary of U? Suppose that U has k-width at least 1 around some simplicial
complex X. (The k-width of an open set around a complex is defined in Chapter 6.)
What can we conclude about the boundary of U?
     d. Suppose that there is a k-contracting map from (U, AU) to a wedge of spheres X
with a large rational homotopy invariant. What can we conclude about the boundary
of U?
     We wish to compare the size of an n-dimensional object to the size of an (n-1)-
dimensional object. If the objects had the same dimension, then it would be possible
to compare them more "directly", for instance, by mapping one onto the other. If
U were a bounded open subset of Hilbert space, then the boundary of U would also
be infinite dimensional, and we could ask if there is a distance-expanding map from
U into its own boundary. In finite dimensions this is impossible. Still, we can ask
for some geometric control of a map from U into its boundary, as in the following
question.
     e. Let V(U) denote the volume of U. Is there a map F from U to the boundary of
U so that, for each p-dimensional manifold M with p-volume V(M) in the boundary
of U, the (p+l)-volume of F-1(M) is less than CV(U) 1 /nV(M)?
     f. Can we find any Sobolev inequalities in the same spirit, bounding some size of

                                            203
# area-expanding

## p. 1
AREA-EXPANDING EMBEDDINGS OF RECTANGLES

                                                                                 LARRY GUTH
arXiv:0710.0403v1 [math.DG] 1 Oct 2007



                                                  Abstract. We estimate whether there is a k-expanding embedding from one
                                                  n-dimensional rectangle into another. Our estimates are accurate up to a
                                                  constant factor C(n).


                                            Suppose that U, V ⊂ Rn are open sets. An embedding I : V → U is called k-
                                         expanding if, for every k-dimensional surface Σ ⊂ V , the volume of I(Σ) is at least
                                         the volume of Σ. Our theorem describes when there is a k-expanding embedding
                                         from one n-dimensional rectangle into another. It is sharp up to a constant factor
                                         in each dimension.
                                         Theorem 1. For each dimension n, there is a constant c(n) > 0 so that the
                                         following holds. Let R be an n-dimensional rectangle with dimensions R1 ≤ ... ≤
                                         Rn , and let S be an n-dimensional rectangle with dimensions S1 ≤ ... ≤ Sn .
                                            If there is a k-expanding embedding from S into R, then, for all integers j, l in
                                         the ranges 0 ≤ j < k ≤ l ≤ n,
                                                                      l−j                                l−j
                                                           (R1 ...Rj ) k−j Rj+1 ...Rl ≥ c(n)(S1 ...Sj ) k−j Sj+1 ...Sl .      (∗)
                                         Theorem 2. Conversely, for each dimension n there is a constant C(n) > 0 so
                                         that the following holds. If, for all integers j, l in the ranges 0 ≤ j < k ≤ l ≤ n,
                                                                      l−j                                l−j
                                                         (R1 ...Rj ) k−j Rj+1 ...Rl ≥ C(n)(S1 ...Sj ) k−j Sj+1 ...Sl ,       (∗∗)
                                         then there is a k-expanding embedding from S into R.
                                            Note that the necessary conditions (∗) and the sufficient conditions (∗∗) are
                                         identical except that the constant c(n) is replaced by the larger constant C(n).
                                            Some special cases of Theorem 1 were proven in [3]. The main contribution of
                                         this paper is to prove Theorem 1 in the remaining harder cases. In order to put
                                         the new methods in context, we give an overview of the problem, starting with the
                                         simplest cases.
                                            Overview of area-expanding embeddings
                                            We begin by discussing the two easy cases k = n and k = 1. If k = n, then
                                         (∗) reduces to the one inequality R1 ...Rn & S1 ...Sn , which says that the volume
                                         of R is bigger than the volume of S. This one condition is suff

## p. 7
AREA-EXPANDING EMBEDDINGS OF RECTANGLES                              7

    In this example, the polyhedral complex X is a triangle. Each side of the triangle
corresponds to an oriented relative 1-chain in S. The solid line in the triangle
corresonds to the two solid curves in S, and so on.
    Complexes of cycles were introduced by Almgren in his thesis [1] on the homotopy
groups of spaces of cycles. He begins with a continuous family of cycles, but the
first step in his argument is to replace the continuous family by a complex of cycles
that approximates it. Complexes of cycles were then used by Gromov in his proof
of the Sweepout Estimate [7]. The first step in Gromov’s proof is also to replace the
continuous family by a complex of cycles approximating it. Almgren and Gromov
did not name the object that they use. The name complex of cycles comes from
[6].
   Here is an outline of the paper. In Section 1, we prove estimates for the isoperi-
metric profile of a rectangle. In Section 2, we state a generalization of Theorem 1.
In Section 3, we define complexes of cycles. In Section 4 we prove a version of the
sweepout lemma for complexes of cycles. With this lemma, we prove Theorem 1
in the easy case j = 0. In Section 5, we give some algebraic preliminaries which
reduce the general case of Theorem 1 to a slightly more special case. In Section
6, we explain the tightening construction and prove Theorem 1. This section is
the heart of the paper. In Section 7, we construct area-expanding embeddings of
rectangles, proving Theorem 2. The paper ends with two appendices. The first
appendix covers the linear algebra related to area-expanding or area-contracting
maps. The second appendix covers generalizations of our results to shapes other
than rectangles.
   Acknowledgements. This paper is a simplified version of the main result of
my thesis [5]. The proof in my thesis was very convoluted. I am grateful to my
thesis advisor, Tom Mrowka, for his support and encouragement.

                1. The isoperimetric profile of a rectangle
    Let R denote the n-dimensional rectangle [0, R1 ] × ... × [0, Rn ], where the di-
mensions are ordered so that R1 ≤ ... ≤ Rn . In this section, we estimate the
isoperimetric profile for relative integral cycles in R. Our goal is to understand the
way that the isoperimetric profile depends on the dimensions Ri .
    If z is a relative integral k-cycle in R, the filling volume of z is the smallest
                                                                k
volume of any relative (k+1)-chain y with ∂y = z. Let IR          (V ) denote the largest
filling volume of any k-dimensional relative integral cycle in R with volume at most
V.
P Remark: We use the following definition for volume. If a chain C is given by
    ci fi where ci ∈ Z and fi is a Lipschitz map from   P the standard       k-simplex to
S, then the volume of the chain C is defined to be         |ci |V ol(fi∗ Euc), where Euc
denotes the Euclidean metric on R. This quantity is also called the mass of C. We
denote the volume of C by |C|.
                                                                   k
    The following theorem estimates the isoperimetric profile IR      for the rectangle R.
Theorem 3. There are constants c(n) > 0, C(n) so that the following holds.
  If V ≤ c(n)R1 ...Rk , then write V = c(n)R1 ...Rj ρk−j for some 0 ≤ j ≤ k − 1
and some ρ in the range Rj ≤ ρ ≤ Rj+1 . (These conditions determine j and ρ
uniquely.)

## p. 10
10                                   LARRY GUTH

                   2. Statement of the main inequalities
   In the paper, we will prove an estimate which is a little more general than
Theorem 1. We now formulate it in terms of k-dilation. Recall that the k-dilation
of a smooth map Φ is defined to be kΛk dΦkL∞ . The k-dilation measures by what
factor the map Φ stretches k-dimensional areas. The k-dilation of Φ is at most Λ if
and only if Φ maps every k-dimensional surface of volume V to an image of volume
at most ΛV .
   Recall that R is an n-dimensional rectangle with dimensions R1 ≤ ... ≤ Rn and
S is an n-dimensional rectangle with dimensions S1 ≤ ... ≤ Sn . We let Qi denote
the quotient Si /Ri . We now state the main estimates of the paper.
Estimate 1. Suppose that U is an open set in R and that Φ is a map of pairs
(U, ∂U ) → (S, ∂S) of degree D > 0. Suppose that j and l lie in the ranges 0 ≤ j <
k ≤ l ≤ n. Then the k-dilation of Φ is bounded below by the following inequality.
                                                             k−j
                       dilk (Φ) ≥ c(n)Q1 ...Qj (Qj+1 ...Ql ) l−j .
   For example, if I is a k-expanding embedding from S into R, then we take U to
be the image of S, and we take Φ to be the inverse of I. The map Φ has k-dilation
at most 1, and it has degree 1, and so Estimate 1 implies Theorem 1. Estimate 1
is slightly more general because Φ need not be a diffeomorphism.
   If the degree D is large, then we can strengthen some of the lower bounds in
Estimate 1 as follows.
Estimate 2. With the same assumptions as above, for any 0 ≤ j < k, the k-dilation
of Φ is bounded below by the following inequality.
                                      k−j                          k−j
                    dilk (Φ) ≥ c(n)D n−j Q1 ...Qj (Qj+1 ...Qn ) n−j .
   In the paper [3], I proved Estimate 1 if either j = 0 or l = n. We will prove all
the cases of Estimate 1 in this paper. The proof of the case j = 0 is essentially the
same as the one in [3], but this paper gives a new proof for the case l = n.

                             3. Complexes of cycles
   We introduce some vocabulary that we will use in our proof.
   A complex of cycles in a rectangle S is a collection of chains of different dimen-
sions that fit together in a coherent way. It consists of the following data. There is
a polyhedron X which is like a parameter space for the complex. Then there is a
map C which assigns to each d-dimensional face F d of X a d-dimensional relative
chain in S. These chains have to fit together so that if the boundary of F d is equal
   PN                                                              PN
to i=1 Fid−1 , then the boundary of the chain C(F ) should be i=1 C(Fi ). In this
paper, we work with complexes of cycles over Z, and so all the faces and chains in
the above discussion are oriented.
   More formally, the map C is a chain map between two complexes. The first
complex is generated by the faces of X with integral multiplicities and the natu-
ral boundary operations. The second complex is the complex of integral relative
Lipschitz cycles in S, which we denote Irel (S).
   This definition is due to Almgren. Almgren introduced it in his paper on the
topology of the space of cycles [1]. For more explanation of the definition, see
Section 1 of [6].

## p. 11
AREA-EXPANDING EMBEDDINGS OF RECTANGLES                           11

   We remark that the complex X may have dimension bigger than n. Even if
d > n, the definition of Lipschitz d-chain in S makes sense.
   We give an example of a complex of cycles. If U ⊂ R is an open set and Φ is a
map from (U, ∂U ) to (S, ∂S), then we can define a complex of cycles by noticing
where Φ maps various chains. Let us fix a polyhedral structure P on R. For each
face F of this structure, we define CΦ (F ) to be Φ(F ∩ U ). The complex CΦ sends
each face F contained in the boundary of R to zero, and so we can say that CΦ is
parametrized by (R, ∂R).
   Since C is a chain map, it induces a map on homology from H∗ (X, Z) to
H∗ (S, ∂S, Z). In particular, if C is a complex of cycles parametrized by (R, ∂R),
then it induces a map from H∗ (R, ∂R, Z) to H∗ (S, ∂S, Z). We define the degree of
C to be the degree of this map on Hn . The degree of CΦ is the same as the degree
of Φ.
   A homotopy of complexes of cycles is a complex C parametrized by X × [0, 1]. If
the restriction of C to X ×{0} is a complex C0 and the restriction of C to X ×{1} is
C1 , then we say that C is a homotopy from C0 to C1 . If C0 and C1 are homotopic,
then the induced maps on homology H∗ (X, Z) → H∗ (S, ∂S, Z) are the same.

                            4. The sweepout lemma
   We now prove a lemma that says that if all the chains in a complex are small
enough then the complex is null-homotopic. The lemma and proof are based on an
argument of Gromov from page 134 of [7].
Lemma 4.1. There is a constant c(n) > 0 so that the following estimate holds.
   Suppose that C0 is a complex of cycles in S parametrized by X. Suppose that
for each vertex v of X, C0 (v) is equal to 0. Suppose that for each p-face F p in X,
C0 (F p ) has volume at most c(n)S1 ...Sp . Then C0 is null-homotopic.
  Lemma 4.1 is closely related to the Sweepout Estimate stated in the introduction.
Gromov used this argument to prove the sweepout estimate on page 134 of [7].
Proof. We let C1 denote the zero map. We have to prove that C0 is homotopic to
C1 by constructing a homotopy C between them. The homotopy C needs to be
defined on X × [0, 1], and it is already defined on X × {0} and on X × {1}. We
define C one skeleton at a time.
   We will prove inductively that we can extend C to the p-skeleton of X × [0, 1]
while preserving the inequality |C(F p )| ≤ c(n)S1 ...Sp for all p ≤ n. To start the
induction, we define C on the 1-skeleton by setting C(v×[0, 1]) equal to zero for each
vertex v of X. Since C0 (v) = 0 = C1 (v), this choice is allowed and it clearly obeys
our volume estimate. By induction, we may assume that we have done the extension
to the (p-1)-skeleton of X × [0, 1]. When we extend to the p-skeleton, we have to
define C(F p ) for each p-face so that ∂C(F p ) = C(∂F p ). By induction, C(∂F p ) is
a (p-1)-cycle in S with volume at most c(n)S1 ...Sp−1 . According to Theorem 3, we
can fill this cycle with volume at most c(n)S1 ...Sp−1 Sp−1 ≤ c(n)S1 ...Sp .
   Next we have to extend C to the (n+1)-skeleton of X. We have already defined
C on the n-skeleton. In particular, C(∂F n+1 ) is a relative n-cycle in S with volume
at most c(n)S1 ...Sn < S1 ...Sn . Therefore this n-cycle is exact. We define C(F n+1 )
to be any (n+1)-chain with the given boundary. Finally we extend to the higher
skeleta. There is no obstruction to finding an extension to the higher skeleta because
Hp (S, ∂S) = 0 for p ≤ n + 1.                           

## p. 12
12                                     LARRY GUTH

   (The same proof works for a complex of cycles parametrized by (R, ∂R). In this
case, we get a homotopy parametrized by (R × [0, 1], ∂R × [0, 1]).)
   Using this lemma, we can prove the easiest cases of Estimates 1 and 2. These
cases were first proven in [3], but we include them here for completeness.
Proposition 4.1. If U is an open set in R and if Φ : (U, ∂U ) → (S, ∂S) is a map
of degree D 6= 0, then the k-dilation of Φ is at least c(n)Q1 ...Qk .
Proof. By scaling, we may assume that Φ is k-contracting and it then suffices to
prove that R1 ...Rk ≥ c(n)S1 ...Sk . We assume that R1 ...Rk < c(n)S1 ...Sk and
proceed to a contradiction.
    We cut R into rectangular blocks which are each congruent to [0, R1 ] × ... ×
[0, Rk ] × [0, ǫ]n−k for some small number ǫ > 0. All the rectangular blocks are
parallel, and they form a grid of dimension 1 × ... × 1 × (Rk+1 /ǫ) × ... × (Rn /ǫ).
Now we look at the complex CΦ corresponding to this decomposition.
    If p < k, then each p-face of our decomposition lies on the boundary of R and so
is mapped to 0. Each k-face of our decomposition has volume at most R1 ...Rk . For
each k-face F k , CΦ (F k ) has volume less than c(n)S1 ...Sk , since Φ is k-contracting.
Similarly, for p > k, each p-face F p has volume at most R1 ...Rk ǫp−k . In Appendix
1, we prove that if Φ is k-contracting then it is also l-contracting for each l ≥ k.
So CΦ (F p ) has volume less than R1 ...Rk ǫp−k . If we choose ǫ small enough, then
Lemma 4.1 implies that CΦ is null-homotopic. In particular CΦ has degree zero.
But we have already seen that CΦ has degree D which we assumed non-zero. 
  Since the map Φ is also l-contracting for all l ≥ k, we get the following more
general proposition.
Proposition 4.2. If l ≥ k, if U is an open set in R, and if Φ : (U, ∂U ) → (S, ∂S)
is a map of degree D 6= 0, then the k-dilation of Φ is at least c(n)(Q1 ...Ql )k/l . Also,
the k-dilation of Φ is at least (|D|Q1 ...Qn )k/n .
Proof. By the last proposition, the l-dilation of Φ is at least c(n)Q1 ...Ql . Also, the
n-dilation of any degree D map is at least |D|Q1 ...Qn . Therefore, the k-dilation of
Φ is at least c(n)(Q1 ...Ql )k/l and at least (|D|Q1 ...Qn )k/n .                     
     Proposition 4.2 proves Estimates 1 and 2 in the case j = 0.

                            5. Algebraic preliminaries
     We rewrite the remaining cases of our estimates.
Estimate 1. (Non-trivial cases) There is a constant c(n) > 0 so that the following
holds. Let R, S be n-dimensional rectangles. Suppose U ⊂ R is an open set. Suppose
that Φ is a k-contracting map from U to S of degree D 6= 0. Suppose 0 < j < k < l.
                                                l−k
                 Then [(R1 ...Rj )/(S1 ...Sj )] k−j R1 ...Rl ≥ c(n)S1 ...Sl .         (1)
Estimate 2. (Non-trivial cases) In the same situation as above, the following in-
equality holds.
                                         n−k
                  [(R1 ...Rj )/(S1 ...Sj )] k−j R1 ...Rn ≥ c(n)|D|S1 ...Sn .          (2)

## p. 14
14                                    LARRY GUTH

   The complex C1 agrees with C0 for faces of dimension at most k. For faces
of higher dimension, C1 is different from C0 . We define C1 by induction on the
dimension.
   First we define C1 (F k+1 ). We have already defined C1 (∂F k+1 ). Each face of
∂F k+1 has k-volume at most δ(n)S1 ...Sj Sjk−j , and so C1 (∂F k+1 ) has volume at
most δ(n)2n S1 ...Sj Sjk−j . If we pick δ small enough, the isoperimetric inequality tells
us that C1 (∂F k+1 ) bounds a (k+1)-chain with volume at most δ(n)CS1 ...Sj Sjk−j+1 .
We define C1 (F k+1 ) to be a (k+1)-chain with this volume bound. We repeat this
construction for every (k+1)-face in our decomposition of R.
   Then we proceed inductively, defining C1 one skeleton at a time so that at each
stage it obeys the inequality |C1 (F p )| < δCS1 ...Sj Sjp−j . Suppose we have defined
C1 on the p-skeleton and that F p+1 is a (p+1)-face. We have already defined
C1 (∂F p+1 ) and it has volume at most δCS1 ...Sj Sjp−j . Assuming δ is sufficiently
small, we can apply the isoperimetric inequality to fill C1 (∂F p+1 ) by a (p+1)-chain
of volume at most δCS1 ...Sj Sjp+1−j . We define C1 (F p+1 ) to be this chain.
   A key point in the proof is that the new complex C1 has the same degree as the
original complex C0 .
Key Lemma. The degree of C1 is equal to the degree of Φ.
This point is the subtlest part of our argument, and so we defer the proof until the
end of the section.
     Gluing a complex of cycles
   In place of B, we now consider a coarser decomposition of the rectangle R. This
time we divide R into blocks with dimensions R1 × ... × Rl × L × ... × L. Each
new n-dimensional block is a union of N = (Rj+1 /L)...(Rl /L) blocks from the old
decomposition. More generally, each interior p-face of the new decomposition is a
union of N p-faces of the old decomposition. We let B + be the complex generated
by the interior faces of this coarser decomposition. Note that each interior face of
B + has dimension p ≥ l and dimensions R1 × ... × Rl × L × ... × L. (There are p − l
factors of L in this formula.)
   Any complex of cycles C : B → Irel (S) can easily be glued together to form a
new complex of cycles C + : B + → Irel (S). Suppose that F is a p-face of B + . As
                                                               PN
we observed above, F is a union of p-faces from B: F = i=1 Fi , where Fi is a face
                                       P  N
of B. Now we just define C + (F ) = i=1 C(Fi ). The degree of C and the degree
     +
of C are always the same.
   In particular, C1+ is the glued-together version of C1 . The volume of C1+ (F p ) is
at most C(n)δN S1 ...Sj Sjp−j . Plugging in the value of N , we see that the volume of
C1+ (F p ) is at most C(n)δRj+1 ...Rl L−l+j S1 ...Sj Sjp−j . Finally, plugging in the value
of L, we see that the volume of C1+ (F p ) is at most
                                R1 ...Rj k−j l−k
                           C(n, δ)[        ]     R1 ...Rl Sjp−l .                  (V )
                                 S1 ...Sj
   Using the volume bound (V ) and the key lemma, we can now prove estimates
(1) and (2). To prove inequality (2), we set l = n. In this case B + consists of
only one n-face, which is the whole rectangle R. According to the formula above,
                                  R ...R n−k
C1+ (R) has volume at most C(n)[ S11 ...Sjj ] k−j R1 ...Rn . On the other hand, by the

## p. 15
AREA-EXPANDING EMBEDDINGS OF RECTANGLES                             15

Key Lemma, C1+ has degree D, and so C1+ (R) must have volume at least |D|S1 ...Sn .
We conclude the following inequality.
                            n−k                              n−k
                 (R1 ...Rj ) k−j R1 ...Rn ≥ c(n)|D|(S1 ...Sj ) k−j S1 ...Sn .
   This inequality is equivalent to (2).
   Next we prove inequality (1) using Lemma 4.1. Recall that each interior face of
B + has dimension p ≥ l. Since C1+ has degree D 6= 0, Lemma 4.1 guarantees that
for some dimension p, we can find an interior face F p so that C1+ (F p ) has volume
at least c(n)S1 ...Sp . On the other hand, this same volume is bounded above by
(V ). Combining these equations, we conclude the following.
                        R1 ...Rj k−j
                                   l−k
                    C(n)[        ]     R1 ...Rl Sjp−l ≥ c(n)S1 ...Sp .
                        S1 ...Sj
  Rearranging this inequality, we get the following.
              R1 ...Rj k−j
                         l−k                          −(p−l)
              [        ]     R1 ...Rl ≥ c(n)S1 ...Sp Sj      ≥ c(n)S1 ...Sl .
              S1 ...Sj
   This proves inequality (1).
   We have now finished proving our main estimates except for the proof of the key
lemma which tells us that the degree of C1 is equal to D.
  Gradually tightening chains
Key Lemma. The degree of C1 is equal to the degree of Φ.
  To prove the lemma, we will need to construct some homotopies between chain
maps. We use the following lemma, which generalizes Lemma 4.1.
Lemma 6.1. There is a constant ǫ(n) > 0 so that the following holds. Suppose
that C0 and C1 are two chain maps X → Irel (S). Suppose that C0 and C1 agree on
the k-skeleton of X. Suppose that for each p-face F p in X of dimension p ≥ k + 1,
the volumes |C0 (F p )| and |C1 (F p )| are at most ǫ(n)S1 ...Sp . Then C0 and C1 are
homotopic.
Proof. We have to build a chain map C : X × [0, 1] → Irel (S), extending C0 and
C1 . If p ≤ k, we define C(F p × [0, 1]) to be 0.
   We will prove inductively that we can extend C to the n-skeleton of X × [0, 1]
while preserving the inequality |C(F p × [0, 1])| ≤ c(n)S1 ...Sp+1 for p ≤ n − 1.
   When we extend to the (p+1)-skeleton, we have to define C(F p × [0, 1]) for
each p-face so that ∂C(F p × [0, 1]) = C((∂F p ) × [0, 1]) + C1 (F p ) − C0 (F p ). By
induction, the right-hand side is a p-cycle in S with volume at most c(n)S1 ...Sp .
According to our isoperimetric inequality, we can fill this cycle with volume at most
c(n)S1 ...Sp Sp ≤ c(n)S1 ...Sp+1 .
   Next we extend C to the (n+1)-skeleton. We have to define C(F n × [0, 1]).
We have already defined C on ∂(F n × [0, 1]); it is an n-cycle with volume less than
S1 ...Sn . Hence it is an exact n-cycle, and we can choose a filling for it. We can then
extend to the higher-dimensional faces because Hq (S, ∂S) = 0 for all q ≥ n + 1. 
   At first we might hope to apply this lemma to build a homotopy from C0 to
C1 . (Recall that C0 and C1 agree on the k-skeleton of B.) In general, this does
not work, because the volumes |C0 (F p )| may be too large. Morally, the problem
is that in building C1 we have suddenly tightened the chains into a quite different

## p. 16
16                                       LARRY GUTH

position. To build a homotopy, we want to gradually tighten the chains so that at
each step they move only slightly. Then we can use the lemma above to build a
homotopy between the small steps.
     Proof of key lemma
   Let Bs be the division of R into rectangular blocks with dimensions R1 × ... ×
Rj × 2−s L × ... × 2−s L. The division B0 is just B, and the other Bs are finer
subdivisions of B.
   Next we define chain maps Γs : Bs → Irel (S) as follows. For each face F p in Bs
of dimension p ≤ k, we define Γs (F ) to be Φ(F ∩ U ). Then we extend Γs to faces
of dimension p ≥ k + 1 inductively, using the isoperimetric inequality for rectangles
at each step as in the construction of C1 . Because the constructions agree exactly,
we may take Γ0 to be equal to C1 .
   First we check that Γs+1 and Γs have the same degree. We let Γ+         s+1 : Bs →
Irel (S) be the glued version of Γs+1 . As in the previous gluing construction, Γ+  s+1
and Γs+1 have the same degree. We will use Lemma 6.1 to show that Γ+        s+1 and  Γs
are homotopic. By construction, they have the same restriction to the k-skeleton
of Bs . By the same argument that we used for C1 , Γs (F p ) has volume at most
δ(n)S1 ...Sj Sjp−j ≤ δ(n)S1 ...Sp . The same holds true for Γs+1 and hence for Γ+  s+1 .
Applying Lemma 6.1, we see that Γs and Γs+1 have the same degree.
   Let βs : Bs → Irel (S) be the chain map sending a face F p to Φ(F p ∩ U ) for every
p. The map βs is analogous to C0 , and so it has degree D for every s.
   If p ≥ k + 1, then the volume of βs (F p ) is at most |F p |, which is at most
R1 ...Rj Lp−j 2−p−js . Since j < k, we may choose s sufficiently large so that for each
p ≥ k + 1, this volume is at most c(n)S1 ...Sp . We now fix s to be this sufficiently
large value. The two chain maps βs and Γs agree on the k-skeleton of Bs . Because
of our choice of s, the volume of βs (F p ) is at most c(n)S1 ...Sp for each p ≥ k + 1.
We checked above that the same inequality holds for Γs . According to Lemma 6.1,
βs and Γs are homotopic and so have the same degree.
   To summarize, the degree of C1 is equal to the degree of Γ0 , which is equal to
the degree of Γs , which is equal to the degree of βs , which is equal to D.
     This concludes the proof of Estimates 1 and 2, and hence the proof of Theorem
1.

                   7. Constructing area-expanding embeddings
     In this section, we prove Theorem 2.
Theorem 2. There is a constant C(n) so that the following holds.
   Suppose that the dimensions of R and S obey the following inequalities for all
0 ≤ j < k ≤ l ≤ n.
                              l−j                              l−j
                 (R1 ...Rj ) k−j Rj+1 ...Rl ≥ C(n)(S1 ...Sj ) k−j Sj+1 ...Sl .
     Then there is a k-expanding embedding from S into R.
   We will construct our embedding by composing a k-expanding linear map and a
simple folding map analogous to the one in Figure 1.
   If R and S are 2-dimensional rectangles with R1 > 3S1 and R1 R2 > 9S1 S2 , then
there is a 1-expanding embedding of S into R. This embedding is illustrated in
Figure 1.

## p. 20
20                                    LARRY GUTH

                    9. Appendix 2: minor generalizations
   In this section, we discuss how far our results generalize to shapes that are not
rectangles.
   First we briefly consider replacing S by another shape. We note that all our
arguments depended only on knowing the isoperimetric profile of S. Therefore, our
methods should adapt to give some estimates for any target where we can estimate
the isoperimetric profile.
   Second we consider replacing R by a more general shape. Our arguments apply
to products of the form: X j ×Y l−j ×Z n−l , where X and Z may be any Riemannian
manifolds, but the middle factor Y is still a rectangle. In this case, our estimate
survives, reading as follows.
Proposition 9.1. Suppose that U is an open set in X × Y × Z, where X j and
Z n−l are Riemannian manifolds and Y l−j is a rectangle. Suppose that Φ is a k-
contracting degree non-zero map from U to an n-dimensional rectangle S. Then
the volumes of X and Y are bounded below by the following inequalities.
                           l−j                        l−j
                       |X| k−j |Y | ≥ c(n)(S1 ...Sj ) k−j Sj+1 ...Sl .
  If X and Z are oriented, l = n, and the degree of the map is large, we also get
                               n−j                           n−j
an analogue of Estimate 2: |X| k−j |Y | ≥ c(n)|D|(S1 ...Sj ) k−j Sj+1 ...Sn .
Proof. (sketch) Use the argument of the paper, cutting the domain into pieces each
a product of the form X times a cube in Y with side-length L times a tiny simplex in
Z. If the domain is not orientable, use mod 2 chains instead of integral chains. 
    The statement of the proposition would still make sense if we allowed the middle
factor Y to be any manifold, but the rectangular structure is used crucially in the
proof, mostly when we cut Y into cubes. I strongly believe that the estimate above
does not generalize to all Riemannian products X × Y × Z.
    The product structure can also be relaxed a little. Suppose our domain An ad-
mits a map π onto Y l−j × Z n−l , where as above Y is a rectangle and Z is any Rie-
mannian manifold. Suppose that for any p-chain C in Y ×Z, the (p+j)-dimensional
volume of π −1 (C) is at most V |C|. Suppose that U is an open set in A admitting a
k-contracting map of non-zero degree to the n-dimensional rectangle S. Then our
                                             l−j                    l−j
inequality again survives in the form V k−j |Y | ≥ c(n)(S1 ...Sj ) k−j Sj+1 ...Sl . (And
the analogue of Estimate 2 holds also.)
    For example, we can   Preplace  R by an ellipsoidal metric on the n-sphere. Define
                             n
E n by the equation             (x
                             i=0 i /E   2
                                     i ) = 1. Here E is an ellipsoid with principal
axes E0 ≤ ... ≤ En . The manifold E is C(n)-bilipschitz to the double of the
rectangle [0, E1 ] × ... × [0, En ]. So for any j ≥ 0, there is a map π from E to
[0, Ej+1 ] × ... × [0, En ] which obeys the conditions of the last paragraph with V ∼
E1 ...Ej . Applying our generalized version of Estimates 1 and 2, we get the following
corollary.
Corollary. Suppose that E and E ′ are n-dimensional ellipsoids with principal axes
E0 ≤ ... ≤ En and E0′ ≤ ... ≤ En′ , and quotients Qi = Ei′ /Ei . Suppose that Φ is a
map from E to E ′ with degree D 6= 0. Then the k-dilation of Φ is bounded below by
the following formulas. First, if 0 ≤ j < k ≤ l ≤

## p. 21
AREA-EXPANDING EMBEDDINGS OF RECTANGLES                                   21


                                                                k−j
                      dilk (Φ) ≥ c(n)Q1 ...Qj (Qj+1 ...Ql ) l−j .
  Second, if 0 ≤ j < k,
                                          k−j                         k−j
                    dilk (Φ) ≥ c(n)|D| n−j Q1 ...Qj (Qj+1 ...Qn ) n−j .

                                       References
[1] Almgren, F. J.; The homotopy groups of the integral cycle groups, Topology 1, 1962, 257-299.
[2] Federer, H., Fleming, W., Normal and integral currents, Ann. of Math. (2) 72 (1960) 458-520.
[3] Guth, L., The width-volume inequality, arXiv:math/0610212.
[4] Guth, L., Area-contracting maps between rectangles, Thesis, MIT 2005.
[5] Guth, L., Notes on Gromov’s systolic estimate, Geometriae Dedicata 123, Number 1, Dec.
    2006, 113-129.
[6] Guth, L., Minimax problems related to cup powers and Steenrod squares,
    arXiv:math/0702066
[7] Gromov, M., Filling Riemannian manifolds, J Diff. Geometry 18, 1983, no. 1, 1-147.

  Department of Mathematics, Stanford, Stanford CA, 94305 USA
  E-mail address: lguth@math.stanford.edu
# minimax

## p. 53
MINIMAX PROBLEMS RELATED TO CUP POWERS AND STEENROD SQUARES                      53

Proof. The proof is essentially the same as in Example 5 of Section 6. Let F (1, 1)
denote a family of 0-cycles in the unit 1-ball consisting of a single point that moves
from one end of the interval to the other. We can think of F (1, 1) as a family of
integral 0-cycles that detects a(0, 1, Z) and also a(0, 1, Z2 ). Take the product of
F (1, 1)s with Example 1 above.                                                     
   For many other cases, there is a big gap between the best upper and lower
bounds. The simplest example concerns 1-cycles in the unit 3-ball. Our best
lower bound for V(a(1, 3, Z)p ) is cp2/3 . The only upper bound that I know for
V(a(1, 3, Z)p ) is Cp, which we get by considering families of p vertical lines.

        9. Appendix 3: Minimax volumes of Riemannian manifolds
   Minimax volumes analogous to those we have studied can also be defined using
a Riemannian manifold (M n , g) in place of the unit n-ball.
   Let Z(k, M ) denote the space of absolute mod 2 k-cycles in M . If M has a bound-
ary, then let Zrel (k, M ) denote the space of relative mod 2 k-cycles in (M, ∂M ). The
construction of the fundamental cohomology class a(k, n) generalizes to the setting
of manifolds. If M is a closed n-manifold, then we get a fundamental cohomology
class a(k, M ) ∈ H n−k (Z(k, M )). If M is a compact n-manifold with boundary,
then we get a fundamental cohomology class a(k, M ) ∈ H n−k (Zrel (k, M )).
   If α is any cohomology class in H ∗ (Z(k, M )), then we can define a minimax
volume associated to α. We let F(α) denote the set of all families of cycles F : P →
Z(k, M ) that detect α. Then we define a minimax volume V(M,g) (α) by the usual
formula.

                          V(M,g) (α) =    inf   sup Vol(C).
                                         F ∈F(α) C∈F
We need the metric g in order to measure the volumes of k-cycles in M . For a fixed
choice of M and α, the minimax volume V(M,g) (α) is a function of g. Roughly
speaking, this function measures how large the manifold (M, g) is. If g ≥ h, then
it’s easy to check that V(M,g) (α) ≥ V(M,h) (α).
    These minimax volumes can be used to control the geometry of degree 1 maps
between Riemannian manifolds. If Φ : M → N is a Lipschitz map, then it induces
a map Zk (Φ) from Z(k, M ) to Z(k, N ) for every k. Similarly, if Φ : (M, ∂M ) →
(N, ∂N ) is a Lipschitz map of pairs, then it induces a map Zk (Φ) from Zrel (k, M )
to Zrel (k, N ). In either case, the pullback Zk (Φ)∗ [a(k, N )] = (deg Φ)a(k, M ). This
equation follows directly from the construction of a(k, M ).
    If Φ : M → N is a piecewise C 1 map, then we say that the k-dilation of Φ is
at most Λ if Φ maps each k-dimensional submanifold of M with volume V to an
image with volume at most ΛV .
Proposition 9.1. Suppose that Φ : (M, g) → (N, h) is a C 1 map with degree 1
mod 2 and k-dilation Λ. Suppose that O denotes any natural cohomology operation
with mod 2 coefficients. In particular, O may denote a cup power or any tower of
Steenrod squares. Then the following inequality holds.

                      ΛV(M,g) (Oa(k, M )) ≥ V(N,h) (Oa(k, N )).

## p. 54
54                                   LARRY GUTH

Proof. For any δ > 0, let Fδ be a family of k-cycles in M that detects Oa(k, M )
with volume at most V(M,g) (Oa(k, M )) + δ. Then Φ(Fδ ) is a family of k-cycles in
(N, h) that detects Oa(k, N ) with volume at most Λ[V(M, g)(Oa(k, M )) + δ]. 
   This proposition gives a large number of lower bounds for the k-dilation Λ of a
degree 1 map from (M, g) to (N, h). If N has a boundary, then we can formulate
a slightly more general version of this proposition.
Proposition 9.2. Suppose that (M n , g) is a compact n-manifold and that (N, h)
is a compact n-manifold with boundary. Suppose that U ⊂ M is an open set with a
piecewise smooth boundary. Suppose that Φ : (U, ∂U ) → (N, ∂N ) is a piecewise C 1
map with degree 1 mod 2 and k-dilation Λ. Let O be a cohomology operation. Then
the following inequality holds.

                      ΛV(M,g) (Oa(k, M )) ≥ V(N,h) (Oa(k, N )).
Proof. For any δ > 0, let Fδ be a family of k-cycles in M that detects Oa(k, M )
with volume at most V(M,g) (Oa(k, M )) + δ. Let F̂δ be the restriction of this family
to U . The family F̂δ detects Oa(k, U ) with volume at most V(M,g) (Oa(k, M )).
Then Φ(F̂δ ) is a family of k-cycles in (N, h) that detects Oa(k, N ) with volume at
most Λ[V(M,g) (Oa(k, M )) + δ].                                                    
   In my thesis [9], I studied the k-dilation of degree 1 maps between various sets
in Euclidean space. The main theorem of the thesis is the following.
Theorem. ([9], [10]) Suppose that R and S are n-dimensional rectangles with di-
mensions R1 ≤ ... ≤ Rn and S1 ≤ ... ≤ Sn respectively. Suppose that U ⊂ R is an
open set with a piecewise C 1 boundary and that Φ : U → S is a degree 1 piecewise
C 1 map with k-dilation Λ. Let Qi = Si /Ri . Then for each integer 0 ≤ j ≤ k and
each number k + 1 ≤ l ≤ n, the following inequality holds.
                                                          k−j
                        Λ ≥ c(n)(Q1 ...Qj )(Qj+1 ...Ql ) l−j .                     (∗)
  Conversely, for each pair of rectangles R, S, there is a set U ⊂ R and a degree 1
                                                                             k−j
map from U to S with k-dilation at most C(n) maxj,l (Q1 ...Qj )(Qj+1 ...Ql ) l−j .
   When I began the work on the material in this paper, one of my motivations was
to find a new proof of (∗). According to the last proposition, we have the following
lower bounds for Λ.

                         Λ ≥ VS (Oa(k, S))/VR (Oa(k, R)).
   Hence, if we could estimate the minimax volumes of a rectangle up to a constant
factor, we would get many lower bounds for Λ. We end with a conjecture about
the minimax volumes that would imply (∗).
                                                                Q
Conjecture. For each k + 1 ≤ l ≤ n, the minimax volume VR (Sqn−l  a(k, R)) is
equal to the following expression up to a constant factor C(n).
                                                                k−j   l−k
                    Q
              VR (Sqn−l a(k, R)) ∼ inf R1 ...Rj (Rj+1 ...Rl ) l−j 2 l−j Q .
                                    0≤j≤k

## p. 55
MINIMAX PROBLEMS RELATED TO CUP POWERS AND STEENROD SQUARES                                 55

                                          References
 [1] Almgren, F., The homotopy groups of the integral cycle groups, Topology 1, 1962, 257-299.
 [2] Almgren, F., The theory of varifolds - a variational calculus in the large for the k-dimensional
     area integrated, unpublished.
 [3] Arnold, V., Topological problems in wave propagation theory and topological economy princi-
     ple in algebraic geometry. The Arnoldfest (Toronto, ON, 1997), 39-54, Fields Inst. Commun.
     24, Amer. Math. Soc., Providence RI 1999.
 [4] Cornea, O.; Lupton, G.; Oprea, J.; and Tanre, D.; Lusternik-Schnirelmann Category, Math-
     ematical Surveys and Monographs Volume 103, American Mathematical Society, 2003.
 [5] Gromov, M., Filling Riemannian manifolds, J. Differential Geom. 18 (1983) no. 1, 1-147.
 [6] Gromov, M., Systoles and intersystolic inequalities. Actes de la Table Ronde de Geometrie
     Differentielle (Luminy, 1992) 291-362, Semin. Cong., 1, Soc. Math. France, Paris, 1996.
 [7] Gromov, M., Isoperimetry of waists and concentration of maps, Geom. Funct. Anal. 13 (2003)
     no. 1, 178-215.
 [8] Guth, L., The width-volume inequality, arxiv math/0609569, to appear in Geometric and
     Functional Analysis.
 [9] Guth, L., Area-contracting maps between rectangles, Ph. D. Thesis, MIT, 2005.
[10] Guth, L., Area-expanding embeddings of rectangles, arXiv:0710.0403.
[11] Hatcher, A., Algebraic Topology, Cambridge University Press, Cambridge, 2002.
[12] Lam, T.-K., Spaces of Real Algebraic Cycles and Homotopy Theory, Ph.D. Thesis, Univ. at
     Stonybrook, 1990.
[13] Lawson, H. B., Algebraic cycles and homotopy theory, Ann. of Math. 129, (1989), 253-291.
[14] Lawson, H. B., Cycles and spectra, Bull. Braz. Math. Soc., New Series 34(1) (2003), 77-105.
[15] Mostovoy, J., Geometry of truncated symmetric products and real roots of real polynomials,
     Bull. London Math. Soc. 30 (1998) no. 2, 159-165.
[16] Nakaoka, M., Cohomology mod p of symmetric products of spheres, J. Inst. Polytech. Osaka
     City Univ. Ser. A 9, 1958, 1-18.
[17] Pitts, J., Existence and Regularity of Minimal Surfaces on Riemannian Manifolds, Math-
     ematical Notes 27, Princeton University Press, Princeton, NJ, University of Tokyo Press,
     Tokyo, 1981.
[18] Serre, J. P., Cohomologie modulo 2 des complexes d’Eilenberg-Maclane, Comment. Math.
     Helv. 27, (1953) 198-232.

   Department of Mathematics, Stanford, Stanford CA, 94305 USA
   E-mail address: lguth@math.stanford.edu
# width-volume

## p. 3
THE WIDTH-VOLUME INEQUALITY                                3

Rn . We consider the translations of S0 by a vector x ∈ [0, 1]n . On average, the
translation of S0 meets U in a region of volume nk . Therefore, we can choose a
translate S of S0 which meets U in a controlled volume. We can then control the
k-volume of any k-cycle lying in the skeleton S.
   It is not possible to sweep out U with cycles lying in the skeleton S, because any
family of cycles sweeping out U must pass through every point of U . But it turns
out to be possible to sweep out U by a family of k-cycles each of which lies in S
except for a subset of controlled volume.
Proposition 2. For any bounded open set V ∈ Rn (of any volume), there is a
family of k-cycles sweeping out V so that each cycle lies in S, except for a subset
of volume at most C(n).
   We include some pictures to indicate how such a family might look for k = 1,
n = 2. The thin lines denote the 1-skeleton S and the thick lines denote a 1-cycle
in our family.
    1.                                  2.



    3.                                  4.



                                  Figure 1
   The general case is somewhat harder than the case k = 1, n = 2. In general,
the family of k-cycles is constructed by starting with a family of parallel k-planes
transverse to S, and then “bending” them so that almost all of the volume of each
k-plane is pushed into the skeleton S. We call this construction “bending planes
around a skeleton”.
   Area-contracting maps between rectangles
   In the second half of the paper, we apply the width-volume inequality to estimate
the k-dilations of degree 1 maps. Recall that k-dilation measures how much a
mapping stretches k-dimensional volumes. If a map f takes any k-dimensional
manifold with volume V to an image with volume at most λV , then f has k-dilation
at most λ.

## p. 4
4                                    LARRY GUTH

   The second main problem of this paper is to estimate the infimal k-dilation of all
degree 1 maps from a rectangle R to another rectangle S. This innocuous-sounding
problem has turned out to be much more complicated than I expected. When I first
approached the problem, I guessed that a linear diffeomorphism from R to S would
give at least roughly the smallest k-dilation. My guess was wrong. Let us define
Dk (R, S) to be the infimal k-dilation of any degree 1 map from R to S (taking the
boundary of R to the boundary of S). For comparison, let us define Link (R, S) to
be the smallest k-dilation of a linear diffeomorphism from R to S.
Proposition 3. For each n ≥ 3 and each k in the range 2 ≤ k ≤ n − 1, there are
pairs of n-dimensional rectangles (R, S) so that the ratio Link (R, S)/Dk (R, S) is
arbitrarily large.
   For example, if the rectangle R has dimensions ǫ × 1 × 1, and the rectangle S
has dimensions ǫ × ǫ × ǫ−1 , then Lin2 (R, S) = ǫ−1 . On the other hand, there is a
non-linear degree 1 map from R to S with 2-dilation less than 1000, regardless of
ǫ. I call this map the snake map because it somewhat resembles a snake uncoiling.
   We take a little time to describe this map. The snake map does not have any
analogue in 2 dimensions, but there is a map related to it. Let U be the unit square,
and let A ⊂ U be the shape in Figure 2.


                                      A

    U


                                  Figure 2
    The set A is bilipschitz to the rectangle [0, ǫ] × [0, ǫ−1 ], and it snakes back and
forth across U roughly ǫ−1 times. Let Ac denote the complement of A in U . The
first map that we consider is a retraction φ of U onto A, which maps Ac onto ∂A.
The 1-dilation of φ is roughly ǫ−1 and the 2-dilation of φ is exactly 1.
    We now turn to three dimensions. The rectangle R is equal to [0, ǫ] × U and
the rectangle S is bilipschitz to [0, ǫ] × A. We can get a degree 1 map from R to
S by first retracting R onto [0, ǫ] × A and then using the bilipschitz equivalence of
[0, ǫ] × A with S.

## p. 5
THE WIDTH-VOLUME INEQUALITY                                  5

   The most obvious retraction from R onto [0, ǫ] × A is id × φ, where id denotes
the identity map from [0, ǫ] to itself. This retraction has 2-dilation roughly ǫ−1 .
Using this retraction, we get a degree 1 map from R to S with 2-dilation roughly
ǫ−1 , slightly larger than the 2-dilation of the linear map.
   The trick in the construction of the snake map is to improve the retraction from
R to [0, ǫ] × A. The improved retraction takes place in two steps. We first retract
R onto the union ({0} × U ) ∪ ([0, ǫ] × A). We then retract this set onto [0, ǫ] × A.
The set ({0} × U ) ∪ ([0, ǫ] × A) resembles a snake sitting on a piece of cardboard.
The first retraction can be done with 1-dilation roughly 1, and hence 2-dilation
roughly 1 also. The second retraction is accomplished by the map id × φ. The
second retraction has 1-dilation roughly ǫ−1 but it has 2-dilation 1. To check the 2-
dilation of the retraction, we reason as follows. The restriction of id × φ to [0, ǫ] × A
is the identity, and so it has 2-dilation 1. But the complement of [0, ǫ] × A in the
domain of our map is just {0} × Ac . Our retraction maps this 2-dimensional set to
the 1-dimensional set {0} × ∂A. Therefore, the second retraction has 2-dilation 1.
   Lower bounds for the k-dilation
   Next we approach the problem from the other side, proving lower bounds for
the k-dilation Dk (R, S). Our lower bounds are based on k-width and on the width-
volume inequality. Our estimates for Dk (R, S) depend on the dimensions of R and
S. We adopt the convention that R and S are n-dimensional rectangles, that R has
dimensions R1 ≤ ... ≤ Rn and that S has dimensions S1 ≤ ... ≤ Sn .
   The first lower bound on Dk (R, S) comes from knowing the k-width of S. Sup-
pose that f is a degree 1 map from R to S with k-diliation λ. The rectangle R can
be sliced into k-dimensional rectangles with dimensions R1 × ... × Rk , and these
rectangles form a family of cycles sweeping out R. The image of each k-dimensional
rectangle has volume at most λR1 ...Rk . The situation is illustrated in Figure 3.



                                             f

               R                          Figure 3
                                                                       S
   The image of our family of rectangles is a family of k-cycles sweeping out S.
According to Proposition 1, this family must contain a cycle with volume at least
c(n)S1 ...Sk . Since each cycle in the family has volume at most λR1 ...Rk , we get a
lower bound for the k-dilation λ.
Proposition 4. Dk (R, S) > c(n)[S1 ...Sk ]/[R1 ...Rk ].
   We can get more estimates if, instead of considering the k-width of S, we work
with the k-width of subsets of S. Let’s see how this idea works out in a particular
case. Suppose that S is a 3-dimensional rectangle with dimensions S1 ≤ S2 ≤ S3 .
Then S contains many subrectangles with dimensions S1 × S2 × S2 . We can find
N disjoint rectangles in S with those dimensions, where N is roughly S3 /S2 . Call
the rectangles Vi . Each one of these rectangles has 2-width roughly S1 S2 . Now

## p. 6
6                                   LARRY GUTH

suppose that f is a degree 1 map from R to S with 2-dilation λ. Then each of our
rectangles has a preimage Ui = f −1 (Vi ), and each of these preimages has 2-width
at least S1 S2 /λ. The situation is illustrated in Figure 4.

             U1            U2
    R                                                        f
                 U3                 U4


    S         V1                V2             V3                V4

                                    Figure 4
   We want to use this information to get a lower bound on λ. Since the sets Ui
are disjoint, one of them must have volume at most R1 R2 R3 /N . We are led to the
following question: if U ⊂ R is an open set with volume V (U ), what is the largest
possible 2-width of U ? Since U is a subset of R, its 2-width is at most R1 R2 .
For large volumes V (U ), this upper bound is the best possible, but for smaller
volumes it can be improved. Using the width-volume inequality, we can bound
the 2-width of U by CV (U )2/3 . This upper bound is sharp for small volumes
V (U ). These upper bounds can be improved if V (U ) is in the intermediate range
R13 << V (U ) << R1 R22 . An example of a set U with 2-width roughly V (U )2/3 is
the round ball of volume V (U ), which has radius roughly V (U )1/3 . If R13 << V (U ),
then this round ball does not fit in the rectangle R. It turns out that all subsets of
R with volume V (U ) are substantially thinner than the round ball. We make this
precise in the following proposition.
Proposition 5. Let R be a 3-dimensional rectangle with dimensions R1 ≤ R2 ≤
R3 . Suppose that U ⊂ R is an open set with volume V (U ). Then the 2-width of U
              1/2
is at most CR1 V (U )1/2 .
   This estimate is a variation on the width-volume inequality adapted to subsets of
the rectangle R. It improves on the original inequality exactly when R13 << V (U ).
The proof is only a small modification of the proof of the width-volume inequality.
Using this inequality to upper bound the 2-width of one of the sets Ui , we get a
new lower bound for D2 (R, S).
Proposition 6. If R and S are 3-dimensional rectangles with dimensions R1 ≤
                                                  1/2 1/2     1/2 1/2
R2 ≤ R3 and S1 ≤ S2 ≤ S3 , then D2 (R, S) > c[S1 S2 S3 ]/[R1 R2 R3 ].

## p. 7
THE WIDTH-VOLUME INEQUALITY                                7

   In the paper we carry out this idea for all values of k and n, proving lower bounds
for Dk (R, S). In the special case that k = n − 1, our lower bounds and the maps
we will construct match up well enough to determine Dn−1 (R, S) up to a constant
factor.
Theorem 2. Let R and S be n-dimensional rectangles. Let R have dimensions
R1 ≤ ... ≤ Rn , and S have dimensions S1 ≤ ... ≤ Sn . Let Qi denote the quotient
Si /Ri . Up to a constant factor C(n), the optimal (n − 1)-dilation Dn−1 (R, S) is
equal to the maximum of the following list of n monomials in the variables Qi .
                                                              n−l−1
   The first n-1 monomials are given by Q1 ...Ql (Ql+1 ...Qn ) n−l , where l is an
integer in the range 1 ≤ l ≤ n − 1. The final monomial is Q2 ...Qn .
   The algebra here is somewhat complicated, but the complicated expressions in
Qi are not the important point. We have seen that the snake map can have (n-1)-
dilation much smaller than that of the linear map. For any two rectangles R and S
we will construct an explicit map with nearly optimal (n-1)-dilation. Depending on
the rectangles, it may be a linear map, or it may be a minor generalization of the
snake map. Up to a constant factor, the expression in the theorem will turn out
to be the (n-1)-dilation of this map. The lower bounds in the theorem guarantee
that the (n-1)-dilation of this map cannot be substantially improved. (On the other
hand, for 2 ≤ k < n − 1, the k-dilation of the snake map can be improved in some
cases. For more information on this problem, see [9].)
   Related results and open questions
   The literature contains a couple of theorems in a similar spirit to the width-
volume inequality. For example, in appendix 1 of [7], page 128, Gromov proved
the following estimate connecting the Uryson width and the area of a Riemannian
2-sphere. (The Uryson width is a different notion of width from the one in this
paper. For a definition, see Gromov’s book [8], page 108.)
Theorem. (Gromov) Let (S 2 , g) be a Riemannian 2-sphere with Uryson 1-width
W and area A. Then W < 2A1/2 .
Another geometric quantity related to the k-width is the volume of the smallest
stationary k-cycle in a Riemannian manifold. According to the work of Almgren [1],
a closed oriented Riemannian manifold (M, g) contains a stationary k-dimensional
varifold with volume at most Wk (M, g). Recently, Nabutovsky and Rotman proved
several estimates for the length of the shortest stationary 1-cycle in a Riemannian
manifold. One important estimate is the following theorem from [11].
Theorem. (Nabutovsky, Rotman) A closed Riemannian n-manifold (M, g) of vol-
ume V contains a stationary 1-cycle of length at most C(n)V 1/n .
Although these theorems are in a similar spirit to Theorem 1, they don’t give any
upper bounds for k-width for any value of k. These theorems hold in a more gen-
eral setting than Theorem 1 because they apply to arbitrary Riemannian metrics,
whereas Theorem 1 applies only to domains in Euclidean space.
   Comparing our result to the results of Gromov, Rotman, and Nabutovsky, it
seems reasonable to ask whether there is a width-volume inequality for all Rie-
mannian manifolds. We phrase this as a problem.
Open Problem. For which integers k < n is there a constant C(k, n) so that
for every closed oriented Riemannian n-manifold (M, g), the k-width is bounded in
terms of the volume by the formula Wk (M, g) <

## p. 22
22                                     LARRY GUTH

differential forms. Suppose that U and V are diffeomorphic. Let dvolU denote the
volume form on U and dvolV denote the volume form on V . Moser proved in [10]
that there is a diffeomorphism φ from U to V so that φ∗ dvolV = µdvolU , where µ
is the ratio Volume(V )/Volume(U ). This diffeomorphism has n-dilation µ. Since
a degree 1 map is surjective, any degree 1 map from U to V must have n-dilation
at least the ratio Volume(V )/Volume(U ). This result is very satisfactory, but it
has no analogue for k < n. Next we consider the case k = 1. For complicated
domains U and V , our problem may be difficult even for k = 1. The distinguishing
feature of k = 1 is that we have a brute force approach which is not available for
higher values of k. If we fix bounded open sets U and V , then the set of maps
from (U, ∂U ) to (V, ∂V ) with 1-dilation at most λ is compact in C 0 . Therefore, at
least in theory, one can systematically search this class of maps for maps of degree
1. This approach can be carried out on a computer if U and V are polyhedra,
and it would give an estimate of D1 (U, V ) to arbitrary accuracy, although it would
be extremely slow. By constrast, the set of maps with 2-dilation at most λ is not
compact in C 0 , so that even with unlimited computing time I don’t know how to
systematically estimate D2 (U, V ) up to a factor of 10100 .
   We will focus on the special case of maps from a rectangle R to a rectangle S.
Even in this special case, the problem is much harder than I initially expected. We
use the convention that the rectangle R has dimensions R1 ≤ ... ≤ Rn and the
rectangle S has dimensions S1 ≤ ... ≤ Sn . To make the algebra simpler, we let Qi
denote the quotient Si /Ri . We now prove some lower bounds for k-dilation.
Proposition 3.3. Suppose that U is a subset of R. Then Dk (U, S) is at least
c(n)Q1 ...Qk .
Proof. Since U is a subset of R, Wk (R) ≥ Wk (U ). Now if there is a degree non-
zero map from U to S with k-dilation λ, then λWk (U ) ≥ Wk (S). Therefore,
λ ≥ Wk (S)/Wk (R). But according to Proposition 1.2, Wk (S) is at least c(n)S1 ...Sk ,
and Wk (R) is at most R1 ...Rk . Therefore, λ is at least c(n)Q1 ...Qk .           
  We can get more complicated bounds by considering the packing-widths of R
and S.
Proposition 3.4. Suppose that U is a subset of R. Then, for each integer l from
                                                         k−l
0 to k, Dk (U, S) is at least c(n)Q1 ...Ql (Ql+1 ...Qn ) n−l .
Proof. Since U is a subset of R, we have Pk,N (R) ≥ Pk,N (U ) for every k and
N. If there is a map f of non-zero degree from U to S with k-dilation λ, then
λPk,N (U ) ≥ Pk,N (S). To see this, let Si be N disjoint subsets of S, each with width
at least Pk,N (S)−ǫ. Then let Ui be the inverse image F −1 (Si ). The map f restricts
to a degree non-zero map from (Ui , ∂Ui ) to (Si , ∂Si ). Therefore the k-width of Ui is
at least λ−1 (Pk,N (S)− ǫ). Since the sets Ui are disjoint, λPk,N (U ) ≥ Pk,N (S). This
estimate gives us a lower bound λ ≥ Pk,N (S)/Pk,N (R), for every natural number
N.
   The value of Pk,N (R) is estimated in Proposition 2.3. Up to a constant factor
                                                           k−l     k−l
C(n), it is equal to the infimum of R1 ...Rl (Rl+1 ...Rn ) n−l N − n−l , where l lies in the
range 0 ≤ l ≤ k. In particular, we can consider the case that N = Sn ...Sl+1 /Sln−l .
Since there are roughly N disjoint rectangles in S with dimens

## p. 23
THE WIDTH-VOLUME INEQUALITY                                     23

                                                       k−l                    k−l
hand, Pk,N (R) is at most C(n)R1 ...Rl (Rl+1 ...Rn ) n−l [Sn ...Sl+1 /Sln−l ]− n−l . There-
                                                               k−l
fore, Pk,N (S)/Pk,N (R) is at least c(n)Q1 ...Ql (Ql+1 ...Qn ) n−l .
   This finishes the proof of the proposition. The reader can check that the supre-
mum over N of the quotient Pk,N (S)/Pk,N (R) is approximately equal to the maxi-
                              k−l
mum of Q1 ...Ql (Ql+1 ...Qn ) n−l for l in the range 0 ≤ l ≤ k. Therefore, the packing-
width does not give any further lower bounds for Dk (R, S).                              
   The second theorem of this paper is an estimate for Dn−1 (R, S).
Theorem 2. Let R and S be n-dimensional rectangles. Suppose that R has dimen-
sions R1 ≤ ... ≤ Rn and that S has dimensions S1 ≤ ... ≤ Sn . Up to a constant
factor C(n), Dn−1 (R, S) is equal to the supremum of the following quantities:
                                                     n−l−1
                                Q1 ...Ql (Ql+1 ...Qn ) n−l                                (1)

                                      Q2 ...Qn .                                 (2)
In equation (1), the number l is allowed to take any value in the range 1 ≤ l ≤ n−1.
                                                                                    1/2   1/2
   For example, if n is 3, then D2 (R, S) is roughly the supremum of Q1 Q2 Q3 ,
Q1 Q2 , and Q2 Q3 .
   We have already proven the lower bounds in equation 1. They are exactly the
lower bounds in Proposition 3.4 in case k = n − 1.
   The lower bound in equation 2 is simple. Suppose that f is a degree 1 map from
R to S with (n − 1)-dilation λ. The map f restricts to a degree 1 map from the
boundary of R to the boundary of S. Since this map must be surjective, it follows
that λVolume(∂R) ≥ Volume(∂S). But the volume of the boundary of R is at most
2nR2 ...Rn , and the volume of the boundary of S is at least 2S2 ...Sn . Therefore, λ is
at least (1/n)Q2 ...Qn . This finishes the proof of the lower bounds on Dn−1 (R, S).
   In the next section, we will construct degree 1 maps showing that these lower
bounds are sharp up to a constant factor.

                      4. Maps with small (n − 1)-dilation
   In this section, we construct a degree 1 map between rectangles with surprisingly
small k-dilation. After the construction, we check that the k-dilation of this map
can be smaller than the k-dilation of any linear diffeomorphism by an arbitrarily
large factor. Then we will finish the proof of Theorem 2, determining Dn−1 (R, S)
up to a constant factor.
Construction 2. (The snake map) Let R and S be n-dimensional rectangles. Sup-
pose that n ≥ 3 and that k lies in the range 2 ≤ k ≤ n − 1. Suppose that Ri = Si
for i ≤ n − k. Suppose that Rn−k+1 ...Rn−k+b ≥ Sn−k+1 ...Sn−k+b for every b in the
range 1 ≤ b ≤ k. Then there is a degree 1 map from R to S with k-dilation less
than C(n).
Proof. We write R as the product R′ × R′′ , where R′ = [0, R1 ] × ... × [0, Rn−k ] and
R′′ = [0, Rn−k+1 ] × ... × [0, Rn ]. Similarly, we write S = S ′ × S ′′ . By assumption
R′ is congruent to S ′ .
   Because of the inequalities Rn−k+1 ...Rn−k+b ≥ Sn−k+1 ...Sn−k+b , there is a
smooth bilipschitz embedding of S ′′ into R′′ with bilipschitz constant at most C(n).

## p. 24
24                                    LARRY GUTH

We will need a little bit of room later, so we let I be a smooth bilipschitz embed-
ding of 3S ′′ into R′′ , with quasi-isometric constant C(n). (By 3S ′′ , we mean the
rectangle S ′′ dilated by a factor of 3 around its center.) We let A be the image of
I in R′′ . (This set A corresponds to the set A in the description of the snake map
before this proof.) Let H be a smooth function on 3S ′′ which is equal to 1 on the
central S ′′ and is equal to zero on a neighborhood of the boundary of S ′′ . We can
                                                                     −1
choose H with Lipschitz constant as close as we like to Sn−k+1           .
                          −1                                      ′′
   The function H ◦ I is defined on the image of I in R , and it is equal to zero on
the boundary of this image. We extend this function to all of R′′ by setting it equal
to zero on the complement of the image of I. We call the resulting function H̄. We
denote a point in R by (x′ , x′′ ), where x′ lies in R′ and x′′ lies in R′′ . We define
Φ1 (x′ , x′′ ) = (H̄(x′′ )x′ , x′′ ). If we differentiate Φ1 , we find that the norm of the
derivative is bounded by the sum sup |H(x′′ )| + sup |x′ |sup|∇H̄|. The first of these
expressions is bounded by 1, and the second by C(n)Rn−k /Sn−k+1 . Because of our
assumptions about the dimensions of R and S, we have Rn−k = Sn−k ≤ Sn−k+1 ,
and so the map Φ1 has Lipschitz constant less than C. The image Φ1 (R) is contained
in R′ × A ∪ {0} × R′′ . We call this set Q.
   The next step of our construction is to retract the region Q onto R′ × A. To do
this, we first pick a retraction φ2 from R′′ to the image of I. We choose φ2 so that
it maps the complement of A onto the boundary of A. We also assume that φ2 is
piecewise smooth. Next, we define Φ2 (x′ , x′′ ) = (x′ , φ2 (x′′ )).
   The map Φ2 has large k-dilation on R, but its restriction to Q has k-dilation 1.
On the intersection of Q with the region R′ × A, Φ2 is the identity, and so it has
k-dilation 1. The complement of this region in Q is given by the conditions x′ = 0
and x′′ ∈ Ac , where Ac denotes the complement of A in R′′ . The map Φ2 takes
this k-dimensional region into the (k − 1)-dimension region given by the conditions
x′ = 0, and x′′ ∈ ∂A. Therefore, Φ2 has k-dilation zero on the second part of Q.
All together, the map Φ2 has k-dilation 1.
   Next, we define a map Φ3 from the region R′ × A to S ′ × 3S ′′ . This map is
defined by Φ3 (x′ , x′′ ) = (x′ , I −1 (x′′ )). It has Lipschitz constant at most C(n). The
composition Φ3 ◦ Φ2 ◦ Φ1 is a map of R into S ′ × 3S ′′ , with k-dilation less than C(n).
The rectangle S ′ × 3S ′′ contains the rectangle S = S ′ × S ′′ . Since S is convex, there
is a retraction Φ4 from S ′ × 3S ′′ to S with Lipschitz constant 1.
   The composition Φ4 ◦ Φ3 ◦ Φ2 ◦ Φ1 is a degree 1 map from (R, ∂R) to (S, ∂S)
with k-dilation less than C(n).                                                          
   Remark: With a little more work, it is possible to construct a PL isomorphism
from R to S with k-dilation less than C(n).
   We now give an example to show that the snake map badly outperforms the
linear map for some rectangles. Let Link (R, S) denote the smallest k-dilation of
any linear diffeomorphism from R to S.
Proposition 4.1. For each n ≥ 3 and each k in the range 2 ≤ k ≤ n − 1, there
are n-dimensional rectangles R and S which make the ratio Link (R, S)/Dk (R, S)
ar

## p. 25
THE WIDTH-VOLUME INEQUALITY                             25

R to S takes each hyperface of R onto a hyperface of S. The rectangle R has 4
hyperfaces with volume ǫn−2 . On the other hand, the rectangle S has 2(n − 1)
hyperfaces with volume ǫn−3 and only 2 hyperfaces with volume ǫn−2 . Any linear
diffeomorphism from R onto S must take a face of R with volume ǫn−2 onto a face
of S with volume ǫn−3 . Therefore, it must have (n-1)-dilation at least ǫ−1 , and we
conclude that Linn−1 (R, S) ≥ ǫ−1 .
   According to Proposition 3.2, a map with k-dilation λ has (k + i)-dilation at
        k+i
most λ k . Therefore, Dk (R, S) is less than C(n) for all k ≥ 2. By the same
                                      k
argument, Link (R, S) is at least ǫ− n−1 for all k ≤ n−1. Combining these estimates,
we see that Link (R, S)/Dk (R, S) may be arbitrarily large for all k in the range
2 ≤ k ≤ n − 1.                                                                     
  Using the snake map, we now finish the proof of Theorem 2.
Proof. By composing snake maps and linear maps, we will construct enough degree
1 maps to prove the theorem. We begin with the case n = 3.
   By scaling the rectangle S, we can assume that the lower bound for D2 (R, S)
given in Theorem 2 is equal to 1. In other words, we suppose R1 R2 > S1 S2 ,
R12 R2 R3 > S12 S2 S3 , and R2 R3 > S2 S3 . Under these assumptions, we need to
construct a degree 1 map from R to S with 2-dilation less than C. We do so in
three cases.
   If R1 < S1 , then we define a 2-contracting linear diffeomorphism from R to T,
with T1 = S1 , T2 = R2 R1 /S1 , and T3 = R3 R1 /S1 . (The length T2 is indeed bigger
than T1 because R1 R2 > S1 S2 .) Using the first two equations in the list above, we
see that T2 > S2 and T2 T3 > S2 S3 . Therefore, there is a snake map from T to S
with 2-dilation less than C.
   If R1 ≥ S1 but R2 < S2 , then we define a 2-contracting linear diffeomorphism
from R to T, with T1 = R1 R2 /S2 , T2 = S2 , and T3 = R3 R2 /S2 . (The length T3 is
indeed bigger than T2 because R2 R3 > S2 S3 .) Since R1 R2 > S1 S2 , T1 > S1 . Since
R2 R3 > S2 S3 , T3 > S3 . Therefore, there is a 1-contracting linear diffeomorphism
from T to S.
   If R1 ≥ S1 and R2 ≥ S2 , since we have assumed that R2 R3 ≥ S2 S3 , there is a
snake map from R to S with 2-dilation less than C.
   We now turn to the case of higher dimensions. As in the three-dimensional case,
we can scale S so that the lower bound on Dn−1 (R, S) is equal to 1. In other words,
we can assume that the rectangles R and S obey the following list of inequalities
denoted (∗):
                                     n−l−1                        n−l−1
                R1 ...Rl (Rl+1 ...Rn ) n−l > S1 ...Sl (Sl+1 ...Sn ) n−l .      (∗1)

                                  R2 ...Rn ≥ S2 ...Sn .                       (∗2)
Equation (∗1) holds for every integer l in the range 1 ≤ l ≤ n − 1.
   Assuming (∗), we have to construct a degree 1 map from R to S with (n −
1)-dilation at most C(n). The maps we will construct will have the following
structure. First, there will be a snake map from R to an intermediate rectangle T ,
with (n-1)-dilation at most C(n). Then there will be an (n-1)-contracting linear
diffeomorphism from T to S. Choosing the rectangle T and constructing the two
maps is very tedious, but it requires only elementary algebra.
