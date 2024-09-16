"""2022 - Day 16 Part 1: Proboscidea Volcanium."""

import re
from typing import AbstractSet


def parse_tunnels(task: str) -> dict[str, list[str]]:
    tunnels: dict[str, list[str]] = {}

    for line in task.splitlines():
        valve, *neighbors = re.findall(r"[A-Z]{2}", line)
        tunnels[valve] = neighbors

    return tunnels


def parse_flow_rates(task: str) -> dict[str, int]:
    flow_rates: dict[str, int] = {}

    for line in task.splitlines():
        _, valve, *_ = line.split(" ")
        [rate_str] = re.findall(r"\d+", line)
        flow_rates[valve] = int(rate_str)

    return flow_rates


def left_score(
    flow_rates: dict[str, int],
    released_valves: AbstractSet[str],
    minute: int = 0,
) -> int:
    total_score = 0

    for valve, score in flow_rates.items():
        if valve not in released_valves:
            total_score += score * minute

    return total_score


def solve(task: str) -> int:
    flow_rates = parse_flow_rates(task)
    tunnels = parse_tunnels(task)
    to_visit = {("AA", 0, frozenset(("AA",)), frozenset(("AA",)))}
    max_score = 0

    for minute in range(29, -1, -1):
        new_to_visit = set()

        for valve, score, released, visited in to_visit:
            if left_score(flow_rates, released, minute) + score < max_score:
                continue

            max_score = max(max_score, score)

            for neighbor in tunnels[valve]:
                if neighbor not in visited:
                    new_to_visit.add(
                        (neighbor, score, released, visited | {neighbor})
                    )

            if flow_rates[valve] and valve not in released:
                visited = frozenset((valve,))
                released |= {valve}
                score += minute * flow_rates[valve]

                new_to_visit.add((valve, score, released, visited))

        to_visit = new_to_visit

    return max_score
