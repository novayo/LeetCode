class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        用union find找到第一個root相同的 => 最後一個邊出現cycle => 答案
        '''
        
        parent = {}
        
        def union(i, j):
            p1 = findParent(i)
            p2 = findParent(j)
            
            if p1 == p2:
                return False
            else:
                parent[p1] = p2
                return True
        
        def findParent(i):
            if i != parent[i]:
                parent[i] = findParent(parent[i])
            return parent[i]
        
        for i, j in edges:
            
            if i not in parent:
                parent[i] = i
            if j not in parent:
                parent[j] = j
            
            if not union(i, j):
                return i, j
        
