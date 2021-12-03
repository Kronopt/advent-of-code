import unittest
import solution

input1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

input2 = """forward 0
forward 0
forward 0
forward 0
forward 0
forward 0
forward 0
forward 0
forward 0
forward 0
forward 0
"""

input3 = """forward -1"""

input4 = """forward -1
down 1"""


class TestSolutionPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part1(input1), 150)

    def test2(self):
        self.assertEqual(solution.solution_part1(input2), 0)

    def test3(self):
        self.assertEqual(solution.solution_part1(input3), 0)

    def test4(self):
        self.assertEqual(solution.solution_part1(input4), -1)


class TestSolutionPart2(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part2(input1), 900)

    def test2(self):
        self.assertEqual(solution.solution_part2(input2), 0)

    def test3(self):
        self.assertEqual(solution.solution_part2(input3), 0)

    def test4(self):
        self.assertEqual(solution.solution_part2(input4), 0)


if __name__ == "__main__":
    unittest.main()
