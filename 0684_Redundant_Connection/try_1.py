class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        disjoint set
        union()
        find root()
        '''
        
        parent = [-1] * 2000
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
        
            if root_x == root_y:
                return False
            else:
                parent[root_x-1] = root_y
                return True
        
        def find(x):
            while parent[x-1] != -1:
                x = parent[x-1]
            
            return x
        
        for x, y in edges:
            if union(x, y) == False:
                return [x, y]
