"""2022 - Day 16 Part 1: Proboscidea Volcanium."""
import re


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


def solve(task: str) -> int:
    flow_rate = parse_flow_rates(task)
    tunnels = parse_tunnels(task)
    to_visit = {("AA", 0, frozenset(("AA",)))}

    for minute in range(29, -1, -1):
        new_to_visit = set()

        for valve, score, released in to_visit:
            if flow_rate[valve] and valve not in released:
                new_to_visit.add(
                    (
                        valve,
                        score + minute * flow_rate[valve],
                        released | {valve},
                    )
                )
            for neighbor in tunnels[valve]:
                new_to_visit.add((neighbor, score, released))

        to_visit = new_to_visit

    return max(score for _, score, _ in to_visit)
