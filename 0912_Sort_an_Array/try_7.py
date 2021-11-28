class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bucke sort
        MAX_LENGTH = 50000
        buckets = [0] * (2*MAX_LENGTH+1)
        
        for num in nums:
            buckets[MAX_LENGTH + num] += 1
        
        ans = []
        for i in range(-MAX_LENGTH, MAX_LENGTH+1):
            ans.extend([i] * buckets[MAX_LENGTH + i])
        
        return ans
