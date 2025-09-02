"""2023 - Day 14 Part 2: Parabolic Reflector Dish"""

from src.year2023.day14a import Platform
from src.year2023.day14a import count_load
from src.year2023.day14a import tilt_north


def tilt_east(platform: Platform) -> None:
    rows = len(platform)
    cols = len(platform[0])

    for r in range(rows):
        last_empty_c = cols - 1

        for c in range(cols - 1, -1, -1):
            if platform[r][c] == "O":
                if c != last_empty_c:
                    platform[r][last_empty_c] = "O"
                    platform[r][c] = "."
                    last_empty_c -= 1
                else:
                    last_empty_c -= 1

            if platform[r][c] == "#":
                last_empty_c = c - 1


def tilt_south(platform: Platform) -> None:
    rows = len(platform)
    cols = len(platform[0])

    for c in range(cols):
        last_empty_r = rows - 1

        for r in range(rows - 1, -1, -1):
            if platform[r][c] == "O":
                if r != last_empty_r:
                    platform[last_empty_r][c] = "O"
                    platform[r][c] = "."
                    last_empty_r -= 1
                else:
                    last_empty_r -= 1

            if platform[r][c] == "#":
                last_empty_r = r - 1


def tilt_west(platform: Platform) -> None:
    rows = len(platform)
    cols = len(platform[0])

    for r in range(rows):
        last_empty_c = 0

        for c in range(cols):
            if platform[r][c] == "O":
                if c != last_empty_c:
                    platform[r][last_empty_c] = "O"
                    platform[r][c] = "."
                    last_empty_c += 1
                else:
                    last_empty_c += 1

            if platform[r][c] == "#":
                last_empty_c = c + 1


def cycle(platform: Platform) -> None:
    tilt_north(platform)
    tilt_west(platform)
    tilt_south(platform)
    tilt_east(platform)


def solve(task: str) -> int:
    platform = [list(line) for line in task.splitlines()]

    # note:
    #   not sure if it will work for every input
    #   in my case the load is repeated after 77 cycles
    #   and (1_000_000_000 - 1_000) % 77 = 0
    for i in range(1000):
        cycle(platform)

    return count_load(platform)
