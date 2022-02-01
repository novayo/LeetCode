class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -float('inf')
        n = len(nums)
        cur_max = cur_min = 1
        
        for num in nums:
            tmp_max = cur_max
            cur_max = max(num, num*cur_max, num*cur_min)
            cur_min = min(num, num*tmp_max, num*cur_min)
            
            ans = max(ans, cur_max)
        
        return ans
