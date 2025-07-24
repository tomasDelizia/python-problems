import unittest

from src.graph.network_delay_time import network_delay_time


class TestNetworkDelayTime(unittest.TestCase):
    def test_valid_nodes(self):
        self.assertEqual(
            network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2
        )

    def test_valid_nodes_one_edge(self):
        self.assertEqual(network_delay_time([[1, 2, 1]], 2, 1), 1)

    def test_invalid_nodes(self):
        self.assertEqual(network_delay_time([[1, 2, 1]], 2, 2), -1)


if __name__ == "__main__":
    unittest.main()
