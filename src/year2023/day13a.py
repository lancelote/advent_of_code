"""2023 - Day 13 Part 1: Point of Incidence"""
from dataclasses import dataclass
from functools import reduce
from typing import Self


def mirror_ids(col: str) -> set[int]:
    result: set[int] = set()
    n = len(col)

    for i in range(1, n):
        size = min(n - i, i)

        if col[i - size : i] == col[i : i + size][::-1]:
            result.add(i)

    return result


@dataclass
class Pattern:
    data: list[str]

    @property
    def n_rows(self) -> int:
        return len(self.data)

    @property
    def n_cols(self) -> int:
        return len(self.data[0])

    @property
    def summary(self) -> int:
        common_cols = reduce(
            set.intersection, [mirror_ids(row) for row in self.rows]
        )

        common_rows = reduce(
            set.intersection, [mirror_ids(col) for col in self.cols]
        )

        assert len(common_cols) <= 1
        assert len(common_rows) <= 1

        if common_cols:
            return common_cols.pop()

        if common_rows:
            return common_rows.pop() * 100

        raise ValueError("both common rows and cols are found")

    @property
    def cols(self) -> list[str]:
        return [
            "".join(self.data[r][c] for r in range(self.n_rows))
            for c in range(self.n_cols)
        ]

    @property
    def rows(self) -> list[str]:
        return self.data

    @classmethod
    def from_text(cls, text: str) -> Self:
        return cls(text.splitlines())


def process_data(task: str) -> list[Pattern]:
    return [Pattern.from_text(x) for x in task.split("\n\n")]


def solve(task: str) -> int:
    patterns = process_data(task)
    return sum(p.summary for p in patterns)
