[![Requirements Status](https://requires.io/github/lancelote/advent_of_code/requirements.svg?branch=master)](https://requires.io/github/lancelote/advent_of_code/requirements/?branch=master)

# advent_of_code

[Advent of code](http://adventofcode.com/) - Programming Christmas Puzzles

- 2015 - ★★★★★★★
- 2016 - ★★★★★★★
- 2017 - ★★★★★★★★★★★★☆
- 2018 - ★★★★★★★★★★★☆

## How to use

To launch the Puzzle Solver on 2017 year day 5 part "A" puzzle:

```bash
python main.py solve 2017 5 a
```

## Requirements

[advent-of-code-data][1] package is used to fetch tasks from the server. You
need to set up a token for it to work. See the [instruction][2].

Python 3.8 is required (at least I am using it). Virtual environment is highly
recommended.

```bash
make install
```

To update `requirements.txt`:

```bash
make pur
```

## Tests

All tests are stored in the `tests` folder, `pytest` is used:

```bash
make test
```

## Syntax Validation

Make sure `pylint`, `pydocstyle`, `pycodestyle` and `mypy` are installed (yes
I love linters) and run:

```bash
make lint
```

# Merry Christmas and Happy New Year!

[1]: https://github.com/wimglenn/advent-of-code-data
[2]: https://github.com/wimglenn/advent-of-code-wim/issues/1
