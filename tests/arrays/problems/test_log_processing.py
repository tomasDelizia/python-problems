import unittest

from src.arrays.problems.log_processing import log_processing


class TestLogProcessing(unittest.TestCase):
    def test_log_processing(self):
        log_processing("logs.txt")


if __name__ == "__main__":
    unittest.main()
