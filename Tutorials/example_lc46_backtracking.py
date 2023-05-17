class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        backtracking
        * 第i個與後面j個交換，交換後再recr(i+1)，之看這個組合的下一個交換
        '''
        ans = []
        def backtracking(i):
            nonlocal ans
            if i == len(nums):
                ans.append(nums.copy())
            
            for k in range(i, len(nums)):
                nums[i], nums[k] = nums[k], nums[i]
                backtracking(i+1)
                nums[i], nums[k] = nums[k], nums[i]
        
        backtracking(0)
        return ans
