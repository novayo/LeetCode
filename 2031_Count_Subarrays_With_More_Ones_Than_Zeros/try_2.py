class BIT:
    def __init__(self, end):
        self.end = end
        self.arr = collections.Counter()
        
    def update(self, i, delta=1):
        while i < self.end:
            self.arr[i] += delta
            i += i & -i
    
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.arr[i]
            i -= i & -i
        return ans

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        ans = 0
        
        # presum
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + (1 if nums[i-1] == 1 else -1)
        
        offset = -min(presum) + 1
        tree = BIT(max(presum) + offset)
        
        # get ans
        for val in presum:
            new_val = val + offset
            tree.update(new_val)
            ans = (ans + tree.query(new_val-1)) % MOD
        return ans

