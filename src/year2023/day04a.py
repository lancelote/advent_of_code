"""2023 - Day 4 Part 1: Scratchcards"""
from dataclasses import dataclass
from typing import Self


@dataclass
class Card:
    pk: int
    winning: set[int]
    numbers: set[int]

    @classmethod
    def from_line(cls, line: str) -> Self:
        card_part, scratch_part = line.split(": ")
        _, pk_part = card_part.split()
        pk = int(pk_part)

        winning_part, numbers_part = scratch_part.split(" | ")
        winning = {int(x) for x in winning_part.split()}
        numbers = {int(x) for x in numbers_part.split()}
        return cls(pk, winning, numbers)

    @property
    def matching(self) -> int:
        count = 0

        for x in self.numbers:
            if x in self.winning:
                count += 1

        return count

    @property
    def points(self) -> int:
        return int(2 ** (self.matching - 1)) if self.matching else 0


def process_data(task: str) -> list[Card]:
    return [Card.from_line(line) for line in task.splitlines()]


def solve(task: str) -> int:
    cards = process_data(task)
    return sum(card.points for card in cards)
