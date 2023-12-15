"""2023 - Day 8 Part 2: Haunted Wasteland"""
import functools
import itertools
import math

from src.year2023.day08a import process_data


def solve(task: str) -> int:
    instructions, nodes = process_data(task)

    starts = [k for k in nodes.keys() if k.endswith("A")]
    cycles: list[int] = []

    for start in starts:
        node = start
        count = 0

        iter_inst = itertools.cycle(instructions)
        while not node.endswith("Z"):
            inst = next(iter_inst)
            if inst == "L":
                node = nodes[node][0]
            else:
                node = nodes[node][1]
            count += 1
        cycles.append(count)

    return int(functools.reduce(math.lcm, cycles))
