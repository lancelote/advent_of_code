"""2023 - Day 15 Part 1: Lens Library"""


def get_hash(sequence: str) -> int:
    value = 0

    for x in sequence:
        value += ord(x)
        value *= 17
        value %= 256

    return value


def solve(task: str) -> int:
    return sum(get_hash(x) for x in task.split(","))
