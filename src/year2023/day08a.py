"""2023 - Day 8 Part 1: Haunted Wasteland"""
from __future__ import annotations

import itertools
import re


def process_data(data: str) -> tuple[str, dict[str, tuple[str, str]]]:
    instructions, tree_part = data.split("\n\n")

    nodes: dict[str, tuple[str, str]] = {}

    for line in tree_part.splitlines():
        val, left, right = re.findall(r"[A-Z]+", line)
        nodes[val] = (left, right)

    return instructions, nodes


def solve(task: str) -> int:
    instructions, nodes = process_data(task)

    node = "AAA"
    count = 0
    for instruction in itertools.cycle(instructions):
        if node == "ZZZ":
            break
        elif instruction == "L":
            node = nodes[node][0]
        elif instruction == "R":
            node = nodes[node][1]
        else:
            raise ValueError(f"unknown instruction {instruction}")
        count += 1

    return count
