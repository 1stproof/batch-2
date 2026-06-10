#!/usr/bin/env python3
"""Round 9 exact and heuristic checks for the small-p Bernoulli problem.

The script is intentionally self-contained and uses exact integer/Fraction
arithmetic for the reported grid certificates.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
import json
import random
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "round9"
DATA.mkdir(parents=True, exist_ok=True)


P_VALUES = [
    Fraction(1, 6),
    Fraction(1, 5),
    Fraction(1, 4),
    Fraction(2, 7),
    Fraction(3, 10),
    Fraction(1, 3),
]


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def ffloat(x: Fraction) -> float:
    return float(x)


def subsets_sums_units(parts: tuple[int, ...]) -> list[int]:
    sums = [0]
    for w in parts:
        sums += [s + w for s in sums]
    return sums


def unitgap_margin_units(parts: tuple[int, ...], denom: int, p: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return (good, bad, margin) for b_i=parts_i/denom.

    S=sum b_i zeta_i.  Good is S >= p(B+1), bad is S < p(B+1)-1.
    """
    n = len(parts)
    a, b = p.numerator, p.denominator
    qnum = b - a
    total_units = sum(parts)
    sums = subsets_sums_units(parts)

    good_num = 0
    bad_num = 0
    # Probability numerator for a subset with k successes is a^k qnum^(n-k).
    pow_a = [a**k for k in range(n + 1)]
    pow_q = [qnum**k for k in range(n + 1)]
    rhs_good = a * (total_units + denom)
    rhs_bad = a * (total_units + denom) - b * denom
    for mask, su in enumerate(sums):
        k = mask.bit_count()
        prob_num = pow_a[k] * pow_q[n - k]
        if b * su >= rhs_good:
            good_num += prob_num
        if b * su < rhs_bad:
            bad_num += prob_num
    den = b**n
    good = Fraction(good_num, den)
    bad = Fraction(bad_num, den)
    margin = good - Fraction(a, qnum) * bad
    return good, bad, margin


def unitgap_grid_search(denoms: list[int], nmax: int) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for p in P_VALUES:
        q = 1 - p
        for denom in denoms:
            for n in range(1, nmax + 1):
                if n <= q / p:
                    continue
                best: tuple[Fraction, tuple[int, ...], Fraction, Fraction] | None = None
                tested = 0
                strict_total = 0
                for parts in combinations_with_replacement(range(1, denom + 1), n):
                    tested += 1
                    # Lower tail can only be nonempty if B > q/p.
                    if Fraction(sum(parts), denom) <= q / p:
                        continue
                    strict_total += 1
                    good, bad, margin = unitgap_margin_units(parts, denom, p)
                    if best is None or margin < best[0]:
                        best = (margin, parts, good, bad)
                if best is None:
                    continue
                margin, parts, good, bad = best
                records.append(
                    {
                        "p": fstr(p),
                        "denom": denom,
                        "n": n,
                        "tested_sorted_positive_vectors": tested,
                        "tested_with_B_gt_q_over_p": strict_total,
                        "min_margin": fstr(margin),
                        "min_margin_float": ffloat(margin),
                        "good": fstr(good),
                        "bad": fstr(bad),
                        "B": fstr(Fraction(sum(parts), denom)),
                        "parts_over_denom": [int(x) for x in parts],
                        "weights": [fstr(Fraction(x, denom)) for x in parts],
                    }
                )
    return records


def unitgap_random_search(trials: int, seed: int = 90210) -> list[dict[str, object]]:
    rng = random.Random(seed)
    records: list[dict[str, object]] = []
    for p in P_VALUES:
        q = 1 - p
        best: tuple[Fraction, tuple[int, ...], int, Fraction, Fraction] | None = None
        tested = 0
        for _ in range(trials):
            denom = rng.choice([24, 30, 36, 42, 60])
            n = rng.randint(max(2, int(q / p) + 1), 14)
            parts = tuple(sorted((rng.randint(1, denom) for _ in range(n))))
            if Fraction(sum(parts), denom) <= q / p:
                # Lift random coordinates until the lower tail is at least possible.
                parts_list = list(parts)
                attempts = 0
                while Fraction(sum(parts_list), denom) <= q / p and attempts < 5 * n:
                    j = rng.randrange(n)
                    if parts_list[j] < denom:
                        parts_list[j] += 1
                    attempts += 1
                parts = tuple(sorted(parts_list))
            if Fraction(sum(parts), denom) <= q / p:
                continue
            tested += 1
            good, bad, margin = unitgap_margin_units(parts, denom, p)
            if best is None or margin < best[0]:
                best = (margin, parts, denom, good, bad)
        if best is not None:
            margin, parts, denom, good, bad = best
            records.append(
                {
                    "p": fstr(p),
                    "tested": tested,
                    "min_margin": fstr(margin),
                    "min_margin_float": ffloat(margin),
                    "good": fstr(good),
                    "bad": fstr(bad),
                    "denom": denom,
                    "n": len(parts),
                    "B": fstr(Fraction(sum(parts), denom)),
                    "parts_over_denom": [int(x) for x in parts],
                    "weights": [fstr(Fraction(x, denom)) for x in parts],
                }
            )
    return records


