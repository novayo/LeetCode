class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        n = len(nums)
        
        ans = 0
        j = cur_far = 0
        for i in range(n-1):
            cur_far = max(cur_far, i + nums[i])
            
            if cur_far >= n-1:
                break
            
            if i == j:
                ans += 1
                j = cur_far
            
        return ans + 1
