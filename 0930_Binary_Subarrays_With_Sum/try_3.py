class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''
        arr =      [0,0,0,1,0,0,0,0,1,0,1]
        presum = [0,0,0,0,1,1,1,1,1,2,2,3]
        
        goal = 1
        
        arr =      [1,0,1,0,1]
        presum = [0,1,1,2,2,3]
        goal = 2
        ans += 0 + 0 + 0 + 1 + 1 + 2 = 4
        {0: 1, 1: 2, 2: 2}
        
        arr =      [0,0,0,0,0]
        presum = [0,0,0,0,0,0]
        goal = 0
        ans += 0 + 1 + 2 +3+4+5 = 15
        {0: 3}
        '''
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        ans = 0
        counter = collections.Counter()
        for num in presum:
            ans += counter[num - goal]
            counter[num] += 1
        return ans
        
