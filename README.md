[![Requirements Status](https://requires.io/github/lancelote/advent_of_code/requirements.svg?branch=master)](https://requires.io/github/lancelote/advent_of_code/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/advent_of_code.svg?branch=master)](https://travis-ci.org/lancelote/advent_of_code)

# advent_of_code

[Advent of code](http://adventofcode.com/) - Programming Christmas Puzzles

## How to use

Puzzle inputs can be too long for console input, if the file is provided - save and move it to `inputs/{year}/day{n}/`, ex. `inputs/2015/day1/` for Day 1 Puzzle Part 1. If the input file is not provided by the Advent of Code - you will be asked by solver to type in the input (ex. for Day 4 Puzzle Part 1).

To launch Puzzle Solver:
```bash
python main.py
# or
make run
```

For all automation tasks I use `Makefile`. You can skip it entirely and just manually run commands from it. If you on Windows you can get `make` with `mingw` or `cygwin` (I use `mingw` while develop on windows machine).

## Requirements

Python 3.5 is required.

For development and testing you should install necessary dependence packages from `requirements.txt`. Virtual environment is recommended.

```bash
make update
```

To update requirements list:

```bash
make requirements
```

## Tests

All tests are stored in the `tests` folder, `unittest` syntax is used. But feel free to use any test runner you like. I prefer `pytest`:

```bash
make test
```

## Syntax Validation

Make sure `pylint`, `pydocstyle`, `pycodestyle` and `mypy` are installed (yes I love linters) and run:

```bash
make lint
```

# Merry Christmas and Happy New Year!
