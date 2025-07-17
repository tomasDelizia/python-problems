import unittest

from src.matrix.problems.is_valid_time_series import is_valid_time_series


class TestIsValidTimeSeries(unittest.TestCase):
    def test_valid_time_series(self):
        grid = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 1, 0]]
        self.assertTrue(is_valid_time_series(grid))

    def test_invalid_time_series(self):
        grid = [[1, 0, 0, 0, 1], [1, 0, 1, 0, 0]]
        self.assertFalse(is_valid_time_series(grid))


if __name__ == "__main__":
    unittest.main()
