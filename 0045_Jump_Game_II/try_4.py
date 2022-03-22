class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = j = farest = 0
        for i, num in enumerate(nums[:-1]):
            farest = max(farest, i+num)
            
            if i == j:
                ans += 1
                j = farest
        
        return ans        