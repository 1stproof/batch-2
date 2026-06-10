<!-- Generated 2026-05-31T01:41:23 -->
<!-- Source PDF: berman__nonnegative_matrices_in_the_mathematical_sciences.pdf (385338 bytes) -->
<!-- Citation: A. Berman, R. J. Plemmons (1994). Nonnegative Matrices in the Mathematical Sciences. SIAM. -->

# A. Berman, R. J. Plemmons (1994). Nonnegative Matrices in the Mathematical Sciences. SIAM.

## Definitions

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem, [Perron 1907] [Flag: missing numeric label].** If A is a square positive matrix then
a) ρ (A) > 0,
b) ρ (A) is a simple eigenvalue of A,
c) to ρ (A) corresponds a positive eigenvector,
d) µ (A) < ρ (A),
e) lim( A / ( ρ ( A)) m ≡ L = xyT , where
   m→∞


  Ax= ρ (A)x, x>0; AT y = ρ ( A) y ,y>0; xT y = 1 ,
f) for every r, µ ( A) / ρ ( A) < r < 1 , there exists a constant C=C(r,A), such that for every m
 ( A / ρ ( A)) m − L       ≤ Cr m , where A ∞ = max aij .
                       ∞
  *Proof:* (no proof in this paper)

- **Corollary [Flag: missing numeric label].** If B ≠ A is a principal submatrix of an irreducible nonnegative matrix A, then
 ρ (B) < ρ (A).
  *Proof:* (no proof in this paper)

- **Another corollary [Flag: missing numeric label].** If A is a square nonnegative matrix,
      n                      n
min ∑ aij ≤ ρ ( A) ≤ max ∑ aij
  i                    i
      j =1                   j =1
  *Proof:* (no proof in this paper)

- **The Perron-Frobenius Theorem [Frobenius 1912] - Part I [Flag: missing numeric label].** In the first three statements of Perron's Theorem, "positive" can be replaced by
"nonnegative irreducible", namely:
If A ≥ 0 is irreducible then

a) ρ (A) > 0,
b) ρ (A) is a simple eigenvalue of A,
c) to ρ (A) corresponds a positive eigenvector.

In addition, if A ≥ 0 is irreducible (which of course includes A>0):

d) if Ax= λ x and x is positive, then λ = ρ (A),
e) if B ≥ A, B ≠ A, then ρ (B) > ρ (A),
f) if B ≤ A, B ≠ A, then ρ (B) < ρ (A).
  *Proof:* (no proof in this paper)

- **The Perron-Frobenius Theorem, Part II [Flag: missing numeric label].** If A ≥ 0 is irreducible and its index of cyclicity is k>1, then
a) the eigenvalues of A of modulus ρ (A) are ρ ( A)e2π i / k ; i=0,1,...,k-1,
b) rotating the complex plane by 2π / k takes the spectrum of A onto itself,
c) A is permutationally similar to

        0       A12    0      . .     0    
                                           
        0        0    A23     . .     .    
        .        .     .      . .     .    
PAPT =                                     
        .              .      . .     0    
        .                     . .   Ak −1k 
                                          
         Ak 1    .     .      . 0    0 

where the zero blocks on the diagonal are square.
  *Proof:* (no proof in this paper)

- **Theorem [Romanovsky 1936] [Flag: missing numeric label].** Let A ≥ 0 be irreducible and let ki be the greatest common divider of the lengths of cycles
in D(A) that pass through i. Then all the ki 's are equal and are equal to the order of
cyclicity of A.
  *Proof:* (no proof in this paper)

- **The Boyle-Handelman Theorem ([Boyle and Handelman 1991]) [Flag: missing numeric label].** Let λ1 , λ2 ,..., λn be nonzero numbers such that λ1 > max(2 ≤ i ≤ n, λi ) .
Then, for some N, λ1 , λ2 ,..., λn are the eigenvalues of an (n+N)x(n+N) primitive matrix,
iff
λ1 = λ1
                                        n
S k ≥ 0 ; k=1,2,... (where S k = ∑ λuk )
                                       i =1

S k >0=> S jk >0; j,k=1,2,...
  *Proof:* (no proof in this paper)

