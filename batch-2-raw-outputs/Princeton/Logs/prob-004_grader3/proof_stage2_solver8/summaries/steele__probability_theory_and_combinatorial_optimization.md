<!-- Generated 2026-05-31T01:48:22 -->
<!-- Source PDF: steele__probability_theory_and_combinatorial_optimization.pdf (643957 bytes) -->
<!-- Citation: J. Michael Steele (1997). Probability Theory and Combinatorial Optimization. SIAM. -->

# The Objective Method: Probabilistic Combinatorial Optimization and Local Weak Convergence (Aldous and Steele, 1997)

## Definitions
- **Deﬁnition 2.1 (Geometric Graphs and the Two Classes G and G   ).** If G = (V, E) is a connected, undirected graph with a countable or inﬁnite vertex set V and if   is an edge length function that makes G locally ﬁnite in the sense that for each vertex v and each real   < ∞ the number of vertices within distance   from v is ﬁnite, then G is called a geometric graph. When there is also a distinguished vertex v, we say that G is a rooted geometric graph with root v. The set of geometric graphs will be denoted by G, and the set of rooted geometric graphs will be denoted by G   .
- **Deﬁnition 2.2 (Convergence in G   ).** We say that Gn converges to G∞ in G   provided that for each continuity point   of G∞ there is an n0 = n0 ( , G∞ ) such that for all n ≥ n0 there exists a isomorphism γn,  from the rooted geometric graph N  (G∞ ) to the rooted geometric graph N  (Gn ) such that for each edge e of N  (G∞ ) the length of γn,  (e) converges to the length of e as n → ∞.
- **Deﬁnition 4.2 (Minimal Spanning Forest).** The minimal spanning forest of an inﬁnite graph G that has all distinct edge lengths is the subgraph M SF (G) of G with the same vertex set as G and with an edge set that contains each edge e = (v1 , v2 ) of G for which
 1. c(G, v1 ; s) and c(G, v2 ; s) are disjoint, and
 2. c(G, v1 ; s) and c(G, v2 ; s) are not both inﬁnite
when s is taken to be the length of the edge e = (v1 , v2 ) ∈ G.
- **Deﬁnition 5.2 (Involution Invariance).** A probability measure µ on G   is said to be involution invariant provided that the σ-ﬁnite measure µ induced on G   by µ is invariant under the involution map ι; that is to say,

                  µ(A) = µ(ι−1 (A))    for all Borel A ⊂ G   .
- **Deﬁnition 6.2 (Stable Functionals and the Inﬂuence Function).** The functional ξ is said to be stable on the locally ﬁnite set S provided that one has
                         lim ξ(S; m) = lim ξ(S; m) .
                       m→∞              m→∞

Moreover, when ξ is stable on S, we let ξ∞ (S) denote the value of the common limit and we call ξ∞ (S) the inﬂuence function of ξ on S.

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 2.3 (Grimmett’s Lemma).** The randomly rooted uniformly distributed labelled tree T n on n vertices converges weakly in G   to the “skeleton tree” T ∞ ; that is, one has
                                d
                           T n −→ T ∞       as n → ∞ .
  *Proof:* (no proof in this paper)
- **Proposition 3.1.** If T is an F -weighted PGW(1) tree where F is continuous and F ([0, ∞)) = 1, then the distribution
                                               
                            G(x) = P B(T ) ≤ x

is the unique solution of the ﬁxed-point equation

                                  DF (G) = G .
  *Proof:* Constructs a recursive random variable mapping by matching root expansion logic with the distributional definition, thereby obtaining the fixed-point uniquely.
- **Proposition 3.2.** For any continuous distribution F with support on [0, ∞), the ﬁxed-point equation
                              DF (H) = H                            (3.15)
