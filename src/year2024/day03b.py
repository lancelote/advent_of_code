"""2024 - Day 3 Part 2: Mull It Over"""

import re


def solve(task: str) -> int:
    result = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", task)

    ans = 0
    skip = False

    for a, b, do, dnt in result:
        if dnt:
            skip = True
        elif do:
            skip = False
        elif skip:
            continue
        else:
            a = int(a)
            b = int(b)
            ans += a * b

    return ans