- **Theorem ([Laffey and Smigoc 2006]) [Flag: missing numeric label].** Let λ1 , λ2 ,..., λn be nonzero complex numbers such that λ1 >0, Re(λi ) ≤ 0 ; i=2,...,n. Then
λ1 , λ2 ,..., λn are the nonzero eigenvalues of an (n+N)x(n+N) nonnegative matrix if
{ λ1 , λ2 ,..., λn }is closed under complex conjugation, S1 ≥ 0 and S 2 > 0 .
The nonnegative matrix can be chosen to be of the form C+tI, where C is a companion
matrix and t is a nonnegative number.
  *Proof:* (no proof in this paper)

- **Corollary ([Laffey and Smigoc 2006]) [Flag: missing numeric label].** The numbers λ1 , λ2 ,..., λn , as in the theorem, solve NIEP iff
{ λ1 , λ2 ,..., λn }is closed under complex conjugation, S1 ≥ 0 ,
S 2 ≥ 0 and S12 ≤ nS2 .
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** Let A ≥ 0 be an n × n primitive matrix and suppose that for some natural number h,
A + A2 + ... + Ah has at least d positive diagonal entries, then γ ( A) ≤ n − d + h ( n − 1) .
  *Proof:* (no proof in this paper)

- **Corollary [Flag: missing numeric label].** If A is an nxn combinatorial symmetric primitive matrix then its index of primitivity is
less than or equal to 2(n-1).
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** The maximal eigenvalue of a stochastic matrix is 1. A nonnegative matrix A is stochastic
iff e, the vector of ones, is an eigenvector of A corresponding to 1.
  *Proof:* (no proof in this paper)

- **Theorem. [Flag: missing numeric label].** If A≥0, ρ ( A) > 0 and Az = ρ ( A) z , then A / ρ ( A) is similar to a stochastic matrix.
  *Proof:* Specifies the required diagonal similarity matrix using the elements of the positive eigenvector.

- **Theorem ([Hardy, Littlewood and Polya 1929]) [Flag: missing numeric label].** An ordered vector x majorizes an ordered vector y iff for some doubly stochastic matrix
A, y=Ax.
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** The set of all n × n doubly stochastic matrices is a convex polyhedron whose vertices are
the permutation matrices.
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** If A is an n × n doubly stochastic matrix then
           n!
 Per ( A) ≥ n
           n
and the minimum is obtained only for the matrix that all of its entries are equal (to 1/n).
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** To the spectral radius of A ≥ 0 there corresponds a positive eigenvector iff the final
classes of A are exactly its basic ones.
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** To the spectral radius of A ≥ 0 a positive eigenvector of A and a positive eigenvector of
AT iff all the classes of A are basic and final.
  *Proof:* (no proof in this paper)

- **Corollary [Flag: missing numeric label].** A is irreducible iff ρ ( A) is simple and positive vectors correspond to ρ ( A) both for A and
for AT .
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** Adj L = kJ where J is a matrix of ones and k is the number of spanning trees of G.
  *Proof:* (no proof in this paper)

- **Neural Networks Theorem [Flag: missing numeric label].** For every graph and for every initial states, there is T such that for all t ≥ T, the states of
the lights at time t+2 are the same as the states at time t.
  *Proof:* Formulates a finite-valued monotonic potential function over state sequences to demonstrate eventual stabilization.

- **Theorem, ([Hall and Newman, 1993]) [Flag: missing numeric label].** The n × n copositive matrices and the n × n completely positive matrices are closed
convex cones in the space of n × n real symmetric matrices, and each is the dual of the
other with respect to the inner product <A,B>=trace AB.
  *Proof:* (no proof in this paper)

- **Theorem (Kaykobad, 1987) [Flag: missing numeric label].** If A = AT is diagonally dominant (aii ≥ ∑ aij , ∀i ) then A is CP.
  *Proof:* (no proof in this paper)

- **Theorem (Drew, Johnson and Loewy , 1996) [Flag: missing numeric label].** A = AT ≥ 0, M ( A) is PSD ⇒ A is CP
  *Proof:* Applies a positive diagonal matrix scaling transformation to construct a diagonally dominant matrix.

- **Theorem (Maxfield and Minc 1962) [Flag: missing numeric label].** For n ≤ 4 ( A = AT ∈ R+n×n ), CP ⇔ DNN
  *Proof:* (no proof in this paper)

- **Theorem (Drew, Johnson and Loewy, 1994) [Flag: missing numeric label].** If A is CP and G(A) does not contain a triangle then M(A) is PSD.
  *Proof:* (no proof in this paper)

