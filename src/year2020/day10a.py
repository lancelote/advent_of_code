"""2020 - Day 10 Part 1: Adapter Array."""
from collections import defaultdict
from typing import DefaultDict


def process_data(data: str) -> list[int]:
    return [int(x) for x in data.strip().split("\n")]


def find_differences(adapters: list[int]) -> DefaultDict[int, int]:
    current = 0
    differences: DefaultDict[int, int] = defaultdict(int)

    for adapter in sorted(adapters):
        differences[adapter - current] += 1
        current = adapter

    return differences


def solve(task: str) -> int:
    """Jolt difference"""
    adapters = process_data(task)
    differences = find_differences(adapters)
    return differences[1] * (differences[3] + 1)
