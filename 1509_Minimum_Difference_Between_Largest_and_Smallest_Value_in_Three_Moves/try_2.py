class Solution:
    def minDifference(self, nums: List[int]) -> int:
        '''
       	針對前三個最大&最小 去刪除找最小差
	'''
        
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        ans = float('inf')
        
        i, j = 3, len(nums)-1
        while i >= 0:
            ans = min(ans, nums[j]-nums[i])
            i -= 1
            j -= 1
        
        return ans

