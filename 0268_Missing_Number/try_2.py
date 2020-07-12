class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        算出總和後相減即可
        '''
        n = len(nums)
        return n*(n+1) // 2 - sum(nums)
