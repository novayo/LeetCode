class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def findParent(self, n):
        if n not in self.parent:
            self.parent[n] = n
            self.rank[n] = 1
        
        if n != self.parent[n]:
            self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
        if p1 == p2:
            return
        
        r1 = self.rank[p1]
        r2 = self.rank[p2]
        
        if r1 > r2:
            self.parent[p2] = p1
        elif r1 < r2:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        tree = UF()
        for i, j in pairs:
            tree.union(i, j)
        
        groups = collections.defaultdict(list)
        for i in range(len(s)):
            groups[tree.findParent(i)].append(s[i])
        
        for k, lists in groups.items():
            lists.sort()
        
        ans = ''
        indices = {}
        for i in range(len(s)):
            p = tree.findParent(i)
            if p not in indices:
                indices[p] = 0
                
            ans += groups[p][indices[p]]
            indices[p] += 1
        return ans