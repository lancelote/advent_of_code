"""Puzzle Solver Runner."""

import importlib
import os
import sys

import click

SUPPORTED_YEARS = [
    '2015',
    '2016',
    '2017',
    '2018',
]
MANUAL_INPUT = [
    ('2015', 'day4a'),
    ('2015', 'day4b'),
    ('2016', 'day5a'),
    ('2016', 'day5b'),
    ('2017', 'day3a'),
    ('2017', 'day3b'),
    ('2018', 'day11a'),
    ('2018', 'day11b'),
]


class Solver:
    @staticmethod
    def main(year: str, day: str, part: str) -> None:
        """Print the result to a console."""

        task = None
        if year not in SUPPORTED_YEARS:
            print('Unknown year, supported: %s' % ', '.join(SUPPORTED_YEARS))
            sys.exit(1)

        day = 'day' + day
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


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Solver()


# ToDo: setup defaults
# ToDo: extract type validation
@cli.command()
@click.argument('year')
@click.argument('day')
@click.argument('part')
@click.pass_obj
def solve(solver, year, day, part):
    """Solve the given YEAR DAY PART puzzle."""

    solver.main(year, day, part)


if __name__ == '__main__':
    cli()
