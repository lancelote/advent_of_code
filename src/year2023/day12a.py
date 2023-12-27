"""2023 - Day 12 Part 1: Hot Springs"""
from dataclasses import dataclass
from typing import Self


@dataclass
class Row:
    springs: str
    segments: list[int]

    @property
    def arrangements(self) -> int:
        n = len(self.segments)

        def dfs(i: int, j: int, filled: int) -> int:
            if i == len(self.springs):
                if (j == n and filled == 0) or (
                    j == n - 1 and filled == self.segments[j]
                ):
                    return 1
                else:
                    return 0

            count = 0

            if self.springs[i] in {".", "?"}:
                if filled == 0:
                    count += dfs(i + 1, j, filled)
                elif filled == self.segments[j]:
                    count += dfs(i + 1, j + 1, 0)

            if self.springs[i] in {"#", "?"}:
                if j < n and filled < self.segments[j]:
                    count += dfs(i + 1, j, filled + 1)

            return count

        return dfs(0, 0, 0)

    @classmethod
    def from_line(cls, line: str) -> Self:
        springs, segments_part = line.split()
        segments = [int(x) for x in segments_part.split(",")]
        return cls(springs, segments)


@dataclass
class Field:
    rows: list[Row]

    @classmethod
    def from_task(cls, task: str) -> Self:
        return cls([Row.from_line(line) for line in task.splitlines()])


def solve(task: str) -> int:
    field = Field.from_task(task)
    return sum(r.arrangements for r in field.rows)
