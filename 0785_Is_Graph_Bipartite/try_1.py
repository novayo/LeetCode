class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        走走看會不會走到重複的顏色即可
        '''
        
        colored = collections.defaultdict(bool)
        
        def notBipartite(node):
            for child in graph[node]:
                if child not in colored:
                    colored[child] = not colored[node]
                    if notBipartite(child):
                        return True
                elif colored[node] == colored[child]:
                    return True
            return False
            
        for node in range(len(graph)):
            if node not in colored:
                colored[node] = False
                if notBipartite(node):
                    return False
        return True
