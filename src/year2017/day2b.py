"""2017 - Day 2 Part 2: Corruption Checksum.

"Great work; looks like we're on the right track after all. Here's a star for
your effort." However, the program seems a little worried. Can programs be
worried?

"Based on what we're seeing, it looks like all the User wanted is some
information about the evenly divisible values in the spreadsheet.
Unfortunately, none of us are equipped for that kind of calculation - most of
us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one
evenly divides the other - that is, where the result of the division operation
is a whole number. They would like you to find those numbers on each line,
divide them, and add up each line's result.

For example, given the following spreadsheet:

    5 9 2 8
    9 4 7 3
    3 8 6 5

    - In the first row, the only two numbers that evenly divide are 8 and 2;
      the result of this division is 4.
    - In the second row, the two numbers are 9 and 3; the result is 3.
    - In the third row, the result is 2.

In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
"""
from typing import List

from src.year2017.day2a import process_data


def find_division(row: List[int]) -> int:
    """Find two evenly divisible items and return the division result."""
    for i, item1 in enumerate(row):
        for item2 in row[i + 1:]:
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
