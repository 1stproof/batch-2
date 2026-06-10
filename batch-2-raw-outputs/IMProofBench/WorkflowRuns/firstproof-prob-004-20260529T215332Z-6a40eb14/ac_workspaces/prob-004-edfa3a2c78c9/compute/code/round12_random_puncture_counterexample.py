"""Scaling check for the random-puncture deformation lemma.

Example:
    R = [0,1] x [0,L^2] x [0,L^2] x [0,L^2]
    S = [0,1] x [0,1] x [0,L] x [0,L]
    f(x1,x2,x3,x4) = (x3/L^2, x4/L^2, L*x1, x2/L).

Then Dil_2(f)=1 and f has degree +/-1 as a map of pairs.  For the
central Q in the last two target coordinates, F=(f3,f4) is independent
of the vertical C coordinates, so Z_y is a full vertical rectangle.
The bad set for a point z is a single vertical rectangle, hence it has
zero 3-dimensional mass inside any rectifiable 3-filling.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Scaling:
    L: float
    q: float
    mass_Z: float
    fill_per_y_lower: float
    A_lower: float
    E_y: float
    I: float
    rhs_no_bad: float
    ratio_A_to_rhs: float
    singular_values: tuple[float, float, float, float]
    dil2: float


def compute(L: float) -> Scaling:
    # Central Q = [L/3,2L/3]^2.
    q = (L / 3.0) ** 2
    mass_Z = L**4

    # For y in central Q, u=(y3/L, L*y4) lies at distance >=1/3 from
    # the x1-boundary of B and >=L^2/3 from the x2-boundary.
    # The calibration d(phi dx3 dx4), with phi=dist_to_boundary(B)
    # truncated smoothly, gives Fill_R(Z_y) >= (1/3)*L^4.
    fill_per_y_lower = (1.0 / 3.0) * L**4
    A_lower = q * fill_per_y_lower

    # On Z_y, dG has operator norm 1/L^2, so lambda^2=1/L^4.
    E_y = mass_Z / L**4
    I = q * E_y

    # S1=R1=1.  The proposed controlled part is R1*I + I^2/(S1*q).
    rhs_no_bad = I + I**2 / q
    ratio = A_lower / rhs_no_bad

    singular_values = tuple(sorted((L, 1.0 / L, 1.0 / L**2, 1.0 / L**2), reverse=True))
    dil2 = singular_values[0] * singular_values[1]
    return Scaling(
        L=L,
        q=q,
        mass_Z=mass_Z,
        fill_per_y_lower=fill_per_y_lower,
        A_lower=A_lower,
        E_y=E_y,
        I=I,
        rhs_no_bad=rhs_no_bad,
        ratio_A_to_rhs=ratio,
        singular_values=singular_values,
        dil2=dil2,
    )


def main() -> None:
    print("L q mass_Z fill_y_lower A_lower E_y I rhs_no_bad A/rhs dil2 singular_values")
    for L in (10.0, 30.0, 100.0, 300.0, 1000.0):
        s = compute(L)
        print(
            f"{s.L:g} {s.q:.6g} {s.mass_Z:.6g} {s.fill_per_y_lower:.6g} "
            f"{s.A_lower:.6g} {s.E_y:.6g} {s.I:.6g} {s.rhs_no_bad:.6g} "
            f"{s.ratio_A_to_rhs:.6g} {s.dil2:.6g} {s.singular_values}"
        )

    print()
    print("Asymptotics:")
    print("  q ~ L^2/9, Mass(Z_y)=L^4, Fill(Z_y) >= L^4/3")
    print("  A >= L^6/27, E_y=1, I=L^2/9")
    print("  R1*I + I^2/(S1*q) = 2L^2/9")
    print("  A / controlled_RHS >= L^4/6")
    print("  For each z, B_z={u_z}xC is 2-dimensional, so the restriction")
    print("  of any rectifiable 3-filling to B_z has zero 3-mass.")


if __name__ == "__main__":
    main()
