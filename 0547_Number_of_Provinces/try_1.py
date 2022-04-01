class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.roots = 0
        
    def add(self, n1, n2):
        if n1 not in self.parent:
            self.parent[n1] = n1
            self.rank[n1] = 0
            self.roots += 1
        
        if n2 not in self.parent:
            self.parent[n2] = n2
            self.rank[n2] = 0
            self.roots += 1
        
    def findParent(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        self.add(n1, n2)
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
        if p1 == p2:
            return
        
        r1 = self.rank[p1]
        r2 = self.rank[p2]
        self.roots -= 1
        
        if r1 > r2:
            self.parent[p2] = p1
        elif r1 < r2:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        tree = UF()
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    tree.union(i, j)
        
        return tree.roots