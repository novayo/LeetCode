class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        def recr(i1, j1, i2, j2):
            if i1 > i2 or j1 > j2:
                return False
            
            if matrix[i1][j1] > target or matrix[i2][j2] < target:
                return False
            
            midJ = j1 + (j2 - j1) // 2
            
            # 找略大的值
            midI = i1
            while midI <= i2 and matrix[midI][midJ] <= target:
                if matrix[midI][midJ] == target:
                    return True
                midI += 1
            
            return recr(i1, midJ+1, midI-1, j2) or recr(midI, j1, i2, midJ-1)
        
        return recr(0, 0, len(matrix)-1, len(matrix[0])-1)
            
        