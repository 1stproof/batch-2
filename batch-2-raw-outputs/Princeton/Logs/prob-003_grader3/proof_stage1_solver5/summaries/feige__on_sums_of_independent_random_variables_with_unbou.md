<!-- Generated 2026-05-31T02:03:57 -->
<!-- Source PDF: feige__on_sums_of_independent_random_variables_with_unbou.pdf (267467 bytes) -->
<!-- Citation: Feige (2006). On sums of independent random variables with unbounded variance and estimating the average degree in a graph. SIAM Journal on Computing. -->

# On sums of independent random variables with unbounded variance and estimating the average degree in a graph (Feige, 2006)

## Definitions
*(None in this paper)*

## Lemmas, Theorems, Propositions, Corollaries

- **Theorem 1.** Let X1 , . . . , Xn be arbitrary nonnegative independent random variables, with expectations µ1 , . . . , µn respectively, where µi ≤ 1 for every i. Let X = \sum_{i=1}^n Xi , and let µ denote the expectation of X (hence, µ = \sum_{i=1}^n µi ). Then for every δ > 0, P r[X < µ + δ] ≥ min[δ/(1 + δ), 1/13]
  *Proof:* Reduces variables to two-valued supports with roughly equal means via a sequence of bounded transformations, and concludes with a deep case analysis on the remaining surplus.

- **Theorem 2.** For any d0 > 0, ² > 0 and ρ = 2 + ², there is a ρ estimation algorithm for the average degree of a graph that uses O(1/² \sqrt{n/d0}) queries, and is applicable to all graphs of average degree at least d0 .
  *Proof:* Bounds overestimations via generalized Markov properties and underestimations via Chebyschev's inequality on high/low degree partitions, combining multiple parallel estimates to bound the total error.

- **Theorem 3.** There is a randomized algorithm that runs in time O( \frac{m}{\epsilon} \sqrt{\frac{n}{c}} \log n ) on graphs with n vertices and m edges, and outputs a list of edges that with high probability satisfies:
  1. Every edge that is on at least c shortest paths is on the list.
  2. No edge that is on less than (1/2 − ²)c shortest paths is on the list.
  *Proof:* Casts the shortest path counting task as estimating average degrees in simultaneous virtual graphs, which are constructed efficiently using forward and backward Breadth First Search trees.

- **Lemma 4.** Let Xit be a random variable whose support includes at least three values. Then Xit can be replaced by a new variable Xit+1 with µt+1 i = µti , and whose support includes only two values from the original support of Xit . This can be done in a way that satisfies inequality (2).
  *Proof:* Formulates a feasible linear program over the conditional probabilities and uses its basic optimal solution to bound the support size.

- **Proposition 5.** If the total surplus satisfies st < δ, then P r[X t ≥ µt + δ] = 0.
  *Proof:* Maximizes the sum by assuming all variables attain their maximum value simultaneously.

- **Lemma 6.** If stage 1 ended with a random variable with mean below 1/2, then P r[X t < µt ] ≥ δ/(1/2 + δ).
  *Proof:* Evaluates the probability of the single remaining variable coming up zero using the lower bound on its surplus.

- **Proposition 7.** If stage 1 ended with all random variables having mean at least 1/2, then µt1 /2 ≤ µtn0 ≤ µt1 < 3/2.
  *Proof:* Traces the last merge operation that created a variable with mean greater than 1 to bound the remaining variables' means.

- **Proposition 8.** Let X1 , . . . , Xn be independent random variables with means µ1 ≥ . . . ≥ µn and supports {0, µ1 + s 1 }, . . . , {0, µ n + s n }, and let X = \sum_{i=1}^n Xi , µ = \sum_{i=1}^n µi and s = \sum_{i=1}^n si . Then P r[X < µ − µn + s] ≥ s/(µ1 + s)
  *Proof:* Bounds the probability that all variables exceed zero by maximizing the product of individual failure probabilities.

- **Lemma 9.** 1. If stage 1 ended with all random variables having mean at least 1/2, and if st < µtn0 , then P r[X t < µt ] ≥ δ/(µt1 + δ) ≥ δ/(3/2 + δ).
  2. If in addition δ ≤ 1/12 then either P r[X t < µt ] < δ/(1 + δ), or one merge operation before the end of stage 1 it must have been the case that P r[X t−1 < µt−1 + δ] ≥ δ/(1 + δ).
  *Proof:* Analyzes the surplus distribution subcases before the final merge operation and bounds the target failure probability using Proposition 8.

- **Lemma 10.** Let α = 1/3, and let r denote the time step at which stage 2 ends. Then either P r[X r < µr ] ≥ 1/13, or one modified merge operation before stage 2 ends P r[X r−1 < µr−1 ] ≥ 1/13.
  *Proof:* Iteratively performs case analyses on the remaining variables' total surplus using the modified sequence of transformations, bounding probabilities through sub-lemmas to minimize the failure bound.

