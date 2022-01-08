import math
from collections.abc import Iterator
from pathlib import Path


def solution_part1(report_file_path: Path) -> int:
    total = 0
    previous = math.inf
    with report_file_path.open() as report_reader:
        for number in report_reader:
            number = float(number)
            if number > previous:
                total += 1
            previous = number

    return total


def solution_part2(report_file_path: Path) -> int:
    total = 0
    previous = math.inf

    with report_file_path.open() as report_reader:
        numbers = report_reader.readlines()

    for i in range(len(numbers) - 2):  # 3 element sliding window
        sum_sliding_window = sum(
            (float(numbers[i]), float(numbers[i + 1]), float(numbers[i + 2]))
        )

        if sum_sliding_window > previous:
            total += 1

        previous = sum_sliding_window

    return total
