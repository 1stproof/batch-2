#!/usr/bin/env python3
"""Round 17 shifted down-set enumeration and LP diagnostics.

The main LP used here is the dual separation test

    p 1 notin P(D)
      iff min_{c_i >= 0, sum c_i = 1} max_{A in D} c(A) < p.

For a down-set it is enough to constrain the maximal faces.  For shifted
families the script also asks for nondecreasing separating weights
c_1 <= ... <= c_n; this agrees with the unrestricted optimum in the checked
range and gives readable certificates.
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, Iterator, List, Sequence, Tuple

import numpy as np
from scipy.optimize import linprog


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from compute_utils import safe_json_dump

DATA_DIR = ROOT / "data" / "round17"
P_GRID: Tuple[Fraction, ...] = (
    Fraction(1, 6),
    Fraction(1, 5),
    Fraction(1, 4),
    Fraction(3, 10),
    Fraction(1, 3),
)
TOL = 1e-9


def bit_count(x: int) -> int:
    return int(x.bit_count())


@lru_cache(None)
def masks_k(n: int, k: int) -> Tuple[int, ...]:
    out: List[int] = []
    for comb in combinations(range(n), k):
        mask = 0
        for i in comb:
            mask |= 1 << i
        out.append(mask)
    return tuple(out)


@lru_cache(None)
def shifted_same_size_predecessors(n: int, mask: int) -> FrozenSet[int]:
    pred = set()
    for j in range(n):
        if not ((mask >> j) & 1):
            continue
        for i in range(j):
            if not ((mask >> i) & 1):
                pred.add((mask & ~(1 << j)) | (1 << i))
    return frozenset(pred)


@lru_cache(None)
def shifted_ideals_in_allowed(n: int, allowed_tuple: Tuple[int, ...]) -> Tuple[FrozenSet[int], ...]:
    """All shifted ideals inside one uniform layer."""
    allowed = set(allowed_tuple)
    elems = tuple(sorted(allowed, key=lambda m: (bit_count(m), m)))
    preds = {m: shifted_same_size_predecessors(n, m) & allowed for m in elems}
    ideals: List[FrozenSet[int]] = []

    def rec(idx: int, inc: set[int]) -> None:
        if idx == len(elems):
            ideals.append(frozenset(inc))
            return
        x = elems[idx]
        rec(idx + 1, inc)
        if preds[x] <= inc:
            inc.add(x)
            rec(idx + 1, inc)
            inc.remove(x)

    rec(0, set())
    return tuple(ideals)


def enumerate_shifted_complexes(n: int) -> Iterator[FrozenSet[int]]:
    """Enumerate shifted simplicial complexes on [n], always including empty."""

    def rec(k: int, previous_layer: FrozenSet[int], all_faces: FrozenSet[int]) -> Iterator[FrozenSet[int]]:
        if k > n:
            yield all_faces
            return
        candidates: List[int] = []
        for mask in masks_k(n, k):
            ok = True
            s = mask
            while s:
                b = s & -s
                if (mask ^ b) not in previous_layer:
                    ok = False
                    break
                s -= b
            if ok:
                candidates.append(mask)
        for layer in shifted_ideals_in_allowed(n, tuple(candidates)):
            yield from rec(k + 1, layer, frozenset(set(all_faces) | set(layer)))

    yield from rec(1, frozenset({0}), frozenset({0}))


def enumerate_all_complexes(n: int) -> Iterator[FrozenSet[int]]:
    """Enumerate all simplicial complexes on [n], for small compression checks."""

    def all_subsets(items: Sequence[int]) -> Iterator[FrozenSet[int]]:
        m = len(items)
        for choice in range(1 << m):
            yield frozenset(items[i] for i in range(m) if (choice >> i) & 1)

    def rec(k: int, previous_layer: FrozenSet[int], all_faces: FrozenSet[int]) -> Iterator[FrozenSet[int]]:
        if k > n:
            yield all_faces
            return
        candidates: List[int] = []
        for mask in masks_k(n, k):
            ok = True
            s = mask
            while s:
                b = s & -s
                if (mask ^ b) not in previous_layer:
                    ok = False
                    break
                s -= b
            if ok:
                candidates.append(mask)
        for layer in all_subsets(candidates):
            yield from rec(k + 1, layer, frozenset(set(all_faces) | set(layer)))

    yield from rec(1, frozenset({0}), frozenset({0}))


def facets(faces: FrozenSet[int], n: int) -> Tuple[int, ...]:
    out = []
    for mask in faces:
        is_facet = True
        for i in range(n):
            if not ((mask >> i) & 1) and (mask | (1 << i)) in faces:
                is_facet = False
                break
        if is_facet:
            out.append(mask)
    return tuple(sorted(out, key=lambda m: (bit_count(m), m)))


def f_vector(faces: FrozenSet[int], n: int) -> Tuple[int, ...]:
    counts = [0] * (n + 1)
    for mask in faces:
        counts[bit_count(mask)] += 1
    return tuple(counts)


def mu_from_fvector(fv: Sequence[int], p: Fraction, n: int) -> Fraction:
    q = 1 - p
    ans = Fraction(0)
    for k, count in enumerate(fv):
        ans += count * (p**k) * (q ** (n - k))
    return ans


def mask_str(mask: int, n: int) -> str:
    if mask == 0:
        return "{}"
    return "".join(str(i + 1) for i in range(n) if (mask >> i) & 1)


def masks_str(masks: Sequence[int], n: int) -> List[str]:
    return [mask_str(m, n) for m in masks]


def is_last_vertex_dictatorship(faces: FrozenSet[int], n: int) -> bool:
    last = 1 << (n - 1)
    return faces == frozenset(mask for mask in range(1 << n) if not (mask & last))


@dataclass(frozen=True)
class Separator:
    optimum: float
    weights: Tuple[float, ...]
    success: bool
    message: str = ""


_sep_cache: Dict[Tuple[int, Tuple[int, ...], bool], Separator] = {}


def separator_lp(n: int, facet_tuple: Tuple[int, ...], monotone: bool = True) -> Separator:
    """Minimize max facet weight with sum weights one."""
    key = (n, facet_tuple, monotone)
    if key in _sep_cache:
        return _sep_cache[key]

    # variables are c_0,...,c_{n-1},t
    objective = np.zeros(n + 1)
    objective[-1] = 1.0
    a_ub: List[List[float]] = []
    b_ub: List[float] = []
    for face in facet_tuple:
        row = np.zeros(n + 1)
        for i in range(n):
            if (face >> i) & 1:
                row[i] = 1.0
        row[-1] = -1.0
        a_ub.append(row.tolist())
        b_ub.append(0.0)
    if monotone:
        for i in range(n - 1):
            row = np.zeros(n + 1)
            row[i] = 1.0
            row[i + 1] = -1.0
            a_ub.append(row.tolist())
            b_ub.append(0.0)
    a_eq = np.zeros((1, n + 1))
    a_eq[0, :n] = 1.0
    b_eq = np.array([1.0])
    bounds = [(0.0, None)] * n + [(0.0, None)]
    res = linprog(
        objective,
        A_ub=np.array(a_ub) if a_ub else None,
        b_ub=np.array(b_ub) if b_ub else None,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        sep = Separator(float("nan"), tuple(), False, res.message)
    else:
        sep = Separator(float(res.fun), tuple(float(x) for x in res.x[:n]), True, res.message)
    _sep_cache[key] = sep
    return sep


def member_p1(n: int, face_set: FrozenSet[int], p: Fraction, monotone: bool = True) -> bool:
    sep = separator_lp(n, facets(face_set, n), monotone=monotone)
    if not sep.success:
        raise RuntimeError(sep.message)
    return sep.optimum + TOL >= float(p)


def rationalize_weights(weights: Sequence[float], max_den: int = 240) -> List[str]:
    fracs = [Fraction(max(0.0, w)).limit_denominator(max_den) for w in weights]
    total = sum(fracs, Fraction(0))
    if total == 0:
        return [str(f) for f in fracs]
    fracs = [f / total for f in fracs]
    return [str(f) for f in fracs]


def compression(faces: FrozenSet[int], n: int, i: int, j: int) -> FrozenSet[int]:
    out = set()
    for face in faces:
        if ((face >> j) & 1) and not ((face >> i) & 1):
            moved = (face & ~(1 << j)) | (1 << i)
            out.add(moved if moved not in faces else face)
        else:
            out.add(face)
    return frozenset(out)


def shifted_extremal_scan(max_n: int = 7) -> Tuple[dict, Dict[int, List[FrozenSet[int]]]]:
    complexes_by_n: Dict[int, List[FrozenSet[int]]] = {}
    summary: dict = {"p_grid": [str(p) for p in P_GRID], "by_n": {}, "global_by_p": {}}

    global_best: Dict[Fraction, Tuple[Fraction, int, List[dict], Fraction | None]] = {}
    for p in P_GRID:
        global_best[p] = (Fraction(-1), -1, [], None)

    for n in range(1, max_n + 1):
        complexes = list(enumerate_shifted_complexes(n))
        complexes_by_n[n] = complexes
        by_p = {}
        for p in P_GRID:
            q = 1 - p
            best_mu = Fraction(-1)
            second_mu: Fraction | None = None
            best_examples: List[dict] = []
            nonmember_count = 0
            member_count = 0
            dictatorship_seen = False
            for faces in complexes:
                fv = f_vector(faces, n)
                mu = mu_from_fvector(fv, p, n)
                sep = separator_lp(n, facets(faces, n), monotone=True)
                if not sep.success:
                    raise RuntimeError(sep.message)
                is_member = sep.optimum + TOL >= float(p)
                if is_member:
                    member_count += 1
                    continue
                nonmember_count += 1
                is_dict = is_last_vertex_dictatorship(faces, n)
                dictatorship_seen = dictatorship_seen or is_dict
                if mu > best_mu:
                    if best_mu >= 0:
                        second_mu = best_mu if second_mu is None else max(second_mu, best_mu)
                    best_mu = mu
                    best_examples = []
                elif mu < best_mu:
                    second_mu = mu if second_mu is None else max(second_mu, mu)
                if mu == best_mu and len(best_examples) < 10:
                    fs = facets(faces, n)
                    best_examples.append(
                        {
                            "facets": masks_str(fs, n),
                            "f_vector": list(fv),
                            "separator_optimum": sep.optimum,
                            "separator_weights": rationalize_weights(sep.weights),
                            "is_last_vertex_dictatorship": is_dict,
                        }
                    )
            by_p[str(p)] = {
                "q": str(q),
                "total_shifted": len(complexes),
                "member_count": member_count,
                "nonmember_count": nonmember_count,
                "best_mu": str(best_mu),
                "best_mu_float": float(best_mu),
                "best_equals_q": best_mu == q,
                "best_example_count_recorded": len(best_examples),
                "best_examples": best_examples,
                "second_best_mu": None if second_mu is None else str(second_mu),
                "second_best_gap_from_q": None if second_mu is None else str(q - second_mu),
                "dictatorship_seen_among_nonmembers": dictatorship_seen,
            }
            g_best, g_n, g_examples, g_second = global_best[p]
            if best_mu > g_best:
                global_best[p] = (best_mu, n, best_examples[:], second_mu)
            elif best_mu < g_best:
                new_second = best_mu if g_second is None else max(g_second, best_mu)
                global_best[p] = (g_best, g_n, g_examples, new_second)
        summary["by_n"][str(n)] = {"shifted_count": len(complexes), "by_p": by_p}

    for p, (best_mu, n, examples, second_mu) in global_best.items():
        q = 1 - p
        summary["global_by_p"][str(p)] = {
            "q": str(q),
            "best_mu": str(best_mu),
            "best_mu_float": float(best_mu),
            "best_n": n,
            "best_equals_q": best_mu == q,
            "examples": examples,
            "second_best_mu_across_n_when_tracked": None if second_mu is None else str(second_mu),
        }
    return summary, complexes_by_n


def slice_sections(faces: FrozenSet[int], n_total: int) -> Tuple[FrozenSet[int], FrozenSet[int]]:
    """Return E,F on the first n_total-1 vertices."""
    last = 1 << (n_total - 1)
    e_faces = frozenset(face for face in faces if not (face & last))
    f_faces = frozenset(face & ~last for face in faces if face & last)
    return e_faces, f_faces


def mixed_slice_scan(complexes_by_n: Dict[int, List[FrozenSet[int]]], max_total_n: int = 7) -> dict:
    out: dict = {"p_grid": [str(p) for p in P_GRID], "by_total_n": {}, "counterexamples": []}
    for total_n in range(2, max_total_n + 1):
        records_by_p = {}
        for p in P_GRID:
            lam = p / (1 - p)
            mixed_count = 0
            implication_counterexamples: List[dict] = []
            max_score = Fraction(-1)
            max_score_nonmember_mixed = Fraction(-1)
            max_score_examples: List[dict] = []
            for faces in complexes_by_n[total_n]:
                e_faces, f_faces = slice_sections(faces, total_n)
                mem_e = member_p1(total_n - 1, e_faces, p, monotone=True)
                if not mem_e:
                    continue
                mem_f = member_p1(total_n - 1, f_faces, p, monotone=True)
                if mem_f:
                    continue
                mu_e = mu_from_fvector(f_vector(e_faces, total_n - 1), p, total_n - 1)
                mu_f = mu_from_fvector(f_vector(f_faces, total_n - 1), p, total_n - 1)
                score = mu_e + lam * mu_f
                mem_d = member_p1(total_n, faces, p, monotone=True)
                if not mem_d and score > max_score_nonmember_mixed:
                    max_score_nonmember_mixed = score
                if score > 1:
                    mixed_count += 1
                    if score > max_score:
                        max_score = score
                        max_score_examples = []
                    if score == max_score and len(max_score_examples) < 5:
                        max_score_examples.append(
                            {
                                "facets_D": masks_str(facets(faces, total_n), total_n),
                                "facets_E": masks_str(facets(e_faces, total_n - 1), total_n - 1),
                                "facets_F": masks_str(facets(f_faces, total_n - 1), total_n - 1),
                                "score": str(score),
                                "mu_E": str(mu_e),
                                "mu_F": str(mu_f),
                                "member_D": mem_d,
                            }
                        )
                    if not mem_d:
                        rec = {
                            "total_n": total_n,
                            "p": str(p),
                            "facets_D": masks_str(facets(faces, total_n), total_n),
                            "facets_E": masks_str(facets(e_faces, total_n - 1), total_n - 1),
                            "facets_F": masks_str(facets(f_faces, total_n - 1), total_n - 1),
                            "score": str(score),
                            "mu_E": str(mu_e),
                            "mu_F": str(mu_f),
                        }
                        implication_counterexamples.append(rec)
                        out["counterexamples"].append(rec)
            records_by_p[str(p)] = {
                "mixed_score_gt_1_count": mixed_count,
                "counterexample_count": len(implication_counterexamples),
                "max_score_gt_1": None if max_score < 0 else str(max_score),
                "max_score_gt_1_examples": max_score_examples,
                "max_score_among_mixed_nonmember_D": None
                if max_score_nonmember_mixed < 0
                else str(max_score_nonmember_mixed),
            }
        out["by_total_n"][str(total_n)] = records_by_p
    return out


def compression_sanity(max_n: int = 5) -> dict:
    """Brute-force the compression contrapositive on all complexes up to max_n."""
    out: dict = {"p_grid": [str(p) for p in P_GRID], "by_n": {}, "failures": []}
    for n in range(1, max_n + 1):
        complexes = list(enumerate_all_complexes(n))
        checked = 0
        for faces in complexes:
            for i in range(n):
                for j in range(i + 1, n):
                    cfaces = compression(faces, n, i, j)
                    checked += 1
                    for p in P_GRID:
                        mem_c = member_p1(n, cfaces, p, monotone=False)
                        if mem_c and not member_p1(n, faces, p, monotone=False):
                            out["failures"].append(
                                {
                                    "n": n,
                                    "p": str(p),
                                    "i": i + 1,
                                    "j": j + 1,
                                    "facets_D": masks_str(facets(faces, n), n),
                                    "facets_CD": masks_str(facets(cfaces, n), n),
                                }
                            )
                            break
        out["by_n"][str(n)] = {"complex_count": len(complexes), "pair_checks": checked}
    return out


def write_markdown(summary: dict, mixed: dict, compression: dict) -> None:
    lines: List[str] = []
    lines.append("# Round 17 shifted enumeration summary\n")
    lines.append("## Shifted complex counts\n")
    lines.append("| n | shifted complexes |")
    lines.append("|---:|---:|")
    for n, rec in summary["by_n"].items():
        lines.append(f"| {n} | {rec['shifted_count']} |")
    lines.append("")

    lines.append("## Extremal non-convex shifted families\n")
    for p in summary["p_grid"]:
        lines.append(f"### p = {p}\n")
        lines.append("| n | nonmembers | best mu | equals q? | second best gap from q | best facets | separator weights |")
        lines.append("|---:|---:|---:|:---:|---:|---|---|")
        for n, nrec in summary["by_n"].items():
            prec = nrec["by_p"][p]
            ex = prec["best_examples"][0] if prec["best_examples"] else {}
            facets_txt = ", ".join(ex.get("facets", []))
            weights_txt = ", ".join(ex.get("separator_weights", []))
            lines.append(
                f"| {n} | {prec['nonmember_count']} | {prec['best_mu']} | "
                f"{'yes' if prec['best_equals_q'] else 'NO'} | "
                f"{prec['second_best_gap_from_q']} | {facets_txt} | {weights_txt} |"
            )
        lines.append("")

    lines.append("## Mixed-slice implication scan\n")
    lines.append("Each row counts shifted D on total_n vertices with p1 in P(E), p1 notin P(F), and mu(E)+lambda mu(F)>1.")
    lines.append("")
    lines.append("| total_n | p | score>1 cases | counterexamples | max score | max score among mixed D nonmembers |")
    lines.append("|---:|---:|---:|---:|---:|---:|")
    for total_n, nrec in mixed["by_total_n"].items():
        for p, prec in nrec.items():
            lines.append(
                f"| {total_n} | {p} | {prec['mixed_score_gt_1_count']} | "
                f"{prec['counterexample_count']} | {prec['max_score_gt_1']} | "
                f"{prec['max_score_among_mixed_nonmember_D']} |"
            )
    lines.append("")
    lines.append(f"Compression sanity failures: {len(compression['failures'])}.")
    lines.append("")
    (DATA_DIR / "shifted_extremal_table.md").write_text("\n".join(lines))


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    summary, complexes_by_n = shifted_extremal_scan(max_n=7)
    mixed = mixed_slice_scan(complexes_by_n, max_total_n=7)
    comp = compression_sanity(max_n=5)
    safe_json_dump(summary, DATA_DIR / "shifted_enum_summary.json", indent=2)
    safe_json_dump(mixed, DATA_DIR / "mixed_slice_scan.json", indent=2)
    safe_json_dump(comp, DATA_DIR / "compression_sanity.json", indent=2)
    write_markdown(summary, mixed, comp)
    print(f"wrote {DATA_DIR}")
    print("shifted counts:", {n: rec["shifted_count"] for n, rec in summary["by_n"].items()})
    print("compression failures:", len(comp["failures"]))
    print("mixed counterexamples:", len(mixed["counterexamples"]))


if __name__ == "__main__":
    main()
