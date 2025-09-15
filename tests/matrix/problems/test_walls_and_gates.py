import unittest

from src.matrix.problems.walls_and_gates import walls_and_gates


class TestWallsAndGates(unittest.TestCase):
    def test_empty_grid(self):
        self.assertEqual(walls_and_gates([]), [])

    def test_single_gate(self):
        grid = [[0]]
        self.assertEqual(walls_and_gates(grid), [[0]])

    def test_multiple_islands(self):
        grid = [
            [float("inf"), -1, 0, float("inf")],
            [float("inf"), float("inf"), float("inf"), -1],
            [float("inf"), -1, float("inf"), -1],
            [0, -1, float("inf"), float("inf")],
        ]
        result = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        self.assertEqual(walls_and_gates(grid), result)


if __name__ == "__main__":
    unittest.main()
