#!/usr/bin/env python3
"""Round 13 exposure-identity experiments.

The identity

    P(S_m < p) = 1 - p * sum_i P(p-w_i <= S_{i-1} < p)

is exact for every deterministic ordering of the weights.  This script records
the contribution profile for several extremal-looking examples and tests a few
stronger local statements that would imply a simple discharging proof.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction
from itertools import permutations
import json
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "round13"
OUT.mkdir(parents=True, exist_ok=True)


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def dist_after_prefix(weights: list[Fraction], p: Fraction) -> dict[Fraction, Fraction]:
    q = 1 - p
    dist: dict[Fraction, Fraction] = {Fraction(0): Fraction(1)}
    for w in weights:
        nxt: dict[Fraction, Fraction] = defaultdict(Fraction)
        for s, pr in dist.items():
            nxt[s] += pr * q
            nxt[s + w] += pr * p
        dist = dict(nxt)
    return dist


def exposure_profile(weights: list[Fraction], p: Fraction) -> dict[str, object]:
    dist: dict[Fraction, Fraction] = {Fraction(0): Fraction(1)}
    q = 1 - p
    contributions: list[Fraction] = []
    for w in weights:
        h = sum(pr for s, pr in dist.items() if p - w <= s < p)
        contributions.append(h)
        nxt: dict[Fraction, Fraction] = defaultdict(Fraction)
        for s, pr in dist.items():
            nxt[s] += pr * q
            nxt[s + w] += pr * p
        dist = dict(nxt)
    lower = sum(pr for s, pr in dist.items() if s < p)
    H = sum(contributions)
    return {
        "p": fstr(p),
        "weights": [fstr(w) for w in weights],
        "weights_float": [float(w) for w in weights],
        "lower_tail": fstr(lower),
        "success_tail": fstr(1 - lower),
        "crossing_intensity_sum": fstr(H),
        "identity_residual": fstr(lower - (1 - p * H)),
        "contributions": [fstr(x) for x in contributions],
        "contributions_float": [float(x) for x in contributions],
        "partial_sums_contrib": [fstr(sum(contributions[: i + 1], Fraction(0))) for i in range(len(contributions))],
    }


def actual_opportunity_distribution(weights: list[Fraction], p: Fraction) -> dict[int, Fraction]:
    """Distribution of the number of predictable crossing opportunities.

    Opportunities after crossing are not counted, matching the predictable
    local-time process in the exposure identity.  At each opportunity a success
    crosses and terminates the opportunity count.
    """

    q = 1 - p
    states: dict[tuple[Fraction, int, bool], Fraction] = {(Fraction(0), 0, False): Fraction(1)}
    for w in weights:
        nxt: dict[tuple[Fraction, int, bool], Fraction] = defaultdict(Fraction)
        for (s, count, crossed), pr in states.items():
            if crossed:
                nxt[(s, count, True)] += pr
                continue
            is_opp = p - w <= s < p
            # failure
            nxt[(s, count + int(is_opp), False)] += pr * q
            # success
            s2 = s + w
            crossed2 = s2 >= p
            nxt[(s2, count + int(is_opp), crossed2)] += pr * p
        states = dict(nxt)
    out: dict[int, Fraction] = defaultdict(Fraction)
    for (_s, count, _crossed), pr in states.items():
        out[count] += pr
    return dict(sorted(out.items()))


def opportunity_summary(weights: list[Fraction], p: Fraction) -> dict[str, object]:
    d = actual_opportunity_distribution(weights, p)
    mean = sum(Fraction(k) * pr for k, pr in d.items())
    return {
        "p": fstr(p),
        "weights": [fstr(w) for w in weights],
        "opportunity_count_distribution": {str(k): fstr(v) for k, v in d.items()},
        "opportunity_count_distribution_float": {str(k): float(v) for k, v in d.items()},
        "mean_opportunities": fstr(mean),
        "mean_opportunities_float": float(mean),
    }


@dataclass
class FailedLocalLemma:
    name: str
    p: str
    weights: list[str]
    order: list[int]
    details: dict[str, object]


def first_failure_local_lemmas() -> list[FailedLocalLemma]:
    """Find compact counterexamples to stronger exposure assertions."""

    failures: list[FailedLocalLemma] = []

    # Lemma A: in decreasing order, each item pays for its own weight:
    #   P(p-w_i <= S_{i-1} < p) >= w_i.
    p = Fraction(1, 3)
    weights = [Fraction(3, 10), Fraction(3, 10), Fraction(2, 5)]
    prof = exposure_profile(weights, p)
    contribs = [Fraction(x) for x in prof["contributions"]]
    for i, (h, w) in enumerate(zip(contribs, weights)):
        if h < w:
            failures.append(
                FailedLocalLemma(
                    name="termwise_contribution_ge_weight_in_decreasing_order",
                    p=fstr(p),
                    weights=[fstr(w) for w in weights],
                    order=list(range(len(weights))),
                    details={"index": i, "contribution": fstr(h), "weight": fstr(w)},
                )
            )
            break

    # Lemma B: once the deterministic prefix weight reaches p, the cumulative
    # exposure contributions already reach the deterministic prefix weight.
    p = Fraction(3, 10)
    weights = [Fraction(1, 4)] * 4
    prof = exposure_profile(weights, p)
    contribs = [Fraction(x) for x in prof["contributions"]]
    c = Fraction(0)
    W = Fraction(0)
    for i, (h, w) in enumerate(zip(contribs, weights)):
        c += h
        W += w
        if W >= p and c < W:
            failures.append(
                FailedLocalLemma(
                    name="prefix_contributions_dominate_prefix_weight_after_prefix_reaches_p",
                    p=fstr(p),
                    weights=[fstr(w) for w in weights],
                    order=list(range(len(weights))),
                    details={"prefix_index": i, "prefix_contribution": fstr(c), "prefix_weight": fstr(W)},
                )
            )
            break

    # Lemma C: every order of a capped vector has at least one deterministic
    # opportunity on every nonempty selected set.  This fails already on the
    # all-failure path, but here is a less vacuous one-success path.
    p = Fraction(3, 10)
    weights = [Fraction(1, 4)] * 4
    selected = {0}
    s = Fraction(0)
    opps = 0
    for i, w in enumerate(weights):
        if p - w <= s < p:
            opps += 1
        if i in selected:
            s += w
    if opps == 0:
        failures.append(
            FailedLocalLemma(
                name="each_nonempty_selected_path_has_an_opportunity",
                p=fstr(p),
                weights=[fstr(w) for w in weights],
                order=list(range(len(weights))),
                details={"selected_indices": sorted(selected), "final_selected_weight": fstr(s), "opportunities": opps},
            )
        )

    return failures


def random_order_spread(weights: list[Fraction], p: Fraction, samples: int, seed: int) -> dict[str, object]:
    rng = random.Random(seed)
    seen: set[tuple[int, ...]] = set()
    records = []
    n = len(weights)
    if n <= 8:
        orders = list(permutations(range(n)))
    else:
        orders = []
        while len(orders) < samples:
            order = list(range(n))
            rng.shuffle(order)
            t = tuple(order)
            if t not in seen:
                seen.add(t)
                orders.append(t)
    for order in orders[:samples]:
        ordered = [weights[i] for i in order]
        prof = exposure_profile(ordered, p)
        records.append(
            {
                "order": list(order),
                "max_contribution": max(float(x) for x in prof["contributions_float"]),
                "nonzero_terms": sum(1 for x in prof["contributions_float"] if x > 0),
                "contributions_float": prof["contributions_float"],
            }
        )
    records.sort(key=lambda r: (r["nonzero_terms"], r["max_contribution"]))
    return {
        "p": fstr(p),
        "weights": [fstr(w) for w in weights],
        "orders_checked": len(records),
        "smallest_nonzero_term_records": records[:5],
        "largest_nonzero_term_records": records[-5:],
    }


def main() -> None:
    examples: dict[str, list[Fraction]] = {
        "equal_quarters_p_3_10": [Fraction(1, 4)] * 4,
        "round12_grid_p_2_7": [Fraction(1, 7)] + [Fraction(3, 14)] * 4,
        "round12_grid_p_4_13": [Fraction(5, 26)] + [Fraction(7, 26)] * 3,
        "pivot_dust_p_3_10_eps_1_100_N_60": [Fraction(29, 100)] + [Fraction(71, 6000)] * 60,
    }
    p_for = {
        "equal_quarters_p_3_10": Fraction(3, 10),
        "round12_grid_p_2_7": Fraction(2, 7),
        "round12_grid_p_4_13": Fraction(4, 13),
        "pivot_dust_p_3_10_eps_1_100_N_60": Fraction(3, 10),
    }

    profiles = {}
    opportunities = {}
    order_spreads = {}
    for name, weights in examples.items():
        p = p_for[name]
        profiles[name + "_given"] = exposure_profile(weights, p)
        profiles[name + "_increasing"] = exposure_profile(sorted(weights), p)
        profiles[name + "_decreasing"] = exposure_profile(sorted(weights, reverse=True), p)
        opportunities[name + "_decreasing"] = opportunity_summary(sorted(weights, reverse=True), p)
        order_spreads[name] = random_order_spread(weights, p, samples=200, seed=13013)

    failures = [asdict(x) for x in first_failure_local_lemmas()]
    out = {"profiles": profiles, "opportunities": opportunities, "order_spreads": order_spreads, "failed_local_lemmas": failures}
    (OUT / "round13_exposure.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    md = ["# Round 13 Exposure Identity Computations", ""]
    for name in sorted(profiles):
        prof = profiles[name]
        md.append(f"## {name}")
        md.append(f"- p = `{prof['p']}`")
        md.append(f"- lower tail P(S<p) = `{prof['lower_tail']}`; success = `{prof['success_tail']}`")
        md.append(f"- crossing intensity sum H = `{prof['crossing_intensity_sum']}`")
        md.append(f"- contributions = `{prof['contributions']}`")
        md.append("")
    md.append("## Failed Stronger Local Lemmas")
    for fail in failures:
        md.append(f"- `{fail['name']}` at p=`{fail['p']}`, weights=`{fail['weights']}`: `{fail['details']}`")
    md.append("")
    (OUT / "round13_exposure_summary.md").write_text("\n".join(md), encoding="utf-8")


if __name__ == "__main__":
    main()
