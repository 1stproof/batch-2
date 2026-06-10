# Round 37 quotient-dual derivation attempt

This note records the finite-dimensional Hahn--Banach calculation and the
target-pullback homotopy route I tried.  It is not a complete proof of QEAT.

## 1. Quotient duals

Let `F_k:C_k^src -> C_k^tar` denote the cellular push-forward.  In finite
dimension

```
Q_k = C_k^src / ker(F_k)  is isomorphic to im(F_k).
```

A quotient `k`-cochain is therefore a target cochain on `im(F_k)`, pulled back
by `F_k`.  For a target boundary `p_y`, the relaxed essential filling LP is

```
EFill_f(y) = min sum_i m_i |c_i|
             subject to F_2 d_src c = p_y.
```

The dual is

```
EFill_f(y) = max <psi,p_y>
             subject to |<F_2^* psi, d_src sigma_i>| <= m_i
             for every source 3-cell sigma_i.
```

Equivalently, after moving the coboundary,

```
|<F_3^* delta psi, sigma_i>| <= m_i.
```

This is the finite cellular version of using target-pullback quotient
cochains from the start.

## 2. Dual of beta_z

For a fixed quotient class represented by the target 3-chain `t=F_3 C`, the
bad seminorm is

```
beta_z(t) = min sum_i w_i(z) |d_i|
            subject to F_3 d = t,
```

where `w_i(z)` is the mass of the part of source cell `sigma_i` lying in the
exact plaque bad set.  Linear programming duality gives

```
beta_z(t) = max <lambda,t>
            subject to |<F_3^* lambda, sigma_i>| <= w_i(z)
            for every source 3-cell sigma_i.
```

This is the useful certificate pattern:

```
residual lambda is allowed only if its pullback is supported/bounded by the
exact bad mask on every source representative of the same target chain.
```

For two `f_#`-equivalent sheets `A,A'` with `F_3 A=F_3 A'=T`, if `A'` is
nonbad then the constraint on `A'` says `|lambda(T)|<=0`, so no nonzero
residual can be charged to `T` even if `A` itself is bad.  This is exactly why
source-local restriction fails and why the quotient seminorm is the right
residual quantity.

## 3. Homotopy identity needed for QEAT

The desired dual form of QEAT can be stated as follows.  For each admissible
dual `psi` with `||F_3^* delta psi||_* <= 1`, and for a.e. `y,z`, construct a
target-pullback decomposition

```
<psi, P_y> = <delta psi, T^reg_{y,z}> + <lambda_{y,z}, F_3 C_y^0>,
```

such that

```
Mass_src(T^reg_{y,z}) <= C (R_1 E_y + E_y^2/S_1),
|<F_3^* lambda_{y,z}, sigma>| <= 1_{sigma in B_z} Mass(sigma).
```

Then the first term is bounded by the regular homotopy mass, and the second
term is bounded by `beta_z([C_y^0])` by the dual formula above.

## 4. Target Green operator route

The only route I see that naturally preserves the quotient is target-side.
For the parameter square `Q`, choose a singular one-form or vector-field kernel
`eta_z` with

```
d eta_z = delta_z - q^{-1} dy_3 dy_4
```

and with tangential boundary normalization.  Pull back by `F=(f_3,f_4)`.  Since
the construction uses `F` and target cochains, it automatically respects
`ker f_#`.

The singular part is supported exactly where the pulled-back coordinate
plaque through a source point sees `z`; this is the exact plaque bad set
`B_z`, not a thickened star.  This is the main advantage over cubical
deformation operators.

The missing estimate is the regular kernel bound.  One would need an averaged
inequality of the schematic form

```
int_Omega int_Q |regular sweep made by F^* eta_z on Z_y| dz dy
    <= C (R_1 I + I^2/(S_1 q)).
```

The plausible mechanism is:

1. the linear-in-energy term `R_1 E_y` comes from sweeping in the short source
   direction after one integration by parts;
2. the quadratic term `E_y^2/S_1` comes from the `L^2` part of the Green
   kernel after applying the good-slice bound `E_y <= 4I/q`;
3. the singular delta contribution is left as the beta-dual residual above.

I was not able to close this kernel estimate.  The obstruction is that the
natural Green kernel has a `1/|w-z|` singularity, and a direct absolute-value
bound either loses a logarithm or charges a thickened bad set.  The exact
plaque statement needs a principal-value/Stokes cancellation that I have not
made rigorous.

## 5. Current conclusion

The finite dual calculation strongly constrains what a proof can look like:
the residual must be a target cochain whose pullback vanishes on all nonbad
representatives.  This supports the target-pullback Green-operator route and
rules out purely source-local exact-plaque projections, but it is still only a
proof route, not a proof of QEAT.
