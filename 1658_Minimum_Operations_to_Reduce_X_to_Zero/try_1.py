class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        sum => find sum-x and max subarray
        '''
        n = len(nums)
        s = sum(nums)
        target = s-x
        
        # max subarray
        cur_sum = i = 0
        max_length = -1
        for j in range(n):
            cur_sum += nums[j]
            
            while i <= j and cur_sum > target:
                cur_sum -= nums[i]
                i += 1
            
            if cur_sum == target:
                max_length = max(max_length, j-i+1)
        
        return n - max_length if max_length > -1 else -1