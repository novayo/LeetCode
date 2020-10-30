class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        def condition(index, height, width):
            x = index // width
            y = index % width
            
            if matrix[x][y] > target:
                return 1
            elif matrix[x][y] == target:
                return 0
            else:
                return -1
        
        if len(matrix) == 0:
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        
        left = 0
        right = height * width - 1
        while left <= right:
            mid = left + (right - left) // 2
            ret = condition(mid, height, width)
            
            if ret == 1:
                right = mid - 1
            elif ret == 0:
                return True
            else:
                left = mid + 1
        return False
