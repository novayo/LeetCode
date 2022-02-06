class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        sliding window
        '''
        n = len(nums)
        
        # sliding window
        ans = float('inf')
        i = j = cur_sum = 0
        
        while j < n:
            cur_sum += nums[j]
            
            while i <= j and cur_sum >= target:
                ans = min(ans, j-i+1)
                cur_sum -= nums[i]
                i += 1
            
            j += 1
        
        return ans if ans < float('inf') else 0
