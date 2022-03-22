class UF:
    def __init__(self, n):
        self.parents = {}
        self.ranks = {}
        self.roots = 0
        
        for i in range(n):
            self.parents[i] = i
            self.ranks[i] = 0
            self.roots += 1
    
    def findParent(self, n1):
        if n1 != self.parents[n1]:
            self.parents[n1] = self.findParent(self.parents[n1])
        return self.parents[n1]
    
    def union(self, n1, n2):
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
        if p1 == p2:
            return
        
        self.roots -= 1
        r1 = self.ranks[p1]
        r2 = self.ranks[p2]
        
        if r1 > r2:
            self.parents[p2] = p1
        elif r1 < r2:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.ranks[p1] += 1
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = UF(n)
        
        for a, b in edges:
            tree.union(a, b)
        
        return tree.roots
        