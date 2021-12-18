class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        height = len(mat)
        width = len(mat[0])
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        diag = collections.defaultdict(int)
        a_diag = collections.defaultdict(int)
        
        ans = 0
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    diag[i-j] += 1
                    a_diag[i+j] += 1
                    ans = max(ans, rows[i], cols[j], diag[i-j], a_diag[i+j])
                else:
                    rows[i] = cols[j] = diag[i-j] = a_diag[i+j] = 0
        
        return ans