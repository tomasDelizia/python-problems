import unittest

from src.arrays.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        sorted = merge_sort(arr)
        self.assertEqual(sorted, [])

    def test_single_element(self):
        arr = [5]
        sorted = merge_sort(arr)
        self.assertEqual(sorted, [5])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        sorted = merge_sort(arr)
        self.assertEqual(sorted, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        sorted = merge_sort(arr)
        self.assertEqual(sorted, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 2, 5]
        sorted = merge_sort(arr)
        self.assertEqual(sorted, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
