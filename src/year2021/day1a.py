"""2021 - Day 1 Part 1: Sonar Sweep."""


def solve(task: str) -> int:
    result = 0
    depths = [int(x) for x in task.strip().split("\n")]
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            result += 1
    return result
