class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = {-1:0}
        found = collections.defaultdict(int)
        
        ans = count = 0
        for i in range(-1, len(nums)):
            count += nums[i]
            if count-k in found:
                ans += found[count-k]
            found[count] += 1
    
        return ans
