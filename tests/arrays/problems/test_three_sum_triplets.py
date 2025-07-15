import unittest

from src.arrays.problems.three_sum_triplets import three_sum_triplets


class TestThreeSumPointers(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual(
            three_sum_triplets([-1, 0, 1, 2, -1, -4], 0),
            [(-1, -1, 2), (-1, 0, 1)],
        )


if __name__ == "__main__":
    unittest.main()
