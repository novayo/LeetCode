class UF:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.parents = {}
        self.ranks = {}
        
    def isValid(self):
        return self.start in self.parents and self.end in self.parents and self.find(self.start) == self.find(self.end)
    
    def add(self, n1):
        if n1 not in self.parents:
            self.parents[n1] = n1
            self.ranks[n1] = 0
    
    def find(self, n1):
        if self.parents[n1] != n1:
            self.parents[n1] = self.find(self.parents[n1])
        return self.parents[n1]
    
    def union(self, n1, n2):
        if n1 not in self.parents or n2 not in self.parents:
            return
        
        p1 = self.find(n1)
        p2 = self.find(n2)
        
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
    def swimInWater(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        graph = {}
        
        for i in range(height):
            for j in range(width):
                graph[grid[i][j]] = (i, j)
        
        
        tree = UF(grid[0][0], grid[-1][-1])
        for val in range(height*width):
            i, j = graph[val]
            tree.add(val)
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height and 0 <= y < width):
                    continue
                tree.union(val, grid[x][y])
            
            if tree.isValid():
                return val
        return -1