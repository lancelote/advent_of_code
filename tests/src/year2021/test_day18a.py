"""2021 - Day 18 Part 1: Snailfish."""
import pytest

from src.year2021.day18a import tokenize
from src.year2021.day18a import LinkedList


@pytest.mark.parametrize(
    "line,expected_tokens",
    [("[1,2]", ["[", "1", "2"]), ("[[1,22],3]", ["[", "[", "1", "22", "3"])],
)
def test_tokenize(line, expected_tokens):
    assert list(tokenize(line)) == expected_tokens


@pytest.mark.parametrize(
    "line,expected_magnitude",
    [
        ("[9,1]", 29),
        ("[1,9]", 21),
        ("[[9,1],[1,9]]", 129),
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ],
)
def test_magnitude(line, expected_magnitude):
    assert LinkedList.from_line(line).magnitude == expected_magnitude


@pytest.mark.parametrize(
    "line",
    [
        "[9,1]",
        "[[9,1],[1,9]]",
        "[[1,2],[[3,4],5]]",
    ],
)
def test_str(line):
    assert str(LinkedList.from_line(line)) == line


def test_add():
    a = LinkedList.from_line("[1,2]")
    b = LinkedList.from_line("[[3,4],5]")
    c = a + b
    assert str(c) == "[[1,2],[[3,4],5]]"


@pytest.mark.parametrize(
    "from_line,to_line",
    [
        (
            "[10,1]",
            "[[5,5],1]",
        ),
        (
            "[[[[0,7],4],[15,[0,13]]],[1,1]]",
            "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
        ),
        (
            "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
            "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]",
        ),
    ],
)
def test_split(from_line, to_line):
    num = LinkedList.from_line(from_line)
    num.split()
    assert str(num) == to_line
