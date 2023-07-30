from collections import defaultdict
from heapq import heappush, heappop

def dijkstra_all(paths):
    # 建立graph
    graph = defaultdict(list)
    for a, b, dist in paths:
        graph[a].append((b, dist))
        graph[b].append((a, dist))
    
    # 初始化起始值
    table = {}
    done_set = set()
    visited_heap = []

    for v in graph.keys():
        table[v] = [float('inf'), -1]

    heappush(visited_heap, (0, 0)) # 距離, 點
    table[0] = [0, -1] # 距離, 父

    # 做dijkstra
    while visited_heap:
        # 挑已經拜訪且還沒完成的點的最小值出來
        cur_dist, v = heappop(visited_heap)

        if v in done_set:
            continue

        # 更新鄰居
        for neighbor, dist in graph[v]:
            # 如果已經完成了就跳過
            if neighbor in done_set:
                continue
            if cur_dist + dist < table[neighbor][0]:
                table[neighbor][0] = cur_dist + dist
                table[neighbor][1] = v
                heappush(visited_heap, (table[neighbor][0], neighbor)) # 距離, 點
        
        done_set.add(v)
    
    return table

paths = [[0,1,2], [0,2,1], [1,2,3], [1,3,5], [2,3,2], [3,4,3], [3,5,4]]
table = dijkstra_all(paths)
for key, value in table.items():
    print(key, value)

# 要找0 -> 4怎麼走？
path = []
v = 4
while v != -1:
    path.append(v)
    v = table[v][1]

print(path[::-1])
