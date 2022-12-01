"""2022 - Day 1 Part 1: Calorie Counting."""


def process_data(task: str) -> list[int]:
    return [
        sum(int(food) for food in elf.split("\n"))
        for elf in task.split("\n\n")
    ]


def solve(task: str) -> int:
    return max(process_data(task))
