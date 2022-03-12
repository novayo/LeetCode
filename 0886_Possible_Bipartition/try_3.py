class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        
        colored = collections.defaultdict(bool)
        def dfs(node):
            for child in graph[node]:
                if child not in colored:
                    colored[child] = not colored[node]
                    if not dfs(child):
                        return False
                elif colored[child] == colored[node]:
                    return False
            return True
        
        for i in range(1, n+1):
            if i not in colored:
                colored[i] = False
                if not dfs(i):
                    return False
        return True
