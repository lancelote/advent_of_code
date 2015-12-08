# coding=utf-8

"""
Puzzle Solver Runner
"""

from src import day1a, day1b


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    day = input('Pick a puzzle (ex. Day 1): ').lower().replace(' ', '')
    part = input('Pick a puzzle part (A or B): ').lower()
    puzzle = day + part
    try:
        with open('inputs/%s/input.txt' % day) as input_file:
            task = input_file.read()
    except FileNotFoundError:
        print('Input file not found')
        return
    solution = eval(puzzle).solve(task)
    print('Answer:', solution)

if __name__ == '__main__':  # pragma: no cover
    main()
