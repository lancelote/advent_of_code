# pylint: disable=no-value-for-parameter

"""Puzzle Solver Runner."""

import importlib

from aocd import get_data
import click

from src.utils.cli import YEAR, PART, DAY

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
    """Main app class."""

    @staticmethod
    def main(year: int, day: int, part: str) -> None:
        """Print the result to a console."""
        task = get_data(day=day, year=year)

        solver = importlib.import_module(f'src.year{year}.day{day}{part}')
        solution = solver.solve(task)  # type: ignore
        print('Answer:', solution)


@click.group()
@click.pass_context
def cli(ctx):
    """Solve Advent of Code puzzles."""
    ctx.obj = Solver()


@cli.command()
@click.argument('year', type=YEAR)
@click.argument('day', type=DAY)
@click.argument('part', type=PART)
@click.pass_obj
def solve(solver, year, day, part):
    """Solve the given YEAR DAY PART puzzle."""
    solver.main(year, day, part)


if __name__ == '__main__':
    cli()
