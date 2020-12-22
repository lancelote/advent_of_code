"""2020 - Day 8 Part 1: Handheld Halting."""
from __future__ import annotations
from typing import List
from dataclasses import dataclass


@dataclass
class Transmission:
    data: List
    preamble_len: int

    @classmethod
    def from_string(cls, string: str, preamble_len: int) -> Transmission:
        numbers = [int(num) for num in string.strip().split("\n")]
        return cls.from_data(numbers, preamble_len)

    @classmethod
    def from_data(cls, data: List[int], preamble_len: int) -> Transmission:
        return cls(data, preamble_len)

    @property
    def first_invalid(self) -> int:
        # ToDo: implement
        ...


def solve(task: str) -> int:
    """What is the first invalid number?"""
    transmission = Transmission.from_string(task, preamble_len=25)
    return transmission.first_invalid
