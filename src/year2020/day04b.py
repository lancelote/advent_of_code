"""2020 - Day 4 Part 2: Passport Processing."""

import re

from src.year2020.day04a import Passport as LegacyPassport
from src.year2020.day04a import process_data

YEAR_PATTERN = r"^\d{4}$"


class Passport(LegacyPassport):
    @property
    def valid_byr(self) -> bool:
        """
        byr (Birth Year) - four digits; at least 1920 and at most 2002
        """
        match = re.match(YEAR_PATTERN, self.fields["byr"])
        if match:
            byr = int(match.group())
            return 1920 <= byr <= 2002
        else:
            return False

    @property
    def valid_iyr(self) -> bool:
        """
        iyr (Issue Year) - four digits; at least 2010 and at most 2020
        """
        match = re.match(YEAR_PATTERN, self.fields["iyr"])
        if match:
            iyr = int(match.group())
            return 2010 <= iyr <= 2020
        else:
            return False

    @property
    def valid_eyr(self) -> bool:
        """
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030
        """
        match = re.match(YEAR_PATTERN, self.fields["eyr"])
        if match:
            eyr = int(match.group())
            return 2020 <= eyr <= 2030
        else:
            return False

    @property
    def valid_hgt(self) -> bool:
        """
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193
            If in, the number must be at least 59 and at most 76
        """
        match = re.match(r"^(?P<number>\d+)(cm|in)$", self.fields["hgt"])
        if match:
            hgt = match.group()
            number = int(match.group("number"))
            if hgt.endswith("cm"):
                return 150 <= number <= 193
            elif hgt.endswith("in"):
                return 59 <= number <= 76
            else:
                raise ValueError(f"unexpect hgt: ${hgt}")
        else:
            return False

    @property
    def valid_hcl(self) -> bool:
        """
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
        """
        return bool(re.match(r"^#[0-9a-f]{6}$", self.fields["hcl"]))

    @property
    def valid_ecl(self) -> bool:
        """
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
        """
        regex = r"^(amb|blu|brn|gry|grn|hzl|oth)$"
        return bool(re.match(regex, self.fields["ecl"]))

    @property
    def valid_pid(self) -> bool:
        """
        pid (Passport ID) - a nine-digit number, including leading zeroes
        """
        return bool(re.match(r"^\d{9}$", self.fields["pid"]))

    @property
    def is_valid(self) -> bool:
        return super().is_valid and all(
            [
                self.valid_byr,
                self.valid_iyr,
                self.valid_eyr,
                self.valid_hgt,
                self.valid_hcl,
                self.valid_ecl,
                self.valid_pid,
            ]
        )


def solve(task: str) -> int:
    """Count valid passports."""
    passports = process_data(task, Passport)
    return sum(passport.is_valid for passport in passports)
