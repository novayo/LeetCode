class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, tmp = [], 1
        for value in nums:
            ans.append(tmp)
            tmp *= value
        
        tmp = 1
        for index, value in enumerate(nums[::-1]):
            ans[-1-index] *= tmp
            tmp *= value
        
        return ans
