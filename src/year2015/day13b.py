"""2015 - Day 13 Part 2: Knights of the Dinner Table."""

from src.year2015.day13a import Preference
from src.year2015.day13a import get_max_happiness
from src.year2015.day13a import process_data


def solve(task: str) -> int:
    preference: Preference = process_data(task)
    names: set[str] = {x[0] for x in preference.keys()}

    names.add("me")

    return get_max_happiness(names, preference)
