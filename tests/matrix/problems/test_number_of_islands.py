import unittest

from src.matrix.problems.number_of_islands import number_of_islands


class TestNumberOfIslands(unittest.TestCase):
    def test_empty_grid(self):
        self.assertEqual(number_of_islands([]), 0)

    def test_single_island(self):
        grid = [["1"]]
        self.assertEqual(number_of_islands(grid), 1)

    def test_multiple_islands(self):
        grid = [
            ["1", "1", "0", "0"],
            ["1", "0", "0", "1"],
            ["0", "0", "1", "1"],
            ["0", "1", "1", "0"],
        ]
        self.assertEqual(number_of_islands(grid), 2)


if __name__ == "__main__":
    unittest.main()
