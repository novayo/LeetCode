class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for r in route:
                graph[r].add(i)
        
        if source not in graph or target not in graph:
            return -1
        
        cache = set()
        queue = collections.deque()
        
        cache.add(source)
        queue.append((source, 0))
        while queue:
            bus, num = queue.popleft()
            
            if bus == target:
                return num
            
            for i in graph[bus]:
                for next_bus in routes[i]:
                    if next_bus in cache:
                        continue
                    cache.add(next_bus)
                    queue.append((next_bus, num+1))
        return -1
            
