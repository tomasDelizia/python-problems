import unittest

from src.graph.cheapest_flight_within_k_stops import (
    cheapest_flight_within_k_stops,
)


class TestCheapestFlightWithinKStops(unittest.TestCase):
    def test_valid_four_nodes(self):
        self.assertEqual(
            cheapest_flight_within_k_stops(
                4,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                    [2, 0, 100],
                    [1, 3, 600],
                    [2, 3, 200],
                ],
                0,
                3,
                1,
            ),
            700,
        )

    def test_valid_three_nodes_with_stops(self):
        self.assertEqual(
            cheapest_flight_within_k_stops(
                3,
                [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                0,
                2,
                1,
            ),
            200,
        )

    def test_valid_three_nodes_no_stops(self):
        self.assertEqual(
            cheapest_flight_within_k_stops(
                3,
                [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                0,
                2,
                0,
            ),
            500,
        )


if __name__ == "__main__":
    unittest.main()
