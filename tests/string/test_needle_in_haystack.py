import unittest

from src.string.needle_in_haystack import needle_in_haystack


class TestNeedleInHaystack(unittest.TestCase):
    def test_empty_needle(self):
        self.assertEqual(needle_in_haystack("haystack", ""), 0)

    def test_needle_not_found(self):
        self.assertEqual(needle_in_haystack("haystack", "needle"), -1)

    def test_needle_at_start(self):
        self.assertEqual(needle_in_haystack("haystack", "hay"), 0)

    def test_needle_at_end(self):
        self.assertEqual(needle_in_haystack("haystack", "stack"), 3)

    def test_needle_in_middle(self):
        self.assertEqual(needle_in_haystack("haystack", "yst"), 2)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(needle_in_haystack("short", "longer"), -1)


if __name__ == "__main__":
    unittest.main()
