class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs 跑所有可能 => 每層代表的意思是 目前可以走的node
        # 要記錄已走過的值，走道重複的 且 此時的k比之前走過的小 => 就不用走這個組合了
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        found = {}
        stack = []
        stack.append((0, 0, k))
        while stack:
            tmp = []
            
            while stack:
                x, y, k = stack.pop()
                
                if (x, y) == (m-1, n-1):
                    return ans
                
                for i, j in [x-1, y], [x, y-1], [x, y+1], [x+1, y]:
                    
                    if i < 0 or j < 0 or i >= m or j >= n or ((i, j) in found and found[i, j] >= k) or (grid[i][j] == 1 and k <= 0):
                        continue
                    
                    if grid[i][j] == 1:
                        tmp.append((i, j, k-1))
                        found[i, j] = k-1
                    else:
                        tmp.append((i, j, k))
                        found[i, j] = k
                        
            stack = tmp
            ans += 1
        
        return -1