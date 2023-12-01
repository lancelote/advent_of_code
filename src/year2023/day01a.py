"""2023 - Day 1 Part 1: Trebuchet?!"""
import re
from collections.abc import Iterator


def process_data(task: str) -> Iterator[str]:
    yield from task.split("\n")


def get_num(line: str) -> int:
    match = re.findall(r"\d", line)
    return int(match[0] + match[-1])


def solve(task: str) -> int:
    return sum(get_num(line) for line in process_data(task))
