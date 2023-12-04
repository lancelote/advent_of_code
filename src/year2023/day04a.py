"""2023 - Day 4 Part 1: Scratchcards"""
from dataclasses import dataclass
from typing import Self


@dataclass
class Card:
    winning: set[int]
    numbers: set[int]

    @classmethod
    def from_line(cls, line: str) -> Self:
        _, scratch_part = line.split(": ")
        winning_part, numbers_part = scratch_part.split(" | ")
        winning = {int(x) for x in winning_part.split()}
        numbers = {int(x) for x in numbers_part.split()}
        return cls(winning, numbers)

    @property
    def points(self) -> int:
        matching = 0

        for x in self.numbers:
            if x in self.winning:
                matching += 1

        return int(2 ** (matching - 1)) if matching else 0


def process_data(task: str) -> list[Card]:
    return [Card.from_line(line) for line in task.splitlines()]


def solve(task: str) -> int:
    cards = process_data(task)
    return sum(card.points for card in cards)
