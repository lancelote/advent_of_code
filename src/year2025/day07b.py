"""2025 - Day 7 Part 2: Laboratories"""

from collections import defaultdict


def solve(task: str) -> int:
    manifold = task.splitlines()

    n_cols = len(manifold[0])

    start_beam = manifold[0].index("S")
    beams = {start_beam}
    timelines: dict[int, int] = defaultdict(int)
    timelines[start_beam] = 1

    for row in manifold:
        new_beams: set[int] = set()
        new_timelines: dict[int, int] = defaultdict(int)

        for beam in beams:
            timeline = timelines[beam]

            if row[beam] == "^":
                left = beam - 1
                right = beam + 1

                if 0 <= left < n_cols:
                    new_beams.add(left)
                    new_timelines[left] += timeline

                if 0 <= right < n_cols:
                    new_beams.add(right)
                    new_timelines[right] += timeline
            else:
                new_beams.add(beam)
                new_timelines[beam] += timeline

        beams = new_beams
        timelines = new_timelines

    return sum(timelines.values())
