import unittest

from src.arrays.shell_sort import shell_sort


class TestShellSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        shell_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [5]
        shell_sort(arr)
        self.assertEqual(arr, [5])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 2, 5]
        shell_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
