class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def condition(guess_ans):
            cur_sum = cur_m = 0
            for num in nums:
                cur_sum += num
                if cur_sum > guess_ans:
                    cur_sum = num
                    cur_m += 1
            
            if cur_sum > 0:
                cur_m += 1
            
            return cur_m <= m
            
        ans = -1
        l, r = max(nums), sum(nums)
        while l <= r:
            mid = l + (r-l) // 2
            if condition(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
