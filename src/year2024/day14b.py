"""2024 - Day 14 Part 2: Restroom Redoubt"""

from dataclasses import dataclass

from src.year2024.day14a import Robot


@dataclass
class Field:
    width: int
    height: int
    robots: list[Robot]

    def make_step(self) -> None:
        for robot in self.robots:
            robot.x = (robot.x + robot.dx) % self.width
            robot.y = (robot.y + robot.dy) % self.height

    def __str__(self) -> str:
        data = [[" " for _ in range(self.width)] for _ in range(self.height)]
        for robot in self.robots:
            data[robot.y][robot.x] = "#"
        return "\n".join("".join(line) for line in data)


def solve(task: str, width: int = 101, height: int = 103) -> int:
    robots = [Robot.from_line(x) for x in task.split("\n")]
    field = Field(width, height, robots)

    for i in range(1, 10_000):
        field.make_step()
        print("second", i)
        print(field)

    return -1
