"""2022 - Day 15 Part 2: Beacon Exclusion Zone."""
from src.year2022.day15a import Sensor


def skip_x(sensor: Sensor, x: int, y: int) -> int:
    to_sensor = abs(sensor.x - x) + abs(sensor.y - y)

    if sensor.distance >= to_sensor:
        if sensor.x < x:
            return sensor.distance - to_sensor + 1
        else:
            return sensor.x - x + sensor.distance - abs(y - sensor.y) + 1
    else:
        return 0


def solve(task: str, limit: int = 4_000_000) -> int:
    sensors = [Sensor.from_line(line) for line in task.splitlines()]
    sensors = sorted(sensors, key=lambda s: (s.x, s.y))

    for y in range(limit):
        x = 0

        for sensor in sensors:
            x += skip_x(sensor, x, y)

            if x > limit:
                break

        if x < limit:
            return x * 4_000_000 + y

    raise ValueError("solution not found")
