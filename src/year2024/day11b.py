"""2024 - Day 11 Part 2: Plutonian Pebbles"""

from functools import cache


@cache
def evolve(stone: int, generation: int) -> int:
    if generation == 0:
        return 1

    if stone == 0:
        return evolve(1, generation - 1)
    elif len(str(stone)) % 2 == 0:
        middle = len(str(stone)) // 2

        left = int(str(stone)[:middle])
        right = int(str(stone)[middle:])

        return evolve(left, generation - 1) + evolve(right, generation - 1)
    else:
        return evolve(stone * 2024, generation - 1)


def solve(task: str) -> int:
    stones = [int(x) for x in task.split()]
    return sum(evolve(stone, 75) for stone in stones)
