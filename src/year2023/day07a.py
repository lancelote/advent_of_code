"""2023 - Day 7 Part 1: Camel Cards"""

from collections import Counter
from typing import Self

CARDS = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


class Hand:
    cards: str
    bid: int
    count: list[int]

    def __init__(self, cards: str, bid: int = 0) -> None:
        self.cards = cards
        self.bid = bid
        self.count = sorted(list(Counter(cards).values()))

    @classmethod
    def from_line(cls, line: str) -> Self:
        # e.g., "72772 82"
        cards, bid_part = line.split()
        return cls(cards, int(bid_part))

    @property
    def five_of_a_kind(self) -> bool:
        return self.count == [5]

    @property
    def four_of_a_kind(self) -> bool:
        return self.count == [1, 4]

    @property
    def full_house(self) -> bool:
        return self.count == [2, 3]

    @property
    def three_of_a_kind(self) -> bool:
        return self.count == [1, 1, 3]

    @property
    def two_pair(self) -> bool:
        return self.count == [1, 2, 2]

    @property
    def one_pair(self) -> bool:
        return self.count == [1, 1, 1, 2]

    @property
    def value(self) -> int:
        if self.five_of_a_kind:
            return 18
        elif self.four_of_a_kind:
            return 17
        elif self.full_house:
            return 16
        elif self.three_of_a_kind:
            return 15
        elif self.two_pair:
            return 14
        elif self.one_pair:
            return 13
        else:
            return -1

    def __lt__(self, other: Self) -> bool:
        if self.value == other.value:
            for a, b in zip(self.cards, other.cards, strict=True):
                if a != b:
                    return CARDS[a] < CARDS[b]

        return self.value < other.value


def process_data(data: str) -> list[Hand]:
    return [Hand.from_line(line) for line in data.splitlines()]


def solve(task: str) -> int:
    hands = process_data(task)
    hands = sorted(hands)
    return sum(i * h.bid for i, h in enumerate(hands, start=1))
