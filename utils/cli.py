"""CLI arguments validation helpers."""

from collections.abc import Sequence

OLDEST_YEAR = 2015
NEWEST_YEAR = 2024


def convert_year(value: str) -> int:
    try:
        year = int(value)
        assert OLDEST_YEAR <= year < NEWEST_YEAR
        return year
    except (TypeError, AssertionError) as err:
        raise ValueError(f"unsupported year: {value}") from err


def convert_day(value: str) -> int:
    try:
        day = int(value)
        assert 1 <= day < 32
        return day
    except (TypeError, AssertionError) as err:
        raise ValueError(f"want int in range 1-31, got {value}") from err


def convert_part(value: str) -> str:
    formatted_value = value.lower()
    if formatted_value in {"a", "b"}:
        return formatted_value
    else:
        raise ValueError(f"want either `a` or `b`, got `{value}`")


def convert_argv(argv: Sequence[str]) -> tuple[int, int, str]:
    assert len(argv) == 3, "arguments: year day part"

    a, b, c = argv

    year = convert_year(a)
    day = convert_day(b)
    part = convert_part(c)

    return year, day, part