def partitions_of(n: int, max_part: int | None = None) -> Iterable[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions_of(n - first, first):
            yield (first,) + rest


def dist_units_fraction(parts: tuple[int, ...], p: Fraction) -> dict[int, Fraction]:
    dist: dict[int, Fraction] = {0: Fraction(1)}
    q = 1 - p
    for w in parts:
        nxt: dict[int, Fraction] = defaultdict(Fraction)
        for s, pr in dist.items():
            nxt[s] += pr * q
            nxt[s + w] += pr * p
        dist = dict(nxt)
    return dist


def phi_failure_units(parts: tuple[int, ...], denom: int, p: Fraction) -> Fraction:
    """Phi_q in failure variables: P_p[w(F)<p] for weights parts/denom."""
    a, b = p.numerator, p.denominator
    dist = dist_units_fraction(parts, p)
    return sum(pr for s, pr in dist.items() if b * s < a * denom)


def endpoint_influence_units(parts: tuple[int, ...], denom: int, p: Fraction) -> Fraction:
    """Total p-biased influence of D={A:w(A)<p}."""
    a, b = p.numerator, p.denominator
    total = Fraction(0)
    multiplicities: dict[int, int] = defaultdict(int)
    for w in parts:
        multiplicities[w] += 1
    for w, mult in multiplicities.items():
        rest = list(parts)
        rest.remove(w)
        dist = dist_units_fraction(tuple(rest), p)
        piv = sum(
            pr
            for s, pr in dist.items()
            if b * s < a * denom and b * (s + w) >= a * denom
        )
        total += mult * piv
    return total


def influence_grid_search(denoms: list[int]) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for p in P_VALUES:
        for denom in denoms:
            best_all: tuple[Fraction, tuple[int, ...]] | None = None
            best_capped: tuple[Fraction, tuple[int, ...]] | None = None
            count = 0
            capped_count = 0
            for parts in partitions_of(denom):
                count += 1
                inf = endpoint_influence_units(parts, denom, p)
                if best_all is None or inf < best_all[0]:
                    best_all = (inf, parts)
                if max(parts) * p.denominator < p.numerator * denom:
                    capped_count += 1
                    if best_capped is None or inf < best_capped[0]:
                        best_capped = (inf, parts)
            rec: dict[str, object] = {
                "p": fstr(p),
                "denom": denom,
                "partitions": count,
                "min_influence_all": fstr(best_all[0]) if best_all else None,
                "min_influence_all_minus_1": fstr(best_all[0] - 1) if best_all else None,
                "min_all_parts": list(best_all[1]) if best_all else None,
                "capped_partitions": capped_count,
            }
            if best_capped:
                rec.update(
                    {
                        "min_influence_capped": fstr(best_capped[0]),
                        "min_influence_capped_minus_1": fstr(best_capped[0] - 1),
                        "min_capped_parts": list(best_capped[1]),
                        "min_capped_weights": [
                            fstr(Fraction(x, denom)) for x in best_capped[1]
                        ],
                    }
                )
            records.append(rec)
    return records


def coalesce_block(parts: tuple[int, ...], block: tuple[int, ...]) -> tuple[int, ...]:
    block_set = set(block)
    new_parts = [parts[i] for i in range(len(parts)) if i not in block_set]
    new_parts.append(sum(parts[i] for i in block))
    return tuple(sorted(new_parts, reverse=True))


def block_and_pair_search(denoms: list[int], max_n: int = 11) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for p in P_VALUES:
        q = 1 - p
        for denom in denoms:
            best_block: tuple[Fraction, tuple[int, ...], Fraction, tuple[int, ...] | None] | None = None
            best_pair_negative_margin: tuple[Fraction, tuple[int, ...], Fraction, Fraction] | None = None
            counter_block = None
            counter_pair_dichotomy = None
            checked = 0
            capped_checked = 0
            all_pair_negative_count = 0
            for parts in partitions_of(denom):
                if len(parts) < 3 or len(parts) > max_n:
                    continue
                checked += 1
                # Nontrivial capped regime w_i < p.
                if max(parts) * p.denominator >= p.numerator * denom:
                    continue
                capped_checked += 1
                base = phi_failure_units(parts, denom, p)
                max_pair_gain: Fraction | None = None
                max_block_gain: Fraction | None = None
                max_block: tuple[int, ...] | None = None
                for r in range(2, len(parts)):
                    for block in combinations(range(len(parts)), r):
                        gain = phi_failure_units(coalesce_block(parts, block), denom, p) - base
                        if r == 2 and (max_pair_gain is None or gain > max_pair_gain):
                            max_pair_gain = gain
                        if max_block_gain is None or gain > max_block_gain:
                            max_block_gain = gain
                            max_block = block
                if max_block_gain is None:
                    continue
                if best_block is None or max_block_gain < best_block[0]:
                    best_block = (max_block_gain, parts, base, max_block)
                if max_block_gain < 0 and counter_block is None:
                    counter_block = (max_block_gain, parts, base, max_block)
                if max_pair_gain is not None and max_pair_gain < 0:
                    all_pair_negative_count += 1
                    gap = q - base
                    if best_pair_negative_margin is None or gap < best_pair_negative_margin[0]:
                        best_pair_negative_margin = (gap, parts, base, max_pair_gain)
                    if base > q and counter_pair_dichotomy is None:
                        counter_pair_dichotomy = (parts, base, max_pair_gain)
            rec: dict[str, object] = {
                "p": fstr(p),
                "q": fstr(q),
                "denom": denom,
                "checked_partitions_len_3_to_max_n": checked,
                "capped_checked": capped_checked,
                "all_pair_negative_count": all_pair_negative_count,
                "proper_block_counterexample": None,
                "pair_dichotomy_counterexample": None,
            }
            if best_block:
                max_gain, parts, base, block = best_block
                rec.update(
                    {
                        "smallest_max_proper_block_gain": fstr(max_gain),
                        "smallest_max_proper_block_gain_float": ffloat(max_gain),
                        "block_witness_parts": list(parts),
                        "block_witness_weights": [fstr(Fraction(x, denom)) for x in parts],
                        "block_witness_phi": fstr(base),
                        "best_block_indices": list(block) if block is not None else None,
                        "best_block_weight": fstr(sum(parts[i] for i in block) / Fraction(denom))
                        if block is not None
                        else None,
                    }
                )
            if counter_block:
                max_gain, parts, base, block = counter_block
                rec["proper_block_counterexample"] = {
                    "max_gain": fstr(max_gain),
                    "parts": list(parts),
                    "weights": [fstr(Fraction(x, denom)) for x in parts],
                    "phi": fstr(base),
                    "best_block_indices": list(block) if block is not None else None,
                }
            if best_pair_negative_margin:
                gap, parts, base, max_pair = best_pair_negative_margin
                rec.update(
                    {
                        "min_q_minus_phi_among_all_pair_negative": fstr(gap),
                        "min_q_minus_phi_float": ffloat(gap),
                        "pair_negative_witness_parts": list(parts),
                        "pair_negative_witness_weights": [
                            fstr(Fraction(x, denom)) for x in parts
                        ],
                        "pair_negative_phi": fstr(base),
                        "max_pair_gain_for_witness": fstr(max_pair),
                    }
                )
            if counter_pair_dichotomy:
                parts, base, max_pair = counter_pair_dichotomy
                rec["pair_dichotomy_counterexample"] = {
                    "parts": list(parts),
                    "weights": [fstr(Fraction(x, denom)) for x in parts],
                    "phi": fstr(base),
                    "max_pair_gain": fstr(max_pair),
                }
            records.append(rec)
    return records


def equal_weight_pair_trap_table(nmax: int = 12) -> list[dict[str, object]]:
    rows = []
    for n in range(4, nmax + 1):
        # Choose a rational point strictly in 1/n < p < 1/(n-1).
        p = Fraction(1, n) + Fraction(1, 3) * (Fraction(1, n - 1) - Fraction(1, n))
        if p > Fraction(1, 3):
            continue
        q = 1 - p
        phi = q**n + n * p * q ** (n - 1)
        pair_gain = p * q ** (n - 2) * (n - 2 - (n - 1) * q)
        rows.append(
            {
                "n": n,
                "p": fstr(p),
                "q": fstr(q),
                "phi": fstr(phi),
                "q_minus_phi": fstr(q - phi),
                "pair_gain_each": fstr(pair_gain),
            }
        )
    return rows


def bellman_boundary_diagnostic() -> list[dict[str, object]]:
    """Small exact diagnostic for the shifted one-parameter invariant.

    The shifted claim P[S>=x+p] >= (p/q)P[S<x-q] is closed under conditioning,
    but the zero-variable terminal condition already fails for x>q.  This table
    records the terminal value and a simple one-step value at representative x.
    """
    rows = []
    for p in [Fraction(1, 5), Fraction(1, 4), Fraction(3, 10), Fraction(1, 3)]:
        q = 1 - p
        lam = p / q
        for x in [q - Fraction(1, 10), q, q + Fraction(1, 10), 1]:
            terminal = Fraction(1 if 0 >= x + p else 0) - lam * Fraction(1 if 0 < x - q else 0)
            # One coefficient b=1, residual terminal at x-q and x+p.
            def g(y: Fraction) -> Fraction:
                return Fraction(1 if 0 >= y + p else 0) - lam * Fraction(1 if 0 < y - q else 0)

            one_step = q * g(x + p) + p * g(x - q)
            rows.append(
                {
                    "p": fstr(p),
                    "x": fstr(x),
                    "terminal_shift_value": fstr(terminal),
                    "one_unit_step_value": fstr(one_step),
                }
            )
    return rows


def write_json(name: str, obj: object) -> None:
    path = DATA / name
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)


