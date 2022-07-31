class UF:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    def checkAnswer(self, n1, n2):
        if n1 not in self.parents or n2 not in self.parents:
            return False
        return self.find(n1) == self.find(n2)
    
    def add(self, n1):
        if n1 not in self.parents:
            self.parents[n1] = n1
            self.ranks[n1] = 0
    
    def find(self, n1):
        if n1 != self.parents[n1]:
            self.parents[n1] = self.find(self.parents[n1])
        return self.parents[n1]
    
    def union(self, n1, n2):
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
        '''
        # O(mn + ans * log(ans)) time / O(mn) space
        tree = UF()
        d = {time: (x, y)} => build d
        
        cur_time = 0
        must loop max(grid[0][0], grid[-1][-1]) times
            => i, j = d[cur_time]
            => add grid[i][j] to tree
                => add four direction
            => cur_time += 1
        
        while check if root of (0, 0) == root of (m-1, n-1):
            => i, j = d[cur_time]
            => add grid[i][j] to tree
            => cur_time += 1
            
        return cur time
        '''
        height, width = len(grid), len(grid[0])
        tree = UF()
        graph = {}
        
        # init
        for i in range(height):
            for j in range(width):
                graph[grid[i][j]] = (i, j)
        
        # get answer
        for t in range(height * width):
            i, j = graph[t]
            
            tree.add(grid[i][j])
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height and 0 <= y < width) or grid[i][j] < grid[x][y]:
                    continue
                tree.union(grid[i][j], grid[x][y])
            
            if tree.checkAnswer(grid[0][0], grid[-1][-1]):
                return t
        
        return -1
