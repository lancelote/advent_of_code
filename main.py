# pylint: disable=no-value-for-parameter

"""Puzzle Solver Runner."""

import importlib

from aocd import get_data
import click

from src.utils.cli import YEAR, PART, DAY


class Solver:
    """Main app class."""

    @staticmethod
    def main(year: int, day: int, part: str) -> None:
        """Print the result to a console."""
        task = get_data(day=day, year=year)

        solver = importlib.import_module(f"src.year{year}.day{day}{part}")
        solution = solver.solve(task)  # type: ignore
        print("Answer:", solution)


@click.group()
@click.pass_context
def cli(ctx):
    """Solve Advent of Code puzzles."""
    ctx.obj = Solver()


@cli.command()
@click.argument("year", type=YEAR)
@click.argument("day", type=DAY)
@click.argument("part", type=PART)
@click.pass_obj
def solve(solver, year, day, part):
    """Solve the given puzzle."""
    solver.main(year, day, part)


if __name__ == "__main__":
    cli()
