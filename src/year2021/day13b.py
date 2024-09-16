"""2021 - Day 13 Part 2: Transparent Origami."""

from src.year2021.day13a import parse_task


def solve(task: str) -> int:
    paper, instructions = parse_task(task)

    for instruction in instructions:
        paper.fold(instruction)

    paper.print()
    return -1
