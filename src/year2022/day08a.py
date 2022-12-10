"""2022 - Day 8 Part 1: Treetop Tree House."""


def process_data(data: str) -> list[list[int]]:
    return [[int(x) for x in line] for line in data.splitlines()]


def count_visible(trees: list[list[int]]) -> int:
    rows = len(trees)
    cols = len(trees[0])

    visible: set[tuple[int, int]] = set()

    # left -> right
    for r in range(rows):
        max_prev = -1
        for c in range(cols):
            if trees[r][c] > max_prev:
                visible.add((r, c))
                max_prev = trees[r][c]

    # right -> left
    for r in range(rows):
        max_prev = -1
        for c in range(cols - 1, -1, -1):
            if trees[r][c] > max_prev:
                visible.add((r, c))
                max_prev = trees[r][c]

    # top -> bottom
    for c in range(cols):
        max_prev = -1
        for r in range(rows):
            if trees[r][c] > max_prev:
                visible.add((r, c))
                max_prev = trees[r][c]

    # bottom -> top
    for c in range(cols):
        max_prev = -1
        for r in range(rows - 1, -1, -1):
            if trees[r][c] > max_prev:
                visible.add((r, c))
                max_prev = trees[r][c]

    return len(visible)


def solve(task: str) -> int:
    trees = process_data(task)
    return count_visible(trees)
