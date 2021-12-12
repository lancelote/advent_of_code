"""2021 - Day 6 Part 1: Lanternfish."""


def tick(ages: list[int]) -> None:
    # Naive and slow - see part 2 for a better solution
    for i in range(len(ages)):
        if ages[i] == 0:
            ages.append(8)
            ages[i] = 6
        else:
            ages[i] -= 1


def solve(task: str) -> int:
    ages = [int(x) for x in task.split(",")]
    for _ in range(80):
        tick(ages)
    return len(ages)
