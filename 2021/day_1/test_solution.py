import unittest
import solution

input1 = """199
200
208
210
200
207
240
269
260
263"""

input2 = """-10
-5
-2
0
2
5
10"""

input3 = """0
0
0
0
0
0
0
0
0
0"""

input4 = """-1.5
0
1.5
99999999
100
99
98
97
96
95"""


class TestSolutionPart1(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part1(input1), 7)

    def test2(self):
        self.assertEqual(solution.solution_part1(input2), 6)

    def test3(self):
        self.assertEqual(solution.solution_part1(input3), 0)

    def test4(self):
        self.assertEqual(solution.solution_part1(input4), 3)


class TestSolutionPart2(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.solution_part2(input1), 5)

    def test2(self):
        self.assertEqual(solution.solution_part2(input2), 4)

    def test3(self):
        self.assertEqual(solution.solution_part2(input3), 0)

    def test4(self):
        self.assertEqual(solution.solution_part2(input4), 3)


if __name__ == "__main__":
    unittest.main()
