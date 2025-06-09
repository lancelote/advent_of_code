"""2015 - Day 9 Part 1: All in a Single Night."""

import sys
from collections import defaultdict

type Data = dict[str, list[tuple[str, int]]]


def process_data(task: str) -> Data:
    result: Data = defaultdict(list)

    for line in task.split("\n"):
        a, _, b, _, c = line.split()

        result[a].append((b, int(c)))
        result[b].append((a, int(c)))

    return result


def find_shortest(data: Data) -> int:
    unique_cities = len(set(data.keys()))
    shortest = sys.maxsize
    path: set[str] = set()

    def dfs(city: str, so_far: int = 0) -> None:
        nonlocal shortest

        if so_far >= shortest:
            return

        if city in path:
            return

        if city not in data:
            return

        if len(path) == unique_cities - 1:
            shortest = so_far
            return

        path.add(city)
        for next_city, distance in data[city]:
            dfs(next_city, so_far + distance)
        path.remove(city)

    for k in data.keys():
        dfs(k)

    return shortest


def solve(task: str) -> int:
    data = process_data(task)
    return find_shortest(data)
