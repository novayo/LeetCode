class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        周圍不是1，邊長+1
        '''
        
        def bfs(x, y, queue):
            ret = 0
            while queue:
                i, j = queue.popleft()
                
                if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0:
                    ret += 1
                elif grid[i][j] == 1:
                    grid[i][j] = 'x'
                    queue.append((i+1, j))
                    queue.append((i-1, j))
                    queue.append((i, j+1))
                    queue.append((i, j-1))
            return ret
        
        ans = 0
        queue = collections.deque()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    queue.append((x, y))
                    ans += bfs(x, y, queue)
        return ans