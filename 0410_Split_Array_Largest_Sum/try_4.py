class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def condition(guess):
            cur_m = cur_sum = 0
            for num in nums:
                cur_sum += num
                if cur_sum > guess:
                    cur_m += 1
                    cur_sum = num
            
            return cur_m < m
        
        l, r = max(nums), sum(nums)
        ans = 0
        while l <= r:
            mid = l + (r-l) // 2
            valid = condition(mid)
            if valid:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans