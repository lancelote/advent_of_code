"""2021 - Day 18 Part 2: Snailfish."""
from src.year2021.day18a import Node


def solve(task: str) -> int:
    nums = [Node.from_line(line) for line in task.splitlines()]

    biggest = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            magnitude1 = (nums[i] + nums[j]).magnitude
            magnitude2 = (nums[j] + nums[i]).magnitude

            biggest = max(biggest, magnitude1, magnitude2)

    return biggest
