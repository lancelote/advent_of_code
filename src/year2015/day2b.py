# coding=utf-8

"""
--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they
only have to worry about the length they need to order, which they would again
like to be exact.

The ribbon required to wrap a present is the shortest distance around its
sides, or the smallest perimeter of any one face. Each present also requires a
bow made out of ribbon as well; the feet of ribbon required for the perfect bow
is equal to the cubic feet of volume of the present. Don't ask how they tie the
bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to
    wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total
    of 34 feet.

    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to
    wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total
    of 14 feet.

How many total feet of ribbon should they order?
"""

from functools import reduce
from operator import mul

from src.year2015.day2a import process_data


def solve(task):
    """
    Solve the puzzle

    Args:
        task (str): length x width x height \n ... (without spaces)

    Returns:
        int: Total feet of ribbon
    """
    data = process_data(task)
    return sum(2*(sum(size) - max(size)) + reduce(mul, size, 1)
               for size in data)
