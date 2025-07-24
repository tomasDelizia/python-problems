import heapq
import math
from collections import defaultdict


# Bellman-Ford algorithm
# TODO: implement
def cheapest_flight_within_k_stops(
    n: int, flights: list[list[int]], src: int, dest: int, k: int
) -> float:
    edges = defaultdict(list)
    for u, v, w in flights:
        edges[u].append((v, w))
    return 0


def cheapest_flight_within_k_stops_bad(
    n: int, flights: list[list[int]], src: int, dest: int, k: int
) -> float:
    edges = defaultdict(list)
    for u, v, w in flights:
        edges[u].append((v, w))
    visited = set()
    # Min heap: weight, node, stops
    heap = [(0, src, -1)]
    cheapest = math.inf
    while heap:
        weight, node, stops = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == dest:
            cheapest = min(cheapest, weight)
        for neighbor, w in edges[node]:
            if neighbor in visited or stops + 1 > k:
                continue
            heapq.heappush(heap, (weight + w, neighbor, stops + 1))

    return cheapest if len(visited) == n else -1
