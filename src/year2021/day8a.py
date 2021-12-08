"""2021 - Day 8 Part 1: ."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Entry:
    signal: list[str]
    output: list[str]

    @classmethod
    def from_line(cls, line: str) -> Entry:
        first, second = line.split(" | ")
        signal = first.strip().split(" ")
        output = second.strip().split(" ")
        return cls(signal, output)


def process_data(data: str) -> list[Entry]:
    lines = data.strip().split("\n")
    return [Entry.from_line(line) for line in lines]


def solve(task: str) -> int:
    entries = process_data(task)
    simple = {2, 3, 4, 7}
    return sum(
        len(pattern) in simple for entry in entries for pattern in entry.output
    )
