"""2023 - Day 10 Part 1: Pipe Maze"""

from collections import defaultdict
from typing import TypeAlias

C: TypeAlias = tuple[int, int]
Map: TypeAlias = dict[C, set[C]]
Land: TypeAlias = list[list[str]]

# | - L J 7 F . S
N_CONN = {"S", "|", "L", "J"}
E_CONN = {"S", "-", "L", "F"}
S_CONN = {"S", "|", "7", "F"}
W_CONN = {"S", "-", "7", "J"}


def construct_map(land: Land) -> Map:
    rows = len(land)
    cols = len(land[0])

    m: dict[C, set[C]] = defaultdict(set)

    for r in range(rows):
        for c in range(cols):
            # N
            if r > 0 and land[r][c] in N_CONN and land[r - 1][c] in S_CONN:
                m[(r, c)].add((r - 1, c))

            # E
            if c < cols - 1 and land[r][c] in E_CONN and land[r][c + 1] in W_CONN:
                m[(r, c)].add((r, c + 1))

            # S
            if r < rows - 1 and land[r][c] in S_CONN and land[r + 1][c] in N_CONN:
                m[(r, c)].add((r + 1, c))

            # W
            if c > 0 and land[r][c] in W_CONN and land[r][c - 1] in E_CONN:
                m[(r, c)].add((r, c - 1))

    return m


def process_data(data: str) -> Land:
    return [list(x) for x in data.splitlines()]


def get_path(prev: C, curr: C, m: Map, land: Land) -> int:
    path = 0

    while land[curr[0]][curr[1]] != "S":
        nxt_set = m[curr] - {prev}

        if len(nxt_set) == 0:
            return -1  # dead end

        prev = curr
        (curr,) = nxt_set
        path += 1

    return path


def find_start(land: Land) -> C:
    rows = len(land)
    cols = len(land[0])

    for r in range(rows):
        for c in range(cols):
            if land[r][c] == "S":
                return r, c

    raise ValueError("start position wasn't found")


def solve(task: str) -> int:
    land = process_data(task)
    m = construct_map(land)
    start = find_start(land)
    return max(get_path(start, x, m, land) for x in m[start]) // 2 + 1
