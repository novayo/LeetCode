class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                
                mat1_i = i
                mat1_j = 0
                mat2_i = 0
                mat2_j = j
                
                while mat1_j < len(mat1[0]):
                    ans[i][j] += mat1[mat1_i][mat1_j] * mat2[mat2_i][mat2_j]
                    mat1_j, mat2_i = mat1_j+1, mat2_i+1
        
        return ans
                
