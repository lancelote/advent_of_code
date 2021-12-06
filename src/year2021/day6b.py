"""2021 - Day 6 Part 2: Lanternfish."""
from collections import deque


def tick(adults: deque[int], children: deque[int]) -> None:
    adult_gen = adults.popleft()
    children_gen = children.popleft()

    adults.append(adult_gen + children_gen)
    children.append(adult_gen)


def solve(task: str) -> int:
    ages = [int(x) for x in task.split(",")]

    day0 = 0
    day1 = ages.count(1)
    day2 = ages.count(2)
    day3 = ages.count(3)
    day4 = ages.count(4)
    day5 = ages.count(5)
    day6 = 0
    day7 = 0
    day8 = 0

    children = deque([day7, day8])
    adults = deque([day0, day1, day2, day3, day4, day5, day6])

    for _ in range(256):
        tick(adults, children)

    return sum(adults) + sum(children)
