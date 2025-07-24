import heapq
import math
from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> float:
    # Build adjacency list
    edges = defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))

    # Min-heap: (weight, node)
    heap = [(0, k)]
    visited = set()
    max_time = 0

    while heap:
        weight, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        max_time = max(max_time, weight)
        # BFS: Add the non visited neighbors of the current node to the heap.
        for neighbor, w in edges[node]:
            if neighbor not in visited:
                weight_to_neighbor = weight + w
                heapq.heappush(heap, (weight_to_neighbor, neighbor))

    return max_time if len(visited) == n else -1


def network_delay_time_complicated(
    times: list[list[int]], n: int, k: int
) -> float:
    shortest_paths = defaultdict(lambda: (math.inf, None))
    heap = []
    visited = set()
    max_time = -1

    # Add the shortest path time to the start node, with predecessor None.
    shortest_paths[k] = (0, None)

    # Add start node and time to the heap
    heapq.heappush(heap, (k, 0))

    while heap:
        curr_node, _ = heapq.heappop(heap)
        if curr_node in visited:
            continue
        visited.add(curr_node)

        current_time, _ = shortest_paths[curr_node]
        direct_edges = [
            [source, dest, time]
            for source, dest, time in times
            if source == curr_node
        ]
        for _, dest, time in direct_edges:
            if dest in visited:
                continue
            new_time = current_time + time
            prev_time, _ = shortest_paths[dest]
            if new_time < prev_time:
                shortest_paths[dest] = (new_time, curr_node)
                heapq.heappush(heap, (dest, new_time))
                max_time = max(max_time, new_time)

    if len(shortest_paths) != n:
        return -1

    return max_time
