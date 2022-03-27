class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def recr(target):
            if target == 0:
                return 1
            
            if target not in memo:
                ret = 0
                for num in nums:
                    if target-num >= 0:
                        ret += recr(target-num)
                memo[target] = ret
            return memo[target]
        
        nums.sort()
        return recr(target)