class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colored = [None] * n
        
        def notValid(i, color):
            colored[i] = color
            
            for nei in graph[i]:
                if colored[nei] != None:
                    if colored[nei] == color:
                        return True
                    continue
                else:
                    if notValid(nei, not color):
                        return True
            return False
        
        for i in range(n):
            if colored[i] == None and notValid(i, True):
                return False
        return True