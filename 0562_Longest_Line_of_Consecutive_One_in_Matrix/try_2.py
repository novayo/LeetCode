class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        height, width = len(mat), len(mat[0])
        rows = [0] * height
        cols = [0] * width
        diag = collections.Counter()
        anti_diag = collections.Counter()
        
        ans = 0
        
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    rows[i] = cols[j] = diag[i-j] = anti_diag[i+j] = 0
                    continue
                
                rows[i] += 1
                cols[j] += 1
                diag[i-j] += 1
                anti_diag[i+j] += 1
                
                ans = max(ans, rows[i], cols[j], diag[i-j], anti_diag[i+j])
        
        return ans
