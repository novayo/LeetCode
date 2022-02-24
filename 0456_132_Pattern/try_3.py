class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        dp[i] => i左邊的最小值是誰
        monotonic stack => 找到遞增（從尾到頭）
        '''
        n = len(nums)
        dp = [float('inf')] * n
        
        # dp[i] => i左邊的最小值是誰
        cur_min = float('inf')
        for i, num in enumerate(nums):
            dp[i] = cur_min
            cur_min = min(cur_min, num)
            
        
        
        # monotonic stack
        right_stack = [-float('inf')]
        for i in range(n-1, -1, -1):
            left = dp[i]
            mid = nums[i]
            right = right_stack[-1]
            
            while mid > right:
                if left < right:
                    return True
                right_stack.pop()
                if not right_stack:
                    break
                right = right_stack[-1]
            right_stack.append(mid)
        
        return False
