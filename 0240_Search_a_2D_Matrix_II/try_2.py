class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bisect_right(l, r, y):
            while l <= r:
                mid_x = l + (r-l)//2
                
                if matrix[mid_x][y] == target:
                    return mid_x
                elif matrix[mid_x][y] < target:
                    l = mid_x+1
                else:
                    r = mid_x-1
            return l
        
        def recr(x1, y1, x2, y2):
            if x1 > x2 or y1 > y2:
                return False
            
            if matrix[x1][y1] > target or matrix[x2][y2] < target:
                return False
            
            mid_y = y1 + (y2-y1) // 2
            mid_x = bisect_right(x1, x2, mid_y) # x => bisect_right (找略大於target的值)
            
            if mid_x < len(matrix) and matrix[mid_x][mid_y] == target:
                return True
            
            return recr(x1, mid_y+1, mid_x-1, y2) \
                   or recr(mid_x, y1, x2, mid_y-1)
        
        return recr(0, 0, len(matrix)-1, len(matrix[0])-1)
