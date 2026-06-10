<!-- Generated 2026-05-31T01:51:32 -->
<!-- Source PDF: fonseca__degree_theory_in_analysis_and_applications.pdf (334857 bytes) -->
<!-- Citation: Fonseca, I., & Gangbo, W. (1995). Degree Theory in Analysis and Applications. Oxford University Press. -->

# On the total variation of the Jacobian (Fonseca, I., & Gangbo, W. (1995). Degree Theory in Analysis and Applications. Oxford University Press.)

## Definitions
None.

## Lemmas, Theorems, Propositions, Corollaries
- **Theorem 1.** Let u be a function of class W 1;p ðO; R2 Þ-Wloc 1;N ðO\f0g; R2 Þ for some pAð1; 2Þ: Let v : ½0; 2p -G; vðWÞ ¼ ðv1 ðWÞ; v2 ðWÞÞ; WA½0; 2p ; be a Lipschitz-continuous map, with vð0Þ ¼ vð2pÞ and G as in (4), and such that lim jjuðR; Þ   vð ÞjjLN ðð0;2pÞ;R2 Þ ¼ 0: If the tangential derivative Dt u of u satisfies the bound sup 1 2 p jDt uj dx ¼ sup 1 2 p r1 p dr juW ðr; WÞjp dWpM0 for some positive constant M0 ; then the total variation of u is given by TVðu; OÞ ¼ jdet DuðxÞj dx þ 1 2 fv ðWÞv2W ðWÞ   v2 ðWÞv1W ðWÞg dW  :
  *Proof:* Establishes a lower bound using tangential derivative estimates and weak convergence. Proves an upper bound for radially symmetric maps using piecewise affine approximations, then extends this to general maps using localized cut-off functions.

- **Corollary 2.** Let G be as in (4), and let u ¼ v : ½0; 2p -G be a Lipschitz-continuous map such that vð0Þ ¼ vð2pÞ: Then det DuðxÞ ¼ 0 for almost every xAR2 and the total variation of the Jacobian determinant is given by TVðu; OÞ ¼ 1 2 fv ðWÞvW ðWÞ   v ðWÞvW ðWÞg dW  :
  *Proof:* (immediate from Theorem 1)

- **Lemma 4.** If v : ½0; 2p -R2 is a Lipschitz-continuous curve such that vðWÞa0 for every WA½0; 2p ; then for every a; bA½0; 2p with aob; there exists kAZ such that Av ðbÞ   Av ðaÞ ¼ Arg vðbÞ   Arg vðaÞ þ 2kp:
  *Proof:* (no proof in this paper)

- **Lemma 5.** Let G be as in (4) and let v : ½0; 2p -G be a Lipschitz-continuous map. If Argðvð0Þ   xÞ ¼ 0 then the curve v may be represented as vðWÞ :¼ x þ rðAv x ðWÞÞðcos Av x ðWÞ; sin Av x ðWÞÞ for all WA½0; 2p :
  *Proof:* Uses Lemma 4 to express the angle function in terms of the argument and matches it with the radial parametrization.

- **Lemma 6 (The ‘‘umbrella’’ lemma).** Let G be as in (4) and let v : ½0; 2p -G be a Lipschitz-continuous map. If a; bA½0; 2p ; aob; are such that Av x ðaÞ ¼ Av x ðbÞ; then for every e40 there exists a Lipschitz-continuous map w : Sða; bÞ-R2 satisfying the boundary conditions wð1; WÞ ¼ vðWÞ 8WA½a; b ; wðR; aÞ ¼ wðR; bÞ ¼ x þ RðvðaÞ   xÞ 8RA½0; 1 ; and such that jdet DwðxÞj dxoe:
  *Proof:* Constructs an explicit parameterized homotopy and bounds its Jacobian determinant, concluding by taking limits.

- **Lemma 7.** Let f : ½a; b -R be a continuous function, piecewise strictly monotone in ½a; b (with a finite number of monotonicity intervals) and such that f ðaÞof ðbÞ: Then there exists a partition a ¼ a0 oa1 o?oaN ¼ b of ½a; b such that, for every i ¼ 1; 2; y; N; either f is strictly increasing in ½ai 1 ; ai ; or f ðai 1 Þ ¼ f ðai Þ:
  *Proof:* (no proof in this paper)

