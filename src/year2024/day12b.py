"""2024 - Day 12 Part 2: Garden Groups"""

from src.year2024.day12a import parse_regions


def solve(task: str) -> int:
    data = task.split("\n")
    regions = parse_regions(data)
    return sum(x.price_with_discount for x in regions)
