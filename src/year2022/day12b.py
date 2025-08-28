"""2022 - Day 12 Part 2: Hill Climbing Algorithm."""

import sys
from collections.abc import Iterator

from src.year2022.day12a import Square, bfs, construct_heightmap, find


def find_all(target: str, task: str) -> Iterator[Square]:
    for r, line in enumerate(task.splitlines()):
        for c, x in enumerate(line):
            if x == target:
                yield r, c


def solve(task: str) -> int:
    heightmap = construct_heightmap(task)
    end = find("E", task)
    shortest = sys.maxsize

    for start in find_all("a", task):
        try:
            path = bfs(start, end, heightmap)
            shortest = min(shortest, path)
        except ValueError:
            pass
    return shortest
