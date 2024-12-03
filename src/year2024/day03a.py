"""2024 - Day 3 Part 1: Mull It Over"""

import re


def solve(task: str) -> int:
    result = re.findall(r"mul\((\d+),(\d+)\)", task)
    return sum(int(a) * int(b) for a, b in result)
