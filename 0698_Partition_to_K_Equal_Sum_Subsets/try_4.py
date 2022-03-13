class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        
        s = s // k
        
        nums.sort()
        if nums[-1] > s:
            return False
        while nums and nums[-1] == s:
            nums.pop()
            k -= 1
        
        
        
        n = len(nums)
        memo = {}
        def helper(cur_sum, cur_k, bitmask):
            if cur_sum > s:
                return False
            
            if cur_k == k:
                return True
            
            if bitmask not in memo:
                for i in range(n):
                    if bitmask & (1<<i) != 0:
                        continue

                    if cur_sum + nums[i] == s:
                        if helper(0, cur_k+1, bitmask | (1<<i)):
                            return True
                    else:
                        if helper(cur_sum + nums[i], cur_k, bitmask | (1<<i)):
                            return True
                memo[bitmask] = False
            return memo[bitmask]
        
        return helper(0, 0, 0)