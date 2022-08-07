class UF:
    def __init__(self, n):
        self.parents = {}
        self.ranks = {}
        self.roots = n
        
        for i in range(n):
            self.parents[i] = i
            self.ranks[i] = 0
    
    def find(self, n1):
        if n1 != self.parents[n1]:
            self.parents[n1] = self.find(self.parents[n1])
        return self.parents[n1]
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        tree = UF(n)
        logs.sort()
        
        for time, i, j in logs:
            tree.union(i, j)
            if tree.roots == 1:
                return time
        return -1
        
