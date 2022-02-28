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
        
        
        def recr(index):
            if index >= n:
                return set([0])
            
            ret = recr(index+1)
            for val in ret.copy():
                ret.add(nums[index] + val)
            return ret
        
        return _sum in recr(0)
