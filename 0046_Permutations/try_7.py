class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def recr(start_index):
            nonlocal ans
            
            if start_index >= len(nums):
                ans.append(nums.copy())
                return
            
            for i in range(start_index, len(nums)):
                nums[start_index], nums[i] = nums[i], nums[start_index]
                recr(start_index+1)
                nums[start_index], nums[i] = nums[i], nums[start_index]
        
        recr(0)
        return ans
