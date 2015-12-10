# coding=utf-8

"""
Puzzle Solver Runner
"""

import importlib


def main():  # pragma: no cover
    """Prints the result to a console"""
    task = None
    day = input('Pick a puzzle (ex. Day 1): ').lower().replace(' ', '')
    part = input('Pick a puzzle part (A or B): ').lower()
    puzzle = day + part

    if puzzle in ['day4a', 'day4b']:
        task = input('Puzzle input: ')
    else:
        for file_name in ['input.txt', 'input']:
            try:
                with open('inputs/%s/%s' % (day, file_name)) as input_file:
                    task = input_file.read()
            except FileNotFoundError:
                pass

        if task is None:
            print('Input file not found')
            return

    solver = importlib.import_module('src.%s' % puzzle)
    solution = solver.solve(task)
    print('Answer:', solution)

if __name__ == '__main__':  # pragma: no cover
    main()
