import re
from pathlib import Path

import pytest

from main import main


def test_solve(mock_get_data, capsys):
    data = "411 players; last marble is worth 71058 points"
    mock_get_data.return_value = data

    main(["2018", "9", "a"])

    assert capsys.readouterr().out == "answer: 424639\n"


def test_wrong_year():
    with pytest.raises(ValueError, match="unsupported year: 1812"):
        main(["1812", "5", "a"])


@pytest.mark.parametrize("day", ["0", "32"])
def test_wrong_day(day):
    with pytest.raises(ValueError, match=f"want int in range 1-31, got {day}"):
        main(["2017", day, "a"])


def test_wrong_part():
    with pytest.raises(ValueError, match="want either `a` or `b`, got `c`"):
        main(["2017", "5", "c"])


def test_correct_solution_file_names():
    src = Path("src")
    for year_dir in src.glob("year*"):
        for file in year_dir.glob("*.py"):
            allowed = {"__init__.py", "intcode.py"}
            solution = re.match(r"day[0-3]\d[ab].py", file.name)
            valid = solution or file.name in allowed
            assert valid, f"unexpected file {file}"


def test_correct_test_file_names():
    tests = Path("tests") / "src"
    for year_dir in tests.glob("year*"):
        for file in year_dir.glob("*.py"):
            allowed = {"__init__.py", "test_intcode.py"}
            solution_test = re.match(r"test_day[0-3]\d[ab].py", file.name)
            valid = solution_test or file.name in allowed
            assert valid, f"unexpected file {file}"
