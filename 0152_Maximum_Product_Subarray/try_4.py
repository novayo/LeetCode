class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -float('inf')
        
        cur_max = cur_min = 1
        for num in nums:
            tmp = cur_max
            cur_max = max(num, cur_max*num, cur_min*num)
            cur_min = min(num, tmp * num, cur_min*num)
            
            ans = max(ans, cur_max)
        return ans
    