"""2017 - Day 2 Part 1: Corruption Checksum."""


def process_data(data: str) -> list[list[int]]:
    """Parse the raw data.

    Return list of rows, each row item is integer.
    """
    rows = [row.split("\t") for row in data.strip().split("\n")]
    return [[int(item) for item in row] for row in rows]


def solve(task: str) -> int:
    """Compute checksum of the given spreadsheet.

    Where checksum is a sum of max and min item difference for each row.
    """
    result = 0
    spreadsheet = process_data(task)
    for row in spreadsheet:
        result += max(row) - min(row)
    return result
