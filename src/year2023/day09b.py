"""2023 - Day 9 Part 2: Mirage Maintenance"""
from src.year2023.day09a import all_zeros
from src.year2023.day09a import process_data


def get_prev_value(hist: list[int]) -> int:
    trail: list[int] = []

    while not all_zeros(hist):
        trail.append(hist[0])
        hist = [hist[i + 1] - hist[i] for i in range(len(hist) - 1)]

    while len(trail) != 1:
        a = trail.pop()
        b = trail.pop()
        trail.append(b - a)

    return trail[0]


def solve(task: str) -> int:
    return sum(get_prev_value(x) for x in process_data(task))
