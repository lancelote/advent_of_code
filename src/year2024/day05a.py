"""2024 - Day 5 Part 1: Print Queue"""

from collections import defaultdict


def is_valid(update: list[int], rules: dict[int, set[int]]) -> bool:
    for i in range(len(update) - 1):
        a = update[i]
        b = update[i + 1]

        if b not in rules[a]:
            return False

    return True


def solve(task: str) -> int:
    first, second = task.split("\n\n")
    rules: dict[int, set[int]] = defaultdict(set)

    for line in first.split("\n"):
        a, b = line.split("|")
        rules[int(a)].add(int(b))

    updates: list[list[int]] = []

    for line in second.split("\n"):
        updates.append([int(x) for x in line.split(",")])

    ans = 0
    for update in updates:
        if is_valid(update, rules):
            middle = update[len(update) // 2]
            ans += middle

    return ans
