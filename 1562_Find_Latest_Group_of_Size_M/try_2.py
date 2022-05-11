class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        dp = [0] * (n+2)
        
        if n == m:
            return m
        
        ans = -1
        for i, a in enumerate(arr):
            left_num = dp[a-1]
            right_num = dp[a+1]
            
            if left_num == m or right_num == m:
                ans = i
            
            dp[a-left_num] = dp[a+right_num] = left_num + right_num + 1
        return ans