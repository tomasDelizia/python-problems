import unittest

from context import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        quick_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [5]
        quick_sort(arr)
        self.assertEqual(arr, [5])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 2, 5]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
