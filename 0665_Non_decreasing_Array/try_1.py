class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        '''
        Input: nums = [3,4,2,5]
        Output: true
        
        # monotonic stack => 遞曾
        [2,2, 1,    2,3]
        stack = [1,2]
        
        [3,2,1]
        stack = [3,2,1]
        
        counter = 1
        [2,1,4,2,3]
        stack = []
        '''
        # [3,2,3,inf] float('inf')
        # [1,4,2,3]
        # [1,4,4,4] => 4
        # [3,4,5,5] => 2
        # [3,4,2,3] => 
        count = 0
        n = len(nums)
        nums.append(float('inf'))
        for i in range(n-1, 0, -1):
            pre, cur, after = nums[i-1], nums[i], nums[i+1]
            
            if pre > cur:
                count += 1
                if count > 1:
                    break
                if pre <= after:
                    nums[i] = after
                else:
                    nums[i-1] = cur
        return count < 2
            