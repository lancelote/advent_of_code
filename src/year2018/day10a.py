"""2018 - Day 10 Part 1: The Stars Align.

It's no use; your navigation system simply isn't capable of providing walking
directions in the arctic circle, and certainly not in 1018.

The Elves suggest an alternative. In times like these, North Pole rescue
operations will arrange points of light in the sky to guide missing Elves back
to base. Unfortunately, the message is easy to miss: the points move slowly
enough that it takes hours to align them, but have so much momentum that they
only stay aligned for a second. If you blink at the wrong time, it might be
hours before another message appears.

You can see these points of light floating in the distance, and record their
position in the sky and their velocity, the relative change in position per
second (your puzzle input). The coordinates are all given from your
perspective; given enough time, those positions and velocities will move the
points into a cohesive message!

Rather than wait, you decide to fast-forward the process and calculate what
the points will eventually spell.

For example, suppose you note the following points:

    position=< 9,  1> velocity=< 0,  2>
    position=< 7,  0> velocity=<-1,  0>
    position=< 3, -2> velocity=<-1,  1>
    position=< 6, 10> velocity=<-2, -1>
    position=< 2, -4> velocity=< 2,  2>
    position=<-6, 10> velocity=< 2, -2>
    position=< 1,  8> velocity=< 1, -1>
    position=< 1,  7> velocity=< 1,  0>
    position=<-3, 11> velocity=< 1, -2>
    position=< 7,  6> velocity=<-1, -1>
    position=<-2,  3> velocity=< 1,  0>
    position=<-4,  3> velocity=< 2,  0>
    position=<10, -3> velocity=<-1,  1>
    position=< 5, 11> velocity=< 1, -2>
    position=< 4,  7> velocity=< 0, -1>
    position=< 8, -2> velocity=< 0,  1>
    position=<15,  0> velocity=<-2,  0>
    position=< 1,  6> velocity=< 1,  0>
    position=< 8,  9> velocity=< 0, -1>
    position=< 3,  3> velocity=<-1,  1>
    position=< 0,  5> velocity=< 0, -1>
    position=<-2,  2> velocity=< 2,  0>
    position=< 5, -2> velocity=< 1,  2>
    position=< 1,  4> velocity=< 2,  1>
    position=<-2,  7> velocity=< 2, -2>
    position=< 3,  6> velocity=<-1, -1>
    position=< 5,  0> velocity=< 1,  0>
    position=<-6,  0> velocity=< 2,  0>
    position=< 5,  9> velocity=< 1, -2>
    position=<14,  7> velocity=<-2,  0>
    position=<-3,  6> velocity=< 2, -1>

Each line represents one point. Positions are given as <X, Y> pairs: X
represents how far left (negative) or right (positive) the point appears, while
Y represents how far up (negative) or down (positive) the point appears.

At 0 seconds, each point has the position given. Each second, each point's
velocity is added to its position. So, a point with velocity <1, -2> is moving
to the right, but is moving upward twice as quickly. If this point's initial
position were <3, 9>, after 3 seconds, its position would become <6, 3>.

Over time, the points listed above would move like this:

Initially:

    ........#.............
    ................#.....
    .........#.#..#.......
    ......................
    #..........#.#.......#
    ...............#......
    ....#.................
    ..#.#....#............
    .......#..............
    ......#...............
    ...#...#.#...#........
    ....#..#..#.........#.
    .......#..............
    ...........#..#.......
    #...........#.........
    ...#.......#..........

After 1 second:

    ......................
    ......................
    ..........#....#......
    ........#.....#.......
    ..#.........#......#..
    ......................
    ......#...............
    ....##.........#......
    ......#.#.............
    .....##.##..#.........
    ........#.#...........
    ........#...#.....#...
    ..#...........#.......
    ....#.....#.#.........
    ......................
    ......................

After 2 seconds:

    ......................
    ......................
    ......................
    ..............#.......
    ....#..#...####..#....
    ......................
    ........#....#........
    ......#.#.............
    .......#...#..........
    .......#..#..#.#......
    ....#....#.#..........
    .....#...#...##.#.....
    ........#.............
    ......................
    ......................
    ......................

After 3 seconds:

    ......................
    ......................
    ......................
    ......................
    ......#...#..###......
    ......#...#...#.......
    ......#...#...#.......
    ......#####...#.......
    ......#...#...#.......
    ......#...#...#.......
    ......#...#...#.......
    ......#...#..###......
    ......................
    ......................
    ......................
    ......................

After 4 seconds:

    ......................
    ......................
    ......................
    ............#.........
    ........##...#.#......
    ......#.....#..#......
    .....#..##.##.#.......
    .......##.#....#......
    ...........#....#.....
    ..............#.......
    ....#......#...#......
    .....#.....##.........
    ...............#......
    ...............#......
    ......................
    ......................

After 3 seconds, the message appeared briefly: HI. Of course, your message will
be much longer and will take many more seconds to appear.

What message will eventually appear in the sky?
"""

import re
from typing import List
from dataclasses import dataclass


@dataclass
class Point:
    """Rescue point on the sky."""

    x: int
    y: int
    dx: int
    dy: int

    @classmethod
    def from_line(cls, line: str) -> 'Point':
        """Get Point from the line."""
        return cls(*map(int, re.findall(r'[\d-]+', line)))

    @classmethod
    def parse_task(cls, task: str) -> List['Point']:
        """Parse the given task returning a list of rescue points."""
        return [cls.from_line(line) for line in task.strip().split('\n')]

    def move(self):
        """Move a star by one tick."""
        self.x += self.dx
        self.y += self.dy

    def back(self):
        """Go back in time by one tick."""
        self.x -= self.dx
        self.y -= self.dy


@dataclass
class Sky:
    """Sky with given rescue points."""

    points: List[Point]

    def move(self):
        """Move sky by one tick forward in time."""
        for point in self.points:
            point.move()

    def back(self):
        """Move sky by one tick backwards in time."""
        for point in self.points:
            point.back()

    def bounds(self):
        """Get extremum points."""
        min_x = min(point.x for point in self.points)
        max_x = max(point.x for point in self.points)
        min_y = min(point.y for point in self.points)
        max_y = max(point.y for point in self.points)
        return min_x, max_x, min_y, max_y

    def move_till_min_area(self):
        """Move in time till rescue points have a minimum area in the sky."""
        current_area = self.area
        self.move()

        while self.area < current_area:
            current_area = self.area
            self.move()

        self.back()

    @property
    def area(self):
        """Calculate the rescue point area in the sky."""
        min_x, max_x, min_y, max_y = self.bounds()
        return (max_x - min_x + 1) * (max_y - min_y + 1)

    def __str__(self):
        min_x, max_x, min_y, max_y = self.bounds()

        sky = []
        for _ in range(min_y, max_y + 1):
            line = []
            for _ in range(min_x, max_x + 1):
                line.append('.')
            sky.append(line)

        for point in self.points:
            sky[point.y - min_y][point.x - min_x] = '#'

        return '\n'.join(''.join(line) for line in sky)


def solve(task: str) -> None:
    """Find a message in the sky."""
    points = Point.parse_task(task)
    sky = Sky(points)
    sky.move_till_min_area()
    print(sky)
