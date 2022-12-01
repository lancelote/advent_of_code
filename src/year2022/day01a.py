"""2022 - Day 1 Part 1: Calorie Counting."""


def process_data(task: str) -> list[list[int]]:
    return [
        [int(food) for food in elf.split("\n")] for elf in task.split("\n\n")
    ]


def solve(task: str) -> int:
    return max(sum(x) for x in process_data(task))
