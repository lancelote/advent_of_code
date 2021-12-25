"""2021 - Day 7 Part 1: The Treachery of Whales."""


def solve(task: str) -> int:
    positions = [int(x) for x in task.strip().split(",")]

    def fuel_cost(align: int) -> int:
        return sum(abs(align - x) for x in positions)

    possible_aligns = range(min(positions), max(positions))
    return min(fuel_cost(align) for align in possible_aligns)
