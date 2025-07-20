import unittest

from src.backtracking.eight_queens import eight_queens


class TestEightQueens(unittest.TestCase):
    def test_solution_exists(self):
        self.assertTrue(eight_queens())


if __name__ == "__main__":
    unittest.main()
