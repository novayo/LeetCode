class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs_level_order(i, j):
            que = collections.deque()
            
            que.appendleft((i, j))
            grid[i][j] = '0'
            
            while que:
                que2 = collections.deque()
                
                for i, j in que:
                    for _i, _j in [i+1,j], [i,j+1], [i-1,j], [i,j-1]:
                        if not (0 <= _i < height and 0 <= _j < width) or grid[_i][_j] == '0':
                            continue

                        grid[_i][_j] = '0'
                        que2.appendleft((_i, _j))
                
                que = que2
        
        height, width = len(grid), len(grid[0])
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    ans += 1
                    bfs_level_order(i, j)
        return ans