- **Lemma 8.** Let v : ½0; 2p -G be a Lipschitz-continuous map, with G as in (4). Let a; bA½0; 2p ; aob; be such that Av x ðaÞ ¼ Av x ðbÞ: If Av x ðWÞ is piecewise strictly monotone in ½a; b (with a finite number of monotonicity intervals) then fðv1 ðWÞ   x1 Þv2W ðWÞ   ðv2 ðWÞ   x2 Þv1W ðWÞg dW ¼ 0:
  *Proof:* Uses an induction argument on the number of monotonicity intervals, showing the integral vanishes by comparing image areas of polar sectors.

- **Lemma 9.** Let v : ½0; 2p -G be a Lipschitz-continuous map, with G as in (4). Let Av x ðWÞ be piecewise strictly monotone in ½a; b (with a finite number of monotonicity intervals). For every e40; there exists a Lipschitz-continuous map w : B1 -R2 such that wð1; WÞ ¼ vðWÞ for every WA½0; 2p ; and jdet DwðxÞj dxoe þ 1 2 fv ðWÞvW ðWÞ   v ðWÞvW ðWÞg dW  :
  *Proof:* Partitions the interval and applies the umbrella lemma to constant intervals, integrating directly over the monotone ones.

- **Lemma 10.** Let uAW 1;N ðB1 ; R2 Þ: For every rAð0; 1 we have det DuðxÞ dx ¼ 1 2 u ðr; WÞ @u2 @W ðr; WÞ   u ðr; WÞ @u1 @W ðr; WÞ dW:
  *Proof:* (no proof in this paper)

- **Lemma 11.** Let u be a map satisfying the assumptions of Theorem 1. There exists a sequence Rj -0 such that lim u1 ðRj ; WÞ @u2 @W ðRj ; WÞ   u2 ðRj ; WÞ @u1 @W ðRj ; WÞ dW ¼ v1 ðWÞ dv2 dW ðWÞ   v2 ðWÞ dv1 dW ðWÞ dW:
  *Proof:* Selects radii using the tangential derivative bounds and uses weak convergence of the gradient sequence to pass to the limit.

- **Theorem 12 (The ‘‘eight’’ curve).** Let g ¼ gþ ,g CR2 be the union of the two circles of radius 1 with centers at ð1; 0Þ and at ð 1; 0Þ: Let v : ½0; 2p -g be a Lipschitz-continuous curve such that vð0Þ ¼ vð2pÞ: Let ðIj ÞjAN be a sequence of disjoint open intervals (possibly empty) of ½0; 2p such that the image vðIj Þ is contained either in gþ or in g ; and vðWÞ ¼ ð0; 0Þ when We jAN Ij : Then, if uðxÞ :¼ vðx=jxjÞ; the following upper estimate holds TVðu; B1 Þp 1 2 fv ðWÞvW ðWÞ   v ðWÞvW ðWÞg dW : Moreover, denoting by Ijþ any previous interval Ij such that vðIj ÞCgþ ; and by Ik any previous interval Ik such that vðIk ÞCg ; we have the following lower estimate TVðu; B1 Þp 1 2 fv vW   v vW g dW  þ fv vW   v vW g dW  :
  *Proof:* Establishes a lower bound utilizing dimension-free limits and interval-specific decompositions. Computes the upper bound by modifying the umbrella sequence to construct target functions handling opposing components separately.

- **Lemma 14.** Let w : ½0; 2p -gþ be a Lipschitz-continuous curve such that wð0Þ ¼ ð2; 0Þ: The real function RðWÞ :¼ w1 ðWÞw2W ðWÞ w2 ðWÞw1W ðWÞ jwðWÞj2 is bounded in ½0; 2p by a constant depending only on the Lipschitz constant of w: Moreover, setting Aw ðWÞ :¼ w1 ðtÞw2W ðtÞ   w2 ðtÞw1W ðtÞ jwðtÞj2 dt; then for every a; bA½0; 2p such that wðaÞað0; 0Þ and wðbÞað0; 0Þ; there exists kAZ such that Aw ðbÞ   Aw ðaÞ ¼ Arg wðbÞ   Arg wðaÞ þ kp:
  *Proof:* (no proof in this paper)

