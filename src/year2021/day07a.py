"""2021 - Day 7 Part 1: The Treachery of Whales."""


def solve(task: str) -> int:
    positions = [int(x) for x in task.strip().split(",")]

    result: int | None = None

    for i in range(min(positions), max(positions)):
        fuel_cost = sum(abs(i - x) for x in positions)
        if result is None or result > fuel_cost:
            result = fuel_cost
        elif result < fuel_cost:
            break

    assert result is not None
    return result
