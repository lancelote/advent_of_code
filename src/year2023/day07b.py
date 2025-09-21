"""2023 - Day 7 Part 2: Camel Cards"""

from collections import Counter
from functools import cached_property
from typing import Self

CARDS = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
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

    @classmethod
    def from_line(cls, line: str) -> Self:
        # e.g., "72772 82"
        cards, bid_part = line.split()
        return cls(cards, int(bid_part))

    @cached_property
    def value(self) -> int:
        return get_value_with_joker(self.cards)

    def __lt__(self, other: Self) -> bool:
        if self.value == other.value:
            for a, b in zip(self.cards, other.cards, strict=True):
                if a != b:
                    return CARDS[a] < CARDS[b]

        return self.value < other.value


def is_five_of_a_kind(count: list[int]) -> bool:
    return count == [5]


def is_four_of_a_kind(count: list[int]) -> bool:
    return count == [1, 4]


def is_full_house(count: list[int]) -> bool:
    return count == [2, 3]


def is_three_of_a_kind(count: list[int]) -> bool:
    return count == [1, 1, 3]


def is_two_pair(count: list[int]) -> bool:
    return count == [1, 2, 2]


def is_one_pair(count: list[int]) -> bool:
    return count == [1, 1, 1, 2]


def get_value_with_joker(cards: str) -> int:
    max_value = -1

    for card_option in CARDS.keys():
        hand_option = cards.replace("J", card_option)

        count = sorted(list(Counter(hand_option).values()))

        if is_five_of_a_kind(count):
            value = 18
        elif is_four_of_a_kind(count):
            value = 17
        elif is_full_house(count):
            value = 16
        elif is_three_of_a_kind(count):
            value = 15
        elif is_two_pair(count):
            value = 14
        elif is_one_pair(count):
            value = 13
        else:
            value = -1

        max_value = max(max_value, value)

        if "J" not in cards:
            break

    return max_value


def process_data(data: str) -> list[Hand]:
    return [Hand.from_line(line) for line in data.splitlines()]


def solve(task: str) -> int:
    hands = process_data(task)
    hands = sorted(hands)
    return sum(i * h.bid for i, h in enumerate(hands, start=1))
