"""2015 - Day 16 Part 2: Aunt Sue."""

from src.year2015.day16a import SENDER
from src.year2015.day16a import Aunt
from src.year2015.day16a import process_data


def contradicts(aunt: Aunt, sender: Aunt) -> bool:
    for k, v in aunt.items():
        match k:
            case "cats" | "trees":
                if v <= sender[k]:
                    return True
            case "pomeranians" | "goldfish":
                if v >= sender[k]:
                    return True
            case _:
                if sender[k] != v:
                    return True
    return False


def solve(task: str) -> int:
    aunts = process_data(task)
    for i, aunt in enumerate(aunts, start=1):
        if not contradicts(aunt, SENDER):
            return i

    raise ValueError("no answer found")
