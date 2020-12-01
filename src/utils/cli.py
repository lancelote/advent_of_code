# pylint: disable=inconsistent-return-statements

"""CLI arguments validation helpers."""

import click


SUPPORTED_YEARS = [
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
]


class YearType(click.ParamType):
    """Year validation.

    SUPPORTED_YEARS variable stores all available years (2018, etc.).
    """

    def convert(self, value, param, ctx):
        try:
            assert value in SUPPORTED_YEARS
            return int(value)
        except (TypeError, AssertionError):
            supported_year = "/".join(SUPPORTED_YEARS)
            self.fail(f"Expected {supported_year}, got {value}", param, ctx)


class DayType(click.ParamType):
    """Day validation.

    From 1 to 31 range inclusive.
    """

    def convert(self, value, param, ctx):
        try:
            value = int(value)
            assert value in range(1, 32)
            return value
        except (TypeError, AssertionError):
            self.fail(f"Expected in range 1-31, got {value}", param, ctx)


class PartType(click.ParamType):
    """Task part validation.

    Either literal “a” or “b”.
    """

    def convert(self, value, param, ctx):
        formatted_value = value.lower()
        if formatted_value in ["a", "b"]:
            return formatted_value
        else:
            self.fail(f"Expected either A or B, got {value}", param, ctx)


YEAR = YearType()
DAY = DayType()
PART = PartType()

__all__ = ["YEAR", "DAY", "PART"]
