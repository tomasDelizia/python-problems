import unittest

from src.hash.top_k_frequent import top_k_frequent


class TestTopKFrequent(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(top_k_frequent([1], 1), [])

    def test_multiple_elements(self):
        self.assertEqual(
            top_k_frequent([1, 1, 1, 2, 2, 3, 3, 3, 100], 2), [1, 3]
        )


if __name__ == "__main__":
    unittest.main()