- **Theorem (Berman and Hershkowitz, 1987) [Flag: missing numeric label].** If G contains an odd cycle of length greater than 4, then it is not CP.
  *Proof:* Constructs a symmetric positive semidefinite block matrix representing an odd cycle and calculates that its comparison matrix has a negative determinant.

- **Theorem (Berman and Grone, 1988) [Flag: missing numeric label].** Bipartite graphs are CP.
  *Proof:* Directly applies Sylvester's law of inertia to a real symmetric block decomposition.

- **Theorem (Kogan and Berman, 1988, 1993) [Flag: missing numeric label].** A graph G is CP iff it does not contain an odd cycle of length greater than 4.
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** a) If a game converges, the final state and the number of steps do not depend on the
      choice of vertices.
   b) If ρ (N(G))<2, every game converges.
   c) G is a looper iff ρ (N((G))=2.
   d) If ρ (N(G))>2, G is not a looper and there are initial states from which the game
      never loops.
   e) The loopers are exactly the following graphs:




                                                                                    …


                                                                                    …


    f) Let x denote the vector of the initial state and let c denote the vector of the
       numbers at the vertices


                                     1

                                     2



     1           2           3           2       1




                                 1



1        2           3       4           3       2       1



                                 1



     2           4           6           5       4       3     2    1
                         1                                                      1       1
                                                         1              1
                                                                            1               1   …
             1                               1           1              1

                                                                                    1

             1                                                              1
                                         1           1
                                                                                                …
                         2                                   2 2 2 2 2
                                         1           1                      1
             1



    then
       1) If cT x <0, the game is not periodical and does not converge,
       2) If cT x =0, the game loops,
       3) If cT x <0, the game loops (this is the Olympic example).
  *Proof:* (no proof in this paper)

- **Sylvester's law of inertia. [Flag: missing numeric label].** B=SAS* , for some nonsingular matrix S iff i(B)=i(A).
  *Proof:* (no proof in this paper)

- **Lyapunov’s Theorem [Flag: missing numeric label].** A ∈ C n×n is positive stable if and only if there exists a positive definite matrix G such that
GA + A*G is positive definite.
Furthermore, if for some positive definite matrix H, there exists an Hermitian matrix G,
such that:
GA + A*G = H
Then A is positive stable iff G is positive definite.
  *Proof:* (no proof in this paper)

- **The Routh-Hurwitz Theorem [Flag: missing numeric label].** A ∈ R n×n is positive stable iff the n leading principal minors of Ω ( A) are positive.
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** Let A be a Z-matrix, A = α I − B ; α real, B nonnegative.
Then the following conditions are equivalent:
    a) α > ρ ( B) , i.e., A is an M-matrix
    b) A is inverse positive, i.e. A−1 exists and is nonnegative.
    c) A is monotone, i.e. Ax ≥ 0 ⇒ x ≥ 0 .
   d) A is diagonally stable, i.e. there exists a positive diagonal matrix D such that
      DA + AT D is positive definite.
   e) A is positive stable.
   f) A is a P-matrix, i.e. all the principal minors of A are positive.
   g) A does not reverse the sign of any vector, i.e., if x ≠ 0 and y=Ax, then for some i,
      xi yi > 0 .
   h) Every real eigenvalue of a principal submatrix of A is positive.
   i) A+tI is nonsingular for all t ≥ 0 .
   j) Every real eigenvalue of A is positive.
  *Proof:* Sequentially establishes chains of logical implications between the conditions.
Relies heavily on nonnegativity properties, inverse operators, and diagonal stability.

- **Theorem [Flag: missing numeric label].** Let A ∈ R n×n of bd K be a proper cone in R n . Then:
    a. If A is K-nonnegative, then ρ ( A) is an eigenvector and K contains a
       corresponding eigenvector;
    b. If A is K-positive, then ρ ( A) is greater than the absolute value of any other
       eigenvalue and an eigenvector corresponding to ρ ( A) lies in int K.
    c. If A is K-irreducible then ρ ( A) is a simple eigenvalue and any other eigenvalue
       with the same modulus is also simple; there is an eigenvector corresponding to
        ρ ( A) in int K, and no other eigenvector (up to scalar multiples) lies in K;
    d. A K-nonnegative matrix is K-primitive iff for some natural number m, Am is K-
       positive.
  *Proof:* (no proof in this paper)

- **Theorem [Flag: missing numeric label].** An n × n irreducible tournament is primitive iff n is greater than 3.
  *Proof:* (no proof in this paper)