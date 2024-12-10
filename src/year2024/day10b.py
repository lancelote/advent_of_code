"""2024 - Day 10 Part 2: Hoof It"""

from src.year2024.day10a import SHIFTS
from src.year2024.day10a import find_trailheads


def get_rating(trailhead: tuple[int, int], data: list[list[int]]) -> int:
    rows = len(data)
    cols = len(data[0])

    def dfs(point: tuple[int, int]) -> int:
        count = 0
        r, c = point

        if data[r][c] == 9:
            return 1

        for dr, dc in SHIFTS:
            nr = r + dr
            nc = c + dc

            in_bounds = 0 <= nr < rows and 0 <= nc < cols
            if in_bounds and data[nr][nc] == data[r][c] + 1:
                count += dfs((nr, nc))

        return count

    return dfs(trailhead)


def solve(task: str) -> int:
    data = [[int(x) for x in line] for line in task.split("\n")]
    trailheads = find_trailheads(data)
    return sum(get_rating(trailhead, data) for trailhead in trailheads)
