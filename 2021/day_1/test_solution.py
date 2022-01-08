import unittest
from pathlib import Path
import solution


cwd = Path(__file__).parent


class TestSolutionPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_1.txt"), 7)

    def test2(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_2.txt"), 6)

    def test3(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_3.txt"), 0)

    def test4(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_4.txt"), 3)

    def test5(self):
        self.assertEqual(
            solution.solution_part1(cwd / "testdata/my_puzzle_input.txt"), 1624
        )


class TestSolutionPart2(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_1.txt"), 5)

    def test2(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_2.txt"), 4)

    def test3(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_3.txt"), 0)

    def test4(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_4.txt"), 3)

    def test5(self):
        self.assertEqual(
            solution.solution_part2(cwd / "testdata/my_puzzle_input.txt"), 1653
        )


if __name__ == "__main__":
    unittest.main()
