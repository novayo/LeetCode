class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        width = len(mat[0 ])
        height = len(mat)
        
        ans = [[0 for i in range(width)] for i in range(height)]
        
        queue = collections.deque()
        found = set()
        
        # get start point => 0
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    found.add((i, j))
        
        # popleft
        while queue:
            x, y, level = queue.popleft()
            
            ans[x][y] = level
            
            for i, j in [x-1, y], [x+1, y], [x, y-1], [x, y+1]:
                if i < 0 or j < 0 or i>=height or j >= width or (i, j) in found:
                    continue
                queue.append((i, j, level+1))
                found.add((i, j))
                
        return ans
