"""2015 - Day 8 Part 1: Matchsticks."""

from dataclasses import dataclass
from typing import Self


@dataclass
class String:
    in_code: int
    in_memory: int
    text: str

    @classmethod
    def from_line(cls, line: str) -> Self:
        in_code = len(line)
        in_memory = -2  # for quotes

        i = 0
        while i < len(line):
            if line[i] == "\\":
                match line[i + 1]:
                    case "x":
                        i += 4
                    case '"':
                        i += 2
                    case "\\":
                        i += 2
                    case _:
                        assert ValueError("unknown escape")
            else:
                i += 1
            in_memory += 1

        return cls(in_code, in_memory, line)


def process_data(task: str) -> list[String]:
    return [String.from_line(line) for line in task.strip().split("\n")]


def solve(task: str) -> int:
    return sum(x.in_code - x.in_memory for x in process_data(task))