has a unique solution H; moreover, one has
                                    
                lim P B T big
                          n     ≤ x = H(x)        for all x ∈ R .
               n→∞
  *Proof:* Relies on Markov chain theory for existence, a simultaneous coupling argument for uniqueness, and bounding through a stabilized recursive limit (Lemma 3.6) to establish the sequence's weak convergence.
- **Theorem 3.3.** If F is a continuous distribution with support on [0, ∞) and a ﬁnite mean, then the maximum weight Mn of an F -weighted random tree on n vertices satisﬁes

                                 1
                              lim  E [Mn ] = E [ξ1(ξ > Y + Z))] TS1
                             n→∞ n

        where the random variables ξ, Y , and Z are independent,

                                  ξ ∼ F,      Y ∼ G,         and     Z∼H,

       and the distributions G and H are the unique solutions of the ﬁxed-point equations
                            DF (G) = G and DF (H) = H .
  *Proof:* Takes the limit under the expectation in the exact inclusion formula using uniform integrability and weak convergence.
- **Theorem 3.4.** If F (x) = 1 − e−x for x ≥ 0, then the maximum weight Mn of a partial matching on an F -weighted random tree on n vertices satisﬁes
                               ∞  s
             1
            limE[Mn ] =                  c(e−y − be−s ) exp(−ce−y − ce−(s−y) )se−s dy ds ,
         n→∞ n                0     0

       where the constants b and c are deﬁned by equations (3.21) and (3.22) of Lemma 3.5. Moreover, by numerical integration one ﬁnds

                                              1
                                        lim       E[Mn ] = 0.239583....
  *Proof:* Integrates the explicitly derived exponential solutions of the fixed-point equations provided in Lemma 3.5.
- **Lemma 3.5.** If F (x) = 1 − e−x for x ≥ 0, then the solutions G and H of the ﬁxed-point equations (3.18) are

                    G(y) = exp(−ce−y )          for y ≥ 0                       (3.19)
                                       −z               −z
              and   H(z) = (1 − be          ) exp(−ce        )   for z ≥ 0 ,    (3.20)

where b and c are related by

                                 b = c2 /(c2 + 2c − 1)                          (3.21)

and c is the unique strictly positive solution of

                                    c2 + e−c = 1 .
  *Proof:* Explicitly solves the probability identities using the lack-of-memory property of the exponential distribution.
- **Lemma 3.6.** Fix the integer k ≥ 1 and suppose for each n we have nonnegative random variables {Xmn
                               : −2k + 1 ≤ m ≤ 0} that are linked to the variables {Ym : −2k + 2 ≤ m ≤ 0} by the relation
            n


      n
     Xm         n
        = max{ ξm − Xm−1
                     n
                         , Ymn }        for all m = −2k + 2, −2k + 3, . . . , 0 ,

where the random variables {ξm n
                                  : −2k + 2 ≤ m ≤ 0} are independent, have distribution F , and are independent from
                   n
                  X−2k+1    and       {Ymn : −2k + 2 ≤ m ≤ 0} .

Further, suppose that one has
                                  d
     (Ymn : −2k + 2 ≤ m ≤ 0) −→ (Ym : −2k + 2 ≤ m ≤ 0) as n → ∞ ,

where the random variables {Ym : m = 0, −1, −2, ...} are independent and have distribution G. If H is the unique solution of

                                  DF (H) = H ,

then we have the bound
      lim sup | P (X0n ≤ x) − H(x) | ≤  k        for all x ∈ R and k = 1, 2, ...
       n→∞

where   is given by                 
                           =             dF (x) dG(y) < 1 .
  *Proof:* (no proof in this paper)
- **Theorem 4.1 (Convergence Theorem for Kn ).** If K n is a randomly rooted complete graph on n vertices with independent edge lengths ξe that satisfy
                  P (ξe ≥ n−1/d x) = e−x for all x ≥ 0 ,
                                        d
then we have the local weak convergence
                                  d
                              K n −→ T   as n → ∞ .

where T is a PWIT with edge weight mean function xd .
  *Proof:* (no proof in this paper)
