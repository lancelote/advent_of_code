"""2015 - Day 18 Part 1: Like a GIF For Your Yard."""

from src.year2015.day18a import Grid
from src.year2015.day18a import count_on
from src.year2015.day18a import count_on_neighbors
from src.year2015.day18a import process_data
from src.year2015.day18a import step


def is_corner(r: int, c: int, grid: Grid) -> bool:
    rows = len(grid)
    cols = len(grid[0])

    return (
        (r == 0 and c == 0)
        or (r == rows - 1 and c == 0)
        or (r == 0 and c == cols - 1)
        or (r == rows - 1 and c == cols - 1)
    )


def toggle(r: int, c: int, grid: Grid) -> str:
    x = grid[r][c]

    if is_corner(r, c, grid):
        return "#"

    on_neighbors = count_on_neighbors(r, c, grid)

    if x == "#":
        return "#" if on_neighbors in {2, 3} else "."
    else:
        return "#" if on_neighbors == 3 else "."


def solve(task: str) -> int:
    grid = process_data(task)

    for _ in range(100):
        grid = step(grid, toggle)

    return count_on(grid)
