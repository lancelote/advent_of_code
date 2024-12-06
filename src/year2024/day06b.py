"""2024 - Day 6 Part 2: Guard Gallivant"""

from src.year2024.day06a import SHIFTS
from src.year2024.day06a import TURN
from src.year2024.day06a import find_guard


def is_paradox(gr: int, gc: int, data: list[list[str]]) -> bool:
    rows = len(data)
    cols = len(data[0])

    visited: set[tuple[str, int, int]] = set()

    while True:
        guard = data[gr][gc]

        if (guard, gr, gc) in visited:
            return True

        visited.add((guard, gr, gc))

        dr, dc = SHIFTS[guard]

        nr = gr + dr
        nc = gc + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            data[gr][gc] = "."
            return False  # out of border

        if data[nr][nc] not in {"#", "O"}:
            data[gr][gc] = "."
            data[nr][nc] = guard

            gr = nr
            gc = nc
        else:
            new_guard = TURN[guard]
            data[gr][gc] = new_guard


def solve(task: str) -> int:
    data = [list(line) for line in task.split("\n")]

    gr, gc = find_guard(data)

    rows = len(data)
    cols = len(data[0])

    count = 0

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "#" or (r, c) == (gr, gc):
                continue

            data[r][c] = "O"
            data[gr][gc] = "^"

            if is_paradox(gr, gc, data):
                count += 1

            data[r][c] = "."

    return count
