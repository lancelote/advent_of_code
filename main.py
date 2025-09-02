"""Puzzle Solver Runner."""

import importlib
from typing import Annotated

import typer
from aocd import get_data

from utils.cli import DAY
from utils.cli import PART
from utils.cli import YEAR

app = typer.Typer()


class Solver:
    """Main app class."""

    @staticmethod
    def main(year: int, day: int, part: str) -> None:
        """Print the result to a console."""
        task = get_data(day=day, year=year)

        solver = importlib.import_module(f"src.year{year}.day{day:02}{part}")
        solution = solver.solve(task)  # type: ignore
        print("Answer:", solution)


@app.command()
def main(
    year: Annotated[int, typer.Argument(click_type=YEAR)],
    day: Annotated[int, typer.Argument(click_type=DAY)],
    part: Annotated[str, typer.Argument(click_type=PART)],
):
    """Solve the given puzzle."""
    Solver().main(year, day, part)


if __name__ == "__main__":
    app()
