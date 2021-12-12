"""2021 - Day 7 Part 2: The Treachery of Whales."""


def fuel(distance: int) -> int:
    return (distance + 1) * distance // 2  # arithmetic progression sum


def solve(task: str) -> int:
    positions = [int(x) for x in task.strip().split(",")]

    result: int | None = None

    for align_pos in range(min(positions), max(positions)):
        fuel_cost = sum(fuel(abs(align_pos - x)) for x in positions)
        if result is None or result > fuel_cost:
            result = fuel_cost
        elif result < fuel_cost:
            break

    assert result is not None
    return result
