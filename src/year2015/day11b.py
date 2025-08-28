"""2015 - Day 11 Part 2: Corporate Policy."""

from dataclasses import dataclass
from string import ascii_lowercase
from typing import Any, Self

TO_INT = {x: i for i, x in enumerate(ascii_lowercase)}
TO_STR = {i: x for i, x in enumerate(ascii_lowercase)}
BANNED = {8, 11, 14}


@dataclass
class Number:
    data: list[int]

    @classmethod
    def from_line(cls, line: str) -> Self:
        return cls([TO_INT[x] for x in line][::-1])

    def __str__(self) -> str:
        return "".join(TO_STR[x] for x in self.data)[::-1]

    def __add__(self, other: Any) -> Self:
        assert isinstance(other, int)
        assert other > 0

        for _ in range(other):
            self.incr()
            while not self.is_valid:
                self.incr()

        return self

    @property
    def is_valid(self) -> bool:
        return not self.has_banned and self.has_two_pairs and self.has_straight

    def incr(self) -> None:
        i = 0
        left = 1

        while left and i < len(self.data):
            self.data[i] = (self.data[i] + left) % 26
            left = self.data[i] == 0
            i += 1

        if left:
            self.data.append(1)

    @property
    def has_banned(self) -> bool:
        for x in self.data:
            if x in BANNED:
                return True
        return False

    @property
    def has_two_pairs(self) -> bool:
        pairs = 0
        used_pair_digits: set[int] = set()

        i = 0
        while i < len(self.data) - 1:
            if self.data[i] == self.data[i + 1] and self.data[i] not in used_pair_digits:
                pairs += 1
                used_pair_digits.add(self.data[i])
                i += 1
            if pairs == 2:
                return True
            i += 1
        return False

    @property
    def has_straight(self) -> bool:
        for i in range(len(self.data) - 2):
            a = self.data[i]
            b = self.data[i + 1] + 1
            c = self.data[i + 2] + 2

            if a == b == c:
                return True
        return False


def solve(task: str) -> str:
    return str(Number.from_line(task) + 2)
