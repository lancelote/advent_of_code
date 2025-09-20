"""2015 - Day 18 Part 1: Like a GIF For Your Yard."""

type Grid = list[list[str]]

SHIFTS = (
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
)


def process_data(data: str) -> Grid:
    return [list(line) for line in data.splitlines()]


def count_on_neighbors(r: int, c: int, grid: Grid) -> int:
    rows = len(grid)
    cols = len(grid[0])

    count = 0

    for dr, dc in SHIFTS:
        nr = r + dr
        nc = c + dc

        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
            continue

        if grid[nr][nc] == "#":
            count += 1

    return count


def toggle(r: int, c: int, grid: Grid) -> str:
    x = grid[r][c]
    on_neighbors = count_on_neighbors(r, c, grid)

    if x == "#":
        return "#" if on_neighbors in {2, 3} else "."
    else:
        return "#" if on_neighbors == 3 else "."


def step(grid: Grid) -> Grid:
    rows = len(grid)
    cols = len(grid[0])

    new_grid: Grid = []

    for r in range(rows):
        new_row: list[str] = []

        for c in range(cols):
            new_row.append(toggle(r, c, grid))

        new_grid.append(new_row)

    return new_grid


def count_on(grid: Grid) -> int:
    count = 0

    for row in grid:
        for x in row:
            if x == "#":
                count += 1

    return count


def solve(task: str) -> int:
    grid = process_data(task)

    for _ in range(100):
        grid = step(grid)

    return count_on(grid)
