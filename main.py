"""Puzzle Solver Runner."""

import importlib
import os

SUPPORTED_YEARS = [
    '2015',
    '2016',
    '2017',
]
MANUAL_INPUT = [
    ('2015', 'day4a'),
    ('2015', 'day4b'),
    ('2016', 'day5a'),
    ('2016', 'day5b'),
    ('2017', 'day3a'),
    ('2017', 'day3b'),
]


def main():  # pragma: no cover
    """Print the result to a console."""
    task = None
    year = input('Pick a year (%s): ' % '/'.join(SUPPORTED_YEARS)).strip()
    if year not in SUPPORTED_YEARS:
        print('Unknown year, supported: %s' % ', '.join(SUPPORTED_YEARS))
        return

    day = input('Pick a puzzle (ex. Day 1): ').lower().replace(' ', '')
    part = input('Pick a puzzle part (A or B): ').lower()
    puzzle = day + part

    if (year, puzzle) in MANUAL_INPUT:
        task = input('Puzzle input: ')
    else:
        for file_name in ['input.txt', 'input']:
            try:
                file_path = os.path.join('inputs', year, day, file_name)
                with open(file_path) as input_file:
                    task = input_file.read()
            except FileNotFoundError:
                pass  # Try another file name

        if task is None:
            print('Input file not found')
            return

    solver = importlib.import_module('src.year%s.%s' % (year, puzzle))
    solution = solver.solve(task)
    print('Answer:', solution)


if __name__ == '__main__':  # pragma: no cover
    main()
