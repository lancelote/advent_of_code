# advent_of_code

[Advent of code](http://adventofcode.com/) - Programming Christmas Puzzles

## How to use

Puzzle inputs can be too long for console input, so save and move them to
`inputs/day{n}{part:a|b}/`, ex. `inputs/day1a/` for Day 1 Puzzle Part 1

Puzzle solver will catch them on the fly!

To launch Puzzle Solver:
```bash
python main.py
```

## Requirements

Python 3 is required.

For development and testing you should install necessary dependence packages
from `requirements.txt`. Virtual environment is recommended.

To update requirements please use `pip-tools` package:

- Update `requirements.in`
- Compile `requirements.txt` with `pip-compile`
- Install/upgrade with `pip-sync`

## ToDo

- [ ] CI
- [ ] paver
- [ ] syntax validation
- [ ] test coverage
- [ ] main testing
