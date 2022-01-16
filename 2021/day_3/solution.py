import copy
from collections import OrderedDict
from pathlib import Path
from typing import Callable


def solution_part1(report_file_path: Path) -> int:
    total_numbers = 0
    sum_per_position = OrderedDict()
    with report_file_path.open() as report_reader:
        for binary_number in report_reader:
            binary_number = binary_number.rstrip()
            current_position = 0
            for bit in binary_number:
                if sum_per_position.get(current_position) is None:
                    sum_per_position[current_position] = 0

                sum_per_position[current_position] += int(bit)
                current_position += 1
            total_numbers += 1

    gamma = ""
    epsilon = ""
    for value in sum_per_position.values():
        if value > total_numbers // 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def solution_part2(report_file_path: Path) -> int:
    numbers = []
    with report_file_path.open() as report_reader:
        for binary_number in report_reader:
            numbers.append(binary_number.rstrip())

    oxygen = filter_number(numbers, "__eq__")
    co2 = filter_number(numbers, "__ne__")

    return int(oxygen, 2) * int(co2, 2)


def filter_number(numbers: list[str], comparison_function: str) -> str:
    """
    recursively filters using the exercise logic.
    comparison_function should either be '__eq__' or '__ne__', for == or != comparisons respectively
    """
    filtered_numbers = copy.deepcopy(numbers)
    safe_number = "0"
    bit = 0
    while len(filtered_numbers) > 1:
        safe_number = filtered_numbers[0]

        if bit > len(filtered_numbers[0]) - 1:
            break

        most_common = most_common_bit_for_position(filtered_numbers, bit)
        filtered_numbers = list(
            filter(
                lambda x: getattr(int(x[bit]), comparison_function)(most_common),
                filtered_numbers,
            )
        )
        bit += 1

    if len(filtered_numbers) == 0:
        filtered_numbers.append(safe_number)

    return filtered_numbers[0]


def most_common_bit_for_position(numbers: list[str], position: int) -> int:
    """calculates the most common bit for a given position (if equal, returns 1)"""
    sum_for_position = 0
    for number in numbers:
        sum_for_position += int(number[position])

    return int(sum_for_position >= len(numbers) / 2)
