"""Round 23 search for Guth thesis Ch. 8.2 exponent counterexamples.

All side lengths are encoded as powers of a large parameter L.  The script
uses the five bounded-2-dilation degree-one maps listed in Guth thesis
Chapter 8.2.  The main search is linear programming over the exponent
variables for fixed move words.  This is stronger than a grid search for the
move parameters: for each tested word it optimizes over all admissible
parameters, initial/terminal linear 2-contractions, and, in the normalized
mode, over all sorted targets S with s1=0 and s4=1.

The corrected interpolated short-side variant uses two independent parameters:
lambda for the first two sides and A for the third output side:

    R -> lambda R1 x lambda^-3 R2 x A x B,
    lambda^4 <= R2/R1, R3 <= A <= (R3 R4)^(1/2), R3 R4 = A B.

The older workspace code used the same exponent for lambda and A; this file
keeps them separate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import random
import time
from typing import Iterable

import numpy as np
from scipy.optimize import linprog


MOVE_TYPES = (
    "snake",
    "codim_snake",
    "short_stretch",
    "short_tech",
    "short_interp",
    "pinch",
    "double_pinch",
)


@dataclass(frozen=True)
class LPResult:
    margin: float
    word: tuple[str, ...]
    status: str
    r: tuple[float, float, float, float] | None
    s: tuple[float, float, float, float] | None
    states: tuple[tuple[float, float, float, float], ...]
    params: tuple[tuple[str, float], ...]
    badness: tuple[float, float, float] | None
    lin_initial: float | None
    lin_terminal: float | None


def fmt_float(x: float) -> str:
    if abs(x) < 5e-9:
        return "0"
    return f"{x:.6g}"


def fmt_vec(v: Iterable[float]) -> str:
    return "(" + ", ".join(fmt_float(float(x)) for x in v) + ")"


def target_badness(r: Iterable[float], s: Iterable[float]) -> tuple[float, float, float]:
    r0, r1, r2, r3 = [float(x) for x in r]
    s0, s1, s2, s3 = [float(x) for x in s]
    return (
        r0 - s0,
        r2 + r3 - s2 - s3,
        r0 + r1 + r2 + r3 - (s0 + 0.5 * s1 + 1.5 * s2 + s3),
    )


def lin2_identity(src: Iterable[float], dst: Iterable[float]) -> float:
    q = [float(b) - float(a) for a, b in zip(src, dst)]
    vals = sorted(q)
    return vals[-1] + vals[-2]


class LPBuilder:
    def __init__(
        self,
        word: tuple[str, ...],
        target_mode: str,
        double_variant: str = "corrected",
        bound: float = 8.0,
    ) -> None:
        self.word = word
        self.target_mode = target_mode
        self.double_variant = double_variant
        self.bound = bound
        self.names: list[str] = []
        self.idx: dict[str, int] = {}
        self.a_ub: list[np.ndarray] = []
        self.b_ub: list[float] = []
        self.a_eq: list[np.ndarray] = []
        self.b_eq: list[float] = []
        self.params: list[tuple[str, str]] = []

    def var(self, name: str) -> int:
        if name not in self.idx:
            self.idx[name] = len(self.names)
            self.names.append(name)
        return self.idx[name]

    def row(self, terms: dict[str, float]) -> np.ndarray:
        out = np.zeros(len(self.names))
        # Variables are normally created before rows are assembled.  This helper
        # also tolerates new variables and resizes existing rows when needed.
        for name in terms:
            self.var(name)
        if len(out) != len(self.names):
            out = np.zeros(len(self.names))
        for name, coef in terms.items():
            out[self.idx[name]] += coef
        return out

    def _resize_rows(self) -> None:
        n = len(self.names)
        for rows in (self.a_ub, self.a_eq):
            for i, row in enumerate(rows):
                if len(row) < n:
                    rows[i] = np.pad(row, (0, n - len(row)))

    def le(self, terms: dict[str, float], rhs: float = 0.0) -> None:
        row = self.row(terms)
        self._resize_rows()
        if len(row) < len(self.names):
            row = np.pad(row, (0, len(self.names) - len(row)))
        self.a_ub.append(row)
        self.b_ub.append(rhs)

    def eq(self, terms: dict[str, float], rhs: float = 0.0) -> None:
        row = self.row(terms)
        self._resize_rows()
        if len(row) < len(self.names):
            row = np.pad(row, (0, len(self.names) - len(row)))
        self.a_eq.append(row)
        self.b_eq.append(rhs)

    def add_sorted(self, prefix: str) -> None:
        for i in range(3):
            self.le({f"{prefix}{i}": 1.0, f"{prefix}{i+1}": -1.0})

    def add_pair_2contraction_identity(self, src_prefix: str, dst_prefix: str) -> None:
        # For sorted rectangles the sorted matching minimizes the sum of the two
        # largest expansion exponents.  We still impose every pair inequality,
        # i.e. (dst_i-src_i)+(dst_j-src_j) <= 0.
        for i, j in combinations(range(4), 2):
            self.le(
                {
                    f"{dst_prefix}{i}": 1.0,
                    f"{src_prefix}{i}": -1.0,
                    f"{dst_prefix}{j}": 1.0,
                    f"{src_prefix}{j}": -1.0,
                }
            )

    def add_move(self, move: str, t: int) -> None:
        x = [f"x{t}_{i}" for i in range(4)]
        y = [f"x{t+1}_{i}" for i in range(4)]

        def lvar(suffix: str) -> str:
            name = f"p{t}_{suffix}"
            self.params.append((move, name))
            return name

        if move == "snake":
            lam = lvar("lam")
            raw = [
                {x[0]: 1.0},
                {x[1]: 1.0},
                {x[2]: 1.0, lam: -1.0},
                {x[3]: 1.0, lam: 1.0},
            ]
            self.le({lam: -1.0})  # lam >= 0
            self.le({lam: 1.0, x[2]: -1.0, x[1]: 1.0})  # lam <= x2-x1
        elif move == "codim_snake":
            lam = lvar("lam")
            raw = [
                {x[0]: 1.0},
                {x[1]: 1.0, lam: -1.0},
                {x[2]: 1.0, lam: 1.0},
                {x[3]: 1.0, lam: -1.0},
            ]
            self.le({lam: -1.0})
            self.le({lam: 1.0, x[1]: -1.0, x[0]: 1.0})
            self.le({lam: 2.0, x[3]: -1.0, x[2]: 1.0})
        elif move == "short_stretch":
            lam = lvar("lam")
            raw = [
                {x[0]: 1.0, lam: 1.0},
                {x[1]: 1.0, lam: -3.0},
                {x[2]: 1.0, lam: 1.0},
                {x[3]: 1.0, lam: -1.0},
            ]
            self.le({lam: -1.0})
            self.le({lam: 4.0, x[1]: -1.0, x[0]: 1.0})
            self.le({lam: 2.0, x[3]: -1.0, x[2]: 1.0})
        elif move == "short_tech":
            lam = lvar("lam")
            raw = [
                {x[0]: 1.0, lam: 1.0},
                {x[1]: 1.0, lam: -3.0},
                {x[2]: 1.0},
                {x[3]: 1.0},
            ]
            self.le({lam: -1.0})
            self.le({lam: 4.0, x[1]: -1.0, x[0]: 1.0})
        elif move == "short_interp":
            lam = lvar("lam")
            a = lvar("A")
            raw = [
                {x[0]: 1.0, lam: 1.0},
                {x[1]: 1.0, lam: -3.0},
                {a: 1.0},
                {x[2]: 1.0, x[3]: 1.0, a: -1.0},
            ]
            self.le({lam: -1.0})
            self.le({lam: 4.0, x[1]: -1.0, x[0]: 1.0})
            self.le({a: -1.0, x[2]: 1.0})  # A >= R3
            self.le({a: 2.0, x[2]: -1.0, x[3]: -1.0})  # A <= sqrt(R3 R4)
        elif move == "pinch":
            a = lvar("A")
            b = lvar("B")
            raw = [{a: 1.0}, {a: 1.0}, {a: 1.0}, {b: 1.0}]
            self.le({a: 1.0, x[0]: -1.0})  # A <= R1
            self.le({a: 1.0, b: -1.0})  # B >= A, side-order convention
            self.le({a: 2.0, b: 1.0, x[1]: -1.0, x[2]: -1.0, x[3]: -1.0})
        elif move == "double_pinch":
            a = lvar("A")
            b = lvar("B")
            if self.double_variant == "ocr_literal":
                first = {x[0]: 1.0, a: -1.0}  # R1/A, not source-corrected
            else:
                first = {x[0]: 2.0, a: -1.0}  # R1^2/A
            raw = [first, {a: 1.0}, {a: 1.0}, {b: 1.0}]
            self.le({a: -1.0, x[0]: 1.0})  # A >= R1
            self.le({a: 2.0, x[1]: -1.0, x[2]: -1.0})
            self.le({a: 1.0, b: -1.0})  # B >= A, side-order convention
            self.le({a: 3.0, b: 1.0, x[0]: -1.0, x[1]: -1.0, x[2]: -1.0, x[3]: -1.0})
        else:
            raise ValueError(move)

        for i, expr in enumerate(raw):
            terms = {f"x{t+1}_{i}": 1.0}
            for name, coef in expr.items():
                terms[name] = terms.get(name, 0.0) - coef
            self.eq(terms)
        self.add_sorted(f"x{t+1}_")

    def solve(self) -> LPResult:
        d = len(self.word)
        # Create variables first so row sizes remain stable.
        for prefix in ["r_", "s_"]:
            for i in range(4):
                self.var(f"{prefix}{i}")
        for t in range(d + 1):
            for i in range(4):
                self.var(f"x{t}_{i}")
        self.var("m")

        self.add_sorted("r_")
        self.add_sorted("s_")
        for t in range(d + 1):
            self.add_sorted(f"x{t}_")

        if self.target_mode == "stress":
            for i, value in enumerate((0.0, 0.0, 1.0, 1.0)):
                self.eq({f"s_{i}": 1.0}, value)
        elif self.target_mode == "normalized":
            self.eq({"s_0": 1.0}, 0.0)
            self.eq({"s_3": 1.0}, 1.0)
        else:
            raise ValueError(self.target_mode)

        self.add_pair_2contraction_identity("r_", "x0_")
        self.add_pair_2contraction_identity(f"x{d}_", "s_")

        # Failure of all three target conclusions by common margin m.
        self.le({"r_0": 1.0, "s_0": -1.0, "m": 1.0})
        self.le({"r_2": 1.0, "r_3": 1.0, "s_2": -1.0, "s_3": -1.0, "m": 1.0})
        self.le(
            {
                "r_0": 1.0,
                "r_1": 1.0,
                "r_2": 1.0,
                "r_3": 1.0,
                "s_0": -1.0,
                "s_1": -0.5,
                "s_2": -1.5,
                "s_3": -1.0,
                "m": 1.0,
            }
        )

        for t, move in enumerate(self.word):
            self.add_move(move, t)

        c = np.zeros(len(self.names))
        c[self.idx["m"]] = -1.0
        self._resize_rows()
        bounds = []
        for name in self.names:
            if name == "m":
                bounds.append((-4.0, 4.0))
            elif name.startswith("s_") and self.target_mode == "normalized":
                bounds.append((0.0, 1.0))
            else:
                bounds.append((-self.bound, self.bound))

        result = linprog(
            c,
            A_ub=np.array(self.a_ub) if self.a_ub else None,
            b_ub=np.array(self.b_ub) if self.b_ub else None,
            A_eq=np.array(self.a_eq) if self.a_eq else None,
            b_eq=np.array(self.b_eq) if self.b_eq else None,
            bounds=bounds,
            method="highs",
        )
        if not result.success:
            return LPResult(
                margin=-float("inf"),
                word=self.word,
                status=result.message,
                r=None,
                s=None,
                states=(),
                params=(),
                badness=None,
                lin_initial=None,
                lin_terminal=None,
            )

        x = result.x
        r = tuple(float(x[self.idx[f"r_{i}"]]) for i in range(4))
        s = tuple(float(x[self.idx[f"s_{i}"]]) for i in range(4))
        states = tuple(
            tuple(float(x[self.idx[f"x{t}_{i}"]]) for i in range(4))
            for t in range(d + 1)
        )
        params = tuple((name, float(x[self.idx[name]])) for _, name in self.params)
        return LPResult(
            margin=float(x[self.idx["m"]]),
            word=self.word,
            status="ok",
            r=r,
            s=s,
            states=states,
            params=params,
            badness=target_badness(r, s),
            lin_initial=lin2_identity(r, states[0]),
            lin_terminal=lin2_identity(states[-1], s),
        )


def solve_word(
    word: tuple[str, ...],
    target_mode: str,
    double_variant: str = "corrected",
    bound: float = 8.0,
) -> LPResult:
    return LPBuilder(word, target_mode, double_variant=double_variant, bound=bound).solve()


def exhaustive_lp(
    target_mode: str,
    max_depth: int,
    double_variant: str = "corrected",
    stop_after_hit: bool = False,
) -> tuple[list[LPResult], int, float]:
    start = time.time()
    best: list[LPResult] = []
    solved = 0
    for depth in range(max_depth + 1):
        for word in product(MOVE_TYPES, repeat=depth):
            solved += 1
            res = solve_word(tuple(word), target_mode, double_variant=double_variant)
            if res.status == "ok":
                best.append(res)
                best.sort(key=lambda item: item.margin, reverse=True)
                del best[12:]
                if stop_after_hit and res.margin > 1e-7:
                    return best, solved, time.time() - start
    return best, solved, time.time() - start


def random_lp(
    target_mode: str,
    depth_range: tuple[int, int],
    trials: int,
    seed: int,
    double_variant: str = "corrected",
) -> tuple[list[LPResult], int, float]:
    rng = random.Random(seed)
    start = time.time()
    best: list[LPResult] = []
    for i in range(trials):
        depth = rng.randint(depth_range[0], depth_range[1])
        word = tuple(rng.choice(MOVE_TYPES) for _ in range(depth))
        res = solve_word(word, target_mode, double_variant=double_variant)
        if res.status == "ok":
            best.append(res)
            best.sort(key=lambda item: item.margin, reverse=True)
            del best[12:]
    return best, trials, time.time() - start


def result_lines(title: str, best: list[LPResult], solved: int, elapsed: float) -> list[str]:
    out = [f"## {title}", f"LPs attempted: {solved}; elapsed: {elapsed:.2f}s"]
    if not best:
        out.append("No feasible templates.")
        return out
    hit_count = sum(1 for item in best if item.margin > 1e-7)
    out.append(f"best margin m = {fmt_float(best[0].margin)}; positive hits retained = {hit_count}")
    for k, item in enumerate(best[:5], 1):
        out.append(f"{k}. m={fmt_float(item.margin)} word={' -> '.join(item.word) if item.word else '(linear only)'}")
        if item.r is not None and item.s is not None:
            out.append(f"   R={fmt_vec(item.r)}  S={fmt_vec(item.s)}")
            out.append(f"   badness={fmt_vec(item.badness or ())}")
            out.append(
                f"   initial_lin2={fmt_float(item.lin_initial or 0.0)} terminal_lin2={fmt_float(item.lin_terminal or 0.0)}"
            )
            if item.params:
                shown = ", ".join(f"{name}={fmt_float(val)}" for name, val in item.params[:12])
                if len(item.params) > 12:
                    shown += ", ..."
                out.append(f"   params: {shown}")
            if len(item.states) <= 7:
                states = " | ".join(fmt_vec(state) for state in item.states)
                out.append(f"   states: {states}")
    return out


def explicit_counterexample_lines() -> list[str]:
    # The shortest clean pattern found by the LP:
    # initial linear -> double_pinch -> corrected short_interp -> terminal identity.
    r: Vec = (Fraction(-1, 6), Fraction(5, 6), Fraction(5, 6), Fraction(5, 6))
    x0: Vec = (Fraction(0), Fraction(2, 3), Fraction(2, 3), Fraction(2, 3))
    x1: Vec = (Fraction(0), Fraction(0), Fraction(0), Fraction(2))
    s: Vec = (Fraction(0), Fraction(0), Fraction(1), Fraction(1))
    bad = (
        r[0] - s[0],
        r[2] + r[3] - s[2] - s[3],
        sum(r) - (s[0] + Fraction(1, 2) * s[1] + Fraction(3, 2) * s[2] + s[3]),
    )
    initial_q = tuple(x0[i] - r[i] for i in range(4))
    out = ["## Explicit exponent pattern from the LP hit"]
    out.append("R -> X0 by an initial diagonal linear map, then double pinching, then the corrected short-side interpolated technical map.")
    out.append(f"R={fvec(r)}")
    out.append(f"X0={fvec(x0)}")
    out.append(f"after double_pinch(A exponent 0, B exponent 2): X1={fvec(x1)}")
    out.append(f"after short_interp(lambda exponent 0, output A exponent 1): S={fvec(s)}")
    out.append(f"initial linear expansion exponents q=X0-R={fvec(initial_q)}, top-two sum={ffmt(sum(sorted(initial_q)[-2:]))}")
    out.append(f"terminal linear exponent={ffmt(lin2_fraction(s, s))}")
    out.append(f"badness exponents (R1/S1, R3R4/S3S4, Vol/T)={fvec(bad)}")
    out.append("Double-pinch constraints at exponent level: A>=R1 is 0>=0, A^2<=R2R3 is 0<=4/3, A^3B<=Vol is 2<=2.")
    out.append("Short-interp constraints at exponent level: lambda^4<=R2/R1 is 0<=0, R3<=A<=sqrt(R3R4) is 0<=1<=1, and AB=R3R4 gives B exponent 1.")
    out.append("The equalities are harmless asymptotically: constants can be chosen so Guth's strict inequalities hold while these exponents remain unchanged.")
    return out


# Corrected grid/beam search for the old concrete stress route.

Vec = tuple[Fraction, Fraction, Fraction, Fraction]


def frange(lo: Fraction, hi: Fraction, step: Fraction) -> list[Fraction]:
    if hi < lo:
        return []
    n0 = int(np.ceil(float(lo / step) - 1e-12))
    n1 = int(np.floor(float(hi / step) + 1e-12))
    return [i * step for i in range(n0, n1 + 1)]


def ffmt(x: Fraction) -> str:
    if x == 0:
        return "0"
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def fvec(v: Vec) -> str:
    return "(" + ", ".join(ffmt(x) for x in v) + ")"


@dataclass(frozen=True)
class Move:
    label: str
    out: Vec


def moves_grid(r: Vec, step: Fraction, span: Fraction = Fraction(4)) -> list[Move]:
    r0, r1, r2, r3 = r
    out: list[Move] = []

    for lam in frange(Fraction(0), r2 - r1, step):
        if lam > 0:
            out.append(Move(f"snake({ffmt(lam)})", (r0, r1, r2 - lam, r3 + lam)))

    for lam in frange(Fraction(0), min(r1 - r0, (r3 - r2) / 2), step):
        if lam > 0:
            out.append(Move(f"codim_snake({ffmt(lam)})", (r0, r1 - lam, r2 + lam, r3 - lam)))

    for lam in frange(Fraction(0), min((r1 - r0) / 4, (r3 - r2) / 2), step):
        if lam > 0:
            out.append(Move(f"short_stretch({ffmt(lam)})", (r0 + lam, r1 - 3 * lam, r2 + lam, r3 - lam)))

    for lam in frange(Fraction(0), (r1 - r0) / 4, step):
        if lam > 0:
            out.append(Move(f"short_tech({ffmt(lam)})", (r0 + lam, r1 - 3 * lam, r2, r3)))

    # Correct two-parameter interpolated technical variant.
    for lam in frange(Fraction(0), (r1 - r0) / 4, step):
        if lam <= 0:
            continue
        for a in frange(r2, (r2 + r3) / 2, step):
            if a > r2:
                b = r2 + r3 - a
                out.append(Move(f"short_interp(lambda={ffmt(lam)},A={ffmt(a)})", (r0 + lam, r1 - 3 * lam, a, b)))

    for a in frange(r0 - span, r0, step):
        if a >= r0:
            continue
        bmax = r1 + r2 + r3 - 2 * a
        for b in frange(a, bmax, step):
            out.append(Move(f"pinch(A={ffmt(a)},B={ffmt(b)})", (a, a, a, b)))

    for a in frange(r0, (r1 + r2) / 2, step):
        if a <= r0:
            continue
        bmax = r0 + r1 + r2 + r3 - 3 * a
        for b in frange(a, bmax, step):
            out.append(Move(f"double_pinch(A={ffmt(a)},B={ffmt(b)})", (2 * r0 - a, a, a, b)))

    return out


def lin2_fraction(src: Vec, dst: Vec) -> Fraction:
    q = sorted(dst[i] - src[i] for i in range(4))
    return q[-1] + q[-2]


def route_to_target_grid(
    start: Vec,
    target: Vec,
    depth: int,
    step: Fraction,
    beam: int,
) -> tuple[bool, list[str], list[tuple[Fraction, Vec, list[str]]]]:
    frontier: list[tuple[Vec, list[str]]] = [(start, [])]
    best_seen: list[tuple[Fraction, Vec, list[str]]] = [(lin2_fraction(start, target), start, [])]
    seen = {start}
    for _ in range(depth):
        candidates: list[tuple[Fraction, int, Vec, list[str]]] = []
        serial = 0
        for state, path in frontier:
            for mv in moves_grid(state, step):
                if mv.out in seen:
                    continue
                seen.add(mv.out)
                npath = path + [mv.label]
                val = lin2_fraction(mv.out, target)
                best_seen.append((val, mv.out, npath))
                if val <= 0:
                    return True, npath + [f"terminal_linear(exp={ffmt(val)})"], sorted(best_seen, key=lambda z: z[0])[:10]
                spread = max(abs(x) for x in mv.out)
                score = val + spread / 50
                candidates.append((score, serial, mv.out, npath))
                serial += 1
        candidates.sort(key=lambda z: (z[0], len(z[3])))
        frontier = [(state, path) for _, _, state, path in candidates[:beam]]
        if not frontier:
            break
    return False, [f"searched {len(seen)} states"], sorted(best_seen, key=lambda z: z[0])[:10]


def grid_route_lines() -> list[str]:
    old_start: Vec = (Fraction(-1), Fraction(4), Fraction(5), Fraction(6))
    old_target: Vec = (Fraction(0), Fraction(0), Fraction(6), Fraction(6))
    norm_start: Vec = tuple(x / 6 for x in old_start)  # type: ignore[assignment]
    norm_target: Vec = (Fraction(0), Fraction(0), Fraction(1), Fraction(1))
    out = ["## Corrected grid route checks for old stress example"]
    specs = [
        ("old integer scale", old_start, old_target, Fraction(1), 5, 3000),
        ("old half scale", old_start, old_target, Fraction(1, 2), 4, 3000),
        ("normalized sixth-grid", norm_start, norm_target, Fraction(1, 6), 4, 3000),
    ]
    for name, start, target, step, depth, beam in specs:
        ok, path, best = route_to_target_grid(start, target, depth, step, beam)
        out.append(f"{name}: step={ffmt(step)} depth={depth} beam={beam}: {'FOUND' if ok else 'not found'}")
        out.append("  " + " -> ".join(path))
        out.append("  best terminal linear exponents:")
        for val, state, state_path in best[:5]:
            path_text = " -> ".join(state_path[-3:]) if state_path else "(start)"
            out.append(f"    exp={ffmt(val)} state={fvec(state)} tail={path_text}")
    return out


def permutation_check_lines(samples: int = 10000, seed: int = 23) -> list[str]:
    # Empirical check for the sorted-matching simplification used in the LP.
    # The beam/grid searches still use the exact sorted pairing formula.
    from itertools import permutations

    rng = random.Random(seed)
    for _ in range(samples):
        r = sorted(rng.uniform(-5, 5) for _ in range(4))
        s = sorted(rng.uniform(-5, 5) for _ in range(4))
        identity = lin2_identity(r, s)
        best = min(
            sum(sorted([s[i] - r[p[i]] for i in range(4)])[-2:])
            for p in permutations(range(4))
        )
        if abs(identity - best) > 1e-8:
            return [
                "## Linear permutation check",
                "Found a random case where sorted matching was not optimal:",
                f"R={fmt_vec(r)} S={fmt_vec(s)} identity={fmt_float(identity)} best={fmt_float(best)}",
            ]
    return [
        "## Linear permutation check",
        f"No counterexample to sorted matching in {samples} random sorted pairs; identity matched exhaustive 24-permutation optimum.",
    ]


def main() -> None:
    out: list[str] = [
        "# Round 23 Guth Ch. 8.2 exponent search",
        "",
        "Move set: snake, codimension-one snake, short-side stretch, corrected short-side technical map, corrected two-parameter interpolated short-side map, pinching, double pinching.",
        "Double pinching is encoded as R1^2/A x A x A x B; the OCR-literal sensitivity run uses R1/A.",
        "",
    ]

    out.extend(permutation_check_lines())
    out.append("")

    out.extend(explicit_counterexample_lines())
    out.append("")

    for target_mode, depth in (("stress", 3), ("normalized", 3)):
        best, solved, elapsed = exhaustive_lp(target_mode, max_depth=depth, double_variant="corrected")
        out.extend(result_lines(f"exhaustive LP, target={target_mode}, corrected double pinch, depth<= {depth}", best, solved, elapsed))
        out.append("")

    best, solved, elapsed = random_lp("normalized", (5, 8), trials=400, seed=2301, double_variant="corrected")
    out.extend(result_lines("random LP, target=normalized, corrected double pinch, depth 5-8", best, solved, elapsed))
    out.append("")

    best, solved, elapsed = random_lp("stress", (5, 8), trials=400, seed=2302, double_variant="corrected")
    out.extend(result_lines("random LP, target=stress, corrected double pinch, depth 5-8", best, solved, elapsed))
    out.append("")

    best, solved, elapsed = exhaustive_lp("normalized", max_depth=3, double_variant="ocr_literal")
    out.extend(result_lines("sensitivity LP, target=normalized, OCR-literal double pinch R1/A, depth<= 3", best, solved, elapsed))
    out.append("")
    out.append("The heavier corrected grid route routine is left in this script but not run by default; the LP hit above is parameter-continuous and shorter than the requested 5-8 move bound.")

    text = "\n".join(out) + "\n"
    Path("data/round23").mkdir(parents=True, exist_ok=True)
    Path("data/round23/guth_ch8_search_report.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
