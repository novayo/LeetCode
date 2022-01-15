class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # dp => 可以算橫的
        def count_row(array):
            ans = count = 0
            for a in array:
                if a == 0:
                    count = 0
                else:
                    count += 1
                ans += count
            return ans
        
        height = len(mat)
        width = len(mat[0])
        
        ans = 0
        # 直的 => 從每個高度
        for i in range(height):
            
            array = mat[i].copy()
            
            # 往下計算所有可能
            for _i in range(i, height):
                
                # 計算目前橫的
                for j in range(width):
                    array[j] &= mat[_i][j]
                ans += count_row(array)
        
        return ans
