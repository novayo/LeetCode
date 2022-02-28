class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        找看看能不能加起來 = 一半
        '''
        n = len(nums)
        _sum = sum(nums)
        
        if _sum % 2 == 1:
            return False
        else:
            _sum //= 2
        
        
        dp = set([0])
        for index in range(n-1, -1, -1):
            if _sum in dp:
                return True
            for val in dp.copy():
                dp.add(nums[index]+val)
        return False
