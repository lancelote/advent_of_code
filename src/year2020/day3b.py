"""2020 - Day 3 Part 2: Toboggan Trajectory."""
from src.year2020.day3a import count_trees
from src.year2020.day3a import process_data


def solve(task: str) -> int:
    """Count trees on the way."""
    plan = process_data(task)

    slope_1_1 = count_trees(plan, x_shift=1, y_shift=1)
    slope_3_1 = count_trees(plan, x_shift=3, y_shift=1)
    slope_5_1 = count_trees(plan, x_shift=5, y_shift=1)
    slope_7_1 = count_trees(plan, x_shift=7, y_shift=1)
    slope_1_2 = count_trees(plan, x_shift=1, y_shift=2)

    return slope_1_1 * slope_3_1 * slope_5_1 * slope_7_1 * slope_1_2
