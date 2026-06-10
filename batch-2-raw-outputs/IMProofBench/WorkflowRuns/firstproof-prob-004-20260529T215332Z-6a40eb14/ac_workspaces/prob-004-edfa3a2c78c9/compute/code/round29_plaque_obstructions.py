#!/usr/bin/env python3
"""Round 29 checks for the LE-HAF plaque route.

This script records two elementary stress tests:

1. The local affine model from the Manhattan-sweep obstruction.  It satisfies
   Dil_2 = 1, but a literal coordinate sweep costs order 1 while the visible
   low-G energy plus averaged exact-plaque bad probability is order L^{-2}.

2. A rank-one oscillatory/comb plaque.  Exact plaque images have zero
   two-dimensional measure, but any delta-neighborhood/cell-star thickening at
   the natural mesh scale covers a fixed fraction of the parameter square.
   This is why the bad set must use exact coordinate plaques if one wants the
   Fubini estimate from J_2 F.
"""

from __future__ import annotations


def local_sweep_rows():
    rows = []
    for L in [10, 30, 100, 300, 1000, 3000]:
        dil2 = 1.0
        lambda_sq = L ** -2
        bad_probability = L ** -2
        track_density = 1.0
        ratio = track_density / (lambda_sq + bad_probability)
        rows.append((L, dil2, lambda_sq, bad_probability, track_density, ratio))
    return rows


def comb_rows():
    """Return exact and thickened bad fractions for a comb plaque.

    Let Q=[0,1]^2 and let gamma_N be the union of N vertical segments, one in
    each strip of width 1/N.  A rank-one plaque map F(u,v)=gamma_N(u) has
    J_2 F = 0, so exact image area is zero.  The delta-neighborhood with
    delta = c/N contains the union of N vertical strips of total width
    min(1, 2c), ignoring only harmless endpoint effects.  This lower bound is
    rigorous for the vertical portions alone.
    """
    rows = []
    for N in [10, 30, 100, 300, 1000]:
        for c in [1 / 6, 1 / 4, 1 / 3]:
            delta = c / N
            exact_area = 0.0
            thickened_lower = min(1.0, 2 * c)
            # If a cell-star rule marks every square of side comparable to
            # delta that meets the image, it has at least this same order.
            rows.append((N, c, delta, exact_area, thickened_lower))
    return rows


def main():
    print("# Round 29 plaque-route obstruction checks")
    print()
    print("## Local coordinate-sweep obstruction")
    print("| L | Dil_2 | lambda^2 | bad probability | track density | ratio |")
    print("|---:|---:|---:|---:|---:|---:|")
    for row in local_sweep_rows():
        L, dil2, lambda_sq, bad_probability, track_density, ratio = row
        print(
            f"| {L} | {dil2:.0f} | {lambda_sq:.6g} | "
            f"{bad_probability:.6g} | {track_density:.0f} | {ratio:.6g} |"
        )
    print()
    print("Model: T=span(e3,e4), dF(e1)=L, dF(e2)=L^{-1},")
    print("dG(e3)=dG(e4)=L^{-1}; singular values are L,L^{-1},L^{-1},L^{-1}.")
    print()
    print("## Thickened plaque/cell-star obstruction")
    print("| N | c in delta=c/N | delta | exact image area | thickened area lower bound |")
    print("|---:|---:|---:|---:|---:|")
    for row in comb_rows():
        N, c, delta, exact_area, thickened_lower = row
        print(
            f"| {N} | {c:.6g} | {delta:.6g} | "
            f"{exact_area:.0f} | {thickened_lower:.6g} |"
        )
    print()
    print("Comb model: F(u,v)=gamma_N(u), where gamma_N runs along N vertical")
    print("segments in Q=[0,1]^2.  J_2 F=0, but a delta-neighborhood with")
    print("delta=c/N covers at least min(1,2c) of Q.")


if __name__ == "__main__":
    main()
