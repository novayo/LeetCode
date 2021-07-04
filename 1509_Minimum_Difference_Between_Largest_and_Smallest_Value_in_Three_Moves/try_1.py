class Solution:
    def minDifference(self, nums: List[int]) -> int:
        ''' 差距大的會在最左邊最右邊，因此變更左右邊3個即可
        '''
        
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        return min(nums[-1] - nums[3],
                   nums[-2] - nums[2],
                   nums[-3] - nums[1],
                   nums[-4] - nums[0])
