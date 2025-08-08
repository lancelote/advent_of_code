"""2015 - Day 12 Part 1: JSAbacusFramework.io."""

import re


def solve(task: str) -> int:
    return sum(int(x) for x in re.findall("-?[0-9]+", task))
