"""2022 - Day 16 Part 2: Proboscidea Volcanium."""
import re
from collections import deque


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
    flow_rate: dict[str, int], released_valves: frozenset[str], minute: int = 0
) -> int:
    total_score = 0

    for valve, score in flow_rate.items():
        if valve not in released_valves:
            total_score += score * minute

    return total_score


def solve(task: str) -> int:
    flow_rate = parse_flow_rates(task)
    tunnels = parse_tunnels(task)
    to_visit: deque[
        tuple[
            int, str, str, int, frozenset[str], frozenset[str], frozenset[str]
        ]
    ] = deque()
    to_visit.append(
        (
            25,
            "AA",
            "AA",
            0,
            frozenset(("AA",)),
            frozenset(("AA",)),
            frozenset(("AA",)),
        )
    )
    max_score = 0

    while to_visit:
        (
            minute,
            valve1,
            valve2,
            score,
            released,
            visited1,
            visited2,
        ) = to_visit.popleft()

        if minute < 0:
            continue

        # optimization if no chance to beat the best score
        if left_score(flow_rate, released, minute) + score < max_score:
            continue

        max_score = max(max_score, score)

        # both move
        for neighbor1 in tunnels[valve1]:
            for neighbor2 in tunnels[valve2]:
                if neighbor1 not in visited1 and neighbor2 not in visited2:
                    to_visit.append(
                        (
                            minute - 1,
                            neighbor1,
                            neighbor2,
                            score,
                            released,
                            visited1 | {neighbor1},
                            visited2 | {neighbor2},
                        ),
                    )

        # valve 1 open
        if flow_rate[valve1] and valve1 not in released:
            visited1 = frozenset((valve1,))
            released |= {valve1}
            score += minute * flow_rate[valve1]

            # valve 2 move
            for neighbor2 in tunnels[valve2]:
                if neighbor2 not in visited2:
                    to_visit.append(
                        (
                            minute - 1,
                            valve1,
                            neighbor2,
                            score,
                            released,
                            visited1,
                            visited2 | {neighbor2},
                        )
                    )

            # valve 2 open
            if flow_rate[valve2] and valve2 not in released:
                visited2 = frozenset((valve2,))
                released |= {valve2}
                score += minute * flow_rate[valve2]
                to_visit.append(
                    (
                        minute - 1,
                        valve1,
                        valve2,
                        score,
                        released,
                        visited1,
                        visited2,
                    )
                )

        # valve 2 open
        elif flow_rate[valve2] and valve2 not in released:
            visited2 = frozenset((valve2,))
            released |= {valve2}
            score += minute * flow_rate[valve2]

            # valve 1 move
            for neighbor1 in tunnels[valve1]:
                if neighbor1 not in visited1:
                    to_visit.append(
                        (
                            minute - 1,
                            neighbor1,
                            valve2,
                            score,
                            released,
                            visited1 | {neighbor1},
                            visited2,
                        )
                    )

    return max_score
