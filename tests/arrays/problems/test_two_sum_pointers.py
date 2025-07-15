import unittest

from .context import two_sum_pointers


class TestTwoSumPointers(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(two_sum_pointers([], 5), [])

    def test_single_element_not_found(self):
        self.assertEqual(two_sum_pointers([3], 5), [])

    def test_two_elements_found(self):
        self.assertEqual(two_sum_pointers([1, 4], 5), [0, 1])

    def test_two_elements_not_found(self):
        self.assertEqual(two_sum_pointers([1, 2], 5), [])

    def test_multiple_elements_found(self):
        self.assertEqual(two_sum_pointers([1, 2, 3, 4, 5], 6), [0, 4])


if __name__ == "__main__":
    unittest.main()
