class UF:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    def _add(self, n):
        if n not in self.parents:
            self.parents[n] = n
            self.ranks[n] = 0
    
    def same_root(self, n1, n2):
        return self.findParent(n1) == self.findParent(n2)
    
    def findParent(self, n):
        self._add(n)
        if n != self.parents[n]:
            self.parents[n] = self.findParent(self.parents[n])
        return self.parents[n]
    
    def union(self, n1, n2):
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
        if p1 == p2:
            return
        
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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        tree = UF()
        
        for a, b in allowedSwaps:
            tree.union(a, b)
            
        bucket = {}
        for i in range(n):
            p = tree.findParent(i)
            
            if p not in bucket:
                bucket[p] = collections.Counter()
            bucket[p][source[i]] += 1
        
        ans = 0
        for i in range(n):
            p = tree.findParent(i)
            if bucket[p][target[i]] == 0:
                ans += 1
            else:
                bucket[p][target[i]] -= 1
        return ans
        
        