import unittest

from src.arrays.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([3], 5), -1)

    def test_multiple_elements_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_multiple_elements_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)


if __name__ == "__main__":
    unittest.main()
