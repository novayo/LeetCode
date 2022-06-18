from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        '''
        => presum => O(mn)
        => loop through all possibility => 要跑長方形，所以得嘗試所有row*col => O(mn * mn)
        
        
        思考一下一維的 => 我要找的是 range maximum sum 
            => 邊掃加總，取答案，如果<0則=0
            => 先算presum, 掃過去之後紀錄最小值，然後目前值-最小值 O(nlogn) for No Larger Than K
        [1,2,4,0,7,5,3,2,0]
        
        dp => 要跑長方形，所以得嘗試所有row*col
        那我們就可以在去跑所有(row的組合) => 計算答案時使用一維的作法 => O(mn * mlogn)
        
        dp = [dp[row[j]] - dp[row[i]], ....]
        '''
        def kadane(presum):
            ans = -float('inf')
            lowest = float('inf')
            for val in presum:
                lowest = min(lowest, val)
                ans = max(ans, val - lowest)
            return ans
        
        def transpose(array):
            new_arr = [[0] * len(array) for _ in range(len(array[0]))]
            for i in range(len(array)):
                for j in range(len(array[0])):
                    new_arr[j][i] = array[i][j]
            return new_arr
        
        # O(nlogn) 
        def helper(dp):
            ans = -float('inf')
            
            kadane_sum = kadane(dp)
            if kadane_sum <= k:
                if kadane_sum == 300:
                    print(dp)
                return kadane_sum
            
            # 1-d array strategy
            tmp = SortedList()
            tmp.add(0)
            for val in dp[1:]:
                idx = tmp.bisect_left(val - k)
                if idx < len(tmp):
                    cur_k = val - tmp[idx]
                    
                    if cur_k <= k:
                        ans = max(ans, cur_k)
                tmp.add(val)
            return ans
        
        
        
        if len(matrix) > len(matrix[0]):
            matrix = transpose(matrix)
        
        height = len(matrix)
        width = len(matrix[0])
        
        # col presum
        for j in range(width):
            for i in range(1, height):
                matrix[i][j] += matrix[i-1][j]
        
        # all combinations of row
        ans = -float('inf')
        for i1 in range(height):
            for i2 in range(i1, height):
                # get rowi - rowj
                rows = []
                for j in range(width):
                    rows.append(matrix[i2][j] - (matrix[i1-1][j] if i1-1 >= 0 else 0))
                    
                # presum
                dp = [0]
                for row in rows:
                    dp.append(dp[-1] + row)
                    
                ans = max(ans, helper(dp))
                if ans == k:
                    return ans
        return ans
                
