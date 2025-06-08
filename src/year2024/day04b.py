"""2024 - Day 4 Part 2: Ceres Search"""

OPTIONS = {
    "MMASS",
    "MSAMS",
    "SSAMM",
    "SMASM",
}

SHIFTS = (
    # dr dc
    (0, 0),
    (0, +2),
    (+1, +1),
    (+2, 0),
    (+2, +2),
)


def is_xmas(r: int, c: int, data: list[str]) -> bool:
    start = data[r][c]

    if start not in {"S", "M"}:
        return False

    word = "".join(data[r + dr][c + dc] for dr, dc in SHIFTS)
    return word in OPTIONS


def solve(task: str) -> int:
    data = task.split("\n")

    ans = 0

    rows = len(data)
    cols = len(data[0])

    for r in range(rows - 2):
        for c in range(cols - 2):
            ans += is_xmas(r, c, data)

    return ans
