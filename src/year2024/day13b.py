"""2024 - Day 13 Part 2: Claw Contraption"""

from src.year2024.day13a import Machine

SHIFT = 10_000_000_000_000


def solve(task: str) -> int:
    machines = [Machine.from_text(x) for x in task.split("\n\n")]

    for machine in machines:
        x, y = machine.prize
        machine.prize = (x + SHIFT, y + SHIFT)

    return sum(x.min_tokens_win for x in machines)
