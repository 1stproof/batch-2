# Compute worker reply — round 33
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c2-07bcb6/compute_workspace_round_33.zip

---

# Round 33 response: status of `(EAT)`

## Verdict

I do **not** have a proof of the current primal `(EAT)`, and I did **not** find a genuine degree-one hard-regime counterexample map.  The precise conclusion is:

**The algebra after `(EAT)` is correct, but the current formulation still needs a boundary-compatible correction or an extra null-respecting carrier lemma.**  The first missing sublemma is now very explicit: a source-side exact-plaque deformation must preserve the quotient by \(f\)-null boundaries.  Standard cellular/acyclic-carrier deformations do not do this.

Round-specific files:

- `code/round33_eat_diagnostic.py`
- `data/round33/eat_diagnostic.txt`
- `data/round33/eat_boundary_diagnostic.tex`

## 1. Conditional algebra checked

Let \(q=|Q|\sim S_3S_4\) and
\[
A_\Omega=\int_\Omega \EFill_f(y)\,dy,\qquad
\Omega=\{y:E_y\le 4I/q\}.
\]
Assume `(EAT)`:
\[
A_\Omega
\le C\left(R_1I+\frac{I^2}{S_1q}\right)
+\frac{C}{q}\int_Q\int_\Omega
       \Mass(C_y^0\llcorner{\mathcal B}_z)\,dy\,dz .
\]
The exact-plaque Fubini estimate gives, for the near-minimizers
\(\Mass C_y^0\le 2\EFill_f(y)\),
\[
\frac1q\int_Q\int_\Omega
\Mass(C_y^0\llcorner{\mathcal B}_z)\,dy\,dz
\le C\frac{R_3R_4}{S_3S_4}A_\Omega .
\]
Thus, if \(R_3R_4\le \kappa S_3S_4\) with \(\kappa\) small, the bad term is absorbed:
\[
A_\Omega\le C\left(R_1I+\frac{I^2}{S_1q}\right).
\]
The calibration lower bound gives
\[
A_\Omega\ge cS_1S_2S_3q\gtrsim S_1S_2S_3^2S_4.
\]
If also \(R_1\le\kappa S_1\) and
\[
I\le \delta S_1S_2^{1/2}S_3^{3/2}S_4,
\]
then
\[
R_1I\le C\kappa\delta S_1S_2S_3^2S_4,\qquad
\frac{I^2}{S_1q}\le C\delta^2S_1S_2S_3^2S_4
\]
using \(S_1\le S_2\le S_3\).  Taking \(\delta,\kappa\) small contradicts the lower bound.  Hence
\[
I\gtrsim S_1S_2^{1/2}S_3^{3/2}S_4,
\]
and the weighted coarea estimate \(I\lesssim \Vol(R)\) gives the desired volume alternative.

Hidden assumptions in this algebra:

- regular values/nonregular values are discarded measure-theoretically;
- a measurable near-minimizing selection \(C_y^0\) is available, or the argument is run with \(\varepsilon\)-minimizers and outer integrals;
- the low-energy restriction to \(\Omega\) is what justifies replacing \(\int_\Omega E_y^2/S_1\) by \(I^2/(S_1q)\);
- the exact-plaque Fubini estimate uses exact coordinate plaques, not thickened cells.

The diagnostic script records the normalized stress scale \(S=(1,1,L,L)\), \(R=(L^{-1/5},L^{13/15},L^{13/15},L^{13/15})\).  In that scale \(A_\Omega\) has exponent \(3\), while the minimal-energy terms have exponents \(9/5\) and \(2\), and the absorbed bad term has exponent \(41/15\).  So `(EAT)` is exactly strong enough to close the known exponent gap.

## 2. Boundary-compatibility obstruction

Set
\[
W_y=\partial C_y^0,\qquad
Z_y=\langle [[R]],F,y\rangle,\qquad
N_y=W_y-Z_y .
\]
Then
\[
f_\#W_y=\pm P_y=f_\#Z_y,\qquad f_\#N_y=0.
\]
The problem is that \(E_y\) controls \(Z_y\), not \(W_y\).

