"""2025 - Day 4 Part 1: Printing Department"""

SHIFTS = (
    # dr dc
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
)


def process_data(task: str) -> list[list[str]]:
    return [list(line) for line in task.splitlines()]


def count_accessible(diagram: list[list[str]]) -> int:
    count = 0

    n_rows = len(diagram)
    n_cols = len(diagram[0])

    for r in range(n_rows):
        for c in range(n_cols):
            if diagram[r][c] == ".":
                continue

            neighbors = 0

            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n_rows and 0 <= nc < n_cols:
                    if diagram[nr][nc] == "@":
                        neighbors += 1

            if neighbors < 4:
                count += 1

    return count


def solve(task: str) -> int:
    diagram = process_data(task)
    return count_accessible(diagram)
