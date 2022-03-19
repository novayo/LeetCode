class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # build graph
        graph = collections.defaultdict(list)
        for a, b in paths:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        # mark nodes as much as possible
        def recr(node):
            nonlocal ans
            neighbors = graph[node]
            
            for i in range(4, 0, -1):
                if any([ans[nei] == i for nei in neighbors]):
                    continue
                
                ans[node] = i
                for nei in neighbors:
                    if ans[nei] == -1:
                        recr(nei)
        
        
        ans = [-1] * n
        for i in range(n):
            if ans[i] == -1:
                recr(i)
        return ans
        