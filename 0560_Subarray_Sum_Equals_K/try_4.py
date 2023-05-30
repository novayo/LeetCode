class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        visit_dict = collections.Counter()
        
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        ans = 0
        for i in range(len(presum)):
            ans += visit_dict[presum[i] - k]
            visit_dict[presum[i]] += 1

        return ans    
        
