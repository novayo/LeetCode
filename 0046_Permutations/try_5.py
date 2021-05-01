class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        
        def recr(startIndex):
            if startIndex == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(startIndex, length):
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                recr(startIndex+1)
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
        
        recr(0)
        return ans
