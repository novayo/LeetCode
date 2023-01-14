class Tree:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        self.totals = 0
    
    def findParent(self, e):
        if e != self.parents[e]:
            self.parents[e] = self.findParent(self.parents[e])
        return self.parents[e]
    
    def add(self, e):
        if e not in self.parents:
            self.parents[e] = e
            self.ranks[e] = 0
            self.totals += 1
    
    def union(self, e1, e2):
        if e1 not in self.parents or e2 not in self.parents:
            return
        
        p1 = self.findParent(e1)
        p2 = self.findParent(e2)
        
        if p1 == p2:
            return
        
        self.totals -= 1
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
    def numIslands(self, grid: List[List[str]]) -> int:
        UF = Tree()
        height, width = len(grid), len(grid[0])
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    UF.add((i, j))
                    
                    for _i, _j in [i+1,j], [i-1,j], [i,j+1], [i,j-1]:
                        UF.union((i,j), (_i,_j))
        
        return UF.totals

