"""2020 - Day 13 Part 1: Shuttle Search."""
import re


def process_data(data: str) -> tuple[int, list[int]]:
    timestamp, shuttles = data.strip().split("\n")
    return int(timestamp), [int(x) for x in re.findall(r"\d+", shuttles)]


def find_closest(timestamp: int, shuttles: list[int]) -> tuple[int, int]:
    closest_id = min(shuttles, key=lambda x: x - timestamp % x)
    to_wait = closest_id - timestamp % closest_id
    return to_wait, closest_id


def solve(task: str) -> int:
    """Find the closest shuttle."""
    timestamp, shuttles = process_data(task)
    to_wait, closest_id = find_closest(timestamp, shuttles)
    return to_wait * closest_id
