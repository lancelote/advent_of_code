"""2017 - Day 2 Part 2: Corruption Checksum."""
from src.year2017.day02a import process_data


def find_division(row: list[int]) -> int:
    """Find two evenly divisible items and return the division result."""
    for i, item1 in enumerate(row):
        for item2 in row[i + 1 :]:
            if item1 % item2 == 0:
                return item1 // item2
            if item2 % item1 == 0:
                return item2 // item1
    return 0


def solve(task: str) -> int:
    """Compute checksum of the given spreadsheet.

    Where checksum is a sum of division result of two evenly divisible items
    for each row.
    """
    result = 0
    spreadsheet = process_data(task)
    for row in spreadsheet:
        result += find_division(row)
    return result
