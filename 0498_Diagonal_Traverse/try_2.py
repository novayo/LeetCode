class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        height = len(mat)
        width = len(mat[0])
        
        ans = []
        all_diags = []
        for j in range(width):
            all_diags.append([])
            x, y = 0, j
            while y >= 0 and x < height:
                all_diags[-1].append(mat[x][y])
                x, y = x+1, y-1
        
        for i in range(1, height):
            all_diags.append([])
            x, y = i, width-1
            while y >= 0 and x < height:
                all_diags[-1].append(mat[x][y])
                x, y = x+1, y-1
        
        for i in range(len(all_diags)):
            if i % 2 == 1:
                ans.extend(all_diags[i])
            else:
                ans.extend(all_diags[i][::-1])
        
        return ans
