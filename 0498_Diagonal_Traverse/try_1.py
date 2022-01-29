class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def isValid(i, j):
            if i < 0 or j < 0 or i >= height or j >= width or (i, j) in found:
                return False
            return True
        
        direction = True
        
        height = len(mat)
        width = len(mat[0])
        
        ans = []
        
        # 1 th half
        found = set()
        i = j = 0
        while i < height:
            found.add((i, j))
            ans.append(mat[i][j])
            
            if i == height-1 and j == width-1:
                break
            
            if direction:
                next_i, next_j = i-1, j+1
            else:
                next_i, next_j = i+1, j-1
            
            if isValid(next_i, next_j):
                i, j = next_i, next_j
            else:
                if direction:
                    for x, y in [i-1, j], [i, j+1], [i+1, j], [i, j-1]:
                        if isValid(x, y):
                            i, j = x, y
                            direction = not direction
                            break
                else:
                    for x, y in [i+1, j], [i, j+1], [i-1, j], [i, j-1]:
                        if isValid(x, y):
                            i, j = x, y
                            direction = not direction
                            break
        return ans
