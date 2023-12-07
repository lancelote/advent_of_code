"""2023 - Day 6 Part 2: Wait For It"""
from src.year2023.day06a import Race


def process_data(data: str) -> Race:
    lines = data.splitlines()
    _, time_parts = lines[0].split(": ")
    _, dist_parts = lines[1].split(": ")

    time = int("".join(time_parts.split()))
    dist = int("".join(dist_parts.split()))

    return Race(time, dist)


def solve(task: str) -> int:
    race = process_data(task)
    return race.ways_to_win
