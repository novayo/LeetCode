class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSum = [0]
        for i in range(len(nums)):
            preSum.append(preSum[-1] + nums[i])
        
        sorted_preSum = sorted(preSum)
        
        ans = 0
        for target in preSum:
            del sorted_preSum[bisect.bisect_left(sorted_preSum, target)] # 把自己刪掉，不要找尋到自己
            ans += bisect.bisect_right(sorted_preSum, target+upper) - bisect.bisect_left(sorted_preSum, target+lower)
        return ans
