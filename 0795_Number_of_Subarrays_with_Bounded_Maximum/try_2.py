class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        
        i = 0
        last_valid_ans = 0
        for j, num in enumerate(nums):
            if num > right:
                i = j+1
                last_valid_ans = 0
                continue
            
            if num < left:
                ans += last_valid_ans
            else:
                last_valid_ans = j-i+1
                ans += last_valid_ans
        return ans
        