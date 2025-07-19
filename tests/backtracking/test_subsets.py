import unittest

from src.backtracking.subsets import subsets


class TestSubsets(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(subsets([]), [[]])

    def test_single_element(self):
        self.assertEqual(subsets([0]), [[], [0]])

    def test_multiple_elements(self):
        self.assertEqual(
            subsets([1, 2, 3]),
            [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],
        )


if __name__ == "__main__":
    unittest.main()
