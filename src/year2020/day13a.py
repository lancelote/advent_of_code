"""2020 - Day 13 Part 1: Shuttle Search."""
import re
from typing import List
from typing import Tuple


def process_data(data: str) -> Tuple[int, List[int]]:
    timestamp, shuttles = data.strip().split("\n")
    return int(timestamp), [int(x) for x in re.findall(r"\d+", shuttles)]


def find_closest(timestamp: int, shuttles: List[int]) -> Tuple[int, int]:
    closest_id = min(shuttles, key=lambda x: x - timestamp % x)
    to_wait = closest_id - timestamp % closest_id
    return to_wait, closest_id


def solve(task: str) -> int:
    """Find the closest shuttle."""
    timestamp, shuttles = process_data(task)
    to_wait, closest_id = find_closest(timestamp, shuttles)
    return to_wait * closest_id
