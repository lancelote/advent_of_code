"""2017 - Day 12 Part 1: Digital Plumber tests."""

from src.year2017.day12a import process_data, solve


def test_process_data():
    data = "0 <-> 2\n586 <-> 640, 688, 1258, 1331"
    expected = [["0", "2"], ["586", "640", "688", "1258", "1331"]]
    assert process_data(data) == expected


def test_solve():
    data = (
        "0 <-> 2\n"
        "1 <-> 1\n"
        "2 <-> 0, 3, 4\n"
        "3 <-> 2, 4\n"
        "4 <-> 2, 3, 6\n"
        "5 <-> 6\n"
        "6 <-> 4, 5\n"
    )
    assert solve(data) == 6
