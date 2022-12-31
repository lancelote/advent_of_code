"""2022 - Day 16 Part 2: Proboscidea Volcanium."""
import itertools
from collections import deque

from src.year2022.day16a import parse_flow_rates
from src.year2022.day16a import parse_tunnels


def solve(task: str) -> int:
    flow_rate = parse_flow_rates(task)
    tunnels = parse_tunnels(task)
    worth_caves = [cave for cave, pressure in flow_rate.items() if pressure]
    worth_caves.append("AA")  # starting position with 0-pressured valve

    def get_path_length(a: str, b: str) -> int:
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

    def compute_paths() -> dict[tuple[str, str], int]:
        lengths: dict[tuple[str, str], int] = {}

        for a, b in itertools.combinations(worth_caves, 2):
            path_length = get_path_length(a, b)
            lengths[(a, b)] = path_length
            lengths[(b, a)] = path_length
            lengths[(a, a)] = 0
            lengths[(b, b)] = 0

        return lengths

    path_lengths = compute_paths()

    to_visit: deque[tuple[str, int, str, int, int, frozenset[str]]] = deque()
    to_visit.append(("AA", 26, "AA", 26, 0, frozenset(("AA",))))
    max_score = 0

    while to_visit:
        valve1, minute1, valve2, minute2, score, released = to_visit.popleft()

        max_score = max(max_score, score)

        for a, b in itertools.permutations(worth_caves, 2):
            if a in released or b in released:
                continue

            new_minute1 = minute1 - path_lengths[(valve1, a)] - 1
            new_minute2 = minute2 - path_lengths[(valve2, b)] - 1

            new_score = score

            if new_minute1 > 0:
                new_score += new_minute1 * flow_rate[a]

            if new_minute2 > 0:
                new_score += new_minute2 * flow_rate[b]

            if new_minute1 > 0 and new_minute2 > 0:
                new_released = released | {a, b}
            elif new_minute1 > 0:
                new_released = released | {a}
            elif new_minute2 > 0:
                new_released = released | {b}
            else:
                continue

            to_visit.append(
                (a, new_minute1, b, new_minute2, new_score, new_released)
            )

    return max_score
