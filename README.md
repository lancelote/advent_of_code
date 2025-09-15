# advent_of_code

[Advent of code](http://adventofcode.com/) — Programming Christmas Puzzles

★ - both the first and the second parts are solved

☆ - only the first part is solved

- 2015 - ★★★★★ ★★★★★ ★★★★★ ★
- 2016 - ★★★★★ ★★
- 2017 - ★★★★★ ★★★★★ ★★
- 2018 - ★★★★★ ★★★★★ ★★
- 2019 - ★★★★★ ★★★★★ ★★★
- 2020 - ★★★★★ ★★★★★ ★★★★★ ☆
- 2021 - ★★★★★ ★★★★★ ★★★★★ ★★★
- 2022 - ★★★★★ ★★★★★ ★★★★★ ★☆
- 2023 - ★★★★★ ★★★★★ ★★★★★ ★★★☆
- 2024 - ★★★★★ ★★★★★ ★★★★★ ☆

## How to use

To launch the Puzzle Solver on 2017 year day 5 part “A” puzzle:

```bash
python main.py solve 2017 5 a
```

## Requirements

Solver uses [advent-of-code-data][1] to fetch tasks from the server. You
need to set up a token for it to work. See the [instruction][2].

For Python version used for development see [.python-version](.python-version).
The code should work fine with older versions, but it is not guaranteed.

To install requirements, `uv` [needs to be installed first](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv sync
```

To update `uv.lock` with the newest package versions

```bash
uv sync --upgrade
```

## Tests

I store all the tests in `tests` folder and use `pytest` as a test runner

```bash
make test
```

## Linters

`basedpyright` and `ruff` are used to check the project

```bash
make check
```

# Merry Christmas and Happy New Year!

[1]: https://github.com/wimglenn/advent-of-code-data
[2]: https://github.com/wimglenn/advent-of-code-wim/issues/1
