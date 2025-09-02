"""2022 - Day 8 Part 2: Treetop Tree House."""

from src.year2022.day08a import process_data


def scenic_score(r: int, c: int, trees: list[list[int]]) -> int:
    rows = len(trees)
    cols = len(trees[0])
    tree = trees[r][c]
    left = top = right = bottom = 0

    # left
    for nc in range(c - 1, -1, -1):
        left += 1
        if trees[r][nc] >= tree:
            break

    # top
    for nr in range(r - 1, -1, -1):
        top += 1
        if trees[nr][c] >= tree:
            break

    # right
    for nc in range(c + 1, cols):
        right += 1
        if trees[r][nc] >= tree:
            break

    # bottom
    for nr in range(r + 1, rows):
        bottom += 1
        if trees[nr][c] >= tree:
            break

    return left * top * right * bottom


def solve(task: str) -> int:
    trees = process_data(task)

    rows = len(trees)
    cols = len(trees[0])

    return max(
        scenic_score(r, c, trees) for c in range(cols) for r in range(rows)
    )
