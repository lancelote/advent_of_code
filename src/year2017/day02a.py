"""2017 - Day 2 Part 1: Corruption Checksum.

As you walk through the door, a glowing humanoid shape yells in your direction.
"You there! Your state appears to be idle. Come help us repair the corruption
in this spreadsheet - if we take another millisecond, we'll have to display an
hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the
recovery process is on the right track, they need you to calculate the
spreadsheet's checksum. For each row, determine the difference between the
largest value and the smallest value; the checksum is the sum of all of these
differences.

For example, given the following spreadsheet:

    5 1 9 5
    7 5 3
    2 4 6 8

    - The first row's largest and smallest values are 9 and 1, and their
      difference is 8.
    - The second row's largest and smallest values are 7 and 3, and their
      difference is 4.
    - The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
"""
from typing import List


def process_data(data: str) -> List[List[int]]:
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
