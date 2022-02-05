class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        可以累加缺的上去 => 然後binary search k看在哪個區域，再看要+多少上去即可
        '''
        n = len(nums)
        presum = [0] * n
        
        for i in range(1, n):
            presum[i] = presum[i-1] + nums[i] - nums[i-1] - 1
        
        index = bisect.bisect_left(presum, k) - 1
        return nums[index] + k - presum[index]
