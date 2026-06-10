"""Round 32 product-flap exponent checks for the averaged tightening gap.

This is not a proof engine.  It records the bookkeeping for the most obvious
low-G-energy null-sheet/flap counterexamples to (AT).

Normalize S=(1,1,L,L), so the central parameter square Q has area q=L^2.
Write R_i=L^{r_i} with r1<=r2<=r3<=r4.  The hard regime is
    r1 < 0,  r3+r4 < 2.

A coordinate-product flap family has a two-dimensional sheet factor and a
two-dimensional normal parameter factor on which F=(f3,f4) covers Q with
bounded 2-dilation.  Since J_2 F <= C, the normal coordinate product must have
exponent at least 2.  But every coordinate two-product is <= R3 R4, hence has
exponent <= r3+r4<2.  Therefore all coordinate-product flap families are
blocked in the hard regime.
"""

from __future__ import annotations

from itertools import combinations


def product_exponents(r: tuple[float, float, float, float]) -> list[tuple[str, float, bool]]:
    out = []
    for pair in combinations(range(4), 2):
        exp = r[pair[0]] + r[pair[1]]
        out.append((f"x{pair[0]+1}x{pair[1]+1}", exp, exp >= 2.0))
    return out


def main() -> None:
    examples = {
        "stress_notes_R=(L^-1/5,L^13/15,L^13/15,L^13/15)": (
            -1 / 5,
            13 / 15,
            13 / 15,
            13 / 15,
        ),
        "symmetric_hard_delta_model_R=(L^0,L^a,L^a,L^a), a=0.9": (
            0.0,
            0.9,
            0.9,
            0.9,
        ),
        "very_short_R1_model_R=(L^-1,L^0.8,L^0.8,L^0.8)": (
            -1.0,
            0.8,
            0.8,
            0.8,
        ),
    }

    lines: list[str] = []
    lines.append("# Round 32 coordinate-product flap check")
    lines.append("")
    lines.append("Target normalized to S=(1,1,L,L), so q=|Q|~L^2.")
    lines.append("A coordinate-product flap needs one coordinate 2-product")
    lines.append("available as the F-normal parameter area with exponent >=2.")
    lines.append("")
    for name, r in examples.items():
        lines.append(f"## {name}")
        lines.append(f"r = {tuple(round(x, 6) for x in r)}")
        lines.append(f"hard exponent r3+r4 = {r[2] + r[3]:.6g} < 2 ? {r[2] + r[3] < 2}")
        lines.append("")
        lines.append("| normal pair | exponent | can cover Q with J2F<=C? |")
        lines.append("|---|---:|---|")
        for label, exp, ok in product_exponents(r):
            lines.append(f"| {label} | {exp:.6g} | {'yes' if ok else 'no'} |")
        lines.append("")

    lines.append("Conclusion: any product construction where the null sheet factor and")
    lines.append("the F-parameter factor are honest coordinate factors is impossible")
    lines.append("in the hard regime.  A counterexample would need a genuinely")
    lines.append("non-product/snake F-submersion using family compatibility, not just")
    lines.append("a low-energy flap inserted in a coordinate slab.")

    text = "\n".join(lines)
    print(text)


if __name__ == "__main__":
    main()
