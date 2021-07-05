class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        om = len(mat)
        on = len(mat[0])
        
        if om*on != r*c:
            return mat
        
        tmp = []
        for m in mat:
            tmp += m
        
        ans = []
        for i in range(r):
            ans.append(tmp[0 + i*c:c+i*c])
        return ans