- **Lemma 4.3.** The average cost A per vertex for the MSF of a PWIT satisﬁes
                                                      ∞
                                                       
                                  A = ζ(3) =                k −3 .
                                                      k=1
  *Proof:* Conditions the Poisson Galton-Watson process, setting up the expected length formula as an integral of the branching extinction probability which is exactly evaluated.
- **Theorem 4.4.** Let each edge e of the complete graph on n vertices be assigned an independent cost ξe with distribution F where F has a ﬁnite variance and where F   (0) exists and is nonzero. If CnMST (F ) denotes the minimal cost of a spanning tree of this graph, then as n → ∞, we have
                     p
     CnMST (F ) −→ ζ(3)/F   (0)            and       E[CnMST (F )] → ζ(3)/F   (0) .
  *Proof:* (no proof in this paper)
- **Theorem 5.1.** If Cn denotes the minimal cost of a perfect matching of the complete graph Kn on n vertices with independent edge costs ξe having the exponential distribution with mean n, then
                                         ∞
                         1          1   −2 1
                      lim  E[Cn ] =    k = ζ(2) .                           (5.1)
                     n→∞ n          2      2
                                        k=1
  *Proof:* Establishes the lower bound via weak convergence to the optimal involution-invariant matching on the Poisson Weighted Infinite Tree (PWIT). Shows the upper bound by demonstrating that a locally optimal $\varepsilon$-feasible matching can be pulled back to $K_n$ at negligible additional cost.
- **Lemma 5.3.** If µ is the probability distribution of G[X] where G[X] is given by the standard construction and G[X] is ﬁnite with probability one, then µ is involution invariant. Conversely, if the probability measure µ is involution invariant and concentrated on the ﬁnite connected graphs in G   , then µ is the distribution of a G   -valued random variable G[X] that is given by the standard construction.
  *Proof:* Computes marginal mass for directed edges by conditioning on the fixed finite graph structure and verifying that uniformly distributed roots directly correspond to symmetric marginal transition probabilities.
- **Theorem 5.4 (MST Convergence Theorem).** Let G∞ denote a G   -valued random variable such that with probability one G∞ has inﬁnitely many vertices and no two of the edges of G have the same length. Further, let {Gn : n = 1, 2, ...} denote a sequence of G   -valued random variables such that for each n the distribution of Gn is given by the standard construction and such that for each n the vertex set of Gn has cardinality n with probability one. If
                               d
                         Gn −→ G∞ as n → ∞ ,                              (5.2)
then one has the joint weak convergence in G   × G   ,
                                             d                           
                     Gn , M ST (Gn )       −→            G∞ , M SF (G∞ ) .   (5.3)

Further, if Nn denotes the degree of the root of M ST (Gn ) and N denotes the degree of the root of M SF (G∞ )
                           d
                     Nn −→ N           and       E[Nn ] → E[N ] = 2 ,        (5.4)

and, if Ln denotes the sum of lengths of the edges incident to the root of M ST (Gn ) and L denotes the corresponding quantities for M SF (G∞ ), then
                                                 d
                                       Ln −→ L .
  *Proof:* Translates tight subsequences via Skorohod embedding to an almost sure space. Uses exclusion principles and the expected bounding constraints derived from involution invariance to verify the subset sets identically match.
- **Lemma 5.5.** Let G be an involution invariant element of G   with root r and let W be an involution invariant subset of the edges of G. If
                               
                           E      1(e ∈ W ) = 0 ,
                                e:r∈e

then W is empty with probability one.
  *Proof:* (no proof in this paper)
- **Lemma 5.6.** E[N ] = 2 .
  *Proof:* Categories incident minimal spanning forest edges into finite/infinite splitting classes and applies involution invariance to show symmetrically opposite bounds equate perfectly to two.
- **Lemma 5.7 (Logistic Solution of a Distributional Identity).** The unique solution of the identity (5.18) is the logistic distribution

                     F (y) = 1/(1 − e−y ),      −∞ < y < ∞                  (5.19)

