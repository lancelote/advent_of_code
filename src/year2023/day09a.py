"""2023 - Day 9 Part 1: Mirage Maintenance"""


def process_data(data: str) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in data.splitlines()]


def all_zeros(generation: list[int]) -> bool:
    for x in generation:
        if x != 0:
            return False
    return True


def get_next_value(hist: list[int]) -> int:
    trail: list[int] = []

    while not all_zeros(hist):
        trail.append(hist[-1])
        hist = [hist[i + 1] - hist[i] for i in range(len(hist) - 1)]

    return sum(trail)


def solve(task: str) -> int:
    return sum(get_next_value(x) for x in process_data(task))
