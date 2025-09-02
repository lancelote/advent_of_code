"""2022 - Day 16 Part 2: Proboscidea Volcanium."""

import itertools
from collections import deque

from src.year2022.day16a import left_score
from src.year2022.day16a import parse_flow_rates
from src.year2022.day16a import parse_tunnels


def get_path_length(a: str, b: str, tunnels: dict[str, list[str]]) -> int:
    todo: deque[tuple[str, int]] = deque()
    seen = set()

    todo.append((a, 0))
    seen.add(a)

    while todo:
        valve, path = todo.popleft()
        if valve == b:
            return path
        else:
            for x in tunnels[valve]:
                if x in seen:
                    continue
                seen.add(x)
                todo.append((x, path + 1))

    raise ValueError("path not found")


def compute_paths(
    worth_caves: list[str], tunnels: dict[str, list[str]]
) -> dict[tuple[str, str], int]:
    lengths: dict[tuple[str, str], int] = {}

    for a, b in itertools.combinations(worth_caves, 2):
        path_length = get_path_length(a, b, tunnels)
        lengths[(a, b)] = path_length
        lengths[(b, a)] = path_length
        lengths[(a, a)] = 0
        lengths[(b, b)] = 0

    return lengths


def solve(task: str) -> int:
    flow_rates = parse_flow_rates(task)
    tunnels = parse_tunnels(task)

    worth_caves = [
        cave
        for cave, pressure in sorted(flow_rates.items(), key=lambda x: -x[1])
        if pressure
    ]
    worth_caves.append("AA")  # starting position with 0-pressured valve
    path_lengths = compute_paths(worth_caves, tunnels)

    max_score = 0
    released = {"AA"}

    def dfs(score: int, minute1: int, minute2: int, valve1: str, valve2: str) -> None:
        nonlocal max_score

        if minute1 <= 0 and minute2 <= 0:
            return

        max_score = max(score, max_score)

        if score + left_score(flow_rates, released, max(minute1, minute2)) < max_score:
            return

        for a, b in itertools.permutations(worth_caves, 2):
            if a not in released and b not in released:
                new_minute1 = minute1 - path_lengths[(valve1, a)] - 1
                new_minute2 = minute2 - path_lengths[(valve2, b)] - 1

                if new_minute1 > 0:
                    released.add(a)
                if new_minute2 > 0:
                    released.add(b)

                new_score = score

                if new_minute1 > 0:
                    new_score += new_minute1 * flow_rates[a]
                if new_minute2 > 0:
                    new_score += new_minute2 * flow_rates[b]

                dfs(new_score, new_minute1, new_minute2, a, b)

                if new_minute1 > 0:
                    released.remove(a)
                if new_minute2 > 0:
                    released.remove(b)

    dfs(0, 26, 26, "AA", "AA")
    return max_score
