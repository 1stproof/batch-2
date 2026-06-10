"""Round 27 LP probe for auxiliary Guth Chapter 8.2 compositions.

Side lengths are exponents of a large parameter L.  The fixed stress model is

    S = (0, 0, 1, 1),
    R = (-1/5, 13/15, 13/15, 13/15).

It violates the desired theorem conclusion by exponent margins
(-1/5, -4/15, -1/10), while saturating Guth's published Estimate 1.

For this fixed hypothetical counterexample R -> S, the script asks whether
precomposing or postcomposing by short words in the valid Guth thesis Ch. 8.2
maps can force a violation of Estimate 1 for the composite.

Important correction relative to older exploratory code:
the technical short-side interpolation is encoded with one parameter A, as in
the thesis text, not with independent lambda and output A.  In exponents it is

    (r1,r2,r3,r4) -> (r1+a, r2-3a, a, r3+r4-a),
    4a <= r2-r1, r3 <= a <= (r3+r4)/2.

The independent-parameter version would reproduce a known false "counterexample"
and is intentionally not used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import linprog


R_STRESS = (-1.0 / 5.0, 13.0 / 15.0, 13.0 / 15.0, 13.0 / 15.0)
S_STRESS = (0.0, 0.0, 1.0, 1.0)

MOVE_TYPES = (
    "linear",
    "snake",
    "codim_snake",
    "short_stretch",
    "short_tech",
    "short_tech_interp",
    "pinch",
    "double_pinch",
)


def fmt(x: float) -> str:
    if abs(x) < 5e-8:
        return "0"
    return f"{x:.6g}"


def fmt_vec(xs: Iterable[float]) -> str:
    return "(" + ", ".join(fmt(float(x)) for x in xs) + ")"


def badness(r: tuple[float, ...], s: tuple[float, ...]) -> tuple[float, float, float]:
    return (
        r[0] - s[0],
        r[2] + r[3] - s[2] - s[3],
        sum(r) - (s[0] + 0.5 * s[1] + 1.5 * s[2] + s[3]),
    )


def estimate_forms() -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for k in (2, 3, 4):
        for j in range(k):
            for ell in range(k, 5):
                out.append((k, j, ell))
    # Remove duplicates while preserving order.
    seen: set[tuple[int, int, int]] = set()
    uniq: list[tuple[int, int, int]] = []
    for item in out:
        if item not in seen:
            seen.add(item)
            uniq.append(item)
    return uniq


ESTIMATE_FORMS = estimate_forms()


def estimate_exponent(src: tuple[float, ...], dst: tuple[float, ...], form: tuple[int, int, int]) -> float:
    k, j, ell = form
    q = [dst[i] - src[i] for i in range(4)]
    return sum(q[:j]) + (float(k - j) / float(ell - j)) * sum(q[j:ell])


def all_estimate_exponents(src: tuple[float, ...], dst: tuple[float, ...]) -> list[tuple[tuple[int, int, int], float]]:
    return [(form, estimate_exponent(src, dst, form)) for form in ESTIMATE_FORMS]


@dataclass(frozen=True)
class LPOpt:
    side: str
    word: tuple[str, ...]
    form: tuple[int, int, int]
    value: float
    status: str
    endpoint: tuple[float, float, float, float] | None


class Builder:
    def __init__(
        self,
        word: tuple[str, ...],
        fixed_start: tuple[float, ...] | None,
        fixed_end: tuple[float, ...] | None,
        bound: float = 8.0,
    ) -> None:
        self.word = word
        self.fixed_start = fixed_start
        self.fixed_end = fixed_end
        self.bound = bound
        self.names: list[str] = []
        self.idx: dict[str, int] = {}
        self.a_ub: list[np.ndarray] = []
        self.b_ub: list[float] = []
        self.a_eq: list[np.ndarray] = []
        self.b_eq: list[float] = []

    def var(self, name: str) -> int:
        if name not in self.idx:
            self.idx[name] = len(self.names)
            self.names.append(name)
        return self.idx[name]

    def row(self, terms: dict[str, float]) -> np.ndarray:
        for name in terms:
            self.var(name)
        out = np.zeros(len(self.names))
        for name, coef in terms.items():
            out[self.idx[name]] += coef
        return out

    def resize_rows(self) -> None:
        n = len(self.names)
        for rows in (self.a_ub, self.a_eq):
            for i, row in enumerate(rows):
                if len(row) < n:
                    rows[i] = np.pad(row, (0, n - len(row)))

    def le(self, terms: dict[str, float], rhs: float = 0.0) -> None:
        row = self.row(terms)
        self.resize_rows()
        if len(row) < len(self.names):
            row = np.pad(row, (0, len(self.names) - len(row)))
        self.a_ub.append(row)
        self.b_ub.append(rhs)

    def eq(self, terms: dict[str, float], rhs: float = 0.0) -> None:
        row = self.row(terms)
        self.resize_rows()
        if len(row) < len(self.names):
            row = np.pad(row, (0, len(self.names) - len(row)))
        self.a_eq.append(row)
        self.b_eq.append(rhs)

    def add_sorted(self, prefix: str) -> None:
        for i in range(3):
            self.le({f"{prefix}{i}": 1.0, f"{prefix}{i+1}": -1.0})

    def set_expr(self, target: str, expr: dict[str, float]) -> None:
        terms = {target: 1.0}
        for name, coef in expr.items():
            terms[name] = terms.get(name, 0.0) - coef
        self.eq(terms)

    def add_move(self, move: str, t: int) -> None:
        x = [f"x{t}_{i}" for i in range(4)]
        y = [f"x{t+1}_{i}" for i in range(4)]

        if move == "linear":
            # Sorted diagonal/permuted linear 2-contraction.  For sorted side
            # vectors, sorted matching is the optimal matching for the top-two
            # expansion sum; impose every pair expansion sum <= 0.
            for i in range(4):
                self.var(y[i])
            for i in range(4):
                for j in range(i + 1, 4):
                    self.le({y[i]: 1.0, x[i]: -1.0, y[j]: 1.0, x[j]: -1.0})
            self.add_sorted(f"x{t+1}_")
            return

        p = f"p{t}"
        raw: list[dict[str, float]]

        if move == "snake":
            raw = [{x[0]: 1}, {x[1]: 1}, {x[2]: 1, p: -1}, {x[3]: 1, p: 1}]
            self.le({p: -1})  # p >= 0
            self.le({p: 1, x[2]: -1, x[1]: 1})  # p <= x2-x1
        elif move == "codim_snake":
            raw = [{x[0]: 1}, {x[1]: 1, p: -1}, {x[2]: 1, p: 1}, {x[3]: 1, p: -1}]
            self.le({p: -1})
            self.le({p: 1, x[1]: -1, x[0]: 1})
            self.le({p: 2, x[3]: -1, x[2]: 1})
        elif move == "short_stretch":
            raw = [{x[0]: 1, p: 1}, {x[1]: 1, p: -3}, {x[2]: 1, p: 1}, {x[3]: 1, p: -1}]
            self.le({p: -1})
            self.le({p: 4, x[1]: -1, x[0]: 1})
            self.le({p: 2, x[3]: -1, x[2]: 1})
        elif move == "short_tech":
            raw = [{x[0]: 1, p: 1}, {x[1]: 1, p: -3}, {x[2]: 1}, {x[3]: 1}]
            self.le({p: -1})
            self.le({p: 4, x[1]: -1, x[0]: 1})
        elif move == "short_tech_interp":
            # Single-parameter reading of the thesis technical interpolation:
            # A is both the stretch factor exponent and the third output side
            # exponent.  There is no independent lambda parameter here.
            raw = [{x[0]: 1, p: 1}, {x[1]: 1, p: -3}, {p: 1}, {x[2]: 1, x[3]: 1, p: -1}]
            self.le({p: -1})
            self.le({p: 4, x[1]: -1, x[0]: 1})
            self.le({p: -1, x[2]: 1})  # p >= x2
            self.le({p: 2, x[2]: -1, x[3]: -1})  # p <= (x2+x3)/2
        elif move == "pinch":
            a = f"{p}_a"
            b = f"{p}_b"
            raw = [{a: 1}, {a: 1}, {a: 1}, {b: 1}]
            self.le({a: 1, x[0]: -1})  # a <= x0
            self.le({a: 1, b: -1})  # b >= a
            self.le({a: 2, b: 1, x[1]: -1, x[2]: -1, x[3]: -1})
        elif move == "double_pinch":
            a = f"{p}_a"
            b = f"{p}_b"
            raw = [{x[0]: 2, a: -1}, {a: 1}, {a: 1}, {b: 1}]
            self.le({a: -1, x[0]: 1})  # a >= x0
            self.le({a: 2, x[1]: -1, x[2]: -1})
            self.le({a: 1, b: -1})  # b >= a
            self.le({a: 3, b: 1, x[0]: -1, x[1]: -1, x[2]: -1, x[3]: -1})
        else:
            raise ValueError(move)

        for i, expr in enumerate(raw):
            self.set_expr(y[i], expr)
        self.add_sorted(f"x{t+1}_")

    def build(self) -> None:
        d = len(self.word)
        for t in range(d + 1):
            for i in range(4):
                self.var(f"x{t}_{i}")
        for t in range(d + 1):
            self.add_sorted(f"x{t}_")
        if self.fixed_start is not None:
            for i, value in enumerate(self.fixed_start):
                self.eq({f"x0_{i}": 1.0}, float(value))
        if self.fixed_end is not None:
            for i, value in enumerate(self.fixed_end):
                self.eq({f"x{d}_{i}": 1.0}, float(value))
        for t, move in enumerate(self.word):
            self.add_move(move, t)

    def solve_max_endpoint_form(
        self,
        fixed_other: tuple[float, ...],
        form: tuple[int, int, int],
        side: str,
    ) -> LPOpt:
        self.build()
        d = len(self.word)
        c = np.zeros(len(self.names))
        k, j, ell = form
        coeff = float(k - j) / float(ell - j)
        if side == "post":
            # Max Estimate exponent for R_STRESS -> endpoint.
            src = fixed_other
            for i in range(j):
                c[self.idx[f"x{d}_{i}"]] -= 1.0
            for i in range(j, ell):
                c[self.idx[f"x{d}_{i}"]] -= coeff
            const = -sum(src[:j]) - coeff * sum(src[j:ell])
        elif side == "pre":
            # Max Estimate exponent for endpoint -> S_STRESS.
            dst = fixed_other
            for i in range(j):
                c[self.idx[f"x0_{i}"]] += 1.0
            for i in range(j, ell):
                c[self.idx[f"x0_{i}"]] += coeff
            const = sum(dst[:j]) + coeff * sum(dst[j:ell])
        else:
            raise ValueError(side)

        self.resize_rows()
        bounds = [(-self.bound, self.bound) for _ in self.names]
        res = linprog(
            c,
            A_ub=np.array(self.a_ub) if self.a_ub else None,
            b_ub=np.array(self.b_ub) if self.b_ub else None,
            A_eq=np.array(self.a_eq) if self.a_eq else None,
            b_eq=np.array(self.b_eq) if self.b_eq else None,
            bounds=bounds,
            method="highs",
        )
        if not res.success:
            return LPOpt(side, self.word, form, float("nan"), res.message, None)
        endpoint_prefix = f"x{d}_" if side == "post" else "x0_"
        endpoint = tuple(float(res.x[self.idx[f"{endpoint_prefix}{i}"]]) for i in range(4))
        value = -float(res.fun) + const
        return LPOpt(side, self.word, form, value, "ok", endpoint)  # type: ignore[arg-type]


def optimize_word(side: str, word: tuple[str, ...], form: tuple[int, int, int], bound: float) -> LPOpt:
    if side == "post":
        builder = Builder(word, fixed_start=S_STRESS, fixed_end=None, bound=bound)
        return builder.solve_max_endpoint_form(R_STRESS, form, side)
    if side == "pre":
        builder = Builder(word, fixed_start=None, fixed_end=R_STRESS, bound=bound)
        return builder.solve_max_endpoint_form(S_STRESS, form, side)
    raise ValueError(side)


def scan(side: str, max_depth: int, bound: float) -> tuple[list[LPOpt], int]:
    best: list[LPOpt] = []
    count = 0
    for depth in range(max_depth + 1):
        for word in product(MOVE_TYPES, repeat=depth):
            for form in ESTIMATE_FORMS:
                count += 1
                opt = optimize_word(side, tuple(word), form, bound)
                if opt.status == "ok":
                    best.append(opt)
                    best.sort(key=lambda item: item.value, reverse=True)
                    del best[20:]
    return best, count


def lines_for_best(title: str, best: list[LPOpt], count: int) -> list[str]:
    out = [f"## {title}", f"LP objectives solved: {count}"]
    if not best:
        out.append("No feasible LPs.")
        return out
    positives = [item for item in best if item.value > 1e-7]
    out.append(f"best Estimate-1 exponent = {fmt(best[0].value)}; positive objectives in retained top list = {len(positives)}")
    for item in best[:8]:
        word = " -> ".join(item.word) if item.word else "(no auxiliary map)"
        out.append(
            f"{item.side:4s} word={word:70s} form(k,j,l)={item.form} "
            f"value={fmt(item.value)} endpoint={fmt_vec(item.endpoint or ())}"
        )
    return out


def main() -> None:
    out: list[str] = []
    out.append("# Round 27 auxiliary-composition LP")
    out.append("")
    out.append(f"R stress exponents = {fmt_vec(R_STRESS)}")
    out.append(f"S stress exponents = {fmt_vec(S_STRESS)}")
    out.append(f"badness exponents = {fmt_vec(badness(R_STRESS, S_STRESS))}")
    out.append("")
    out.append("Direct Guth Estimate 1 exponents for R -> S:")
    direct = all_estimate_exponents(R_STRESS, S_STRESS)
    for form, value in direct:
        out.append(f"  form(k,j,l)={form}: {fmt(value)}")
    out.append(f"  maximum direct exponent = {fmt(max(value for _, value in direct))}")
    out.append("")
    out.append("Move set: " + ", ".join(MOVE_TYPES))
    out.append("Technical interpolation uses one parameter A; no independent lambda/output-A variant is allowed.")
    out.append("")

    for depth in (1, 2, 3):
        post_best, post_count = scan("post", depth, bound=8.0)
        pre_best, pre_count = scan("pre", depth, bound=8.0)
        out.extend(lines_for_best(f"postcomposition search depth <= {depth}", post_best, post_count))
        out.append("")
        out.extend(lines_for_best(f"precomposition search depth <= {depth}", pre_best, pre_count))
        out.append("")

    path = Path("data/round27")
    path.mkdir(parents=True, exist_ok=True)
    (path / "aux_composition_lp_report.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
