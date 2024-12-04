"""2024 - Day 4 Part 1: Ceres Search"""

SHIFTS = {
    # dr  dc
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
}

XMAS = "XMAS"


def is_xmas(r: int, c: int, data: list[str]) -> int:
    count = 0

    rows = len(data)
    cols = len(data[0])

    for dr, dc in SHIFTS:
        nr = r
        nc = c

        for i in range(4):
            in_bounds = 0 <= nr < rows and 0 <= nc < cols
            if not in_bounds or XMAS[i] != data[nr][nc]:
                break

            nr += dr
            nc += dc
        else:
            count += 1

    return count


def solve(task: str) -> int:
    data = task.split("\n")

    ans = 0

    rows = len(data)
    cols = len(data[0])

    for r in range(rows):
        for c in range(cols):
            ans += is_xmas(r, c, data)

    return ans
