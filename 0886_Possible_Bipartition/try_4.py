class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # O(V+E) time / O(V+E) space
        
        # build graph
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        memo = {}
        def notValid(color_d, i, color):
            if i in memo:
                return False
            
            color_d[i] = color
            
            for nei in graph[i]:
                if nei in color_d:
                    if color_d[nei] == color:
                        return True
                    continue
                else:
                    if notValid(color_d, nei, not color):
                        return True
            
            memo[i] = False
            del color_d[i]
            return False
        
        for i in range(n):
            if notValid({}, i, True):
                return False
        return True