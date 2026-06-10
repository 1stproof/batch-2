#!/usr/bin/env python3
"""A concrete PL chart where exact-plaque badness is not f-saturated.

Two disjoint cubical charts have coordinates (u,v,s,t).  The central
horizontal squares A and A' are {s=t=0}.  On both central squares

    f(u,v,0,0) = (u,v,0,0),

so the two oriented 2-cells have the same cellular push-forward.  The
transverse F=(f_3,f_4) behaviour differs:

    F_A(s,t)  = (s,t),
    F_A'(s,t) = eps (s,t).

Thus, for eps << |z| < 1, the exact transverse coordinate plaque through A
contains z in its F-image, while the corresponding plaque through A' does not.
Both affine pieces have 2-dilation at most 1 in the normalized Euclidean
coordinates used here.
"""

from __future__ import annotations


def two_dilation(diagonal: tuple[float, float, float, float]) -> float:
    s = sorted((abs(x) for x in diagonal), reverse=True)
    return s[0] * s[1]


def in_square(z: tuple[float, float], radius: float) -> bool:
    return abs(z[0]) <= radius and abs(z[1]) <= radius


def main() -> None:
    eps = 0.1
    z = (0.5, 0.25)

    dil_A = two_dilation((1, 1, 1, 1))
    dil_Ap = two_dilation((1, 1, eps, eps))
    bad_A = in_square(z, 1.0)
    bad_Ap = in_square(z, eps)
    exact_prob_Ap = eps**2
    saturated_prob_Ap = 1.0

    lines = [
        "# Round 34 PL plaque-saturation model",
        "",
        "Charts: A uses f=(u,v,s,t); A' uses f=(u,v,eps s,eps t).",
        f"epsilon = {eps}, z = {z}",
        "",
        "| sheet | f on central square | transverse F-plaque image | Dil_2 | z-bad? |",
        "|---|---|---|---:|---|",
        f"| A | (u,v,0,0) | [-1,1]^2 | {dil_A:.6g} | {'yes' if bad_A else 'no'} |",
        f"| A' | (u,v,0,0) | [-eps,eps]^2 | {dil_Ap:.6g} | {'yes' if bad_Ap else 'no'} |",
        "",
        "Both central 2-cells push forward to the same target square P, but",
        "the exact-plaque bad set for z contains A and not A'.",
        "",
        "If badness is saturated over the f-equivalence A~A', then A' is",
        "declared bad for every z in the large A-plaque image.  In this",
        "normalized chart the exact average bad probability of A' is",
        f"eps^2 = {exact_prob_Ap:.6g}, while the saturated probability is",
        f"{saturated_prob_Ap:.6g}, a loss factor {saturated_prob_Ap / exact_prob_Ap:.6g}.",
    ]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
