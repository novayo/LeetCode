class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        
        # init
        found = set()
        queue = set()
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    queue.add((i, j))
                    found.add((i, j))
        
        layer = 1
        while queue:
            tmp = set()
            while queue:
                i, j = queue.pop()
                
                for x, y in [i+1, j], [i-1, j], [i, j+1], [i, j-1]:
                    if x < 0 or y < 0 or x >= height or y >= width or (x, y) in found:
                        continue
                    
                    mat[x][y] = layer
                    found.add((x, y))
                    tmp.add((x, y))
                
            layer += 1
            queue = tmp
        
        return mat
                
