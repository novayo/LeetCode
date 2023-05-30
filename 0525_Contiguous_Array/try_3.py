class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        visited_dict = {0: 0}
        ans = presum = 0
        for i, num in enumerate(nums):
            if num == 0:
                num = -1
            
            presum += num
            if presum in visited_dict:
                ans = max(ans, i - visited_dict[presum] + 1)
            else:
                visited_dict[presum] = i + 1
        
        return ans
        
