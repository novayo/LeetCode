class BIT:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.parent = {}
        self.size = {}
        
        for i in range(self.n):
            for j in range(self.n):
                self.parent[i, j] = (i, j)
                self.size[i, j] = 1
    
    def getScoreByPos(self, pos):
        x, y = pos
        
        parent_set = set()
        for i, j in [x-1, y], [x, y-1], [x+1, y], [x, y+1]:
            if i < 0 or j < 0 or i >= self.n or j >= self.n or self.grid[i][j] != 1:
                continue
            parent_set.add(self.findParent((i, j)))
        
        _sum = 0
        while parent_set:
            _pos = parent_set.pop()
            _sum += self.size[_pos]
        
        return _sum
    
    def findParent(self, pos):
        if pos != self.parent[pos]:
            self.parent[pos] = self.findParent(self.parent[pos])
        return self.parent[pos]
    
    def union(self, pos1, pos2):
        p1 = self.findParent(pos1)
        p2 = self.findParent(pos2)
        
        if p1 == p2:
            return
        
        s1 = self.size[p1]
        s2 = self.size[p2]
        
        if s1 >= s2:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
            

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tree = BIT(grid)
        
        # union all 1
        for j in range(1, n):
            if grid[0][j-1] == 1 and grid[0][j] == 1:
                tree.union((0, j-1), (0, j))
        for i in range(1, n):
            if grid[i-1][0] == 1 and grid[i][0] == 1:
                tree.union((i-1, 0), (i, 0))
        for i in range(1, n):
            for j in range(1, n):
                if grid[i][j] == 1:
                    if grid[i-1][j] == 1:
                        tree.union((i, j), (i-1, j))
                    if grid[i][j-1] == 1:
                        tree.union((i, j), (i, j-1))
        
        # find answer
        ans = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    ans = max(ans, tree.getScoreByPos((x, y))+1)
        return ans if ans != 0 else n*n
        