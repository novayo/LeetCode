class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def recr(i):
            if i >= len(nums):
                return {0:1}
            
            ret = collections.defaultdict(int)
            for k, v in recr(i+1).items():
                ret[k + nums[i]] += v
                ret[k - nums[i]] += v
            return ret
        
        return recr(0)[target]