[![Requirements Status](https://requires.io/github/lancelote/advent_of_code/requirements.svg?branch=master)](https://requires.io/github/lancelote/advent_of_code/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/advent_of_code.svg?branch=master)](https://travis-ci.org/lancelote/advent_of_code)

# advent_of_code

[Advent of code](http://adventofcode.com/) - Programming Christmas Puzzles

## How to use

Puzzle inputs can be too long for console input, if the file is provided - save and move it to `inputs/{year}/day{n}/`, ex. `inputs/2015/day1/` for Day 1 Puzzle Part 1. If the input file is not provided by the Advent of Code - you will be asked by solver to type in the input (ex. for Day 4 Puzzle Part 1).

To launch Puzzle Solver:
```bash
python main.py
```

## Requirements

Python 3 is required.

For development and testing you should install necessary dependence packages from `requirements.txt`. Virtual environment is recommended.

To update requirements list please use `pur` package:

```bash
pur -r requirements.txt
```

## Tests

All tests are stored in the `tests` folder, `unittest` syntax are used. But feel free to use any test runner you like. I prefer `pytest`:

```bash
pytest tests/
```

## Syntax Validation

Make sure pylint is installed and run:
```bash
pylint main.py src tests
```

# Merry Christmas and Happy New Year!
