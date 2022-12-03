"""2022 - Day 3 Part 1: Rucksack Reorganization."""
from dataclasses import dataclass


@dataclass
class Rucksack:
    items: str

    @property
    def duplicate(self) -> str:
        middle = len(self.items) // 2
        left = set(self.items[:middle])
        right = set(self.items[middle:])
        return (left & right).pop()


def priority(char: str) -> int:
    assert len(char) == 1

    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def process_data(task: str) -> list[Rucksack]:
    return [Rucksack(line) for line in task.strip().splitlines()]


def solve(task: str) -> int:
    return sum(priority(x.duplicate) for x in process_data(task))
