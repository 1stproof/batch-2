<!-- Generated 2026-05-31T01:16:17 -->
<!-- Source PDF: hairer__exponential_mixing_properties_of_stochastic_pdes_t.pdf (290285 bytes) -->
<!-- Citation: Hairer, M. (2002). Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling. Probability Theory and Related Fields. -->

# Exponential Mixing Properties of Stochastic PDEs Through Asymptotic Coupling

## Definitions
- **Definition 2.2.** Let be a Markov chain on a Polish space and let P be the associated family of measures on the pathspace . A coupling for is a family C of probability measures on satisfying C P and C P , where and are defined as above.
- **Definition 3.1.** Let by a RDS with state space as before. A Lyapunov function for is a function ] for which there exist constants ( ) and , such that ( ) ( ) ( ) , with ( ) .

## Lemmas, Theorems, Propositions, Corollaries
- **Lemma 2.3.** The measures P satisfy P for .
  *Proof:* Bound marginal measures using the definitions of the coupling construction.
- **Lemma 3.2.** Let be a RDS satisfying assumptions A1 and A2. Then, there exists a constant such that ,) , for every and every .
  *Proof:* Use Markov's inequality combined with the Lyapunov condition.
- **Proposition 3.4.** Let Q be defined as above and suppose that assumptions A1 and A4 hold. Then there exists for every a constant such that ( Q ( , whenever ( ' ) .
  *Proof:* Apply Lemma 3.2 and take the limit as time approaches infinity.
- **Proposition 3.5.** Let assumptions A1, A2 and A5 hold. Then, there exists a positive constant and, for every , a constant such that ( (RQ ) ( , holds for every , whenever ( ' ) .
  *Proof:* Bound the total variation norm using Lemma 3.6 and Assumption A5. Optimize the constants to ensure an exponential decay rate.
- **Lemma 3.6.** Let ( ) be two equivalent probability measures with ( ) ( ) ( ). Then the conditions ( ) ) and ( ) ( ) , for some measurable set imply that ( ) ) ) .
  *Proof:* Direct algebraic manipulation of the total variation norm definition.
- **Theorem 4.1.** Let be a RDS with state space satisfying assumptions A1–A5. Then, there exists a constant such that ) ( ( L ( ' ) , for every ( ' ) and every .
  *Proof:* Bound tail distributions using Lemma 4.5. Handle hitting times using standard Lyapunov function techniques.
- **Corollary 4.3.** If satisfies assumptions A1–A5, it possesses a unique invariant measure and ( ) ( ( ) L
  *Proof:* Show the sequence of measures is Cauchy in the Wasserstein norm using the Lyapunov structure.
- **Lemma 4.4.** Let be a RDS with state space satisfying assumptions A1 and A3, and let be defined as above. Then, there exists a constant such that ) ( P ( L , for every ( ' ) and every .
  *Proof:* Express the total variation norm bound in terms of the constructed stopping time.
- **Lemma 4.5.** If the have an exponential tail and we define max , then the probability distribution of also has an exponential tail.
  *Proof:* Apply Cauchy's formula to the probability generating function.
- **Theorem 5.5.** Let , and be such that assumptions B1 and B2 are satisfied. If there exists a function such that assumptions B3 and B4 hold, constants then the solution of (5.1) possesses a unique invariant measure and there exist such that ( P&)& ( L ( )
  *Proof:* Construct explicit binding functions and compute their densities using Girsanov's theorem. Use cut-off procedures to ensure a-priori bounds hold uniformly to validate assumptions A1–A5.
- **Lemma 5.6.** The family of densities ( ) is given by ( ) exp ( ' ) (' ) ( ) ) ( ( ) ( , where the arguments of in the second term are the same as in the first term.
  *Proof:* Validate conditions for Girsanov's theorem using a cut-off procedure and a-priori bounds.
- **Theorem 6.1.** There exist positive constants and , and a unique measure ( ) such that ( )& ( L ( ( ), for every and every .
  *Proof:* Project the difference process onto unstable modes and verify a differential inequality.
- **Theorem 6.2.** There exists a unique probability measure ( ) such that for every . Furthermore, there exist constants and such that , ( )& ( L , for every ( ).
  *Proof:* Use a known uniform estimate on the Lyapunov function combined with Theorem 4.1.
- **Theorem 6.4.** For the problem (6.9), there exists a unique probability measure ( ) such that constants and such that for every . Furthermore, there exist , ( )& ( L for every ( ).
  *Proof:* Split the system into low and high modes. Recursively construct a sequence of polynomial binding variables to force contraction.