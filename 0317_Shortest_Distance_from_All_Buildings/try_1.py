class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # start from house
        height, width = len(grid), len(grid[0])
        dp = [[0] * width for _ in range(height)]
        ans = float('inf')
        target = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    ans = float('inf')
                    que = set([(i, j)])
                    layer = 1
                    while que:
                        next_que = set()
                        for _i, _j in que:
                            for x, y in [_i-1, _j], [_i+1, _j], [_i, _j-1], [_i, _j+1]:
                                if not (0 <= x < height and 0 <= y < width) or grid[x][y] != target:
                                    continue
                                
                                grid[x][y] -= 1
                                dp[x][y] += layer
                                ans = min(ans, dp[x][y])
                                next_que.add((x, y))
                        que = next_que
                        layer += 1
                    target -= 1
        return ans if ans < float('inf') else -1
