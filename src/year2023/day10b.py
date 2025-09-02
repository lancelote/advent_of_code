"""2023 - Day 10 Part 2: Pipe Maze"""

from src.year2023.day10a import C
from src.year2023.day10a import Land
from src.year2023.day10a import Map
from src.year2023.day10a import construct_map
from src.year2023.day10a import find_start
from src.year2023.day10a import process_data


def get_path(m: Map, land: Land) -> list[C]:
    start = find_start(land)

    def construct_path_from(prev: C, curr: C) -> list[C]:
        path: list[C] = []

        while land[curr[0]][curr[1]] != "S":
            nxt_set = m[curr] - {prev}

            if not nxt_set:
                return []

            path.append(curr)
            prev = curr
            (curr,) = nxt_set

        path.append(start)
        return path

    for x in m[start]:
        if p := construct_path_from(start, x):
            return p

    raise ValueError("path not found")


def get_corners(path: list[C], land: Land) -> list[C]:
    corners: list[C] = []

    for i in range(len(path) - 1):
        r, c = path[i]

        if land[r][c] in {"L", "J", "7", "F"}:
            corners.append(path[i])

    def is_start_corner() -> bool:
        pr, pc = path[0]
        nr, nc = path[-2]

        p = land[pr][pc]
        n = land[nr][nc]

        return not (p == n and p in {"|", "-"})

    if is_start_corner():
        corners.append(path[-1])

    return corners


def get_gauss_area(corners: list[C]) -> int:
    n = len(corners)

    return (
        abs(
            sum(
                corners[i][0] * (corners[i - 1][1] - corners[(i + 1) % n][1])
                for i in range(n)
            )
        )
        // 2
    )


def solve(task: str) -> int:
    land = process_data(task)
    m = construct_map(land)
    path = get_path(m, land)
    corners = get_corners(path, land)

    # geometry goes brrr
    area = get_gauss_area(corners)
    boundary_points = len(path)
    inner_points = area - boundary_points // 2 + 1

    return inner_points
