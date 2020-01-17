"""2019 - Day 10 Part 2: Monitoring Station."""

from src.year2019.day10a import Chart


def solve(task: str) -> int:
    """Remove asteroids and get the last one coordinates."""
    chart = Chart.from_string(task)
    _, station_x, station_y = chart.optimal_station_position
    chart.set_base(station_x, station_y)
    x, y = chart.remove_till(200)
    return x * 100 + y
