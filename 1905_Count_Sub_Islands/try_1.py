class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # bfs
        
        def bfs(i, j):
            q = collections.deque()
            
            ret = True
            found = set()
            q.appendleft((i, j))
            while q:
                x, y = q.pop()
                
                if x < 0 or x >= len(grid1) or y < 0 or y >= len(grid1[0]) or (x, y) in found or grid2[x][y] != 1:
                    continue
                
                if grid1[x][y] != 1:
                    ret = False
                
                found.add((x, y))
                grid2[x][y] = 0
                q.appendleft((x+1, y))
                q.appendleft((x-1, y))
                q.appendleft((x, y+1))
                q.appendleft((x, y-1))
            
            return ret
        
        ans = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    ans += int(bfs(i, j))
        return ans
                
