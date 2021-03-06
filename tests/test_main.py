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
