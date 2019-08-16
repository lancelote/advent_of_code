[![Requirements Status](https://requires.io/github/lancelote/advent_of_code/requirements.svg?branch=master)](https://requires.io/github/lancelote/advent_of_code/requirements/?branch=master)

# advent_of_code

[Advent of code](http://adventofcode.com/) - Programming Christmas Puzzles

- 2015 - ★★★★★★★
- 2016 - ★★★★★★★
- 2017 - ★★★★★★★★★★★★☆
- 2018 - ★★★★★★★★★★★☆

## How to use

Puzzle inputs can be too long for console input, if an input file is provided - save and move it to `inputs/{year}/day{n}/`, ex. `inputs/2015/day1/` for Day 1 Puzzle Part 1. If an input file is not expected - you will be asked by the solver for manual input (ex. for Day 4 Puzzle Part 1).

To launch the Puzzle Solver:
```bash
python main.py
# or
make run
```

For all automation tasks I use `Makefile`. You can skip it entirely and just manually run commands from it. If you are on Windows you can get `make` with `mingw` or `cygwin` (I use `mingw` while develop on windows machine).

## Requirements

Python 3.7 is required (at least it was tested with it).

For development and testing you should install necessary dependence packages from `requirements.txt`. Virtual environment is highly recommended.

```bash
make update
```

To update `requirements.txt`:

```bash
make deps
```

## Tests

All tests are stored in the `tests` folder, `pytest` is used:

```bash
make test
```

## Syntax Validation

Make sure `pylint`, `pydocstyle`, `pycodestyle` and `mypy` are installed (yes I love linters) and run:

```bash
make lint
```

# Merry Christmas and Happy New Year!
