"""2021 - Day 7 Part 2: The Treachery of Whales."""


def fuel(distance: int) -> int:
    return (distance + 1) * distance // 2  # arithmetic progression sum


def solve(task: str) -> int:
    positions = [int(x) for x in task.strip().split(",")]

    min_fuel_cost: int | None = None

    for align_pos in range(min(positions), max(positions)):
        fuel_cost = sum(fuel(abs(align_pos - x)) for x in positions)
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
        elif min_fuel_cost < fuel_cost:
            break

    assert min_fuel_cost is not None
    return min_fuel_cost
