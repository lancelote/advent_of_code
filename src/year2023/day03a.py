"""2023 - Day 3 Part 1: Gear Ratios"""
from dataclasses import dataclass
from typing import Self

SHIFTS = (
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
    (-1, -1),
)


@dataclass
class Symbol:
    value: str
    coords: tuple[int, int]

    @classmethod
    def from_coords(cls, r: int, c: int, data: list[str]) -> Self | None:
        value: str | None = None

        while value is None and c < len(data[r]) and data[r][c].isdigit():
            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(data) and 0 <= nc < len(data[nr]):
                    value_opt = data[nr][nc]

                    if not value_opt.isdigit() and value_opt != ".":
                        return cls(value_opt, (nr, nc))

            c += 1

        return None


@dataclass
class Part:
    symbol: Symbol
    number: int

    @classmethod
    def from_coords(cls, r: int, c: int, data: list[str]) -> Self | None:
        if c > 0 and data[r][c - 1].isdigit():
            return None  # already parsed

        shift = 0
        num_list_str: list[str] = []

        while c + shift < len(data[r]) and data[r][c + shift].isdigit():
            num_list_str.append(data[r][c + shift])
            shift += 1

        num = int("".join(num_list_str))
        symbol = Symbol.from_coords(r, c, data)

        return cls(symbol, num) if symbol else None


def process_data(task: str) -> list[Part]:
    data = task.splitlines()
    parts: list[Part] = []

    for r, row in enumerate(data):
        for c, x in enumerate(row):
            if x.isdigit():
                part = Part.from_coords(r, c, data)
                if part:
                    parts.append(part)

    return parts


def solve(task: str) -> int:
    parts = process_data(task)
    return sum(part.number for part in parts)
