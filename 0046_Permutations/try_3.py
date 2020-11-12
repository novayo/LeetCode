class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        backtracking
        * 第i個與後面j個交換，交換後再recr(i+1)，之看這個組合的下一個交換
        '''
        
        def backtracking(startIndex, ans):
            if startIndex == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(startIndex, len(nums)):
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                backtracking(startIndex+1, ans)
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
            
        ans = []
        backtracking(0, ans)
        return ans
