#!/usr/bin/env python3
"""Round 33 scale checks for the essential averaged tightening estimate.

This is not a search for maps.  It records the algebraic consequences of
EAT in the normalized high-aspect stress scale S=(1,1,L,L), and it records
the size of the f-null compatibility gap in a toy chain-level model.
"""

from __future__ import annotations


def stress_rows():
    """Return exponents for the formal hard stress scale.

    In the stress model used throughout the run,
        S=(1,1,L,L),
        R=(L^{-1/5}, L^{13/15}, L^{13/15}, L^{13/15}).
    The desired volume exponent is 5/2 and the formal source volume exponent
    is 12/5, so a proof needs to rule this scale out.  If I were only of the
    minimal slice-energy scale q*S1*S2=L^2, EAT would fail by a factor L.
    """

    return {
        "S1": 0.0,
        "S2": 0.0,
        "S3": 1.0,
        "S4": 1.0,
        "q=|Q|": 2.0,
        "target A_lower=S1*S2*S3*q": 3.0,
        "minimal_slice_energy_I=q*S1*S2": 2.0,
        "R1": -1.0 / 5.0,
        "R3R4": 26.0 / 15.0,
        "R1*I_min": 9.0 / 5.0,
        "I_min^2/(S1*q)": 2.0,
        "(R3R4/S3S4)*A_lower": 41.0 / 15.0,
        "desired_volume": 2.5,
        "formal_source_volume": 12.0 / 5.0,
    }


def null_gap_rows():
    """A toy f-null discrepancy showing what a source carrier must preserve.

    Let N=A-A' be two oppositely oriented sheets with the same f-image, so
    f_#N=0.  A local source projection/restriction that keeps A and kills A'
    produces f_#P(N)=f_#A, of full target area.  Thus any EAT proof based on a
    source chain operator needs an extra null-respecting property; f_#N=0 alone
    is not stable under support-local exact-plaque operations.
    """

    rows = []
    for area in [1, 10, 100, 1000]:
        before = 0
        after = area
        rows.append((area, before, after))
    return rows


def main():
    print("# Round 33 EAT diagnostic")
    print()
    print("## Normalized stress-scale exponents")
    print("| quantity | L-exponent |")
    print("|---|---:|")
    for key, value in stress_rows().items():
        print(f"| {key} | {value:.6g} |")
    print()
    print(
        "Interpretation: with only minimal slice energy I~L^2, the EAT left "
        "side is L^3.  In the hard stress scale, the two energy terms are "
        "L^{9/5} and L^2, and the averaged bad term is at most L^{41/15}; "
        "hence EAT would force extra energy and exactly closes the theorem."
    )
    print()
    print("## f-null discrepancy toy model")
    print("| sheet target area | f_#N before projection | f_#P(N) after one-sided projection |")
    print("|---:|---:|---:|")
    for area, before, after in null_gap_rows():
        print(f"| {area} | {before} | {after} |")
    print()
    print(
        "This is only a chain-level obstruction to proof strategies, not a "
        "degree-one hard-regime map.  It identifies the missing sublemma: an "
        "exact-plaque carrier must act on the quotient by f-null boundaries, "
        "or the argument must be phrased dually using target pullback cochains."
    )


if __name__ == "__main__":
    main()
