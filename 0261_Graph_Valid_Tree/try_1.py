class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        # check forest
        # recr check if cycle
        visited = set()
        
        cache = set()
        def isCycle(parent_node, current_node):
            
            visited.add(current_node)
            
            for child in graph[current_node]:
                if child == parent_node:
                    continue
                
                # find cycle
                if child in cache:
                    return True
                
                cache.add(child)
                if isCycle(current_node, child):
                    return True
                cache.remove(child)
            
            return False
        
        ret = isCycle(None, 0)
        return not ret and n == len(visited)
        
    
        
        
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
