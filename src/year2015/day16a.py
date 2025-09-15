"""2015 - Day 16 Part 1: Aunt Sue."""

import re

type Aunt = dict[str, int]


def aunt_from_line(line: str) -> Aunt:
    aunt: Aunt = {}

    fields: list[tuple[str, str]] = re.findall(r" ([a-z]+): (\d+)", line)
    for k, v in fields:
        aunt[k] = int(v)

    return aunt


def contradicts(aunt: Aunt, sender: Aunt) -> bool:
    for k, v in aunt.items():
        if sender[k] != v:
            return True
    return False


def process_data(task: str) -> list[Aunt]:
    return [aunt_from_line(line) for line in task.splitlines()]


def solve(task: str) -> int:
    sender = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    aunts = process_data(task)
    for i, aunt in enumerate(aunts, start=1):
        if not contradicts(aunt, sender):
            return i

    raise ValueError("no answer found")
