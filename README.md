[![Requirements Status](https://requires.io/github/lancelote/advent_of_code/requirements.svg?branch=master)](https://requires.io/github/lancelote/advent_of_code/requirements/?branch=master)

# advent_of_code

[Advent of code](http://adventofcode.com/) — Programming Christmas Puzzles

★ - both the first and the second parts are solved
☆ - only the first part is solved

- 2015 - ★★★★★★★
- 2016 - ★★★★★★★
- 2017 - ★★★★★★★★★★★★☆
- 2018 - ★★★★★★★★★★★★
- 2019 - ★★☆

## How to use

To launch the Puzzle Solver on 2017 year day 5 part “A” puzzle:

```bash
python main.py solve 2017 5 a
```

## Requirements

Solver uses [advent-of-code-data][1] to fetch tasks from the server. You
need to set up a token for it to work. See the [instruction][2].

I use Python 3.8 for development. The code should work fine on Python 3.7 as
well.

```bash
make install
```

To update `requirements.txt`:

```bash
make pur
```

## Tests

I store all the tests in `tests` folder and use `pytest` as a test runner:

```bash
make test
```

## Syntax Validation

Make sure to have `pylint`, `pydocstyle`, `pycodestyle` and `mypy` installed
(yes I love linters) and run:

```bash
make lint
```

# Merry Christmas and Happy New Year!

[1]: https://github.com/wimglenn/advent-of-code-data
[2]: https://github.com/wimglenn/advent-of-code-wim/issues/1
