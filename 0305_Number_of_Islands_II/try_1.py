class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.roots = 0
    
    def add(self, n):
        if n not in self.parent:
            self.parent[n] = n
            self.rank[n] = 1
            self.roots += 1
    
    def findParent(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        if n1 not in self.parent or n2 not in self.parent:
            return
        
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
        if p1 == p2:
            return
        
        self.roots -= 1
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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        tree = UF()
        
        ans = []
        for i, j in positions:
            tree.add((i, j))
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < m or 0 <= y < n or (x, y) in node):
                    continue
                
                tree.union((i, j), (x, y))
            ans.append(tree.roots)
        return ans