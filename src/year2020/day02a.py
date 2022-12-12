"""2020 - Day 2 Part 1: Password Philosophy."""
from __future__ import annotations

from typing import NamedTuple

Password = str


class Policy(NamedTuple):
    char: str
    first: int
    second: int

    @staticmethod
    def from_str(string: str) -> Policy:
        """E.g. '1-3 a'"""
        diapason, character = string.split()
        first, second = diapason.split("-")
        return Policy(character, int(first), int(second))


def process_data(task: str) -> list[tuple[Policy, Password]]:
    """Line like '4-6 f: fmfgfcf'"""
    entries = []

    for line in task.strip().split("\n"):
        policy_str, password = line.split(": ")
        entries.append((Policy.from_str(policy_str), password))

    return entries


def is_valid(policy: Policy, password: Password) -> bool:
    return policy.first <= password.count(policy.char) <= policy.second


def solve(task: str) -> int:
    """Count invalid passwords."""
    data = process_data(task)
    return sum(is_valid(policy, password) for (policy, password) in data)
