class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # presum
        presum = [0]
        for i in range(len(nums)):
            presum.append(nums[i]+presum[i])
        
        # hash => key => presum value, value => list of index
        table = collections.defaultdict(list)
        for i in range(len(presum)):
            table[presum[i]].append(i)
        
        
        # find two sum of max length
        ans = 0
        for i in range(len(presum)):
            num = presum[i]
            target = num+k
            
            if num not in table or target not in table:
                continue
            
            lower_index = table[num][0]
            higher_index = table[target][-1]
            
            ans = max(ans, higher_index-lower_index)
        
        return ans
            
