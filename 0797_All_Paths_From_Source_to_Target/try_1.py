class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        
        
        memo = set()
        def dfs(node, path):
            nonlocal ans
            
            if node == n-1:
                ans.append(path[:])
                return
            
            for child in graph[node]:
                if child not in memo:
                    memo.add(child)
                    dfs(child, path + [child])
                    memo.remove(child)
        
        dfs(0, [0])
        return ans