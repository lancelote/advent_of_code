"""2020 - Day 4 Part 1: Passport Processing."""

from __future__ import annotations

import re
from dataclasses import dataclass

MANDATORY_FIELDS = {
    "byr",  # Birth Year
    "iyr",  # Issue Year
    "eyr",  # Expiration Year
    "hgt",  # Height
    "hcl",  # Hair Color
    "ecl",  # Eye Color
    "pid",  # Passport ID
}


@dataclass
class Passport:
    fields: dict[str, str]

    @classmethod
    def from_str(cls, data: str) -> Passport:
        fields = {}
        for field in re.split(r"\s", data.strip()):
            key, value = field.split(":")
            fields[key] = value
        return cls(fields=fields)

    @property
    def is_valid(self) -> bool:
        return all(
            mandatory_field in self.fields
            for mandatory_field in MANDATORY_FIELDS
        )


def process_data(task: str, document: type[Passport]) -> list[Passport]:
    return [document.from_str(block) for block in task.strip().split("\n\n")]


def solve(task: str) -> int:
    """Count valid passports."""
    passports = process_data(task, Passport)
    return sum(passport.is_valid for passport in passports)