Suppose one tries the old source-chain-map skeleton.  Let \(P_z,H_z\) satisfy
\[
\partial H_z(T)+H_z(\partial T)=P_z(T)-T.
\]
The natural candidate using the near-minimizer \(C_y^0\) and the actual slice \(Z_y\) is
\[
D_{y,z}=P_z(C_y^0)-H_z(Z_y).
\]
Then
\[
\partial D_{y,z}
=P_zW_y-(P_zZ_y-Z_y)
=Z_y+P_zN_y.
\]
After pushing forward,
\[
f_\#\partial D_{y,z}=P_y+f_\#P_zN_y.
\]
Thus \(D_{y,z}\) is an admissible essential filling only if
\[
f_\#P_zN_y=0
\]
or if this defect has a filling paid by the displayed RHS of `(EAT)`.

This is the first exact missing sublemma:
\[
\boxed{\quad f_\#N=0\Longrightarrow f_\#P_zN=0
\text{ for the exact-plaque carrier }P_z,\quad}
\]
together with
\[
\Mass P_z(C_y^0)\lesssim \Mass(C_y^0\llcorner{\mathcal B}_z),\qquad
\Mass H_z(Z_y)\lesssim R_1E_y+E_y^2/S_1.
\]
Standard source-local cellular maps do not preserve \(f\)-nullity.  The toy obstruction is two oppositely oriented sheets \(N=A-A'\) with identical \(f\)-image, so \(f_\#N=0\).  A local projection that keeps \(A\) and kills \(A'\) gives \(f_\#P_zN=f_\#A\), of full target area.  This is saved numerically/scalewise in `data/round33/eat_diagnostic.txt`.  It is not a hard-regime counterexample map, but it rules out the naive acyclic-carrier proof.

Using \(H_z(W_y)\) instead of \(H_z(Z_y)\) avoids this boundary defect, but then the homotopy mass must be controlled by the energy of \(W_y\), which is not bounded by \(E_y\).  That is exactly the boundary-compatibility issue.

## 3. Most promising corrected formulation

The cleanest correction I see is a dual essential estimate.  Define
\[
\EFill_f^\vee(y)=
\sup\left\{
  \langle P_y,\eta\rangle:
  \eta\in{\mathcal D}^2(S,\partial S),\
  \|f^*d\eta\|_\infty\le1
\right\}.
\]
For real normal currents this is the Hahn--Banach dual of the primal mass minimization
\[
\inf\{\Mass C:\partial f_\#C=\pm P_y\};
\]
for integral currents, this should be treated as the relaxed dual norm unless an integrality/no-gap argument is supplied.  The same calibration lower bound survives.

The corrected target is:
\[
\int_\Omega \langle P_y,\eta_y\rangle\,dy
\le
C\left(R_1I+\frac{I^2}{S_1q}\right)
+\frac{C}{q}\int_Q\int_\Omega
   \int_{C_y^0\llcorner{\mathcal B}_z}|f^*d\eta_y|\,dy\,dz .
\tag{EAT^\vee}
\]
Here \(\eta_y\) is a measurable near-dual family.  This formulation is boundary-compatible because
\[
\langle P_y,\eta_y\rangle
=\langle Z_y,f^*\eta_y\rangle
=\langle \partial C_y^0,f^*\eta_y\rangle;
\]
the discrepancy \(N_y=\partial C_y^0-Z_y\) is invisible to target pullback cochains.  Since \(|f^*d\eta_y|\le1\), the bad term is bounded by the same exact-plaque mass term used in the draft, so the absorption algebra is unchanged.

This is still unproved, but it is a corrected formulation of the missing estimate: the carrier/cochain homotopy must act in the quotient by \(f\)-null boundaries.  The current primal `(EAT)` can remain as a conditional reduction only if it is supplemented by the boxed null-respecting carrier lemma above, or replaced by the dual statement `(EAT^\vee)`.

## Recommendation for `answer.tex`

Do not present `(EAT)` as established.  I would change the “Remaining open issues” paragraph to say that the missing estimate is not merely an averaged tightening, but an averaged tightening **in the quotient by \(f\)-null boundary discrepancies**.  The insertable diagnostic/corrected statement is in:

`data/round33/eat_boundary_diagnostic.tex`.
