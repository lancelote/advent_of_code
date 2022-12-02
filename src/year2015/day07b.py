"""2015 - Day 7 Part 2: Some Assembly Required."""
from src.year2015.day07a import process_data
from src.year2015.day07a import Solution


def solve(task: str) -> int:
    connections = process_data(task)
    solution = Solution(connections)
    a = solution.get_value("a")
    solution.cache.clear()
    solution.cache["b"] = a
    return solution.get_value("a")
