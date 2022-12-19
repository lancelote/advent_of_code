# advent_of_code

[Advent of code](http://adventofcode.com/) — Programming Christmas Puzzles

★ - both the first and the second parts are solved

☆ - only the first part is solved

- 2015 - ★★★★★ ★★
- 2016 - ★★★★★ ★★
- 2017 - ★★★★★ ★★★★★ ★★
- 2018 - ★★★★★ ★★★★★ ★★
- 2019 - ★★★★★ ★★★★★ ★★★
- 2020 - ★★★★★ ★★★★★ ★★★★★ ☆
- 2021 - ★★★★★ ★★★★★ ★★★★★ ★★★
- 2022 - ★★★★★ ★★★★★ ★★★☆

## How to use

To launch the Puzzle Solver on 2017 year day 5 part “A” puzzle:

```bash
python main.py solve 2017 5 a
```

## Requirements

Solver uses [advent-of-code-data][1] to fetch tasks from the server. You
need to set up a token for it to work. See the [instruction][2].

I use Python 3.11 for development. The code should work fine with older
versions.

To install requirements (virtual environment is recommended)

```bash
python -m pip install -r requirements-dev.txt
```

To update `requirements.txt` with the newest package versions

```bash
pur -r requirements.txt
```

## Tests

I store all the tests in `tests` folder and use `pytest` as a test runner

```bash
python -m pytest tests
```

## Linters

`mypy`, `flake8`, `black`, and `reorder-python-imports` are used in pre-commit
hook. To run linters

```bash
pre-commit install
pre-commit run --all-files
```

# Merry Christmas and Happy New Year!

[1]: https://github.com/wimglenn/advent-of-code-data
[2]: https://github.com/wimglenn/advent-of-code-wim/issues/1
