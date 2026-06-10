# Compute worker reply — round 34
status: done
error: (none)
workspace: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/ac_workspaces/prob-004-edfa3a2c78c9/compute
zip: /data/output/workflow_runs/firstproof-prob-004-20260529T215332Z-6a40eb14/agents/Compute-c3-5fb124/compute_workspace_round_34.zip

---

# Round 34 response: `(QEAT)` quotient tightening

## Verdict

I did **not** prove `(QEAT)`, and I did **not** find a genuine counterexample to the rectangle theorem or to `(QEAT)` as a black-box estimate.  I did find a concrete finite obstruction to the natural proof strategy requested in the prompt:

> A source-local exact-plaque carrier/cochain homotopy does not descend to
> \(N_\ast(R,\partial R)/\ker f_\#\) unless it preserves \(f\)-null chains.
> Making it quotient-preserving forces nonlocal \(f\)-saturation/transfer, and
> that destroys the exact bad-mass estimate used in `(QEAT)`.

Round files:

- `code/round34/quotient_obstruction.py`
- `data/round34/quotient_obstruction.txt`
- `code/round34/plaque_saturation_model.py`
- `data/round34/plaque_saturation_model.txt`
- `data/round34/qeat_obstruction_insert.tex`
- `data/round34/lit_search_note.md`

## Quotient setup

In a finite cubical model, put
\[
Q_\ast=C_\ast(R,\partial R;\mathbb R)/\ker f_\# .
\]
Equivalently \(Q_\ast\simeq \operatorname{im} f_\#\).  A source cochain descends to the quotient iff it annihilates \(\ker f_\#\).  A source chain operator \(P_z\) induces an operator on the quotient only if
\[
        P_z(\ker f_\#)\subseteq \ker f_\# .
\]
The same condition is needed in the dual construction: if \(\phi\) is a quotient cochain, then \(P_z^\ast\phi\) is again a quotient cochain only under this kernel-preservation condition.

The usual source-chain proof skeleton would use
\[
        \partial H_z(T)+H_z(\partial T)=P_zT-T
\]
and then, for an essential filling \(C_y^0\),
\[
        [Z_y]=\partial\big([P_zC_y^0]-[H_zZ_y]\big)
\]
in the quotient.  This implication requires \(P_z(\partial C_y^0-Z_y)\in\ker f_\#\).  Thus the old boundary-compatibility problem has not disappeared; it has become exactly the condition that the carrier descend to \(Q_\ast\).

## Finite obstruction

Take a relative cubical \(2\)-complex with two oriented \(2\)-cells \(A,A'\), and a target \(2\)-complex with one cell \(P\).  Define
\[
        f_\#A=P,\qquad f_\#A'=P.
\]
Then \(A-A'\in\ker f_\#\), and quotient \(2\)-cochains are precisely vectors \((x,x)\) on the ordered basis \((A,A')\).

Assume the exact-plaque bad set for a puncture \(z\) contains \(A\) but not \(A'\).  The source-local bad-cell projection is
\[
        P_{\rm bad}=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
With \(f_\#=(1\;1)\) and \(N=A-A'\), the script computes
\[
        f_\#P_{\rm bad}N=-P\ne0.
\]
So \(P_{\rm bad}\) does not preserve \(\ker f_\#\).  Dually, for the quotient cochain \(\phi=(1,1)\),
\[
        P_{\rm bad}^\ast\phi=(1,0),
\]
which does not annihilate \(A-A'\).  Hence the cochain homotopy cannot be a quotient cochain homotopy.

The exact output is in `data/round34/quotient_obstruction.txt`; the key table is:

| exact-plaque mask on \((A,A')\) | descends to quotient? |
|---|---|
| \((0,0)\) | yes |
| \((1,0)\) | no |
| \((0,1)\) | no |
| \((1,1)\) | yes |

Thus a diagonal/source-local exact-plaque mask descends only when it is constant on the whole \(f\)-equivalence class.

There is a nonlocal way to preserve the quotient: send both \(A\) and \(A'\) to \(A\).  Matrix-wise,
\[
        T_{\rm bad}=\begin{pmatrix}1&1\\0&0\end{pmatrix}
\]
does carry \(A-A'\) to zero.  But it violates exact bad localization: \(A'\cap{\mathcal B}_z=\emptyset\), while \(T_{\rm bad}A'=A\) has positive mass.  This is the basic tradeoff.

## PL realization of nonsaturated badness

The obstruction is not just formal.  It is realized by two disjoint cubical charts with coordinates \((u,v,s,t)\).  Let the central squares be \(A=A'=\{s=t=0\}\) in their respective charts.  On both central squares set
\[
        f(u,v,0,0)=(u,v,0,0),
\]
so both push forward to the same target square \(P\).

Extend transversely by
\[
        F_A(s,t)=(s,t),\qquad F_{A'}(s,t)=\varepsilon(s,t),
\]
where \(F=(f_3,f_4)\).  Both affine pieces have \(\operatorname{Dil}_2\le1\) in this normalized chart.  For \(z\) with \(\varepsilon\ll |z|<1\), the exact transverse coordinate plaque through \(A\) contains \(z\), while the corresponding plaque through \(A'\) does not.  Therefore \({\mathcal B}_z\) is not saturated under the relation \(A\sim A'\) induced by \(f_\#\).

If one forcibly saturates badness over \(A\sim A'\), the Fubini estimate can fail.  In the model, the exact average bad probability of \(A'\) is \(\varepsilon^2\), but the saturated bad probability is \(1\), a loss factor \(\varepsilon^{-2}\).  This is saved in `data/round34/plaque_saturation_model.txt`.

## Consequence for the requested cochain identity

The literal identity
\[
        \phi=K_z\delta\phi+\Pi_z\phi+\delta L_z\phi
\]
cannot be obtained by a source-local exact-plaque residual supported on a nonsaturated bad set.  In the two-cell relative complex above there are no \(1\)- or \(3\)-cells, so \(\delta\phi=0\) and \(\delta L_z\phi=0\).  The identity would reduce to \(\phi=\Pi_z\phi\).  But the only quotient cochain supported in the nonsaturated bad set \(\{A\}\) is zero, because quotient cochains must have equal values on \(A\) and \(A'\).

This does not disprove every possible variant of `(QEAT)`.  It rules out the standard source-local Federer--Fleming/Guth carrier route unless a new nonlocal quotient-localization mechanism is supplied.

## Minimal missing sublemma

A proof of `(QEAT)` would need something like the following, which is stronger than standard deformation theorems.

**Quotient exact-plaque carrier lemma.**  For a.e. \(z\), for each relevant slice \(Z_y\), and for each near-minimizing quotient filling \(C_y^0\), there are quotient-level operators/lifts such that, in \(Q_\ast\),
\[
        [Z_y]=\partial\big(P_z^Q[C_y^0]-H_z^Q[Z_y]\big),
\]
with
\[
        \Mass H_z^Q[Z_y]\le C\left(R_1E_y+\frac{E_y^2}{S_1}\right),
\]
and with a source lift satisfying
\[
        \Mass P_z^Q[C_y^0]\le C\,\Mass(C_y^0\llcorner{\mathcal B}_z).
\]
Equivalently in dual form, the homotopy must send quotient cochains to quotient cochains and its residual coboundary must pair only with the exact bad part of the chosen source representative \(C_y^0\).

Standard Federer--Fleming or Guth cellular carriers do not give this lemma.  They are source-local and preserve geometric skeleta/neighborhoods, not the equivalence relation generated by \(\ker f_\#\).  If modified to be quotient-invariant by saturating over \(f\)-equivalence classes, the exact-plaque Fubini estimate can be lost by the \(\varepsilon^{-2}\) example above.

## Literature check

Only a light secondary search was run because round 32 already did the heavy retrieval.  I found no source stating `(QEAT)` or the desired 4D rectangle \(2\)-dilation theorem.  The search again points only to known adjacent sources: Guth’s *Area-expanding embeddings of rectangles* (arXiv:0710.0403), Guth’s *The width-volume inequality*, Guth’s thesis title *Area-Contracting Maps between Rectangles*, and the SLMath 2011 abstract *Contraction of Areas and Homotopy Types of Mappings*.  Details are in `data/round34/lit_search_note.md`.

## Recommendation for `answer.tex`

Keep `(QEAT)` as a conditional missing estimate, but sharpen the open issue.  The missing input is not merely a quotient formulation; it is a quotient-equivariant exact-plaque carrier that remains localized to the unsaturated exact bad set.  The insertable obstruction lemma in `data/round34/qeat_obstruction_insert.tex` is suitable for the “Remaining open issues” section if the draft wants to document why standard carriers are insufficient.
