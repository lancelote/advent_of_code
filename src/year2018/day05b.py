"""2018 - Day 5 Part 2: Alchemical Reduction."""
import re
import string

from src.year2018.day05a import solve as length


def solve(task: str) -> int:
    """Find the shortest polymer for each possible reduction."""
    results = []
    polymer = task.strip()

    for char in string.ascii_lowercase:
        pattern = f"{char}|{char.upper()}"
        results.append(length(re.sub(pattern, "", polymer)))

    return min(results)
