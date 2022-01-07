"""2021 - Day 18 Part 1: Snailfish."""
import pytest

from src.year2021.day18a import Node
from src.year2021.day18a import explode
from src.year2021.day18a import split


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
    assert Node.from_line(line).magnitude == expected_magnitude


@pytest.mark.parametrize(
    "line",
    [
        "[9,1]",
        "[[9,1],[1,9]]",
        "[[1,2],[[3,4],5]]",
    ],
)
def test_str(line):
    assert str(Node.from_line(line)) == line


def test_add():
    a = Node.from_line("[1,2]")
    b = Node.from_line("[[3,4],5]")
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
    num = Node.from_line(from_line)
    assert str(split(num)) == to_line


@pytest.mark.parametrize(
    "from_line,to_line",
    [
        (
            "[[[[[9,8],1],2],3],4]",
            "[[[[0,9],2],3],4]",
        ),
        (
            "[7,[6,[5,[4,[3,2]]]]]",
            "[7,[6,[5,[7,0]]]]",
        ),
        (
            "[[6,[5,[4,[3,2]]]],1]",
            "[[6,[5,[7,0]]],3]",
        ),
        (
            "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
            "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
        ),
        (
            "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
            "[[3,[2,[8,0]]],[9,[5,[7,0]]]]",
        )
    ]
)
def test_explode(from_line, to_line):
    num = Node.from_line(from_line)
    assert str(explode(num)) == to_line
