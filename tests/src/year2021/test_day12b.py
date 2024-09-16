"""2021 - Day 12 Part 2: Passage Pathing."""

from textwrap import dedent

import pytest

from src.year2021.day12b import solve


@pytest.mark.parametrize(
    "task,routes",
    [
        (
            """
            start-A
            A-b
            b-c
            A-end
            """,
            4,
        ),
        (
            """
            start-A
            start-b
            A-c
            A-b
            b-d
            A-end
            b-end
            """,
            36,
        ),
        (
            """
            dc-end
            HN-start
            start-kj
            dc-start
            dc-HN
            LN-dc
            HN-end
            kj-sa
            kj-HN
            kj-dc
            """,
            103,
        ),
        (
            """
            fs-end
            he-DX
            fs-he
            start-DX
            pj-DX
            end-zg
            zg-sl
            zg-pj
            pj-he
            RW-he
            fs-DX
            pj-RW
            zg-RW
            start-pj
            he-WI
            zg-he
            pj-fs
            start-RW
            """,
            3509,
        ),
    ],
)
def test_solve(task, routes):
    task = dedent(task).strip()
    assert solve(task) == routes