- **Lemma 15 (The ‘‘umbrella’’ lemma for the ‘‘eight’’ curve).** Let w : ½0; 2p -gþ be a Lipschitz-continuous curve. Assume that there exist a; bA½0; 2p ; aob; such that Aw ðaÞ ¼ Aw ðbÞ: Then for every e40 there exists a Lipschitz-continuous map w̃ : Sða; bÞ-R2 satisfying the boundary conditions w̃ð1; WÞ ¼ wðWÞ 8WA½a; b ; w̃ðR; aÞ ¼ RwðaÞ 8RA½0; 1 ; w̃ðR; bÞ ¼ RwðbÞ 8RA½0; 1 ; and such that jdet Dw̃ðxÞj dxoe:
  *Proof:* (no proof in this paper)

- **Lemma 16.** Let w : ½0; 2p -gþ be a Lipschitz-continuous map. If a; bA½0; 2p ; aob; are such that Aw ðaÞ ¼ Aw ðbÞ; and if the function Aw ðWÞ is piecewise strictly monotone in ½a; b (with a finite number of monotonicity intervals), then fw1 ðWÞw2W ðWÞ   w2 ðWÞw1W ðWÞg dW ¼ 0:
  *Proof:* Follows an area-comparison argument similar to Lemma 8 using strict monotonicity.

- **Lemma 17.** Let u : ½0; 2p -g ¼ gþ ,g be a Lipschitz-continuous map. Assume that there exist N disjoint open intervals Ij C½0; 2p such that uðIj Þ is contained either in gþ or in g for every j ¼ 1; 2; y; N; and uðWÞ ¼ ð0; 0Þ when We j¼1 Ij : Assume, in addition, that the function W-u1 ðWÞu2W ðWÞ   u2 ðWÞu1W ðWÞ has piecewise constant sign in ½0; 2p : Then, for every e40; there exists a Lipschitz-continuous map w̃ : B1 -R2 satisfying the boundary condition w̃ð1; WÞ ¼ uðWÞ for every WA½0; 2p ; and such that jdet Dw̃ðxÞj dxoe þ 1 2 fu ðWÞuW ðWÞ   u ðWÞuW ðWÞg dW :
  *Proof:* Applies the boundary-adjusted figure-eight umbrella map recursively across isolated loops and aggregates the variation bounds.

- **Theorem 21 (Lower semicontinuity below the critical exponent).** Let O be an open set of Rn : Let g : RN -R be a nonnegative convex function. Then lim inf gðMðDuh ÞÞ dxX gðMðDuÞÞ dx; for every sequence uh which converge to u in the weak topology of W 1;p ðO; Rn Þ for some p4n   1; with u; uh AWloc 1;n ðO; Rn Þ for every hAN:
  *Proof:* (no proof in this paper)

- **Lemma 22 (Lower bound—first estimate).** Let uALN ðO; Rn Þ-W 1;p ðO; Rn Þ-Wloc 1;N ðO\f0g; Rn Þ for some pAðn   1; nÞ: The following estimate holds TVðu; OÞX det DũðxÞ dx  ; whenever ũ : O-Rn is a Lipschitz-continuous map which agrees with u on the boundary of O; i.e., ũðxÞ ¼ uðxÞ on @O:
  *Proof:* Truncates approximating sequences uniformly to handle L-infinity behavior, and localizes onto inner annuli using cut-off functions. Bounds the resulting limits via algebraic minor inequalities and applies weak convergence.

- **Lemma 23 (Lower bound—second estimate).** Let u be a function of class LN ðO; Rn Þ-W 1;p ðO; Rn Þ-Wloc 1;N ðO\f0g; Rn Þ for some pAðn   1; nÞ: For every r40 such that Br CO the following estimate holds TVðu; OÞX jdet DuðxÞj dx þ det DũðxÞ dx  ; where ũ : Br -Rn is any Lipschitz-continuous map which coincides with u on the boundary of Br ; i.e., ũðxÞ ¼ uðxÞ on @Br :
  *Proof:* Splits the limit integral between the ball and its complement, applying Lemma 22 inside and classical lower semicontinuity outside.