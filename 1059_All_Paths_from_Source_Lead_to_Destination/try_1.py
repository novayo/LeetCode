class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, des: int) -> bool:
        '''
        O(V+E) time comp / O(V+E) space comp
        - where E is number of the edges of the input graph.
        '''
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        # if destination has children.
        if len(graph[des]) > 0:
            return False
        
        memo = set()
        cache = set()
        
        def not_valid(node):
            if node == des:
                return False
            
            if len(graph[node]) == 0:
                return True
            
            for child in graph[node]:
                if child in memo:
                    continue
                    
                if child in cache:
                    return True
                
                cache.add(child)
                
                if not_valid(child):
                    return True
                
                memo.add(child)
                cache.remove(child)
            return False
        
        return not not_valid(source)
