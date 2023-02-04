class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        
        # presum
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + (1 if nums[i-1] == 1 else -1)
        
        # get ans
        counter = collections.Counter()
        ans = 0
        for val in presum:
            counter[val] += 1
            for k, v in counter.items():
                if k < val:
                    ans = (ans + v) % MOD
        return ans

