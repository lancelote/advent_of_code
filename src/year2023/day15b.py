"""2023 - Day 15 Part 2: Lens Library"""

import re
from collections import defaultdict
from typing import TypeAlias

from src.year2023.day15a import get_hash

Boxes: TypeAlias = dict[int, dict[str, int]]


def parse_task(task: str) -> Boxes:
    boxes: Boxes = defaultdict(dict)

    for step in task.split(","):
        [(label, op, focal)] = re.findall(r"([a-z]+)([=\-])(\d+)?", step)
        box = get_hash(label)

        if op == "=":
            boxes[box][label] = int(focal)
        elif op == "-":
            if label in boxes[box]:
                del boxes[box][label]
        else:
            raise ValueError(f"unknown op: {op}")

    return boxes


def get_focus_power(boxes: Boxes) -> int:
    total = 0

    for box in range(256):
        for slot, (_, focal) in enumerate(boxes[box].items(), start=1):
            total += (box + 1) * slot * focal

    return total


def solve(task: str) -> int:
    boxes = parse_task(task)
    return get_focus_power(boxes)
