class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        queue = set()
        ans = 0
        fresh = 0
        
        # init
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.add((i, j))
                
                if grid[i][j] == 1:
                    fresh += 1
        
        # bfs
        while queue:
            tmp = set()
            while queue:
                i, j = queue.pop()
                
                for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                        continue
                    
                    fresh -= 1
                    grid[x][y] = 2
                    tmp.add((x, y))
            
            if not tmp:
                break
            
            ans += 1
            queue = tmp
            
        return ans if fresh == 0 else -1
