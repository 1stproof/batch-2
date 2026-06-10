"""Exponent model for Guth thesis Chapter 8.2 maps.

Side lengths are represented by exponents of a large parameter L.  The
transformations below are the five degree-one bounded-2-dilation maps listed
on Guth thesis pp.145-148, plus two technical variants of the short-side
stretch.  The model is asymptotic: strict inequalities and dimensional
constants are ignored.

The script has two uses:

1. Check whether short compositions of the listed maps can carry the scaling
   R=(L^-1,L^4,L^5,L^6) to S=(1,1,L^6,L^6), up to a final linear
   2-contracting map.
2. Randomly scan short compositions for maps R->S whose exponents violate all
   three target alternatives in the problem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
import heapq
import random
from typing import Callable, Iterable


Vec = tuple[Fraction, Fraction, Fraction, Fraction]


def F(x: int | float | Fraction) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(x)


def fmt(x: Fraction) -> str:
    if x == 0:
        return "0"
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def fmt_vec(v: Vec) -> str:
    return "(" + ", ".join(fmt(x) for x in v) + ")"


def sortv(v: Iterable[Fraction]) -> Vec:
    s = sorted(v)
    return (s[0], s[1], s[2], s[3])


def lin2_exponent(r: Vec, s: Vec) -> Fraction:
    """Smallest diagonal/permuted linear 2-dilation exponent from r to s."""
    best: Fraction | None = None
    for p in permutations(range(4)):
        q = sorted([s[i] - r[p[i]] for i in range(4)])
        val = q[-1] + q[-2]
        if best is None or val < best:
            best = val
    assert best is not None
    return best


def linear_2_contracts(r: Vec, s: Vec) -> bool:
    return lin2_exponent(r, s) <= 0


def target_badness(r: Vec, s: Vec) -> tuple[Fraction, Fraction, Fraction]:
    """Return exponents of the three ratios in the problem conclusion."""
    first = r[0] - s[0]
    third_fourth = r[2] + r[3] - s[2] - s[3]
    denom = s[0] + Fraction(1, 2) * s[1] + Fraction(3, 2) * s[2] + s[3]
    volume = sum(r) - denom
    return first, third_fourth, volume


def all_bad(r: Vec, s: Vec, margin: Fraction = Fraction(0)) -> bool:
    return all(x < -margin for x in target_badness(r, s))


@dataclass(frozen=True)
class Move:
    name: str
    out: Vec
    param: Fraction | tuple[Fraction, Fraction] | None = None

    def label(self) -> str:
        if self.param is None:
            return self.name
        if isinstance(self.param, tuple):
            return f"{self.name}{tuple(fmt(x) for x in self.param)}"
        return f"{self.name}({fmt(self.param)})"


def grid_between(lo: Fraction, hi: Fraction, step: Fraction) -> list[Fraction]:
    if hi < lo:
        return []
    n0 = (lo / step).__ceil__()
    n1 = (hi / step).__floor__()
    return [i * step for i in range(n0, n1 + 1)]


def moves(r: Vec, step: Fraction = Fraction(1, 2)) -> list[Move]:
    r1, r2, r3, r4 = r
    out: list[Move] = []

    # 1. Snake: R1 x R2 x R3 x R4 -> R1 x R2 x A^-1 R3 x A R4.
    for a in grid_between(Fraction(0), r3 - r2, step):
        if a:
            out.append(Move("snake", sortv((r1, r2, r3 - a, r4 + a)), a))

    # 2. Codimension-one snake.
    hi = min(r2 - r1, (r4 - r3) / 2)
    for a in grid_between(Fraction(0), hi, step):
        if a:
            out.append(Move("codim_snake", sortv((r1, r2 - a, r3 + a, r4 - a)), a))

    # 3. Short-side stretch.
    hi = min((r2 - r1) / 4, (r4 - r3) / 2)
    for a in grid_between(Fraction(0), hi, step):
        if a:
            out.append(Move("short_stretch", sortv((r1 + a, r2 - 3 * a, r3 + a, r4 - a)), a))

    # 3'. Technical short-side stretch.
    hi = (r2 - r1) / 4
    for a in grid_between(Fraction(0), hi, step):
        if a:
            out.append(Move("short_tech", sortv((r1 + a, r2 - 3 * a, r3, r4)), a))

    # 3''. Interpolated technical variant:
    # R -> A R1 x A^-3 R2 x A x B, with A^4 < R2/R1,
    # R3 < A < (R3 R4)^1/2, and R3 R4 = A B.
    lo = r3
    hi = min((r2 - r1) / 4, (r3 + r4) / 2)
    for a in grid_between(lo, hi, step):
        if a > r3:
            b = r3 + r4 - a
            out.append(Move("short_interp", sortv((r1 + a, r2 - 3 * a, a, b)), a))

    # 4. Pinching: R -> A x A x A x B, A<R1, A^2 B<R2 R3 R4.
    # Scan a bounded window below r1 and use extremal b plus nearby smaller b.
    for a in grid_between(r1 - 4, r1, step):
        if a < r1:
            bmax = r2 + r3 + r4 - 2 * a
            for b in {bmax, bmax - step, bmax - 2 * step, a}:
                if b >= a and 2 * a + b <= r2 + r3 + r4:
                    out.append(Move("pinch", sortv((a, a, a, b)), (a, b)))

    # 5. Double pinching: R -> R1^2/A x A x A x B.
    # The thesis OCR often drops the superscript in R_1^2/A.  The exponent
    # 2*r1-a is forced by Step 3 -> Step 5 on p.148: the linear map from
    # R1 x R1 x A^2/R1 x AB/R1 to R1^2/A x A x A x B has factors
    # R1/A, A/R1, R1/A, R1/A and hence 2-dilation 1.
    hi = (r2 + r3) / 2
    for a in grid_between(r1, hi, step):
        if a > r1:
            bmax = sum(r) - 3 * a
            for b in {bmax, bmax - step, bmax - 2 * step, a}:
                if b >= a and 3 * a + b <= sum(r):
                    out.append(Move("double_pinch", sortv((2 * r1 - a, a, a, b)), (a, b)))

    return out


def shortest_route_to_target(
    start: Vec,
    target: Vec,
    depth: int,
    step: Fraction,
    beam: int = 300,
) -> tuple[bool, list[str]]:
    """Beam search for a route ending with a linear 2-contracting map to target."""
    seen = {start}
    q: list[tuple[Vec, list[str]]] = [(start, [])]
    if linear_2_contracts(start, target):
        return True, ["linear"]
    for _ in range(depth):
        candidates: list[tuple[Fraction, int, Vec, list[str]]] = []
        counter = 0
        for state, path in q:
            for mv in moves(state, step):
                if mv.out in seen:
                    continue
                seen.add(mv.out)
                npath = path + [mv.label()]
                if linear_2_contracts(mv.out, target):
                    return True, npath + [f"linear_2_contract(exp={fmt(lin2_exponent(mv.out, target))})"]
                # Primary heuristic: final linear 2-dilation exponent to the target.
                # Secondary heuristic: keep exponents in a bounded range to avoid
                # spending the whole scan on irrelevant pinched rectangles.
                spread = max(abs(x) for x in mv.out)
                score = lin2_exponent(mv.out, target) + Fraction(1, 20) * spread
                candidates.append((score, counter, mv.out, npath))
                counter += 1
        candidates.sort(key=lambda x: (x[0], len(x[3])))
        q = [(state, path) for _, _, state, path in candidates[:beam]]
        if not q:
            break
    return False, [f"searched {len(seen)} states"]


def random_counterexample_scan(seed: int = 1, trials: int = 1_000, depth: int = 4) -> list[str]:
    rng = random.Random(seed)
    hits: list[tuple[Fraction, Vec, Vec, list[str], tuple[Fraction, Fraction, Fraction]]] = []
    for _ in range(trials):
        vals = sorted(Fraction(rng.randint(-8, 8), 2) for _ in range(4))
        r0: Vec = (vals[0], vals[1], vals[2], vals[3])
        state = r0
        path: list[str] = []
        for __ in range(depth):
            ms = moves(state, Fraction(1, 2))
            if not ms:
                break
            mv = rng.choice(ms)
            state = mv.out
            path.append(mv.label())
            bad = target_badness(r0, state)
            score = max(bad)
            if all_bad(r0, state):
                hits.append((score, r0, state, path.copy(), bad))
                break
    hits.sort(key=lambda x: x[0])
    lines: list[str] = []
    if not hits:
        lines.append(f"No all-three violating composition found in {trials} random trials of depth {depth}.")
        return lines
    for score, r, s, path, bad in hits[:10]:
        lines.append(f"score={fmt(score)} R={fmt_vec(r)} S={fmt_vec(s)} bad={tuple(fmt(x) for x in bad)}")
        lines.append("  " + " -> ".join(path))
    return lines


def main() -> None:
    start: Vec = (F(-1), F(4), F(5), F(6))
    target: Vec = (F(0), F(0), F(6), F(6))
    print("# Guth Chapter 8.2 exponent search")
    print(f"start R0 = {fmt_vec(start)}")
    print(f"target S = {fmt_vec(target)}")
    print(f"target badness R0/S = {tuple(fmt(x) for x in target_badness(start, target))}")
    print(f"final linear 2-dilation exponent from R0 to S = {fmt(lin2_exponent(start, target))}")
    print()

    for step in (Fraction(1, 1), Fraction(1, 2)):
        ok, path = shortest_route_to_target(start, target, depth=3, step=step)
        print(f"beam route search step={fmt(step)} depth=3: {'FOUND' if ok else 'not found'}")
        print("  " + " -> ".join(path))
    print()

    residual: Vec = (F(0), F(1), F(5), F(6))
    print(f"residual after short_tech(1): {fmt_vec(residual)}")
    print(f"residual badness original R0 vs final target = {tuple(fmt(x) for x in target_badness(start, target))}")
    print(f"linear 2-dilation exponent residual -> target = {fmt(lin2_exponent(residual, target))}")
    print("single moves from residual with best final linear exponent to target:")
    ranked = sorted(
        ((lin2_exponent(mv.out, target), mv) for mv in moves(residual, Fraction(1, 2))),
        key=lambda x: (x[0], x[1].label()),
    )
    for val, mv in ranked[:12]:
        print(f"  {mv.label():30s} -> {fmt_vec(mv.out):22s} final linear exp {fmt(val)}")
    print()

    for line in random_counterexample_scan():
        print(line)


if __name__ == "__main__":
    main()
