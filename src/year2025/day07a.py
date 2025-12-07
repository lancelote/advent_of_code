"""2025 - Day 7 Part 1: Laboratories"""


def solve(task: str) -> int:
    manifold = task.splitlines()

    n_cols = len(manifold[0])

    splits = 0
    beams = {manifold[0].index("S")}

    for row in manifold:
        new_beams: set[int] = set()

        for beam in beams:
            if row[beam] == "^":
                splits += 1
                left = beam - 1
                right = beam + 1

                if 0 <= left < n_cols:
                    new_beams.add(left)

                if 0 <= right < n_cols:
                    new_beams.add(right)
            else:
                new_beams.add(beam)

        beams = new_beams

    return splits
