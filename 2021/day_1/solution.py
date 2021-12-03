import math
from collections.abc import Iterator


def solution_part1(report: str) -> int:
    total = 0
    previous = math.inf
    for number in report.split("\n"):
        number = float(number)
        if number > previous:
            total += 1
        previous = number

    return total


def solution_part2(report: str) -> int:
    total = 0
    previous = math.inf
    numbers = report.split("\n")
    for i in range(len(numbers) - 2):  # 3 element sliding window
        sum_sliding_window = sum(
            (float(numbers[i]), float(numbers[i + 1]), float(numbers[i + 2]))
        )

        if sum_sliding_window > previous:
            total += 1

        previous = sum_sliding_window

    return total