- **Lemma 11.** If stage 2 ends without the condition s0 ≤ αµr1 being reached, then P r[X r < µr ] > α/(1 + α).
  *Proof:* Bounds the failure probability directly since only one nonconstant random variable remains.

- **Lemma 12.** If stage 2 ends with βµr1 ≤ s0 ≤ αµr1 , where 0 ≤ β ≤ α is some constant that will be optimized later, then P r[X r < µr ] ≥ min[ (α − 2α2)/(1 + α) , (β − 2β 2)/(1 + β) ].
  *Proof:* Uses Markov's inequality and Proposition 8 to analyze the single variable with small mean against the combined surplus of the others.

- **Lemma 13.** If stage 2 ends with s0 < βµr1 , and 0 < β < α/2, then one merge prior to the end of stage 2 it must have been the case that P r[X r−1 < µr−1 ] was at least the minimum of the following expressions:
  1. (α−β)/(1/2+α−β) * (1/2−β)/(1−β)
  2. (α−3β/2)/(1+α−3β/2) * (1−3β/2)/(3/2−3β/2)
  3. (α−2β)/(1+α−2β)
  4. ((1/2−β)/(1−β))^2
  5. (1/2−3β/2)/(3/2−3β/2) * (1−3β/2)/(3/2−3β/2)
  *Proof:* Divides into two main cases based on the means of the last merged variables and minimizes the probabilities over local extrema of the conditional surplus probabilities.

- **Corollary 14.** There is some universal constant α > 0 such that for every graph with average degree d, by querying t random vertices (with replacement) for their degree, the average d∗ satisfies P r[d∗ ≤ (1 + 1/t)d] ≥ α.
  *Proof:* (immediate from Theorem 1)

- **Lemma 15.** For arbitrary δ > 0 (that will later be fixed to 50 \sqrt{2/α}, where α is as in Corollary 14), with probability at least 1 − 4 \sqrt{2}/δ − 2^{−Ω(δ)} , X ≥ E[X]/2 (1 − δ/k)
  *Proof:* Partitions the graph vertices into high and low degrees to bound the variance of the edge endpoint counts, then applies Chebyschev's inequality to each part to prove concentration around the mean.

- **Proposition 16.** With probability 1 − 2^{−Ω(c)} , Y1 ≥ ch/2
  *Proof:* Applies a concentration bound on the expected number of queried high-degree vertices.

- **Proposition 17.** A vertex in L can cover at most |H| = c \sqrt{nd0}/k endpoints in EL,H .
  *Proof:* Leverages the fact that the graph is simple to bound the maximum possible edges a single low-degree vertex can have into the high-degree set.

- **Proposition 18.** For λ > 0, with probability at least 1 − 1/λ2 , Y2 ≥ E[Y2 ] − λ \sqrt{cdn/2}
  *Proof:* Bounds the variance of the high/low endpoints and applies Chebyschev's inequality.

- **Proposition 19.** For λ > 0, with probability at least 1 − 1/λ2 , Y3 ≥ E[Y3 ] − λ \sqrt{hkm3 / \sqrt{d0 n}}
  *Proof:* Maximizes the variance using the bounded maximum degree in the low-degree set and applies Chebyschev's inequality.

- **Proposition 20.** With probability at least 1 − 2/λ2 − 2^{−Ω(c)} , X ≥ E[X]/2 + ch/2 − λ \sqrt{cdn/2} − λ \sqrt{hkm3 / \sqrt{d0 n}} + km3 / \sqrt{d0 n}
  *Proof:* Sums the respective lower bounds from Propositions 16, 18, and 19.

- **Corollary 21.** For some universal constant β, using β/² \sqrt{n/d0} queries, one can estimate the average degree d of an n node graph within a ratio of (2 + ²), provided that d > d0 .
  *Proof:* Takes the minimum over multiple parallel unbiased estimations to bound the error.

- **Proposition 22.** For every (reasonable) n, d, ², one can construct a graph G1 with (1 + ²)nd edges and a graph G2 with dn/2 edges, such that Ω( 1/² \sqrt{n/d} ) vertices need to be queried in order to have probability above 2/3 of distinguishing between them.
  *Proof:* Constructs two graphs with different average degrees but statistically indistinguishable degree distributions under small sample sizes.

- **Proposition 23.** Under the tie breaking convention specified above, there is an O(m)-time algorithm that does the following. Given a connected graph G with n vertices and m edges and an arbitrary vertex v, it simultaneously counts for every edge e, for how many vertices u does edge e participate in the shortest path connecting u and v.
  *Proof:* Builds forward and backward Breadth First Search trees from the root vertex to tally shortest paths passing through each edge in linear time.