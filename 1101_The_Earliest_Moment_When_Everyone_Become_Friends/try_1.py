class UF:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.root = n
        
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        
        if p1 == p2:
            return
        
        self.root -= 1
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        
        tree = UF(n)
        for time, a, b in logs:
            tree.union(a, b)
            if tree.root == 1:
                return time
        return -1
        