def main() -> None:
    unit_grid = unitgap_grid_search(denoms=[8], nmax=8)
    # A second exact slice with denominator 12, but one fewer arity, catches
    # the common boundary chambers without making the run dominated by n=9.
    unit_grid += unitgap_grid_search(denoms=[12], nmax=7)
    unit_rand = unitgap_random_search(trials=6000)
    influence = influence_grid_search(denoms=[18, 24])
    blocks = block_and_pair_search(denoms=[12, 15], max_n=10)
    equal_traps = equal_weight_pair_trap_table(12)
    bellman = bellman_boundary_diagnostic()

    payload = {
        "unitgap_grid": unit_grid,
        "unitgap_random": unit_rand,
        "endpoint_influence": influence,
        "block_and_pair": blocks,
        "equal_weight_pair_traps": equal_traps,
        "bellman_boundary_diagnostic": bellman,
    }
    write_json("round9_results.json", payload)

    lines: list[str] = []
    lines.append("# Round 9 computation summary\n")
    lines.append("## Unit-gap exact grid minima\n")
    for rec in unit_grid:
        lines.append(
            f"- p={rec['p']}, d={rec['denom']}, n={rec['n']}: "
            f"min margin {rec['min_margin']} ({rec['min_margin_float']:.9g}), "
            f"B={rec['B']}, weights={rec['weights']}"
        )
    lines.append("\n## Unit-gap random rational minima\n")
    for rec in unit_rand:
        lines.append(
            f"- p={rec['p']}, tested={rec['tested']}: min margin {rec['min_margin']} "
            f"({rec['min_margin_float']:.9g}), d={rec['denom']}, n={rec['n']}, "
            f"B={rec['B']}, weights={rec['weights']}"
        )
    lines.append("\n## Endpoint influence minima\n")
    for rec in influence:
        cap = rec.get("min_influence_capped")
        lines.append(
            f"- p={rec['p']}, d={rec['denom']}: all min I={rec['min_influence_all']} "
            f"at parts={rec['min_all_parts']}; capped min I={cap} "
            f"at parts={rec.get('min_capped_parts')}"
        )
    lines.append("\n## Block/pair coalescence search\n")
    for rec in blocks:
        lines.append(
            f"- p={rec['p']}, d={rec['denom']}: capped={rec['capped_checked']}, "
            f"smallest max proper block gain={rec.get('smallest_max_proper_block_gain')}, "
            f"proper block counterexample={rec['proper_block_counterexample']}, "
            f"all-pair-negative={rec['all_pair_negative_count']}, "
            f"min q-Phi among those={rec.get('min_q_minus_phi_among_all_pair_negative')}"
        )
    lines.append("\n## Equal-weight all-pair-negative traps\n")
    for rec in equal_traps:
        lines.append(
            f"- n={rec['n']}, p={rec['p']}: Phi={rec['phi']}, q-Phi={rec['q_minus_phi']}, "
            f"each pair gain={rec['pair_gain_each']}"
        )
    lines.append("\n## Bellman shifted-boundary diagnostic\n")
    for rec in bellman:
        lines.append(
            f"- p={rec['p']}, x={rec['x']}: terminal={rec['terminal_shift_value']}, "
            f"one-step b=1 value={rec['one_unit_step_value']}"
        )
    (DATA / "round9_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
