from pathlib import Path


def solution_part1(commands_file_path: Path) -> int:
    horizontal = 0
    depth = 0
    with commands_file_path.open() as commands_reader:
        for line in commands_reader:
            command, value = line.split(" ")
            value = int(value)

            if command == "forward":
                horizontal += value
            elif command == "down":
                depth += value
            elif command == "up":
                depth -= value

    return horizontal * depth


def solution_part2(commands_file_path: Path) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    with commands_file_path.open() as commands_reader:
        for line in commands_reader:
            command, value = line.split(" ")
            value = int(value)

            if command == "forward":
                horizontal += value
                depth += aim * value
            elif command == "down":
                aim += value
            elif command == "up":
                aim -= value

    return horizontal * depth
