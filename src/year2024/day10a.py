"""2024 - Day 10 Part 1: Hoof It"""

SHIFTS = (
    # r c
    (-1, 0),  # up
    (0, +1),  # right
    (+1, 0),  # down
    (0, -1),  # left
)


def get_score(trailhead: tuple[int, int], data: list[list[int]]) -> int:
    rows = len(data)
    cols = len(data[0])

    summits: set[tuple[int, int]] = set()

    def dfs(point: tuple[int, int]) -> None:
        r, c = point

        if data[r][c] == 9:
            summits.add(point)

        for dr, dc in SHIFTS:
            nr = r + dr
            nc = c + dc

            in_bounds = 0 <= nr < rows and 0 <= nc < cols
            if in_bounds and data[nr][nc] == data[r][c] + 1:
                dfs((nr, nc))

    dfs(trailhead)
    return len(summits)


def find_trailheads(data: list[list[int]]) -> list[tuple[int, int]]:
    rows = len(data)
    cols = len(data[0])

    trailheads: list[tuple[int, int]] = []

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == 0:
                trailheads.append((r, c))

    return trailheads


def solve(task: str) -> int:
    data = [[int(x) for x in line] for line in task.split("\n")]
    trailheads = find_trailheads(data)
    return sum(get_score(trailhead, data) for trailhead in trailheads)
