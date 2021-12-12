import re
from pathlib import Path

import pytest
from click.testing import CliRunner

from main import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_solve(runner, mock_get_data):
    data = "411 players; last marble is worth 71058 points"
    mock_get_data.return_value = data

    result = runner.invoke(cli, ["solve", "2018", "9", "a"])

    assert result.exit_code == 0
    assert result.output == "Answer: 424639\n"


def test_wrong_year(runner):
    result = runner.invoke(cli, ["solve", "1812", "5", "a"])

    assert result.exit_code == 2
    assert "Invalid value for 'YEAR'" in result.output


@pytest.mark.parametrize("day", ["0", "32"])
def test_wrong_day(runner, day):
    result = runner.invoke(cli, ["solve", "2017", day, "a"])

    assert result.exit_code == 2
    assert "Invalid value for 'DAY'" in result.output


def test_wrong_part(runner):
    result = runner.invoke(cli, ["solve", "2017", "5", "c"])

    assert result.exit_code == 2
    assert "Invalid value for 'PART'" in result.output


def test_correct_solution_file_names():
    src = Path("src")
    for year_dir in src.glob("year*"):
        for file in year_dir.glob("*.py"):
            allowed = {"__init__.py", "intcode.py"}
            solution = re.match(r"day[0-3][0-9][ab].py", file.name)
            valid = solution or file.name in allowed
            assert solution or file.name in allowed, f"unexpected file {file}"


def test_correct_test_file_names():
    tests = Path("tests") / "src"
    for year_dir in tests.glob("year*"):
        for file in year_dir.glob("*.py"):
            allowed = {"__init__.py", "test_intcode.py"}
            solution_test = re.match(r"test_day[0-3][0-9][ab].py", file.name)
            valid = solution_test or file.name in allowed
            assert valid, f"unexpected file {file}"
