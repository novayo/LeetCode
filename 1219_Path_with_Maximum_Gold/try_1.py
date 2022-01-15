class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        '''
        dfs from every point and calculate local maximum
        '''
        height = len(grid)
        width = len(grid[0])
        
        
        def dfs(i, j, cur_gold, found, local_max):
            if cur_gold > local_max[0]:
                local_max[0] = cur_gold
            
            if i < 0 or j < 0 or i >= height or j >= width or (i, j) in found or grid[i][j] == 0:
                return
            
            found.add((i, j))
            sum_gold = cur_gold + grid[i][j]
            dfs(i+1, j, sum_gold, found, local_max)
            dfs(i-1, j, sum_gold, found, local_max)
            dfs(i, j+1, sum_gold, found, local_max)
            dfs(i, j-1, sum_gold, found, local_max)
            found.remove((i, j))
        
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] != 0:
                    local_max = [0]
                    dfs(i, j, 0, set(), local_max)
                    ans = max(ans, local_max[0])
        
        return ans
