"""2024 - Day 5 Part 2: ..."""

import functools
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

    def compare(x: int, y: int) -> int:
        if y in rules[x]:
            return -1
        else:
            return +1

    for line in second.split("\n"):
        updates.append([int(x) for x in line.split(",")])

    ans = 0
    for update in updates:
        if not is_valid(update, rules):
            update.sort(key=functools.cmp_to_key(compare))
            middle = update[len(update) // 2]
            ans += middle

    return ans
