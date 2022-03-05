class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))

        
        # calculate costs from src
        costs = collections.defaultdict(lambda: float('inf'))
        costs[src] = _k = 0
        stack = set([src])
        
        while stack:
            next_stack = set()
            
            tmp = costs.copy()
            for x in stack:
                for child, price in graph[x]:
                    costs[child] = min(costs[child], tmp[x] + price)
                    next_stack.add(child)
            
            stack = next_stack
            _k += 1
            if _k > k:
                break
        
        return costs[dst] if costs[dst] != float('inf') else -1
