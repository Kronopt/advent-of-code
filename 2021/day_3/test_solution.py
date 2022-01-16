import unittest
from pathlib import Path
import solution


cwd = Path(__file__).parent


class TestSolutionPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_1.txt"), 198)

    def test2(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_2.txt"), 0)

    def test3(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_3.txt"), 220)

    def test4(self):
        self.assertEqual(solution.solution_part1(cwd / "testdata/input_4.txt"), 220)

    def test5(self):
        self.assertEqual(
            solution.solution_part1(cwd / "testdata/my_puzzle_input.txt"), 4001724
        )


class TestSolutionPart2(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_1.txt"), 230)

    def test2(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_2.txt"), 0)

    def test3(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_3.txt"), 400)

    def test4(self):
        self.assertEqual(solution.solution_part2(cwd / "testdata/input_4.txt"), 400)

    def test5(self):
        self.assertEqual(
            solution.solution_part2(cwd / "testdata/my_puzzle_input.txt"), 587895
        )


if __name__ == "__main__":
    unittest.main()
