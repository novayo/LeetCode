class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        divide-and-conquer
        用上下左右四個變數，代表目前的區域大小。
        1. 先用左右找中間（mid）
        2. 再用mid，找上下（binary search）
            * 若找到，則return
            * 若沒找到，則代表， 
                left = 0
                up = 0
                right = len(matrix[0])
                down = len(matrix)

                P 為 最接近target的略大的值 (binary search)
                P = (mid, y)
                |_____________________|
                |          x          |
                |   不需要  x   找     |
                |          x          |
                |xxxxxxxxxxPxxxxxxxxxx|
                |    找    x  不需要   |
                |_____________________|

                * 因為「左上」的都比 P 的小（左右比較）
                  右下都比 P 大（因為P下面的右邊都比P大）
                  因此只需要找右上跟左下
                * 每個區間都有最小值（左上）以及最大值（右下）
                  若target比左下小 或 target比右下大 => 則不用找
        '''
        if not matrix:
            return False
        
        def recr(left, up, right, down):
            if left > right or up > down:
                return False
            elif matrix[up][left] > target or matrix[down][right] < target:
                return False
            
            y_mid = left + (right - left) // 2
            
            next_row = up
            tmp_down = down
            while next_row <= tmp_down:
                x_mid = next_row + (tmp_down - next_row) // 2
                if matrix[x_mid][y_mid] < target:
                    next_row = x_mid + 1
                elif matrix[x_mid][y_mid] == target:
                    return True
                else:
                    tmp_down = x_mid - 1
            
            return recr(left, next_row, y_mid-1, down) or recr(y_mid+1, up, right, next_row-1)
        return recr(0, 0, len(matrix[0])-1, len(matrix)-1)