corresponding to the density function

                  f (y) = (ey/2 + e−y/2 )−2 ,    −∞ < y < ∞ .
  *Proof:* Interprets the fixed-point equation as the void probability of a 2D Poisson process, converting it into a separable differential equation solved explicitly by the logistic curve.
- **Lemma 5.8 (Triple Tree Process).** There exists a process (T , ξe , X(e) : e ∈ ET ) where T is a PWIT with associated edge lengths { ξe : e ∈ ET } and where { X(e) : e ∈ ET } is stochastic process indexed by the directed edges of T with the three following properties:
(i). for each directed edge e = (u, v) ∈ ET we have
           X(u, v) = min{ξ(v, w) − X(v, w) : (v, w) ∈ ET , w = u}          (5.21)
(ii). for each e ∈ ET that is directed away from the root of T the random variable X(e) has the logistic distribution, and
(iii). for each pair of oppositely directed edges (u, v) and (v, u) in ET , the random variables X(u, v) and X(v, u) are independent.
  *Proof:* Constructs the process depth-by-depth recursively from independent logistic roots, utilizing Kolmogorov's consistency theorem for the infinite extension.
- **Lemma 5.9 (Matching Lemma).** The set of edges (v, v ∗ ) deﬁned by the rule ϕ(v) = v ∗ is a matching on the special PWIT T .
  *Proof:* Checks that substituting the strict criteria backwards verifies uniqueness and mutual bidirectionality, confirming $\phi(\phi(v))=v$.
- **Lemma 5.10 (Optimality on the PWIT).** Let M denote any matching of T that is involution invariant. If (r, s) is the edge of M that contains the root r of T , then one has
                            E[ξ(r, s)] ≥ E[ξ(r, r∗ )] .
  *Proof:* (no proof in this paper)
- **Lemma 5.11.**                                                 π2
                               E[ξ(r, r∗ )] =
                                                6
  *Proof:* Calculates the expectation directly by integrating over the independent logistically distributed split thresholds condition on the conditionally Poisson variable lengths.
- **Theorem 6.1.** For the randomly rooted normalized sample

                         Sn = n1/d (Xi − XI : 1 ≤ i ≤ n)

of independent random variables with the uniform distribution on [0, 1]d, one has the joint local weak convergence
                                           d                         
                     Sn , M ST (Sn )       −→        P0 , M SF (P0 ) .
  *Proof:* (immediate from Theorem 5.4)
- **Theorem 6.3.** For each constant 0 < τ < ∞ we suppose that ξ is almost surely stable for the homogenous Poisson process Pτ with intensity τ , and we let ξ∞ (Pτ ) denote the corresponding inﬂuence function. If the sequence
                                           
        ξ(n1/d X1 ; n1/d Xn ) : 1 ≤ n < ∞   is uniformly integrable ,    (6.8)

where observations in the sample Xn = {X1 , X2 , ..., Xn } are i.i.d. with density f on Rd , then the inﬂuence function satisﬁes
   I[τ ] = E[ξ∞ (Pτ )] < ∞     for each 0 < τ < ∞ such that f (τ ) > 0 ,      (6.9)

and the normalized sums satisfy
                                   
                 n−1 Hξ (Xn ) →          I[f (x)]f (x)dx    inL1 .           (6.10)
  *Proof:* (no proof in this paper)
- **Theorem 6.4.** Suppose that G is a G   -valued random variable that is a weak limit in G   of a sequence {Gn [Xn ] : n = 1, 2, ...} of uniformly rooted random graphs where
    (1) for each n ≥ 1, the graph Gn is planar with probability one, and
    (2) max{deg(v) : v ∈ Gn } ≤ M < ∞ for all n ≥ 1,
then with probability one, the random walk on the graph G(ω) is recurrent.
  *Proof:* (no proof in this paper)