"""2020 - Day 2 Part 1: Password Philosophy."""
from __future__ import annotations

from typing import List
from typing import NamedTuple
from typing import Tuple

Password = str


class Policy(NamedTuple):
    char: str
    minimum: int
    maximum: int

    @staticmethod
    def from_str(string: str) -> Policy:
        """E.g. '1-3 a'"""
        diapason, character = string.split()
        minimum, maximum = diapason.split("-")
        return Policy(character, int(minimum), int(maximum))


def process_data(task: str) -> List[Tuple[Policy, Password]]:
    """Line like '4-6 f: fmfgfcf'"""
    entries = []

    for line in task.strip().split("\n"):
        policy_str, password = line.split(": ")
        entries.append((Policy.from_str(policy_str), password))

    return entries


def is_valid(policy: Policy, password: Password) -> bool:
    return policy.minimum <= password.count(policy.char) <= policy.maximum


def solve(task: str) -> int:
    """Count invalid passwords."""
    data = process_data(task)
    return sum(is_valid(policy, password) for (policy, password) in data)
