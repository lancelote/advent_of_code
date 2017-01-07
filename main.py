"""Puzzle Solver Runner."""

import os
import importlib


def main():  # pragma: no cover
    """Print the result to a console."""
    task = None
    year = input('Pick a year (2015/2016): ').strip()
    day = input('Pick a puzzle (ex. Day 1): ').lower().replace(' ', '')
    part = input('Pick a puzzle part (A or B): ').lower()
    puzzle = day + part

    if year not in ['2015', '2016']:
        print('Unknown year, please specify 2015 or 2016')
        return

    # Special case for puzzles without input files
    if (year == '2015' and puzzle in ['day4a', 'day4b']) or \
            (year == '2016' and puzzle in ['day5a', 'day5b']):
        task = input('Puzzle input: ')

    # Everything else should have a separate input file
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
