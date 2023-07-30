from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(paths, start_v, end_v):
    # 建立graph
    graph = defaultdict(list)
    for a, b, dist in paths:
        graph[a].append((b, dist))
        graph[b].append((a, dist))

    visited_heap = [(0, start_v)]
    done_set = set()
    path = []
    while visited_heap:
        cur_dist, v = heappop(visited_heap)
        if v in done_set:
            continue
        path.append(v)
        done_set.add(v)

        if v == end_v:
            return cur_dist

        for neighbor, dist in graph[v]:
            if neighbor in done_set:
                continue
            heappush(visited_heap, (cur_dist + dist, neighbor))
    
    return path

paths = [[0,1,2], [0,2,1], [1,2,3], [1,3,5], [2,3,2], [3,4,3], [3,5,4]]
shortest_dist = dijkstra(paths, 0, 4)
print(shortest_dist)