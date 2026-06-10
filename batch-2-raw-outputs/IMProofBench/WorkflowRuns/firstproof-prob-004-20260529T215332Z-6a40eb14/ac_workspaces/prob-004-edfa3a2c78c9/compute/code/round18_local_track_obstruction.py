"""Local scaling obstruction for a naive weighted Manhattan estimate.

This is not a counterexample to equation (13).  It isolates the first
pointwise estimate one would like in a coordinate-plaque proof and shows that it
is false.

At a point of a fiber Z_y take the tangent plane T = span(e3,e4), and take a
linear differential with singular values

    dF(e1)=L, dF(e2)=L^{-1}, dG(e3)=L^{-1}, dG(e4)=L^{-1}.

Then Dil_2 = 1 and lambda^2 on T is L^{-2}.  Sweeping the e3e4 sheet in the
x1 direction has unit directional track density, while the weighted density is
only L^{-2}.  If the parameter square Q has area q=L^2, the relevant coordinate
plaque F(P_12) has area 1, so the averaged bad-puncture probability is also
L^{-2}.  Thus a local bound

    track_density <= C (lambda^2 + bad_probability)

fails by a factor comparable to L^2.
"""

from __future__ import annotations


def row(L: float) -> tuple[float, float, float, float, float, float]:
    dil2 = 1.0
    lambda_sq = L ** -2
    track_density = 1.0
    q = L**2
    bad_probability = 1.0 / q
    ratio = track_density / (lambda_sq + bad_probability)
    return L, dil2, lambda_sq, bad_probability, track_density, ratio


def main() -> None:
    print(
        "L dil2 lambda_sq bad_probability track_density "
        "track/(lambda_sq+bad_probability)"
    )
    for L in (10.0, 30.0, 100.0, 300.0, 1000.0):
        print("%g %.6g %.6g %.6g %.6g %.6g" % row(L))

    print()
    print("Asymptotic ratio = L^2/2 for q=L^2.")


if __name__ == "__main__":
    main()
