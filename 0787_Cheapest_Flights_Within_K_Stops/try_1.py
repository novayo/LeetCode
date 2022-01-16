class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for a, b, cost in flights:
            graph[a].append((cost, b))
        
        # bellman ford
        table = [float('inf')] * n
        table[src] = 0
        
        for _ in range(k+1):
            old_table = table.copy()
            for i in range(n):
                if old_table[i] == float('inf'):
                    continue
                
                for cost, nei in graph.get(i, []):
                    table[nei] = min(table[nei], old_table[i]+cost)
        
        return table[dst] if table[dst] != float('inf') else -1