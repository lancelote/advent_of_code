"""2023 - Day 13 Part 2: Point of Incidence"""


def diff(a: list[str], b: list[str]) -> int:
    result = 0

    for r1, r2 in zip(a, b):
        for x1, x2 in zip(r1, r2):
            if x1 != x2:
                result += 1

    return result


def find_reflection(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        above = pattern[:i][::-1]
        below = pattern[i:]

        if diff(above, below) == 1:
            return i

    return 0


def get_cols(pattern: list[str]) -> list[str]:
    n_rows = len(pattern)
    n_cols = len(pattern[0])

    return ["".join(pattern[r][c] for r in range(n_rows)) for c in range(n_cols)]


def process_data(task: str) -> list[list[str]]:
    return [block.splitlines() for block in task.split("\n\n")]


def solve(task: str) -> int:
    result = 0
    patterns = process_data(task)

    for pattern in patterns:
        result += find_reflection(pattern) * 100
        result += find_reflection(get_cols(pattern))

    return result
