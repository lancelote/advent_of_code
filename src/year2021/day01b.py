"""2021 - Day 1 Part 2: Sonar Sweep."""


def solve(task: str) -> int:
    result = 0
    depths = [int(x) for x in task.strip().split("\n")]

    previous = depths[0] + depths[1] + depths[2]

    for i in range(1, len(depths) - 2):
        current = depths[i] + depths[i + 1] + depths[i + 2]
        if current > previous:
            result += 1
        previous = current

    return result
